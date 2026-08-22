# AGENTS.md

## Purpose

This repository contains the canonical STG-DE specification, dictionary, validator tools, public corpus-derived metrics, and the packaged Agent Skill source.

## Source of truth

- Edit canonical rules in `rules/`.
- Edit central terminology in `dictionary/`.
- Edit mapping data in `mapping/`.
- Do not hand-edit generated files in `skills/simplified-technical-german/references/` or the generated skill linter copy.
- After canonical changes, run `python tools/sync_skill.py`.
- Rebuild `STG-DE.md` with `python tools/build_standalone.py`.
- Rebuild `manifest.yaml` with `python tools/build_manifest.py`.

## Corpus boundary

Use only public or explicitly approved corpus sources in repository-facing validation artifacts. Do not commit full third-party manuals or private source documents. Store source metadata and derived metrics only.

## Validation

Run before commit:

```bash
python tools/sync_skill.py
python tools/build_standalone.py
python tools/build_manifest.py
python -m unittest discover -s tests -v
python tools/sync_skill.py --check
python tools/validate_release.py
```

## Language design

Do not add a word to the central dictionary merely because it appears frequently. Prefer project terminology for narrow product, company, scientific, legal, medical, or industry-specific terms. Preserve the distinction between deterministic violations and review-required heuristics.
