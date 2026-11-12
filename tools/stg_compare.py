#!/usr/bin/env python3
"""Deterministic meaning-preservation check for STG-DE rewrites.

Compares a source text with its rewrite. The check cannot prove that meaning is
preserved. It detects content that a rewrite must not lose or change silently:

- protected content (numbers, units, identifiers, code, URLs, quoted UI text,
  safety signal words): a loss is a FAIL;
- modality, negation, conditions, and limits: a change is REVIEW evidence.

A PASS means only that none of these signals changed.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

STG_VERSION = "0.5.0"

NUMBER_WORDS = {
    "null": "0", "eins": "1", "zwei": "2", "drei": "3", "vier": "4", "fünf": "5", "sechs": "6",
    "sieben": "7", "acht": "8", "neun": "9", "zehn": "10", "elf": "11", "zwölf": "12",
}
# "ein/eine" are articles in most contexts and are therefore not normalized.
UNIT_RE = (r"(?:%|‰|°C|°F|°|mm|cm|dm|km|m²|m³|m|µm|nm|mg|kg|g|t|ml|l|L|bar|mbar|Pa|kPa|MPa|psi|"
           r"Nm|N|kN|V|mV|kV|A|mA|W|kW|MW|Wh|kWh|Hz|kHz|MHz|GHz|Ω|ms|s|min|h|d|U/min|rpm|dB|"
           r"Byte|KB|MB|GB|TB|kB|KiB|MiB|GiB|Bit|Mbit/s|Gbit/s|px|Sekunden?|Minuten?|Stunden?|Tagen?|Tage|"
           r"Wochen?|Monaten?|Monate|Jahren?|Jahre|Prozent|Grad|Volt|Ampere|Watt|Meter|Millimeter|Zentimeter|"
           r"Kilogramm|Gramm|Liter|Milliliter)")
NUMBER_RE = re.compile(r"(?<![\w.,])(?<![A-Za-zÄÖÜäöüß]-)(\d+(?:[.,]\d+)*)(?:\s*(" + UNIT_RE + r"))?(?![\wÄÖÜäöüß])")
CODE_RE = re.compile(r"`[^`\n]+`")
URL_RE = re.compile(r"https?://[^\s)>\]]+|www\.[^\s)>\]]+", re.I)
QUOTE_RE = re.compile(r"„([^“”\n]{1,80})[“”]|\"([^\"\n]{1,80})\"|»([^«\n]{1,80})«")
# Acronyms and alphanumeric identifiers such as API, DUT, X-200, M8, ISO 3864.
IDENT_RE = re.compile(r"(?<![\w-])(?:[A-ZÄÖÜ]{2,}[A-Z0-9ÄÖÜ]*(?:-[A-Z0-9]+)*|[A-Z]+\d+[A-Z0-9]*|[A-Z][a-z]*-\d+[A-Za-z0-9]*)(?![\w-])")
SIGNAL_WORDS = ("GEFAHR", "WARNUNG", "VORSICHT", "ACHTUNG", "HINWEIS")
WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß]+")

MODALITY = {
    "requirement": {"muss", "müssen", "musst", "müsst", "erforderlich", "notwendig", "verpflichtend", "zwingend", "pflicht"},
    "permission": {"darf", "dürfen", "zulässig", "erlaubt"},
    "possibility": {"kann", "können", "möglich", "optional", "wahlweise"},
    "recommendation": {"sollte", "sollten", "empfehlen", "empfohlen", "empfiehlt", "empfehlung", "ratsam"},
    "ambiguous": {"soll", "sollen", "müsste", "müssten", "könnte", "könnten"},
}
NEGATORS = {"nicht", "kein", "keine", "keinen", "keinem", "keiner", "keines", "nie", "niemals", "nichts", "ohne", "weder"}
# Words within one group are interchangeable for this check ("falls" -> "wenn" is fine).
CONDITIONS = {"wenn", "falls", "sofern", "sobald", "solange", "bevor", "nachdem"}
RESTRICTIONS = {"außer", "ausgenommen", "nur", "ausschließlich", "lediglich"}
LIMITS = {"mindestens", "höchstens", "maximal", "minimal", "max", "min", "spätestens", "frühestens", "genau", "exakt", "ca", "circa", "etwa", "ungefähr"}
LIST_MARKER_RE = re.compile(r"^(\s*)\d+[.)](?=\s)", re.M)
NEGATIVE_IMPERATIVE_RE = re.compile(r"(?:^|[.!?:]\s+|\n\s*(?:\d+[.)]\s*|[-*]\s*)?)[A-ZÄÖÜ][a-zäöüß]+(?:en|ern|eln)\s+Sie\b[^.!?\n]*?\b(?:nicht|nie|niemals|kein\w*)\b")
PROHIBITION_RE = re.compile(r"\b(?:darf|dürfen)\b[^.!?]*?\b(?:nicht|kein\w*|nie|niemals)\b|\b(?:nicht|nie|niemals)\b[^.!?]*?\b(?:darf|dürfen)\b|\bverboten\b|\bunzulässig\b", re.I)


@dataclass
class Finding:
    check: str
    severity: str  # "fail" or "review"
    message: str
    source: list[str]
    rewrite: list[str]
    rule: str | None = None


def normalize_number(raw: str) -> str:
    value = raw.replace(" ", "")
    # Treat "2,5" and "2.5" as the same decimal; keep thousands groups intact as digits.
    if re.fullmatch(r"\d{1,3}(?:\.\d{3})+", value):
        value = value.replace(".", "")
    return value.replace(",", ".")


def normalize_unit(unit: str | None) -> str:
    if not unit:
        return ""
    aliases = {"prozent": "%", "grad": "°", "sekunde": "s", "sekunden": "s", "minute": "min", "minuten": "min",
               "stunde": "h", "stunden": "h", "volt": "V", "ampere": "A", "watt": "W", "meter": "m",
               "millimeter": "mm", "zentimeter": "cm", "kilogramm": "kg", "gramm": "g", "liter": "l",
               "milliliter": "ml", "rpm": "U/min", "L": "l"}
    return aliases.get(unit.casefold(), aliases.get(unit, unit))


def strip_protected(text: str) -> str:
    return URL_RE.sub(" ", CODE_RE.sub(" ", text))


def numbers(text: str) -> Counter:
    # Step numbering identifies a work step and is not content (STG-8.6).
    plain = LIST_MARKER_RE.sub(r"\1", strip_protected(text))
    for word, digit in NUMBER_WORDS.items():
        plain = re.sub(rf"(?<![\wÄÖÜäöüß]){word}(?![\wÄÖÜäöüß])", digit, plain, flags=re.I)
    found = Counter()
    for m in NUMBER_RE.finditer(plain):
        found[(normalize_number(m.group(1)), normalize_unit(m.group(2)))] += 1
    return found


def words(text: str) -> list[str]:
    return [w.casefold() for w in WORD_RE.findall(strip_protected(text))]


def count_set(tokens: list[str], vocabulary: set[str]) -> Counter:
    return Counter(t for t in tokens if t in vocabulary)


def imperative_count(text: str) -> int:
    # Formal imperative: sentence-initial finite verb followed by "Sie" ("Prüfen Sie ...").
    return len(re.findall(r"(?:^|[.!?:]\s+|\n\s*(?:\d+\.\s*|[-*]\s*)?)[A-ZÄÖÜ][a-zäöüß]+(?:en|ern|eln)\s+Sie\b", text))


def missing(source: Counter, rewrite: Counter) -> list:
    return sorted((source - rewrite).elements(), key=str)


def compare(source: str, rewrite: str) -> dict:
    findings: list[Finding] = []

    # Protected content: exact preservation required.
    src_num, new_num = numbers(source), numbers(rewrite)
    src_values = Counter(v for v, _ in src_num.elements())
    new_values = Counter(v for v, _ in new_num.elements())
    lost_values = missing(src_values, new_values)
    if lost_values:
        findings.append(Finding("numbers", "fail", "Zahlen aus dem Original fehlen in der Umschreibung.",
                                lost_values, [], "STG-8.6"))
    added_values = missing(new_values, src_values)
    if added_values:
        findings.append(Finding("numbers", "review", "Die Umschreibung enthält Zahlen, die im Original fehlen. Prüfen Sie, ob Information erfunden wurde.",
                                [], added_values))
    for value in sorted(set(src_values) & set(new_values)):
        src_units = {u for v, u in src_num if v == value}
        new_units = {u for v, u in new_num if v == value}
        if src_units != new_units and src_units - {""}:
            findings.append(Finding("units", "fail", f"Die Einheit zum Wert {value} hat sich geändert.",
                                    sorted(src_units), sorted(new_units), "STG-8.6"))

    for check, pattern, label in (
        ("code", CODE_RE, "Code oder Kennungen in Backticks fehlen."),
        ("urls", URL_RE, "URLs fehlen."),
    ):
        lost = missing(Counter(pattern.findall(source)), Counter(pattern.findall(rewrite)))
        if lost:
            findings.append(Finding(check, "fail", label, lost, []))

    src_quotes = Counter(next(g for g in m.groups() if g) for m in QUOTE_RE.finditer(source))
    new_quotes = Counter(next(g for g in m.groups() if g) for m in QUOTE_RE.finditer(rewrite))
    lost_quotes = [q for q in missing(src_quotes, new_quotes) if q not in rewrite]
    if lost_quotes:
        findings.append(Finding("quoted_text", "fail", "Zitierter Text (z. B. UI-Beschriftungen) fehlt oder wurde verändert.",
                                lost_quotes, []))

    src_ids = Counter(IDENT_RE.findall(strip_protected(source)))
    new_ids = Counter(IDENT_RE.findall(strip_protected(rewrite)))
    lost_ids = [i for i in missing(src_ids, new_ids) if i not in SIGNAL_WORDS and i not in rewrite]
    if lost_ids:
        findings.append(Finding("identifiers", "fail", "Kennungen, Abkürzungen oder Produktnamen fehlen.",
                                lost_ids, [], "STG-1.8"))

    lost_signals = [s for s in SIGNAL_WORDS if source.count(s) > rewrite.count(s)]
    if lost_signals:
        findings.append(Finding("safety_signal", "fail", "Ein Signalwort für einen Sicherheitshinweis fehlt.",
                                lost_signals, [], "STG-7.1"))

    # Review evidence: meaning-bearing function words.
    src_words, new_words = words(source), words(rewrite)
    src_mod = {k: sum(count_set(src_words, v).values()) for k, v in MODALITY.items()}
    new_mod = {k: sum(count_set(new_words, v).values()) for k, v in MODALITY.items()}
    src_imp, new_imp = imperative_count(source), imperative_count(rewrite)
    def prohibitions(text: str) -> int:
        return len(PROHIBITION_RE.findall(text)) + len(NEGATIVE_IMPERATIVE_RE.findall(text))

    def modal_prohibitions(text: str) -> int:
        return len(PROHIBITION_RE.findall(text))

    src_prohib, new_prohib = prohibitions(source), prohibitions(rewrite)
    # "darf nicht" is a prohibition, not a permission.
    src_mod["permission"] = max(0, src_mod["permission"] - modal_prohibitions(source))
    new_mod["permission"] = max(0, new_mod["permission"] - modal_prohibitions(rewrite))

    if src_prohib > new_prohib:
        findings.append(Finding("prohibition", "review", "Ein Verbot (z. B. 'darf nicht') ist in der Umschreibung seltener. Prüfen Sie, ob es erhalten ist.",
                                [str(src_prohib)], [str(new_prohib)], "STG-DE-3.2"))
    # Requirements may legitimately become formal imperatives.
    if src_mod["requirement"] > new_mod["requirement"] + max(0, new_imp - src_imp):
        findings.append(Finding("modality", "review", "Pflichtangaben (muss, erforderlich) sind seltener und nicht durch Imperative ersetzt.",
                                [str(src_mod["requirement"])], [str(new_mod["requirement"])], "STG-DE-3.2"))
    for weak in ("possibility", "recommendation", "permission"):
        if src_mod[weak] > new_mod[weak] and (new_mod["requirement"] > src_mod["requirement"] or new_imp > src_imp):
            findings.append(Finding("modality", "review",
                                    f"Modalität '{weak}' ist seltener, Pflicht oder Imperativ häufiger. Prüfen Sie, ob Möglichkeit oder Empfehlung zur Pflicht wurde.",
                                    [str(src_mod[weak])], [str(new_mod[weak])], "STG-DE-3.2"))
    if src_mod["requirement"] > new_mod["requirement"] and new_mod["recommendation"] + new_mod["possibility"] > src_mod["recommendation"] + src_mod["possibility"]:
        findings.append(Finding("modality", "review", "Eine Pflicht wurde möglicherweise zu Empfehlung oder Möglichkeit abgeschwächt.",
                                [str(src_mod["requirement"])], [str(new_mod["requirement"])], "STG-DE-3.2"))

    for check, vocabulary, message, rule in (
        ("negation", NEGATORS, "Verneinungen sind seltener. Prüfen Sie, ob eine Verneinung verloren ging oder ihr Bereich sich änderte.", "STG-DE-4.4"),
        ("conditions", CONDITIONS, "Bedingungen (wenn, falls, bevor) sind seltener.", "STG-5.4"),
        ("restrictions", RESTRICTIONS, "Einschränkungen (nur, außer, ausschließlich) sind seltener.", "STG-DE-4.4"),
        ("limits", LIMITS, "Grenz- oder Näherungsangaben (mindestens, höchstens, ca.) sind seltener.", "STG-DE-9.2"),
    ):
        src_c, new_c = count_set(src_words, vocabulary), count_set(new_words, vocabulary)
        # Compare the group total. Word forms within a group are interchangeable.
        if sum(src_c.values()) > sum(new_c.values()):
            findings.append(Finding(check, "review", message, missing(src_c, new_c), missing(new_c, src_c), rule))

    counts = Counter(f.severity for f in findings)
    result = "FAIL" if counts["fail"] else ("REVIEW" if counts["review"] else "PASS")
    return {
        "tool": "stg_compare.py",
        "standard": f"STG-DE {STG_VERSION}",
        "result": result,
        "counts": {"fail": counts["fail"], "review": counts["review"]},
        "findings": [asdict(f) for f in findings],
        "limitations": [
            "PASS means that protected content and modality/negation/condition signals are unchanged; it does not prove equal meaning.",
            "Counts are document-level. A moved negation or condition can keep its count and still change scope.",
            "Review findings require a human or model to compare the affected sentences.",
        ],
    }


def render(result: dict) -> str:
    lines = [f"STG-DE Bedeutungsprüfung: {result['result']}", ""]
    if not result["findings"]:
        lines.append("Keine Abweichungen bei geschützten Inhalten, Modalität, Verneinung, Bedingungen und Grenzwerten.")
    for i, f in enumerate(result["findings"], 1):
        rule = f" ({f['rule']})" if f.get("rule") else ""
        lines.append(f"{i}. [{f['severity'].upper()}] {f['check']}{rule}: {f['message']}")
        if f["source"]:
            lines.append(f"   Original: {', '.join(map(str, f['source']))}")
        if f["rewrite"]:
            lines.append(f"   Umschreibung: {', '.join(map(str, f['rewrite']))}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Compare a source text with its STG-DE rewrite for lost or changed meaning signals")
    ap.add_argument("source", help="Original UTF-8 text file")
    ap.add_argument("rewrite", help="Rewritten UTF-8 text file, or - for stdin")
    ap.add_argument("--format", choices=["text", "json"], default="text")
    ap.add_argument("--fail-on", choices=["fail", "review", "never"], default="never",
                    help="Exit 1 when the result is at least this severe")
    args = ap.parse_args()
    source = Path(args.source).read_text(encoding="utf-8")
    rewrite = sys.stdin.read() if args.rewrite == "-" else Path(args.rewrite).read_text(encoding="utf-8")
    result = compare(source, rewrite)
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == "json" else render(result))
    if args.fail_on == "fail":
        return 1 if result["result"] == "FAIL" else 0
    if args.fail_on == "review":
        return 1 if result["result"] in {"FAIL", "REVIEW"} else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
