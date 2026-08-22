# Contributing to STG-DE

STG-DE is intended to work across industries and communication types. Contributions should therefore separate general German from domain-specific terminology.

## Central vocabulary proposals

Do not add a word directly to `dictionary/approved-words.yaml` only because it occurs frequently in a corpus.

For a normative central-lexicon change:

1. Read `dictionary/GOVERNANCE.md`.
2. Copy `dictionary/proposals/TEMPLATE.yaml`.
3. Assign a proposal ID such as `LEX-2026-001`.
4. Define one controlled meaning and part of speech.
5. Document ambiguity risk and alternatives considered.
6. Add corpus/public/linguistic evidence where applicable.
7. Explain whether the term belongs in the central core rather than project terminology.
8. Add or update tests if validator behavior changes.
9. Record the final review decision before merging the normative dictionary change.

The proposal format is defined by `schemas/lexicon-proposal.schema.json`.

### Core vs project terminology

Prefer `.stg-de.yaml` project terminology when a word is primarily:

- a product or component name;
- domain-specific jargon with a precise local meaning;
- terminology defined by one organization or technical standard;
- useful mainly for increasing one corpus/domain's coverage.

A rejected central-core proposal can still be valid project terminology.

## Rule changes

A rule change should include:

- the problem it solves;
- at least one non-compliant and compliant example;
- the expected effect on existing texts;
- validator implications when applicable;
- an update to `quality/RULE-COVERAGE.md` when automation status changes.

Rule IDs are stable identifiers. Do not invent a new ID in validator code before adding it to `rules/rule-index.yaml`.

## Corpus changes

Follow `corpus/PROTOCOL.md`.

Do not commit third-party full-text corpus documents unless redistribution rights are explicit. Add metadata and derived metrics instead.

The holdout partition is evaluation-only. Do not use its unknown-token list to select central vocabulary for the same release.

## Tests

For normal development run:

```bash
python -m unittest discover -s tests -v
python tools/sync_skill.py --check
python tools/validate_release.py --skip-manifest
```

Before a tagged release, rebuild the manifest and run the full integrity check:

```bash
python tools/build_manifest.py
python tools/validate_release.py
```

A validator feature must include regression tests for its rule ID and for a known false-positive boundary when applicable.
