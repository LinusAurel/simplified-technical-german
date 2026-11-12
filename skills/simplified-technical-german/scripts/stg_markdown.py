#!/usr/bin/env python3
"""Markdown-aware text segmentation shared by the STG-DE tools (standard library only)."""
from __future__ import annotations

import re

FENCE_RE = re.compile(r"^\s*(```|~~~)")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
FRONT_MATTER_RE = re.compile(r"\A---\n.*?\n---[ \t]*(?:\n|\Z)", re.S)
# Regions between these markers are not checked, e.g. intentionally non-compliant examples.
LINT_OFF_RE = re.compile(r"<!--\s*stg-lint:\s*off\s*-->.*?(?:<!--\s*stg-lint:\s*on\s*-->|\Z)", re.S)
# Markdown list markers and the bullets common in plain text, PDF, and Word exports.
LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+•‣◦▪▸→–]|\d+[.)])\s+")
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)*\|?\s*$")


def strip_markdown_code(text: str) -> str:
    """Blank fenced code, HTML comments, and stg-lint:off regions; keep the line count."""
    # YAML front matter at the start of a Markdown file is metadata, not prose.
    front = FRONT_MATTER_RE.match(text)
    if front:
        text = "\n" * front.group(0).count("\n") + text[front.end():]
    text = LINT_OFF_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    text = HTML_COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    out, fence = [], None
    for line in text.splitlines():
        m = FENCE_RE.match(line)
        if fence:
            if m and m.group(1) == fence:
                fence = None
            out.append("")
        elif m:
            fence = m.group(1)
            out.append("")
        else:
            out.append(line)
    return "\n".join(out)


def prose_blocks(text: str) -> list[str]:
    """Split Markdown/plain text into prose blocks.

    Headings, list items, table cells, and paragraphs are separate blocks, so that a
    sentence never runs across Markdown structure.
    """
    blocks: list[str] = []
    current: list[str] = []

    def flush() -> None:
        if current:
            blocks.append(" ".join(current))
            current.clear()

    for line in strip_markdown_code(text).splitlines():
        stripped = line.strip()
        if stripped.startswith(">"):
            stripped = stripped.lstrip("> ").strip()
        if not stripped:
            flush()
        elif stripped.startswith("#"):
            flush()
            blocks.append(stripped.lstrip("#").strip())
        elif stripped.startswith("|"):
            flush()
            if not TABLE_SEPARATOR_RE.match(stripped):
                blocks += [cell.strip() for cell in stripped.strip("|").split("|") if cell.strip()]
        elif LIST_ITEM_RE.match(line):
            flush()
            current.append(LIST_ITEM_RE.sub("", line).strip())
        else:
            current.append(stripped)
    flush()
    return [b for b in blocks if b]


SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])(?:[\"'»”)]*)\s+(?=[A-ZÄÖÜ0-9„\"'([])")
# A period after these abbreviations does not end a sentence.
ABBREVIATIONS = (
    "bzw", "ca", "ggf", "evtl", "vgl", "inkl", "exkl", "bspw", "sog", "zzgl", "Dr", "Hr", "Hrsg",
    "z. B", "z.B", "d. h", "d.h", "u. a", "u.a", "u. U", "i. d. R", "o. Ä", "v. a", "s. o", "s. u", "z. T",
)
# These abbreviations are protected only before a number ("Nr. 5", "Abb. 3").
NUMBERED_ABBREVIATIONS = ("Nr", "Abb", "Kap", "Abs", "Art", "Ziff", "Tab", "Pos", "Bd", "S", "Tel", "max", "min", "ca")
ABBREVIATION_RE = re.compile(
    r"(?<![\wÄÖÜäöüß])(" + "|".join(re.escape(a) for a in sorted(ABBREVIATIONS, key=len, reverse=True)) + r")\."
    + r"|(?<![\wÄÖÜäöüß])((?i:" + "|".join(re.escape(a) for a in NUMBERED_ABBREVIATIONS) + r"))\.(?=\s*\d)"
)
MONTHS = "Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember"
ORDINAL_DATE_RE = re.compile(r"(?<!\d)(\d{1,2})\.(?=\s+(?:" + MONTHS + r")\b)")
PROTECTED_DOT = "\u2024"  # one-dot leader, restored after splitting


def split_sentences(text: str) -> list[str]:
    """Split prose into sentences without splitting after abbreviations or ordinal dates."""
    text = re.sub(r"\s+", " ", text.strip())
    if not text:
        return []
    protected = ABBREVIATION_RE.sub(lambda m: (m.group(1) or m.group(2)).replace(".", PROTECTED_DOT) + PROTECTED_DOT, text)
    protected = ORDINAL_DATE_RE.sub(lambda m: m.group(1) + PROTECTED_DOT, protected)
    return [part.strip().replace(PROTECTED_DOT, ".") for part in SENTENCE_SPLIT_RE.split(protected) if part.strip()]
