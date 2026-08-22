# STG-DE — Simplified Technical German

Standalone specification snapshot for release 0.4.0. The repository files remain the canonical source.

---

<!-- source: specification.md -->

# STG-DE normative specification

## 1. Scope

STG-DE is a controlled form of written German for technical documentation. It is intended for procedures, maintenance information, operating information, system descriptions, service documentation, technical reports, safety instructions, and similar technical content.

STG-DE controls **expression**, not document layout. Typography, numbering systems, page design, product-specific warning graphics, units policy, and document architecture remain subject to the applicable publication standard or company directive.

## 2. Design principles

STG-DE is based on these principles:

1. **One term — one concept.** Use one approved designation for one technical concept within a defined scope.
2. **One general word — one controlled meaning.** A central lexicon can restrict a general-language word to one meaning and one word class.
3. **Actions use verbs.** Prefer direct verbs to nominalizations and function-verb constructions.
4. **Known agent first.** Use active voice when the agent is known. Use the formal imperative for instructions.
5. **One instruction per sentence.** Combine actions only when they are simultaneous or form one inseparable physical action.
6. **Conditions before commands.** The reader sees the condition before the action it controls.
7. **Short sentences.** Maximum 20 words for procedure/safety commands; maximum 25 words for descriptions and notes.
8. **One topic per sentence and paragraph.** Add information progressively.
9. **No stylistic synonym variation.** Repetition is preferred to lexical variation.
10. **No hidden modality.** Distinguish requirement, permission, capability/possibility, recommendation, and prohibition.
11. **No unresolved reference.** Pronouns, demonstratives, ellipses, and negation must have an unambiguous scope.
12. **German morphology is explicit data.** Dictionary entries carry gender, plural, inflection, separability, and approved forms as applicable.

## 3. German baseline

The default spelling profile is `de-DE` and follows the **Amtliches Regelwerk der deutschen Rechtschreibung (2024)** unless an applicable official directive requires another German national or organizational spelling profile.

Project configuration may declare a different profile, for example `de-CH`. A document must not mix spelling profiles without an explicit reason.

## 4. Text types

### 4.1 Procedure

A procedure tells the reader what to do. Instructions use the formal imperative with `Sie` unless a mandatory project directive specifies a different controlled imperative profile.

Default:

> Entfernen Sie die Abdeckung.

Not default:

> Abdeckung entfernen.

The infinitive instruction style can be enabled only as a project profile and must then be used consistently.

### 4.2 Description

A description gives information and does not command the reader. Descriptions normally use Präsens. Each sentence has one main topic.

### 4.3 Safety instruction

A safety instruction contains:

1. the signal word or other project-defined risk identifier,
2. the preventive command or the condition,
3. the consequence/risk when known.

The risk taxonomy comes from the applicable safety standard, not from STG-DE.

### 4.4 Note

A note gives optional supporting information. A note must not contain an instruction, mandatory requirement, acceptance limit, tolerance, or safety-critical action.

### 4.5 Locked external text

Legal names, UI labels, placards, document titles, identifiers, formulas, quoted material, and externally controlled strings may be outside STG-DE. The surrounding sentence must still obey STG rules where possible.

## 5. Conformance

### 5.1 `STG-R`

A text conforms to `STG-R` when all applicable mandatory writing rules are satisfied.

### 5.2 `STG-T`

A text conforms to `STG-T` when it conforms to `STG-R` and every technical noun and technical verb is approved in the applicable terminology source.

### 5.3 `STG-C-core`

A text conforms to `STG-C-core` when it conforms to `STG-T` and every other non-locked lexical item is approved for its used meaning and word class in the central v0.4 authoring-core lexicon. Unknown general-language words are not accepted automatically.

### 5.4 `STG-C`

A text conforms to `STG-C` when it conforms to `STG-T` and every other lexical item is approved for its used meaning and word class in a broad, human-reviewed central controlled lexicon.

`STG-C-core` is a closed-vocabulary profile for constrained authoring with the shipped v0.4 core lexicon. `STG-C` remains reserved for a broader, human-reviewed central lexicon and is not a general certification claim in this release.


### 5.5 Canonical lemma and inflection collisions

Lexical resolution must check canonical lemmas before accepting an inflection alias from another entry. If the same surface form can represent two controlled concepts, the lexicon must encode the distinction explicitly and the validator must use context/word class/entry precedence.

Normative example: `Daten` is an independent restricted noun for technical data/information. It must not be resolved automatically as the plural of `Datum`.

## 6. Terminology sources

The terminology resolution order is:

1. Regulatory or contractual terminology that cannot be changed
2. Approved company/product terminology
3. Approved industry/domain terminology
4. STG central lexicon
5. New term proposal subject to review

An agent must not replace an official technical designation merely because a shorter or more common synonym exists.

## 7. Word counting

For rule limits:

- A whitespace-delimited orthographic word normally counts as one word.
- A number with its directly associated unit counts as one word.
- An abbreviation or alphanumeric identifier counts as one word.
- A protected proper name, title, label, or quoted string counts as one word in the surrounding sentence.
- Parenthetical text counts as one word in the outer sentence and is also checked as its own sentence/fragment.
- A hyphenated compound counts as one orthographic word, but the compound-complexity rule still applies.
- Numbering that only identifies a work step does not count.

The word-count rules are compatibility rules, not a license to build syntactically dense compounds.

## 8. Machine-checking philosophy

Rules are classified as:

- `deterministic` — can normally be checked mechanically, for example word count or prohibited semicolon.
- `heuristic` — can be detected with high-value heuristics, for example passive voice or vague words.
- `semantic` — requires terminology or meaning analysis, for example one term/one concept or pronoun ambiguity.
- `domain` — requires approved terminology or subject-matter knowledge.

A validator must distinguish a hard violation from a heuristic finding.


## 8.1 Corpus evidence and lexical governance

Corpus frequency is evidence for lexical review, not automatic approval. A common expression can remain prohibited or review-required when it is vague, polysemous, stylistically redundant, or difficult to resolve deterministically.

A corpus audit must distinguish at least:

- general-language lexical gaps,
- inflection/contraction resolution gaps,
- approved project terminology candidates,
- protected identifiers/names/labels,
- prohibited or review-required wording.

STG-DE must not increase general-language coverage by silently classifying unknown words as technical terms.

## 9. Rule traceability

`rules/rule-index.yaml` is the canonical index for every STG-DE rule and recommendation. Rule IDs are stable within a major release line. A rule record identifies its scope, level, title, and the canonical Markdown file that contains its normative wording.

## 10. Change control

A change to a mandatory rule or dictionary meaning must include:

- identifier,
- old wording/meaning,
- proposed wording/meaning,
- technical reason,
- examples,
- impact on validators,
- migration note.

Versioning follows semantic versioning while the project is experimental. Before a stable 1.0 release, rule IDs should remain stable whenever possible.

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

---

<!-- source: corpus/validation-report.md -->

# STG-DE v0.4 — Multi-industry corpus validation report

## Executive result

v0.4 validates the authoring core against a **stratified six-industry corpus** rather than a single engineering domain. The public validation set contains **18 independent technical sources** — three per industry — and **2,066 analyzed tokens** in short German excerpts. The release does **not** redistribute the excerpts or manuals; it stores source metadata, hashes, frequencies, and aggregate metrics only.

| Metric | v0.3 baseline | v0.4 normalization only | v0.4 final |
|---|---:|---:|---:|
| Controlled central surface coverage | 51.4% | 52.7% | **58.1%** |
| `NEEDS_LEXICON_REVIEW` tokens | 272 | 245 | **232** |
| Routed/classified rate | 86.8% | 88.1% | **88.8%** |

The final central surface coverage is **6.7 percentage points** above the historical v0.3 baseline on this public set. This is not a target acceptance rate: technical nouns, product names, identifiers, domain verbs, and intentionally disallowed language are expected to remain outside the general core.

## Corpus design

| Industry | Sources | Tokens | v0.3 baseline | v0.4 final |
|---|---:|---:|---:|---:|
| Anlagenbau | 3 | 311 | 49.2% | **58.5%** |
| Automotive | 3 | 359 | 49.6% | **58.8%** |
| Elektrotechnik | 3 | 342 | 48.8% | **55.0%** |
| Maschinenbau | 3 | 356 | 50.3% | **58.4%** |
| Medizintechnik | 3 | 334 | 52.1% | **55.4%** |
| Software/IT | 3 | 364 | 58.0% | **62.1%** |

The six strata are Maschinenbau, Automotive, Elektrotechnik, Software/IT, Medizintechnik, and Anlagenbau. Source selection favors manufacturer or project documentation that is publicly accessible in German. `corpus/sources.yaml` records exact source metadata and sample hashes.

The token counts are intentionally close but not identical. Equal document count prevents one industry from dominating the curation pass. Because third-party manuals are not included, this release should be read as a **stratified evidence corpus**, not a full-text archive.

## What v0.4 changed

### 1. German noun morphology is part of lexical resolution

v0.3 stored plural forms such as `Informationen`, `Gefahren`, `Schritte`, and `Geräte` in noun metadata but the development validator did not resolve them. v0.4 recognizes **declared noun plurals** as `CENTRAL_INFLECTION`. On the same public excerpts, normalization alone raises controlled coverage from 51.4% to 52.7%.

This is a validator correction, not vocabulary inflation.

### 2. `Datum` and `Daten` are no longer conflated

The corpus exposed a German lexical collision: `Datum` has the plural `Daten`, while technical documentation usually uses `Daten` to mean information/data. A naive plural index therefore gives the wrong controlled meaning. v0.4 adds an independent restricted lemma `Daten` and gives canonical lemmas priority over plural aliases.

This finding is important for agentic validation: lexical surface equality is insufficient when German inflection collides with another lexical concept.

### 3. Capitalization no longer means “technical term”

German capitalizes all nouns. The v0.3 development heuristic routed any unknown capitalized token to `TECHNICAL_TERM_CANDIDATE`; this overstates terminology coverage. v0.4 uses the neutral class `LEXICAL_NOUN_CANDIDATE`. A candidate becomes project terminology only after resolution against an approved project glossary or a technical-noun category.

### 4. Only cross-domain, controllable vocabulary entered the core

v0.4 adds general technical-document concepts such as `Betriebsanleitung`, `Fachpersonal`, `Verletzung`, `Verwendung`, `Produkt`, `Version`, `Änderung`, `Kennzeichnung`, `Symbol`, `Daten`, and direct verbs such as `lesen`, `wählen`, `bedienen`, and `benötigen`.

Frequency alone was **not** sufficient for approval. Common words such as `führen`, `bieten`, `berücksichtigen`, and `gewährleisten` are routed to review because their technical meaning is too context-dependent or abstract for unconditional approval.

### 5. The coverage curve is now reproducible

`corpus/coverage-curves.csv` starts with the historical v0.3 result, applies the v0.4 normalization layer, and then adds each new core entry in a deterministic evidence order. This separates gains from grammar/lemmatization fixes from gains caused by new vocabulary.

## Final industry distribution

| Industry | Controlled | Unknown | Review | Prohibited | Lexical noun candidates |
|---|---:|---:|---:|---:|---:|
| Anlagenbau | 58.5% | 32 | 6 | 4 | 81 |
| Automotive | 58.8% | 39 | 7 | 5 | 85 |
| Elektrotechnik | 55.0% | 44 | 10 | 4 | 80 |
| Maschinenbau | 58.4% | 41 | 11 | 5 | 79 |
| Medizintechnik | 55.4% | 42 | 9 | 6 | 83 |
| Software/IT | 62.1% | 34 | 6 | 5 | 81 |

## Recurring non-STG patterns

The corpus continues to justify rejecting or reviewing ordinary professional German that is not sufficiently deterministic for controlled authoring. Recurring examples include `sowie`, `entsprechend`, `gegebenenfalls`, `ausreichend`, and context-dependent verbs such as `führen` or `durchführen`.

The goal is not to make existing manuals pass unchanged. The goal is to give authors and agents deterministic rewrites and to separate general core vocabulary from domain terminology.


## What v0.4 does not prove

v0.4 is materially stronger than v0.3, but it is still an experimental authoring standard. It does not establish population-level coverage of German technical documentation, and it does not replace:

- expert review by German technical writers and terminologists;
- full-text licensed corpus analysis at substantially larger scale;
- a deterministic German morphological and syntactic analyzer;
- reader comprehension testing;
- safety-domain validation against the publication standard applicable to a product;
- project terminology governance.

`STG-C-core` therefore remains experimental. `STG-C` remains reserved for a later, human-reviewed release.

---

## Structured appendix: `rules/rule-index.yaml`

```yaml
schema_version: '0.4'
release: 0.4.0
rule_or_recommendation_count: 75
mandatory_or_normative_rule_count: 67
general_recommendation_count: 8
rules:
- id: STG-1.1
  title: Zulässiger Wortschatz
  file: rules/01-words.md
  level: MUST
- id: STG-1.2
  title: Wortart
  file: rules/01-words.md
  level: MUST
- id: STG-1.3
  title: Kontrollierte Bedeutung
  file: rules/01-words.md
  level: MUST
- id: STG-1.4
  title: Zulässige Flexionsformen
  file: rules/01-words.md
  level: MUST
- id: STG-1.5
  title: Technische Substantive
  file: rules/01-words.md
  level: MUST
- id: STG-1.6
  title: Nicht-zentrale Wörter als technische Terme
  file: rules/01-words.md
  level: MUST
- id: STG-1.7
  title: Technisches Substantiv ist nicht automatisch Verb
  file: rules/01-words.md
  level: MUST
- id: STG-1.8
  title: Offizielle technische Benennungen
  file: rules/01-words.md
  level: MUST
- id: STG-1.9
  title: Neue technische Benennungen kurz halten
  file: rules/01-words.md
  level: SHOULD
- id: STG-1.10
  title: Keine regionale Sprache, Umgangssprache oder Jargon
  file: rules/01-words.md
  level: MUST_NOT
- id: STG-1.11
  title: Ein Konzept, eine Benennung
  file: rules/01-words.md
  level: MUST
- id: STG-1.12
  title: Technische Verben
  file: rules/01-words.md
  level: MUST
- id: STG-1.13
  title: Technisches Verb ist nicht automatisch Substantiv
  file: rules/01-words.md
  level: MUST
- id: STG-1.14
  title: Deutsche Standardschreibung
  file: rules/01-words.md
  level: MUST
- id: STG-2.1
  title: Begrenze die semantische Dichte technischer Benennungen
  file: rules/02-compounds-and-terms.md
  level: MUST
- id: STG-2.2
  title: Lange offizielle Benennung zuerst vollständig
  file: rules/02-compounds-and-terms.md
  level: MUST
- id: STG-DE-2.1
  title: Deutsche Komposita als Terminologieobjekte
  file: rules/02-compounds-and-terms.md
  level: MUST
- id: STG-DE-2.2
  title: Bindestriche nicht als Komplexitäts-Trick verwenden
  file: rules/02-compounds-and-terms.md
  level: MUST_NOT
- id: STG-DE-2.3
  title: Abkürzungen sparsam und stabil verwenden
  file: rules/02-compounds-and-terms.md
  level: MUST
- id: STG-3.1
  title: Nur freigegebene Verbformen
  file: rules/03-verbs.md
  level: MUST
- id: STG-3.2
  title: Kontrollierte Tempora und Modi
  file: rules/03-verbs.md
  level: MUST
- id: STG-3.3
  title: Partizip II für Zustand oder Attribut
  file: rules/03-verbs.md
  level: MUST
- id: STG-3.4
  title: Keine unnötigen Hilfsverbketten
  file: rules/03-verbs.md
  level: MUST_NOT
- id: STG-3.5
  title: Keine englische `-ing`-Sonderregel; kontrolliere deutsche Nominalisierung
  file: rules/03-verbs.md
  level: MUST
- id: STG-3.6
  title: Aktiv bevorzugen
  file: rules/03-verbs.md
  level: MUST
- id: STG-3.7
  title: Handlungen mit direkten Verben ausdrücken
  file: rules/03-verbs.md
  level: MUST
- id: STG-DE-3.1
  title: Trennbare Verben kontrollieren
  file: rules/03-verbs.md
  level: SHOULD
- id: STG-DE-3.2
  title: Modalität eindeutig kodieren
  file: rules/03-verbs.md
  level: MUST
- id: STG-DE-3.3
  title: '`werden` restriktiv verwenden'
  file: rules/03-verbs.md
  level: SHOULD_NOT
- id: STG-4.1
  title: Kurze, eindeutige Sätze
  file: rules/04-sentences.md
  level: MUST
- id: STG-4.2
  title: Keine bedeutungstragenden Auslassungen
  file: rules/04-sentences.md
  level: MUST_NOT
- id: STG-4.3
  title: Vertikale Listen für komplexe Aufzählungen
  file: rules/04-sentences.md
  level: MUST
- id: STG-4.4
  title: Logische Verknüpfungen explizit machen
  file: rules/04-sentences.md
  level: MUST
- id: STG-4.5
  title: Artikel und Demonstrativa eindeutig verwenden
  file: rules/04-sentences.md
  level: MUST
- id: STG-DE-4.1
  title: Nebensatzverschachtelung begrenzen
  file: rules/04-sentences.md
  level: MUST
- id: STG-DE-4.2
  title: Pronomen nur mit eindeutigem Bezug
  file: rules/04-sentences.md
  level: MUST
- id: STG-DE-4.3
  title: '`man` nicht als technischer Akteur verwenden'
  file: rules/04-sentences.md
  level: MUST_NOT
- id: STG-DE-4.4
  title: Negationsbereich eindeutig machen
  file: rules/04-sentences.md
  level: MUST
- id: STG-DE-4.5
  title: Pronominaladverbien nur mit eindeutigem Bezug
  file: rules/04-sentences.md
  level: MUST
- id: STG-5.1
  title: Maximal 20 Wörter pro prozeduralem Satz
  file: rules/05-procedures.md
  level: MUST
- id: STG-5.2
  title: Eine Anweisung pro Satz
  file: rules/05-procedures.md
  level: MUST
- id: STG-5.3
  title: Anweisungen im formalen Imperativ
  file: rules/05-procedures.md
  level: MUST
- id: STG-5.4
  title: Bedingung vor Anweisung
  file: rules/05-procedures.md
  level: MUST
- id: STG-5.5
  title: Hinweise enthalten keine Anweisungen
  file: rules/05-procedures.md
  level: MUST
- id: STG-6.1
  title: Informationen schrittweise geben
  file: rules/06-descriptions.md
  level: MUST
- id: STG-6.2
  title: Schlüsselwörter und feste Verknüpfungen wiederverwenden
  file: rules/06-descriptions.md
  level: MUST
- id: STG-6.3
  title: Maximal 25 Wörter pro beschreibendem Satz
  file: rules/06-descriptions.md
  level: MUST
- id: STG-6.4
  title: Verwandte Informationen in Absätzen gruppieren
  file: rules/06-descriptions.md
  level: MUST
- id: STG-6.5
  title: Ein Thema pro Absatz
  file: rules/06-descriptions.md
  level: MUST
- id: STG-6.6
  title: Maximal sechs Sätze pro Absatz
  file: rules/06-descriptions.md
  level: MUST
- id: STG-7.1
  title: Risikostufe eindeutig kennzeichnen
  file: rules/07-safety.md
  level: MUST
- id: STG-7.2
  title: Mit Schutzhandlung oder Bedingung beginnen
  file: rules/07-safety.md
  level: MUST
- id: STG-7.3
  title: Gefahr oder Folge nennen
  file: rules/07-safety.md
  level: MUST
- id: STG-8.1
  title: Standardsatzzeichen; kein Semikolon zum Verbinden von Aussagen
  file: rules/08-punctuation-and-counting.md
  level: MUST_NOT
- id: STG-8.2
  title: Bindestriche nur für echte Wortstruktur
  file: rules/08-punctuation-and-counting.md
  level: MUST
- id: STG-8.3
  title: Klammern restriktiv verwenden
  file: rules/08-punctuation-and-counting.md
  level: MUST
- id: STG-8.4
  title: Doppelpunkt beendet die Einleitung einer vertikalen Liste
  file: rules/08-punctuation-and-counting.md
  level: MUST
- id: STG-8.5
  title: Klammertext separat prüfen
  file: rules/08-punctuation-and-counting.md
  level: MUST
- id: STG-8.6
  title: Geschützte Einheiten zählen als ein Wort
  file: rules/08-punctuation-and-counting.md
  level: MUST
- id: STG-8.7
  title: Bindestrichkomposita zählen orthografisch als ein Wort
  file: rules/08-punctuation-and-counting.md
  level: MUST
- id: STG-DE-8.1
  title: Schrägstrichkombinationen vermeiden
  file: rules/08-punctuation-and-counting.md
  level: SHOULD_NOT
- id: STG-9.1
  title: Satz neu bauen, wenn Wortersatz nicht reicht
  file: rules/09-writing-practices.md
  level: MUST
- id: STG-9.2
  title: Freigegebene Wörter korrekt verwenden
  file: rules/09-writing-practices.md
  level: MUST
- id: STG-9.3
  title: Keine idiomatischen Verbgefüge als Ersatz für direkte Verben
  file: rules/09-writing-practices.md
  level: MUST_NOT
- id: STG-9.4
  title: Terminologie und Formulierungen konsistent halten
  file: rules/09-writing-practices.md
  level: MUST
- id: STG-GR-1
  title: Nebensatzmarker explizit und korrekt
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-2
  title: '`mit` auf Mehrdeutigkeit prüfen'
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-3
  title: Pronomen sparsam verwenden
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-4
  title: Demonstrativa mit Nomen verwenden
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-5
  title: Lehnübersetzungen und falsche Freunde prüfen
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-6
  title: Abkürzungen in Fließtext reduzieren
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-7
  title: Neutrale Personenbezeichnungen bevorzugen
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-8
  title: Genitivketten vermeiden
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-DE-9.1
  title: Modalpartikeln und rhetorische Füllwörter vermeiden
  file: rules/09-writing-practices.md
  level: MUST_NOT
- id: STG-DE-9.2
  title: Vage Qualitäts- und Zeitangaben ersetzen
  file: rules/09-writing-practices.md
  level: MUST

```

---

## Structured appendix: `dictionary/approved-words.yaml`

```yaml
schema_version: '0.4'
release: 0.4.0
status: multi_industry_corpus_validated_authoring_core
language: de-DE
normative_for_profile: STG-C-core
design_basis:
  source: independent German lexical design
  human_linguistic_review: not_yet_completed
  corpus_validation: v0.4_stratified_multi_industry_public_excerpt_corpus
entries:
- entry_id: DE-PRE-ab
  lemma: ab
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.from_starting_point
    definition: kennzeichnet einen ausdrücklich genannten zeitlichen, räumlichen oder numerischen Ausgangspunkt
  review_status: corpus_candidate_v0.3
  restrictions:
  - Ausgangspunkt ausdrücklich nennen.
- entry_id: DE-VER-abbrechen
  lemma: abbrechen
  part_of_speech: verb
  status: approved
  meanings:
  - id: abort
    definition: einen laufenden Vorgang vor seinem regulären Ende beenden
  review_status: provisional_v0.2
  separable: true
  prefix: ab
  approved_examples:
  - Brechen Sie den Test ab, wenn die Temperatur 80 °C überschreitet.
- entry_id: DE-VER-abdichten
  lemma: abdichten
  part_of_speech: verb
  status: restricted
  meanings:
  - id: seal
    definition: eine Verbindung oder Oberfläche so herstellen, dass das festgelegte Medium innerhalb der spezifizierten
      Leckagegrenze nicht austritt
  review_status: provisional_v0.2
  separable: true
  prefix: ab
  restrictions:
  - Dichtheitskriterium muss aus Verfahren oder Spezifikation hervorgehen.
- entry_id: DE-CON-aber
  lemma: aber
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.but
    definition: kennzeichnet einen direkten Gegensatz oder eine Einschränkung zur vorherigen Aussage
  review_status: provisional_v0.2
- entry_id: DE-VER-abkuehlen
  lemma: abkühlen
  part_of_speech: verb
  status: approved
  meanings:
  - id: cool.down
    definition: die Temperatur eines Objekts oder Mediums verringern oder sinken lassen
  review_status: corpus_candidate_v0.3
  separable: true
  prefix: ab
  surface_forms:
  - abgekühlt
  approved_examples:
  - Lassen Sie das Gerät auf 40 °C abkühlen.
- entry_id: DE-VER-ablassen
  lemma: ablassen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: drain.release
    definition: Flüssigkeit, Gas oder Druck kontrolliert aus einem System ausströmen lassen
  review_status: provisional_v0.2
  separable: true
  prefix: ab
  restrictions:
  - 'Objekt nennen: Flüssigkeit, Gas oder Druck.'
- entry_id: DE-VER-abschlie-en
  lemma: abschließen
  part_of_speech: verb
  status: approved
  meanings:
  - id: complete.finish
    definition: einen Vorgang regulär beenden und als beendet kennzeichnen
  review_status: provisional_v0.2
  separable: true
  prefix: ab
  restrictions:
  - Nicht mit verriegeln oder verschließen verwechseln.
- entry_id: DE-NOU-abschnitt
  lemma: Abschnitt
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.section
    definition: klar abgegrenzter Teil eines Dokuments oder einer Struktur
  review_status: provisional_v0.2
  gender: masc
  plural: Abschnitte
- entry_id: DE-NOU-abstand
  lemma: Abstand
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.distance
    definition: räumliche Entfernung zwischen zwei ausdrücklich bestimmten Punkten, Flächen oder Objekten
  review_status: provisional_v0.2
  gender: masc
  plural: Abstände
- entry_id: DE-VER-abziehen
  lemma: abziehen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: pull.remove
    definition: einen Steckverbinder, eine Abdeckung oder ein vergleichbares Teil durch Ziehen von seiner Verbindung
      entfernen
  review_status: corpus_candidate_v0.3
  separable: true
  prefix: ab
  surface_forms:
  - abgezogen
  restrictions:
  - Objekt und Verbindung müssen eindeutig sein. Für mathematische Subtraktion subtrahieren verwenden.
- entry_id: DE-QUA-acht
  lemma: acht
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.eight
    definition: bezeichnet die Zahl 8 in ausgeschriebener Form
  review_status: corpus_candidate_v0.3
- entry_id: DE-VER-addieren
  lemma: addieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: add.math
    definition: zwei oder mehr numerische Werte mathematisch zusammenzählen
  review_status: provisional_v0.2
- entry_id: DE-ADJ-aktiv
  lemma: aktiv
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.active
    definition: in einem freigegebenen eingeschalteten oder wirksamen Zustand
  review_status: provisional_v0.2
- entry_id: DE-VER-aktivieren
  lemma: aktivieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: activate
    definition: eine Funktion oder ein System in den freigegebenen aktiven Zustand bringen
  review_status: provisional_v0.2
- entry_id: DE-VER-aktualisieren
  lemma: aktualisieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: update
    definition: Daten oder Software auf einen ausdrücklich bezeichneten neueren Stand bringen
  review_status: provisional_v0.2
  restrictions:
  - Zielversion oder Quelle nennen, wenn für die Aufgabe relevant.
- entry_id: DE-DET-alle
  lemma: alle
  part_of_speech: determiner
  status: approved
  meanings:
  - id: determiner.all
    definition: bezeichnet die Gesamtheit einer klar bestimmten Menge
  review_status: provisional_v0.2
  surface_forms:
  - alle
  - aller
  - allen
  approved_examples:
  - Entfernen Sie alle Schrauben.
- entry_id: DE-CON-als
  lemma: als
  part_of_speech: conjunction
  status: restricted
  meanings:
  - id: conj.comparison
    definition: kennzeichnet den Vergleich nach einer ausdrücklich genannten Vergleichsgröße
  - id: conj.role
    definition: kennzeichnet die ausdrücklich benannte Funktion oder Rolle eines Objekts
  review_status: corpus_candidate_v0.3
  restrictions:
  - Nicht als unspezifischen zeitlichen Erzähler verwenden. Vergleichsgröße oder Rolle muss eindeutig sein.
  approved_examples:
  - Der Druck muss größer als 5 bar sein.
  - Verwenden Sie Anschluss X1 als Referenz.
- entry_id: DE-PRE-an
  lemma: an
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.at_on
    definition: kennzeichnet Kontakt, unmittelbare Nähe oder eine definierte Position an einem Objekt
  review_status: provisional_v0.2
- entry_id: DE-VER-analysieren
  lemma: analysieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: analyze
    definition: Daten, Material oder einen Fehler systematisch in Bestandteile oder Ursachen untersuchen
  review_status: provisional_v0.2
  restrictions:
  - Analyseziel und Datenbasis angeben, wenn sie nicht aus dem Kontext eindeutig sind.
- entry_id: DE-NOU-anfang
  lemma: Anfang
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.start
    definition: erster Punkt oder erste Phase eines ausdrücklich bestimmten Ablaufs oder Bereichs
  review_status: provisional_v0.2
  gender: masc
  plural: Anfänge
- entry_id: DE-NOU-angabe
  lemma: Angabe
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.angabe
    definition: ausdrücklich genannter technischer Wert oder dokumentierte Information
  review_status: multi_industry_candidate_v0.4
  plural: Angaben
  restrictions:
  - Wenn möglich den konkreten Informationstyp nennen, zum Beispiel Wert, Maß oder Datum.
- entry_id: DE-NOU-anleitung
  lemma: Anleitung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.anleitung
    definition: Dokument oder abgegrenzter Dokumentteil mit Informationen oder Anweisungen zur Verwendung eines
      Produkts
  review_status: multi_industry_candidate_v0.4
  plural: Anleitungen
  restrictions:
  - Wenn ein offizieller Dokumenttitel vorhanden ist, diesen Titel verwenden.
- entry_id: DE-VER-anpassen
  lemma: anpassen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: adapt.adjust
    definition: einen Parameter, eine Verbindung oder ein Objekt an eine ausdrücklich genannte Anforderung oder
      Referenz angleichen
  review_status: provisional_v0.2
  restrictions:
  - Referenz oder Zielzustand nennen.
  surface_forms:
  - angepasst
- entry_id: DE-VER-anschliessen
  lemma: anschließen
  part_of_speech: verb
  status: approved
  meanings:
  - id: connect.interface
    definition: ein Kabel, einen Steckverbinder oder ein Gerät mit einer ausdrücklich genannten Schnittstelle elektrisch
      oder funktional verbinden
  review_status: corpus_candidate_v0.3
  separable: true
  prefix: an
  surface_forms:
  - angeschlossen
  approved_examples:
  - Schließen Sie das Kabel an Anschluss X1 an.
- entry_id: DE-VER-anwenden
  lemma: anwenden
  part_of_speech: verb
  status: approved
  meanings:
  - id: apply.method
    definition: ein Verfahren, eine Regel oder ein Mittel für den vorgesehenen Zweck verwenden
  review_status: provisional_v0.2
- entry_id: DE-NOU-anzahl
  lemma: Anzahl
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.count
    definition: gezählte Menge diskreter Elemente
  review_status: provisional_v0.2
  gender: fem
  plural: Anzahlen
- entry_id: DE-VER-anzeigen
  lemma: anzeigen
  part_of_speech: verb
  status: approved
  meanings:
  - id: display
    definition: Information auf einem Display, Instrument oder einer Benutzeroberfläche sichtbar ausgeben
  review_status: provisional_v0.2
  separable: true
  prefix: an
- entry_id: DE-NOU-art
  lemma: Art
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.type
    definition: klar definierte Kategorie oder Klasse von Elementen
  review_status: provisional_v0.2
  gender: fem
  plural: Arten
- entry_id: DE-ADV-auch
  lemma: auch
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.also
    definition: fügt ein weiteres ausdrücklich genanntes Element mit derselben Aussage hinzu
  review_status: provisional_v0.2
  restrictions:
  - Nicht verwenden, wenn unklar ist, auf welchen Satzteil sich auch bezieht.
- entry_id: DE-PRE-auf
  lemma: auf
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.on_to
    definition: kennzeichnet eine Position auf einer Oberfläche oder ein festgelegtes Ziel einer Einstellung
  review_status: provisional_v0.2
- entry_id: DE-VER-aufbewahren
  lemma: aufbewahren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: store.physical
    definition: einen Gegenstand oder ein Dokument an einem ausdrücklich festgelegten Ort für spätere Verwendung
      lagern
  review_status: corpus_candidate_v0.3
  separable: true
  prefix: auf
  surface_forms:
  - aufbewahrt
  restrictions:
  - Ort oder Aufbewahrungsanforderung nennen, wenn sie für die Sicherheit oder Funktion relevant ist.
- entry_id: DE-VER-auffangen
  lemma: auffangen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: collect.flow
    definition: austretende Flüssigkeit, Partikel oder Material in einem geeigneten Behälter oder Hilfsmittel sammeln
  review_status: corpus_candidate_v0.3
  separable: true
  prefix: auf
  surface_forms:
  - aufgefangen
  restrictions:
  - Medium und Auffangmittel nennen, wenn sie nicht aus dem Arbeitsschritt eindeutig sind.
- entry_id: DE-NOU-aufgabe
  lemma: Aufgabe
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.task
    definition: abgegrenzte technische Tätigkeit mit einem definierten Ziel
  review_status: provisional_v0.2
  gender: fem
  plural: Aufgaben
- entry_id: DE-VER-aufladen
  lemma: aufladen
  part_of_speech: verb
  status: approved
  meanings:
  - id: charge.battery
    definition: einen elektrischen Energiespeicher mit Energie laden
  review_status: provisional_v0.2
  separable: true
  prefix: auf
- entry_id: DE-VER-auflisten
  lemma: auflisten
  part_of_speech: verb
  status: approved
  meanings:
  - id: list
    definition: mehrere Elemente in einer ausdrücklich strukturierten Liste nennen
  review_status: provisional_v0.2
  separable: true
  prefix: auf
- entry_id: DE-VER-auftragen
  lemma: auftragen
  part_of_speech: verb
  status: approved
  meanings:
  - id: apply.material
    definition: Material kontrolliert auf eine Oberfläche bringen
  review_status: provisional_v0.2
  separable: true
  prefix: auf
- entry_id: DE-VER-auftreten
  lemma: auftreten
  part_of_speech: verb
  status: restricted
  meanings:
  - id: occur
    definition: als Ereignis, Fehler oder Zustand entstehen oder vorhanden werden
  review_status: provisional_v0.2
  separable: true
  prefix: auf
  restrictions:
  - Nicht für räumliches Auftreten einer Person verwenden.
- entry_id: DE-VER-aufzeichnen
  lemma: aufzeichnen
  part_of_speech: verb
  status: approved
  meanings:
  - id: record
    definition: Messwerte, Ereignisse oder Signale fortlaufend als Daten speichern
  review_status: provisional_v0.2
  separable: true
  prefix: auf
- entry_id: DE-PRE-aus
  lemma: aus
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.from_out_of
    definition: kennzeichnet Herkunft aus einem Inneren oder Materialzusammensetzung
  review_status: provisional_v0.2
  restrictions:
  - Nur verwenden, wenn Herkunft oder Materialbezug eindeutig ist.
- entry_id: DE-PHR-aus-bestehen
  lemma: aus ... bestehen
  part_of_speech: phrase
  status: approved
  meanings:
  - id: consist.of
    definition: gibt die vollständig oder teilweise genannten Bestandteile eines Objekts an
  review_status: provisional_v0.2
- entry_id: DE-VER-ausbauen
  lemma: ausbauen
  part_of_speech: verb
  status: approved
  meanings:
  - id: remove.installed
    definition: ein eingebautes Bauteil aus seiner Einbauposition entfernen
  review_status: provisional_v0.2
  separable: true
  prefix: aus
- entry_id: DE-VER-ausf-hren
  lemma: ausführen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: execute.software
    definition: einen Softwarebefehl, ein Programm oder ein Skript starten und abarbeiten lassen
  review_status: provisional_v0.2
  restrictions:
  - Nicht als allgemeines Füllverb für Tätigkeiten verwenden.
  surface_forms:
  - ausgeführt
- entry_id: DE-ADJ-ausgeschaltet
  lemma: ausgeschaltet
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.off
    definition: nicht im aktiven Energie- oder Betriebszustand
  review_status: provisional_v0.2
- entry_id: DE-VER-ausladen
  lemma: ausladen
  part_of_speech: verb
  status: approved
  meanings:
  - id: unload.cargo
    definition: Material oder Gegenstände aus einem Transport- oder Aufnahmeobjekt entfernen
  review_status: provisional_v0.2
  separable: true
  prefix: aus
- entry_id: DE-VER-ausrichten
  lemma: ausrichten
  part_of_speech: verb
  status: approved
  meanings:
  - id: align
    definition: ein Objekt in eine festgelegte geometrische Lage oder Richtung bringen
  review_status: provisional_v0.2
  separable: true
  prefix: aus
- entry_id: DE-VER-ausschalten
  lemma: ausschalten
  part_of_speech: verb
  status: approved
  meanings:
  - id: switch.off
    definition: ein Gerät, System oder eine Funktion aus dem aktiven Energie- oder Betriebszustand bringen
  review_status: provisional_v0.2
  separable: true
  prefix: aus
  prohibited_synonyms:
  - ausmachen
- entry_id: DE-VER-ausschneiden
  lemma: ausschneiden
  part_of_speech: verb
  status: approved
  meanings:
  - id: cut.ui
    definition: ein markiertes digitales Element entfernen und für späteres Einfügen zwischenspeichern
  review_status: provisional_v0.2
  separable: true
  prefix: aus
- entry_id: DE-ADV-au-en
  lemma: außen
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.outside
    definition: kennzeichnet die Außenseite oder den Außenraum eines definierten Objekts
  review_status: provisional_v0.2
- entry_id: DE-PHR-au-er-betrieb-sein
  lemma: außer Betrieb sein
  part_of_speech: phrase
  status: restricted
  meanings:
  - id: state.out_of_operation
    definition: kennzeichnet, dass ein System nicht für den vorgesehenen Betrieb verfügbar ist
  review_status: provisional_v0.2
- entry_id: DE-VER-ausw-hlen
  lemma: auswählen
  part_of_speech: verb
  status: approved
  meanings:
  - id: select
    definition: eine Option aus mehreren Optionen bestimmen
  review_status: provisional_v0.2
  separable: true
  prefix: aus
- entry_id: DE-NOU-baugruppe
  lemma: Baugruppe
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.assembly
    definition: aus mehreren Teilen bestehende technische Einheit
  review_status: provisional_v0.2
  gender: fem
  plural: Baugruppen
  restrictions:
  - Offizielle Produktbenennung hat Vorrang.
- entry_id: DE-NOU-bauteil
  lemma: Bauteil
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.component
    definition: einzelnes technisch abgegrenztes Teil eines Systems oder einer Baugruppe
  review_status: provisional_v0.2
  gender: neut
  plural: Bauteile
  restrictions:
  - Offizielle Produktbenennung hat Vorrang.
- entry_id: DE-VER-beachten
  lemma: beachten
  part_of_speech: verb
  status: restricted
  meanings:
  - id: heed
    definition: einen ausdrücklich genannten Hinweis, Grenzwert oder Umstand bei einer Handlung berücksichtigen
  review_status: provisional_v0.2
  restrictions:
  - In Arbeitsanweisungen nach Möglichkeit direkte Handlung formulieren statt beachten.
- entry_id: DE-VER-bedienen
  lemma: bedienen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: verb.bedienen
    definition: ein technisches Produkt mit den vorgesehenen Bedienelementen steuern
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - bediene
  - bedienst
  - bedient
  - bedienen
  - bediente
  - bedienten
  restrictions:
  - Nicht als allgemeines Synonym für verwenden einsetzen.
- entry_id: DE-NOU-bedienung
  lemma: Bedienung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.bedienung
    definition: Interaktion einer Person mit Bedienelementen oder einer Benutzeroberfläche
  review_status: multi_industry_candidate_v0.4
  restrictions:
  - In Verfahren das direkte Bedienverb verwenden.
- entry_id: DE-NOU-bedingung
  lemma: Bedingung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.condition
    definition: ausdrücklich definierter Zustand, der für eine Aussage oder Handlung erfüllt sein muss
  review_status: provisional_v0.2
  gender: fem
  plural: Bedingungen
- entry_id: DE-VER-befestigen
  lemma: befestigen
  part_of_speech: verb
  status: approved
  meanings:
  - id: attach
    definition: ein Teil so verbinden, dass es in der vorgesehenen Position gehalten wird
  review_status: provisional_v0.2
- entry_id: DE-ADJ-befestigt
  lemma: befestigt
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.attached
    definition: in der vorgesehenen Position mechanisch gehalten
  review_status: provisional_v0.2
- entry_id: DE-VER-befolgen
  lemma: befolgen
  part_of_speech: verb
  status: approved
  meanings:
  - id: obey
    definition: die Anweisungen oder Regeln eines ausdrücklich genannten Dokuments ausführen
  review_status: provisional_v0.2
- entry_id: DE-VER-beheben
  lemma: beheben
  part_of_speech: verb
  status: restricted
  meanings:
  - id: correct.fault
    definition: einen ausdrücklich identifizierten Fehler oder eine ausdrücklich identifizierte Störung korrigieren
  review_status: corpus_candidate_v0.3
  surface_forms:
  - behebe
  - behebst
  - behebt
  - beheben
  - behob
  - behoben
  restrictions:
  - Fehler oder Störung nennen. Nicht für physisches Entfernen von Material verwenden.
- entry_id: DE-PRE-bei
  lemma: bei
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.at
    definition: kennzeichnet eine definierte Position, einen Betriebszustand oder einen Messwert
  review_status: provisional_v0.2
  restrictions:
  - Für Bedingungen mit Handlung nach Möglichkeit einen wenn-Satz verwenden.
- entry_id: DE-DET-beide
  lemma: beide
  part_of_speech: determiner
  status: approved
  meanings:
  - id: determiner.both
    definition: bezeichnet genau zwei zuvor bestimmte Elemente
  review_status: provisional_v0.2
  surface_forms:
  - beide
  - beider
  - beiden
  restrictions:
  - Nur verwenden, wenn die Menge nachweislich genau zwei Elemente enthält.
- entry_id: DE-NOU-beispiel
  lemma: Beispiel
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.beispiel
    definition: konkreter Fall, der eine Regel, Funktion oder Verwendung erläutert
  review_status: multi_industry_candidate_v0.4
  plural: Beispiele
- entry_id: DE-VER-beladen
  lemma: beladen
  part_of_speech: verb
  status: approved
  meanings:
  - id: load.cargo
    definition: Material oder Gegenstände in oder auf ein Transport- oder Aufnahmeobjekt bringen
  review_status: provisional_v0.2
- entry_id: DE-VER-belueften
  lemma: belüften
  part_of_speech: verb
  status: restricted
  meanings:
  - id: ventilate
    definition: einem Bereich kontrolliert Luft zuführen oder Luft austauschen
  review_status: corpus_candidate_v0.3
  surface_forms:
  - belüftet
  restrictions:
  - Erforderlichen Luftstrom oder das maßgebliche Kriterium nennen, wenn relevant.
- entry_id: DE-VER-benachrichtigen
  lemma: benachrichtigen
  part_of_speech: verb
  status: approved
  meanings:
  - id: notify
    definition: einer bestimmten Person oder Stelle eine Information gezielt übermitteln
  review_status: provisional_v0.2
- entry_id: DE-NOU-benennung
  lemma: Benennung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.designation
    definition: freigegebener sprachlicher Ausdruck für einen technischen Begriff
  review_status: provisional_v0.2
  gender: fem
  plural: Benennungen
- entry_id: DE-NOU-benutzer
  lemma: Benutzer
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.user
    definition: Person oder Systemrolle, die eine Benutzeroberfläche oder Funktion verwendet
  review_status: provisional_v0.2
  gender: masc
  plural: Benutzer
  restrictions:
  - Wenn Geschlechtsneutralität oder Rollenbezeichnung projektseitig anders geregelt ist, offizielle Rollenbezeichnung
    verwenden.
- entry_id: DE-VER-benoetigen
  lemma: benötigen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: verb.benoetigen
    definition: eine ausdrücklich genannte Voraussetzung, Ressource oder Komponente für eine Handlung erfordern
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - benötige
  - benötigst
  - benötigt
  - benötigen
  - benötigte
  - benötigten
  restrictions:
  - In Verfahren Voraussetzungen möglichst vor den Arbeitsschritten auflisten.
- entry_id: DE-VER-berechnen
  lemma: berechnen
  part_of_speech: verb
  status: approved
  meanings:
  - id: calculate
    definition: einen Wert mit einer festgelegten mathematischen Beziehung bestimmen
  review_status: provisional_v0.2
- entry_id: DE-NOU-bereich
  lemma: Bereich
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.area
    definition: räumlich, funktional oder dokumentarisch abgegrenzter Teil
  review_status: provisional_v0.2
  gender: masc
  plural: Bereiche
  restrictions:
  - Art des Bereichs nennen, wenn nicht eindeutig.
- entry_id: DE-VER-bereitstellen
  lemma: bereitstellen
  part_of_speech: verb
  status: approved
  meanings:
  - id: provide.available
    definition: ein ausdrücklich genanntes Objekt, Signal, eine Ressource oder Funktion für die Verwendung verfügbar
      machen
  review_status: corpus_candidate_v0.3
  separable: true
  prefix: bereit
  surface_forms:
  - bereitgestellt
- entry_id: DE-VER-ber-hren
  lemma: berühren
  part_of_speech: verb
  status: approved
  meanings:
  - id: touch
    definition: physischen Kontakt mit einem Objekt oder einer Oberfläche herstellen
  review_status: provisional_v0.2
- entry_id: DE-VER-beschreiben
  lemma: beschreiben
  part_of_speech: verb
  status: approved
  meanings:
  - id: describe
    definition: Eigenschaften, Aufbau, Funktion oder Ablauf eines ausdrücklich genannten Gegenstands sachlich darstellen
  review_status: corpus_candidate_v0.3
  surface_forms:
  - beschreibe
  - beschreibst
  - beschreibt
  - beschreiben
  - beschrieb
  - beschrieben
- entry_id: DE-NOU-beschreibung
  lemma: Beschreibung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.description
    definition: Text, der technische Information gibt und keine direkte Arbeitsanweisung ist
  review_status: provisional_v0.2
  gender: fem
  plural: Beschreibungen
- entry_id: DE-ADJ-besch-digt
  lemma: beschädigt
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.damaged
    definition: weist einen Schaden auf, der im anwendbaren Prüf- oder Reparaturkriterium als Schaden gilt
  review_status: provisional_v0.2
  restrictions:
  - Bei Akzeptanzentscheidungen Schadenskriterium oder Referenz angeben.
- entry_id: DE-VER-bestehen
  lemma: bestehen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: verb.consist_with_aus
    definition: zusammen mit der Präposition aus die Bestandteile eines ausdrücklich genannten Objekts angeben
  review_status: corpus_candidate_v0.3
  surface_forms:
  - bestehe
  - bestehst
  - besteht
  - bestehen
  - bestand
  - bestanden
  restrictions:
  - Nur im Muster „X besteht aus Y“ für Zusammensetzung verwenden. Andere Bedeutungen sind nicht zentral freigegeben.
- entry_id: DE-VER-best-tigen
  lemma: bestätigen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: confirm
    definition: eine Information oder Auswahl ausdrücklich als erhalten, korrekt oder akzeptiert kennzeichnen
  review_status: provisional_v0.2
  restrictions:
  - Nicht verwenden, wenn eigentlich prüfen oder genehmigen gemeint ist.
- entry_id: DE-VER-betreiben
  lemma: betreiben
  part_of_speech: verb
  status: approved
  meanings:
  - id: operate.transitive
    definition: ein Gerät oder System aktiv bedienen oder in seinem vorgesehenen Betriebszustand halten
  review_status: provisional_v0.2
- entry_id: DE-NOU-betreiber
  lemma: Betreiber
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.operator
    definition: Organisation oder Rolle, die ein System verantwortlich betreibt
  review_status: provisional_v0.2
  gender: masc
  plural: Betreiber
  restrictions:
  - Offizielle Rollenbezeichnung hat Vorrang.
- entry_id: DE-NOU-betrieb
  lemma: Betrieb
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.operation
    definition: Zustand oder Tätigkeit, in der ein System seine vorgesehene Funktion ausführt
  review_status: provisional_v0.2
  gender: masc
- entry_id: DE-NOU-betriebsanleitung
  lemma: Betriebsanleitung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.betriebsanleitung
    definition: offizielle Anleitung für sicheren Betrieb, Bedienung oder Instandhaltung eines Produkts
  review_status: multi_industry_candidate_v0.4
  plural: Betriebsanleitungen
- entry_id: DE-CON-bevor
  lemma: bevor
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.before
    definition: ordnet eine Handlung oder einen Zustand zeitlich vor einer anderen Handlung an
  review_status: provisional_v0.2
- entry_id: DE-VER-bewegen
  lemma: bewegen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: move
    definition: die Position eines Objekts ändern
  review_status: provisional_v0.2
  restrictions:
  - Richtung oder Ziel nennen, wenn relevant.
- entry_id: DE-VER-biegen
  lemma: biegen
  part_of_speech: verb
  status: approved
  meanings:
  - id: bend
    definition: die Form eines Werkstücks durch Biegung verändern
  review_status: provisional_v0.2
- entry_id: DE-VER-bilden
  lemma: bilden
  part_of_speech: verb
  status: restricted
  meanings:
  - id: form.constitute
    definition: ausdrücken, dass ausdrücklich genannte Teile zusammen eine klar bezeichnete Einheit oder Struktur
      ergeben
  review_status: corpus_candidate_v0.3
  surface_forms:
  - bilde
  - bildest
  - bildet
  - bilden
  - bildete
  - gebildet
  restrictions:
  - Nur für eine konkrete Zusammensetzung oder Struktur verwenden. Für „darstellen“ oder „erzeugen“ das präzisere
    Verb verwenden.
- entry_id: DE-CON-bis
  lemma: bis
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.until
    definition: kennzeichnet den Endzustand oder Endzeitpunkt einer fortgesetzten Handlung
  review_status: provisional_v0.2
- entry_id: DE-PRE-bis
  lemma: bis
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.up_to
    definition: kennzeichnet eine obere räumliche, zeitliche oder numerische Grenze
  review_status: provisional_v0.2
- entry_id: DE-VER-bleiben
  lemma: bleiben
  part_of_speech: verb
  status: approved
  meanings:
  - id: remain.state
    definition: in einem Zustand oder an einer Position fortbestehen
  review_status: provisional_v0.2
  surface_forms:
  - bleibe
  - bleibst
  - bleibt
  - bleiben
  - blieb
  - blieben
  - geblieben
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-ADJ-breit
  lemma: breit
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.wide
    definition: hat eine große Ausdehnung in Breitenrichtung relativ zur ausdrücklich genannten Referenz
  review_status: provisional_v0.2
- entry_id: DE-NOU-breite
  lemma: Breite
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.width
    definition: lineare Abmessung in der festgelegten Breitenrichtung
  review_status: provisional_v0.2
  gender: fem
  plural: Breiten
- entry_id: DE-CON-damit
  lemma: damit
  part_of_speech: conjunction
  status: restricted
  meanings:
  - id: conj.so_that
    definition: leitet den ausdrücklich genannten Zweck einer Handlung ein
  review_status: provisional_v0.2
  restrictions:
  - Nicht als Pronomen verwenden. Bei langen Sätzen den Zweck in einen eigenen Satz aufteilen.
- entry_id: DE-ADV-danach
  lemma: danach
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.afterwards
    definition: kennzeichnet eine Handlung oder einen Zustand nach dem unmittelbar vorher genannten Ereignis
  review_status: provisional_v0.2
- entry_id: DE-ADV-dann
  lemma: dann
  part_of_speech: adverb
  status: approved
  meanings:
  - id: sequence.then
    definition: kennzeichnet den ausdrücklich nächsten Schritt oder Zustand in einer zeitlichen Reihenfolge
  review_status: corpus_candidate_v0.3
- entry_id: DE-VER-darstellen
  lemma: darstellen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: represent.show
    definition: Information in einer Abbildung, Tabelle, Anzeige oder strukturierten Darstellung sichtbar wiedergeben
  review_status: corpus_candidate_v0.3
  separable: true
  prefix: dar
  surface_forms:
  - dargestellt
  restrictions:
  - Darstellung oder Informationsquelle nennen. Nicht als stilistisches Synonym für sein, bilden oder beschreiben
    verwenden.
- entry_id: DE-CON-dass
  lemma: dass
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.that
    definition: leitet einen Inhaltssatz ein, der den Inhalt einer Aussage, Prüfung oder Feststellung angibt
  review_status: provisional_v0.2
  approved_examples:
  - Stellen Sie sicher, dass das Ventil geschlossen ist.
- entry_id: DE-NOU-daten
  lemma: Daten
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.daten
    definition: digital oder analog dargestellte technische Informationen, Messwerte oder gespeicherte Inhalte
  review_status: multi_industry_candidate_v0.4
  plural: Daten
  restrictions:
  - Nicht als Plural von Datum interpretieren. Kontext muss technische Informationen oder Werte bezeichnen.
  approved_examples:
  - Speichern Sie die Daten.
- entry_id: DE-NOU-datum
  lemma: Datum
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.date
    definition: Kalenderangabe eines bestimmten Tages
  review_status: corrected_v0.4_lexical_collision
  gender: neut
  plural: Daten
  restrictions:
  - Im technischen Informationskontext bezeichnet Daten das eigene Lemma Daten und nicht den Plural von Datum.
- entry_id: DE-NOU-dauer
  lemma: Dauer
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.duration
    definition: Zeitspanne zwischen Beginn und Ende eines Ereignisses
  review_status: provisional_v0.2
  gender: fem
  plural: Dauern
- entry_id: DE-ADV-davor
  lemma: davor
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.beforehand
    definition: kennzeichnet eine Handlung oder einen Zustand vor dem unmittelbar danach genannten oder zuvor referenzierten
      Ereignis
  review_status: provisional_v0.2
  restrictions:
  - Nur verwenden, wenn der Bezug eindeutig ist.
- entry_id: DE-VER-deaktivieren
  lemma: deaktivieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: deactivate
    definition: eine Funktion oder ein System in den freigegebenen inaktiven Zustand bringen
  review_status: provisional_v0.2
- entry_id: DE-VER-definieren
  lemma: definieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: define
    definition: Bedeutung, Grenze, Parameter oder Eigenschaft eines ausdrücklich genannten Elements verbindlich
      festlegen
  review_status: corpus_candidate_v0.3
  surface_forms:
  - definiere
  - definierst
  - definiert
  - definieren
  - definierte
- entry_id: DE-VER-deinstallieren
  lemma: deinstallieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: uninstall.software
    definition: installierte Software kontrolliert aus einem System entfernen
  review_status: provisional_v0.2
- entry_id: DE-ART-der
  lemma: der
  part_of_speech: article
  status: approved
  meanings:
  - id: article.definite
    definition: bestimmter Artikel für ein bereits bestimmtes oder eindeutig identifiziertes Substantiv
  review_status: provisional_v0.2
  surface_forms:
  - der
  - die
  - das
  - den
  - dem
  - des
- entry_id: DE-ADV-derzeit
  lemma: derzeit
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.currently
    definition: kennzeichnet den zum Dokumentzeitpunkt geltenden Zustand
  review_status: provisional_v0.2
  restrictions:
  - Bei versionskritischen Informationen zusätzlich Version oder Datum nennen.
- entry_id: DE-ADV-deshalb
  lemma: deshalb
  part_of_speech: adverb
  status: approved
  meanings:
  - id: result.therefore
    definition: kennzeichnet einen direkten Folgezusammenhang zur vorherigen Aussage
  review_status: corpus_candidate_v0.3
- entry_id: DE-VER-dienen
  lemma: dienen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: serve.function
    definition: die ausdrücklich festgelegte technische Funktion oder den Zweck eines Objekts angeben
  review_status: corpus_candidate_v0.3
  surface_forms:
  - diene
  - dienst
  - dient
  - dienen
  - diente
  - gedient
  restrictions:
  - Funktion oder Zweck konkret nennen; nicht für allgemeine Nutzenbehauptungen verwenden.
- entry_id: DE-PRO-dies
  lemma: dies
  part_of_speech: pronoun
  status: restricted
  meanings:
  - id: pronoun.this
    definition: verweist auf einen eindeutig bestimmten vorherigen Sachverhalt
  review_status: provisional_v0.2
  surface_forms:
  - dies
  restrictions:
  - Wenn der Bezug nicht eindeutig ein Satz oder Sachverhalt ist, das Substantiv wiederholen.
- entry_id: DE-DET-dieser
  lemma: dieser
  part_of_speech: determiner
  status: restricted
  meanings:
  - id: determiner.this
    definition: verweist auf ein eindeutig bestimmtes, bereits genanntes Substantiv
  review_status: provisional_v0.2
  surface_forms:
  - dieser
  - diese
  - dieses
  - diesen
  - diesem
  restrictions:
  - Nur verwenden, wenn genau ein möglicher Bezug besteht. Das Substantiv nach dem Determinierer nennen.
- entry_id: DE-ADJ-direkt
  lemma: direkt
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.direct
    definition: ohne Zwischenstufe, Umlenkung oder vermittelndes Element
  review_status: provisional_v0.2
- entry_id: DE-ADV-direkt
  lemma: direkt
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.directly
    definition: kennzeichnet eine unmittelbare Verbindung, Lage oder Folge ohne Zwischenstufe
  review_status: provisional_v0.2
  restrictions:
  - Nicht als bloße Verstärkung verwenden.
- entry_id: DE-VER-dividieren
  lemma: dividieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: divide.math
    definition: einen numerischen Wert mathematisch durch einen anderen teilen
  review_status: provisional_v0.2
- entry_id: DE-NOU-dokument
  lemma: Dokument
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.document
    definition: abgegrenzte Informationsquelle mit eigener Identifikation oder Funktion
  review_status: provisional_v0.2
  gender: neut
  plural: Dokumente
- entry_id: DE-NOU-dokumentation
  lemma: Dokumentation
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.dokumentation
    definition: geordnete Menge technischer Dokumente oder aufgezeichneter technischer Informationen
  review_status: multi_industry_candidate_v0.4
  plural: Dokumentationen
  restrictions:
  - Für ein einzelnes Dokument den konkreten Dokumenttyp verwenden.
- entry_id: DE-VER-dokumentieren
  lemma: dokumentieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: document
    definition: eine technische Tatsache, Entscheidung oder ein Ergebnis in einem vorgesehenen Dokumentationssystem
      festhalten
  review_status: provisional_v0.2
- entry_id: DE-ADV-dort
  lemma: dort
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.there
    definition: verweist auf einen zuvor eindeutig identifizierten Ort
  review_status: provisional_v0.2
  restrictions:
  - Ort wiederholen, wenn mehr als ein möglicher Bezug besteht.
- entry_id: DE-VER-drehen
  lemma: drehen
  part_of_speech: verb
  status: approved
  meanings:
  - id: turn.rotate
    definition: ein Objekt um eine Achse oder einen Punkt bewegen
  review_status: provisional_v0.2
- entry_id: DE-QUA-drei
  lemma: drei
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.three
    definition: bezeichnet die Zahl 3 in ausgeschriebener Form
  review_status: corpus_candidate_v0.3
- entry_id: DE-VER-dr-cken
  lemma: drücken
  part_of_speech: verb
  status: approved
  meanings:
  - id: push.press
    definition: eine Kraft auf eine Fläche oder in Richtung weg vom Kraftausübenden ausüben
  review_status: provisional_v0.2
- entry_id: DE-PRE-durch
  lemma: durch
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.through
    definition: kennzeichnet einen Weg durch einen Raum, eine Öffnung oder ein Material
  review_status: provisional_v0.2
  restrictions:
  - Nicht als unklaren Ersatz für eine Ursache oder ein Werkzeug verwenden.
- entry_id: DE-VER-d-rfen
  lemma: dürfen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: may.permission
    definition: Erlaubnis ausdrücken
  - id: may.prohibition
    definition: mit nicht ein Verbot ausdrücken
  review_status: provisional_v0.2
  surface_forms:
  - darf
  - darfst
  - dürfen
  - dürft
  - durfte
  - durften
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-ART-ein
  lemma: ein
  part_of_speech: article
  status: approved
  meanings:
  - id: article.indefinite
    definition: unbestimmter Artikel für ein neu eingeführtes einzelnes zählbares Substantiv
  review_status: provisional_v0.2
  surface_forms:
  - ein
  - eine
  - einen
  - einem
  - einer
  - eines
- entry_id: DE-VER-einbauen
  lemma: einbauen
  part_of_speech: verb
  status: approved
  meanings:
  - id: install.mechanical
    definition: ein mechanisches oder elektrisches Bauteil in seine vorgesehene Einbauposition bringen
  review_status: provisional_v0.2
  separable: true
  prefix: ein
  surface_forms:
  - eingebaut
- entry_id: DE-VER-einf-gen
  lemma: einfügen
  part_of_speech: verb
  status: approved
  meanings:
  - id: paste.insert
    definition: digitale Daten oder ein Element an einer bestimmten Position ergänzen
  review_status: provisional_v0.2
  separable: true
  prefix: ein
- entry_id: DE-ADJ-eingebaut
  lemma: eingebaut
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.installed
    definition: in der vorgesehenen Einbauposition vorhanden
  review_status: provisional_v0.2
- entry_id: DE-VER-eingeben
  lemma: eingeben
  part_of_speech: verb
  status: approved
  meanings:
  - id: enter.data
    definition: Daten in ein System übertragen oder erfassen
  review_status: provisional_v0.2
  separable: true
  prefix: ein
- entry_id: DE-ADJ-eingeschaltet
  lemma: eingeschaltet
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.on
    definition: im aktiven Energie- oder Betriebszustand
  review_status: provisional_v0.2
- entry_id: DE-VER-einhalten
  lemma: einhalten
  part_of_speech: verb
  status: restricted
  meanings:
  - id: comply.limit
    definition: einen ausdrücklich genannten Grenzwert, Abstand, Zeitraum oder eine Anforderung nicht überschreiten
      oder unterschreiten
  review_status: corpus_candidate_v0.3
  separable: true
  prefix: ein
  surface_forms:
  - eingehalten
  restrictions:
  - Grenzwert oder referenzierte Anforderung muss eindeutig identifiziert sein.
- entry_id: DE-NOU-einheit
  lemma: Einheit
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.unit
    definition: definierte funktionale oder physische Einheit oder Maßeinheit
  review_status: provisional_v0.2
  gender: fem
  plural: Einheiten
  restrictions:
  - Bedeutung muss aus Kontext eindeutig sein.
- entry_id: DE-QUA-einige
  lemma: einige
  part_of_speech: quantifier
  status: restricted
  meanings:
  - id: quantifier.some
    definition: bezeichnet eine nicht genau bestimmte Teilmenge
  review_status: provisional_v0.2
  restrictions:
  - Nicht in Anweisungen verwenden, wenn die genaue Menge bekannt oder sicherheitsrelevant ist.
- entry_id: DE-VER-einrasten
  lemma: einrasten
  part_of_speech: verb
  status: restricted
  meanings:
  - id: latch
    definition: in eine definierte Rast- oder Verriegelungsposition gelangen oder gebracht werden
  review_status: provisional_v0.2
  separable: true
  prefix: ein
- entry_id: DE-QUA-eins
  lemma: eins
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.one
    definition: bezeichnet die Zahl 1 in ausgeschriebener Form
  review_status: provisional_v0.2
- entry_id: DE-VER-einschalten
  lemma: einschalten
  part_of_speech: verb
  status: approved
  meanings:
  - id: switch.on
    definition: ein Gerät, System oder eine Funktion in den aktiven Energie- oder Betriebszustand bringen
  review_status: provisional_v0.2
  separable: true
  prefix: ein
  prohibited_synonyms:
  - anmachen
- entry_id: DE-VER-einstellen
  lemma: einstellen
  part_of_speech: verb
  status: approved
  meanings:
  - id: set.adjust
    definition: einen Parameter oder ein Bedienelement auf einen festgelegten Wert oder Zustand bringen
  review_status: provisional_v0.2
  separable: true
  prefix: ein
  surface_forms:
  - eingestellt
- entry_id: DE-NOU-einstellung
  lemma: Einstellung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.einstellung
    definition: festgelegter oder auswählbarer Wert oder Zustand eines Systems oder Parameters
  review_status: multi_industry_candidate_v0.4
  plural: Einstellungen
  restrictions:
  - Nicht für die allgemeine Haltung oder Meinung einer Person verwenden.
- entry_id: DE-VER-empfangen
  lemma: empfangen
  part_of_speech: verb
  status: approved
  meanings:
  - id: receive
    definition: übertragene Daten, ein Signal oder eine Nachricht aufnehmen
  review_status: provisional_v0.2
- entry_id: DE-VER-empfehlen
  lemma: empfehlen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: recommend
    definition: eine nicht verbindliche bevorzugte Handlung ausdrücklich als Empfehlung kennzeichnen
  review_status: provisional_v0.2
  restrictions:
  - Nicht verwenden, wenn eine Pflicht oder Sicherheitsanforderung gemeint ist.
- entry_id: DE-NOU-ende
  lemma: Ende
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.end
    definition: letzter Punkt oder Abschluss eines ausdrücklich bestimmten Ablaufs oder Bereichs
  review_status: provisional_v0.2
  gender: neut
  plural: Enden
- entry_id: DE-ADJ-eng
  lemma: eng
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.narrow
    definition: hat eine geringe lichte Weite oder einen kleinen Abstand relativ zur ausdrücklich genannten Referenz
  review_status: provisional_v0.2
- entry_id: DE-VER-entfalten
  lemma: entfalten
  part_of_speech: verb
  status: approved
  meanings:
  - id: unfold
    definition: ein gefaltetes Teil in seine vorgesehene offene Form bringen
  review_status: provisional_v0.2
- entry_id: DE-VER-entfernen
  lemma: entfernen
  part_of_speech: verb
  status: approved
  meanings:
  - id: remove
    definition: ein Objekt von einer Position, Oberfläche oder Verbindung wegnehmen
  review_status: provisional_v0.2
- entry_id: DE-ADJ-entfernt
  lemma: entfernt
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.removed
    definition: nicht mehr an der zuvor bezeichneten Position vorhanden
  review_status: provisional_v0.2
- entry_id: DE-VER-enthalten
  lemma: enthalten
  part_of_speech: verb
  status: approved
  meanings:
  - id: contain
    definition: ausdrücken, dass ein Objekt, Dokument oder Datensatz ausdrücklich genannte Bestandteile oder Informationen
      umfasst
  review_status: corpus_candidate_v0.3
  surface_forms:
  - enthalte
  - enthältst
  - enthält
  - enthalten
  - enthielt
- entry_id: DE-VER-entladen
  lemma: entladen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: discharge.electrical
    definition: elektrische Ladung oder gespeicherte elektrische Energie kontrolliert verringern oder entfernen
  review_status: provisional_v0.2
- entry_id: DE-VER-entleeren
  lemma: entleeren
  part_of_speech: verb
  status: approved
  meanings:
  - id: empty
    definition: Material, Flüssigkeit oder Gas vollständig aus einem Behälter oder Raum entfernen
  review_status: provisional_v0.2
- entry_id: DE-VER-entl-ften
  lemma: entlüften
  part_of_speech: verb
  status: approved
  meanings:
  - id: bleed.vent
    definition: Luft oder Gas kontrolliert aus einem System oder einer Leitung entfernen
  review_status: provisional_v0.2
- entry_id: DE-VER-entriegeln
  lemma: entriegeln
  part_of_speech: verb
  status: approved
  meanings:
  - id: unlock
    definition: eine mechanische oder logische Verriegelung aus dem gesicherten Zustand freigeben
  review_status: provisional_v0.2
- entry_id: DE-ADJ-entriegelt
  lemma: entriegelt
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.unlocked
    definition: nicht verriegelt und für die vorgesehene Bewegung freigegeben
  review_status: provisional_v0.2
- entry_id: DE-VER-entsprechen
  lemma: entsprechen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: conform.reference
    definition: mit einer ausdrücklich genannten Anforderung, Spezifikation oder Referenz übereinstimmen
  review_status: corpus_candidate_v0.3
  surface_forms:
  - entspreche
  - entsprichst
  - entspricht
  - entsprechen
  - entsprach
  - entsprochen
  restrictions:
  - Referenz oder Anforderung ausdrücklich nennen.
- entry_id: DE-PHR-entweder-oder
  lemma: entweder ... oder
  part_of_speech: phrase
  status: approved
  meanings:
  - id: alternative.exclusive_or_open
    definition: kennzeichnet zwei ausdrücklich genannte Alternativen
  review_status: corpus_candidate_v0.3
  surface_forms:
  - entweder ... oder
  restrictions:
  - Wenn beide Alternativen gleichzeitig möglich sind, diese Möglichkeit ausdrücklich nennen.
- entry_id: DE-VER-erden
  lemma: erden
  part_of_speech: verb
  status: restricted
  meanings:
  - id: ground
    definition: eine elektrische Verbindung zur festgelegten Erde oder Masse herstellen
  review_status: provisional_v0.2
  restrictions:
  - Nur im elektrischen Sinn verwenden.
- entry_id: DE-ADJ-erforderlich
  lemma: erforderlich
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.necessary
    definition: für die Erfüllung einer ausdrücklich genannten Anforderung notwendig
  review_status: provisional_v0.2
  restrictions:
  - Nicht als versteckte Anweisung verwenden; in Verfahren direkte Anweisung geben.
- entry_id: DE-NOU-ergebnis
  lemma: Ergebnis
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.result
    definition: festgestellter Wert oder Zustand, der aus einer Handlung, Prüfung oder Berechnung folgt
  review_status: provisional_v0.2
  gender: neut
  plural: Ergebnisse
- entry_id: DE-VER-erh-hen
  lemma: erhöhen
  part_of_speech: verb
  status: approved
  meanings:
  - id: increase.transitive
    definition: einen numerischen Wert größer machen
  review_status: provisional_v0.2
- entry_id: DE-VER-erkennen
  lemma: erkennen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: detect
    definition: durch Sensorik, Messung oder eindeutige Merkmale das Vorhandensein eines Zustands feststellen
  review_status: provisional_v0.2
  restrictions:
  - Bei formaler Sensor- oder Erkennungsfunktion als technisches Verb im Projektterminologiebestand führen.
- entry_id: DE-ADV-erneut
  lemma: erneut
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.again
    definition: kennzeichnet die Wiederholung derselben Handlung oder Prüfung
  review_status: provisional_v0.2
- entry_id: DE-VER-erreichen
  lemma: erreichen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: reach.threshold_position
    definition: einen ausdrücklich genannten Wert, Grenzwert, Zustand oder eine Position erreichen
  review_status: corpus_candidate_v0.3
  surface_forms:
  - erreiche
  - erreichst
  - erreicht
  - erreichen
  - erreichte
  restrictions:
  - Zielwert, Zustand oder Position nennen.
- entry_id: DE-VER-ersetzen
  lemma: ersetzen
  part_of_speech: verb
  status: approved
  meanings:
  - id: replace
    definition: ein vorhandenes Objekt durch ein anderes Objekt mit derselben vorgesehenen Funktion austauschen
  review_status: provisional_v0.2
- entry_id: DE-VER-erweitern
  lemma: erweitern
  part_of_speech: verb
  status: restricted
  meanings:
  - id: expand
    definition: Größe, Umfang oder Funktionsumfang in eine ausdrücklich genannte Richtung vergrößern
  review_status: provisional_v0.2
  restrictions:
  - Art und Ziel der Erweiterung nennen.
- entry_id: DE-VER-erzeugen
  lemma: erzeugen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: generate.output
    definition: ein ausdrücklich genanntes physisches, elektrisches oder informationstechnisches Ergebnis hervorbringen
  review_status: corpus_candidate_v0.3
  surface_forms:
  - erzeuge
  - erzeugst
  - erzeugt
  - erzeugen
  - erzeugte
  restrictions:
  - Ergebnis oder Ausgangsgröße nennen.
- entry_id: DE-PRO-es
  lemma: es
  part_of_speech: pronoun
  status: restricted
  meanings:
  - id: pronoun.it
    definition: ersetzt ein eindeutig identifiziertes neutrales Substantiv oder dient in unpersönlichen Konstruktionen
  review_status: provisional_v0.2
  surface_forms:
  - es
  restrictions:
  - Nicht verwenden, wenn mehr als ein plausibler Bezug besteht.
- entry_id: DE-PHR-es-gibt
  lemma: es gibt
  part_of_speech: phrase
  status: restricted
  meanings:
  - id: exist.there_is
    definition: drückt aus, dass ein ausdrücklich genanntes Objekt oder ein Zustand vorhanden ist
  review_status: provisional_v0.2
  restrictions:
  - Nur verwenden, wenn der Existenzbezug klarer ist als vorhanden sein.
- entry_id: DE-ADJ-extern
  lemma: extern
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.external
    definition: außerhalb des ausdrücklich genannten Systems, Geräts oder organisatorischen Bereichs
  review_status: provisional_v0.2
- entry_id: DE-NOU-fachpersonal
  lemma: Fachpersonal
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.fachpersonal
    definition: Personen mit der für eine ausdrücklich genannte technische Tätigkeit erforderlichen Qualifikation
  review_status: multi_industry_candidate_v0.4
  plural: Fachpersonal
  restrictions:
  - Erforderliche Qualifikation oder Rollenbezeichnung angeben, wenn sie sicherheitsrelevant ist.
- entry_id: DE-ADJ-falsch
  lemma: falsch
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.incorrect
    definition: entspricht einer eindeutig festgelegten Tatsache, Auswahl oder Anforderung nicht
  review_status: provisional_v0.2
- entry_id: DE-VER-falten
  lemma: falten
  part_of_speech: verb
  status: approved
  meanings:
  - id: fold
    definition: Material oder ein flexibles Teil entlang einer Linie umlegen
  review_status: provisional_v0.2
- entry_id: DE-ADJ-fehlend
  lemma: fehlend
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.missing
    definition: an der erwarteten Stelle nicht vorhanden
  review_status: provisional_v0.2
- entry_id: DE-NOU-fehler
  lemma: Fehler
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.error_fault
    definition: Abweichung von einer definierten Funktion, Anforderung oder korrekten Information
  review_status: provisional_v0.2
  gender: masc
  plural: Fehler
  restrictions:
  - Fehlertyp nennen, wenn mehrere Bedeutungen möglich sind.
- entry_id: DE-ADJ-fehlerhaft
  lemma: fehlerhaft
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.faulty
    definition: erfüllt eine definierte funktionale oder Datenanforderung nicht
  review_status: provisional_v0.2
  restrictions:
  - Konkrete Abweichung nennen, wenn möglich.
- entry_id: DE-ADJ-fern
  lemma: fern
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.far
    definition: hat einen großen Abstand zur ausdrücklich genannten Referenz
  review_status: provisional_v0.2
  restrictions:
  - Wenn der Abstand relevant ist, Grenzwert nennen.
- entry_id: DE-ADJ-fest
  lemma: fest
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.tight
    definition: mechanisch so gehalten oder angezogen, dass die definierte Bewegung oder Lockerung nicht auftritt
  review_status: provisional_v0.2
  restrictions:
  - Bei Schraubverbindungen bevorzugt Drehmoment oder Prüfkriterium angeben.
- entry_id: DE-VER-festlegen
  lemma: festlegen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: specify.set
    definition: einen Wert, Zustand, Ablauf oder eine Anforderung ausdrücklich und verbindlich bestimmen
  review_status: corpus_candidate_v0.3
  separable: true
  prefix: fest
  surface_forms:
  - festgelegt
  restrictions:
  - Festgelegtes Element und Wert/Regel nennen.
- entry_id: DE-VER-festziehen
  lemma: festziehen
  part_of_speech: verb
  status: approved
  meanings:
  - id: tighten
    definition: eine Schraub- oder Klemmverbindung bis zum festgelegten Zustand oder Drehmoment anziehen
  review_status: provisional_v0.2
  separable: true
  prefix: fest
- entry_id: DE-VER-finden
  lemma: finden
  part_of_speech: verb
  status: approved
  meanings:
  - id: find
    definition: das Vorhandensein eines gesuchten oder unerwarteten Elements oder Zustands feststellen
  review_status: provisional_v0.2
- entry_id: DE-NOU-folge
  lemma: Folge
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.consequence
    definition: Wirkung oder Ergebnis, das aus einer ausdrücklich genannten Ursache entsteht
  review_status: provisional_v0.2
  gender: fem
  plural: Folgen
- entry_id: DE-ADJ-folgend
  lemma: folgend
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.folgend
    definition: im Dokument oder in einer festgelegten Reihenfolge unmittelbar danach kommend
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - folgende
  - folgenden
  - folgender
  - folgendes
  - folgendem
  restrictions:
  - Nur verwenden, wenn die Reihenfolge eindeutig ist.
- entry_id: DE-NOU-form
  lemma: Form
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.form
    definition: geometrische Gestalt oder festgelegte sprachliche/strukturelle Ausprägung
  review_status: provisional_v0.2
  gender: fem
  plural: Formen
- entry_id: DE-VER-formatieren
  lemma: formatieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: format
    definition: ein digitales Speichermedium oder Datenobjekt nach einer festgelegten Struktur vorbereiten
  review_status: provisional_v0.2
  restrictions:
  - Nicht im Sinn von Textgestaltung verwenden, sofern dies nicht ausdrücklich gemeint ist.
- entry_id: DE-VER-fortsetzen
  lemma: fortsetzen
  part_of_speech: verb
  status: approved
  meanings:
  - id: continue
    definition: einen unterbrochenen Vorgang ab seinem Unterbrechungspunkt weiterführen
  review_status: provisional_v0.2
- entry_id: DE-VER-freigeben
  lemma: freigeben
  part_of_speech: verb
  status: restricted
  meanings:
  - id: release.approve
    definition: ein zuvor gesperrtes Objekt, Signal, Verfahren oder einen Zustand ausdrücklich zur Verwendung zulassen
  review_status: provisional_v0.2
  separable: true
  prefix: frei
  restrictions:
  - Nicht mit mechanischem loslassen verwechseln. Freigabeart muss aus dem Kontext eindeutig sein.
- entry_id: DE-NOU-funktion
  lemma: Funktion
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.function
    definition: vorgesehene technische Aufgabe oder Wirkung eines Systems, Bauteils oder Prozesses
  review_status: provisional_v0.2
  gender: fem
  plural: Funktionen
- entry_id: DE-VER-funktionieren
  lemma: funktionieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: operate.correctly
    definition: die vorgesehene Funktion ohne den beschriebenen Fehler erfüllen
  review_status: provisional_v0.2
  restrictions:
  - Wenn ein konkretes Leistungskriterium existiert, dieses Kriterium angeben.
- entry_id: DE-VER-f-llen
  lemma: füllen
  part_of_speech: verb
  status: approved
  meanings:
  - id: fill
    definition: Material, Flüssigkeit oder Gas in einen Behälter oder Raum einbringen
  review_status: provisional_v0.2
- entry_id: DE-QUA-fuenf
  lemma: fünf
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.five
    definition: bezeichnet die Zahl 5 in ausgeschriebener Form
  review_status: corpus_candidate_v0.3
- entry_id: DE-PRE-f-r
  lemma: für
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.for
    definition: kennzeichnet Zweck, Zielgruppe oder Zuordnung
  review_status: provisional_v0.2
- entry_id: DE-ADJ-gebraucht
  lemma: gebraucht
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.used
    definition: bereits verwendet und nicht als neu klassifiziert
  review_status: provisional_v0.2
- entry_id: DE-NOU-gefahr
  lemma: Gefahr
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.hazard
    definition: Quelle oder Situation mit möglichem Schaden für Personen, Objekte oder Umwelt
  review_status: provisional_v0.2
  gender: fem
  plural: Gefahren
  restrictions:
  - Risikoklassifikation richtet sich nach anwendbarem Sicherheitsstandard.
- entry_id: DE-PRE-gegen
  lemma: gegen
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.against
    definition: kennzeichnet physischen Kontakt, entgegengesetzte Richtung oder eine definierte Gegenkraft
  review_status: provisional_v0.2
- entry_id: DE-NOU-ger-t
  lemma: Gerät
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.device
    definition: technische Einheit, die eine oder mehrere vorgesehene Funktionen ausführt
  review_status: provisional_v0.2
  gender: neut
  plural: Geräte
  restrictions:
  - Offizielle Produktbenennung hat Vorrang.
- entry_id: DE-ADJ-geschlossen
  lemma: geschlossen
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.closed
    definition: in einem definierten geschlossenen Zustand
  review_status: provisional_v0.2
- entry_id: DE-ADJ-getrennt
  lemma: getrennt
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.disconnected
    definition: nicht mit dem ausdrücklich genannten Objekt verbunden
  review_status: provisional_v0.2
- entry_id: DE-ADJ-gleich
  lemma: gleich
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.equal
    definition: hat denselben ausdrücklich verglichenen Wert, Zustand oder dieselbe Identität
  review_status: provisional_v0.2
  restrictions:
  - Vergleichsmerkmal muss eindeutig sein.
- entry_id: DE-ADV-gleichzeitig
  lemma: gleichzeitig
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.simultaneously
    definition: kennzeichnet Handlungen oder Zustände, die im selben Zeitraum stattfinden
  review_status: provisional_v0.2
- entry_id: DE-NOU-grenze
  lemma: Grenze
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.limit
    definition: Wert oder Position, die einen zulässigen oder definierten Bereich begrenzt
  review_status: provisional_v0.2
  gender: fem
  plural: Grenzen
- entry_id: DE-ADJ-gro
  lemma: groß
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.large
    definition: hat eine größere physische Abmessung als die ausdrücklich genannte Referenz
  review_status: provisional_v0.2
  restrictions:
  - Wenn möglich konkrete Abmessung nennen.
- entry_id: DE-NOU-grund
  lemma: Grund
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.reason
    definition: ausdrücklich genannte Ursache oder Begründung für eine Aussage oder Handlung
  review_status: provisional_v0.2
  gender: masc
  plural: Gründe
  restrictions:
  - Für technische Kausalität bevorzugt Ursache verwenden.
- entry_id: DE-VER-haben
  lemma: haben
  part_of_speech: verb
  status: approved
  meanings:
  - id: have.possess
    definition: etwas besitzen, enthalten oder als Teil aufweisen
  review_status: provisional_v0.2
  surface_forms:
  - habe
  - hast
  - hat
  - haben
  - habt
  - hatte
  - hatten
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-VER-halten
  lemma: halten
  part_of_speech: verb
  status: approved
  meanings:
  - id: hold
    definition: ein Objekt oder einen Zustand an einer Position oder einem Wert beibehalten
  review_status: provisional_v0.2
- entry_id: DE-VER-heben
  lemma: heben
  part_of_speech: verb
  status: approved
  meanings:
  - id: lift
    definition: ein Objekt in eine höhere Position bewegen
  review_status: provisional_v0.2
- entry_id: DE-NOU-hersteller
  lemma: Hersteller
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.manufacturer
    definition: Organisation, die ein Produkt herstellt und als Hersteller verantwortlich zeichnet
  review_status: provisional_v0.2
  gender: masc
  plural: Hersteller
- entry_id: DE-VER-herunterladen
  lemma: herunterladen
  part_of_speech: verb
  status: approved
  meanings:
  - id: download
    definition: Daten von einem entfernten System auf das lokale System übertragen
  review_status: provisional_v0.2
  separable: true
  prefix: herunter
- entry_id: DE-ADV-hier
  lemma: hier
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.here
    definition: verweist auf den unmittelbar aktuellen Dokument- oder Ortskontext
  review_status: provisional_v0.2
  restrictions:
  - Nicht verwenden, wenn der Referenzort nicht eindeutig ist.
- entry_id: DE-PRE-hinter
  lemma: hinter
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.behind
    definition: kennzeichnet eine Position auf der Rückseite oder weiter hinten als ein Referenzobjekt
  review_status: provisional_v0.2
- entry_id: DE-NOU-hinweis
  lemma: Hinweis
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.note
    definition: zusätzliche Information, die keine Anweisung, Grenze oder Sicherheitsmaßnahme enthält
  review_status: provisional_v0.2
  gender: masc
  plural: Hinweise
- entry_id: DE-ADJ-hoch
  lemma: hoch
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.high
    definition: hat im definierten Bezugssystem eine große räumliche Position oder einen als hoch bezeichneten Zustand
  review_status: provisional_v0.2
  restrictions:
  - Für numerische Werte bevorzugt konkreten Wert oder mehr als verwenden.
- entry_id: DE-VER-hochladen
  lemma: hochladen
  part_of_speech: verb
  status: approved
  meanings:
  - id: upload
    definition: Daten vom lokalen System an ein entferntes System übertragen
  review_status: provisional_v0.2
  separable: true
  prefix: hoch
- entry_id: DE-ADV-h-chstens
  lemma: höchstens
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.maximum
    definition: kennzeichnet einen eingeschlossenen oberen Grenzwert
  review_status: provisional_v0.2
- entry_id: DE-NOU-h-he
  lemma: Höhe
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.height
    definition: lineare Abmessung oder Position in vertikaler Richtung
  review_status: provisional_v0.2
  gender: fem
  plural: Höhen
- entry_id: DE-DET-Ihr
  lemma: Ihr
  part_of_speech: determiner
  status: restricted
  meanings:
  - id: determiner.de_det_ihr
    definition: bezeichnet den Besitz oder Bezug zur formal angesprochenen lesenden Person
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - Ihr
  - Ihre
  - Ihren
  - Ihrem
  - Ihrer
  - Ihres
  case_sensitive: true
  restrictions:
  - Bezugsobjekt nach dem Determinierer nennen.
- entry_id: DE-ADV-immer
  lemma: immer
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.always
    definition: kennzeichnet, dass eine Aussage ohne Ausnahme in allen Fällen des definierten Geltungsbereichs gilt
  review_status: provisional_v0.2
  restrictions:
  - Nur verwenden, wenn tatsächlich keine Ausnahme existiert.
- entry_id: DE-PRE-in
  lemma: in
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.in_into
    definition: kennzeichnet eine Position innerhalb eines Bereichs oder eine Bewegung in einen Bereich
  review_status: provisional_v0.2
- entry_id: DE-PHR-in-betrieb-sein
  lemma: in Betrieb sein
  part_of_speech: phrase
  status: restricted
  meanings:
  - id: state.in_operation
    definition: kennzeichnet, dass ein System in seinem vorgesehenen Betriebszustand ist
  review_status: provisional_v0.2
- entry_id: DE-NOU-information
  lemma: Information
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.information
    definition: technischer Inhalt, der einen Sachverhalt, Zustand, Wert oder Zusammenhang beschreibt
  review_status: provisional_v0.2
  gender: fem
  plural: Informationen
- entry_id: DE-NOU-inhalt
  lemma: Inhalt
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.content
    definition: Information oder Material innerhalb eines ausdrücklich genannten Behälters, Dokuments oder Datenobjekts
  review_status: provisional_v0.2
  gender: masc
  plural: Inhalte
- entry_id: DE-ADV-innen
  lemma: innen
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.inside
    definition: kennzeichnet die Innenseite oder den Innenraum eines definierten Objekts
  review_status: provisional_v0.2
- entry_id: DE-PRE-innerhalb
  lemma: innerhalb
  part_of_speech: preposition
  status: approved
  meanings:
  - id: within.bound
    definition: kennzeichnet eine ausdrücklich genannte räumliche, zeitliche oder numerische Grenze
  review_status: corpus_candidate_v0.3
- entry_id: DE-NOU-installation
  lemma: Installation
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.installation
    definition: Vorgang oder Ergebnis des Einbauens, Anschließens oder Einrichtens eines technischen Systems
  review_status: multi_industry_candidate_v0.4
  plural: Installationen
  restrictions:
  - In Verfahren bevorzugt installieren, einbauen, anschließen oder einrichten entsprechend der konkreten Handlung
    verwenden.
- entry_id: DE-VER-installieren
  lemma: installieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: install.software
    definition: Software oder ein digitales Paket in einem System einrichten
  - id: install.system
    definition: ein System nach offizieller Terminologie in Betrieb setzen
  review_status: provisional_v0.2
  restrictions:
  - Für mechanische Bauteile bevorzugt einbauen verwenden.
  surface_forms:
  - installiert
- entry_id: DE-ADJ-intern
  lemma: intern
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.internal
    definition: innerhalb des ausdrücklich genannten Systems, Geräts oder organisatorischen Bereichs
  review_status: provisional_v0.2
- entry_id: DE-VER-isolieren
  lemma: isolieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: isolate
    definition: ein Objekt elektrisch, thermisch, stofflich oder logisch von seiner Umgebung trennen
  review_status: provisional_v0.2
  restrictions:
  - Art der Isolation nennen, wenn nicht eindeutig.
- entry_id: DE-QUA-je
  lemma: je
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: per.each
    definition: kennzeichnet eine Menge oder einen Wert pro ausdrücklich genannter Einheit
  review_status: corpus_candidate_v0.3
  approved_examples:
  - Der maximale Strom beträgt 500 mA je Kanal.
- entry_id: DE-DET-jeder
  lemma: jeder
  part_of_speech: determiner
  status: approved
  meanings:
  - id: determiner.each
    definition: bezeichnet jedes einzelne Element einer klar bestimmten Menge
  review_status: provisional_v0.2
  surface_forms:
  - jeder
  - jede
  - jedes
  - jeden
  - jedem
  approved_examples:
  - Prüfen Sie jede Verbindung.
- entry_id: DE-VER-kalibrieren
  lemma: kalibrieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: calibrate
    definition: ein Messsystem mit einer festgelegten Referenz vergleichen und nach dem freigegebenen Verfahren
      justieren
  review_status: provisional_v0.2
  restrictions:
  - Nur verwenden, wenn ein formales Kalibrierverfahren gemeint ist.
- entry_id: DE-DET-kein
  lemma: kein
  part_of_speech: determiner
  status: approved
  meanings:
  - id: determiner.none
    definition: verneint das Vorhandensein oder die Zugehörigkeit eines Substantivs
  review_status: provisional_v0.2
  surface_forms:
  - kein
  - keine
  - keinen
  - keinem
  - keiner
  - keines
  approved_examples:
  - Stellen Sie sicher, dass keine Leckage vorhanden ist.
- entry_id: DE-NOU-kenntnis
  lemma: Kenntnis
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.kenntnis
    definition: fachliches Wissen, das für eine ausdrücklich genannte Tätigkeit vorausgesetzt wird
  review_status: multi_industry_candidate_v0.4
  plural: Kenntnisse
  restrictions:
  - Bei sicherheitsrelevanten Voraussetzungen erforderliche Qualifikation konkret nennen.
- entry_id: DE-VER-kennzeichnen
  lemma: kennzeichnen
  part_of_speech: verb
  status: approved
  meanings:
  - id: label.mark
    definition: ein Objekt, einen Zustand oder einen Bereich mit einer eindeutigen Kennzeichnung versehen
  review_status: provisional_v0.2
- entry_id: DE-NOU-kennzeichnung
  lemma: Kennzeichnung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.kennzeichnung
    definition: sichtbare oder maschinenlesbare Markierung zur Identifikation oder Klassifikation
  review_status: multi_industry_candidate_v0.4
  plural: Kennzeichnungen
- entry_id: DE-ADJ-klein
  lemma: klein
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.small
    definition: hat eine kleinere physische Abmessung als die ausdrücklich genannte Referenz
  review_status: provisional_v0.2
  restrictions:
  - Wenn möglich konkrete Abmessung nennen.
- entry_id: DE-VER-klicken
  lemma: klicken
  part_of_speech: verb
  status: restricted
  meanings:
  - id: click
    definition: eine Zeigeraktion mit einer Maustaste ausführen
  review_status: provisional_v0.2
  restrictions:
  - Nur für Benutzeroberflächen verwenden, bei denen ein Klick tatsächlich die Bedienhandlung ist.
- entry_id: DE-VER-komprimieren
  lemma: komprimieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: compress
    definition: Volumen oder digitale Daten nach einem definierten Verfahren verkleinern
  review_status: provisional_v0.2
  restrictions:
  - Physische und digitale Bedeutung müssen aus dem Objekt eindeutig sein.
- entry_id: DE-VER-konfigurieren
  lemma: konfigurieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: configure
    definition: freigegebene Parameter eines Systems auf eine definierte Konfiguration einstellen
  review_status: provisional_v0.2
  restrictions:
  - Konfiguration oder Referenz nennen, wenn sie nicht eindeutig vorgegeben ist.
- entry_id: DE-VER-kopieren
  lemma: kopieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: copy
    definition: eine identische digitale oder dokumentarische Kopie erstellen
  review_status: provisional_v0.2
- entry_id: DE-ADJ-korrekt
  lemma: korrekt
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.correct
    definition: entspricht der ausdrücklich geltenden Anforderung, Referenz oder Sollvorgabe
  review_status: provisional_v0.2
  restrictions:
  - Referenz muss aus Kontext oder Dokument eindeutig sein.
- entry_id: DE-VER-korrigieren
  lemma: korrigieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: correct
    definition: einen nachweislich falschen Wert, Text oder Zustand in den festgelegten korrekten Zustand bringen
  review_status: provisional_v0.2
- entry_id: DE-ADJ-kurz
  lemma: kurz
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.short
    definition: hat eine geringe Ausdehnung in Längsrichtung oder Dauer relativ zur ausdrücklich genannten Referenz
  review_status: provisional_v0.2
  restrictions:
  - Wenn möglich konkreten Wert nennen.
- entry_id: DE-VER-k-nnen
  lemma: können
  part_of_speech: verb
  status: restricted
  meanings:
  - id: can.capability
    definition: technische oder physische Fähigkeit ausdrücken
  - id: can.possibility
    definition: faktische Möglichkeit ausdrücken
  review_status: provisional_v0.2
  restrictions:
  - Nicht als Ersatz für Erlaubnis verwenden; dafür dürfen verwenden.
  surface_forms:
  - kann
  - kannst
  - können
  - könnt
  - konnte
  - konnten
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-ADJ-lang
  lemma: lang
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.long
    definition: hat eine große Ausdehnung in Längsrichtung oder Dauer relativ zur ausdrücklich genannten Referenz
  review_status: provisional_v0.2
  restrictions:
  - Wenn möglich konkreten Wert nennen.
- entry_id: DE-ADV-langsam
  lemma: langsam
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.slowly
    definition: kennzeichnet eine geringe Geschwindigkeit
  review_status: provisional_v0.2
  restrictions:
  - Wenn die Geschwindigkeit sicherheits- oder qualitätskritisch ist, einen messbaren Grenzwert angeben.
- entry_id: DE-VER-lassen
  lemma: lassen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: allow.process
    definition: einen ausdrücklich genannten physikalischen Prozess ohne weitere aktive Handlung fortlaufen lassen
  review_status: corpus_candidate_v0.3
  surface_forms:
  - lasse
  - lässt
  - lassen
  - ließ
  - ließen
  - gelassen
  restrictions:
  - Nur verwenden, wenn der Leser einen natürlichen oder automatischen Prozess abwartet, zum Beispiel Abkühlen.
    Nicht verwenden, um den verantwortlichen Akteur zu verschleiern.
- entry_id: DE-ADJ-leer
  lemma: leer
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.empty
    definition: enthält keine relevante Menge des ausdrücklich genannten Inhalts
  review_status: provisional_v0.2
- entry_id: DE-ADJ-lesbar
  lemma: lesbar
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.readable
    definition: mit dem vorgesehenen Medium ohne zusätzliche Rekonstruktion erkennbar und interpretierbar
  review_status: provisional_v0.2
- entry_id: DE-VER-lesen
  lemma: lesen
  part_of_speech: verb
  status: approved
  meanings:
  - id: verb.lesen
    definition: geschriebenen oder angezeigten Text aufnehmen und inhaltlich erfassen
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - lese
  - liest
  - lesen
  - las
  - lasen
  - gelesen
  approved_examples:
  - Lesen Sie die Betriebsanleitung.
- entry_id: DE-NOU-leser
  lemma: Leser
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.reader
    definition: Person, für die der technische Text bestimmt ist
  review_status: provisional_v0.2
  gender: masc
  plural: Leser
  restrictions:
  - In inklusiven Unternehmensrichtlinien kann eine andere neutrale Rollenbezeichnung vorgeschrieben sein.
- entry_id: DE-VER-liegen
  lemma: liegen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: lie.position
    definition: sich an einer ausdrücklich bestimmten räumlichen Position befinden
  - id: value.in_range
    definition: einen Messwert oder Parameter innerhalb eines ausdrücklich genannten Bereichs haben
  review_status: corpus_candidate_v0.3
  surface_forms:
  - liege
  - liegst
  - liegt
  - liegen
  - lag
  - lagen
  - gelegen
  restrictions:
  - Nicht in abstrakten Wendungen wie „die Ursache liegt in“ verwenden; Ursache direkt nennen.
- entry_id: DE-ADV-links
  lemma: links
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.left
    definition: kennzeichnet die linke Seite relativ zum festgelegten Bezugssystem
  review_status: provisional_v0.2
- entry_id: DE-ADJ-lokal
  lemma: lokal
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.local
    definition: am ausdrücklich genannten Gerät, Ort oder System selbst statt über eine entfernte Verbindung
  review_status: provisional_v0.2
- entry_id: DE-ADJ-lose
  lemma: lose
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.loose
    definition: nicht ausreichend befestigt oder nicht in der vorgesehenen festen Verbindung
  review_status: provisional_v0.2
- entry_id: DE-VER-loslassen
  lemma: loslassen
  part_of_speech: verb
  status: approved
  meanings:
  - id: release.hand
    definition: ein zuvor gehaltenes Objekt freigeben
  review_status: provisional_v0.2
  separable: true
  prefix: los
- entry_id: DE-NOU-l-nge
  lemma: Länge
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.length
    definition: lineare Abmessung in der festgelegten Längsrichtung
  review_status: provisional_v0.2
  gender: fem
  plural: Längen
- entry_id: DE-VER-l-schen
  lemma: löschen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: delete.data
    definition: Daten oder einen digitalen Eintrag entfernen
  review_status: provisional_v0.2
  restrictions:
  - Für Feuer löschen nur verwenden, wenn der Kontext eindeutig Brandbekämpfung ist; sonst Feuer löschen als feste
    Wortgruppe verwenden.
- entry_id: DE-VER-l-sen
  lemma: lösen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: release.mechanical
    definition: eine mechanische Befestigung, Verriegelung oder Verbindung lockern oder freigeben
  review_status: provisional_v0.2
  restrictions:
  - Nicht für das abstrakte Lösen eines Problems verwenden.
- entry_id: DE-VER-markieren
  lemma: markieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: mark.select
    definition: ein Element sichtbar oder logisch als ausgewählt oder gekennzeichnet festlegen
  review_status: provisional_v0.2
- entry_id: DE-PHR-mehr-als
  lemma: mehr als
  part_of_speech: phrase
  status: approved
  meanings:
  - id: phrase.more_than
    definition: kennzeichnet einen Wert oder eine Menge oberhalb einer nicht eingeschlossenen Grenze
  review_status: provisional_v0.2
- entry_id: DE-QUA-mehrere
  lemma: mehrere
  part_of_speech: quantifier
  status: restricted
  meanings:
  - id: quantifier.several
    definition: bezeichnet mehr als zwei Elemente ohne genaue Anzahl
  review_status: provisional_v0.2
  restrictions:
  - Nicht verwenden, wenn die genaue Anzahl bekannt oder für die Aufgabe relevant ist.
- entry_id: DE-VER-melden
  lemma: melden
  part_of_speech: verb
  status: approved
  meanings:
  - id: report
    definition: einen Zustand, Fehler oder ein Ergebnis an eine vorgesehene Stelle übermitteln
  review_status: provisional_v0.2
- entry_id: DE-NOU-menge
  lemma: Menge
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.quantity
    definition: bestimmte oder messbare Quantität eines Stoffes oder einer nicht diskreten Größe
  review_status: provisional_v0.2
  gender: fem
  plural: Mengen
- entry_id: DE-VER-messen
  lemma: messen
  part_of_speech: verb
  status: approved
  meanings:
  - id: measure
    definition: den quantitativen Wert einer physikalischen oder technischen Größe bestimmen
  review_status: provisional_v0.2
  surface_forms:
  - gemessen
- entry_id: DE-NOU-methode
  lemma: Methode
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.method
    definition: festgelegte Art, eine Aufgabe oder Analyse auszuführen
  review_status: provisional_v0.2
  gender: fem
  plural: Methoden
- entry_id: DE-ADV-mindestens
  lemma: mindestens
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.minimum
    definition: kennzeichnet einen eingeschlossenen unteren Grenzwert
  review_status: provisional_v0.2
- entry_id: DE-VER-mischen
  lemma: mischen
  part_of_speech: verb
  status: approved
  meanings:
  - id: mix
    definition: zwei oder mehr Stoffe zu einer Mischung zusammenbringen
  review_status: provisional_v0.2
- entry_id: DE-PRE-mit
  lemma: mit
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.with
    definition: kennzeichnet ein Werkzeug, Mittel, Material oder eine eindeutige gemeinsame Beteiligung
  review_status: provisional_v0.2
  restrictions:
  - Satz neu formulieren, wenn mit mehr als eine plausible Beziehung ausdrücken kann.
- entry_id: DE-NOU-mitte
  lemma: Mitte
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.middle
    definition: geometrischer oder funktionaler Zentralbereich zwischen festgelegten Grenzen
  review_status: provisional_v0.2
  gender: fem
  plural: Mitten
- entry_id: DE-VER-multiplizieren
  lemma: multiplizieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: multiply.math
    definition: numerische Werte mathematisch miteinander multiplizieren
  review_status: provisional_v0.2
- entry_id: DE-ADJ-m-glich
  lemma: möglich
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.possible
    definition: unter den genannten technischen Bedingungen realisierbar oder eintretbar
  review_status: provisional_v0.2
  restrictions:
  - Wenn die Wahrscheinlichkeit oder Bedingung relevant ist, diese explizit nennen.
- entry_id: DE-VER-m-ssen
  lemma: müssen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: must.requirement
    definition: eine verbindliche Anforderung oder zwingende Bedingung ausdrücken
  review_status: provisional_v0.2
  restrictions:
  - In direkten Arbeitsanweisungen nach Möglichkeit Imperativ verwenden.
  surface_forms:
  - muss
  - musst
  - müssen
  - müsst
  - musste
  - mussten
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-PRE-nach
  lemma: nach
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.after_toward
    definition: kennzeichnet eine zeitlich spätere Position oder eine eindeutig bezeichnete Richtung
  review_status: provisional_v0.2
  restrictions:
  - Zeit- und Richtungsbedeutung dürfen im selben Satz nicht konkurrieren.
- entry_id: DE-CON-nachdem
  lemma: nachdem
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.after
    definition: ordnet eine Handlung oder einen Zustand zeitlich nach einer abgeschlossenen Handlung an
  review_status: provisional_v0.2
- entry_id: DE-ADV-nacheinander
  lemma: nacheinander
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.sequentially
    definition: kennzeichnet Handlungen oder Elemente in einer ausdrücklich geordneten Folge
  review_status: provisional_v0.2
- entry_id: DE-ADJ-nah
  lemma: nah
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.near
    definition: hat einen kleinen Abstand zur ausdrücklich genannten Referenz
  review_status: provisional_v0.2
  restrictions:
  - Wenn der Abstand sicherheits- oder funktionsrelevant ist, Grenzwert nennen.
- entry_id: DE-NOU-name
  lemma: Name
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.name
    definition: offizielle oder eindeutig festgelegte sprachliche Identifikation eines Objekts, Dokuments oder Elements
  review_status: provisional_v0.2
  gender: masc
  plural: Namen
- entry_id: DE-ADJ-nass
  lemma: nass
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.wet
    definition: weist sichtbare oder relevante Flüssigkeit auf
  review_status: provisional_v0.2
- entry_id: DE-PRE-neben
  lemma: neben
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.next_to
    definition: kennzeichnet eine Position unmittelbar seitlich eines Referenzobjekts
  review_status: provisional_v0.2
- entry_id: DE-ADJ-neu
  lemma: neu
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.new
    definition: noch nicht verwendet oder ausdrücklich als neues Ersatzteil vorgesehen
  review_status: provisional_v0.2
  restrictions:
  - Nicht als Synonym für neueste Version verwenden.
- entry_id: DE-QUA-neun
  lemma: neun
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.nine
    definition: bezeichnet die Zahl 9 in ausgeschriebener Form
  review_status: corpus_candidate_v0.3
- entry_id: DE-ADV-nicht
  lemma: nicht
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.not
    definition: verneint genau das unmittelbar zugeordnete Prädikat, Merkmal oder Element
  review_status: provisional_v0.2
  restrictions:
  - Negationsbereich muss eindeutig sein.
- entry_id: DE-ADV-nie
  lemma: nie
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.never
    definition: kennzeichnet, dass eine Handlung oder ein Zustand im definierten Geltungsbereich in keinem Fall
      zulässig oder möglich ist
  review_status: provisional_v0.2
  restrictions:
  - Für direkte Verbote in Verfahren bevorzugt nicht + Imperativ verwenden.
- entry_id: DE-ADJ-niedrig
  lemma: niedrig
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.low
    definition: hat im definierten Bezugssystem eine geringe räumliche Position oder einen als niedrig bezeichneten
      Zustand
  review_status: provisional_v0.2
  restrictions:
  - Für numerische Werte bevorzugt konkreten Wert oder weniger als verwenden.
- entry_id: DE-QUA-null
  lemma: 'null'
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.zero
    definition: bezeichnet die Zahl 0 in ausgeschriebener Form
  review_status: corpus_candidate_v0.3
- entry_id: DE-NOU-nummer
  lemma: Nummer
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.number
    definition: numerische oder alphanumerische Identifikation
  review_status: provisional_v0.2
  gender: fem
  plural: Nummern
- entry_id: DE-ADV-nur
  lemma: nur
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.only
    definition: beschränkt eine Aussage auf das ausdrücklich genannte Element oder die ausdrücklich genannte Bedingung
  review_status: provisional_v0.2
- entry_id: DE-CON-ob
  lemma: ob
  part_of_speech: conjunction
  status: restricted
  meanings:
  - id: whether.check
    definition: leitet eine Ja/Nein-Bedingung ein, deren Ergebnis ausdrücklich geprüft oder bestimmt wird
  review_status: corpus_candidate_v0.3
  restrictions:
  - Nur verwenden, wenn genau zwei klar unterscheidbare Zustände oder ein klares Ja/Nein-Kriterium vorliegen.
- entry_id: DE-ADV-oben
  lemma: oben
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.up
    definition: kennzeichnet eine höhere Position im festgelegten Bezugssystem
  review_status: provisional_v0.2
- entry_id: DE-NOU-oberfl-che
  lemma: Oberfläche
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.surface
    definition: äußere oder definierte Grenzfläche eines Materials oder Objekts
  review_status: provisional_v0.2
  gender: fem
  plural: Oberflächen
- entry_id: DE-CON-oder
  lemma: oder
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.or
    definition: verbindet echte Alternativen
  review_status: provisional_v0.2
  restrictions:
  - Nicht verwenden, wenn inklusive und exklusive Alternative unterschieden werden muss; dann die Auswahl explizit
    beschreiben.
- entry_id: DE-ADJ-offen
  lemma: offen
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.open
    definition: in einem definierten geöffneten Zustand
  review_status: provisional_v0.2
- entry_id: DE-PRE-ohne
  lemma: ohne
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.without
    definition: kennzeichnet das Fehlen eines ausdrücklich genannten Elements oder Zustands
  review_status: provisional_v0.2
- entry_id: DE-NOU-option
  lemma: Option
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.option
    definition: ausdrücklich angebotene auswählbare Alternative
  review_status: provisional_v0.2
  gender: fem
  plural: Optionen
  restrictions:
  - Alternativen vollständig nennen, wenn sie für die Entscheidung relevant sind.
- entry_id: DE-NOU-person
  lemma: Person
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.person
    definition: ein einzelner Mensch ohne geschlechtsspezifische Benennung
  review_status: provisional_v0.2
  gender: fem
  plural: Personen
- entry_id: DE-NOU-position
  lemma: Position
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.position
    definition: definierte räumliche Lage oder definierter Zustand eines Bedienelements
  review_status: provisional_v0.2
  gender: fem
  plural: Positionen
  restrictions:
  - Räumliche und Schalterzustandsbedeutung müssen aus Kontext eindeutig sein.
- entry_id: DE-VER-positionieren
  lemma: positionieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: position
    definition: ein Objekt in eine ausdrücklich definierte Position bringen
  review_status: provisional_v0.2
- entry_id: DE-ADJ-prim-r
  lemma: primär
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.primary
    definition: als erste, wichtigste oder vorgesehene Hauptfunktion in der anwendbaren Terminologie definiert
  review_status: provisional_v0.2
  restrictions:
  - Nicht als bloßes Synonym für wichtig verwenden.
- entry_id: DE-NOU-problem
  lemma: Problem
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.problem
    definition: Zustand, der die vorgesehene Funktion oder Ausführung einer Aufgabe verhindert oder beeinträchtigt
  review_status: provisional_v0.2
  gender: neut
  plural: Probleme
  restrictions:
  - Wenn möglich konkreten Fehler oder Zustand nennen.
- entry_id: DE-NOU-produkt
  lemma: Produkt
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.produkt
    definition: technische Einheit oder Ware, auf die sich die Dokumentation bezieht
  review_status: multi_industry_candidate_v0.4
  plural: Produkte
  restrictions:
  - Offizielle Produkt- oder Komponentenbezeichnung hat Vorrang.
- entry_id: DE-NOU-prozess
  lemma: Prozess
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.process
    definition: geordnete Folge von Zuständen oder Vorgängen mit definiertem Zweck
  review_status: provisional_v0.2
  gender: masc
  plural: Prozesse
- entry_id: DE-VER-pr-fen
  lemma: prüfen
  part_of_speech: verb
  status: approved
  meanings:
  - id: check
    definition: feststellen, ob ein definierter Zustand, ein Merkmal oder eine Anforderung erfüllt ist
  review_status: provisional_v0.2
  approved_examples:
  - Prüfen Sie den Druck.
  prohibited_synonyms:
  - überprüfen
  - kontrollieren
  - checken
  surface_forms:
  - geprüft
- entry_id: DE-NOU-pr-fung
  lemma: Prüfung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.check
    definition: festgelegte Handlung zur Feststellung, ob ein Zustand oder Kriterium erfüllt ist
  review_status: provisional_v0.2
  gender: fem
  plural: Prüfungen
- entry_id: DE-ADV-rechts
  lemma: rechts
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.right
    definition: kennzeichnet die rechte Seite relativ zum festgelegten Bezugssystem
  review_status: provisional_v0.2
- entry_id: DE-VER-reduzieren
  lemma: reduzieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: reduce
    definition: einen Umfang, eine Menge oder eine Größe kleiner machen
  review_status: provisional_v0.2
  restrictions:
  - Für reine numerische Werte bevorzugt verringern verwenden.
- entry_id: DE-VER-referenzieren
  lemma: referenzieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: reference
    definition: eine eindeutig bezeichnete Quelle oder ein Objekt als Referenz angeben
  review_status: provisional_v0.2
  restrictions:
  - In Lesertexten bevorzugt auf ... verweisen.
- entry_id: DE-VER-regeln
  lemma: regeln
  part_of_speech: verb
  status: restricted
  meanings:
  - id: regulate
    definition: eine Größe automatisch oder manuell auf einen Sollwert oder innerhalb eines Bereichs halten
  review_status: provisional_v0.2
  restrictions:
  - Nur im technischen Regelungs-Sinn verwenden.
- entry_id: DE-VER-reinigen
  lemma: reinigen
  part_of_speech: verb
  status: approved
  meanings:
  - id: clean
    definition: unerwünschtes Material von einem Objekt oder einer Oberfläche entfernen
  review_status: provisional_v0.2
- entry_id: DE-VER-reparieren
  lemma: reparieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: repair
    definition: einen beschädigten oder fehlerhaften Gegenstand nach einem freigegebenen Verfahren wieder in den
      zulässigen Zustand bringen
  review_status: provisional_v0.2
- entry_id: DE-NOU-richtung
  lemma: Richtung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.direction
    definition: orientierte räumliche oder logische Bewegungsrichtung
  review_status: provisional_v0.2
  gender: fem
  plural: Richtungen
- entry_id: DE-NOU-risiko
  lemma: Risiko
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.risk
    definition: Kombination aus Möglichkeit eines schädlichen Ereignisses und dessen Auswirkung nach anwendbarem
      Sicherheitsmodell
  review_status: provisional_v0.2
  gender: neut
  plural: Risiken
- entry_id: DE-ADJ-sauber
  lemma: sauber
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.clean
    definition: frei von dem im Verfahren nicht zulässigen Schmutz oder Fremdmaterial
  review_status: provisional_v0.2
  restrictions:
  - Bei kritischer Sauberkeit messbares oder referenziertes Kriterium verwenden.
- entry_id: DE-NOU-schaden
  lemma: Schaden
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.damage
    definition: physische, funktionale oder materielle Beeinträchtigung eines Objekts oder einer Person
  review_status: provisional_v0.2
  gender: masc
  plural: Schäden
- entry_id: DE-VER-schieben
  lemma: schieben
  part_of_speech: verb
  status: approved
  meanings:
  - id: push.slide
    definition: ein Objekt durch eine geradlinige Druckbewegung zu einer ausdrücklich genannten Position bewegen
  review_status: corpus_candidate_v0.3
  surface_forms:
  - schiebe
  - schiebst
  - schiebt
  - schieben
  - schob
  - schoben
  - geschoben
- entry_id: DE-VER-schlie-en
  lemma: schließen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: close
    definition: ein Teil, eine Öffnung, Datei oder Funktion aus dem offenen Zustand in den geschlossenen Zustand
      bringen
  review_status: provisional_v0.2
  restrictions:
  - Bei Software und Mechanik muss der Kontext eindeutig sein.
  surface_forms:
  - geschlossen
- entry_id: DE-VER-schmieren
  lemma: schmieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: lubricate
    definition: ein freigegebenes Schmiermittel auf eine Reib- oder Kontaktstelle aufbringen
  review_status: provisional_v0.2
  restrictions:
  - Schmiermittel nennen oder auf freigegebene Spezifikation verweisen.
- entry_id: DE-VER-schneiden
  lemma: schneiden
  part_of_speech: verb
  status: approved
  meanings:
  - id: cut.material
    definition: Material mit einem dafür vorgesehenen Schneidwerkzeug trennen
  review_status: provisional_v0.2
- entry_id: DE-ADV-schnell
  lemma: schnell
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.quickly
    definition: kennzeichnet eine hohe Geschwindigkeit
  review_status: provisional_v0.2
  restrictions:
  - Wenn die Geschwindigkeit sicherheits- oder qualitätskritisch ist, einen messbaren Grenzwert angeben.
- entry_id: DE-NOU-schritt
  lemma: Schritt
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.step
    definition: einzelne abgegrenzte Handlung oder Anweisung innerhalb eines Verfahrens
  review_status: provisional_v0.2
  gender: masc
  plural: Schritte
- entry_id: DE-VER-sch-tzen
  lemma: schützen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: protect
    definition: ein Objekt oder eine Person durch eine ausdrücklich genannte Maßnahme vor einer definierten Gefahr
      oder Einwirkung bewahren
  review_status: provisional_v0.2
  restrictions:
  - Gefahr oder Einwirkung nennen, wenn sie nicht eindeutig ist.
- entry_id: DE-VER-scrollen
  lemma: scrollen
  part_of_speech: verb
  status: approved
  meanings:
  - id: scroll.ui
    definition: den sichtbaren Ausschnitt einer digitalen Ansicht verschieben
  review_status: provisional_v0.2
- entry_id: DE-QUA-sechs
  lemma: sechs
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.six
    definition: bezeichnet die Zahl 6 in ausgeschriebener Form
  review_status: corpus_candidate_v0.3
- entry_id: DE-VER-sein
  lemma: sein
  part_of_speech: verb
  status: approved
  meanings:
  - id: be.state
    definition: einen Zustand, eine Eigenschaft, Identität oder Existenz ausdrücken
  review_status: provisional_v0.2
  restrictions:
  - Nicht als Hilfsverb für eine unnötige Passivkonstruktion verwenden.
  surface_forms:
  - bin
  - bist
  - ist
  - sind
  - seid
  - war
  - waren
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-PRE-seit
  lemma: seit
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.since
    definition: kennzeichnet den Beginn eines Zeitraums, der bis zum Bezugszeitpunkt andauert
  review_status: provisional_v0.2
- entry_id: DE-NOU-seite
  lemma: Seite
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.side_page
    definition: räumliche Seite eines Objekts oder Seite eines Dokuments
  review_status: provisional_v0.2
  gender: fem
  plural: Seiten
  restrictions:
  - Räumliche und dokumentarische Bedeutung müssen aus Kontext eindeutig sein.
- entry_id: DE-ADJ-sekund-r
  lemma: sekundär
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.secondary
    definition: als zweite oder unterstützende Funktion in der anwendbaren Terminologie definiert
  review_status: provisional_v0.2
- entry_id: DE-VER-senden
  lemma: senden
  part_of_speech: verb
  status: approved
  meanings:
  - id: send
    definition: Daten, ein Signal oder eine Nachricht zu einem Empfänger übertragen
  review_status: provisional_v0.2
- entry_id: DE-VER-senken
  lemma: senken
  part_of_speech: verb
  status: approved
  meanings:
  - id: lower.position
    definition: ein Objekt in eine tiefere Position bewegen
  review_status: provisional_v0.2
- entry_id: DE-PRO-sich
  lemma: sich
  part_of_speech: pronoun
  status: restricted
  meanings:
  - id: pron.reflexive
    definition: reflexives Pronomen, das eindeutig auf das grammatische Subjekt derselben Klausel verweist
  review_status: corpus_candidate_v0.3
  restrictions:
  - Nur bei eindeutigem reflexivem Bezug verwenden. Bei möglichem Bezug auf mehrere Objekte den technischen Begriff
    wiederholen.
- entry_id: DE-ADJ-sicher
  lemma: sicher
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.sicher
    definition: ohne eine nach dem anwendbaren Risikokriterium unzulässige Gefahr
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - sichere
  - sicheren
  - sicherer
  - sicheres
  - sicherem
  restrictions:
  - Nicht als unquantifizierte Qualitätsbehauptung verwenden.
- entry_id: DE-VER-sicherstellen
  lemma: sicherstellen
  part_of_speech: verb
  status: approved
  meanings:
  - id: ensure
    definition: durch eine Prüfung oder eindeutige Feststellung bestätigen, dass eine genannte Bedingung erfüllt
      ist
  review_status: provisional_v0.2
  separable: true
  prefix: sicher
  approved_examples:
  - Stellen Sie sicher, dass das Ventil geschlossen ist.
  forms:
    imperative_formal: Stellen Sie sicher, dass ...
- entry_id: DE-ADJ-sichtbar
  lemma: sichtbar
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.visible
    definition: mit dem vorgesehenen visuellen Verfahren erkennbar
  review_status: provisional_v0.2
  restrictions:
  - Für Prüfhandlungen bevorzugt Stellen Sie sicher, dass Sie ... sehen können, wenn Beobachterbezug relevant ist.
- entry_id: DE-PRO-SIE-READER
  lemma: Sie
  part_of_speech: pronoun
  status: approved
  meanings:
  - id: pronoun.reader_formal
    definition: bezeichnet die lesende oder handelnde Person in formalen Anweisungen
  review_status: provisional_v0.2
  surface_forms:
  - Sie
  - Ihnen
  approved_examples:
  - Entfernen Sie die Abdeckung.
  case_sensitive: true
- entry_id: DE-PRO-sie
  lemma: sie
  part_of_speech: pronoun
  status: restricted
  meanings:
  - id: pronoun.she_they
    definition: ersetzt ein eindeutig identifiziertes feminines Singular- oder Pluralreferenzobjekt
  review_status: provisional_v0.2
  surface_forms:
  - sie
  - ihnen
  restrictions:
  - Nicht verwenden, wenn Numerus oder Bezug mehrdeutig ist.
  case_sensitive: true
- entry_id: DE-QUA-sieben
  lemma: sieben
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.seven
    definition: bezeichnet die Zahl 7 in ausgeschriebener Form
  review_status: corpus_candidate_v0.3
- entry_id: DE-NOU-signal
  lemma: Signal
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.signal
    definition: physikalische oder digitale Größe, die Information überträgt
  review_status: provisional_v0.2
  gender: neut
  plural: Signale
- entry_id: DE-VER-sinken
  lemma: sinken
  part_of_speech: verb
  status: approved
  meanings:
  - id: decrease.intransitive
    definition: von selbst oder durch einen Prozess einen niedrigeren numerischen Wert annehmen
  review_status: provisional_v0.2
- entry_id: DE-PHR-so-viel-wie
  lemma: so viel wie
  part_of_speech: phrase
  status: restricted
  meanings:
  - id: phrase.equal_amount
    definition: kennzeichnet Gleichheit einer Menge oder eines Werts
  review_status: provisional_v0.2
- entry_id: DE-CON-sobald
  lemma: sobald
  part_of_speech: conjunction
  status: restricted
  meanings:
  - id: conj.as_soon_as
    definition: kennzeichnet den ersten Zeitpunkt, an dem eine eindeutig definierte Bedingung erfüllt ist
  review_status: provisional_v0.2
  restrictions:
  - Nur verwenden, wenn die Reaktion tatsächlich unmittelbar beim Eintritt der Bedingung erfolgen soll.
- entry_id: DE-ADV-sofort
  lemma: sofort
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.immediately
    definition: kennzeichnet, dass keine absichtliche Verzögerung zulässig ist
  review_status: provisional_v0.2
- entry_id: DE-CON-sondern
  lemma: sondern
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.but_rather
    definition: ersetzt nach einer Verneinung ein ausgeschlossenes Element durch das korrekte Element
  review_status: provisional_v0.2
- entry_id: DE-VER-sortieren
  lemma: sortieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: sort
    definition: Elemente nach einem ausdrücklich genannten Kriterium in eine Reihenfolge bringen
  review_status: provisional_v0.2
- entry_id: DE-VER-speichern
  lemma: speichern
  part_of_speech: verb
  status: approved
  meanings:
  - id: save.data
    definition: Daten dauerhaft oder für spätere Verwendung ablegen
  review_status: provisional_v0.2
- entry_id: DE-VER-sp-len
  lemma: spülen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: flush
    definition: ein System oder eine Oberfläche mit einem Flüssigkeits- oder Gasstrom reinigen oder auswaschen
  review_status: provisional_v0.2
  restrictions:
  - Spülmedium und Ziel nennen, wenn nicht durch Verfahren festgelegt.
- entry_id: DE-ADJ-stabil
  lemma: stabil
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.stable
    definition: ändert den relevanten Zustand oder Wert innerhalb des definierten Beobachtungszeitraums nicht außerhalb
      der zulässigen Grenze
  review_status: provisional_v0.2
  restrictions:
  - Kriterium oder Zeitraum nennen, wenn für Entscheidung relevant.
- entry_id: DE-VER-starten
  lemma: starten
  part_of_speech: verb
  status: approved
  meanings:
  - id: start
    definition: einen Prozess, Test, Motor oder Ablauf beginnen lassen
  review_status: provisional_v0.2
  prohibited_synonyms:
  - beginnen
  - anfangen
  surface_forms:
  - gestartet
- entry_id: DE-VER-steigen
  lemma: steigen
  part_of_speech: verb
  status: approved
  meanings:
  - id: increase.intransitive
    definition: von selbst oder durch einen Prozess einen höheren numerischen Wert annehmen
  review_status: provisional_v0.2
- entry_id: DE-NOU-stelle
  lemma: Stelle
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.location
    definition: genau bezeichneter räumlicher Punkt, Dokumentort oder organisatorischer Empfänger
  review_status: provisional_v0.2
  gender: fem
  plural: Stellen
  restrictions:
  - Art der Stelle nennen, wenn nicht eindeutig.
- entry_id: DE-VER-steuern
  lemma: steuern
  part_of_speech: verb
  status: approved
  meanings:
  - id: control
    definition: den Zustand oder Ablauf eines Systems durch Signale oder Befehle beeinflussen
  review_status: provisional_v0.2
- entry_id: DE-VER-stoppen
  lemma: stoppen
  part_of_speech: verb
  status: approved
  meanings:
  - id: stop
    definition: einen laufenden Prozess oder eine Bewegung gezielt anhalten
  review_status: provisional_v0.2
- entry_id: DE-VER-subtrahieren
  lemma: subtrahieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: subtract.math
    definition: einen numerischen Wert mathematisch von einem anderen abziehen
  review_status: provisional_v0.2
- entry_id: DE-NOU-symbol
  lemma: Symbol
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.symbol
    definition: grafisches Zeichen mit festgelegter technischer oder sicherheitsbezogener Bedeutung
  review_status: multi_industry_candidate_v0.4
  plural: Symbole
- entry_id: DE-NOU-system
  lemma: System
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.system
    definition: funktional zusammengehörige Menge von Elementen mit einer definierten Aufgabe
  review_status: provisional_v0.2
  gender: neut
  plural: Systeme
- entry_id: DE-NOU-tabelle
  lemma: Tabelle
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.table
    definition: strukturierte Darstellung von Daten in Zeilen und Spalten
  review_status: provisional_v0.2
  gender: fem
  plural: Tabellen
- entry_id: DE-ADJ-technisch
  lemma: technisch
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.technisch
    definition: auf Technik, ein technisches Produkt oder einen technischen Prozess bezogen
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - technische
  - technischen
  - technischer
  - technisches
  - technischem
  restrictions:
  - Nur verwenden, wenn die Bezugsart für den Leser relevant ist.
- entry_id: DE-NOU-teil
  lemma: Teil
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.part
    definition: abgegrenztes Element eines größeren Ganzen
  review_status: provisional_v0.2
  gender: neut
  plural: Teile
  restrictions:
  - Offizielle technische Benennung bevorzugen.
- entry_id: DE-ADV-teilweise
  lemma: teilweise
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.partly
    definition: kennzeichnet, dass nur ein ausdrücklich bestimmter Teil betroffen ist
  review_status: provisional_v0.2
  restrictions:
  - Den betroffenen Teil nennen, wenn er für die Aufgabe relevant ist.
- entry_id: DE-VER-testen
  lemma: testen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: test
    definition: mit einem definierten Test feststellen, ob eine Funktion oder ein System festgelegte Kriterien erfüllt
  review_status: provisional_v0.2
  restrictions:
  - Nur verwenden, wenn ein definierter Test gemeint ist; sonst prüfen verwenden.
- entry_id: DE-NOU-text
  lemma: Text
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.text
    definition: geschriebene sprachliche Information
  review_status: provisional_v0.2
  gender: masc
  plural: Texte
- entry_id: DE-VER-tippen
  lemma: tippen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: tap.ui
    definition: eine Touch-Oberfläche kurz berühren, um eine Bedienhandlung auszuführen
  review_status: provisional_v0.2
  restrictions:
  - Nicht im Sinn von Text mit Tastatur eingeben verwenden.
- entry_id: DE-VER-trennen
  lemma: trennen
  part_of_speech: verb
  status: approved
  meanings:
  - id: disconnect
    definition: eine bestehende mechanische, elektrische oder logische Verbindung aufheben
  review_status: provisional_v0.2
- entry_id: DE-ADJ-trocken
  lemma: trocken
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.dry
    definition: weist keine für die Aufgabe relevante freie Feuchtigkeit oder Flüssigkeit auf
  review_status: provisional_v0.2
- entry_id: DE-VER-trocknen
  lemma: trocknen
  part_of_speech: verb
  status: approved
  meanings:
  - id: dry
    definition: Feuchtigkeit oder Flüssigkeit von einem Objekt oder aus einem Bereich entfernen
  review_status: provisional_v0.2
- entry_id: DE-NOU-typ
  lemma: Typ
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.type_class
    definition: definierte technische oder dokumentarische Klasse
  review_status: provisional_v0.2
  gender: masc
  plural: Typen
- entry_id: DE-NOU-taetigkeit
  lemma: Tätigkeit
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.taetigkeit
    definition: abgegrenzte menschliche technische Handlung oder Arbeitsaufgabe
  review_status: multi_industry_candidate_v0.4
  plural: Tätigkeiten
  restrictions:
  - In Verfahren die konkrete Handlung mit einem direkten Verb formulieren.
- entry_id: DE-PRE-um
  lemma: um
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.around
    definition: kennzeichnet eine Bewegung oder Position um eine ausdrücklich genannte Achse oder ein Objekt
  - id: prep.delta
    definition: kennzeichnet eine ausdrücklich genannte Änderung um einen numerischen Betrag
  - id: prep.time
    definition: kennzeichnet einen ausdrücklich genannten Zeitpunkt
  review_status: corpus_candidate_v0.3
  restrictions:
  - Die Konstruktion „um ... zu“ ist nicht durch diesen Eintrag freigegeben; Zweck besser als eigener Satz oder
    mit einer eindeutigen Zweckangabe ausdrücken.
- entry_id: DE-CON-und
  lemma: und
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.and
    definition: verbindet gleichrangige Elemente, Aussagen oder gleichzeitig geltende Bedingungen
  review_status: provisional_v0.2
- entry_id: DE-ADV-ungef-hr
  lemma: ungefähr
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.approximately
    definition: kennzeichnet einen Näherungswert, für den keine exakte Grenze gemeint ist
  review_status: provisional_v0.2
  restrictions:
  - Nicht für Akzeptanzgrenzen, Toleranzen oder sicherheitskritische Werte verwenden.
- entry_id: DE-ADJ-unm-glich
  lemma: unmöglich
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.impossible
    definition: unter den genannten technischen Bedingungen nicht realisierbar oder nicht eintretbar
  review_status: provisional_v0.2
- entry_id: DE-ADV-unten
  lemma: unten
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.down
    definition: kennzeichnet eine tiefere Position im festgelegten Bezugssystem
  review_status: provisional_v0.2
- entry_id: DE-PRE-unter
  lemma: unter
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.below_under
    definition: kennzeichnet eine räumlich tiefere Position oder eine Lage unter einem Objekt
  review_status: provisional_v0.2
  restrictions:
  - Nicht für numerische Grenzwerte verwenden; dafür weniger als verwenden.
- entry_id: DE-ADJ-unterschiedlich
  lemma: unterschiedlich
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.different
    definition: hat im ausdrücklich verglichenen Merkmal nicht denselben Wert oder Zustand
  review_status: provisional_v0.2
- entry_id: DE-VER-untersuchen
  lemma: untersuchen
  part_of_speech: verb
  status: approved
  meanings:
  - id: examine
    definition: ein Objekt oder einen Bereich systematisch auf Schäden, Fehler oder andere festgelegte Merkmale
      ansehen oder prüfen
  review_status: provisional_v0.2
- entry_id: DE-ADJ-unvollst-ndig
  lemma: unvollständig
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.incomplete
    definition: enthält nicht alle für den definierten Umfang erforderlichen Teile oder Daten
  review_status: provisional_v0.2
- entry_id: DE-ADJ-unzul-ssig
  lemma: unzulässig
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.not_permitted
    definition: durch eine ausdrücklich geltende Anforderung, Grenze oder Freigabe nicht erlaubt
  review_status: provisional_v0.2
- entry_id: DE-NOU-ursache
  lemma: Ursache
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.cause
    definition: Ereignis oder Zustand, der eine ausdrücklich genannte Wirkung hervorruft
  review_status: provisional_v0.2
  gender: fem
  plural: Ursachen
- entry_id: DE-VER-verbinden
  lemma: verbinden
  part_of_speech: verb
  status: approved
  meanings:
  - id: connect
    definition: zwei oder mehr Teile, Leitungen, Systeme oder Datenpfade funktional miteinander koppeln
  review_status: provisional_v0.2
  surface_forms:
  - verbunden
- entry_id: DE-NOU-verbindung
  lemma: Verbindung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.connection
    definition: mechanische, elektrische, stoffliche oder logische Kopplung zwischen ausdrücklich genannten Elementen
  review_status: provisional_v0.2
  gender: fem
  plural: Verbindungen
- entry_id: DE-ADJ-verboten
  lemma: verboten
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.forbidden
    definition: durch eine Regel oder Sicherheitsanforderung ausdrücklich nicht erlaubt
  review_status: provisional_v0.2
- entry_id: DE-ADJ-verbunden
  lemma: verbunden
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.connected
    definition: mit dem ausdrücklich genannten Objekt mechanisch, elektrisch oder logisch gekoppelt
  review_status: provisional_v0.2
  restrictions:
  - Art der Verbindung muss aus dem Kontext eindeutig sein.
- entry_id: DE-NOU-verfahren
  lemma: Verfahren
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.procedure
    definition: festgelegte Folge von Handlungen zur Erreichung eines technischen Ziels
  review_status: provisional_v0.2
  gender: neut
  plural: Verfahren
- entry_id: DE-ADJ-verf-gbar
  lemma: verfügbar
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.available
    definition: für die vorgesehene Verwendung oder Auswahl vorhanden und zugänglich
  review_status: provisional_v0.2
  restrictions:
  - Zeit- oder Systembezug nennen, wenn veränderlich.
- entry_id: DE-NOU-verfuegbarkeit
  lemma: Verfügbarkeit
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.verfuegbarkeit
    definition: Zustand, in dem eine ausdrücklich genannte Funktion, Ressource oder Komponente zur vorgesehenen
      Nutzung bereitsteht
  review_status: multi_industry_candidate_v0.4
  restrictions:
  - Nicht als unquantifizierte Zuverlässigkeitskennzahl verwenden.
- entry_id: DE-VER-vergleichen
  lemma: vergleichen
  part_of_speech: verb
  status: approved
  meanings:
  - id: compare
    definition: zwei oder mehr Werte, Zustände oder Merkmale gegenüberstellen
  review_status: provisional_v0.2
- entry_id: DE-VER-verhindern
  lemma: verhindern
  part_of_speech: verb
  status: approved
  meanings:
  - id: prevent
    definition: eine ausdrücklich genannte unerwünschte Wirkung oder Handlung unmöglich machen
  review_status: provisional_v0.2
- entry_id: DE-NOU-verletzung
  lemma: Verletzung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.verletzung
    definition: körperliche Schädigung einer Person
  review_status: multi_industry_candidate_v0.4
  plural: Verletzungen
- entry_id: DE-VER-verriegeln
  lemma: verriegeln
  part_of_speech: verb
  status: approved
  meanings:
  - id: lock
    definition: eine mechanische oder logische Verriegelung in den gesicherten Zustand bringen
  review_status: provisional_v0.2
- entry_id: DE-ADJ-verriegelt
  lemma: verriegelt
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.locked
    definition: in einem definierten Verriegelungszustand
  review_status: provisional_v0.2
- entry_id: DE-VER-verringern
  lemma: verringern
  part_of_speech: verb
  status: approved
  meanings:
  - id: decrease.transitive
    definition: einen numerischen Wert kleiner machen
  review_status: provisional_v0.2
- entry_id: DE-VER-verschieben
  lemma: verschieben
  part_of_speech: verb
  status: approved
  meanings:
  - id: move.relocate
    definition: ein Objekt oder Datenelement von einer Position an eine andere Position bewegen
  review_status: provisional_v0.2
- entry_id: DE-VER-verschliessen
  lemma: verschließen
  part_of_speech: verb
  status: approved
  meanings:
  - id: close.seal_opening
    definition: eine Öffnung mit dem vorgesehenen Verschlusselement schließen
  review_status: corpus_candidate_v0.3
  surface_forms:
  - verschließe
  - verschließt
  - verschließen
  - verschloss
  - verschlossen
  restrictions:
  - Nicht mit verriegeln verwechseln.
- entry_id: DE-NOU-version
  lemma: Version
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.version
    definition: eindeutig identifizierter Entwicklungs- oder Ausgabestand eines Produkts, Dokuments oder Softwareelements
  review_status: multi_industry_candidate_v0.4
  plural: Versionen
- entry_id: DE-VER-verursachen
  lemma: verursachen
  part_of_speech: verb
  status: approved
  meanings:
  - id: cause
    definition: eine ausdrücklich genannte Wirkung als Ursache hervorrufen
  review_status: provisional_v0.2
- entry_id: DE-VER-verweisen
  lemma: verweisen
  part_of_speech: verb
  status: approved
  meanings:
  - id: refer
    definition: den Leser auf eine eindeutig bezeichnete Stelle, Quelle oder Referenz lenken
  review_status: provisional_v0.2
- entry_id: DE-VER-verwenden
  lemma: verwenden
  part_of_speech: verb
  status: approved
  meanings:
  - id: use
    definition: ein Werkzeug, Material, Bauteil oder Hilfsmittel für einen ausdrücklich genannten Zweck einsetzen
  review_status: provisional_v0.2
  prohibited_synonyms:
  - benutzen
  - nutzen
  - gebrauchen
  surface_forms:
  - verwendet
- entry_id: DE-NOU-verwendung
  lemma: Verwendung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.verwendung
    definition: Einsatz eines Produkts, Werkzeugs, Stoffes oder Verfahrens für einen ausdrücklich genannten Zweck
  review_status: multi_industry_candidate_v0.4
  plural: Verwendungen
  restrictions:
  - In Anweisungen bevorzugt das direkte Verb verwenden.
- entry_id: DE-QUA-vier
  lemma: vier
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.four
    definition: bezeichnet die Zahl 4 in ausgeschriebener Form
  review_status: corpus_candidate_v0.3
- entry_id: DE-ADJ-voll
  lemma: voll
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.full
    definition: enthält die definierte maximale oder vorgesehene Füllmenge
  review_status: provisional_v0.2
  restrictions:
  - Bei Messbehältern nach Möglichkeit Füllgrenze nennen.
- entry_id: DE-ADJ-vollst-ndig
  lemma: vollständig
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.complete
    definition: enthält alle für den definierten Umfang erforderlichen Teile oder Daten
  review_status: provisional_v0.2
- entry_id: DE-ADV-vollst-ndig
  lemma: vollständig
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.completely
    definition: kennzeichnet, dass kein Teil oder Rest der beschriebenen Menge oder Handlung fehlt
  review_status: provisional_v0.2
- entry_id: DE-PRE-von
  lemma: von
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.from_of
    definition: kennzeichnet Ausgangspunkt, Urheber oder eindeutige Zuordnung
  review_status: provisional_v0.2
- entry_id: DE-PRE-vor
  lemma: vor
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.before_in_front
    definition: kennzeichnet eine räumlich vordere Position oder einen früheren Zeitpunkt
  review_status: provisional_v0.2
  restrictions:
  - Bei komplexen Zeitbedingungen einen bevor-Satz verwenden.
- entry_id: DE-ADJ-vorhanden
  lemma: vorhanden
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.present
    definition: an der ausdrücklich genannten Stelle oder im System existent
  review_status: provisional_v0.2
- entry_id: DE-NOU-vorschrift
  lemma: Vorschrift
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.vorschrift
    definition: verbindliche dokumentierte Regel oder Anforderung aus einer ausdrücklich identifizierten Quelle
  review_status: multi_industry_candidate_v0.4
  plural: Vorschriften
  restrictions:
  - Quelle oder Dokument nennen, wenn sie für die Handlung oder Konformität erforderlich ist.
- entry_id: DE-NOU-warnung
  lemma: Warnung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.warnung
    definition: Sicherheitsinformation, die auf eine Gefahr für Personen hinweist
  review_status: multi_industry_candidate_v0.4
  plural: Warnungen
  restrictions:
  - Risikokategorie muss mit dem anwendbaren Sicherheitsstandard übereinstimmen.
- entry_id: DE-VER-warten
  lemma: warten
  part_of_speech: verb
  status: restricted
  meanings:
  - id: wait
    definition: eine Handlung bis zum Eintritt eines ausdrücklich genannten Zeitpunkts oder Zustands nicht fortsetzen
  review_status: provisional_v0.2
  restrictions:
  - Nicht im Sinn von Instandhaltung verwenden. Für Instandhaltung Projektterminologie verwenden.
- entry_id: DE-PRE-wegen
  lemma: wegen
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.because_of
    definition: kennzeichnet eine ausdrücklich benannte Ursache
  review_status: provisional_v0.2
  restrictions:
  - Bei komplexer Ursache einen weil-Satz verwenden.
- entry_id: DE-CON-weil
  lemma: weil
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.because
    definition: leitet eine ausdrücklich genannte Ursache oder Begründung ein
  review_status: provisional_v0.2
- entry_id: DE-PHR-weniger-als
  lemma: weniger als
  part_of_speech: phrase
  status: approved
  meanings:
  - id: phrase.less_than
    definition: kennzeichnet einen Wert oder eine Menge unterhalb einer nicht eingeschlossenen Grenze
  review_status: provisional_v0.2
- entry_id: DE-CON-wenn
  lemma: wenn
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.if
    definition: leitet eine ausdrücklich genannte Bedingung ein
  review_status: provisional_v0.2
  approved_examples:
  - Wenn die Anzeige rot ist, stoppen Sie den Test.
- entry_id: DE-VER-werden
  lemma: werden
  part_of_speech: verb
  status: restricted
  meanings:
  - id: become.future
    definition: den Übergang in einen neuen Zustand oder eine ausdrücklich notwendige Zukunft ausdrücken
  review_status: provisional_v0.2
  restrictions:
  - Nicht für vermeidbares Vorgangspassiv verwenden. Zukunft nach Möglichkeit mit Präsens und Zeitangabe ausdrücken.
  surface_forms:
  - werde
  - wirst
  - wird
  - werden
  - werdet
  - wurde
  - wurden
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-NOU-wert
  lemma: Wert
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.value
    definition: quantitative oder eindeutig codierte Ausprägung einer Größe oder eines Parameters
  review_status: provisional_v0.2
  gender: masc
  plural: Werte
- entry_id: DE-ADJ-wichtig
  lemma: wichtig
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.wichtig
    definition: für Sicherheit, korrekte Funktion oder das Ergebnis wesentlich
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - wichtige
  - wichtigen
  - wichtiger
  - wichtiges
  - wichtigem
  restrictions:
  - Wenn möglich den konkreten Grund oder die Folge nennen.
- entry_id: DE-CON-wie
  lemma: wie
  part_of_speech: conjunction
  status: restricted
  meanings:
  - id: comparison.like
    definition: kennzeichnet einen ausdrücklich benannten Vergleich oder eine ausdrücklich benannte Referenz
  review_status: corpus_candidate_v0.3
  restrictions:
  - Vergleich oder Referenz muss eindeutig sein. Nicht als vage Art-und-Weise-Angabe verwenden.
- entry_id: DE-VER-wiederholen
  lemma: wiederholen
  part_of_speech: verb
  status: approved
  meanings:
  - id: repeat
    definition: dieselbe ausdrücklich bestimmte Handlung oder Prüfung erneut ausführen
  review_status: provisional_v0.2
- entry_id: DE-PRO-wir
  lemma: wir
  part_of_speech: pronoun
  status: restricted
  meanings:
  - id: pronoun.organization
    definition: bezeichnet die herausgebende Organisation oder den Hersteller
  review_status: provisional_v0.2
  surface_forms:
  - wir
  - uns
  restrictions:
  - Nur verwenden, wenn der Autor eindeutig für die herausgebende Organisation spricht.
- entry_id: DE-VER-waehlen
  lemma: wählen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: verb.waehlen
    definition: eine Option aus einer ausdrücklich vorhandenen Menge auswählen
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - wähle
  - wählst
  - wählt
  - wählen
  - wählte
  - wählten
  - gewählt
  restrictions:
  - Auswahlmenge oder Benutzeroberflächenoption muss eindeutig sein.
  approved_examples:
  - Wählen Sie die Funktion aus.
- entry_id: DE-CON-w-hrend
  lemma: während
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.while
    definition: kennzeichnet zwei Zustände oder Handlungen, die im selben Zeitraum gelten
  review_status: provisional_v0.2
- entry_id: DE-PRE-w-hrend
  lemma: während
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.during
    definition: kennzeichnet einen Zeitraum, in dem ein Zustand oder eine Handlung gilt
  review_status: provisional_v0.2
- entry_id: DE-QUA-zehn
  lemma: zehn
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.ten
    definition: bezeichnet die Zahl 10 in ausgeschriebener Form
  review_status: corpus_candidate_v0.3
- entry_id: DE-VER-zeigen
  lemma: zeigen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: show
    definition: Information oder einen sichtbaren Zustand für den Leser erkennbar machen
  review_status: provisional_v0.2
  restrictions:
  - Nicht im Sinn von beweisen oder hinweisen verwenden.
  surface_forms:
  - zeige
  - zeigst
  - zeigt
  - zeigen
  - zeigte
  - zeigten
  - gezeigt
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-NOU-zeit
  lemma: Zeit
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.time
    definition: Zeitpunkt oder Zeitgröße im ausdrücklich genannten Kontext
  review_status: provisional_v0.2
  gender: fem
  plural: Zeiten
- entry_id: DE-VER-zerlegen
  lemma: zerlegen
  part_of_speech: verb
  status: approved
  meanings:
  - id: disassemble
    definition: eine Baugruppe nach einem vorgesehenen Verfahren in ihre Teile trennen
  review_status: provisional_v0.2
- entry_id: DE-VER-ziehen
  lemma: ziehen
  part_of_speech: verb
  status: approved
  meanings:
  - id: pull
    definition: eine Kraft in Richtung zum Kraftausübenden oder entlang einer definierten Richtung ausüben
  review_status: provisional_v0.2
- entry_id: DE-NOU-ziel
  lemma: Ziel
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.target
    definition: ausdrücklich festgelegter gewünschter Endzustand oder Zweck
  review_status: provisional_v0.2
  gender: neut
  plural: Ziele
- entry_id: DE-PRE-zu
  lemma: zu
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.to
    definition: kennzeichnet eine Richtung zu einem Ziel oder eine feste Beziehung in einer freigegebenen Wortgruppe
  review_status: provisional_v0.2
- entry_id: DE-ADV-zuerst
  lemma: zuerst
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.first
    definition: kennzeichnet den ersten Schritt einer ausdrücklich geordneten Folge
  review_status: provisional_v0.2
- entry_id: DE-NOU-zugriff
  lemma: Zugriff
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.access
    definition: technische Möglichkeit, auf ein Objekt, einen Bereich oder Daten zuzugreifen
  review_status: provisional_v0.2
  gender: masc
  plural: Zugriffe
- entry_id: DE-ADJ-zul-ssig
  lemma: zulässig
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.permitted
    definition: durch eine ausdrücklich geltende Anforderung, Grenze oder Freigabe erlaubt
  review_status: provisional_v0.2
  restrictions:
  - Geltende Anforderung oder Grenzwert muss bestimmbar sein.
- entry_id: DE-PHR-zum-beispiel
  lemma: zum Beispiel
  part_of_speech: phrase
  status: restricted
  meanings:
  - id: example.nonexhaustive
    definition: leitet ausdrücklich eine nicht vollständige Menge von Beispielen ein
  review_status: corpus_candidate_v0.3
  surface_forms:
  - zum Beispiel
  restrictions:
  - Nicht verwenden, wenn die Liste vollständig sein muss.
- entry_id: DE-VER-zusammenbauen
  lemma: zusammenbauen
  part_of_speech: verb
  status: approved
  meanings:
  - id: assemble
    definition: mehrere Teile nach einer festgelegten Struktur zu einer Baugruppe verbinden
  review_status: provisional_v0.2
  separable: true
  prefix: zusammen
- entry_id: DE-NOU-zustand
  lemma: Zustand
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.state
    definition: feststellbare Ausprägung eines Systems, Objekts oder Parameters zu einem Zeitpunkt
  review_status: provisional_v0.2
  gender: masc
  plural: Zustände
- entry_id: DE-ADV-zusaetzlich
  lemma: zusätzlich
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: addition.additional
    definition: kennzeichnet ein weiteres, ausdrücklich identifiziertes Element neben bereits genannten Elementen
  review_status: corpus_candidate_v0.3
  restrictions:
  - Das zusätzliche Element muss konkret genannt sein.
- entry_id: DE-QUA-zwei
  lemma: zwei
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.two
    definition: bezeichnet die Zahl 2 in ausgeschriebener Form
  review_status: provisional_v0.2
- entry_id: DE-PRE-zwischen
  lemma: zwischen
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.between
    definition: kennzeichnet eine Position oder Beziehung zwischen zwei klar identifizierten Grenzen oder Objekten
  review_status: provisional_v0.2
- entry_id: DE-VER-z-hlen
  lemma: zählen
  part_of_speech: verb
  status: approved
  meanings:
  - id: count
    definition: die Anzahl diskreter Elemente bestimmen
  review_status: provisional_v0.2
- entry_id: DE-VER-ndern
  lemma: ändern
  part_of_speech: verb
  status: restricted
  meanings:
  - id: change
    definition: einen ausdrücklich bezeichneten Wert, Zustand oder Inhalt in einen anderen Wert, Zustand oder Inhalt
      überführen
  review_status: provisional_v0.2
  restrictions:
  - Zielzustand oder geänderten Parameter nennen.
- entry_id: DE-NOU-aenderung
  lemma: Änderung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.aenderung
    definition: feststellbare Abweichung eines Zustands, Werts, Produkts oder Dokuments gegenüber einem vorherigen
      Stand
  review_status: multi_industry_candidate_v0.4
  plural: Änderungen
  restrictions:
  - Geändertes Objekt oder Merkmal nennen.
- entry_id: DE-VER-ffnen
  lemma: öffnen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: open
    definition: ein Teil, eine Öffnung, Datei oder Funktion aus dem geschlossenen Zustand zugänglich machen
  review_status: provisional_v0.2
  restrictions:
  - Bei Software und Mechanik muss der Kontext eindeutig sein.
  surface_forms:
  - geöffnet
- entry_id: DE-PRE-ber
  lemma: über
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.above_over
    definition: kennzeichnet eine räumlich höhere Position oder eine Bewegung über ein Objekt
  review_status: provisional_v0.2
  restrictions:
  - Nicht für numerische Grenzwerte verwenden; dafür mehr als verwenden.
- entry_id: DE-VER-bertragen
  lemma: übertragen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: transmit
    definition: Daten, Energie, Kraft oder ein Signal von einer Quelle zu einem Ziel weitergeben
  review_status: provisional_v0.2
  restrictions:
  - Die Art der übertragenen Größe muss aus dem Satz eindeutig sein.
- entry_id: DE-VER-berwachen
  lemma: überwachen
  part_of_speech: verb
  status: approved
  meanings:
  - id: monitor
    definition: einen Zustand oder Wert fortlaufend beobachten oder erfassen
  review_status: provisional_v0.2

```

---

## Structured appendix: `dictionary/prohibited-words.yaml`

```yaml
schema_version: '0.4'
release: 0.4.0
status: corpus_validated_authoring_core
entries:
- term: abklemmen
  status: prohibited
  reason: fach-/umgangssprachlich für unterschiedliche Trennvorgänge
  rewrite: trennen und Objekt/Verbindung nennen oder als technischen Term freigeben.
  approved_alternatives:
  - trennen
- term: aktuell
  status: prohibited
  reason: mehrdeutig zwischen derzeit gültig und neueste Version
  rewrite: derzeit, gültig oder konkrete Version/Datum nennen.
  approved_alternatives:
  - derzeit
- term: anfangen
  status: prohibited
  reason: Synonymvariation zu starten
  rewrite: starten verwenden.
  approved_alternatives:
  - starten
- term: angemessen
  status: prohibited
  reason: Bewertungskriterium bleibt ungenannt
  rewrite: Messbares oder referenziertes Kriterium nennen.
- term: anhand
  status: review_required
  reason: die Datenbasis oder das Mittel kann implizit bleiben
  rewrite: Datenbasis ausdrücklich nennen; wenn möglich mit oder aus verwenden.
- term: anmachen
  status: prohibited
  reason: umgangssprachlich und mehrdeutig
  rewrite: einschalten verwenden.
  approved_alternatives:
  - einschalten
- term: anschließend
  status: prohibited
  reason: stilistische Sequenzvariante zu danach
  rewrite: danach verwenden.
  approved_alternatives:
  - danach
- term: arbeiten
  status: review_required
  reason: kann menschliche Tätigkeit oder Maschinenfunktion bedeuten
  rewrite: Konkrete Tätigkeit oder funktionieren/betreiben verwenden.
- term: aufspüren
  status: prohibited
  reason: stilistische oder bildhafte Variante für finden/prüfen
  rewrite: finden oder prüfen entsprechend der beabsichtigten Handlung verwenden.
  approved_alternatives:
  - finden
  - prüfen
- term: ausmachen
  status: prohibited
  reason: umgangssprachlich und mehrdeutig
  rewrite: ausschalten verwenden.
  approved_alternatives:
  - ausschalten
- term: ausreichend
  status: review_required
  reason: Kriterium für ausreichend bleibt häufig ungenannt
  rewrite: Grenzwert oder Referenz nennen.
- term: ausschließlich
  status: review_required
  reason: starke Exklusivitätsaussage; der ausgeschlossene Bereich muss klar sein
  rewrite: Nur verwenden, wenn die Exklusivität technisch oder normativ belegt ist; sonst konkrete Einschränkung
    nennen.
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - ausschliesslich
- term: austauschen
  status: prohibited
  reason: kann ersetzen oder gegenseitig vertauschen bedeuten
  rewrite: ersetzen verwenden, wenn ein Ersatzteil eingesetzt wird.
  approved_alternatives:
  - ersetzen
- term: automatisch
  status: review_required
  reason: kann Systemfunktion oder bloße Erwartung bedeuten
  rewrite: Nur als freigegebene technische Funktion verwenden; sonst Akteur/Trigger nennen.
- term: bald
  status: prohibited
  reason: Zeitgrenze ist nicht messbar
  rewrite: Frist oder Zeitpunkt nennen.
- term: baldmöglichst
  status: prohibited
  reason: Zeitgrenze ist nicht messbar
  rewrite: Frist oder Zeitpunkt nennen.
- term: bearbeiten
  status: review_required
  reason: mehrdeutig zwischen mechanisch bearbeiten, Daten bearbeiten und administrativ bearbeiten
  rewrite: Konkrete technische Handlung oder als Domainterm freigeben.
- term: beginnen
  status: prohibited
  reason: Synonymvariation zu starten
  rewrite: starten verwenden.
  approved_alternatives:
  - starten
- term: behandeln
  status: review_required
  reason: mehrdeutig zwischen verarbeiten, medizinisch behandeln, chemisch behandeln und thematisieren
  rewrite: Konkretes technisches Verb verwenden.
- term: behutsam
  status: prohibited
  reason: Handlung oder Grenzwert bleibt unbestimmt
  rewrite: Konkrete Geschwindigkeit, Kraft oder Abstand nennen.
- term: bei Bedarf
  status: prohibited
  reason: Bedingung für den Bedarf ist nicht definiert
  rewrite: Bedingung mit wenn ausdrücklich nennen.
- term: benutzen
  status: prohibited
  reason: Synonymvariation zu verwenden
  rewrite: verwenden verwenden.
  approved_alternatives:
  - verwenden
- term: bereits
  status: review_required
  reason: unspezifischer Zeitbezug; häufig entbehrlich
  rewrite: weglassen oder einen konkreten Zeitpunkt/Zustand nennen.
- term: berücksichtigen
  status: review_required
  reason: kann eine relevante Bedingung nennen, ohne zu sagen, welche konkrete Handlung daraus folgt
  rewrite: Bedingung ausdrücklich formulieren und die daraus erforderliche Handlung nennen.
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - berücksichtigt
  - berücksichtigte
  - berücksichtigten
- term: beseitigen
  status: review_required
  reason: kann physisches Entfernen oder Fehlerbehebung bedeuten
  rewrite: entfernen für Material/Teil oder beheben für einen identifizierten Fehler verwenden.
  approved_alternatives:
  - entfernen
  - beheben
- term: bestmöglich
  status: prohibited
  reason: nennt kein überprüfbares Zielkriterium
  rewrite: Messbares oder referenziertes Kriterium nennen.
- term: beziehungsweise
  status: prohibited
  reason: kann oder, und, genauer gesagt oder eine Zuordnung bedeuten
  rewrite: Exakte Relation mit und, oder oder getrennten Sätzen ausdrücken.
  approved_alternatives:
  - und
  - oder
- term: bieten
  status: review_required
  reason: abstraktes Besitz- oder Leistungsverb; technische Beziehung bleibt häufig unpräzise
  rewrite: Je nach Bedeutung haben, geben, bereitstellen oder enthalten verwenden.
  review_status: multi_industry_candidate_v0.4
  approved_alternatives:
  - haben
  - geben
  - bereitstellen
  - enthalten
  surface_forms:
  - bietet
  - bot
  - boten
  - geboten
- term: bringen
  status: review_required
  reason: kann physische Bewegung oder Zustandsänderung bedeuten
  rewrite: bewegen, positionieren oder Zustandsverb verwenden.
- term: bzw.
  status: prohibited
  reason: mehrdeutige Kurzform von beziehungsweise
  rewrite: Exakte Relation ausschreiben.
  approved_alternatives:
  - und
  - oder
- term: ca.
  status: review_required
  reason: Abkürzung und unklare Genauigkeit
  rewrite: ungefähr nur für echte Näherungswerte verwenden; sonst exakten Wert nennen.
  approved_alternatives:
  - ungefähr
- term: checken
  status: prohibited
  reason: Umgangssprache/Anglizismus für mehrere mögliche Prüfhandlungen
  rewrite: prüfen verwenden.
  approved_alternatives:
  - prüfen
- term: circa
  status: review_required
  reason: Näherungsangabe kann bei Grenzwerten unzulässig sein
  rewrite: ungefähr nur für echte Näherungswerte verwenden; sonst exakten Wert nennen.
  approved_alternatives:
  - ungefähr
- term: da
  status: review_required
  reason: kann Ort, Ursache oder Verweis bedeuten
  rewrite: dort für einen eindeutigen Ort, weil für eine Ursache oder das konkrete Bezugsnomen verwenden.
- term: dabei
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Bezugsnomen, Handlung oder Bedingung wiederholen; siehe STG-DE-4.5.
- term: dafür
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Bezugsnomen, Zweck oder Handlung ausdrücklich nennen; siehe STG-DE-4.5.
- term: daher
  status: prohibited
  reason: stilistische Ergebnisvariante zu deshalb
  rewrite: deshalb verwenden.
  approved_alternatives:
  - deshalb
- term: daraus
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Quelle, Ursache oder Bestandteil ausdrücklich nennen; siehe STG-DE-4.5.
- term: darüber
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Bezugsobjekt oder Thema ausdrücklich nennen; siehe STG-DE-4.5.
- term: davon
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Bezugsobjekt ausdrücklich nennen; siehe STG-DE-4.5.
- term: dazu
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Bezugsobjekt, Zweck oder Handlung ausdrücklich nennen; siehe STG-DE-4.5.
- term: detailliert
  status: review_required
  reason: unspezifische Aussage über Informationsumfang
  rewrite: Konkrete Information geben oder den relevanten Abschnitt nennen.
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - detaillierte
  - detaillierten
  - detaillierter
  - detailliertes
  - detailliertem
- term: doch
  status: prohibited
  reason: Modalpartikel oder unspezifischer Kontrast
  rewrite: aber oder explizite Gegenaussage verwenden.
- term: durchführen
  status: review_required
  reason: Funktionsverb kann eine spezifische Handlung verdecken
  rewrite: Direktes Verb verwenden; nur bei offiziell benanntem Verfahren/Test ohne präziseres Verb zulassen.
- term: eben
  status: prohibited
  reason: Modalpartikel oder mehrdeutige Bedeutung
  rewrite: Entfernen; nur als technischer Begriff für geometrisch eben zulassen, wenn als Terminologie freigegeben.
- term: einfach
  status: review_required
  reason: kann Füllwort oder unprüfbare Bewertung bedeuten
  rewrite: Entfernen oder als definierte Eigenschaft ausdrücklich qualifizieren.
- term: einsetzen
  status: review_required
  reason: mehrdeutig zwischen verwenden, einbauen, einfügen und Personal zuweisen
  rewrite: verwenden, einbauen oder einfügen gemäß der konkreten Handlung verwenden.
  approved_alternatives:
  - verwenden
  - einbauen
  - einfügen
- term: entsprechend
  status: review_required
  reason: Bezug oder Zuordnung kann fehlen
  rewrite: Bezugsobjekt oder Regel ausdrücklich nennen.
- term: entsprechend den Vorschriften
  status: prohibited
  reason: Vorschriften sind nicht identifiziert
  rewrite: Dokument, Abschnitt oder konkrete Anforderung nennen.
- term: erfassen
  status: prohibited
  reason: mehrdeutig zwischen eingeben, messen, erkennen und dokumentieren
  rewrite: eingeben, messen, erkennen oder dokumentieren entsprechend der Bedeutung verwenden.
- term: erfolgen
  status: prohibited
  reason: unpersönliche/passivische Form verschleiert den Akteur
  rewrite: Akteur und direktes Verb nennen.
  surface_forms:
  - erfolgt
  - erfolgte
  - erfolgten
  - erfolgend
- term: ermöglichen
  status: review_required
  reason: abstrakte Fähigkeitskonstruktion kann den eigentlichen Akteur und die Handlung verdecken
  rewrite: Akteur + direktes Verb oder können + direktes Verb verwenden.
- term: erst
  status: prohibited
  reason: mehrdeutig zwischen zuerst, erst ab und nur
  rewrite: zuerst, frühestens oder nur entsprechend der Bedeutung verwenden.
- term: etc.
  status: prohibited
  reason: offene Aufzählung lässt relevante Elemente ungenannt
  rewrite: Vollständige Liste geben oder mit andere + definierter Kategorie abschließen.
- term: etwa
  status: review_required
  reason: mehrdeutig zwischen ungefähr und beispielsweise
  rewrite: ungefähr oder Beispielkonstruktion entsprechend der Bedeutung verwenden.
- term: eventuell
  status: prohibited
  reason: unspezifische Möglichkeit
  rewrite: kann mit klarer Bedingung oder Ursache verwenden.
- term: extrem
  status: review_required
  reason: unspezifische Verstärkung ohne Grenze
  rewrite: Messwert oder definierte Sicherheitskategorie nennen.
- term: fachgerecht
  status: prohibited
  reason: verweist auf ungenannte Fachregeln
  rewrite: Anwendbare Spezifikation oder konkrete Handlung nennen.
- term: fahren
  status: review_required
  reason: kann Fahrzeugbewegung, Maschinenhub oder Softwarezustand bedeuten
  rewrite: Konkrete Bewegungs- oder Systemaktion verwenden.
- term: falls erforderlich
  status: prohibited
  reason: Bedingung für erforderlich ist nicht definiert
  rewrite: Bedingung mit wenn und messbarem Kriterium nennen.
- term: falls möglich
  status: prohibited
  reason: Bedingung für möglich ist nicht definiert
  rewrite: Technische Bedingung ausdrücklich nennen.
- term: falls nötig
  status: prohibited
  reason: Bedingung für nötig ist nicht definiert
  rewrite: Bedingung mit wenn nennen.
- term: festmachen
  status: prohibited
  reason: umgangssprachliche Alternative zu befestigen
  rewrite: befestigen verwenden.
  approved_alternatives:
  - befestigen
- term: fixieren
  status: prohibited
  reason: kann befestigen, chemisch fixieren oder gedanklich festlegen bedeuten
  rewrite: befestigen oder technische Spezialbedeutung als Terminologie freigeben.
  approved_alternatives:
  - befestigen
- term: führen
  status: review_required
  reason: hochgradig mehrdeutig zwischen physischer Bewegung, Leitung, Ergebnisbeziehung und Bedienhandlung
  rewrite: Konkretes Verb oder eine explizite Ursache-Folge-Konstruktion verwenden.
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - führt
  - führte
  - führten
  - geführt
- term: gebrauchen
  status: prohibited
  reason: Synonymvariation zu verwenden und teilweise veraltet
  rewrite: verwenden verwenden.
  approved_alternatives:
  - verwenden
- term: geeignet
  status: review_required
  reason: Eignungskriterium bleibt häufig ungenannt
  rewrite: Eignungskriterium oder freigegebene Spezifikation nennen.
- term: gegebenen Bedingungen
  status: prohibited
  reason: Bedingungen sind nicht identifiziert
  rewrite: Konkrete Bedingungen nennen.
- term: gegebenenfalls
  status: prohibited
  reason: versteckt eine nicht genannte Bedingung
  rewrite: Bedingung mit wenn ausdrücklich nennen.
  approved_alternatives:
  - wenn
- term: genügend
  status: review_required
  reason: Kriterium für genügend bleibt häufig ungenannt
  rewrite: Grenzwert oder Referenz nennen.
- term: gerade
  status: prohibited
  reason: mehrdeutig zwischen aktuell, genau jetzt, geometrisch gerade und Verstärkung
  rewrite: Exakte Bedeutung ausdrücken oder als freigegebenen technischen Term führen.
- term: gewährleisten
  status: review_required
  reason: abstrakte Ergebniszusage ohne sichtbare Prüfhandlung oder messbares Kriterium
  rewrite: Prüfbare Bedingung und konkrete Maßnahme nennen; falls passend sicherstellen mit prüfbarer Bedingung
    verwenden.
  review_status: multi_industry_candidate_v0.4
  approved_alternatives:
  - sicherstellen
  surface_forms:
  - gewährleistet
  - gewährleistete
  - gewährleisteten
- term: ggf.
  status: prohibited
  reason: Abkürzung von gegebenenfalls; die Bedingung bleibt implizit
  rewrite: Bedingung mit wenn ausdrücklich nennen.
  approved_alternatives:
  - wenn
- term: grundsätzlich
  status: prohibited
  reason: Geltungsbereich und Ausnahmen können unklar sein
  rewrite: Geltungsbereich und Ausnahmen ausdrücklich nennen.
- term: halt
  status: prohibited
  reason: Modalpartikel ohne technische Information
  rewrite: Entfernen.
- term: handhaben
  status: review_required
  reason: vage oder jargonartige Sammelbezeichnung
  rewrite: Konkrete Handlungen nennen.
- term: hierfür
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Bezugsobjekt oder Zweck ausdrücklich nennen; siehe STG-DE-4.5.
- term: hochfahren
  status: prohibited
  reason: kann Booten, Starten oder Erhöhen bedeuten
  rewrite: starten oder Wert erhöhen entsprechend der Bedeutung verwenden.
- term: hochgradig
  status: prohibited
  reason: unspezifischer Grad
  rewrite: Messwert oder definierte Kategorie nennen.
- term: im Allgemeinen
  status: prohibited
  reason: Geltungsbereich und Ausnahmen können unklar sein
  rewrite: Konkreten Geltungsbereich nennen.
- term: in Betrieb nehmen
  status: review_required
  reason: kann mehrere technische Einzelschritte zusammenfassen
  rewrite: Konkrete Start-/Aktivierungsanweisung oder freigegebenes Inbetriebnahmeverfahren nennen.
- term: in der Regel
  status: prohibited
  reason: Ausnahmen bleiben ungenannt
  rewrite: Regel und Ausnahmen ausdrücklich nennen.
- term: insbesondere
  status: review_required
  reason: kann einen offenen, nicht vollständigen Umfang erzeugen
  rewrite: vollständige Menge nennen oder ausdrücklich als Beispiel kennzeichnen.
- term: irgendwann
  status: prohibited
  reason: Zeitpunkt ist unbestimmt
  rewrite: Konkreten Zeitpunkt oder Bedingung nennen.
- term: irgendwelche
  status: prohibited
  reason: Menge und Auswahl sind unbestimmt
  rewrite: Konkrete Elemente oder Kategorie nennen.
- term: irgendwie
  status: prohibited
  reason: Methode ist unbestimmt
  rewrite: Konkrete Methode nennen.
- term: irgendwo
  status: prohibited
  reason: Ort ist unbestimmt
  rewrite: Konkreten Ort nennen.
- term: jederzeit
  status: review_required
  reason: unbegrenzte zeitliche Aussage kann technisch oder vertraglich zu stark sein
  rewrite: Gültigen Zeitraum oder Systemzustand nennen, wenn die Verfügbarkeit nicht wirklich uneingeschränkt ist.
  review_status: multi_industry_candidate_v0.4
- term: jedoch
  status: prohibited
  reason: stilistische Kontrastvariante zu aber
  rewrite: aber verwenden.
  approved_alternatives:
  - aber
- term: jeweils
  status: review_required
  reason: Zuordnung kann unklar sein, wenn mehrere Mengen oder Objekte vorkommen
  rewrite: Zuordnung pro Objekt oder Einheit ausdrücklich angeben; je verwenden, wenn eine Rate gemeint ist.
  approved_alternatives:
  - je
- term: kontrollieren
  status: prohibited
  reason: kann prüfen oder steuern bedeuten
  rewrite: prüfen für Inspektion; steuern/regeln für Systemkontrolle verwenden.
  approved_alternatives:
  - prüfen
  - steuern
  - regeln
- term: koppeln
  status: prohibited
  reason: kann mechanische, elektrische oder logische Spezialbedeutung haben
  rewrite: verbinden verwenden oder als technischen Term freigeben.
  approved_alternatives:
  - verbinden
- term: könnte
  status: prohibited
  reason: unspezifische hypothetische Möglichkeit
  rewrite: kann mit klarer Bedingung oder explizite Wahrscheinlichkeit verwenden.
  approved_alternatives:
  - können
- term: könnten
  status: prohibited
  reason: unspezifische hypothetische Möglichkeit
  rewrite: können mit klarer Bedingung verwenden.
  approved_alternatives:
  - können
- term: laufen
  status: prohibited
  reason: kann funktionieren, sich bewegen oder Software ausführen bedeuten
  rewrite: funktionieren, bewegen oder ausführen entsprechend der Bedeutung verwenden.
- term: lediglich
  status: prohibited
  reason: stilistische Variante zu nur
  rewrite: nur verwenden.
  approved_alternatives:
  - nur
- term: leicht
  status: review_required
  reason: mehrdeutig zwischen geringem Gewicht, geringer Kraft und einfach
  rewrite: Messwert oder eindeutiges Adjektiv verwenden.
- term: letzte
  status: review_required
  reason: mehrdeutig zwischen vorherige und endgültige
  rewrite: vorherige oder endgültige entsprechend der Bedeutung verwenden.
- term: machen
  status: prohibited
  reason: zu allgemeines Verb für technische Handlungen
  rewrite: Präzises direktes Verb verwenden.
- term: mal
  status: prohibited
  reason: umgangssprachliche Modalpartikel
  rewrite: Entfernen; mathematische Multiplikation separat als Symbol oder multiplizieren ausdrücken.
- term: man
  status: prohibited
  reason: Akteur bleibt unbestimmt
  rewrite: Formalen Imperativ oder konkreten Akteur verwenden.
- term: meistens
  status: prohibited
  reason: Häufigkeit ist unbestimmt
  rewrite: Häufigkeit quantifizieren oder Bedingungen nennen.
- term: möglicherweise
  status: prohibited
  reason: unspezifische Möglichkeit
  rewrite: kann mit klarer Bedingung oder Ursache verwenden.
- term: möglichst
  status: prohibited
  reason: nennt kein überprüfbares Ziel oder Grenzkriterium
  rewrite: Messbaren Zielwert, Grenzwert oder konkrete Handlung nennen.
- term: müsste
  status: prohibited
  reason: verbindliche Anforderung und Unsicherheit werden vermischt
  rewrite: muss oder klare Möglichkeitsaussage verwenden.
  approved_alternatives:
  - müssen
- term: müssten
  status: prohibited
  reason: verbindliche Anforderung und Unsicherheit werden vermischt
  rewrite: müssen oder klare Möglichkeitsaussage verwenden.
  approved_alternatives:
  - müssen
- term: nach Bedarf
  status: prohibited
  reason: Bedingung für den Bedarf ist nicht definiert
  rewrite: Bedingung und Handlung ausdrücklich nennen.
- term: neueste
  status: review_required
  reason: relative Version ohne Referenzzeitpunkt
  rewrite: Konkrete Version oder Datum nennen.
- term: noch
  status: review_required
  reason: mehrdeutiger Zeit-, Mengen- oder Fortsetzungsbezug
  rewrite: konkreten Zeitpunkt, Restwert oder Zustand nennen.
- term: normalerweise
  status: prohibited
  reason: Ausnahmen bleiben ungenannt
  rewrite: Normalzustand definieren oder konkrete Bedingung nennen.
- term: nutzen
  status: prohibited
  reason: kann verwenden oder einen Vorteil ziehen bedeuten
  rewrite: verwenden für Gebrauch; Vorteil explizit beschreiben.
  approved_alternatives:
  - verwenden
- term: nächste
  status: review_required
  reason: kann räumlich oder zeitlich gemeint sein
  rewrite: Richtung, Schritt oder Zeitpunkt ausdrücklich nennen.
- term: optimal
  status: prohibited
  reason: behauptet ein Optimum ohne definiertes Optimierungskriterium
  rewrite: Konkretes Ziel oder Grenzkriterium nennen.
- term: ordnungsgemäß
  status: prohibited
  reason: verweist auf eine nicht genannte Norm oder korrekte Ausführung
  rewrite: Konkrete Anforderung oder Referenz nennen.
- term: pro
  status: prohibited
  reason: Synonymvariation zu je bei Mengen pro Einheit
  rewrite: je verwenden.
  approved_alternatives:
  - je
- term: problemlos
  status: prohibited
  reason: behauptet das Fehlen von Problemen ohne Kriterium
  rewrite: Konkrete Bedingung oder erwartetes Ergebnis nennen.
- term: realisieren
  status: prohibited
  reason: mehrdeutig zwischen umsetzen und erkennen
  rewrite: konkretes Verb verwenden.
- term: relativ
  status: review_required
  reason: Vergleichsmaßstab fehlt häufig
  rewrite: Vergleichsmaßstab oder Messwert ausdrücklich nennen.
- term: rund
  status: review_required
  reason: kann geometrisch oder ungefähr bedeuten
  rewrite: ungefähr oder konkrete Geometrie ausdrücken.
- term: runterfahren
  status: prohibited
  reason: kann Stoppen, Herunterfahren oder Verringern bedeuten
  rewrite: System stoppen/beenden oder Wert verringern ausdrücklich formulieren.
- term: sachgemäß
  status: prohibited
  reason: verweist auf eine nicht genannte korrekte Methode
  rewrite: Konkrete Handlung oder Referenz nennen.
- term: schon
  status: prohibited
  reason: mehrdeutig zwischen bereits, Betonung und Einschränkung
  rewrite: bereits nur verwenden, wenn der Zeitbezug relevant ist; sonst entfernen.
- term: schwach
  status: review_required
  reason: unspezifischer Grad oder Kraft
  rewrite: Messwert oder definierte Kategorie nennen.
- term: sehr
  status: review_required
  reason: unspezifische Verstärkung
  rewrite: Messwert oder definierte Kategorie nennen.
- term: setzen
  status: review_required
  reason: sehr viele Bedeutungen
  rewrite: einstellen, positionieren, aktivieren oder anderes präzises Verb verwenden.
- term: sichern
  status: prohibited
  reason: mehrdeutig zwischen befestigen, speichern, verriegeln und absichern
  rewrite: befestigen, speichern, verriegeln oder schützen entsprechend der Bedeutung verwenden.
- term: so
  status: review_required
  reason: kann Art und Weise, Grad, Folge oder anaphorischen Verweis ausdrücken
  rewrite: konkrete Art, Wert, Bedingung oder Folge nennen.
- term: so schnell wie möglich
  status: prohibited
  reason: Geschwindigkeit oder Frist ist nicht definiert
  rewrite: Konkrete Frist, Geschwindigkeit oder unverzügliche Handlung mit sofort angeben.
- term: sodass
  status: review_required
  reason: kausale/resultative Nebensatzkette kann Handlung und Folge verdichten
  rewrite: bei komplexen Sätzen Folge als neuen Satz mit deshalb formulieren.
  approved_alternatives:
  - deshalb
- term: sollte
  status: prohibited
  reason: Modalität zwischen Empfehlung und Anforderung ist unklar
  rewrite: Beabsichtigte Modalität als Imperativ, muss, darf, kann oder ausdrücklich als Empfehlung formulieren.
- term: sollten
  status: prohibited
  reason: Modalität zwischen Empfehlung und Anforderung ist unklar
  rewrite: Beabsichtigte Modalität ausdrücklich formulieren.
- term: sowie
  status: prohibited
  reason: stilistische und teilweise mehrdeutige Aufzählungsvariante zu und
  rewrite: und verwenden oder die Aufzählung in getrennte Punkte aufteilen.
  approved_alternatives:
  - und
- term: sowohl ... als auch
  status: prohibited
  reason: unnötig komplexe koordinierende Konstruktion
  rewrite: und verwenden oder zwei parallele Sätze schreiben.
  approved_alternatives:
  - und
- term: stark
  status: review_required
  reason: unspezifischer Grad oder Kraft
  rewrite: Messwert oder definierte Kategorie nennen.
- term: stattfinden
  status: review_required
  reason: nennt nur das Eintreten, nicht die technische Handlung
  rewrite: Konkrete Handlung oder Prozessverb nennen.
- term: stellen
  status: review_required
  reason: sehr viele räumliche und funktionale Bedeutungen
  rewrite: positionieren, einstellen oder präzises Verb verwenden.
- term: tun
  status: prohibited
  reason: zu allgemeines Verb für technische Handlungen
  rewrite: Präzises direktes Verb verwenden.
- term: typischerweise
  status: prohibited
  reason: Kriterium für typisch ist nicht definiert
  rewrite: Konkrete Bedingung, Verteilung oder Häufigkeit nennen.
- term: u. a.
  status: prohibited
  reason: macht unklar, welche weiteren Elemente gelten
  rewrite: Vollständige relevante Elemente nennen.
- term: usw.
  status: prohibited
  reason: offene Aufzählung lässt relevante Elemente ungenannt
  rewrite: Vollständige Liste geben.
- term: vernünftig
  status: prohibited
  reason: subjektive Bewertung
  rewrite: Technisches Kriterium nennen.
- term: verschieden
  status: review_required
  reason: kann Unterschiede behaupten, ohne das unterscheidende Merkmal zu nennen
  rewrite: Unterschied oder konkrete Varianten nennen.
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - verschiedene
  - verschiedenen
  - verschiedener
  - verschiedenes
  - verschiedenem
- term: vgl.
  status: prohibited
  reason: Abkürzung in Fließtext und unklare Handlungsart
  rewrite: einen expliziten Dokumentverweis formulieren oder vergleichen als direktes Verb verwenden.
- term: vornehmen
  status: prohibited
  reason: Funktionsverb ohne konkrete Handlung
  rewrite: Direktes Verb verwenden.
- term: vorsichtig
  status: prohibited
  reason: Handlung oder Grenzwert bleibt unbestimmt
  rewrite: Konkrete Geschwindigkeit, Kraft, Abstand oder verbotene Handlung nennen.
- term: wahrscheinlich
  status: review_required
  reason: Wahrscheinlichkeit ist nicht quantifiziert oder begründet
  rewrite: Wenn relevant, definierte Wahrscheinlichkeit oder beobachtbare Bedingung nennen.
- term: warten (Instandhaltung)
  status: prohibited
  reason: Homonym zu zeitlichem warten und dadurch lexikalisch mehrdeutig
  rewrite: Instand halten oder projektseitige technische Benennung verwenden.
  exceptions_or_contexts:
  - Zeitliches warten ist als eingeschränkter zentraler Eintrag zugelassen.
- term: wechseln
  status: prohibited
  reason: kann ersetzen, ändern oder zwischen Zuständen umschalten bedeuten
  rewrite: ersetzen, ändern oder auswählen entsprechend der Bedeutung verwenden.
- term: weiter
  status: prohibited
  reason: mehrdeutig zwischen räumlich weiter, zusätzlich und fortsetzen
  rewrite: Beabsichtigte Bedeutung explizit formulieren.
- term: wohl
  status: prohibited
  reason: unspezifische Wahrscheinlichkeit
  rewrite: Klare Möglichkeits- oder Wahrscheinlichkeitsaussage verwenden.
- term: würde
  status: prohibited
  reason: Konjunktiv II verschleiert Zeit, Bedingung oder Modalität
  rewrite: Präsens, klare wenn-Bedingung oder ausdrücklich notwendige Zukunft verwenden.
- term: würden
  status: prohibited
  reason: Konjunktiv II verschleiert Zeit, Bedingung oder Modalität
  rewrite: Präsens, klare wenn-Bedingung oder ausdrücklich notwendige Zukunft verwenden.
- term: z. B.
  status: review_required
  reason: Abkürzung und Beispielcharakter können Anforderungen verwischen
  rewrite: In normativen Anweisungen vollständige relevante Liste geben.
- term: zeitnah
  status: prohibited
  reason: Zeitgrenze ist nicht messbar
  rewrite: Frist oder Zeitpunkt nennen.
- term: ziemlich
  status: prohibited
  reason: unspezifischer Grad
  rewrite: Messwert oder definierte qualitative Kategorie nennen.
- term: zugehörig
  status: review_required
  reason: Bezug kann unklar sein, wenn mehrere Systeme oder Dokumentteile möglich sind
  rewrite: Zugehöriges System, Objekt oder Dokument ausdrücklich nennen.
  review_status: multi_industry_candidate_v0.4
  surface_forms:
  - zugehörige
  - zugehörigen
  - zugehöriger
  - zugehöriges
  - zugehörigem
- term: zur Anwendung kommen
  status: prohibited
  reason: Funktionsverbkonstruktion
  rewrite: anwenden oder verwenden verwenden.
  approved_alternatives:
  - anwenden
  - verwenden
- term: zuvor
  status: prohibited
  reason: stilistische Sequenzvariante; Bezugspunkt kann unklar sein
  rewrite: bevor + konkrete Handlung oder davor + eindeutigen Bezug verwenden.
  approved_alternatives:
  - bevor
- term: überprüfen
  status: prohibited
  reason: Synonymvariation zu prüfen ohne zusätzlichen Bedeutungsgewinn
  rewrite: prüfen verwenden.
  approved_alternatives:
  - prüfen
- term: üblicherweise
  status: prohibited
  reason: Ausnahmen bleiben ungenannt
  rewrite: Konkrete Bedingung oder definierte Häufigkeit nennen.

```
