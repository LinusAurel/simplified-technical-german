# STG-Änderungsvorschlag STG-2026-002: Modalität von Empfehlungen in Regeln

**Vorschlags-ID:** STG-2026-002
**Status:** accepted
**Änderungsklasse:** other normative
**Ziel-Release:** 0.4.0
**Betroffene Regeln:** `STG-4.1`, `STG-DE-4.5`, `STG-GR-5`, Spezifikation Abschnitt 10

## Problem

Einige Sätze haben eine andere Modalität als die Stufe ihrer Regel:

- `STG-GR-5` hat die Stufe `RECOMMENDATION`. Der Text sagt aber „dürfen nicht“.
- In Regeln mit der Stufe `MUST` stehen Sätze mit „Wir empfehlen“. Ein Leser kann nicht erkennen, ob diese Sätze verbindlich sind.
- `STG-DE-4.5` empfiehlt eine Meldung durch den Validator. `validator-contract.md` verlangt dieselbe Meldung als Pflicht.
- Die Spezifikation empfiehlt stabile Regel-IDs „wenn das möglich ist“. `ROADMAP.md` und `VERSIONING.md` behandeln stabile Regel-IDs als Prinzip.
- `dictionary/README.md` nennt eine andere Reihenfolge der Auflösung als `dictionary/MORPHOLOGY.md` und `validator-contract.md`.

## Bisheriges Verhalten

- `STG-GR-5`: „Autoren und Übersetzungssysteme dürfen Bedeutungen nicht aus dem Englischen übertragen …“
- `STG-4.1`: „In beschreibendem Text empfehlen wir ein Hauptthema je Satz.“
- `STG-DE-4.5`: „Wir empfehlen, dass ein Validator ein ungeklärtes Pronominaladverb als `NEEDS_REFERENCE_INPUT` meldet.“
- Spezifikation Abschnitt 10: „Empfehlung: Halten Sie Regel-IDs vor einem stabilen Release 1.0 stabil, wenn das möglich ist.“
- `dictionary/README.md`: Suche in der Sperrliste vor der morphologischen Analyse.

## Neues Verhalten

1. `STG-GR-5` bleibt eine Empfehlung. Der Text verwendet den Imperativ „Prüfen Sie …“ statt „dürfen nicht“.
2. `STG-4.1`: Der Satz zum Hauptthema bleibt eine Empfehlung und beginnt mit „Empfehlung:“.
3. `STG-DE-4.5`: Ein Validator muss ein Pronominaladverb mit ungeklärtem Bezug als Befund zur Prüfung melden.
4. Spezifikation Abschnitt 10: Eine veröffentlichte Regel-ID muss auch vor 1.0 stabil bleiben. Eine Änderung braucht einen angenommenen Änderungsvorschlag.
5. Spezifikation Abschnitt 10 legt fest: Ein Satz mit „Wir empfehlen“ oder „Empfehlung:“ ist auch in einer Regel mit der Stufe `MUST` eine Empfehlung.
6. `dictionary/README.md` folgt `dictionary/MORPHOLOGY.md`: zuerst die morphologische Analyse, danach die Suche in der Sperrliste für das aufgelöste Lemma.
7. `dictionary/GOVERNANCE.md`: Die Belege aus zwei Domänen bleiben eine Empfehlung für Maintainer.

## Beispiele

### Konform

```text
Verbinden Sie den Sensor mit dem Adapter. Beschädigen Sie die Dichtung nicht, wenn Sie den Sensor verbinden.
```

### Nicht konform

```text
Verbinden Sie den Sensor mit dem Adapter. Dabei darf die Dichtung nicht beschädigt werden.
```

Ein Validator meldet `Dabei` zur Prüfung. Der Validator wählt kein Bezugswort aus.

## Auswirkung auf die Kompatibilität

- Kein bisher konformer Text wird nicht konform.
- Keine kontrollierte Bedeutung ändert sich.
- Die Schweregrade im Linter ändern sich nicht. Linter und Analysewerkzeug melden `dabei` und andere Pronominaladverbien bereits zur Prüfung.
- Der Agent Skill ändert keine Umformulierung.

## Belege

- Widerspruch zwischen `rules/rule-index.yaml` (Stufe von `STG-GR-5`) und dem Text der Regel.
- Widerspruch zwischen `rules/04-sentences.md` und `validator-contract.md` Abschnitt 11.
- Widerspruch zwischen `dictionary/README.md` und `dictionary/MORPHOLOGY.md`. Eine Sperrliste vor der Morphologie erkennt gebeugte Formen gesperrter Wörter nicht (Befund aus `corpus/HOLDOUT-PRECISION.md`).

## Geprüfte Alternativen

- `STG-GR-5` als Pflicht: Die Regel schreibt ohne Kontext keinen Ersatz vor. Eine Pflicht wäre nicht prüfbar.
- Ein Hauptthema je Satz als Pflicht in `STG-4.1`: Die primäre Aussage ist bereits Pflicht. Das Hauptthema ist nicht deterministisch prüfbar.
- Belege aus zwei Domänen als Pflicht: `dictionary/GOVERNANCE.md` gibt Maintainern absichtlich Ermessen.

## Auswirkung auf die Implementierung

- Regeln: `rules/04-sentences.md`, `rules/09-writing-practices.md`.
- Spezifikation: Abschnitt 10.
- Wörterbuch: `dictionary/README.md`, `dictionary/GOVERNANCE.md`, `dictionary/DECISIONS.md`.
- Validator und Profile: keine Änderung.
- Agent Skill: neue Referenzen durch `tools/sync_skill.py`.

## Entscheidung

**Ergebnis:** accepted

**Begründung:** Der Maintainer hat am 12. November 2026 entschieden. Die Änderungen beseitigen Widersprüche. Sie ändern kein Prüfergebnis.
