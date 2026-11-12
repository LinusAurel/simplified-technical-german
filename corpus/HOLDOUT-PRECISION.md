# Präzision des Linters auf dem Holdout

Diese Messung prüft, wie oft der Linter auf echten deutschen Texten richtig liegt. Grundlage ist die Holdout-Partition des Korpus aus `corpus/v0.5-sources.yaml`. Die Holdout-Partition hat 4 Quellen: eine Bedienungsanleitung (Anlagenbau), eine Hilfeseite (Logistik), eine Behördenseite (öffentlicher Sektor) und einen Ratgeber für Verbraucher (Energie).

Die Kennzahlen stehen in `corpus/holdout-precision.yaml`. Das Repository enthält keinen Text aus den Quellen. Jeder bewertete Befund hat nur eine ID: die ersten 16 Zeichen des SHA-256-Hashes aus Quelle, Regel und Satz.

## Methode

1. `tools/holdout_precision.py sample` lädt die Quellen und prüft sie mit dem Profil `description`. Das Werkzeug wählt mit festem Startwert bis zu 50 Befunde je Quelle aus (Stufe `error` und `warning`).
2. Das Werkzeug wählt zusätzlich 15 Sätze je Quelle ohne Befund aus.
3. Eine Person oder ein Modell bewertet jeden Befund:
   - `tp`: Der Befund ist ein echter Verstoß gegen die Regel.
   - `fp`: Der Linter liegt falsch.
   - `extraction`: Der Befund entsteht beim Auslesen von PDF oder HTML, zum Beispiel durch zusammengefügte Seitenköpfe, Menüs oder Tabellen.
   - Für Sätze ohne Befund: `fn`, wenn der Satz gegen eine implementierte Prüfung verstößt, sonst `ok`.
4. `tools/holdout_precision.py score` berechnet die Kennzahlen.

## Ergebnis für Linter 0.6.0

| Kennzahl | Wert |
|---|---:|
| Bewertete Befunde | 131 |
| Richtig (`tp`) | 52 |
| Falsch (`fp`) | 4 |
| Extraktionsfehler | 75 |
| Präzision ohne Extraktionsfehler | 92,9 % |
| Präzision mit Extraktionsfehlern | 39,7 % |
| Sätze ohne Befund mit übersehenem Verstoß | 5 von 60 |

| Regel | Bewertet | Richtig | Falsch | Extraktion | Präzision ohne Extraktion |
|---|---:|---:|---:|---:|---:|
| `STG-1.1` | 45 | 42 | 0 | 3 | 100 % |
| `STG-6.3` | 67 | 8 | 3 | 56 | 72,7 % |
| `STG-6.6` | 16 | 0 | 0 | 16 | keine Aussage |
| `STG-8.1` | 1 | 0 | 1 | 0 | keine Aussage |
| `STG-DE-4.3` | 1 | 1 | 0 | 0 | keine Aussage |
| `STG-DE-8.1` | 1 | 1 | 0 | 0 | keine Aussage |

## Bewertung

- Die lexikalische Prüfung (`STG-1.1`) ist präzise. Jeder Befund ohne Extraktionsfehler war ein Wort aus der Sperrliste in einer Verwendung, die STG-DE vermeidet.
- Die Prüfungen auf Satzlänge (`STG-6.3`) und Absatzlänge (`STG-6.6`) hängen stark von der Textextraktion ab. Auf sauberem Markdown oder Text sind diese Prüfungen zuverlässig. Auf extrahierten PDF- und HTML-Texten sind die meisten Befunde Artefakte.
- Die Zahlen sind klein. Für `STG-8.1`, `STG-DE-4.3` und `STG-DE-8.1` gibt es nur je einen Befund. Die Messung erlaubt für diese Regeln keine Aussage.

## Gefundene Schwächen und Korrekturen

Die Messung hat drei Schwächen des Linters gezeigt. Die Korrekturen sind nach der Messung entstanden:

1. **Aufzählungspunkte:** Der Linter hat `•` und ähnliche Zeichen nicht als Listenpunkt erkannt. Aufzählungen sind deshalb zu langen „Sätzen“ verschmolzen. 3 der 4 falschen Befunde haben diese Ursache.
2. **Abkürzungen:** `bzw.`, `z. B.`, `Nr. 5` und Datumsangaben wie `31. Dezember` haben einen Satz fälschlich beendet.
3. **Flexion:** Gebeugte Formen gesperrter Adjektive (`einfache`, `aktuellen`, `entsprechenden`) waren unerkannt. 5 von 60 Sätzen ohne Befund enthielten solche Formen. Der Linter wertet jetzt das Feld `surface_forms` der Sperrliste aus. 20 Adjektive haben gebeugte Formen erhalten.

Mit den Korrekturen sinkt die Zahl der `STG-6.3`-Befunde auf dem Holdout von 229 auf 174. Die Zahl der `STG-6.6`-Befunde steigt von 49 auf 74. Der Grund: Das Wilo-PDF hat keine Leerzeilen. Ohne erkannte Aufzählungen war jede Seite ein einziger Absatz mit bis zu 219 Sätzen. Die erkannten Aufzählungen teilen diese Blöcke, die Teile bleiben aber zu lang. Alle zusätzlichen Befunde sind Extraktionsfehler.

## Grenzen

- **Bewertung durch ein Modell:** Ein KI-Modell (Claude) hat die Befunde bewertet. Ein Mensch hat die Bewertung noch nicht geprüft. Prüfen Sie die Bewertung mit `tools/holdout_precision.py sample`. Der feste Startwert erzeugt dieselbe Stichprobe.
- **Verbrauchter Holdout:** Die drei Korrekturen sind nach Befunden auf diesem Holdout entstanden. Eine Messung der korrigierten Version braucht neue Holdout-Quellen.
- **Zeitpunkt:** Die Quellen sind Webseiten und PDFs. Ihr Inhalt kann sich ändern. Die Hashes in `corpus/v0.5-fulltext-metrics.yaml` zeigen, ob eine Quelle noch dieselbe ist.
- **Übersehene Verstöße:** Die Stichprobe der Sätze ohne Befund prüft nur implementierte Prüfungen. Verstöße gegen semantische Regeln zählt sie nicht.
