# AGENTS.md

## Zweck

Dieses Repository enthält die kanonische Spezifikation von STG-DE, das Wörterbuch, die Validator-Werkzeuge, öffentliche Kennzahlen aus Korpora und die Quelle des paketierten Agent Skills.

## Maßgebliche Quellen

- Ändern Sie kanonische Regeln in `rules/`.
- Ändern Sie die zentrale Terminologie in `dictionary/`.
- Ändern Sie Daten der Zuordnung in `mapping/`.
- Ändern Sie erzeugte Dateien in `skills/simplified-technical-german/references/` nicht von Hand. Ändern Sie die erzeugte Kopie des Linters im Skill nicht von Hand.
- Ändern Sie den Code der Werkzeuge (Linter, Analysewerkzeug, Vergleich) in `stg_de/`. Diese Module sind die einzige Implementierung.
- Ändern Sie die Datenkopien in `stg_de/dictionary/` und `stg_de/profiles/` nicht von Hand.
- Führen Sie nach kanonischen Änderungen `python tools/sync_skill.py` und `python tools/sync_package.py` aus.
- Committen Sie `STG-DE.md` und `manifest.yaml` nicht. Der Release-Workflow erzeugt beide Dateien und hängt sie an das GitHub-Release an.

## Grenze für Korpora

Verwenden Sie in Validierungsartefakten des Repositorys nur öffentliche oder ausdrücklich genehmigte Korpusquellen. Committen Sie keine vollständigen Handbücher Dritter und keine privaten Quelldokumente. Speichern Sie nur Metadaten der Quellen und abgeleitete Kennzahlen.

## Validierung

Dieser Abschnitt ist die maßgebliche Liste der Prüfungen. Die CI führt dieselben Prüfungen aus. Nur der Release-Workflow erzeugt und prüft das Manifest.

Erzeugen Sie vor einem Commit die abgeleiteten Dateien neu:

```bash
python tools/sync_skill.py
python tools/sync_package.py
```

Führen Sie danach diese Prüfungen aus:

```bash
python -m unittest discover -s tests -v
python tools/sync_skill.py --check
python tools/sync_package.py --check
python tools/validate_release.py --skip-manifest
```

## Sprachdesign

Fügen Sie ein Wort nicht nur deshalb in das zentrale Wörterbuch ein, weil das Wort häufig vorkommt. Bevorzugen Sie Projektterminologie für enge Begriffe aus Produkt, Unternehmen, Wissenschaft, Recht, Medizin oder Branche. Erhalten Sie die Unterscheidung zwischen deterministischen Verstößen und heuristischen Befunden, die eine Prüfung erfordern.
