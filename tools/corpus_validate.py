#!/usr/bin/env python3
"""Development corpus audit for STG-DE v0.4.

This tool measures lexical coverage and routes unresolved tokens for curation. It is not
the normative STG conformance validator.

Important v0.4 changes:
- declared noun plurals are recognized as controlled inflections;
- plural aliases never override an independently approved lemma (Datum/Daten collision);
- unknown capitalized German words are routed as LEXICAL_NOUN_CANDIDATE, not assumed
  to be technical terminology;
- exact/surface forms and controlled inflections are reported separately;
- source text is never copied into the audit output.
"""
from __future__ import annotations
import argparse, collections, hashlib, json, re, subprocess, tempfile
from pathlib import Path
import yaml
try:
    from nltk.stem.snowball import GermanStemmer
except Exception:
    GermanStemmer = None

TOKEN_RE = re.compile(r"[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß0-9_:+/-]*|\d+(?:[.,]\d+)?", re.UNICODE)


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def extract_text(path: Path) -> str:
    if path.suffix.lower() == '.pdf':
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/'out.txt'
            subprocess.run(['pdftotext','-layout',str(path),str(out)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            return out.read_text(encoding='utf-8',errors='ignore')
    return path.read_text(encoding='utf-8',errors='ignore')


def clean_text(text: str) -> str:
    text=text.replace('\u00ad','')
    text=re.sub(r'-\n(?=[a-zäöüß])','',text)
    text=re.sub(r'\s+',' ',text)
    return text.strip()


def looks_protected(tok: str) -> bool:
    if any(ch.isdigit() for ch in tok) and any(ch.isalpha() for ch in tok):
        return True
    if re.search(r'[_:+/]', tok):
        return True
    letters=''.join(c for c in tok if c.isalpha())
    if len(letters) >= 2 and letters.isupper():
        return True
    if re.search(r'[a-zäöüß][A-ZÄÖÜ]', tok):
        return True
    if tok.casefold() in {'true','false','null','std','bool','const','void','int','double','string','return','include','define'}:
        return True
    return False


def build_central_indexes(entries):
    """Return exact index and collision-safe declared-inflection index."""
    exact_ci=collections.defaultdict(list); exact_cs=collections.defaultdict(list)
    canonical_ci=set(); canonical_cs=set()
    for e in entries:
        lemma=str(e.get('lemma',''))
        if lemma and ' ' not in lemma and '...' not in lemma:
            if e.get('case_sensitive'):
                canonical_cs.add(lemma); exact_cs[lemma].append(e)
            else:
                canonical_ci.add(lemma.casefold()); exact_ci[lemma.casefold()].append(e)
        for s in e.get('surface_forms') or []:
            if not s or ' ' in str(s) or '...' in str(s): continue
            if e.get('case_sensitive'):
                exact_cs[str(s)].append(e)
            else:
                exact_ci[str(s).casefold()].append(e)
    infl_ci=collections.defaultdict(list); infl_cs=collections.defaultdict(list)
    # Only explicitly declared noun plurals count as controlled inflections here.
    # If the plural is itself a canonical lemma, the independent lemma wins.
    for e in entries:
        if e.get('part_of_speech')!='noun': continue
        p=e.get('plural')
        if not p or not isinstance(p,str) or ' ' in p: continue
        if e.get('case_sensitive'):
            if p not in canonical_cs: infl_cs[p].append(e)
        else:
            k=p.casefold()
            if k not in canonical_ci: infl_ci[k].append(e)
    return exact_ci, exact_cs, infl_ci, infl_cs


def build_simple_index(entries, lemma_key='lemma'):
    ci=collections.defaultdict(list); cs=collections.defaultdict(list)
    for e in entries:
        vals=[e.get(lemma_key,'')]+list(e.get('surface_forms') or [])
        for s in vals:
            if not s or ' ' in str(s) or '...' in str(s): continue
            if e.get('case_sensitive'):
                cs[str(s)].append(e)
            else:
                ci[str(s).casefold()].append(e)
    return ci,cs


def make_stem_index(entries):
    if GermanStemmer is None: return {}
    st=GermanStemmer(); idx=collections.defaultdict(set)
    for e in entries:
        lemma=str(e.get('lemma',''))
        if re.fullmatch(r'[A-Za-zÄÖÜäöüß-]+',lemma) and ' ' not in lemma:
            idx[st.stem(lemma.casefold())].add(lemma)
    return idx


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('corpus')
    ap.add_argument('--root',default=str(Path(__file__).resolve().parents[1]))
    ap.add_argument('--json-out'); ap.add_argument('--md-out')
    args=ap.parse_args(); root=Path(args.root)
    approved=load_yaml(root/'dictionary/approved-words.yaml')['entries']
    prohibited=load_yaml(root/'dictionary/prohibited-words.yaml')['entries']
    contractions_path=root/'dictionary/contractions.yaml'
    contractions=load_yaml(contractions_path)['entries'] if contractions_path.exists() else []
    central,central_cs,infl,infl_cs=build_central_indexes(approved)
    pwrapped=[{'lemma':e['term'],'surface_forms':e.get('surface_forms',[]),'status':e['status'],'entry':e} for e in prohibited]
    prohib,prohib_cs=build_simple_index(pwrapped)
    contr={e['surface'].casefold():e['expands_to'] for e in contractions}
    stem_idx=make_stem_index(approved); stemmer=GermanStemmer() if GermanStemmer else None

    source=Path(args.corpus); raw=extract_text(source); text=clean_text(raw)
    source_hash=hashlib.sha256(raw.encode('utf-8',errors='ignore')).hexdigest(); tokens=TOKEN_RE.findall(text)
    counts=collections.Counter(); by_token=collections.defaultdict(collections.Counter)
    morph_targets=collections.defaultdict(collections.Counter); contraction_expansions=collections.Counter()

    for tok in tokens:
        low=tok.casefold()
        if tok[0].isdigit(): cls='PROTECTED_TOKEN_CANDIDATE'
        elif tok in prohib_cs or low in prohib:
            pe=prohib_cs.get(tok) or prohib.get(low) or []
            statuses={x['entry']['status'] for x in pe}; cls='PROHIBITED' if 'prohibited' in statuses else 'REVIEW_REQUIRED'
        elif tok in central_cs or low in central: cls='CENTRAL_EXACT'
        elif tok in infl_cs or low in infl: cls='CENTRAL_INFLECTION'
        elif low in contr:
            expansion=contr[low]
            ok=True
            for piece in expansion:
                k=piece.casefold()
                if not (k in central or k in infl): ok=False; break
            cls='CONTRACTION' if ok else 'NEEDS_LEXICON_REVIEW'
            if ok: contraction_expansions[f"{low} -> {' + '.join(expansion)}"]+=1
        elif looks_protected(tok): cls='PROTECTED_TOKEN_CANDIDATE'
        elif tok[:1].isupper(): cls='LEXICAL_NOUN_CANDIDATE'
        elif stemmer is not None:
            stem=stemmer.stem(low); targets=stem_idx.get(stem,set())
            if targets:
                cls='MORPHOLOGY_CANDIDATE'
                for t in targets: morph_targets[low][t]+=1
            else: cls='NEEDS_LEXICON_REVIEW'
        else: cls='NEEDS_LEXICON_REVIEW'
        counts[cls]+=1; by_token[cls][low]+=1

    total=len(tokens)
    controlled=counts['CENTRAL_EXACT']+counts['CENTRAL_INFLECTION']+counts['CONTRACTION']
    assisted=controlled+counts['MORPHOLOGY_CANDIDATE']
    routed=total-counts['NEEDS_LEXICON_REVIEW']
    result={
      'schema_version':'0.4','tool':'tools/corpus_validate.py','tool_role':'development_audit_not_normative_validator',
      'corpus':{'name':source.name,'sha256':source_hash,'tokens':total,'types':len({t.casefold() for t in tokens})},
      'counts':dict(counts),
      'metrics':{
        'central_controlled_surface_coverage':round(controlled/total,4) if total else 0,
        'central_with_morphology_candidate_coverage':round(assisted/total,4) if total else 0,
        'classified_or_review_routed_rate':round(routed/total,4) if total else 0,
        'lexical_noun_candidate_share':round(counts['LEXICAL_NOUN_CANDIDATE']/total,4) if total else 0,
        'protected_candidate_share':round(counts['PROTECTED_TOKEN_CANDIDATE']/total,4) if total else 0,
      },'top':{},'contraction_expansions':dict(contraction_expansions.most_common(30))}
    for cls in ['PROHIBITED','REVIEW_REQUIRED','NEEDS_LEXICON_REVIEW','LEXICAL_NOUN_CANDIDATE','PROTECTED_TOKEN_CANDIDATE','MORPHOLOGY_CANDIDATE','CENTRAL_INFLECTION']:
        result['top'][cls]=[{'token':k,'count':v} for k,v in by_token[cls].most_common(100)]
    result['morphology_candidates']={k:[{'lemma':a,'count':b} for a,b in v.most_common(5)] for k,v in list(morph_targets.items())[:500]}
    if args.json_out: Path(args.json_out).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    if args.md_out:
        lines=['# STG-DE corpus audit','',f'- Corpus: `{source.name}`',f'- SHA-256: `{source_hash}`',f'- Tokens: **{total}**',f'- Types: **{result["corpus"]["types"]}**',f'- Controlled surface coverage: **{result["metrics"]["central_controlled_surface_coverage"]:.1%}**',f'- Controlled + morphology-candidate coverage: **{result["metrics"]["central_with_morphology_candidate_coverage"]:.1%}**',f'- Routed/classified rate: **{result["metrics"]["classified_or_review_routed_rate"]:.1%}**','','## Classification counts','','| Class | Count |','|---|---:|']
        order=['CENTRAL_EXACT','CENTRAL_INFLECTION','CONTRACTION','MORPHOLOGY_CANDIDATE','LEXICAL_NOUN_CANDIDATE','PROTECTED_TOKEN_CANDIDATE','PROHIBITED','REVIEW_REQUIRED','NEEDS_LEXICON_REVIEW']
        for k in order: lines.append(f'| `{k}` | {counts[k]} |')
        for cls in ['PROHIBITED','REVIEW_REQUIRED','NEEDS_LEXICON_REVIEW','LEXICAL_NOUN_CANDIDATE','MORPHOLOGY_CANDIDATE']:
            lines += ['',f'## Top {cls}','', '| Token | Count |','|---|---:|']
            for item in result['top'][cls][:30]: lines.append(f"| `{item['token']}` | {item['count']} |")
        lines += ['','## Interpretation','',
          '- `CENTRAL_INFLECTION` is limited to explicitly declared noun plurals and is a controlled lexical form.',
          '- `MORPHOLOGY_CANDIDATE` is a Snowball-stem development heuristic and never an automatic conformance pass.',
          '- `LEXICAL_NOUN_CANDIDATE` is deliberately neutral: German capitalization alone does not prove technical terminology.',
          '- Project terminology must resolve domain nouns before `STG-T` or `STG-C-core` can pass.',
          '- The report stores frequencies only and does not redistribute source sentences.','']
        Path(args.md_out).write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({'tokens':total,'counts':dict(counts),'metrics':result['metrics']},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
