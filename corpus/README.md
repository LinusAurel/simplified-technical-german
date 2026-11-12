# Artefakte zur Korpusvalidierung von STG-DE

Dieses Verzeichnis enthält abgeleitete Validierungsartefakte aus öffentlicher deutscher technischer Dokumentation. Es enthält keine Handbücher von Dritten und keine Auszüge aus Quellen.

## Dateien

- `validation-report.md`: Ergebnisse der Validierung des Belegsets von Release 0.4.0 in einer für Menschen lesbaren Form.
- `sources.yaml`: Metadaten öffentlicher Quellen, Zugriffsdaten, Token-Anzahl der Stichproben und SHA-256-Hashes der Stichproben.
- `source-metrics.csv`: lexikalische Metriken je Quelle.
- `industry-metrics.csv`: aggregierte Metriken je Branche.
- `coverage-curves.csv`: Ergebnisse zur schrittweisen lexikalischen Abdeckung.
- `findings.yaml`: Befunde und Einschränkungen der Kuratierung in einer für Agenten lesbaren Form.
- `v0.5-sources.yaml`: Quellen des Volltextkorpus mit Domäne, Textsorte, Organisation, Partition, Abrufdatum und Extraktionsmethode. Die Partition steht vor jeder Analyse fest.
- `v0.5-fulltext-metrics.yaml`: Kennzahlen des Volltextkorpus je Quelle, Partition, Domäne und Textsorte, mit und ohne Obergrenze je Quelle.
- `HOLDOUT-PRECISION.md` und `holdout-precision.yaml`: Präzision des Linters auf der Holdout-Partition. Die YAML-Datei enthält nur Kennzahlen, Hashes und Bewertungen.

## Design des Korpus

Das Belegset von Release 0.4.0 in `sources.yaml` enthält 18 öffentliche deutsche Quellen. Es enthält je drei Quellen aus Maschinenbau, Automotive, Elektrotechnik, Software/IT, Medizintechnik und Anlagenbau. Das Repository verteilt nur abgeleitete Metriken und Metadaten.

Ab Release 0.5.0 misst STG-DE die Abdeckung mit dem Volltextkorpus in `v0.5-sources.yaml`. Die Zahl der Quellen, Partitionen und Domänen steht in `v0.5-fulltext-metrics.yaml`.

Die Abdeckung misst, wie viele beobachtete Token zu einem dieser Elemente aufgelöst werden: zentrales kontrolliertes Lexikon, deklarierte Pluralformen von Nomen oder zugelassene Kontraktionen. Die Abdeckung ist keine Qualitätsbewertung einer Quelle. Sie ist auch kein Ziel, das Sie durch die Aufnahme von Domänenterminologie in den Kern maximieren.
