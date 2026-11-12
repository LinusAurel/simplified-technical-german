# Vale-Regeln für STG-DE

Dieses Verzeichnis enthält eine kleine, konservative Auswahl von Regeln für [Vale](https://vale.sh). Verwenden Sie die Regeln in Editoren und in Pipelines für Dokumentation.

Die Vale-Regeln sind **kein** vollständiger STG-DE-Validator. Die Regeln decken nur Bedingungen ab, die das Mustermodell von Vale eindeutig abbilden kann.

| Vale-Regel | STG-DE-Regel | Stufe |
|---|---|---|
| `STG-DE.Semicolon` | `STG-8.1` | Fehler |
| `STG-DE.IndefiniteMan` | `STG-DE-4.3` | Fehler |
| `STG-DE.AmbiguousSlash` | `STG-DE-8.1` | Warnung für „und/oder“ und „oder/und“ |

Verwenden Sie `stg lint` für die kanonische deterministische Prüfung. Verwenden Sie `stg analyze` für heuristische Belege.

## Beispiel für `.vale.ini`

```ini
StylesPath = ./vale
MinAlertLevel = suggestion

[*.{md,txt,rst}]
BasedOnStyles = STG-DE
```

Kopieren Sie das Verzeichnis `STG-DE` in den `StylesPath` von Vale. Sie können `StylesPath` auch auf das Verzeichnis `vale/` dieses Repositorys setzen.

Fügen Sie hier keine breiten regulären Ausdrücke hinzu. Eine neue Regel braucht ein begrenztes Risiko für falsch positive Befunde und Tests gegen die Bedeutung der kanonischen Regel.
