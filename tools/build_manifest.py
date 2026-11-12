#!/usr/bin/env python3
"""Write manifest.yaml with size and SHA-256 of every file that Git tracks.

manifest.yaml is a release artifact. The repository does not track it; the
release workflow builds it and attaches it to the GitHub release.
"""
from pathlib import Path
import argparse, hashlib, subprocess, yaml
ROOT=Path(__file__).resolve().parents[1]
# Version of the manifest file format, not of the release. Change it only when
# the structure of manifest.yaml changes (see VERSIONING.md, "Schema-Versionen").
MANIFEST_SCHEMA_VERSION='0.1'
VERSION=next(l.split(':',1)[1].strip() for l in (ROOT/'CITATION.cff').read_text(encoding='utf-8').splitlines() if l.startswith('version:'))


def tracked_files():
    """Only files under version control belong in the release manifest.

    Build output, virtual environments, and other ignored files can exist in a
    working copy but are never part of a release checkout.
    """
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True).stdout
    return sorted(p for p in out.decode("utf-8").split("\0") if p and p != "manifest.yaml")


def build_manifest() -> dict:
    files = []
    for rel in tracked_files():
        p = ROOT / rel
        if not p.is_file():
            continue
        files.append({'path': rel, 'size_bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    return {'schema_version': MANIFEST_SCHEMA_VERSION, 'release': VERSION, 'status': 'experimental', 'files': files}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=str(ROOT / "manifest.yaml"), help="Output path (default: manifest.yaml in the repository root).")
    args = ap.parse_args()
    manifest = build_manifest()
    Path(args.out).write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding='utf-8')
    print(f"Wrote manifest with {len(manifest['files'])} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
