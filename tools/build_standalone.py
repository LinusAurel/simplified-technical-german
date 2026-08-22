#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
out=["# STG-DE — Simplified Technical German\n\nStandalone specification snapshot for release 0.4.0. The repository files remain the canonical source.\n"]
sections=[ROOT/'specification.md']
sections += sorted((ROOT/'rules').glob('[0-9][0-9]-*.md'))
sections += [ROOT/'dictionary/README.md', ROOT/'dictionary/MORPHOLOGY.md', ROOT/'dictionary/DECISIONS.md', ROOT/'corpus/validation-report.md']
for p in sections:
    out += [f"\n---\n\n<!-- source: {p.relative_to(ROOT)} -->\n\n",p.read_text(encoding='utf-8')]
# Structured appendices make the standalone file agent-readable without third-party source text.
for p in [ROOT/'rules/rule-index.yaml',ROOT/'dictionary/approved-words.yaml',ROOT/'dictionary/prohibited-words.yaml']:
    out += [f"\n---\n\n## Structured appendix: `{p.relative_to(ROOT)}`\n\n```yaml\n",p.read_text(encoding='utf-8'),"\n```\n"]
(ROOT/'STG-DE.md').write_text(''.join(out),encoding='utf-8')
print(ROOT/'STG-DE.md')
