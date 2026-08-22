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

## Implemented coverage

| Rule | Current automated check | Coverage | Severity |
|---|---|---|---|
| `STG-1.1` | Matches entries in `dictionary/prohibited-words.yaml` and returns the configured status. | partial | error/review |
| `STG-DE-4.3` | Detects standalone `man` as an indefinite technical actor. | deterministic | error |
| `STG-5.1` | Counts words in procedure mode and flags sentences above 20 words. | deterministic | error |
| `STG-6.3` | Counts words in description/default mode and flags sentences above 25 words. | deterministic | error |
| `STG-6.6` | Counts sentences in descriptive prose paragraphs and flags more than six. | deterministic | error |
| `STG-8.1` | Flags semicolons in prose lines. | partial | error |
| `STG-DE-8.1` | Detects a conservative set of known ambiguous slash forms such as `und/oder`; protected URLs/code are excluded. | partial | warning |
| `STG-9.4` | Enforces `preferred_terms` from `.stg-de.yaml`. | partial | error |

The validator also reports unknown central-lexicon surface forms when `--lexicon-report` is enabled. Unknown words are review candidates, not automatic violations.

## Test policy

Every implemented validator path must have regression coverage. The suite must include, where applicable:

1. a violating example;
2. a non-violating example;
3. the expected published rule ID;
4. the expected severity/result;
5. a false-positive guard;
6. a global assertion that every emitted rule ID exists in `rules/rule-index.yaml`.

The current suite includes explicit false-positive guards for `man` vs `Mann`, URLs vs slash forms, paragraph boundaries, and compliant sentence lengths.

## Rules not yet mechanically proven

### Vocabulary and terminology

Most of `STG-1.2` through `STG-1.14`, `STG-2.1`, `STG-2.2`, and `STG-DE-2.1` through `STG-DE-2.3` still need morphology, part-of-speech analysis, compound analysis, abbreviation tracking, or document-level terminology state.

### Verbs and modality

`STG-3.1` through `STG-3.7` and `STG-DE-3.1` through `STG-DE-3.3` require verb-form analysis, passive detection, separable-verb distance, modal classification, or nominal-style detection. These should not be promoted to deterministic errors until measured precision is acceptable.

### Sentence structure

Most of Section 4 remains semantic or parser-assisted. `STG-DE-4.3` is the deterministic exception. Future work includes subordinate-clause depth, pronoun-reference review, negation scope, and pronominal-adverb review.

### Procedures

`STG-5.1` is deterministic. `STG-5.2` through `STG-5.5` require instruction-structure, condition, and modality analysis.

### Descriptions

`STG-6.3` and `STG-6.6` are deterministic. `STG-6.1`, `STG-6.2`, `STG-6.4`, and `STG-6.5` are discourse-level rules.

### Safety

`STG-7.1` through `STG-7.3` require explicit safety structure or high-confidence semantic analysis before strict automation is reliable.

### Punctuation and counting

`STG-8.1` has partial semicolon support. `STG-DE-8.1` has conservative slash-pattern support. The remaining Section 8 rules need structured list/parenthesis handling and more exact protected-token counting.

### Writing practices and recommendations

`STG-9.4` has partial project-terminology support. Many fillers and vague expressions are caught indirectly through `STG-1.1`. The remaining rules and recommendations should stay review-oriented until their semantics can be measured.

## Quality rule

A validator feature must not emit a rule ID unless that ID exists in `rules/rule-index.yaml`.

No validator feature should be labeled `deterministic` merely because it uses a regular expression. The classification means the implemented subset has a clear, mechanically testable condition with intentionally bounded scope.

## v0.5 acceptance target

v0.5 does not require automatic enforcement of all 75 rules/recommendations. It requires:

- a complete automation inventory;
- regression tests for every implemented check;
- no invalid rule IDs;
- clear separation of error, warning, review, and unresolved semantic cases;
- additional low-risk deterministic checks only when false-positive risk is bounded;
- measured evaluation against a held-out corpus before parser/LLM-assisted checks are promoted.
