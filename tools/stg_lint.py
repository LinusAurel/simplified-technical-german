#!/usr/bin/env python3
"""Deterministic STG-DE lint checks.

This linter intentionally checks only conditions that can be detected with acceptable
reliability without a full German parser. It complements, but does not replace, semantic
review against the STG-DE rules.
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
    parts = SENTENCE_SPLIT_RE.split(text)
    return [p.strip() for p in parts if p.strip()]


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
    # Explicit noun plurals are controlled forms unless they collide with a canonical lemma.
    for e in entries:
        if e.get("part_of_speech") == "noun" and e.get("plural"):
            p = str(e["plural"]).casefold()
            if p not in canonical:
                out.add(p)
    return out


def audit_text(text: str, root: Path, text_type: str = "auto", project: dict | None = None,
               lexicon_report: bool = False) -> dict:
    project = project or {}
    if (root / "dictionary" / "approved-words.yaml").exists():
        approved_path = root / "dictionary" / "approved-words.yaml"
        prohibited_path = root / "dictionary" / "prohibited-words.yaml"
    else:
        approved_path = root / "references" / "approved-words.yaml"
        prohibited_path = root / "references" / "prohibited-words.yaml"
    approved_data = load_yaml(approved_path)
    prohibited_data = load_yaml(prohibited_path)
    approved = approved_data.get("entries", [])
    prohibited = prohibited_data.get("entries", [])
    allowed_project, avoid_project = project_terms(project)
    allowed_core = approved_surfaces(approved)

    findings: list[Finding] = []
    masked = mask_protected(text)

    # STG-8.1: semicolons must not join statements.
    for line in text.splitlines():
        if ";" in line and not line.lstrip().startswith("#"):
            findings.append(Finding(
                "error", "STG-8.1", "Semikolon verwenden Sie nicht. Teilen Sie den Satz.",
                line.strip(), "Schreiben Sie zwei getrennte Sätze."
            ))

    # STG-1.1: controlled/prohibited vocabulary.
    for entry in prohibited:
        term = str(entry.get("term", "")).strip()
        if not term:
            continue
        rx = phrase_regex(term)
        if not rx.search(masked):
            continue
        status = entry.get("status", "review_required")
        severity = "error" if status == "prohibited" else "review"
        alternatives = entry.get("approved_alternatives") or []
        suggestion = entry.get("rewrite")
        if alternatives:
            suggestion = (suggestion + " " if suggestion else "") + "Bevorzugt: " + ", ".join(map(str, alternatives)) + "."
        findings.append(Finding(
            severity, "STG-1.1", str(entry.get("reason") or f"{term} erfordert Prüfung."),
            term, suggestion, term
        ))

    # STG-9.4: project preferred terminology.
    lowered = masked.casefold()
    for avoided, preferred in avoid_project.items():
        if phrase_regex(avoided).search(lowered):
            findings.append(Finding(
                "error", "STG-9.4", "Projektterminologie ist nicht konsistent.",
                avoided, f"Verwenden Sie `{preferred}`.", avoided
            ))

    # STG-5.1 / STG-6.3: sentence length.
    cap = 20 if text_type == "procedure" else 25
    for sentence in split_sentences(text):
        n = count_words(sentence)
        if n > cap:
            rule = "STG-5.1" if text_type == "procedure" else "STG-6.3"
            findings.append(Finding(
                "error", rule, f"Der Satz hat {n} Wörter. Zulässig sind höchstens {cap} Wörter in diesem Prüfmodus.",
                sentence, "Teilen Sie den Satz, ohne Bedingungen oder technische Bedeutung zu entfernen."
            ))

    # Optional lexical routing report. Unknown words are review items, never automatic violations.
    unknown_counts: dict[str, int] = {}
    if lexicon_report:
        tokens = [t for t in WORD_RE.findall(masked) if not t.isdigit()]
        for tok in tokens:
            low = tok.casefold().strip(".-")
            if not low or low in {"protected_url", "protected_code"}:
                continue
            if low in allowed_core or low in allowed_project:
                continue
            unknown_counts[low] = unknown_counts.get(low, 0) + 1

    counts = {"error": 0, "warning": 0, "review": 0}
    for f in findings:
        counts[f.severity] = counts.get(f.severity, 0) + 1
    result = "FAIL" if counts.get("error", 0) else ("PASS WITH REVIEW" if counts.get("review", 0) or counts.get("warning", 0) else "PASS")
    return {
        "tool": "stg_lint.py",
        "standard": "STG-DE 0.4.0",
        "text_type": text_type,
        "result": result,
        "counts": counts,
        "findings": [asdict(f) for f in findings],
        "unknown_lexicon": sorted(unknown_counts.items(), key=lambda x: (-x[1], x[0])) if lexicon_report else [],
        "limitations": [
            "Deterministic checks do not prove full STG-DE conformance.",
            "Unknown words are review candidates, not automatic errors.",
            "Semantic ambiguity, passive voice, pronoun reference, and instruction structure still require contextual review."
        ],
    }


def render_text(result: dict) -> str:
    lines = [f"STG-DE audit: {result['result']}", ""]
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
    ap.add_argument("--text-type", choices=["auto", "procedure", "description"], default="auto")
    ap.add_argument("--format", choices=["text", "json"], default="text")
    ap.add_argument("--lexicon-report", action="store_true")
    ap.add_argument("--fail-on-error", action="store_true", help="Exit 1 when deterministic errors exist")
    args = ap.parse_args()

    root = Path(args.root)
    if args.input == "-":
        text = sys.stdin.read()
    else:
        text = Path(args.input).read_text(encoding="utf-8")
    project = load_yaml(Path(args.project)) if args.project else {}
    result = audit_text(text, root, args.text_type, project, args.lexicon_report)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result))
    return 1 if args.fail_on_error and result["counts"].get("error", 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())
