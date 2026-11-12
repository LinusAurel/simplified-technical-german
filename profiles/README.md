# Anwendungsprofile von STG-DE

Anwendungsprofile passen den einen Standard STG-DE an verschiedene Zwecke der Kommunikation an. Anwendungsprofile erzeugen keine eigenen Dialekte. Anwendungsprofile ändern keine kontrollierten Bedeutungen von Wörtern.

Die maschinenlesbaren Definitionen stehen in `profiles.yaml`.

## Profile

| Profil | Typischer Inhalt | Strukturelle Basis |
|---|---|---|
| `procedure` | Arbeitsschritte für Installation, Betrieb und Wartung | Anleitung, Satzgrenze 20 Wörter |
| `safety` | Warnungen, Vorsichtshinweise, Schutzmaßnahmen | Anleitung, Satzgrenze 20 Wörter + Priorität für Abschnitt 7 |
| `description` | technische Erklärungen und sachliche Beschreibungen | Beschreibung, Satzgrenze 25 Wörter |
| `requirement` | Spezifikationen und Abnahmekriterien | Beschreibung, Priorität für explizite Modalität und expliziten Geltungsbereich |
| `support` | Fehlersuche, Kunden-Support und interner Support | Beschreibung, Priorität für umsetzbare Aussagen und einheitliche Terminologie |
| `consumer` | Anweisungen und Serviceinformationen im B2C-Bereich | Beschreibung, Priorität für klare und explizite Sprache |
| `agent` | Prompts, Tool-Beschreibungen, Anweisungen zwischen Agenten | Anleitung, Satzgrenze 20 Wörter + Priorität für maschinelle Verarbeitung |

## Auswahl

Autoren und Werkzeuge wählen ein Profil am besten nach dem Zweck des Texts aus, nicht nach der Branche.

Ein Medizinprodukt kann Inhalte für `procedure`, `safety` und `description` enthalten. Ein Softwareprodukt kann diese drei Arten von Inhalt enthalten und zusätzlich Inhalte für `support` und `agent`.

Wenn kein Profil klar anwendbar ist, verwenden Sie die Basis von STG-DE. Erfinden Sie kein Profil.

## Anwendbarkeit

`primary_rules` nennt die Regeln, die in einem Profil besondere Aufmerksamkeit verdienen. `primary_rules` deaktiviert die anderen Regeln von STG-DE nicht.

Ein Profil kann eine strukturelle Grenze explizit festlegen. Ein Profil kann aber keine sicherheitsrelevante oder rechtliche Bedeutung abschwächen. Ein Profil kann keine kontrollierte lexikalische Bedeutung ändern.

## CLI

```bash
python tools/stg_lint.py instructions.md --profile procedure
python tools/stg_lint.py warning.md --profile safety --format json
python tools/stg_lint.py prompt.md --profile agent --format json
```

Die ältere Option `--text-type` ist als explizite strukturelle Überschreibung verfügbar. Wenn der Wert `auto` ist, liefert das ausgewählte Profil den strukturellen Typ.
