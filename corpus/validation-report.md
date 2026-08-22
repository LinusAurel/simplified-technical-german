# STG-DE v0.4 — Multi-industry corpus validation report

## Executive result

v0.4 validates the authoring core against a **stratified six-industry corpus** rather than a single engineering domain. The public validation set contains **18 independent technical sources** — three per industry — and **2,066 analyzed tokens** in short German excerpts. The release does **not** redistribute the excerpts or manuals; it stores source metadata, hashes, frequencies, and aggregate metrics only.

| Metric | v0.3 baseline | v0.4 normalization only | v0.4 final |
|---|---:|---:|---:|
| Controlled central surface coverage | 51.4% | 52.7% | **58.1%** |
| `NEEDS_LEXICON_REVIEW` tokens | 272 | 245 | **232** |
| Routed/classified rate | 86.8% | 88.1% | **88.8%** |

The final central surface coverage is **6.7 percentage points** above the historical v0.3 baseline on this public set. This is not a target acceptance rate: technical nouns, product names, identifiers, domain verbs, and intentionally disallowed language are expected to remain outside the general core.

## Corpus design

| Industry | Sources | Tokens | v0.3 baseline | v0.4 final |
|---|---:|---:|---:|---:|
| Anlagenbau | 3 | 311 | 49.2% | **58.5%** |
| Automotive | 3 | 359 | 49.6% | **58.8%** |
| Elektrotechnik | 3 | 342 | 48.8% | **55.0%** |
| Maschinenbau | 3 | 356 | 50.3% | **58.4%** |
| Medizintechnik | 3 | 334 | 52.1% | **55.4%** |
| Software/IT | 3 | 364 | 58.0% | **62.1%** |

The six strata are Maschinenbau, Automotive, Elektrotechnik, Software/IT, Medizintechnik, and Anlagenbau. Source selection favors manufacturer or project documentation that is publicly accessible in German. `corpus/sources.yaml` records exact source metadata and sample hashes.

The token counts are intentionally close but not identical. Equal document count prevents one industry from dominating the curation pass. Because third-party manuals are not included, this release should be read as a **stratified evidence corpus**, not a full-text archive.

## What v0.4 changed

### 1. German noun morphology is part of lexical resolution

v0.3 stored plural forms such as `Informationen`, `Gefahren`, `Schritte`, and `Geräte` in noun metadata but the development validator did not resolve them. v0.4 recognizes **declared noun plurals** as `CENTRAL_INFLECTION`. On the same public excerpts, normalization alone raises controlled coverage from 51.4% to 52.7%.

This is a validator correction, not vocabulary inflation.

### 2. `Datum` and `Daten` are no longer conflated

The corpus exposed a German lexical collision: `Datum` has the plural `Daten`, while technical documentation usually uses `Daten` to mean information/data. A naive plural index therefore gives the wrong controlled meaning. v0.4 adds an independent restricted lemma `Daten` and gives canonical lemmas priority over plural aliases.

This finding is important for agentic validation: lexical surface equality is insufficient when German inflection collides with another lexical concept.

### 3. Capitalization no longer means “technical term”

German capitalizes all nouns. The v0.3 development heuristic routed any unknown capitalized token to `TECHNICAL_TERM_CANDIDATE`; this overstates terminology coverage. v0.4 uses the neutral class `LEXICAL_NOUN_CANDIDATE`. A candidate becomes project terminology only after resolution against an approved project glossary or a technical-noun category.

### 4. Only cross-domain, controllable vocabulary entered the core

v0.4 adds general technical-document concepts such as `Betriebsanleitung`, `Fachpersonal`, `Verletzung`, `Verwendung`, `Produkt`, `Version`, `Änderung`, `Kennzeichnung`, `Symbol`, `Daten`, and direct verbs such as `lesen`, `wählen`, `bedienen`, and `benötigen`.

Frequency alone was **not** sufficient for approval. Common words such as `führen`, `bieten`, `berücksichtigen`, and `gewährleisten` are routed to review because their technical meaning is too context-dependent or abstract for unconditional approval.

### 5. The coverage curve is now reproducible

`corpus/coverage-curves.csv` starts with the historical v0.3 result, applies the v0.4 normalization layer, and then adds each new core entry in a deterministic evidence order. This separates gains from grammar/lemmatization fixes from gains caused by new vocabulary.

## Final industry distribution

| Industry | Controlled | Unknown | Review | Prohibited | Lexical noun candidates |
|---|---:|---:|---:|---:|---:|
| Anlagenbau | 58.5% | 32 | 6 | 4 | 81 |
| Automotive | 58.8% | 39 | 7 | 5 | 85 |
| Elektrotechnik | 55.0% | 44 | 10 | 4 | 80 |
| Maschinenbau | 58.4% | 41 | 11 | 5 | 79 |
| Medizintechnik | 55.4% | 42 | 9 | 6 | 83 |
| Software/IT | 62.1% | 34 | 6 | 5 | 81 |

## Recurring non-STG patterns

The corpus continues to justify rejecting or reviewing ordinary professional German that is not sufficiently deterministic for controlled authoring. Recurring examples include `sowie`, `entsprechend`, `gegebenenfalls`, `ausreichend`, and context-dependent verbs such as `führen` or `durchführen`.

The goal is not to make existing manuals pass unchanged. The goal is to give authors and agents deterministic rewrites and to separate general core vocabulary from domain terminology.


## What v0.4 does not prove

v0.4 is materially stronger than v0.3, but it is still an experimental authoring standard. It does not establish population-level coverage of German technical documentation, and it does not replace:

- expert review by German technical writers and terminologists;
- full-text licensed corpus analysis at substantially larger scale;
- a deterministic German morphological and syntactic analyzer;
- reader comprehension testing;
- safety-domain validation against the publication standard applicable to a product;
- project terminology governance.

`STG-C-core` therefore remains experimental. `STG-C` remains reserved for a later, human-reviewed release.
