# Section 1 — Wörter und Terminologie

## STG-1.1 — Zulässiger Wortschatz

**Level:** `MUST`

Use only words that belong to at least one approved class:

1. a word in the central STG lexicon,
2. an approved technical noun,
3. an approved technical verb,
4. locked external text where changing the text is not permitted.

Unknown general-language words are not automatically technical terms.

**Nicht STG**

> Die Komponente ist irgendwie falsch positioniert.

**STG**

> Die Komponente ist in der falschen Position.

## STG-1.2 — Wortart

**Level:** `MUST`

Use an approved lexical item only with its approved word class. German derivational morphology does not automatically create a new approved entry.

If `Prüfung` is approved as a noun, this does not automatically approve `prüfen` as a verb. Each lexeme/word class combination is a separate dictionary entry unless the lexicon explicitly links them.

## STG-1.3 — Kontrollierte Bedeutung

**Level:** `MUST`

Use an approved word only with an approved meaning. If the intended meaning is not approved, select another approved word or rewrite the sentence.

**Example:** If `lösen` is approved only for releasing a mechanical connection, do not use it for `ein Problem lösen` unless that second meaning is separately approved.

## STG-1.4 — Zulässige Flexionsformen

**Level:** `MUST`

Use only grammatically valid forms that the dictionary schema permits for the entry.

For German, the lexicon may specify:

- noun gender and plural,
- adjective inflection class and comparison policy,
- verb person/number forms,
- imperative form,
- participle forms,
- separable prefix,
- auxiliary selection where relevant.

A generated form is permitted only if it follows the declared morphology and the rule set does not prohibit its syntactic use.

## STG-1.5 — Technische Substantive

**Level:** `MUST`

A technical noun is a term for a defined concept in a technical subject field. Use a word or multiword term as a technical noun only when it fits an approved technical-noun category and is accepted by the applicable terminology source.

The category model is in `dictionary/technical-nouns.yaml`.

## STG-1.6 — Nicht-zentrale Wörter als technische Terme

**Level:** `MUST`

A word that is not approved in the central lexicon may be used only when it is part of an approved technical term or protected external designation.

Do not use the existence of a word inside one technical term as permission to use that word with its ordinary general-language meaning.

## STG-1.7 — Technisches Substantiv ist nicht automatisch Verb

**Level:** `MUST`

Do not convert a technical noun into a verb unless the verb itself is approved as a technical verb or central lexical entry.

**Nicht STG**

> Ölen Sie die Führung.

**STG**

> Tragen Sie Öl auf die Führung auf.

If `ölen` is explicitly approved as a project technical verb, the project entry takes precedence.

## STG-1.8 — Offizielle technische Benennungen

**Level:** `MUST`

Use the technical designation approved by the company, product, industry, contract, drawing, parts catalog, data model, or terminology database. Do not replace an official designation merely to make it shorter.

## STG-1.9 — Neue technische Benennungen kurz halten

**Level:** `SHOULD`

When no approved technical designation exists, create the shortest designation that uniquely identifies the concept.

For a newly created German compound, prefer no more than three meaningful lexical components when this is technically sufficient. If more components are necessary, apply the compound rules in Section 2.

Do not remove differentiating information that is necessary for technical correctness.

## STG-1.10 — Keine regionale Sprache, Umgangssprache oder Jargon

**Level:** `MUST_NOT`

Do not use regional expressions, colloquial wording, workshop slang, internet slang, or unexplained jargon as general technical language.

Project-specific technical terms are permitted only after terminology approval.

**Nicht STG**

> Wenn das Update fehlschlägt, darf das Gerät nicht gebrickt werden.

**STG**

> Wenn das Update fehlschlägt, darf das Gerät nicht funktionsunfähig werden.

Better still, state the exact failure condition when known.

## STG-1.11 — Ein Konzept, eine Benennung

**Level:** `MUST`

Use the same approved technical designation every time you refer to the same concept within the defined document scope.

Do not alternate between synonyms such as `Steuergerät`, `Controller`, and `Regler` for the same component unless the terminology model defines them as different concepts.

## STG-1.12 — Technische Verben

**Level:** `MUST`

A technical verb denotes a defined technical process or action in a subject field. Use a technical verb only when:

1. the action has a domain-specific meaning,
2. the verb is approved in the applicable terminology source,
3. a simpler central STG verb would not express the same technical action precisely.

The category model is in `dictionary/technical-verbs.yaml`.

## STG-1.13 — Technisches Verb ist nicht automatisch Substantiv

**Level:** `MUST`

Do not nominalize an approved technical verb and treat the result as an approved technical noun unless the noun is separately approved.

This rule is important in German because productive nominalization can create formally valid but uncontrolled terms.

**Nicht STG**

> Das Reamen des Lochs erfolgt danach.

**STG**

> Reiben Sie danach das Loch auf.

If `Reiben` is an official process name in a heading, approve it as a technical noun entry.

## STG-1.14 — Deutsche Standardschreibung

**Level:** `MUST`

Use the declared German spelling profile. The default profile `de-DE` follows the 2024 official German orthography.

For `de-DE`:

- preserve `ä`, `ö`, `ü`, and `ß` where standard spelling requires them,
- do not replace them with `ae`, `oe`, `ue`, or `ss` unless a technical identifier or system limitation requires it,
- capitalize German nouns,
- preserve the official spelling of product names, identifiers, UI strings, and quoted text.

A project may declare `de-CH` or another approved profile, but one document should not mix profiles.
