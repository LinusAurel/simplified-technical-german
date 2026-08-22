# STG-DE Rule Automation Coverage

This document records what the shipped validator can prove today. It is intentionally conservative.

A rule can be part of the STG-DE standard even when the current validator cannot detect it automatically.

## Detection classes

| Class | Meaning |
|---|---|
| `deterministic` | The validator can detect the listed condition mechanically with high confidence. |
| `partial` | A deterministic subset is implemented, but the complete rule needs context or additional analysis. |
| `heuristic` | Automation can provide evidence, but a finding must remain a review item. |
| `semantic` | Correct application depends primarily on meaning or discourse context. |
| `human-review` | The rule currently has no reliable automated implementation. |

## Implemented deterministic coverage in v0.4/v0.5-foundation

| Rule | Current automated check | Coverage |
|---|---|---|
| `STG-1.1` | Matches entries in `dictionary/prohibited-words.yaml` and returns the configured severity. | partial |
| `STG-5.1` | Counts words in procedure mode and flags sentences above 20 words. | deterministic |
| `STG-6.3` | Counts words in description/default mode and flags sentences above 25 words. | deterministic |
| `STG-8.1` | Flags semicolons used in prose lines. | partial |
| `STG-9.4` | Enforces `preferred_terms` from `.stg-de.yaml`. | partial |

The validator also reports unknown central-lexicon surface forms when `--lexicon-report` is enabled. Unknown words are review candidates, not automatic violations.

## Rules not yet mechanically proven

The following groups need either more deterministic implementation, NLP assistance, or semantic review.

### Vocabulary and terminology

- `STG-1.2` through `STG-1.14`
- `STG-2.1`, `STG-2.2`
- `STG-DE-2.1` through `STG-DE-2.3`

Likely future support: morphology, part-of-speech tagging, compound analysis, abbreviation tracking, terminology consistency across a document.

### Verbs and modality

- `STG-3.1` through `STG-3.7`
- `STG-DE-3.1` through `STG-DE-3.3`

Likely future support: verb-form analysis, passive detection, separable-verb distance, modal classification, nominal-style detection.

### Sentence structure

- `STG-4.1` through `STG-4.5`
- `STG-DE-4.1` through `STG-DE-4.5`

Likely future support: dependency parsing, subordinate-clause depth, pronoun-reference review, negation scope, pronominal-adverb review.

### Procedures

- `STG-5.2` through `STG-5.5`

`STG-5.1` is currently deterministic. The remaining procedure rules require instruction-structure and modality analysis.

### Descriptions

- `STG-6.1`, `STG-6.2`, `STG-6.4`, `STG-6.5`, `STG-6.6`

`STG-6.3` is currently deterministic. Paragraph sentence count (`STG-6.6`) is a candidate for the next deterministic implementation.

### Safety

- `STG-7.1` through `STG-7.3`

These require a safety-text model or explicit structured markup before strict automation is reliable.

### Punctuation and counting

- `STG-8.2` through `STG-8.7`
- `STG-DE-8.1`

`STG-8.1` currently has partial deterministic support for semicolons. Slash combinations and parenthesis/list rules are candidates for deterministic checks.

### Writing practices and recommendations

- `STG-9.1`, `STG-9.2`, `STG-9.3`
- `STG-GR-1` through `STG-GR-8`
- `STG-DE-9.1`, `STG-DE-9.2`

`STG-9.4` currently has partial deterministic support through project preferred terminology. Many prohibited fillers and vague expressions are also caught indirectly through `STG-1.1` dictionary routing.

## Quality rule

A validator feature must not emit a rule ID unless that ID exists in `rules/rule-index.yaml`.

Regression tests enforce this for currently implemented checks. Future rule implementations must add:

1. at least one positive case;
2. at least one negative case;
3. the expected published rule ID;
4. the expected severity;
5. a case that guards against a known false positive when applicable.

## Target for v0.5

The v0.5 target is not automatic enforcement of all 75 entries. The target is:

- full inventory of automation status;
- comprehensive tests for every implemented deterministic check;
- no invalid rule IDs;
- explicit distinction between deterministic, heuristic, semantic, and human-review findings;
- prioritized implementation of additional low-risk deterministic rules.
