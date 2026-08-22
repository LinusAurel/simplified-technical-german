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
