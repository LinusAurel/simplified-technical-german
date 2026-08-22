# STG-DE Corpus Protocol

This protocol governs corpus-based development from v0.5 onward. The objective is to improve the language model and validator without overfitting the central dictionary to a small set of documents.

## 1. Corpus partitions

Every evaluation corpus must assign each document to exactly one partition.

### Development set

Use for:

- discovering missing core vocabulary;
- finding recurring ambiguity patterns;
- proposing new rules or validator checks;
- improving morphology and terminology routing.

Dictionary and rule changes may be derived from this set.

### Validation set

Use during implementation to compare candidate changes and identify regressions.

Do not add vocabulary only because it improves validation-set coverage. A candidate still needs cross-domain justification.

### Holdout set

Use only for release evaluation.

Do not inspect holdout unknown-token lists while curating the dictionary for the same release. Holdout results estimate generalization to unseen German text.

Recommended initial split by document count:

```text
70% development
15% validation
15% holdout
```

Stratify the split by domain and, where practical, by source organization.

## 2. Target domains

The corpus should not be limited to engineering manuals. STG-DE is intended for controlled German across technical, operational, B2B, B2C, and agent-facing communication.

Target strata for v0.5:

1. Maschinenbau and manufacturing
2. Automotive and mobility
3. Elektrotechnik and energy
4. Software, SaaS, and IT operations
5. Medizintechnik and health-product instructions
6. Anlagenbau and infrastructure
7. Customer support and help-center content
8. Consumer product instructions
9. Public-sector and administrative instructions
10. Finance and insurance customer communication
11. Logistics and transport
12. Telecommunications
13. Requirements and specifications
14. Agent, API, tool, and system instructions

No single stratum should dominate the token count enough to define the general core vocabulary by itself.

## 3. Source eligibility

A source is eligible when:

- it is public, licensed for the intended analysis, or otherwise available for lawful internal evaluation;
- its language is primarily German;
- its document identity and version can be recorded;
- its provenance can be reproduced;
- the text represents real communication rather than synthetic text generated solely to improve STG-DE metrics.

Do not redistribute third-party full text unless the right to redistribute it is explicit.

## 4. Source metadata

Record at least:

```yaml
id: unique-source-id
partition: development | validation | holdout
domain: software_it
organization: Example GmbH
title: Example Benutzerhandbuch
url: https://example.org/exact-document
version: "2.4"
published_on: 2026-01-15
accessed_on: 2026-08-22
language: de-DE
source_type: manual
license_or_access_basis: public-analysis-only
content_sha256: ...
token_count: 12345
extraction_method: html-text | pdf-text | other
notes: ...
```

Prefer an exact document URL over a manufacturer homepage.

## 5. Sampling and deduplication

For full-text evaluation:

- remove navigation chrome, repeated headers/footers, cookie text, and obvious boilerplate where possible;
- retain meaningful headings, warnings, lists, procedures, and prose;
- detect exact duplicates by content hash;
- identify near-duplicate manuals or versioned copies where practical;
- avoid counting the same source text through mirrors or multiple URLs.

For excerpt evaluation:

- document the selection method before inspecting STG-DE results;
- do not cherry-pick excerpts because they contain known violations or known approved vocabulary;
- keep excerpt lengths comparable within the same benchmark.

## 6. Core-vocabulary admission

Corpus frequency alone does not make a word suitable for the central dictionary.

A proposed core entry should normally satisfy all of these conditions:

- appears across multiple independent documents;
- appears across more than one domain or has a strong general-language function;
- has a controllable meaning and part of speech;
- is preferable to competing synonyms for clarity or consistency;
- is not primarily a product, organization, standard, or domain-specific term;
- can be documented with a stable controlled meaning.

Domain-specific terms belong in project terminology unless there is evidence for general core use.

## 7. Evaluation metrics

Report at least:

- total token count;
- unique normalized token count;
- central controlled surface coverage;
- project/domain terminology routing rate where applicable;
- unknown-token rate;
- prohibited/review-term rate;
- deterministic finding count per 1,000 words;
- metrics per domain and partition.

Coverage is not a quality score. Increasing coverage by absorbing domain vocabulary into the central core is not automatically an improvement.

## 8. Manual holdout review

For each release candidate, manually label a sample from the holdout set.

At minimum, record for each validator finding:

```text
true positive
false positive
severity correct/incorrect
rule ID correct/incorrect
```

Also review a sample of unflagged sentences for false negatives.

Report precision for deterministic checks separately from heuristic checks. Do not combine them into one headline accuracy number.

## 9. Release discipline

For a release that changes the dictionary, rules, or validator:

1. freeze the development changes;
2. run the validation set;
3. resolve implementation bugs without using holdout vocabulary for curation;
4. run the holdout once for the release candidate;
5. publish aggregate holdout metrics;
6. move old holdout material into development only when a new independent holdout has been selected for the next cycle.

## 10. v0.5 scale target

Initial target:

- at least 100,000 German tokens across the full corpus;
- at least 10 target strata represented where suitable public/licensed material exists;
- multiple independent organizations per major stratum;
- a non-empty document-level holdout partition.

Preferred target before v0.6: 500,000+ tokens with improved German linguistic analysis.
