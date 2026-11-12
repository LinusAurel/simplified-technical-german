# Beiträge zu STG-DE

STG-DE soll branchenübergreifend und für verschiedene Arten von Kommunikation funktionieren. Aus diesem Grund sollen Beiträge allgemeines Deutsch von fachspezifischer Terminologie trennen.

## Vorschläge für das zentrale Vokabular

Fügen Sie ein Wort nicht direkt in `dictionary/approved-words.yaml` ein, nur weil das Wort in einem Korpus häufig vorkommt.

Für eine normative Änderung am zentralen Lexikon:

1. Lesen Sie `dictionary/GOVERNANCE.md`.
2. Kopieren Sie `dictionary/proposals/TEMPLATE.yaml`.
3. Vergeben Sie eine ID für den Vorschlag, zum Beispiel `LEX-2026-001`.
4. Definieren Sie eine kontrollierte Bedeutung und eine Wortart.
5. Dokumentieren Sie das Risiko der Mehrdeutigkeit und die geprüften Alternativen.
6. Fügen Sie Belege aus Korpus, öffentlichen Quellen oder Linguistik hinzu, wenn anwendbar.
7. Erklären Sie, ob der Begriff in den zentralen Kern gehört und nicht in die Projektterminologie.
8. Fügen Sie Tests hinzu oder aktualisieren Sie Tests, wenn sich das Verhalten des Validators ändert.
9. Dokumentieren Sie die endgültige Entscheidung der Prüfung vor dem Merge der normativen Änderung am Wörterbuch.

`schemas/lexicon-proposal.schema.json` definiert das Format der Vorschläge.

### Zentraler Kern oder Projektterminologie

Bevorzugen Sie die Projektterminologie in `.stg-de.yaml`, wenn ein Wort hauptsächlich zu einer dieser Gruppen gehört:

- ein Name eines Produkts oder einer Komponente,
- fachspezifischer Jargon mit einer präzisen lokalen Bedeutung,
- Terminologie, die eine Organisation oder ein technischer Standard definiert,
- ein Wort, das hauptsächlich die Abdeckung eines Korpus oder eines Fachgebiets erhöht.

Ein abgelehnter Vorschlag für den zentralen Kern kann trotzdem gültige Projektterminologie sein.

## Änderungen an Regeln

Eine Änderung an einer Regel soll diese Punkte enthalten:

- das Problem, das die Änderung löst,
- mindestens ein nicht konformes Beispiel und ein konformes Beispiel,
- die erwartete Wirkung auf vorhandene Texte,
- die Folgen für den Validator, wenn anwendbar,
- eine Aktualisierung von `quality/RULE-COVERAGE.md`, wenn sich der Stand der Automatisierung ändert.

Regel-IDs sind stabile Bezeichner. Erfinden Sie im Code des Validators keine neue ID, bevor Sie die ID in `rules/rule-index.yaml` eingetragen haben.

## Änderungen am Korpus

Befolgen Sie `corpus/PROTOCOL.md`.

Committen Sie keine Volltextdokumente Dritter für das Korpus, außer die Rechte zur Weitergabe sind explizit. Fügen Sie stattdessen Metadaten und abgeleitete Kennzahlen hinzu.

Die Holdout-Partition dient nur der Evaluation. Verwenden Sie die Liste der unbekannten Tokens der Holdout-Partition nicht, um zentrales Vokabular für dasselbe Release auszuwählen.

## Tests

Führen Sie für die normale Entwicklung diese Befehle aus:

```bash
python -m unittest discover -s tests -v
python tools/sync_skill.py --check
python tools/validate_release.py --skip-manifest
```

Erzeugen Sie vor einem getaggten Release das Manifest neu. Führen Sie danach die vollständige Prüfung der Integrität aus:

```bash
python tools/build_manifest.py
python tools/validate_release.py
```

Eine Funktion des Validators muss Regressionstests für die Regel-ID der Funktion enthalten. Wenn anwendbar, muss die Funktion auch Regressionstests für eine bekannte Grenze falsch positiver Befunde enthalten.
