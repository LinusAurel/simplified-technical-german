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
