# STG-DE dictionary and morphology guide

Generated from canonical repository documentation.


---

<!-- source: dictionary/README.md -->

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

---

<!-- source: dictionary/MORPHOLOGY.md -->

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

---

<!-- source: dictionary/DECISIONS.md -->

# STG-DE lexical decisions — through v0.4

## Status

This file records high-impact lexical choices accumulated through the v0.4 authoring core. The entries are **provisional** until review by German technical-writing and terminology specialists.

The source standard uses a controlled dictionary in which approved words have a specified word class and approved meaning, while non-approved words can point to approved alternatives or a different sentence construction. STG-DE keeps that architecture but does **not** translate the English dictionary one-to-one.

## Release objective

v0.3 defines an enforceable **authoring core** for common German technical prose. It is intended to make generation and rewriting deterministic enough for agents and validators while leaving domain terminology to project terminology sources.

### Selection order

1. Preserve official technical terminology.
2. Prefer one short, common German general-language lemma for one intended meaning.
3. Split meanings when German has a more precise lexical choice.
4. Prohibit stylistic synonyms when they add no technical distinction.
5. Mark a word `restricted` when it is useful but needs context or an explicit criterion.
6. Send domain-specific manufacturing, legal, medical, military, and scientific verbs to project terminology unless they are broadly necessary.

## Important lexical decisions

### `verwenden` instead of `benutzen`, `nutzen`, `gebrauchen`

`verwenden` is the preferred general verb for using a tool, material, component, or aid. `anwenden` is reserved for methods, rules, and procedures. This keeps two useful concepts separate while removing stylistic synonym variation.

### `prüfen` versus `testen` versus `untersuchen`

- `prüfen`: determine whether an explicit condition or requirement is satisfied.
- `testen`: execute a defined test against criteria.
- `untersuchen`: systematically look for damage, defects, or specified features.

### `erhöhen` / `verringern` versus `steigen` / `sinken`

Use the transitive pair when an actor changes a value. Use the intransitive pair when the value changes as a process result.

### `einbauen` versus `installieren`

Use `einbauen` for mechanical/electrical components in an installation position. Use `installieren` primarily for software or when official terminology defines installation of a whole system.

### `warten`

The temporal verb `warten` is permitted. The maintenance meaning is intentionally not part of the central lexicon because the homonym is highly ambiguous. Use approved project terminology for maintenance, for example `instand halten` if the project approves it.

### `sichern`

The general verb is not approved because it can mean fastening, data backup, locking, safeguarding, or making safe. Use the precise verb: `befestigen`, `speichern`, `verriegeln`, `schützen`, or a project technical term.

### `können`, `dürfen`, `müssen`

- `können`: capability or factual possibility.
- `dürfen`: permission; `nicht dürfen`: prohibition.
- `müssen`: explicit requirement.

Conditional or tentative forms such as `könnte`, `müsste`, and `sollte` are not part of controlled mandatory wording.

### Vague qualifiers

Words such as `ordnungsgemäß`, `geeignet`, `ausreichend`, `vorsichtig`, and `zeitnah` are prohibited or review-required because they often replace a missing criterion. A validator should request the criterion rather than invent it.

## Unknown-word policy

For `STG-C-core`, a non-locked general-language token that does not resolve to this lexicon is **not automatically a synonym candidate**. The agent must:

1. check whether it is approved project terminology,
2. check whether it is a protected name/label/identifier,
3. check the prohibited/rewrite list,
4. otherwise return `NEEDS_LEXICON_REVIEW`.

This is intentionally conservative.


## v0.3 corpus-driven decisions

### Corpus frequency is not approval

A frequent word in ordinary technical German can still be unsuitable for controlled German. Corpus evidence creates a review obligation; it does not override precision rules. This is why frequent forms such as `sowie`, `beziehungsweise`, vague qualifiers, and impersonal constructions remain prohibited or review-required.

### Contractions are normalized, not prohibited

German forms such as `im`, `am`, `beim`, `vom`, `zum`, and `zur` are regular grammatical contractions. Treating them as independent unknown words created false lexical gaps in v0.2. v0.3 expands them for lookup while preserving the surface text.

### Controlled connector set

Corpus analysis showed substantial stylistic variation in logical connectors. v0.3 prefers a smaller explicit set:

- addition: `und`
- contrast: `aber`
- sequence: `dann` / `danach`
- result: `deshalb`
- condition: `wenn`
- cause: `weil`
- earlier event: `bevor`
- simultaneous period: `während`

Consequently, `sowie`, `jedoch`, `daher`, and `anschließend` are normalized to controlled alternatives when meaning is preserved.

### Pronominal adverbs

`dabei`, `dazu`, `daraus`, `davon`, `darüber`, `dafür`, and `hierfür` are useful German forms but can compress both an antecedent and a semantic relation. They are therefore `review_required` in the strict core and governed by STG-DE-4.5.

### Cross-domain direct verbs

The public corpus evidence supported adding narrow central meanings for verbs that occur across technical domains and describe concrete actions or relations. Examples include `anschließen`, `abziehen`, `abkühlen`, `verschließen`, `beheben`, `bereitstellen`, `enthalten`, and `entsprechen`.

The same evidence did **not** justify moving product-specific or engineering-domain verbs into the central lexicon. Those remain project technical verbs.

### `bestehen`

Only the composition meaning is centrally controlled: `X besteht aus Y`. Other meanings of `bestehen` (for example succeeding in an examination, continuing to exist, or insisting on something) are outside the central entry.

### `lassen`

`lassen` is restricted to constructions where the reader allows an explicitly named physical or automatic process to continue, for example cooling. It must not be used to hide the responsible actor.

---

# v0.4 corpus decisions

## D-04-01 — Declared noun plurals are controlled inflections

**Decision:** A noun's declared plural is resolved as a controlled inflection without requiring a second dictionary entry.

**Reason:** The v0.3 validator incorrectly routed ordinary declared plurals such as `Informationen`, `Gefahren`, `Schritte`, and `Geräte` as unknown/term candidates. This is a validator gap, not a vocabulary gap.

## D-04-02 — Canonical lemma wins over an inflection alias

**Decision:** Before accepting an inflection alias, check whether that surface form is itself a canonical lemma.

**Reason:** `Datum` declares plural `Daten`, but technical German uses `Daten` as an independent concept for technical information/data. v0.4 therefore adds `DE-NOU-daten` and prevents the plural alias from overriding it.

## D-04-03 — Capitalization does not establish terminology status

**Decision:** Unknown capitalized words are routed as `LEXICAL_NOUN_CANDIDATE`, not `TECHNICAL_TERM_CANDIDATE`.

**Reason:** All German nouns are capitalized. Treating capitalization as terminology evidence systematically over-classified ordinary general nouns.

## D-04-04 — Cross-domain frequency is necessary evidence, not sufficient approval

**Decision:** Frequent words enter the central lexicon only when a narrow controlled meaning can be specified.

**Approved/restricted examples:** `Betriebsanleitung`, `Fachpersonal`, `Verletzung`, `Produkt`, `Version`, `Daten`, `lesen`, `wählen`.

**Review-required despite frequency:** `führen`, `bieten`, `berücksichtigen`, `gewährleisten`.

The latter group is too polysemous or abstract for unconditional automated acceptance.
