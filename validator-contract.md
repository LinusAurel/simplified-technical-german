# STG-DE validator contract

## 1. Purpose

This file defines a practical contract for linters, authoring tools, LLM reviewers, CI gates, and editor integrations.

## 2. Input

Minimum input:

```yaml
text: "..."
text_type: procedure | description | safety | note
locale: de-DE
conformance_target: STG-R | STG-T | STG-C-core | STG-C
```

Recommended additional input:

```yaml
terminology_sources:
  - project-terms.yaml
locked_spans:
  - start: 120
    end: 145
    type: ui_label
safety_profile: project-safety-v2
instruction_profile: formal-sie-imperative
```

## 3. Output

```yaml
status: pass | fail | needs_input
metrics:
  sentences: 8
  max_words_in_sentence: 19
  passive_candidates: 1
  terminology_unknown: 0
diagnostics:
  - rule: STG-3.6
    severity: error
    confidence: 0.97
    span: "Die Sicherung wird entfernt."
    message: "Passive instruction."
    proposed_fix: "Entfernen Sie die Sicherung."
```

## 4. Severity

- `error`: deterministic mandatory violation or high-confidence semantic violation.
- `warning`: heuristic finding that requires review.
- `info`: non-mandatory recommendation.
- `needs_input`: safe rewrite requires domain, safety, or modality information.

## 5. Recommended rule pipeline

### Phase A — protected spans

Identify and freeze:

- identifiers,
- formulas,
- part numbers,
- UI labels,
- proper names,
- quoted/legal text,
- document titles.

### Phase B — segmentation and counts

Check:

- sentence boundaries,
- list structure,
- 20/25-word limits,
- paragraph sentence count,
- semicolons,
- parentheses rules.

### Phase C — deterministic lexical checks

Check:

- prohibited terms/phrases,
- unapproved abbreviations,
- locale spelling profile where tooling permits,
- known project terminology variants.

### Phase D — syntax heuristics

Detect:

- passive candidates (`werden` + Partizip II),
- long sentence brackets from separable verbs,
- nominalizations and function-verb constructions,
- nested subordinate clauses,
- `man`,
- ambiguous modal verbs,
- ambiguous negation.

A parser must distinguish state constructions such as `ist geschlossen` from action passives where possible.

### Phase E — semantic/domain checks

Check:

- one term per concept,
- pronoun antecedent ambiguity,
- technical-term approval,
- technical-verb approval,
- modality intent,
- safety consequence and category consistency.

## 6. Compound complexity heuristic

For new/unapproved compounds, a validator may split a noun using a compound splitter. Emit a warning when:

- more than three meaningful lexical components are detected, or
- more than one plausible decomposition exists, or
- the compound is longer than 30 characters and is not an approved term.

This is a heuristic, not a mandatory lexical rule for official terms.

## 7. Passive detection

High-value patterns:

- `werden` + Partizip II → likely Vorgangspassiv,
- modal + Partizip II + `werden` → complex passive,
- `sein` + Partizip II → state/adjective candidate, not automatically a violation.

In a `procedure`, a passive candidate should normally be an error. In a `description`, it is a warning unless the agent/actor is clearly known.

## 8. Modality detection

Flag:

- `soll`, `sollen`, `sollte`, `sollten`,
- `müsste`, `müssten`,
- `könnte`, `könnten`,
- `gegebenenfalls`, `ggf.`.

The tool must not auto-convert these to `muss` or an imperative without knowing the intended force.

## 9. Pronoun resolution

If a third-person pronoun or demonstrative has more than one plausible antecedent of compatible number/gender in the preceding sentence or clause, emit a warning or error.

Prefer noun repetition in proposed fixes.

## 10. Unknown words

For `STG-R`, an unknown general word is not automatically an error unless it violates a specific rule.

For `STG-T`, unknown technical-looking terms are errors or `needs_input` until approved.

For `STG-C-core`, every non-locked lexical item must resolve to an approved/restricted central v0.4 entry or an approved technical entry. Restricted entries must satisfy their restrictions. Unknown general words produce `needs_input`/`NEEDS_LEXICON_REVIEW`.

For `STG-C`, every non-locked lexical item must resolve to a future broad, human-reviewed central or technical entry. v0.4 does not claim general `STG-C` certification.


## 11. Lexical resolution in v0.4

Recommended resolution order for `STG-C-core`:

1. locked/protected spans,
2. approved project terminology,
3. longest approved/prohibited phrase patterns,
4. German contraction expansion from `dictionary/contractions.yaml`,
5. case-sensitive lexical distinctions (`Sie` vs `sie`),
6. canonical central lemma with correct part of speech and approved meaning,
7. declared surface forms and controlled inflections, with canonical-lemma precedence on collisions,
8. deterministic morphology and separable-verb reconstruction,
9. prohibited/review list at the resolved lemma,
10. unknown -> `NEEDS_LEXICON_REVIEW`.

A `restricted` central word can pass only when its restriction is satisfied. A validator must not turn `review_required` into an automatic pass.

Lexical lookup is lemma-based. Apply morphological analysis before lookup and reconstruct separable verb lemmas where possible; see `dictionary/MORPHOLOGY.md`.


## 12. Pronominal adverbs

Detect German pronominal adverbs such as `dabei`, `dazu`, `daraus`, `davon`, `darüber`, `dafür`, and `hierfür`. If the form can refer to more than one object, action, cause, purpose, or preceding proposition, return `NEEDS_REFERENCE_INPUT` under STG-DE-4.5. Do not auto-select an antecedent.

## 13. Corpus-development mode

A development tool may classify unresolved tokens as `MORPHOLOGY_CANDIDATE`, `LEXICAL_NOUN_CANDIDATE`, or `PROTECTED_TOKEN_CANDIDATE`. These labels are triage states and are not conformance passes. See `tools/corpus_validate.py`.
## 14. German noun-candidate routing

Do not infer `technical noun` from capitalization. All German nouns are capitalized. An unknown capitalized token is a `LEXICAL_NOUN_CANDIDATE` until it resolves to the central lexicon, approved project/domain terminology, a protected span, or review.

For declared noun plurals, accept only lexicon-declared plural forms. Before applying a plural alias, check whether the surface form is itself a canonical lemma. `Daten` must resolve to `DE-NOU-daten` in the technical-data meaning rather than being consumed by the `Datum` plural alias.

