# Artefakte zur Korpusvalidierung von STG-DE

Dieses Verzeichnis enthält abgeleitete Validierungsartefakte aus öffentlicher deutscher technischer Dokumentation. Es enthält keine Handbücher von Dritten und keine Auszüge aus Quellen.

## Dateien

- `fulltext-sources.yaml`: Quellen des Volltextkorpus mit Domäne, Textsorte, Organisation, Partition, Abrufdatum und Extraktionsmethode. Die Partition steht vor jeder Analyse fest.
- `fulltext-metrics.yaml`: Kennzahlen des Volltextkorpus je Quelle, Partition, Domäne und Textsorte, mit und ohne Obergrenze je Quelle.
- `HOLDOUT-PRECISION.md` und `holdout-precision.yaml`: Präzision des Linters auf der Holdout-Partition. Die YAML-Datei enthält nur Kennzahlen, Hashes und Bewertungen.

## Design des Korpus

STG-DE misst die Abdeckung mit dem Volltextkorpus in `fulltext-sources.yaml`. Die Zahl der Quellen, Partitionen und Domänen steht in `fulltext-metrics.yaml`. Das Repository verteilt nur abgeleitete Kennzahlen und Metadaten. Der Befehl `python tools/build_corpus.py` lädt die Quellen und berechnet die Kennzahlen.

Die Abdeckung misst, wie viele beobachtete Token zu einem dieser Elemente aufgelöst werden: zentrales kontrolliertes Lexikon, deklarierte Pluralformen von Nomen oder zugelassene Kontraktionen. Die Abdeckung ist keine Qualitätsbewertung einer Quelle. Sie ist auch kein Ziel, das Sie durch die Aufnahme von Domänenterminologie in den Kern maximieren.
