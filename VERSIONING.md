# STG-DE-Versionierungsrichtlinie

STG-DE verwendet für öffentliche Releases semantische Versionen: `MAJOR.MINOR.PATCH`.

Spezifikation, Wörterbuch, Validator und mitgelieferter Agent Skill sind eng gekoppelt. Solange diese Kopplung besteht, erscheinen sie zusammen als ein Release des Repositorys. Einzelne Werkzeuge können später eigene Paketversionen erhalten. Jedes paketierte Artefakt muss die Version der STG-DE-Spezifikation angeben, auf die es sich bezieht.

## Vor 1.0

Das Projekt ist experimentell. Minor-Releases können normative Ergänzungen oder Einschränkungen enthalten. Jede inkompatible Änderung muss in `CHANGELOG.md` ausdrücklich genannt sein.

- **PATCH**: redaktionelle Korrekturen, Tests, Korrekturen an Werkzeugen und Korrekturen am Validator, die das Verhalten an die veröffentlichten Regeln anpassen.
- **MINOR**: neue Regeln, neue Anwendungsprofile, Ergänzungen im zentralen Wörterbuch, neue Funktionen des Validators oder dokumentierte normative Präzisierungen.
- **MAJOR**: reserviert für 1.0 oder für einen absichtlichen Bruch der Kompatibilität nach 1.0.

## Nach 1.0

### PATCH

Kein beabsichtigter Bruch der normativen Kompatibilität. Beispiele:

- Korrekturen von Tippfehlern und Dokumentation,
- Fehlerkorrekturen, wenn die Implementierung der veröffentlichten Regel widersprach,
- zusätzliche Tests,
- Verbesserungen der Leistung,
- neue nicht normative Beispiele.

### MINOR

Abwärtskompatible Ergänzungen von Funktionen. Beispiele:

- ein neues optionales Anwendungsprofil,
- ein neues zugelassenes zentrales Wort, das keine vorhandenen Bedeutungen ändert,
- zusätzliche Warnungen des Validators oder zusätzliche Belege für das Review,
- neue Werkzeuge oder Integrationen.

### MAJOR

Eine Änderung, durch die ein bisher konformer Text nicht mehr konform sein kann. Oder eine Änderung, die die kontrollierte Interpretation eines vorhandenen Texts ändert. Beispiele:

- eine vorhandene zugelassene Bedeutung einschränken oder verbieten,
- einen verbindlichen Schwellenwert für Sätze ändern,
- die kontrollierte Bedeutung eines vorhandenen Eintrags ändern,
- die Semantik eines Profils inkompatibel ändern,
- eine unterstützte öffentliche Schnittstelle entfernen.

## Regel-IDs

Regel-IDs sind stabiler als die Dateistruktur. Wenn Sie einen Regelabschnitt umbenennen oder verschieben, ist das kein Grund für eine neue Nummerierung der IDs.

Eine abgekündigte Regel-ID bleibt reserviert.

## Kompatibilität des Wörterbuchs

Wir empfehlen, jede normative lexikalische Änderung in ihrem Vorschlag mit einer dieser Klassen zu kennzeichnen:

- `compatible_addition`,
- `clarification`,
- `restriction`,
- `meaning_change`,
- `deprecation`,
- `prohibition`.

Einschränkungen, Bedeutungsänderungen, Abkündigungen und Verbote müssen im Changelog deutlich sichtbar sein.

## Schweregrad im Validator

Wenn Sie einen vorhandenen Befund von `review` oder `warning` zu einem deterministischen `error` hochstufen, ist das eine normative Änderung der Kompatibilität. Eine Ausnahme gilt, wenn diese zwei Bedingungen zutreffen: Die veröffentlichte Regel forderte dieses Verhalten vorher eindeutig. Der vorherige Schweregrad war ein Fehler der Implementierung.

## Agent Skill

Änderungen, die nur das Prompt-Routing oder die Qualität der Implementierung verbessern, sind im Normalfall PATCH-Änderungen. Eine Änderung am Skill kann die Semantik der STG-DE-Ausgabe absichtlich ändern. Für diese Änderung gelten dieselben Kompatibilitätsregeln wie für den zugrunde liegenden Standard.
