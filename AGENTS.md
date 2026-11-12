# AGENTS.md

## Zweck

Dieses Repository enthält die kanonische Spezifikation von STG-DE, das Wörterbuch, die Validator-Werkzeuge, öffentliche Kennzahlen aus Korpora und die Quelle des paketierten Agent Skills.

## Maßgebliche Quellen

- Ändern Sie kanonische Regeln in `rules/`.
- Ändern Sie die zentrale Terminologie in `dictionary/`.
- Ändern Sie Daten der Zuordnung in `mapping/`.
- Ändern Sie erzeugte Dateien in `skills/simplified-technical-german/references/` nicht von Hand. Ändern Sie die erzeugte Kopie des Linters im Skill nicht von Hand.
- Ändern Sie die Kopien im Paket `stg_de/` nicht von Hand.
- Führen Sie nach kanonischen Änderungen `python tools/sync_skill.py` und `python tools/sync_package.py` aus.
- Erzeugen Sie `STG-DE.md` mit `python tools/build_standalone.py` neu.
- Erzeugen Sie `manifest.yaml` nur vor einem getaggten Release mit `python tools/build_manifest.py` neu.

## Grenze für Korpora

Verwenden Sie in Validierungsartefakten des Repositorys nur öffentliche oder ausdrücklich genehmigte Korpusquellen. Committen Sie keine vollständigen Handbücher Dritter und keine privaten Quelldokumente. Speichern Sie nur Metadaten der Quellen und abgeleitete Kennzahlen.

## Validierung

Dieser Abschnitt ist die maßgebliche Liste der Prüfungen. Die CI führt dieselben Prüfungen aus. Die CI überspringt nur die Prüfung des Manifests (`--skip-manifest`). Der Release-Workflow prüft das Manifest.

Erzeugen Sie vor einem Commit die abgeleiteten Dateien neu. Fügen Sie neue Dateien vor `build_manifest.py` mit `git add` hinzu, weil das Manifest nur Dateien unter Git-Kontrolle enthält:

```bash
python tools/sync_skill.py
python tools/sync_package.py
python tools/build_standalone.py
python tools/build_manifest.py
```

Führen Sie danach diese Prüfungen aus:

```bash
python -m unittest discover -s tests -v
python tools/sync_skill.py --check
python tools/build_standalone.py --check
python tools/sync_package.py --check
python tools/validate_release.py
```

## Sprachdesign

Fügen Sie ein Wort nicht nur deshalb in das zentrale Wörterbuch ein, weil das Wort häufig vorkommt. Bevorzugen Sie Projektterminologie für enge Begriffe aus Produkt, Unternehmen, Wissenschaft, Recht, Medizin oder Branche. Erhalten Sie die Unterscheidung zwischen deterministischen Verstößen und heuristischen Befunden, die eine Prüfung erfordern.
