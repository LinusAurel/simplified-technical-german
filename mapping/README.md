# Rückverfolgbarkeit zu den Quellregeln

`ste100-issue9.yaml` ordnet jede Schreibregel und jede allgemeine Empfehlung von **ASD-STE100 Issue 9 (Januar 2025)** der STG-DE-Regel zu, die dieselbe Absicht für das Deutsche umsetzt.

## Die Zuordnung lesen

| Feld | Bedeutung |
|---|---|
| `ste` | Regelnummer von ASD-STE100 (`1.1` … `9.4`) oder allgemeine Empfehlung (`GR-1` … `GR-8`). |
| `stg` | Primäre STG-DE-Regel. Nummerierte STG-Regeln verwenden die Nummer von ASD-STE100: `STG-5.1` setzt Regel 5.1 um. |
| `related` | Andere STG-DE-Regeln, die einen Teil desselben Risikos abdecken. |
| `relation` | `equivalent`, `adapted` oder `replaced` (siehe unten). |
| `note` | Unabhängig geschriebene deutsche Erklärung der Anpassung. |

- `equivalent` — dieselbe Absicht. Die deutschen Formulierungen und Beispiele sind unabhängig.
- `adapted` — dieselbe Absicht, aber Geltungsbereich, Schwellenwerte oder Mechanik sind an die deutsche Grammatik angepasst.
- `replaced` — die Quellregel betrifft ein Phänomen des Englischen, zum Beispiel die `-ing`-Form oder Phrasal Verbs. STG-DE ersetzt die Quellregel durch das deutsche Phänomen mit demselben Risiko, zum Beispiel Nominalisierung oder Funktionsverbgefüge.

`german_extensions` nennt die `STG-DE-*`-Regeln ohne direktes Gegenstück in ASD-STE100, mit der nächstliegenden Quellregel.

## Zusammenfassung

| Beziehung | Schreibregeln | Allgemeine Empfehlungen |
|---|---:|---:|
| equivalent | 35 | 2 |
| adapted | 15 | 4 |
| replaced | 3 | 2 |
| **gesamt** | **53** | **8** |

Alle 75 STG-DE-Regeln und -Empfehlungen sind von dieser Datei aus erreichbar. `tests/test_mapping.py` prüft die Vollständigkeit.

## Grenze des Urheberrechts

ASD-STE100 ist ein Urheberrecht und eine in der EU eingetragene Marke von ASD (Aerospace, Security and Defence Industries Association of Europe), Brüssel. Der Standard ist kostenlos unter <https://www.asd-ste100.org> erhältlich. Eine Weitergabe erfordert aber eine schriftliche Genehmigung von ASD.

Aus diesem Grund enthält dieses Repository **nur Regelnummern und unabhängig geschriebenen deutschen Text**. Das Repository gibt keine Formulierungen von Regeln, keine Beispiele und keine Wörterbucheinträge aus ASD-STE100 wieder. STG-DE ist keine offizielle Veröffentlichung von ASD. STG-DE hat keine Billigung (Endorsement) durch ASD oder die STEMG.
