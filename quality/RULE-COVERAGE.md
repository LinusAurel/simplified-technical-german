# Automatisierungsabdeckung der STG-DE-Regeln

Dieses Dokument beschreibt, was der mitgelieferte Validator heute nachweisen kann. Das Dokument ist absichtlich konservativ.

Eine Regel kann Teil des STG-DE-Standards sein, auch wenn der derzeitige Validator sie nicht automatisch erkennen kann.

## Erkennungsklassen

| Klasse | Bedeutung |
|---|---|
| `deterministic` | Der Validator kann die genannte Bedingung maschinell und mit hoher Konfidenz erkennen. |
| `partial` | Eine deterministische Teilmenge ist implementiert. Die vollständige Regel erfordert Kontext oder eine zusätzliche Analyse. |
| `heuristic` | Die Automatisierung kann Belege liefern. Ein Befund muss ein Review-Punkt bleiben. |
| `semantic` | Die korrekte Anwendung hängt hauptsächlich von der Bedeutung oder vom Kontext des Diskurses ab. |
| `human-review` | Für die Regel gibt es derzeit keine zuverlässige automatisierte Implementierung. |

## Implementierte Abdeckung

`quality/rule-coverage.yaml` ist die maßgebliche Liste. Diese Liste nennt für jede der 75 Regeln und Empfehlungen die Erkennungsklasse und den Stand der Implementierung. 19 Regeln haben eine implementierte Prüfung: 9 Regeln im Linter und 10 Regeln im Analyzer.

### Linter (`stg_de/stg_lint.py`)

| Regel | Derzeitige automatisierte Prüfung | Abdeckung | Schweregrad |
|---|---|---|---|
| `STG-1.1` | Findet Einträge aus `dictionary/prohibited-words.yaml` und gibt den konfigurierten Status zurück. | partial | error/review |
| `STG-DE-4.3` | Erkennt ein alleinstehendes `man` als unbestimmten technischen Akteur. | deterministic | error |
| `STG-5.1` | Zählt im Modus „procedure“ die Wörter und markiert Sätze mit mehr als 20 Wörtern. | deterministic | error |
| `STG-5.3` | Erkennt die formale Anrede („Sie“, „Ihnen“, „Ihr…“, „Prüfen Sie“) und die Anrede mit „du“ (Pronomen). Mit festgelegter `anrede` ist eine andere Form ein Fehler. Ohne Festlegung ergibt eine gemischte Anrede eine Warnung. Ein Imperativ mit „du“ ohne Pronomen und der Infinitivstil bleiben unerkannt. | partial | error/warning |
| `STG-6.3` | Zählt im Modus „description“ und im Standardmodus die Wörter und markiert Sätze mit mehr als 25 Wörtern. | deterministic | error |
| `STG-6.6` | Zählt die Sätze in beschreibenden Absätzen und markiert Absätze mit mehr als sechs Sätzen. | deterministic | error |
| `STG-8.1` | Markiert Semikolons in Prosazeilen. | partial | error |
| `STG-DE-8.1` | Erkennt eine konservative Menge bekannter mehrdeutiger Formen mit Schrägstrich, zum Beispiel `und/oder`. Geschützte URLs und Code sind ausgenommen. | partial | warning |
| `STG-9.4` | Setzt `preferred_terms` aus `.stg-de.yaml` durch. | partial | error |

Der Wortzähler für `STG-5.1` und `STG-6.3` zählt ein Bindestrichkompositum als ein Wort. Diese Zählung setzt `STG-8.7` um. `STG-8.7` hat keine eigene Prüfung und erzeugt keine eigenen Befunde. Aus diesem Grund hat `STG-8.7` in `quality/rule-coverage.yaml` den Wert `implemented: false`.

### Analyzer (`stg_de/stg_analyze.py`)

Der Analyzer gibt nur Belege für das Review zurück. Die Belege beschreibt `quality/GERMAN-ANALYSIS.md`.

| Regel | Beleg für das Review | Abdeckung |
|---|---|---|
| `STG-DE-2.1` | Kandidaten für sehr lange deutsche Komposita | heuristic |
| `STG-3.5` | Kandidaten für Nominalisierungen | heuristic |
| `STG-3.6` | mögliche Passivkonstruktionen | heuristic |
| `STG-DE-3.1` | lange Klammern durch trennbare Verben | heuristic |
| `STG-DE-3.2` | mehrdeutige Modalformen wie `sollte` und Beobachtungen zu `muss`, `darf` und `kann` | partial |
| `STG-DE-3.3` | restriktives Review von `werden` | heuristic |
| `STG-DE-4.1` | mehrere oder lange Marker für Nebensätze | heuristic |
| `STG-DE-4.2` | mögliche mehrdeutige Pronomenbezüge | partial |
| `STG-DE-4.4` | Geltungsbereich von Negation oder Fokus | partial |
| `STG-DE-4.5` | Pronominaladverbien | partial |

Mit der Option `--lexicon-report` meldet der Validator auch Oberflächenformen, die das zentrale Lexikon nicht kennt. Unbekannte Wörter sind Kandidaten für ein Review und keine automatischen Verstöße.

### Verarbeitung der Eingabe

Der Linter und der Analyzer segmentieren Markdown, bevor sie Sätze zählen (`stg_de/stg_markdown.py`):

- Die Werkzeuge ignorieren Codeblöcke, HTML-Kommentare und YAML-Frontmatter.
- Die Werkzeuge ignorieren Bereiche zwischen `<!-- stg-lint: off -->` und `<!-- stg-lint: on -->`. Verwenden Sie diese Markierungen nur für absichtlich nicht konforme Beispiele.
- Überschriften, Listenelemente und Tabellenzellen sind getrennte Blöcke. Ein Satz geht deshalb nie über eine Markdown-Struktur hinaus.
- Inline-Code, URLs und zitierter Text (`„…“`, `»…«`, `"…"`) sind vor lexikalischen Prüfungen geschützt und zählen als ein Wort (`STG-8.6`).

## Gemessene Präzision

`corpus/HOLDOUT-PRECISION.md` dokumentiert die Präzision des Linters auf dem Holdout des Korpus. Für Linter 0.3.0 gilt ohne Extraktionsfehler: 92,9 % insgesamt, 100 % für `STG-1.1` und 72,7 % für `STG-6.3`. Auf extrahierten PDF- und HTML-Texten sind die meisten Befunde zu `STG-6.3` und `STG-6.6` Artefakte der Extraktion.

## Bedeutungserhaltung

`stg_de/stg_compare.py` vergleicht einen Quelltext mit seiner Umformulierung. Das Werkzeug ist keine Konformitätsprüfung und meldet keine Verstöße im Zieltext.

| Signal | Ergebnis bei Änderung | Zugehörige Regel |
|---|---|---|
| Zahlen, Einheiten | `FAIL` (verloren), `REVIEW` (hinzugefügt) | `STG-8.6` |
| Code, URLs, zitierte UI-Texte, Kennungen | `FAIL` | `STG-1.8` |
| Signalwörter für Sicherheit | `FAIL` | `STG-7.1` |
| Verbote, Verhältnis von Anforderung, Empfehlung und Möglichkeit | `REVIEW` | `STG-DE-3.2` |
| Negationen, Einschränkungen | `REVIEW` | `STG-DE-4.4` |
| Bedingungen | `REVIEW` | `STG-5.4` |
| Grenzwerte und Näherungen | `REVIEW` | `STG-DE-9.2` |

Die Zählungen gelten für das ganze Dokument. Eine verschobene Negation oder Bedingung kann ihre Anzahl behalten und trotzdem den Geltungsbereich ändern. Ein `PASS` beweist deshalb nie eine gleiche Bedeutung.

## Testrichtlinie

Jeder implementierte Pfad des Validators muss eine Abdeckung durch Regressionstests haben. Die Suite muss diese Elemente enthalten, wenn zutreffend:

1. ein Beispiel mit Verstoß,
2. ein Beispiel ohne Verstoß,
3. die erwartete veröffentlichte Regel-ID,
4. den erwarteten Schweregrad oder das erwartete Ergebnis,
5. einen Schutz gegen falsch positive Befunde,
6. eine globale Prüfung, dass jede ausgegebene Regel-ID in `rules/rule-index.yaml` existiert.

Die derzeitige Suite enthält ausdrückliche Schutztests gegen falsch positive Befunde. Diese Tests betreffen `man` gegenüber `Mann`, URLs gegenüber Schrägstrichformen, Absatzgrenzen und konforme Satzlängen.

## Regeln ohne maschinellen Nachweis

### Vokabular und Terminologie

Die meisten Regeln von `STG-1.2` bis `STG-1.14`, `STG-2.1`, `STG-2.2` und `STG-DE-2.1` bis `STG-DE-2.3` benötigen zusätzliche Analysen. Diese Analysen umfassen Morphologie, Wortartanalyse, Analyse von Komposita, Verfolgung von Abkürzungen und Terminologiestatus auf Dokumentebene.

### Verben und Modalität

`STG-3.1` bis `STG-3.7` und `STG-DE-3.1` bis `STG-DE-3.3` erfordern zusätzliche Analysen. Für `STG-3.5`, `STG-3.6` und `STG-DE-3.1` bis `STG-DE-3.3` liefert der Analyzer nur Belege für das Review. Diese Analysen umfassen die Analyse von Verbformen, die Erkennung von Passiv, der Abstand bei trennbaren Verben, die Klassifizierung von Modalverben und die Erkennung von Nominalstil. Wir empfehlen, diese Regeln nicht zu deterministischen Fehlern hochzustufen, bis die gemessene Präzision akzeptabel ist.

### Satzstruktur

Der größte Teil von Abschnitt 4 bleibt semantisch oder benötigt einen Parser. `STG-DE-4.3` ist die deterministische Ausnahme. Für `STG-DE-4.1`, `STG-DE-4.2`, `STG-DE-4.4` und `STG-DE-4.5` liefert der Analyzer nur Belege für das Review. Zukünftige Arbeit umfasst die Tiefe von Nebensätzen, das Review von Pronomenbezügen, den Geltungsbereich von Negationen und das Review von Pronominaladverbien.

### Anleitungen

`STG-5.1` ist deterministisch. `STG-5.2` bis `STG-5.5` erfordern eine Analyse von Anweisungsstruktur, Bedingungen und Modalität.

### Beschreibungen

`STG-6.3` und `STG-6.6` sind deterministisch. `STG-6.1`, `STG-6.2`, `STG-6.4` und `STG-6.5` sind Regeln auf Ebene des Diskurses.

### Sicherheit

`STG-7.1` bis `STG-7.3` erfordern eine ausdrückliche Sicherheitsstruktur oder eine semantische Analyse mit hoher Konfidenz. Ohne diese Voraussetzungen ist eine strikte Automatisierung nicht zuverlässig.

### Zeichensetzung und Zählung

`STG-8.1` unterstützt Semikolons teilweise. `STG-DE-8.1` unterstützt Schrägstrichmuster konservativ. Die restlichen Regeln von Abschnitt 8 benötigen eine strukturierte Verarbeitung von Listen und Klammern. Sie benötigen auch eine exaktere Zählung geschützter Token.

### Schreibpraxis und Empfehlungen

`STG-9.4` unterstützt Projektterminologie teilweise. Viele Füllwörter und vage Ausdrücke erkennt der Validator indirekt über `STG-1.1`. Wir empfehlen, die restlichen Regeln und Empfehlungen auf das Review auszurichten, bis ihre Semantik messbar ist.

## Qualitätsregel

Eine Funktion des Validators darf eine Regel-ID nur ausgeben, wenn diese ID in `rules/rule-index.yaml` existiert.

Wir empfehlen, keine Funktion des Validators nur deshalb als `deterministic` zu kennzeichnen, weil sie einen regulären Ausdruck verwendet. Die Klassifizierung bedeutet: Die implementierte Teilmenge hat eine klare, maschinell testbare Bedingung mit absichtlich begrenztem Geltungsbereich.

## Abnahmeziel vor 1.0

STG-DE fordert vor 1.0 keine automatische Durchsetzung aller 75 Regeln und Empfehlungen. STG-DE fordert diese Punkte:

- ein vollständiges Inventar der Automatisierung,
- Regressionstests für jede implementierte Prüfung,
- keine ungültigen Regel-IDs,
- eine klare Trennung von Fehlern, Warnungen, Review-Punkten und ungelösten semantischen Fällen,
- zusätzliche deterministische Prüfungen mit geringem Risiko nur dann, wenn das Risiko falsch positiver Befunde begrenzt ist,
- eine gemessene Evaluation mit einem Holdout-Korpus, bevor Prüfungen mit Parser- oder LLM-Unterstützung hochgestuft werden.
