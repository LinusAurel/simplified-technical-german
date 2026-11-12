# STG-DE-Release-Checkliste

Verwenden Sie diese Checkliste für jedes Release mit Tag.

## Umfang und Kompatibilität

- [ ] Legen Sie die vorgesehene Version nach `VERSIONING.md` fest.
- [ ] Prüfen Sie alle Änderungen an normativen Regeln und am Wörterbuch seit dem vorherigen Release.
- [ ] Dokumentieren Sie Einschränkungen, Bedeutungsänderungen, Abkündigungen und Verbote in `CHANGELOG.md`.
- [ ] Prüfen Sie, dass niemand veröffentlichte Regel-IDs versehentlich neu nummeriert oder wiederverwendet hat.
- [ ] Prüfen Sie, dass die Anwendungsprofile gültige Regel-IDs referenzieren.

## Spezifikation und Wörterbuch

- [ ] Parsen Sie alle YAML- und JSON-Ressourcen.
- [ ] Prüfen Sie, dass die IDs der Wörterbucheinträge und der kontrollierten Bedeutungen eindeutig sind.
- [ ] Prüfen Sie, dass sich zugelassene und verbotene kanonische Einträge nicht unbeabsichtigt überschneiden.
- [ ] Prüfen Sie die angenommenen lexikalischen Vorschläge für das Release.
- [ ] Prüfen Sie, dass Projekt- oder Domänenterminologie nicht nur für eine höhere Korpus-Abdeckung in den zentralen Kern kam.

## Validator und Qualität

- [ ] Führen Sie `python -m unittest discover -s tests -v` aus.
- [ ] Führen Sie `python tools/sync_skill.py --check` aus.
- [ ] Führen Sie `python tools/validate_release.py --skip-manifest` aus.
- [ ] Prüfen Sie, dass `quality/rule-coverage.yaml` jede veröffentlichte Regel genau einmal enthält.
- [ ] Prüfen Sie bei neuen deterministischen Prüfungen die Grenzen für falsch positive Befunde.
- [ ] Prüfen Sie, dass die Golden-Audit-Fixtures bestehen.

## Korpus und Belege

- [ ] Prüfen Sie, dass die Entwicklungs-, Validierungs- und Holdout-Partitionen vor der Release-Evaluation festgelegt sind.
- [ ] Prüfen Sie, dass niemand Holdout-Belege verwendet hat, um Wörterbuch oder Regeln desselben Release abzustimmen.
- [ ] Führen Sie den reproduzierbaren Korpus-Workflow aus, wenn das Release korpusabhängiges Verhalten ändert.
- [ ] Dokumentieren Sie Fehler bei Quellen und Einschränkungen bei der Extraktion.
- [ ] Veröffentlichen Sie nur zulässige Metadaten und abgeleitete Metriken. Fügen Sie keinen unbearbeiteten Text von Dritten ohne Rechte zur Weitergabe hinzu.
- [ ] Dokumentieren Sie die Token-Anzahl und die Metriken je Domäne und je Partition.

## Agent Skill

- [ ] Führen Sie `python tools/package_skill.py` und `claude plugin validate .` aus.
- [ ] Führen Sie `python tools/run_evals.py --outputs evals/reference` aus. Das Ergebnis muss 100 % sein.
- [ ] Prüfen Sie, dass die mitgelieferten Referenzen und der Linter mit den kanonischen Dateien des Repositorys synchron sind.
- [ ] Führen Sie `python tools/run_evals.py --command "<model CLI>"` mit mindestens einem Modell aus. Dokumentieren Sie das Ergebnis.
- [ ] Prüfen Sie, dass sich das Standardverhalten der Ausgabe für WRITE und REWRITE nicht unbeabsichtigt geändert hat.

## Integrität der Artefakte

- [ ] Erstellen Sie die eigenständigen generierten Artefakte, wenn zutreffend.
- [ ] Führen Sie `python tools/build_manifest.py` nur aus, wenn alle Release-Dateien endgültig sind.
- [ ] Führen Sie `python tools/validate_release.py` mit aktivierter Validierung des Manifests aus.
- [ ] Erzeugen Sie SHA-256-Prüfsummen für die herunterladbaren Release-Artefakte.
- [ ] Prüfen Sie, dass der Commit mit dem Tag zum Release-Manifest passt.

## Veröffentlichung

- [ ] Aktualisieren Sie die Version in `CITATION.cff`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `pyproject.toml` und `stg_de/__init__.py`. Aktualisieren Sie `STG_VERSION` in `tools/stg_lint.py` und `tools/stg_compare.py`. Aktualisieren Sie die Felder `release` der Datendateien. `tests/test_packaging.py` prüft, dass alle Versionen übereinstimmen.
- [ ] Erstellen Sie den Git-Tag `vX.Y.Z`. Der Release-Workflow erstellt das Skill-ZIP und die Prüfsumme und veröffentlicht das GitHub-Release.
- [ ] Veröffentlichen Sie Release Notes aus `CHANGELOG.md` und den angenommenen Vorschlägen.
- [ ] Hängen Sie den paketierten Agent Skill und andere Release-Artefakte an, wenn verfügbar.
- [ ] Veröffentlichen Sie die Prüfsummendatei mit den Release-Assets.
- [ ] Prüfen Sie Versions- und Statusinformationen und Installationsbeispiele in der README.

## Nach dem Release

- [ ] Prüfen Sie die CI für den Commit mit dem Tag und für den Commit auf dem Standard-Branch.
- [ ] Öffnen Sie Folge-Issues für bekannte Einschränkungen, deren Bearbeitung ausdrücklich verschoben wurde.
- [ ] Ändern Sie Holdout-Ergebnisse für das Release mit Tag nicht nachträglich.
