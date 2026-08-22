# Changelog

## 0.4.0 — 2026-08-22

Public repository release.

- Added a stratified public validation set with 18 German technical sources across six industries.
- Increased the central lexicon to 435 entries and 442 controlled meanings.
- Added collision-safe handling for German inflection, including the `Datum` / `Daten` case.
- Replaced capitalization-based technical-term assumptions with neutral noun-candidate routing.
- Added public per-source, per-industry, and incremental coverage metrics.
- Added a reusable Agent Skill for writing, rewriting, and auditing German text with STG-DE.
- Added a deterministic linter and project terminology configuration.
- Added repository CI and release/skill validation.

## 0.3.0

- Expanded the controlled core vocabulary and morphology model.
- Added corpus-driven lexical review and validator improvements.
- Added explicit handling for ambiguous pronominal adverbs and German contractions.

## 0.2.0

- Expanded the controlled dictionary and prohibited/review-required term list.
- Added morphology guidance, schemas, validator contracts, and conformance tests.

## 0.1.0

- Initial German controlled-language specification.
- Added the first STG-DE rule index and German-specific rules.
- Added German-specific rules for compounds, separable verbs, sentence brackets, modality, nominal style, pronouns, and negation.
