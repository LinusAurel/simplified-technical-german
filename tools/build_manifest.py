#!/usr/bin/env python3
from pathlib import Path
import hashlib, yaml
ROOT=Path(__file__).resolve().parents[1]
exclude={'.git','dist','__pycache__','.pytest_cache'}
files=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or any(part in exclude for part in p.parts):
        continue
    if p.name=='manifest.yaml':
        continue
    rel=p.relative_to(ROOT).as_posix()
    files.append({'path':rel,'size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
manifest={'schema_version':'0.4','release':'0.4.0','status':'experimental','files':files}
(ROOT/'manifest.yaml').write_text(yaml.safe_dump(manifest,sort_keys=False,allow_unicode=True),encoding='utf-8')
print(f'Wrote manifest with {len(files)} files')
