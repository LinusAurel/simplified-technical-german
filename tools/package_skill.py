#!/usr/bin/env python3
"""Build a release ZIP of the Agent Skill and a SHA-256 checksum file.

The ZIP contains the folder `simplified-technical-german/` at its top level, which
is the layout that claude.ai (Settings > Capabilities > Skills) and other skill
loaders expect for upload.
"""
from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "simplified-technical-german"
EXCLUDE_PARTS = {"__pycache__", ".DS_Store"}
FIXED_TIME = (2026, 1, 1, 0, 0, 0)  # reproducible archives


def version() -> str:
    for line in (ROOT / "CITATION.cff").read_text(encoding="utf-8").splitlines():
        if line.startswith("version:"):
            return line.split(":", 1)[1].strip().strip("'\"")
    raise SystemExit("version not found in CITATION.cff")


def build(out_dir: Path) -> Path:
    check = subprocess.run([sys.executable, str(ROOT / "tools" / "sync_skill.py"), "--check"], capture_output=True, text=True)
    if check.returncode:
        raise SystemExit("Skill is out of sync. Run python tools/sync_skill.py first.\n" + check.stdout)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"simplified-technical-german-{version()}.zip"
    files = sorted(p for p in SKILL.rglob("*") if p.is_file() and not (set(p.parts) & EXCLUDE_PARTS) and p.suffix != ".pyc")
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            info = zipfile.ZipInfo(str(Path(SKILL.name) / path.relative_to(SKILL)), FIXED_TIME)
            info.external_attr = (0o755 if path.suffix == ".py" else 0o644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, path.read_bytes())
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    (out_dir / (target.name + ".sha256")).write_text(f"{digest}  {target.name}\n", encoding="utf-8")
    return target


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=str(ROOT / "dist"), help="Output directory (default: dist/)")
    target = build(Path(ap.parse_args().out))
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
