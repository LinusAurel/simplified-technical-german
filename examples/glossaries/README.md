# Beispiel-Glossare

Diese Dateien zeigen Projektterminologie für Branchen, die das zentrale Wörterbuch absichtlich nicht enthält. Kopieren Sie eine Datei als `.stg-de.yaml` in Ihr Projekt. Entfernen Sie Begriffe, die Ihr Projekt nicht verwendet. Ergänzen Sie die Begriffe Ihres Produkts.

| Datei | Bereich |
|---|---|
| `embedded-iot.stg-de.yaml` | Firmware, Gateways, Feldbusse, Flotten von Geräten und OTA-Updates |
| `functional-safety.stg-de.yaml` | Funktionale Sicherheit nach IEC 61508, ISO 13849 und ISO 26262 |
| `product-security.stg-de.yaml` | Schwachstellen, Sicherheitsupdates und Cyber Resilience Act |
| `medical-devices.stg-de.yaml` | Medizinprodukte nach MDR, IEC 62304, IEC 60601-1 und ISO 14971 |

Die Definitionen sind kurze Arbeitsdefinitionen. Die Norm oder die Verordnung Ihres Projekts ist maßgeblich.

Ein Begriff im Glossar hat Vorrang vor der zentralen Sperrliste. Die Beispiele enthalten deshalb kein gesperrtes Wort. Ein Test prüft das.

Kombinieren Sie mehrere Glossare in einer Datei, wenn Ihr Projekt mehrere Bereiche hat. Ein Gateway mit einer Sicherheitsfunktion benötigt zum Beispiel `embedded-iot` und `functional-safety`.
