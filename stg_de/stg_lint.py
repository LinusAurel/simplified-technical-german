#!/usr/bin/env python3
"""Deterministic STG-DE lint checks.

The linter checks conditions that can be detected with acceptable reliability without
claiming that deterministic checks prove full STG-DE conformance.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from stg_markdown import LIST_ITEM_RE, prose_blocks, split_sentences, strip_markdown_code  # noqa: E402

STG_VERSION = "0.4.0"
TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".rst", ".adoc"}
SEVERITY_RANK = {"review": 1, "warning": 2, "error": 3}

WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß0-9_:+/.-]*|\d+(?:[.,]\d+)?", re.UNICODE)
URL_RE = re.compile(r"https?://\S+|www\.\S+", re.I)
CODE_RE = re.compile(r"`[^`]*`")
# Quoted text (UI labels, citations, mentioned words) is protected and counts as one word (STG-8.6).
QUOTE_RE = re.compile(r"„[^“”\n]{1,120}[“”]|»[^«\n]{1,120}«|\"[^\"\n]{1,120}\"")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])(?:[\"'»”)]*)\s+(?=[A-ZÄÖÜ0-9„\"'([])")
MAN_RE = re.compile(r"(?<![\wÄÖÜäöüß])man(?![\wÄÖÜäöüß])", re.I)
AMBIGUOUS_SLASH_PATTERNS = (
    re.compile(r"(?<![\w])und\s*/\s*oder(?![\w])", re.I),
    re.compile(r"(?<![\w])oder\s*/\s*und(?![\w])", re.I),
    re.compile(r"(?<![\w])(der|die|das)\s*/\s*(der|die|das)(?![\w])", re.I),
    re.compile(r"(?<![\w])(ein|eine|einen|einem|einer)\s*/\s*(eine?|einen|einem|einer)(?![\w])", re.I),
    re.compile(r"(?<![\w])ein-\s*/\s*ausschalten(?![\w])", re.I),
)


ADDRESS_FORMS = ("sie", "du", "infinitiv")
# Formal address: capitalized "Sie"/"Ihnen"/"Ihr…" after the first word of a sentence, or a
# sentence-initial formal imperative ("Prüfen Sie …"). Lowercase "sie" is third person.
FORMAL_RE = re.compile(r"(?<=[^\s.!?:]\s)(?:Sie|Ihnen|Ihre?[mnrs]?)\b|^[A-ZÄÖÜ][a-zäöüß]+(?:en|ern|eln)\s+Sie\b")
INFORMAL_RE = re.compile(r"(?<![\wÄÖÜäöüß])(?:[Dd]u|[Dd]ich|[Dd]ir|[Dd]ein(?:e|em|en|er|es)?|[Ee]uch|[Ee]uer|[Ee]ure[mnrs]?)(?![\wÄÖÜäöüß])")
ADDRESS_LABEL = {"sie": "formale Anrede mit „Sie“", "du": "Anrede mit „du“"}


@dataclass
class Finding:
    severity: str
    rule: str
    message: str
    original: str
    suggestion: str | None = None
    term: str | None = None
    line: int | None = None
    occurrences: int | None = None


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def mask_protected(text: str) -> str:
    text = URL_RE.sub(" PROTECTED_URL ", text)
    text = CODE_RE.sub(" PROTECTED_CODE ", text)
    text = QUOTE_RE.sub(" PROTECTED_QUOTE ", text)
    return text


def prose_sentences(text: str) -> list[str]:
    return [s for block in prose_blocks(text) for s in split_sentences(block)]


def split_paragraphs(text: str) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []
    for line in strip_markdown_code(text).splitlines():
        stripped = line.strip()
        if not stripped:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if stripped.startswith(("#", "|", ">")) or LIST_ITEM_RE.match(stripped):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        current.append(stripped)
    if current:
        paragraphs.append(" ".join(current))
    return paragraphs


def count_words(sentence: str) -> int:
    return len(WORD_RE.findall(mask_protected(sentence)))


def phrase_regex(term: str) -> re.Pattern[str]:
    escaped = re.escape(term).replace(r"\ ", r"\s+")
    return re.compile(rf"(?<![\wÄÖÜäöüß]){escaped}(?![\wÄÖÜäöüß])", re.I)


def project_terms(project: dict) -> tuple[set[str], dict[str, str]]:
    allowed: set[str] = set()
    avoid_to_preferred: dict[str, str] = {}
    for key in ("technical_nouns", "technical_verbs"):
        for item in project.get(key, []) or []:
            if isinstance(item, str):
                allowed.add(item.casefold())
            elif isinstance(item, dict) and item.get("term"):
                allowed.add(str(item["term"]).casefold())
    for item in project.get("protected_terms", []) or []:
        if isinstance(item, str):
            allowed.add(item.casefold())
    for item in project.get("preferred_terms", []) or []:
        if not isinstance(item, dict) or not item.get("preferred"):
            continue
        preferred = str(item["preferred"])
        allowed.add(preferred.casefold())
        for avoided in item.get("avoid", []) or []:
            avoid_to_preferred[str(avoided).casefold()] = preferred
    return allowed, avoid_to_preferred


def approved_surfaces(entries: list[dict]) -> set[str]:
    out: set[str] = set()
    canonical: set[str] = set()
    for e in entries:
        lemma = str(e.get("lemma", "")).strip()
        if lemma:
            canonical.add(lemma.casefold())
            out.add(lemma.casefold())
        for s in e.get("surface_forms", []) or []:
            if s:
                out.add(str(s).casefold())
    for e in entries:
        if e.get("part_of_speech") == "noun" and e.get("plural"):
            plural = str(e["plural"]).casefold()
            if plural not in canonical:
                out.add(plural)
    return out


def load_profiles(root: Path) -> dict[str, dict]:
    candidates = [root / "profiles" / "profiles.yaml", root / "references" / "profiles.yaml"]
    for path in candidates:
        if path.exists():
            return (load_yaml(path).get("profiles") or {})
    return {}


def resolve_profile(root: Path, profile: str | None, text_type: str) -> tuple[str, int, dict | None]:
    if not profile:
        effective_type = "procedure" if text_type == "procedure" else "description"
        return effective_type, 20 if effective_type == "procedure" else 25, None
    profiles = load_profiles(root)
    if profile not in profiles:
        available = ", ".join(sorted(profiles)) or "none"
        raise ValueError(f"Unknown STG-DE profile `{profile}`. Available profiles: {available}")
    config = profiles[profile]
    effective_type = text_type if text_type != "auto" else str(config["base_text_type"])
    limit = int(config.get("sentence_word_limit", 20 if effective_type == "procedure" else 25))
    return effective_type, limit, config


def address_findings(sentences: list[str], declared: str | None) -> list[Finding]:
    """STG-5.3: one form of address per document set."""
    hits: dict[str, list[str]] = {"sie": [], "du": []}
    for sentence in sentences:
        if FORMAL_RE.search(sentence):
            hits["sie"].append(sentence)
        if INFORMAL_RE.search(sentence):
            hits["du"].append(sentence)
    if declared:
        out = []
        for form, found in hits.items():
            if form == declared:
                continue
            for sentence in found:
                out.append(Finding("error", "STG-5.3",
                                   f"Das Projekt legt die Anrede `{declared}` fest. Der Satz verwendet die {ADDRESS_LABEL[form]}.",
                                   sentence, "Verwenden Sie die festgelegte Anredeform."))
        return out
    if hits["sie"] and hits["du"]:
        minority = "du" if len(hits["du"]) <= len(hits["sie"]) else "sie"
        return [Finding("warning", "STG-5.3",
                        "Das Dokument mischt die formale Anrede mit „Sie“ und die Anrede mit „du“.",
                        hits[minority][0], "Legen Sie eine Anredeform fest (`anrede` in `.stg-de.yaml`) und verwenden Sie nur diese.")]
    return []


def resolve_address(project: dict, address: str | None) -> str | None:
    value = address or project.get("anrede") or project.get("address")
    if value is None:
        return None
    value = str(value).casefold()
    if value not in ADDRESS_FORMS:
        raise ValueError(f"unknown form of address: {value} (expected sie, du or infinitiv)")
    return value


def audit_text(text: str, root: Path, text_type: str = "auto", project: dict | None = None,
               lexicon_report: bool = False, profile: str | None = None, address: str | None = None) -> dict:
    project = project or {}
    declared_address = resolve_address(project, address)
    if (root / "dictionary" / "approved-words.yaml").exists():
        approved_path = root / "dictionary" / "approved-words.yaml"
        prohibited_path = root / "dictionary" / "prohibited-words.yaml"
    else:
        approved_path = root / "references" / "approved-words.yaml"
        prohibited_path = root / "references" / "prohibited-words.yaml"
    approved = load_yaml(approved_path).get("entries", [])
    prohibited = load_yaml(prohibited_path).get("entries", [])
    allowed_project, avoid_project = project_terms(project)
    allowed_core = approved_surfaces(approved)
    effective_type, sentence_limit, profile_config = resolve_profile(root, profile, text_type)

    findings: list[Finding] = []
    prose = strip_markdown_code(text)
    masked = mask_protected(prose)

    for line in prose.splitlines():
        if ";" in mask_protected(line) and not line.lstrip().startswith("#"):
            findings.append(Finding("error", "STG-8.1", "Semikolon verwenden Sie nicht. Teilen Sie den Satz.", line.strip(), "Schreiben Sie zwei getrennte Sätze."))

    for sentence in prose_sentences(masked):
        if MAN_RE.search(sentence):
            findings.append(Finding("error", "STG-DE-4.3", "`man` bezeichnet den Akteur nicht eindeutig.", sentence, "Nennen Sie den Akteur oder verwenden Sie eine direkte Anweisung.", "man"))

    findings += address_findings(prose_sentences(masked), declared_address)

    for line in masked.splitlines():
        if line.lstrip().startswith("#"):
            continue
        for pattern in AMBIGUOUS_SLASH_PATTERNS:
            match = pattern.search(line)
            if match:
                findings.append(Finding("warning", "STG-DE-8.1", "Die Schrägstrichkombination kann mehrdeutig sein.", match.group(0), "Verwenden Sie `und`, `oder`, eine Liste oder getrennte Sätze.", match.group(0)))

    # Terms with a dedicated structural check are reported once, by that check.
    # Project terminology (technical nouns/verbs, protected and preferred terms) takes
    # precedence over the central prohibited list (STG-1.6, STG-1.8).
    dedicated_terms = {f.term.casefold() for f in findings if f.term} | allowed_project
    masked_sentences = prose_sentences(masked)
    for entry in prohibited:
        term = str(entry.get("term", "")).strip()
        if not term or term.casefold() in dedicated_terms:
            continue
        forms = [term] + [str(f) for f in entry.get("surface_forms", []) or []]
        patterns = [phrase_regex(f) for f in forms]
        hits = [s for s in masked_sentences if any(p.search(s) for p in patterns)]
        if not hits:
            continue
        status = entry.get("status", "review_required")
        severity = "error" if status == "prohibited" else "review"
        alternatives = entry.get("approved_alternatives") or []
        suggestion = entry.get("rewrite")
        if alternatives:
            suggestion = (suggestion + " " if suggestion else "") + "Bevorzugt: " + ", ".join(map(str, alternatives)) + "."
        # One finding per term; `original` is the first sentence with the term, so the reader
        # can judge the use in context. `occurrences` counts all sentences with the term.
        findings.append(Finding(severity, "STG-1.1", str(entry.get("reason") or f"{term} erfordert Prüfung."),
                                hits[0], suggestion, term, occurrences=len(hits)))

    lowered = masked.casefold()
    for avoided, preferred in avoid_project.items():
        if phrase_regex(avoided).search(lowered):
            findings.append(Finding("error", "STG-9.4", "Projektterminologie ist nicht konsistent.", avoided, f"Verwenden Sie `{preferred}`.", avoided))

    for sentence in prose_sentences(prose):
        n = count_words(sentence)
        if n > sentence_limit:
            rule = "STG-5.1" if effective_type == "procedure" else "STG-6.3"
            findings.append(Finding("error", rule, f"Der Satz hat {n} Wörter. Das Profil erlaubt höchstens {sentence_limit} Wörter.", sentence, "Teilen Sie den Satz, ohne Bedingungen oder technische Bedeutung zu entfernen."))

    if effective_type == "description":
        for paragraph in split_paragraphs(text):
            sentences = split_sentences(paragraph)
            if len(sentences) > 6:
                findings.append(Finding("error", "STG-6.6", f"Der Absatz hat {len(sentences)} Sätze. Zulässig sind höchstens 6 Sätze.", paragraph, "Teilen Sie den Absatz nach Thema oder logischem Zusammenhang."))

    unknown_counts: dict[str, int] = {}
    if lexicon_report:
        for token in WORD_RE.findall(masked):
            if token.isdigit():
                continue
            low = token.casefold().strip(".-")
            if not low or low in {"protected_url", "protected_code", "protected_quote"} or low in allowed_core or low in allowed_project:
                continue
            unknown_counts[low] = unknown_counts.get(low, 0) + 1

    for finding in findings:
        finding.line = locate_line(text, finding.original)

    counts = {"error": 0, "warning": 0, "review": 0}
    for finding in findings:
        counts[finding.severity] = counts.get(finding.severity, 0) + 1
    result = "FAIL" if counts["error"] else ("PASS WITH REVIEW" if counts["review"] or counts["warning"] else "PASS")
    return {
        "tool": "stg_lint.py",
        "standard": f"STG-DE {STG_VERSION}",
        "profile": profile,
        "address": declared_address,
        "profile_priorities": (profile_config or {}).get("priorities", []),
        "text_type": effective_type,
        "sentence_word_limit": sentence_limit,
        "result": result,
        "counts": counts,
        "findings": [asdict(f) for f in findings],
        "unknown_lexicon": sorted(unknown_counts.items(), key=lambda x: (-x[1], x[0])) if lexicon_report else [],
        "limitations": [
            "Deterministic checks do not prove full STG-DE conformance.",
            "Application profiles change applicability/priorities, not controlled word meanings.",
            "Unknown words are review candidates, not automatic errors.",
            "Semantic ambiguity, passive voice, pronoun reference, modality, and instruction structure still require contextual review."
        ],
    }


def locate_line(text: str, original: str) -> int | None:
    """Return the 1-based line where a finding starts, also for sentences that wrap lines."""
    words = []
    for word in (original or "").split():
        if "PROTECTED_" in word:
            break
        words.append(word)
        if len(words) == 8:
            break
    if not words:
        return None
    pattern = r"[\s>*+-]*".join(re.escape(w) for w in words)
    if len(words) == 1:
        pattern = r"(?<![\wÄÖÜäöüß])" + pattern + r"(?![\wÄÖÜäöüß])"
    m = re.search(pattern, text) or re.search(pattern, text, re.I)
    return text.count("\n", 0, m.start()) + 1 if m else None


def render_text(result: dict) -> str:
    label = f"STG-DE audit ({result['profile']})" if result.get("profile") else "STG-DE audit"
    lines = [f"{label}: {result['result']}", ""]
    if not result["findings"]:
        lines.append("Keine deterministischen Befunde.")
    else:
        for i, f in enumerate(result["findings"], 1):
            where = f" (Zeile {f['line']})" if f.get("line") else ""
            term = f" `{f['term']}`" if f.get("term") and f["rule"] == "STG-1.1" else ""
            count = f" ({f['occurrences']}×)" if (f.get("occurrences") or 0) > 1 else ""
            lines.append(f"{i}. [{f['severity'].upper()}] {f['rule']}{where}{term}{count}: {f['message']}")
            lines.append(f"   Original: {f['original']}")
            if f.get("suggestion"):
                lines.append(f"   Vorschlag: {f['suggestion']}")
    if result.get("unknown_lexicon"):
        lines += ["", "Unbekannte Lexikoneinträge (Review, keine automatischen Fehler):"]
        for term, count in result["unknown_lexicon"][:50]:
            lines.append(f"- {term}: {count}")
    return "\n".join(lines)


def collect_inputs(inputs: list[str]) -> list[str]:
    """Expand directories to text/Markdown files; keep files and '-' as given."""
    paths: list[str] = []
    for item in inputs:
        p = Path(item)
        if item != "-" and p.is_dir():
            paths += sorted(str(f) for f in p.rglob("*") if f.is_file() and f.suffix.lower() in TEXT_SUFFIXES
                            and not any(part.startswith(".") for part in f.relative_to(p).parts))
        else:
            paths.append(item)
    return paths


def overall_result(results: list[dict]) -> str:
    states = {r["result"] for r in results}
    if "FAIL" in states:
        return "FAIL"
    return "PASS WITH REVIEW" if "PASS WITH REVIEW" in states else "PASS"


def render_github(path: str, result: dict) -> str:
    level = {"error": "error", "warning": "warning", "review": "notice"}
    out = []
    for f in result["findings"]:
        loc = f"file={path}" + (f",line={f['line']}" if f.get("line") else "")
        msg = f"{f['message']} Vorschlag: {f['suggestion']}" if f.get("suggestion") else f["message"]
        msg = msg.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        out.append(f"::{level.get(f['severity'], 'notice')} {loc},title={f['rule']}::{msg}")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic STG-DE linter")
    ap.add_argument("inputs", nargs="+", metavar="input", help="UTF-8 text/Markdown files, directories, or - for stdin")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parents[1]), help="STG-DE repository/skill reference root")
    ap.add_argument("--project", help="Project terminology file (default: ./.stg-de.yaml when present)")
    ap.add_argument("--no-project", action="store_true", help="Do not load ./.stg-de.yaml automatically")
    ap.add_argument("--profile", help="Application profile: procedure, safety, description, requirement, support, consumer, agent")
    ap.add_argument("--anrede", "--address", dest="address", choices=list(ADDRESS_FORMS),
                    help="Form of address for instructions (default: `anrede` in .stg-de.yaml; otherwise only mixing is reported)")
    ap.add_argument("--text-type", choices=["auto", "procedure", "description"], default="auto", help="Legacy structural override; profile base type is used when auto")
    ap.add_argument("--format", choices=["text", "json", "github"], default="text")
    ap.add_argument("--lexicon-report", action="store_true")
    ap.add_argument("--fail-on", choices=["error", "warning", "review", "never"], default="never",
                    help="Exit 1 when a finding of this severity or higher exists")
    ap.add_argument("--fail-on-error", action="store_true", help="Alias for --fail-on error")
    args = ap.parse_args()

    root = Path(args.root)
    project_path = args.project
    if not project_path and not args.no_project and Path(".stg-de.yaml").is_file():
        project_path = ".stg-de.yaml"
    project = load_yaml(Path(project_path)) if project_path else {}
    threshold = "error" if args.fail_on_error else args.fail_on

    paths = collect_inputs(args.inputs)
    if not paths:
        ap.error("no text or Markdown files found")
    results = []
    for path in paths:
        try:
            text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            ap.error(f"{path}: {exc}")
        try:
            result = audit_text(text, root, args.text_type, project, args.lexicon_report, args.profile, args.address)
        except ValueError as exc:
            ap.error(str(exc))
        result["path"] = "<stdin>" if path == "-" else path
        results.append(result)

    if args.format == "json":
        if len(results) == 1:
            print(json.dumps(results[0], ensure_ascii=False, indent=2))
        else:
            print(json.dumps({"tool": "stg_lint.py", "standard": f"STG-DE {STG_VERSION}", "result": overall_result(results),
                              "files": results}, ensure_ascii=False, indent=2))
    elif args.format == "github":
        text_out = "\n".join(filter(None, (render_github(r["path"], r) for r in results)))
        if text_out:
            print(text_out)
        print(f"STG-DE: {overall_result(results)} ({len(results)} Datei(en))")
    else:
        blocks = []
        for r in results:
            block = render_text(r)
            blocks.append(f"== {r['path']}\n{block}" if len(results) > 1 else block)
        if len(results) > 1:
            blocks.append(f"Gesamtergebnis: {overall_result(results)} ({len(results)} Dateien)")
        print("\n\n".join(blocks))

    if threshold == "never":
        return 0
    limit = SEVERITY_RANK[threshold]
    worst = max((SEVERITY_RANK.get(f["severity"], 0) for r in results for f in r["findings"]), default=0)
    return 1 if worst >= limit else 0


if __name__ == "__main__":
    raise SystemExit(main())
