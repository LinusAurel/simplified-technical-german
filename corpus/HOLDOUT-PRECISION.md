# Präzision des Linters auf dem Holdout

Diese Messung prüft, wie oft der Linter auf echten deutschen Texten richtig liegt. Grundlage ist die Holdout-Partition des Korpus aus `corpus/v0.5-sources.yaml`. Die Entwicklung des Wörterbuchs und des Linters verwendet diese Quellen nicht.

Die Kennzahlen der letzten Messung stehen in `corpus/holdout-precision.yaml`. Das Repository enthält keinen Text aus den Quellen. Jeder bewertete Befund hat nur eine ID: die ersten 16 Zeichen des SHA-256-Hashes aus Quelle, Regel und Satz.

## Zweck

Eine stabile Version 1.0 verlangt eine dokumentierte Rate falsch positiver Befunde (siehe `ROADMAP.md`). Die Messung zeigt, welchen Prüfungen ein Autor vertrauen kann. Die Messung zeigt auch, welche Prüfungen eine Korrektur brauchen, bevor eine Prüfung eine höhere Stufe erhält.

## Methode

1. `tools/holdout_precision.py sample` lädt die Quellen und prüft sie mit dem Profil `description`. Das Werkzeug wählt mit festem Startwert bis zu 50 Befunde je Quelle aus (Stufe `error` und `warning`).
2. Das Werkzeug wählt zusätzlich 15 Sätze je Quelle ohne Befund aus. Das Werkzeug prüft jeden dieser Sätze einzeln mit dem Linter.
3. Jeder Befund erhält ein Label:
   - `tp`: Der Befund ist ein echter Verstoß gegen die Regel.
   - `fp`: Der Linter liegt falsch.
   - `extraction`: Der Befund entsteht beim Auslesen von PDF oder HTML, zum Beispiel durch zusammengefügte Seitenköpfe, Menüs oder Tabellen.
   - Für Sätze ohne Befund: `fn`, wenn der Satz gegen eine implementierte Prüfung verstößt, sonst `ok`.
4. `tools/holdout_precision.py score` berechnet die Kennzahlen.

### Bewertung durch zwei Modelle

Zwei Sprachmodelle von zwei Anbietern bewerten jeden Eintrag unabhängig. Kein Modell sieht das Label des anderen Modells:

1. `gpt-6.1-sol` mit mittlerem Aufwand über die Codex-CLI,
2. `claude-opus-5-5` über die Claude-Code-CLI.

Bei gleichen Labels gilt dieses Label. Bei verschiedenen Labels bewerten beide Modelle den Eintrag erneut mit höherem Aufwand. Beide Modelle sehen dann beide Labels. Wenn die Modelle sich danach nicht einigen, entscheidet ein dritter Durchgang mit dem Auszug und beiden Begründungen. Die Bewertungsdatei mit allen Labels liegt außerhalb des Repositorys, weil sie Text der Quellen enthält.

## Ergebnis für den Linter nach 0.6.0

Gemessen am 12. November 2026 mit dem Stand von `main` nach Release 0.6.0. Dieser Stand enthält die drei Korrekturen aus Issue #3. Die Holdout-Partition hat 7 Quellen aus 7 Domänen:

- Release Notes einer Firmware,
- eine Hilfeseite zum Firmware-Update,
- eine Bedienungsanleitung aus der Messtechnik,
- eine Seite zur funktionalen Sicherheit,
- eine Seite mit Anweisungen für Agenten,
- ein Hilfeartikel einer B2B-Software,
- eine Produktinformation zu einem Medizinprodukt.

Die Modelle hatten bei 274 von 295 eindeutigen Einträgen dasselbe Label (93 %). Die zweite Runde hat 7 Abweichungen gelöst. Der dritte Durchgang hat 14 Einträge entschieden.

| Kennzahl | Wert |
|---|---:|
| Bewertete Befunde | 197 |
| Richtig (`tp`) | 87 |
| Falsch (`fp`) | 22 |
| Extraktionsfehler | 88 |
| Präzision ohne Extraktionsfehler | 79,8 % |
| Präzision mit Extraktionsfehlern | 44,2 % |
| Sätze ohne Befund mit übersehenem Verstoß | 4 von 105 |

| Regel | Bewertet | Richtig | Falsch | Extraktion | Präzision ohne Extraktion |
|---|---:|---:|---:|---:|---:|
| `STG-1.1` | 47 | 35 | 7 | 5 | 83,3 % |
| `STG-5.3` | 2 | 1 | 0 | 1 | keine Aussage |
| `STG-6.3` | 115 | 45 | 5 | 65 | 90,0 % |
| `STG-6.6` | 15 | 0 | 0 | 15 | keine Aussage |
| `STG-8.1` | 14 | 2 | 10 | 2 | 16,7 % |
| `STG-DE-4.3` | 3 | 3 | 0 | 0 | keine Aussage |
| `STG-DE-8.1` | 1 | 1 | 0 | 0 | keine Aussage |

### Bewertung

- **Satzlänge (`STG-6.3`):** 90 % der Befunde ohne Extraktionsfehler sind richtig. Die falschen Befunde zählen fett gedruckte Marken wie `**NEU**` vor dem Satz mit. Oder ein `z.B.` ohne Leerzeichen beendet den Satz nicht richtig.
- **Wortschatz (`STG-1.1`):** 83 % sind richtig. Die falschen Befunde betreffen Namen und UI-Texte, zum Beispiel den Titel einer Zeitschrift mit `aktuell` oder die Schaltfläche `Weiter`. Auch ein `sollte` am Satzanfang als Bedingung zählt dazu.
- **Semikolon (`STG-8.1`):** Diese Prüfung ist auf echten Texten nicht zuverlässig. 10 von 12 Befunden sind Semikolons in Listen von Autoren oder Normen, zum Beispiel `IEC 60601-1; IEC 60601-1-2`. Diese Semikolons verbinden keine Aussagen. Die Regel verbietet nur Semikolons zwischen Aussagen.
- **Absatzlänge (`STG-6.6`):** Alle 15 Befunde sind Extraktionsfehler. Die Messung erlaubt keine Aussage über die Prüfung.
- **Übersehene Verstöße:** 3 der 4 Sätze mit `fn` enthalten `entsprechend`. Der Linter meldet `entsprechend` mit der Stufe `review`. Die Stichprobe zählt nur Befunde mit `error` und `warning`. Diese Sätze sind deshalb kein Fehler des Linters.

### Folgerungen

- Die Prüfung `STG-8.1` braucht eine Unterscheidung zwischen Semikolons in Listen und Semikolons zwischen Aussagen.
- Die Prüfung `STG-6.3` soll Marken in Fettschrift am Satzanfang nicht mitzählen. Die Prüfung soll `z.B.` ohne Leerzeichen als Abkürzung erkennen.
- Extraktionsfehler verursachen fast die Hälfte aller Befunde. Diese Fehler entstehen im Werkzeug für das Korpus, nicht im Linter. Auf sauberem Markdown oder Text treten diese Fehler nicht auf.

Die Korrekturen stehen in `ROADMAP.md` (Release 0.8.0). Eine Messung der korrigierten Version braucht wieder neue Holdout-Quellen.

## Frühere Messung: Linter 0.6.0

Die erste Messung war mit Linter 0.6.0 auf der damaligen Holdout-Partition. Diese Partition hatte 4 Quellen: eine Bedienungsanleitung (Anlagenbau), eine Hilfeseite (Logistik), eine Behördenseite (öffentlicher Sektor) und einen Ratgeber für Verbraucher (Energie). Ein Modell (Claude) hat die Befunde bewertet.

| Kennzahl | Wert |
|---|---:|
| Bewertete Befunde | 131 |
| Richtig (`tp`) | 52 |
| Falsch (`fp`) | 4 |
| Extraktionsfehler | 75 |
| Präzision ohne Extraktionsfehler | 92,9 % |
| Präzision mit Extraktionsfehlern | 39,7 % |
| Sätze ohne Befund mit übersehenem Verstoß | 5 von 60 |

Die Messung hat drei Schwächen des Linters gezeigt. Die Korrekturen sind nach der Messung entstanden:

1. **Aufzählungspunkte:** Der Linter hat `•` und ähnliche Zeichen nicht als Listenpunkt erkannt. Aufzählungen sind deshalb zu langen „Sätzen“ verschmolzen.
2. **Abkürzungen:** `bzw.`, `z. B.`, `Nr. 5` und Datumsangaben wie `31. Dezember` haben einen Satz fälschlich beendet.
3. **Flexion:** Gebeugte Formen gesperrter Adjektive (`einfache`, `aktuellen`, `entsprechenden`) waren unerkannt. Der Linter wertet jetzt das Feld `surface_forms` der Sperrliste aus.

Die 4 Quellen dieser Messung sind jetzt in der Entwicklungspartition (Protokoll Abschnitt 9).

Diese Messung ist nicht vollständig reproduzierbar. Die drei HTML-Seiten haben sich nach der Messung geändert. Eine neue Stichprobe mit Linter 0.6.0 vom 12. November 2026 enthält 89 der 191 bewerteten Einträge. Die Bewertungsdatei der Messung ist nicht erhalten. Außerdem konnte die Stichprobe der Sätze ohne Befund Sätze mit einem gemeldeten Wort enthalten. Das Werkzeug prüft jetzt jeden Satz einzeln und speichert die Hashes der Quellen in der Bewertungsdatei.

## Grenzen

- **Keine Prüfung durch Menschen:** Sprachmodelle haben die Befunde bewertet. Zwei Modelle von zwei Anbietern verringern das Risiko, dass ein Modell systematisch falsch bewertet. Ein Review durch Fachleute ist ein Kriterium für 1.0.
- **Kleine Zahlen:** Für `STG-5.3`, `STG-6.6`, `STG-DE-4.3` und `STG-DE-8.1` gibt es zu wenige Befunde für eine Aussage.
- **Übersehene Verstöße:** Die Stichprobe der Sätze ohne Befund prüft nur implementierte Prüfungen. Verstöße gegen semantische Regeln zählt sie nicht.
- **Zeitpunkt:** Die Quellen sind Webseiten und PDFs. Ihr Inhalt kann sich ändern. Die Hashes in `corpus/v0.5-fulltext-metrics.yaml` und in der Bewertungsdatei zeigen, ob eine Quelle noch dieselbe ist.

## Messung wiederholen

```bash
python tools/holdout_precision.py sample --out <Ordner außerhalb des Repositorys>
python tools/holdout_precision.py score <Ordner>/holdout-labels.yaml --labeler "<Bewertung>"
```

Wiederholen Sie die Stichprobe für Linter 0.6.0 mit den alten Quellen:

```bash
python tools/holdout_precision.py sample --out <Ordner> --sources PLANT-WILO-STRATOS-FULL LOG-DHL-ONLINE-FRANKIERUNG PUBLIC-AUSWEISAPP ENERGY-VZ-WECHSEL
```
