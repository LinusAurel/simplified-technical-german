# Evaluation des STG-DE-Skills

Dieses Verzeichnis misst, wie gut ein Agent STG-DE mit dem mitgelieferten Skill anwendet.

| Datei | Zweck |
|---|---|
| `cases.yaml` | 12 Fälle für WRITE, REWRITE und AUDIT in allen sieben Profilen, mit maschinell prüfbaren Erwartungen. |
| `triggers.yaml` | Anfragen, bei denen der Agent den Skill laden soll, und Anfragen, bei denen der Agent den Skill nicht laden soll. Prüfen Sie mit diesen Anfragen die `description` des Skills. |
| `reference/` | Referenzausgaben. Die Referenzausgaben bestehen jede Prüfung und belegen, dass das Bewertungswerkzeug funktioniert. |

## Was die Evaluation misst

Alle Prüfungen sind deterministisch:

- **Einhaltung der Regeln:** keine deterministischen Fehler des Linters in der Ausgabe von WRITE und REWRITE, mit dem Profil des Falls.
- **Treue:** `stg_compare.py` darf keinen verlorenen geschützten Inhalt melden (Zahlen, Einheiten, Bezeichner, Code, URLs, zitierte UI-Texte, Signalwörter für Sicherheit).
- **Fakten:** Erforderliche Zeichenketten sind vorhanden. Verbotene Zeichenketten fehlen.
- **Ausgabedisziplin:** keine Einleitung. Eine `Hinweis:`-Zeile, wenn der Ausgangstext ohne neue Fakten nicht konform werden kann. Konforme Eingabe bleibt unverändert.
- **Genauigkeit des Audits:** Das Audit nennt die erwarteten Regel-IDs und die korrekte `Ergebnis:`-Zeile.

Die Prüfungen beweisen nicht, dass die Bedeutung erhalten bleibt. Prüfen Sie die `REVIEW`-Befunde von `stg_compare.py` und eine Stichprobe der Ausgaben manuell.

## Ausführen

Bewerten Sie die Referenzausgaben:

```bash
python tools/run_evals.py --outputs evals/reference
```

Erzeugen und bewerten Sie Ausgaben mit einer beliebigen CLI, die einen Prompt von stdin liest:

```bash
python tools/run_evals.py --outputs runs/claude --command "claude -p"
```

Vergleichen Sie Durchläufe mit installiertem Skill und ohne installierten Skill. Vergleichen Sie Durchläufe auch zwischen verschiedenen Modellen. Speichern Sie die Ausgaben der Durchläufe außerhalb des Repositorys oder in einem datierten Verzeichnis. Fügen Sie für jeden Fehler aus der realen Verwendung einen Fall zu `cases.yaml` hinzu.
