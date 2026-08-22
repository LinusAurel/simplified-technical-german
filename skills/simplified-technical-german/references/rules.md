# STG-DE writing rules

Generated from the canonical top-level `rules/` directory.

---

<!-- source: rules/01-words.md -->

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

---

<!-- source: rules/02-compounds-and-terms.md -->

# Section 2 — Komposita und Mehrwortterme

German technical language relies heavily on compounds. STG-DE therefore defines dedicated rules for their controlled use.

## STG-2.1 — Begrenze die semantische Dichte technischer Benennungen

**Level:** `MUST`

A newly created technical designation must be understandable without having to infer several possible internal relations between components.

Use these methods in order:

1. Use the approved official term if one exists, regardless of length.
2. For a new term, prefer at most three meaningful lexical components.
3. If a longer designation is necessary, use a grammatically clear phrase or a structured compound.
4. Use a hyphen when it materially clarifies the boundaries of a long compound or when the official orthography requires or permits it for clarity.
5. Do not create a chain of modifiers only to keep the expression to one orthographic word.

**Nicht STG**

> Kraftstoffhauptpumpenausgangsdruckprüfanschlussabdeckung

**STG**

> Abdeckung des Prüfanschlusses am Ausgang der Hauptkraftstoffpumpe

If the long compound is the official part name, keep the official name and define a controlled shorter form under STG-2.2.

## STG-2.2 — Lange offizielle Benennung zuerst vollständig

**Level:** `MUST`

When an official technical designation is long:

1. write the full official designation at first occurrence,
2. define an approved short form or abbreviation if useful,
3. use only that short form afterwards within the declared scope.

Do not introduce several short forms for the same term.

**Example**

> Die **zentrale Steuerung der Kühlmittelpumpe (Kühlmittelsteuerung)** überwacht den Druck. Die **Kühlmittelsteuerung** schaltet die Pumpe bei Überdruck aus.

## STG-DE-2.1 — Deutsche Komposita als Terminologieobjekte

**Level:** `MUST`

Treat a German compound as a terminology object, not merely as a concatenation of approved general words.

For each approved compound, a terminology database should store:

- canonical spelling,
- concept identifier,
- grammatical gender,
- plural form,
- approved short form if any,
- decomposition into meaningful components when useful for validators.

Approval of `Druck`, `Regler`, and `Ventil` does not automatically approve `Druckregelventil` as a technical term.

## STG-DE-2.2 — Bindestriche nicht als Komplexitäts-Trick verwenden

**Level:** `MUST_NOT`

Do not use hyphens solely to make a complex designation appear shorter for the word-count rule. A hyphenated compound counts as one orthographic word, but it still receives a compound-complexity check.

## STG-DE-2.3 — Abkürzungen sparsam und stabil verwenden

**Level:** `MUST`

Use an abbreviation only when it is official or explicitly introduced. At first occurrence, write the full term followed by the abbreviation in parentheses unless the abbreviation is universally required by the project.

After introduction, do not alternate between multiple abbreviations or between several shortened forms.

---

<!-- source: rules/03-verbs.md -->

# Section 3 — Verben

## STG-3.1 — Nur freigegebene Verbformen

**Level:** `MUST`

Use only verb forms permitted by the lexical entry and by this section. German conjugation is productive, but grammatical availability does not imply STG approval.

## STG-3.2 — Kontrollierte Tempora und Modi

**Level:** `MUST`

Use these default forms:

### Procedures

- formal imperative: `Entfernen Sie ...`
- infinitive only inside an approved infinitive construction, not as the default instruction style.

### Descriptions

- Präsens for current states, functions, and general technical facts,
- Präteritum or Perfekt only when a past event must be reported,
- present tense plus explicit time expression for future scheduled states when possible.

Avoid Futur I when Präsens is equally clear.

**Nicht STG**

> Der Test wird morgen durchgeführt werden.

**STG**

> Das Personal prüft das System morgen.

Or, if the actor is irrelevant but the schedule is the point:

> Der Test ist für morgen geplant.

## STG-3.3 — Partizip II für Zustand oder Attribut

**Level:** `MUST`

A past participle may be used as an adjective or state description when it describes a condition and not an omitted action.

**STG**

> Die Abdeckung ist geschlossen.

**STG**

> Prüfen Sie die gereinigte Fläche.

If the sentence describes who performs an action, use active voice instead.

## STG-3.4 — Keine unnötigen Hilfsverbketten

**Level:** `MUST_NOT`

Do not use complex auxiliary/modal constructions when a direct verb expresses the same information.

**Nicht STG**

> Die Dichtung muss ersetzt worden sein, bevor die Prüfung durchgeführt werden kann.

**STG**

> Ersetzen Sie die Dichtung vor der Prüfung.

If the completed state itself is the requirement:

> Vor der Prüfung muss die Dichtung ersetzt sein.

## STG-3.5 — Keine englische `-ing`-Sonderregel; kontrolliere deutsche Nominalisierung

**Level:** `MUST`

German has no direct equivalent of the English `-ing` ambiguity. The corresponding German risk is productive nominalization.

Use nominalizations only when they denote an approved technical concept, document heading, process name, or result. For actions in sentences, prefer a finite or imperative verb.

**Nicht STG**

> Nach Durchführung der Reinigung erfolgt die Prüfung der Oberfläche.

**STG**

> Reinigen Sie die Oberfläche. Prüfen Sie danach die Oberfläche.

## STG-3.6 — Aktiv bevorzugen

**Level:** `MUST`

Use active voice when the agent is known or can be stated correctly.

In procedures, use the imperative instead of passive instructions.

**Nicht STG**

> Die Sicherung wird entfernt.

**STG**

> Entfernen Sie die Sicherung.

In descriptions, passive voice is permitted only when the agent is genuinely unknown, irrelevant to the technical meaning, or intentionally omitted by an applicable legal/publication rule.

Do not confuse a state with passive voice:

> Die Sicherung ist entfernt.

This can be a valid state description if `entfernt` describes the required condition.

## STG-3.7 — Handlungen mit direkten Verben ausdrücken

**Level:** `MUST`

When an approved direct verb expresses the action, use it instead of a noun-heavy construction.

**Nicht STG**

> Führen Sie eine Prüfung des Steckers durch.

**STG**

> Prüfen Sie den Stecker.

**Nicht STG**

> Nehmen Sie eine Einstellung des Drucks vor.

**STG**

> Stellen Sie den Druck ein.

## STG-DE-3.1 — Trennbare Verben kontrollieren

**Level:** `SHOULD`

Separable verbs are permitted when they are the approved technical/general verb. Keep the sentence bracket short.

If more than about 12 words occur between the finite verb and its separable prefix, rewrite the sentence unless the terminology or syntax makes the longer bracket clearly preferable.

**Schwer lesbar**

> Schalten Sie nach dem Ende der automatischen Kalibrierung die externe 24-V-Stromversorgung am hinteren Bedienfeld vollständig aus.

**Besser**

> Schalten Sie nach der Kalibrierung die externe 24-V-Stromversorgung aus.

## STG-DE-3.2 — Modalität eindeutig kodieren

**Level:** `MUST`

Use modality consistently:

| Meaning | STG form |
|---|---|
| Mandatory action in a procedure | Imperative |
| Mandatory state/requirement | `muss` |
| Prohibition | `darf nicht` or negative imperative, depending text type |
| Permission | `darf` |
| Physical/technical capability or factual possibility | `kann` |
| Recommendation | explicit recommendation wording only when recommendations are permitted |

Do not use `soll`, `sollte`, or `müsste` when the intended force is mandatory, permitted, or merely possible.

**Ambiguous**

> Die Schraube sollte ersetzt werden.

Possible STG rewrites depend on intent:

> Ersetzen Sie die Schraube.  
> Die Schraube muss ersetzt sein.  
> Wir empfehlen, die Schraube zu ersetzen.

If the intended modality is unknown, return `NEEDS_MODALITY_INPUT`.

## STG-DE-3.3 — `werden` restriktiv verwenden

**Level:** `SHOULD_NOT`

Avoid `werden` when it only creates passive voice or Futur I. It may be used for an actual change of state when that meaning is clear.

**STG**

> Das Gehäuse wird warm.

**Nicht bevorzugt**

> Die Leitung wird vom Steuergerät überwacht.

**STG**

> Das Steuergerät überwacht die Leitung.

---

<!-- source: rules/04-sentences.md -->

# Section 4 — Sätze

## STG-4.1 — Kurze, eindeutige Sätze

**Level:** `MUST`

Write short sentences with one primary proposition. In descriptive text, each sentence should have one main topic. Do not compress several independent facts into one sentence.

**Nicht STG**

> Der Sensor sitzt am Gehäuse, misst den Druck und sendet die Werte an das Steuergerät, das bei einem Grenzwertfehler die Pumpe abschaltet.

**STG**

> Der Sensor sitzt am Gehäuse. Der Sensor misst den Druck. Das Steuergerät empfängt die Messwerte. Bei einem Grenzwertfehler schaltet das Steuergerät die Pumpe aus.

## STG-4.2 — Keine bedeutungstragenden Auslassungen

**Level:** `MUST_NOT`

Do not omit a subject, object, verb, article, or reference when the omission can create ambiguity. Do not use telegraphic fragments as normal running text.

**Nicht STG**

> Schalter auf EIN.

**STG**

> Stellen Sie den Schalter auf EIN.

Headings, table cells, labels, and other controlled fragments may be exempt under their content model.

## STG-4.3 — Vertikale Listen für komplexe Aufzählungen

**Level:** `MUST`

Use a vertical list when a sentence contains many parallel items, conditions, or actions.

Rules:

- introduce the list with a grammatically complete lead-in and colon,
- keep all list items grammatically parallel,
- do not mix procedural commands and descriptive statements in the same list,
- use a full stop for a list item that is a complete sentence,
- do not use commas or semicolons as end punctuation merely to chain list items.

## STG-4.4 — Logische Verknüpfungen explizit machen

**Level:** `MUST`

Use stable connecting words when the logical relation between sentences matters.

Preferred controlled connectors include:

- `und` — addition,
- `aber` — contrast,
- `dann` / `danach` — sequence,
- `deshalb` — result,
- `weil` — cause,
- `wenn` — condition,
- `bevor` — earlier event,
- `während` — simultaneous period.

Do not vary connectors merely for style.

## STG-4.5 — Artikel und Demonstrativa eindeutig verwenden

**Level:** `MUST`

Use articles and demonstratives according to German grammar and to make reference status clear. Ensure agreement in case, gender, and number.

Do not use a bare demonstrative pronoun when more than one antecedent is possible. Prefer a demonstrative adjective plus noun or repeat the technical noun.

**Ambiguous**

> Entfernen Sie den Sensor aus dem Halter. Dieser ist beschädigt.

**STG**

> Entfernen Sie den Sensor aus dem Halter. Der Sensor ist beschädigt.

or

> Entfernen Sie den Sensor aus dem Halter. Der Halter ist beschädigt.

## STG-DE-4.1 — Nebensatzverschachtelung begrenzen

**Level:** `MUST`

Do not nest subordinate clauses inside subordinate clauses in procedural or safety text. In descriptive text, one level of subordination is the default maximum.

Rewrite deeper structures as separate sentences.

## STG-DE-4.2 — Pronomen nur mit eindeutigem Bezug

**Level:** `MUST`

A pronoun must have exactly one plausible antecedent in the local context. If it can refer to more than one noun, repeat the noun.

**Ambiguous**

> Verbinden Sie den Sensor mit dem Adapter, wenn er trocken ist.

**STG**

> Wenn der Sensor trocken ist, verbinden Sie den Sensor mit dem Adapter.

## STG-DE-4.3 — `man` nicht als technischer Akteur verwenden

**Level:** `MUST_NOT`

Do not use the indefinite pronoun `man` to hide or generalize the actor in technical instructions or requirements.

Use:

- the imperative when the reader acts,
- a named role when a specified actor acts,
- the responsible system/component when it acts automatically.

## STG-DE-4.4 — Negationsbereich eindeutig machen

**Level:** `MUST`

Place `nicht`, `kein`, and other negative expressions so that only one interpretation is plausible. When the scope is complex, rewrite with an explicit condition.

**Ambiguous**

> Schalten Sie das Gerät nicht mit geöffnetem Gehäuse ein.

**STG**

> Wenn das Gehäuse offen ist, schalten Sie das Gerät nicht ein.

Avoid double negation.


## STG-DE-4.5 — Pronominaladverbien nur mit eindeutigem Bezug

**Level:** `MUST`

German pronominal adverbs such as `dabei`, `dazu`, `daraus`, `davon`, `darüber`, `dafür` and `hierfür` can compress a reference to an object, action, cause, purpose, or previous sentence. Use such a form only when exactly one local antecedent and exactly one semantic relation are possible.

In strict `STG-C-core` authoring, repeat the technical noun, action, or condition when the reference could be interpreted in more than one way.

**Mehrdeutig**

> Verbinden Sie den Sensor mit dem Adapter. Dabei darf die Dichtung nicht beschädigt werden.

`Dabei` can refer to connecting, to the adapter, or to the complete previous situation.

**STG**

> Wenn Sie den Sensor mit dem Adapter verbinden, beschädigen Sie die Dichtung nicht.

A validator should report an unresolved pronominal adverb as `NEEDS_REFERENCE_INPUT`; it must not invent the antecedent.

---

<!-- source: rules/05-procedures.md -->

# Section 5 — Prozedurales Schreiben

## STG-5.1 — Maximal 20 Wörter pro prozeduralem Satz

**Level:** `MUST`

A procedural sentence, including a safety command, has a maximum of **20 words** under the counting rules in Section 8.

A note is descriptive text and may contain up to 25 words per sentence.

## STG-5.2 — Eine Anweisung pro Satz

**Level:** `MUST`

Write one instruction per sentence.

More than one action is permitted in one sentence only when the actions:

- occur at the same time,
- are a single inseparable physical operation,
- or one action is an immediate acceptance/result statement belonging to the same work step.

**Nicht STG**

> Öffnen Sie die Abdeckung und entfernen Sie danach den Filter.

**STG**

> 1. Öffnen Sie die Abdeckung.  
> 2. Entfernen Sie den Filter.

**Permitted simultaneous action**

> Halten Sie die Leitung fest und lösen Sie die Mutter.

## STG-5.3 — Anweisungen im formalen Imperativ

**Level:** `MUST`

Use the formal German imperative with `Sie` for required reader actions.

**STG**

> Entfernen Sie die Abdeckung.  
> Stellen Sie den Druck auf 2 bar ein.  
> Prüfen Sie die Leitung auf Schäden.

Do not use passive voice, `soll`, or noun-only fragments to encode a command.

A project may adopt an infinitive instruction profile only by explicit directive; mixed imperative profiles are not permitted within one controlled document set.

## STG-5.4 — Bedingung vor Anweisung

**Level:** `MUST`

If the reader must know a condition before an action, place the condition first and separate it from the command with a comma.

**Nicht STG**

> Entfernen Sie die Sicherung, wenn die Anzeige rot ist.

**STG**

> Wenn die Anzeige rot ist, entfernen Sie die Sicherung.

## STG-5.5 — Hinweise enthalten keine Anweisungen

**Level:** `MUST`

A note may provide useful context only. It must not contain:

- a command,
- a safety action,
- a mandatory requirement,
- an acceptance criterion,
- a limit or tolerance that is required to complete the work step correctly.

Test: Remove every note from the procedure. The reader must still be able to perform the procedure correctly and safely.

**Nicht STG**

> HINWEIS: Ziehen Sie die Schraube mit 8 Nm fest.

**STG**

> Ziehen Sie die Schraube mit 8 Nm fest.

---

<!-- source: rules/06-descriptions.md -->

# Section 6 — Beschreibendes Schreiben

## STG-6.1 — Informationen schrittweise geben

**Level:** `MUST`

Introduce one topic, then add related information in a logical sequence. Do not force the reader to decode several new concepts in the same sentence.

## STG-6.2 — Schlüsselwörter und feste Verknüpfungen wiederverwenden

**Level:** `MUST`

Reuse the same key terms and connecting words to make relationships explicit. Do not replace a key term with a synonym for stylistic variety.

## STG-6.3 — Maximal 25 Wörter pro beschreibendem Satz

**Level:** `MUST`

A descriptive sentence has a maximum of **25 words** under the counting rules in Section 8.

If a sentence exceeds the limit, divide it by topic or logical relation; do not only remove articles or compress terms.

## STG-6.4 — Verwandte Informationen in Absätzen gruppieren

**Level:** `MUST`

Use paragraphs as logical units. Start a paragraph with a topic sentence when the content type permits it.

## STG-6.5 — Ein Thema pro Absatz

**Level:** `MUST`

A paragraph has one primary topic. Start a new paragraph when the topic changes.

A useful test: The first sentence of each paragraph should form a meaningful outline of the section.

## STG-6.6 — Maximal sechs Sätze pro Absatz

**Level:** `MUST`

A descriptive paragraph has no more than six sentences. If more sentences are necessary, check whether the paragraph contains more than one topic and divide it.

---

<!-- source: rules/07-safety.md -->

# Section 7 — Sicherheitsanweisungen

STG-DE controls the language of a safety instruction. The applicable safety standard controls the risk taxonomy, signal-word set, colors, symbols, and layout.

## STG-7.1 — Risikostufe eindeutig kennzeichnen

**Level:** `MUST`

Use the signal word or symbol required by the project's safety classification system. A document must use one consistent safety taxonomy.

Do not infer a lower risk category merely from legacy wording. If the correct category is unknown, return `NEEDS_SAFETY_INPUT`.

## STG-7.2 — Mit Schutzhandlung oder Bedingung beginnen

**Level:** `MUST`

After the signal word, state the preventive action or the necessary condition immediately. The reader must know what to do before reading secondary explanation.

**STG pattern**

> WARNUNG: Schalten Sie die Stromversorgung aus. ...

or

> WARNUNG: Wenn die Abdeckung offen ist, berühren Sie keine spannungsführenden Teile. ...

## STG-7.3 — Gefahr oder Folge nennen

**Level:** `MUST`

When the consequence is known, explain the hazard or possible result in concrete terms.

Avoid abstract formulations such as `Vorsicht ist geboten` or `besondere Sorgfalt ist erforderlich`.

**Nicht STG**

> WARNUNG: Arbeiten Sie vorsichtig.

**STG**

> WARNUNG: Schalten Sie die Stromversorgung aus. Eine elektrische Spannung kann schwere Verletzungen verursachen.

The technical safety content must come from an approved safety assessment; the language rule does not invent hazards.

---

<!-- source: rules/08-punctuation-and-counting.md -->

# Section 8 — Zeichensetzung und Wortzählung

## STG-8.1 — Standardsatzzeichen; kein Semikolon zum Verbinden von Aussagen

**Level:** `MUST_NOT`

Use standard German punctuation. Do not use the semicolon (`;`) to connect independent technical propositions. Write separate sentences instead.

This restriction is intentionally stronger than ordinary German punctuation rules because it limits sentence complexity.

## STG-8.2 — Bindestriche nur für echte Wortstruktur

**Level:** `MUST`

Use hyphens according to German orthography and approved terminology. Use them when they clarify compound boundaries, connect letters/numbers with words where required, or are part of an official term.

Do not use hyphens to hide syntactic complexity or to force a long phrase into one counted word.

## STG-8.3 — Klammern restriktiv verwenden

**Level:** `MUST`

Parentheses may be used for:

- figure/text references,
- identifiers,
- work-step identifiers,
- abbreviations after the full form,
- short clarifications,
- controlled alternatives where the project format explicitly permits them.

Do not put a required instruction, safety action, or primary technical condition only in parentheses.

## STG-8.4 — Doppelpunkt beendet die Einleitung einer vertikalen Liste

**Level:** `MUST`

For word counting, the text before a colon that introduces a vertical list is counted as one sentence. Each list item is checked separately.

Limits:

- 20 words for procedural items,
- 25 words for descriptive items.

## STG-8.5 — Klammertext separat prüfen

**Level:** `MUST`

Parenthetical text counts as one word in the outer sentence. The text inside parentheses is also checked separately for clarity and applicable sentence length.

This counting rule does not permit complex instructions inside parentheses.

## STG-8.6 — Geschützte Einheiten zählen als ein Wort

**Level:** `MUST`

For sentence-length counting, each of these counts as one word in the surrounding sentence:

- a number,
- a number directly combined with its unit,
- an abbreviation,
- an alphanumeric identifier,
- quoted/locked text,
- an official title/heading/label,
- a protected proper name.

Do not count numbering that only identifies a work step.

## STG-8.7 — Bindestrichkomposita zählen orthografisch als ein Wort

**Level:** `MUST`

A hyphenated German compound counts as one orthographic word for sentence length. The compound is still subject to Section 2 complexity rules.

## STG-DE-8.1 — Schrägstrichkombinationen vermeiden

**Level:** `SHOULD_NOT`

Avoid forms such as `und/oder`, `der/die`, `ein-/ausschalten`, and compressed slash alternatives in running technical text when they can have more than one interpretation.

Use an explicit `und`, `oder`, a vertical list, or separate sentences.

Exceptions are locked identifiers and project-defined compact table notation.

---

<!-- source: rules/09-writing-practices.md -->

# Section 9 — Schreibpraxis

## STG-9.1 — Satz neu bauen, wenn Wortersatz nicht reicht

**Level:** `MUST`

Do not replace an unapproved word mechanically when the replacement changes grammar, meaning, or modality. Rewrite the complete sentence while preserving technical meaning.

A language tool must prefer `NEEDS_DOMAIN_INPUT` to an invented rewrite when the intended meaning is unclear.

## STG-9.2 — Freigegebene Wörter korrekt verwenden

**Level:** `MUST`

Before using an approved word, check its approved meaning, word class, restrictions, and domain profile.

If a word has several approved meanings, the lexicon must distinguish them with separate meaning IDs.

## STG-9.3 — Keine idiomatischen Verbgefüge als Ersatz für direkte Verben

**Level:** `MUST_NOT`

In German, ambiguity and verbosity often come from idioms and function-verb constructions.

Do not use an idiomatic or noun-heavy verb phrase when a direct approved verb gives the same technical meaning.

**Nicht STG**

> Nehmen Sie eine Prüfung vor.

**STG**

> Prüfen Sie das Bauteil.

**Nicht STG**

> Bringen Sie die Änderung zur Anwendung.

**STG**

> Wenden Sie die Änderung an.

Lexicalized technical multiword verbs may be approved as single dictionary entries when the domain requires them.

## STG-9.4 — Terminologie und Formulierungen konsistent halten

**Level:** `MUST`

For the same action in the same context, use the same approved wording. Do not alternate sentence patterns for stylistic variety.

Templates are encouraged for recurrent work steps.

---

# General recommendations

These recommendations are not mandatory by default. A project may promote any of them to mandatory status.

## STG-GR-1 — Nebensatzmarker explizit und korrekt


Use explicit conjunctions such as `dass`, `wenn`, `weil`, and `bevor` when they make clause relations clear. Avoid compressed headline-style omission in running text.

## STG-GR-2 — `mit` auf Mehrdeutigkeit prüfen


The preposition `mit` can express instrument, accompaniment, association, or condition. If more than one reading is plausible, rewrite the sentence.

**Ambiguous**

> Montieren Sie die Abdeckung mit den roten Schrauben.

Possible intended meanings include:

- the cover already has red screws,
- install the cover together with the red screws,
- use the red screws as fasteners.

State the intended relation explicitly.

## STG-GR-3 — Pronomen sparsam verwenden


Use a pronoun only when its antecedent is unmistakable. Repetition of a technical noun is preferable to ambiguous reference.

## STG-GR-4 — Demonstrativa mit Nomen verwenden


Prefer `diese Leitung`, `dieser Wert`, `diese Methode` to a bare `dies` or `diese`, especially after several possible antecedents.

## STG-GR-5 — Lehnübersetzungen und falsche Freunde prüfen


Writers and translation systems must not transfer meanings from English merely because a German word looks similar. Examples requiring context checks include `realisieren`, `kontrollieren`, `eventuell`, and `aktuell` when translating to/from English.

The rule does not prescribe a replacement without context.

## STG-GR-6 — Abkürzungen in Fließtext reduzieren


Prefer full German expressions to general prose abbreviations such as `z. B.`, `d. h.`, `ggf.`, `bzw.`, and `usw.` when the abbreviation could reduce clarity.

`ggf.` and `bzw.` are prohibited by the seed vocabulary policy because they often hide a condition or relation.

## STG-GR-7 — Neutrale Personenbezeichnungen bevorzugen


Use role or function terms that are neutral and technically precise where possible, for example `Personal`, `Fachkraft`, `Bedienperson`, `Prüfperson`, or a project-defined role name.

Avoid gender-specific pronouns when they are unnecessary. Special orthographic gender markers are governed by the applicable language/style directive; STG-DE itself does not require them.

## STG-GR-8 — Genitivketten vermeiden


A simple German genitive is permitted. Avoid long chains of possessive/genitive relations that force the reader to resolve several nested dependencies.

**Schwer lesbar**

> die Prüfung der Dichtung des Ausgangs des Reglers

**Besser**

> die Prüfung der Dichtung am Reglerausgang

## STG-DE-9.1 — Modalpartikeln und rhetorische Füllwörter vermeiden

**Level:** `MUST_NOT`

Do not use modal particles or conversational fillers such as `mal`, `doch`, `eben`, `halt`, `wohl`, `eigentlich`, `einfach` when they do not have a precise technical meaning.

## STG-DE-9.2 — Vage Qualitäts- und Zeitangaben ersetzen

**Level:** `MUST`

Replace vague expressions with observable criteria whenever the criterion matters to the task.

Examples of terms that normally require rewriting:

- `möglichst schnell`,
- `zeitnah`,
- `ordnungsgemäß`,
- `fachgerecht`,
- `ausreichend`,
- `bei Bedarf`,
- `gegebenenfalls`.

**Nicht STG**

> Ziehen Sie die Schraube ausreichend fest.

**STG**

> Ziehen Sie die Schraube mit 8 Nm fest.

If no measurable criterion is available, request domain input instead of inventing one.
