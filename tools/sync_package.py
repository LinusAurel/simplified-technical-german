#!/usr/bin/env python3
"""Synchronize/check the data copies in the package stg_de/ against the canonical data.

The code in stg_de/ is canonical. Only the dictionary and profile data are copies.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "stg_de"
MAPPINGS = {
    ROOT / "dictionary" / "approved-words.yaml": PACKAGE / "dictionary" / "approved-words.yaml",
    ROOT / "dictionary" / "prohibited-words.yaml": PACKAGE / "dictionary" / "prohibited-words.yaml",
    ROOT / "profiles" / "profiles.yaml": PACKAGE / "profiles" / "profiles.yaml",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    mismatches = []
    for source, target in MAPPINGS.items():
        if args.check:
            if not target.exists() or target.read_bytes() != source.read_bytes():
                mismatches.append(str(target.relative_to(ROOT)))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    if mismatches:
        print("Package data copies are out of sync:")
        for path in mismatches:
            print("-", path)
        return 1
    print("Package copies are in sync." if args.check else "Package copies updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
