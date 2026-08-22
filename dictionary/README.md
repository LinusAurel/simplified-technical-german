# STG-DE controlled dictionary — v0.4

**Release:** 0.4.0  
**Profile:** `de-DE`  
**Status:** stratified-corpus-validated experimental authoring core; not yet a human-reviewed full German general-language dictionary.

## Contents

- **435** central approved/restricted lexical entries,
- **442** controlled meanings,
- **160** prohibited or review-required words/phrases,
- **172** controlled central verbs,
- controlled contractions,
- declared noun plurals and curated irregular surface forms,
- concept index and release coverage metadata,
- project/domain technical noun and verb category models.

The lexicon is independently designed for German. It is a controlled dictionary with defined meanings, word classes, and approved forms.

## Files

- `approved-words.yaml` — normative v0.4 authoring-core entries.
- `prohibited-words.yaml` — prohibited/review-required wording and rewrite guidance.
- `contractions.yaml` — preposition+article normalization before lexical lookup.
- `concept-index.yaml` — controlled-meaning index for agents and validators.
- `coverage.yaml` — release counts and corpus summary.
- `DECISIONS.md` — curation rationale.
- `MORPHOLOGY.md` — lemma/inflection and separable-verb resolution.
- `technical-nouns.yaml` — categories for project/domain technical nouns.
- `technical-verbs.yaml` — categories for project/domain technical verbs.

## Resolution principle

Resolve input in this order:

1. protected text/identifier,
2. approved project/domain terminology,
3. longest phrase,
4. contraction normalization,
5. case-sensitive lexical distinction,
6. canonical central lemma or declared surface form,
7. declared controlled inflection,
8. prohibited/review lookup,
9. deterministic morphology/separable-verb analysis,
10. otherwise `NEEDS_LEXICON_REVIEW`.

A canonical lemma takes precedence over another entry's inflection alias. This prevents `Daten` (technical information/data) from being silently resolved as the plural of `Datum`.

## Status values

- `approved` — permitted for the listed controlled meaning.
- `restricted` — permitted only when all listed restrictions are satisfied.
- `technical_only` — requires project/domain terminology approval.
- `prohibited` — do not use except inside protected external text.
- `review_required` — not safe for automatic acceptance; context or rewrite is required.

## Corpus policy

Corpus frequency is evidence for **review**, not approval. v0.4 adds a word to the core only when its cross-domain meaning can be controlled usefully. Common but abstract/polysemous verbs such as `führen`, `bieten`, `berücksichtigen`, and `gewährleisten` remain review-required.

Domain parts, product names, medical concepts, vehicle terms, software identifiers, and similar vocabulary belong to project/domain terminology even when frequent.

See `../corpus/validation-report.md`.

## `STG-C-core` versus `STG-C`

`STG-C-core` is a closed-vocabulary experimental profile for texts intentionally authored with this core plus approved project terminology.

`STG-C` remains reserved for a future broader, human-reviewed lexicon and must not be claimed by this release.
