# STG-DE morphology and lexical resolution — v0.4

`STG-C-core` is defined at the **lemma + word class + controlled meaning** level. A validator must not require every inflected German surface form to be a separate dictionary entry.

## Resolution order

1. Protected/locked spans
2. Approved project/domain terminology
3. Longest approved/prohibited phrase match
4. Standard contraction expansion
5. Case-sensitive lexical lookup
6. Exact canonical central lemma or declared `surface_forms`
7. Declared controlled inflection
8. Deterministic morphological analysis and separable-verb reconstruction
9. Prohibited/review lookup at the resolved lemma
10. Otherwise `NEEDS_LEXICON_REVIEW`

Approximate spelling or stemming is not a normative substitute for lemmatization.

## Canonical-lemma precedence

If an inflected form of one entry is also the canonical lemma of another entry, the canonical lemma takes precedence.

### Required example: `Datum` / `Daten`

German permits `Daten` as the plural of `Datum`. Technical German also uses `Daten` as an independent lexical concept meaning technical information/data.

Therefore:

```text
Daten  -> DE-NOU-daten      # technical data/information
Datum  -> DE-NOU-datum      # calendar date
```

A validator must **not** accept a naive `Datum -> Daten` plural mapping before checking whether `Daten` is itself a canonical entry.

## German contractions

Standard preposition+article contractions are grammar, not technical vocabulary. Normalize forms such as:

- `im` -> `in` + `dem`
- `am` -> `an` + `dem`
- `beim` -> `bei` + `dem`
- `vom` -> `von` + `dem`
- `zum` -> `zu` + `dem`
- `zur` -> `zu` + `der`

Expansion is for lexical analysis only. Do not rewrite a correct, unambiguous surface form merely to expose the components.

## Nouns

An approved noun permits its grammatical case forms and its explicitly declared plural unless a restriction says otherwise.

The development validator counts the **declared plural** as `CENTRAL_INFLECTION`. It does not invent unlisted plurals.

Unknown capitalized words are not automatically technical terms. German capitalizes ordinary nouns; an unresolved noun must resolve to a central entry, project terminology, a protected name/identifier, or review.

## Case-sensitive forms

Resolve formal reader forms before case folding:

- `Sie`, `Ihnen`
- `Ihr`, `Ihre`, `Ihren`, `Ihrem`, `Ihrer`, `Ihres`

Third-person `sie` / `ihr` are separate restricted entries and require an unambiguous antecedent.

## Articles and determiners

Common inflected forms are stored in `surface_forms`. Resolve them to their controlled determiner/article entry before syntactic validation.

## Verbs

A normative validator should lemmatize finite and non-finite forms before dictionary lookup.

For separable verbs, reconstruct the lemma from the clause:

- `Schalten Sie das Gerät ein.` -> `einschalten`
- `Die Anzeige zeigt den Wert an.` -> `anzeigen`
- `Stellen Sie den Datensatz bereit.` -> `bereitstellen`
- `Legen Sie den Grenzwert fest.` -> `festlegen`

A finite stem such as `stellt` must not be judged in isolation when a separable prefix later in the clause can change the lemma.

## Adjectives

Regularly inflected adjective forms resolve to the approved base lemma. Comparative and superlative forms require explicit permission or a rule/entry that allows the comparison. Do not assume every approved adjective can be compared meaningfully.

## Phrases

Resolve multi-token entries before single-token lookup. Entries containing `...` require a syntactic pattern rather than literal substring matching.

## Development heuristics

`tools/corpus_validate.py` may use the German Snowball stemmer to emit `MORPHOLOGY_CANDIDATE`. This class is evidence for curation only and **never counts as normative conformance**.
