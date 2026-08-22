# Corpus validation assets — STG-DE v0.4

This directory contains derived validation artifacts from public German technical documentation. It does not contain third-party manuals or source excerpts.

## Files

- `validation-report.md` — human-readable validation results.
- `sources.yaml` — public source metadata, access dates, sample token counts, and SHA-256 sample hashes.
- `source-metrics.csv` — per-source lexical metrics.
- `industry-metrics.csv` — per-industry aggregate metrics.
- `coverage-curves.csv` — incremental lexical coverage results.
- `findings.yaml` — agent-readable curation findings and limitations.

## Corpus design

The v0.4 evidence set contains 18 public German sources: three each from Maschinenbau, Automotive, Elektrotechnik, Software/IT, Medizintechnik, and Anlagenbau. Only derived metrics and metadata are distributed.

Coverage measures how many observed tokens resolve to the central controlled lexicon, declared noun plurals, or approved contractions. It is not a quality score for a source and is not a target to maximize by absorbing domain terminology into the core.
