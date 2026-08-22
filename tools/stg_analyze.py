#!/usr/bin/env python3
"""Conservative German-language review evidence for STG-DE.

This module intentionally produces REVIEW evidence, not deterministic conformance errors.
It uses bounded lexical/syntactic heuristics that can run without downloading an NLP model.
The deterministic `stg_lint.py` remains the authority for mechanically proven checks.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

WORD = r"[A-Za-zÄÖÜäöüß]+"
TOKEN_RE = re.compile(WORD)
SENTENCE_RE = re.compile(r"(?<=[.!?])(?:[\"'»”)]*)\s+(?=[A-ZÄÖÜ0-9„\"'([])")
CODE_RE = re.compile(r"`[^`]*`")
URL_RE = re.compile(r"https?://\S+|www\.\S+", re.I)

SUBORDINATORS = {
    "als", "bevor", "bis", "da", "damit", "dass", "falls", "indem", "nachdem",
    "ob", "obwohl", "sobald", "sofern", "solange", "während", "weil", "wenn",
}
PRONOMINAL_ADVERBS = {
    "dabei", "dafür", "dagegen", "dahinter", "damit", "danach", "daneben", "daran",
    "darauf", "daraus", "darin", "darüber", "darum", "darunter", "davon", "davor", "dazu",
}
PRONOUNS = {
    "er", "ihm", "ihn", "ihnen", "ihr", "ihre", "ihrem", "ihren", "ihrer", "ihres",
    "sie", "es", "sein", "seine", "seinem", "seinen", "seiner", "seines",
}
MODALS = {
    "muss": "requirement", "müssen": "requirement", "musste": "requirement",
    "darf": "permission_or_prohibition", "dürfen": "permission_or_prohibition", "durfte": "permission_or_prohibition",
    "kann": "capability_or_possibility", "können": "capability_or_possibility", "konnte": "capability_or_possibility",
    "soll": "ambiguous_normative", "sollen": "ambiguous_normative", "sollte": "ambiguous_normative", "sollten": "ambiguous_normative",
    "müsste": "ambiguous_normative", "müssten": "ambiguous_normative",
}
SEPARABLE_PARTICLES = {
    "ab", "an", "auf", "aus", "bei", "ein", "fest", "fort", "frei", "her", "hin", "los",
    "mit", "nach", "nieder", "statt", "teil", "um", "vor", "weg", "weiter", "wieder", "zu", "zurück", "zusammen",
}
NOMINAL_SUFFIXES = ("ierung", "isation", "isierung", "tion", "tät", "ung")
AUX_PASSIVE = {"wird", "werden", "wurde", "wurden", "worden"}
PARTICIPLE_PREFIXES = ("ge", "be", "er", "ent", "ver", "zer")
NEGATORS = {"nicht", "kein", "keine", "keinen", "keinem", "keiner", "keines", "nur"}


@dataclass
class Evidence:
    rule: str
    kind: str
    confidence: str
    message: str
    sentence: str
    trigger: str
    suggestion: str | None = None


def mask(text: str) -> str:
    return CODE_RE.sub(" PROTECTED_CODE ", URL_RE.sub(" PROTECTED_URL ", text))


def sentences(text: str) -> list[str]:
    compact = re.sub(r"\s+", " ", mask(text).strip())
    if not compact:
        return []
    return [part.strip() for part in SENTENCE_RE.split(compact) if part.strip()]


def words(sentence: str) -> list[str]:
    return TOKEN_RE.findall(sentence)


def lower_words(sentence: str) -> list[str]:
    return [token.casefold() for token in words(sentence)]


def likely_participle(token: str) -> bool:
    low = token.casefold()
    if len(low) < 6:
        return False
    if low.endswith(("iert", "isiert")):
        return True
    if low.startswith("ge") and low.endswith(("t", "en")):
        return True
    if low.startswith(PARTICIPLE_PREFIXES) and low.endswith(("t", "en")):
        return True
    return False


def analyze_sentence(sentence: str) -> list[Evidence]:
    tokens = words(sentence)
    lower = [t.casefold() for t in tokens]
    evidence: list[Evidence] = []

    # STG-DE-4.1: subordinate-clause complexity evidence.
    sub_positions = [i for i, token in enumerate(lower) if token in SUBORDINATORS]
    if len(sub_positions) >= 2:
        evidence.append(Evidence(
            "STG-DE-4.1", "subordinate_clause_complexity", "medium",
            "Der Satz enthält mehrere Nebensatzmarker. Prüfen Sie die Verschachtelung.", sentence,
            ", ".join(lower[i] for i in sub_positions[:4]),
            "Teilen Sie verschachtelte Bedingungen oder Beschreibungen in getrennte Sätze."
        ))
    elif sub_positions and len(tokens) > 22:
        evidence.append(Evidence(
            "STG-DE-4.1", "long_subordinate_clause", "low",
            "Ein langer Satz enthält einen Nebensatzmarker. Prüfen Sie die Satzklammer und Verschachtelung.", sentence,
            lower[sub_positions[0]], "Kürzen oder teilen Sie den Satz, wenn der Bezug nicht sofort eindeutig ist."
        ))

    # STG-3.6 / STG-DE-3.3: passive/werden candidates.
    for i, token in enumerate(lower):
        if token not in AUX_PASSIVE:
            continue
        window = tokens[max(0, i - 4): min(len(tokens), i + 6)]
        participles = [candidate for candidate in window if likely_participle(candidate)]
        if participles:
            evidence.append(Evidence(
                "STG-3.6", "passive_candidate", "medium",
                "Die Konstruktion kann ein Vorgangspassiv sein. Prüfen Sie, ob ein expliziter Akteur klarer ist.", sentence,
                f"{tokens[i]} … {participles[0]}", "Verwenden Sie Aktiv, wenn der Akteur bekannt und relevant ist."
            ))
        else:
            evidence.append(Evidence(
                "STG-DE-3.3", "werden_candidate", "low",
                "`werden` ist vorhanden. Prüfen Sie seine Funktion und ob eine direktere Form möglich ist.", sentence,
                tokens[i], None
            ))

    # STG-DE-3.2: modality classification and ambiguous normative forms.
    for i, token in enumerate(lower):
        if token not in MODALS:
            continue
        modal_class = MODALS[token]
        if modal_class == "ambiguous_normative":
            evidence.append(Evidence(
                "STG-DE-3.2", "ambiguous_modality", "high",
                "Die Modalität ist für STG-DE nicht eindeutig kodiert.", sentence, tokens[i],
                "Verwenden Sie je nach Bedeutung Imperativ, `muss`, `darf`, `darf nicht` oder `kann`."
            ))
        else:
            evidence.append(Evidence(
                "STG-DE-3.2", "modality_observation", "low",
                f"Modalverb erkannt: {modal_class}. Prüfen Sie, ob diese Stärke der beabsichtigten Aussage entspricht.",
                sentence, tokens[i], None
            ))

    # STG-DE-4.5: ambiguous pronominal-adverb review.
    for token in lower:
        if token in PRONOMINAL_ADVERBS:
            evidence.append(Evidence(
                "STG-DE-4.5", "pronominal_adverb", "medium",
                "Ein Pronominaladverb kann einen unklaren Bezug haben.", sentence, token,
                "Nennen Sie das Bezugsobjekt ausdrücklich, wenn mehr als ein Bezug möglich ist."
            ))

    # STG-DE-4.2 / GR-3: third-person pronoun review when several noun-like candidates precede it.
    capitalized = [t for t in tokens if t[:1].isupper() and t.casefold() not in {w.casefold() for w in PRONOUNS}]
    if len(capitalized) >= 2:
        for token in lower:
            if token in PRONOUNS:
                evidence.append(Evidence(
                    "STG-DE-4.2", "pronoun_reference", "low",
                    "Ein Pronomen steht in einem Satz mit mehreren möglichen nominalen Bezugsobjekten.", sentence,
                    token, "Wiederholen Sie das Substantiv, wenn der Bezug nicht eindeutig ist."
                ))
                break

    # STG-3.5: nominal style candidates. Keep as low-confidence review.
    nominal_candidates = []
    for token in tokens:
        low = token.casefold()
        if len(low) >= 8 and token[:1].isupper() and low.endswith(NOMINAL_SUFFIXES):
            nominal_candidates.append(token)
    if nominal_candidates:
        evidence.append(Evidence(
            "STG-3.5", "nominalization_candidate", "low",
            "Der Satz enthält mögliche Handlungssubstantive. Prüfen Sie eine direkte Verbform.", sentence,
            ", ".join(nominal_candidates[:4]), "Verwenden Sie ein direktes Verb, wenn dadurch Akteur und Handlung klarer werden."
        ))

    # STG-DE-3.1: approximate long separable-verb bracket evidence.
    if len(tokens) >= 14 and lower:
        final = lower[-1]
        if final in SEPARABLE_PARTICLES:
            evidence.append(Evidence(
                "STG-DE-3.1", "separable_particle_distance", "medium",
                "Ein möglicher abgetrennter Verbteil steht weit vom Satzanfang entfernt.", sentence, tokens[-1],
                "Formulieren Sie den Satz so um, dass Verb und Verbteil näher zusammenstehen."
            ))

    # STG-DE-4.4: negation/scope review when multiple scope-sensitive markers occur.
    scope_tokens = [token for token in lower if token in NEGATORS]
    if len(scope_tokens) >= 2:
        evidence.append(Evidence(
            "STG-DE-4.4", "negation_scope", "medium",
            "Mehrere Negations- oder Fokusmarker können den Geltungsbereich unklar machen.", sentence,
            ", ".join(scope_tokens), "Formulieren Sie den Geltungsbereich von Negation oder Einschränkung ausdrücklich."
        ))

    # STG-DE-2.1: long German compound candidates, review only.
    compounds = [t for t in tokens if t[:1].isupper() and len(t) >= 24 and "-" not in t]
    if compounds:
        evidence.append(Evidence(
            "STG-DE-2.1", "long_compound_candidate", "low",
            "Ein langes deutsches Kompositum kann hohe semantische Dichte haben.", sentence,
            ", ".join(compounds[:3]), "Prüfen Sie, ob die Benennung eindeutig definiert und im Dokument konsistent ist."
        ))

    return evidence


def analyze(text: str) -> dict:
    findings = [item for sentence in sentences(text) for item in analyze_sentence(sentence)]
    counts: dict[str, int] = {"high": 0, "medium": 0, "low": 0}
    for item in findings:
        counts[item.confidence] += 1
    return {
        "tool": "stg_analyze.py",
        "standard": "STG-DE",
        "status": "REVIEW EVIDENCE ONLY",
        "evidence_count": len(findings),
        "confidence_counts": counts,
        "evidence": [asdict(item) for item in findings],
        "limitations": [
            "These findings are heuristic review evidence and never prove a violation by themselves.",
            "The fallback analyzer does not perform dependency parsing, morphological disambiguation, or coreference resolution.",
            "Use sentence meaning and the normative STG-DE rule text before changing content."
        ],
    }


def render(result: dict) -> str:
    lines = [f"STG-DE language analysis: {result['status']}", ""]
    if not result["evidence"]:
        return "\n".join(lines + ["Keine heuristischen Review-Befunde."])
    for index, item in enumerate(result["evidence"], 1):
        lines.append(f"{index}. [{item['confidence'].upper()}] {item['rule']} {item['kind']}: {item['message']}")
        lines.append(f"   Trigger: {item['trigger']}")
        lines.append(f"   Satz: {item['sentence']}")
        if item.get("suggestion"):
            lines.append(f"   Review: {item['suggestion']}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Heuristic German review evidence for STG-DE")
    parser.add_argument("input", help="UTF-8 text/Markdown file or - for stdin")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()
    text = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
    result = analyze(text)
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == "json" else render(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
