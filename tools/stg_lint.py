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

WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß0-9_:+/.-]*|\d+(?:[.,]\d+)?", re.UNICODE)
URL_RE = re.compile(r"https?://\S+|www\.\S+", re.I)
CODE_RE = re.compile(r"`[^`]*`")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])(?:[\"'»”)]*)\s+(?=[A-ZÄÖÜ0-9„\"'([])")
MAN_RE = re.compile(r"(?<![\wÄÖÜäöüß])man(?![\wÄÖÜäöüß])", re.I)
AMBIGUOUS_SLASH_PATTERNS = (
    re.compile(r"(?<![\w])und\s*/\s*oder(?![\w])", re.I),
    re.compile(r"(?<![\w])oder\s*/\s*und(?![\w])", re.I),
    re.compile(r"(?<![\w])(der|die|das)\s*/\s*(der|die|das)(?![\w])", re.I),
    re.compile(r"(?<![\w])(ein|eine|einen|einem|einer)\s*/\s*(eine?|einen|einem|einer)(?![\w])", re.I),
    re.compile(r"(?<![\w])ein-\s*/\s*ausschalten(?![\w])", re.I),
)


@dataclass
class Finding:
    severity: str
    rule: str
    message: str
    original: str
    suggestion: str | None = None
    term: str | None = None


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def mask_protected(text: str) -> str:
    text = URL_RE.sub(" PROTECTED_URL ", text)
    text = CODE_RE.sub(" PROTECTED_CODE ", text)
    return text


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text.strip())
    if not text:
        return []
    return [p.strip() for p in SENTENCE_SPLIT_RE.split(text) if p.strip()]


def split_paragraphs(text: str) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if stripped.startswith("#") or re.match(r"^(?:[-*+] |\d+[.)] )", stripped):
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


def audit_text(text: str, root: Path, text_type: str = "auto", project: dict | None = None,
               lexicon_report: bool = False, profile: str | None = None) -> dict:
    project = project or {}
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
    masked = mask_protected(text)

    for line in text.splitlines():
        if ";" in line and not line.lstrip().startswith("#"):
            findings.append(Finding("error", "STG-8.1", "Semikolon verwenden Sie nicht. Teilen Sie den Satz.", line.strip(), "Schreiben Sie zwei getrennte Sätze."))

    for sentence in split_sentences(masked):
        if MAN_RE.search(sentence):
            findings.append(Finding("error", "STG-DE-4.3", "`man` bezeichnet den Akteur nicht eindeutig.", sentence, "Nennen Sie den Akteur oder verwenden Sie eine direkte Anweisung.", "man"))

    for line in masked.splitlines():
        if line.lstrip().startswith("#"):
            continue
        for pattern in AMBIGUOUS_SLASH_PATTERNS:
            match = pattern.search(line)
            if match:
                findings.append(Finding("warning", "STG-DE-8.1", "Die Schrägstrichkombination kann mehrdeutig sein.", match.group(0), "Verwenden Sie `und`, `oder`, eine Liste oder getrennte Sätze.", match.group(0)))

    for entry in prohibited:
        term = str(entry.get("term", "")).strip()
        if not term or not phrase_regex(term).search(masked):
            continue
        status = entry.get("status", "review_required")
        severity = "error" if status == "prohibited" else "review"
        alternatives = entry.get("approved_alternatives") or []
        suggestion = entry.get("rewrite")
        if alternatives:
            suggestion = (suggestion + " " if suggestion else "") + "Bevorzugt: " + ", ".join(map(str, alternatives)) + "."
        findings.append(Finding(severity, "STG-1.1", str(entry.get("reason") or f"{term} erfordert Prüfung."), term, suggestion, term))

    lowered = masked.casefold()
    for avoided, preferred in avoid_project.items():
        if phrase_regex(avoided).search(lowered):
            findings.append(Finding("error", "STG-9.4", "Projektterminologie ist nicht konsistent.", avoided, f"Verwenden Sie `{preferred}`.", avoided))

    for sentence in split_sentences(text):
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
            if not low or low in {"protected_url", "protected_code"} or low in allowed_core or low in allowed_project:
                continue
            unknown_counts[low] = unknown_counts.get(low, 0) + 1

    counts = {"error": 0, "warning": 0, "review": 0}
    for finding in findings:
        counts[finding.severity] = counts.get(finding.severity, 0) + 1
    result = "FAIL" if counts["error"] else ("PASS WITH REVIEW" if counts["review"] or counts["warning"] else "PASS")
    return {
        "tool": "stg_lint.py",
        "standard": "STG-DE 0.4.0",
        "profile": profile,
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


def render_text(result: dict) -> str:
    label = f"STG-DE audit ({result['profile']})" if result.get("profile") else "STG-DE audit"
    lines = [f"{label}: {result['result']}", ""]
    if not result["findings"]:
        lines.append("Keine deterministischen Befunde.")
    else:
        for i, f in enumerate(result["findings"], 1):
            lines.append(f"{i}. [{f['severity'].upper()}] {f['rule']}: {f['message']}")
            lines.append(f"   Original: {f['original']}")
            if f.get("suggestion"):
                lines.append(f"   Vorschlag: {f['suggestion']}")
    if result.get("unknown_lexicon"):
        lines += ["", "Unbekannte Lexikoneinträge (Review, keine automatischen Fehler):"]
        for term, count in result["unknown_lexicon"][:50]:
            lines.append(f"- {term}: {count}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic STG-DE linter")
    ap.add_argument("input", help="UTF-8 text/Markdown file or - for stdin")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parents[1]), help="STG-DE repository/skill reference root")
    ap.add_argument("--project", help="Optional .stg-de.yaml project terminology")
    ap.add_argument("--profile", help="Application profile: procedure, safety, description, requirement, support, consumer, agent")
    ap.add_argument("--text-type", choices=["auto", "procedure", "description"], default="auto", help="Legacy structural override; profile base type is used when auto")
    ap.add_argument("--format", choices=["text", "json"], default="text")
    ap.add_argument("--lexicon-report", action="store_true")
    ap.add_argument("--fail-on-error", action="store_true", help="Exit 1 when deterministic errors exist")
    args = ap.parse_args()

    root = Path(args.root)
    text = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
    project = load_yaml(Path(args.project)) if args.project else {}
    try:
        result = audit_text(text, root, args.text_type, project, args.lexicon_report, args.profile)
    except ValueError as exc:
        ap.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == "json" else render_text(result))
    return 1 if args.fail_on_error and result["counts"].get("error", 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())
