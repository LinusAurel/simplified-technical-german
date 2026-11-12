# Artefakte zur Korpusvalidierung: STG-DE v0.4

Dieses Verzeichnis enthält abgeleitete Validierungsartefakte aus öffentlicher deutscher technischer Dokumentation. Es enthält keine Handbücher von Dritten und keine Auszüge aus Quellen.

## Dateien

- `validation-report.md`: Ergebnisse der Validierung in einer für Menschen lesbaren Form.
- `sources.yaml`: Metadaten öffentlicher Quellen, Zugriffsdaten, Token-Anzahl der Stichproben und SHA-256-Hashes der Stichproben.
- `source-metrics.csv`: lexikalische Metriken je Quelle.
- `industry-metrics.csv`: aggregierte Metriken je Branche.
- `coverage-curves.csv`: Ergebnisse zur schrittweisen lexikalischen Abdeckung.
- `findings.yaml`: Befunde und Einschränkungen der Kuratierung in einer für Agenten lesbaren Form.

## Design des Korpus

Das Belegset von v0.4 enthält 18 öffentliche deutsche Quellen. Es enthält je drei Quellen aus Maschinenbau, Automotive, Elektrotechnik, Software/IT, Medizintechnik und Anlagenbau. Das Repository verteilt nur abgeleitete Metriken und Metadaten.

Die Abdeckung misst, wie viele beobachtete Token zu einem dieser Elemente aufgelöst werden: zentrales kontrolliertes Lexikon, deklarierte Pluralformen von Nomen oder zugelassene Kontraktionen. Die Abdeckung ist keine Qualitätsbewertung einer Quelle. Sie ist auch kein Ziel, das Sie durch die Aufnahme von Domänenterminologie in den Kern maximieren.
