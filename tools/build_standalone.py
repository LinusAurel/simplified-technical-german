#!/usr/bin/env python3
"""Build STG-DE.md from the canonical sources.

STG-DE.md is a release artifact. The repository does not track it; the release
workflow builds it and attaches it to the GitHub release.
"""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "STG-DE.md"


def build() -> str:
    version = next(l.split(':', 1)[1].strip() for l in (ROOT / 'CITATION.cff').read_text(encoding='utf-8').splitlines() if l.startswith('version:'))
    out = ["# STG-DE — Vereinfachtes Technisches Deutsch\n\nEigenständige Fassung der Spezifikation für Release " + version + ". Die Dateien im Repository bleiben die kanonische Quelle.\n"]
    sections = [ROOT / 'specification.md']
    sections += sorted((ROOT / 'rules').glob('[0-9][0-9]-*.md'))
    sections += [ROOT / 'dictionary/README.md', ROOT / 'dictionary/MORPHOLOGY.md', ROOT / 'dictionary/DECISIONS.md', ROOT / 'mapping/README.md']
    for p in sections:
        out += [f"\n---\n\n<!-- source: {p.relative_to(ROOT)} -->\n\n", p.read_text(encoding='utf-8')]
    # Structured appendices make the standalone file agent-readable without third-party source text.
    for p in [ROOT / 'rules/rule-index.yaml', ROOT / 'mapping/ste100-issue9.yaml', ROOT / 'dictionary/approved-words.yaml', ROOT / 'dictionary/prohibited-words.yaml']:
        out += [f"\n---\n\n## Strukturierter Anhang: `{p.relative_to(ROOT)}`\n\n```yaml\n", p.read_text(encoding='utf-8'), "\n```\n"]
    return ''.join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=str(TARGET), help="Output path (default: STG-DE.md in the repository root).")
    args = ap.parse_args()
    out = Path(args.out)
    out.write_text(build(), encoding='utf-8')
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
