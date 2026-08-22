#!/usr/bin/env python3
"""Generate standalone Agent Skill references from canonical STG-DE sources."""
from __future__ import annotations
import argparse, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "simplified-technical-german"
REF = SKILL / "references"


def generated() -> dict[Path, str]:
    rules_parts = ["# STG-DE writing rules\n\nGenerated from the canonical top-level `rules/` directory.\n"]
    for p in sorted((ROOT / "rules").glob("[0-9][0-9]-*.md")):
        rules_parts += [f"\n---\n\n<!-- source: {p.relative_to(ROOT)} -->\n\n", p.read_text(encoding="utf-8")]
    guide = "# STG-DE dictionary and morphology guide\n\nGenerated from canonical repository documentation.\n\n"
    for p in [ROOT / "dictionary" / "README.md", ROOT / "dictionary" / "MORPHOLOGY.md", ROOT / "dictionary" / "DECISIONS.md"]:
        guide += f"\n---\n\n<!-- source: {p.relative_to(ROOT)} -->\n\n" + p.read_text(encoding="utf-8")
    return {
        REF / "rules.md": "".join(rules_parts),
        REF / "dictionary-guide.md": guide,
        REF / "validator-contract.md": (ROOT / "validator-contract.md").read_text(encoding="utf-8"),
        REF / "approved-words.yaml": (ROOT / "dictionary" / "approved-words.yaml").read_text(encoding="utf-8"),
        REF / "prohibited-words.yaml": (ROOT / "dictionary" / "prohibited-words.yaml").read_text(encoding="utf-8"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    REF.mkdir(parents=True, exist_ok=True)
    expected = generated()
    mismatches = []
    for path, content in expected.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                mismatches.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(content, encoding="utf-8")
    script_target = SKILL / "scripts" / "stg_lint.py"
    source = ROOT / "tools" / "stg_lint.py"
    if args.check:
        if not script_target.exists() or script_target.read_bytes() != source.read_bytes():
            mismatches.append(str(script_target.relative_to(ROOT)))
    else:
        script_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, script_target)
    if mismatches:
        print("Skill references are out of sync:")
        for m in mismatches: print("-", m)
        return 1
    print("Skill references are in sync." if args.check else "Skill references updated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
