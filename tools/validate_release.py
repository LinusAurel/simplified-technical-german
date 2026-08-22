#!/usr/bin/env python3
from pathlib import Path
import collections, csv, hashlib, json, re, subprocess, sys, yaml
ROOT=Path(__file__).resolve().parents[1]

def fail(msg):
    print('FAIL:',msg,file=sys.stderr); raise SystemExit(1)

def main():
    # Parse structured resources.
    for p in ROOT.rglob('*.yaml'):
        try: yaml.safe_load(p.read_text(encoding='utf-8'))
        except Exception as e: fail(f'YAML parse {p.relative_to(ROOT)}: {e}')
    for p in ROOT.rglob('*.json'):
        try: json.loads(p.read_text(encoding='utf-8'))
        except Exception as e: fail(f'JSON parse {p.relative_to(ROOT)}: {e}')
    A=yaml.safe_load((ROOT/'dictionary/approved-words.yaml').read_text(encoding='utf-8'))['entries']
    P=yaml.safe_load((ROOT/'dictionary/prohibited-words.yaml').read_text(encoding='utf-8'))['entries']
    if len({e['entry_id'] for e in A}) != len(A): fail('duplicate dictionary entry_id')
    mids=[m['id'] for e in A for m in e.get('meanings',[])]
    if len(mids)!=len(set(mids)): fail('duplicate controlled meaning id')
    app={e['lemma'].casefold() for e in A}; pro={e['term'].casefold() for e in P}
    if app & pro: fail(f'approved/prohibited overlap: {sorted(app&pro)}')
    ri=yaml.safe_load((ROOT/'rules/rule-index.yaml').read_text(encoding='utf-8'))['rules']
    if len(ri)!=75 or len({r['id'] for r in ri})!=75: fail('expected 75 unique rules/recommendations')
    src=yaml.safe_load((ROOT/'corpus/sources.yaml').read_text(encoding='utf-8'))
    if src.get('source_count')!=18: fail('expected 18 public corpus sources')
    inds=collections.Counter(s['industry'] for s in src['sources'])
    if len(inds)!=6 or set(inds.values())!={3}: fail(f'corpus imbalance: {dict(inds)}')
    # Skill must be synchronized.
    cp=subprocess.run([sys.executable,str(ROOT/'tools/sync_skill.py'),'--check'],capture_output=True,text=True)
    if cp.returncode: fail(cp.stdout+cp.stderr)
    # Manifest integrity.
    man=yaml.safe_load((ROOT/'manifest.yaml').read_text(encoding='utf-8'))
    for item in man.get('files',[]):
        fp=ROOT/item['path']
        if not fp.exists(): fail(f"manifest file missing: {item['path']}")
        if hashlib.sha256(fp.read_bytes()).hexdigest()!=item['sha256']: fail(f"manifest hash mismatch: {item['path']}")
    rows=list(csv.DictReader((ROOT/'corpus/coverage-curves.csv').open(encoding='utf-8')))
    final=float(rows[-1]['overall_coverage']) if rows else 0
    print(json.dumps({'status':'PASS','release':'0.4.0','central_entries':len(A),'controlled_meanings':len(mids),'prohibited_or_review_entries':len(P),'rules_and_recommendations':len(ri),'public_corpus_sources':18,'public_corpus_industries':6,'final_public_controlled_surface_coverage':final,'agent_skill':'PASS'},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
