#!/usr/bin/env python3
"""Write manifest.yaml with size and SHA-256 of every file that Git tracks."""
from pathlib import Path
import hashlib, subprocess, yaml
ROOT=Path(__file__).resolve().parents[1]
VERSION=next(l.split(':',1)[1].strip() for l in (ROOT/'CITATION.cff').read_text(encoding='utf-8').splitlines() if l.startswith('version:'))


def tracked_files():
    """Only files under version control belong in the release manifest.

    Build output, virtual environments, and other ignored files can exist in a
    working copy but are never part of a release checkout.
    """
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True).stdout
    return sorted(p for p in out.decode("utf-8").split("\0") if p and p != "manifest.yaml")


files=[]
for rel in tracked_files():
    p=ROOT/rel
    if not p.is_file():
        continue
    files.append({'path':rel,'size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
manifest={'schema_version':'0.4','release':VERSION,'status':'experimental','files':files}
(ROOT/'manifest.yaml').write_text(yaml.safe_dump(manifest,sort_keys=False,allow_unicode=True),encoding='utf-8')
print(f'Wrote manifest with {len(files)} files')
