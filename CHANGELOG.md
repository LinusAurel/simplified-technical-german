# Änderungsprotokoll

## Unveröffentlicht

### Modalität von Empfehlungen (STG-2026-002)

- `STG-GR-5` bleibt eine Empfehlung. Der Text verwendet jetzt den Imperativ statt „dürfen nicht“.
- `STG-DE-4.5`: Ein Validator muss ein Pronominaladverb mit ungeklärtem Bezug zur Prüfung melden. Vorher war diese Meldung eine Empfehlung.
- Spezifikation Abschnitt 10: Veröffentlichte Regel-IDs müssen auch vor 1.0 stabil bleiben. Ein Satz mit „Wir empfehlen“ ist auch in einer Pflichtregel eine Empfehlung.
- `dictionary/README.md` nennt jetzt dieselbe Reihenfolge der Auflösung wie `dictionary/MORPHOLOGY.md`: zuerst die Morphologie, danach die Sperrliste.
- `dictionary/DECISIONS.md` nennt den Autorenkern bis Version 0.1.

### Korpus: Branchen und Textsorten (Issue #18)

- 15 neue öffentliche Quellen in `corpus/v0.2-sources.yaml`. Die neuen Domänen sind Embedded und IoT, funktionale Sicherheit, Produktsicherheit, Messtechnik, IIoT und Energietechnik, Finanzen, B2B-Software und Texte für Agenten. Eine neue Quelle ist ein zweites Medizinprodukt. Neue Textsorten sind Release Notes, Anleitungen für Firmware-Updates, Anforderungsspezifikationen, FAQ für Hersteller und Anweisungen für Agenten.
- Das Korpus hat jetzt 359.075 Token aus 28 Quellen.
- Jede Quelle hat jetzt die Felder `text_type`, `organization`, `accessed_on` und `extraction_method`.
- Eine Obergrenze von 10.000 Token je Quelle gleicht die Kennzahlen aus (`capped_tokens`, `capped_coverage`). Die größte Quelle hat jetzt 9,4 % der begrenzten Token. Vorher hatte das Medizinhandbuch 59 % aller Token.
- Neue Holdout-Partition mit 7 Quellen. Die 4 Quellen der Messung für Linter 0.3.0 sind jetzt in der Entwicklungspartition (`previous_partition: holdout`, Protokoll Abschnitt 9).
- `build_corpus_v02.py` liest Textdateien auch in der Kodierung cp1252, meldet Kennzahlen je Textsorte und liest die Version aus `pyproject.toml`.

### Evaluation und Beispiele

- 7 neue Fälle in `evals/cases.yaml`. Die Fälle sind eine Anforderung nach dem Muster EARS, eine Sicherheitsanforderung mit SIL, Release Notes, eine Meldung einer Schwachstelle und eine Prüfanweisung. Dazu kommen eine Anleitung für ein Firmware-Update und ein Audit.
- Vier Beispiel-Glossare in `examples/glossaries/`: Embedded und IoT, funktionale Sicherheit, Produktsicherheit, Medizinprodukte.

### Werkzeug für die Präzisionsmessung (Issue #19)

- Fehler korrigiert: Die Stichprobe der Sätze ohne Befund konnte Sätze mit einem gemeldeten Wort enthalten. Der Linter meldet ein Wort aus der Sperrliste nur einmal je Dokument. Das Werkzeug prüft jetzt jeden Satz der Stichprobe einzeln.
- Die Bewertungsdatei enthält jetzt die Quellen mit Hash und die Version des Linters. `score` verwendet diese Quellen.
- Neue Bewertung `skip`: Ein Eintrag zählt dann nicht in den Kennzahlen.
- Neue Optionen `--sources` und `--prefill` für `sample`.

### Präzision auf dem Holdout (Issue #3)

- Neues Werkzeug `tools/holdout_precision.py`: Stichprobe von Befunden auf dem Holdout, Bewertung und Kennzahlen. Fremder Text bleibt außerhalb des Repositorys.
- Erste Messung für Linter 0.3.0 in `corpus/HOLDOUT-PRECISION.md` und `corpus/holdout-precision.yaml`: 92,9 % Präzision ohne Extraktionsfehler, 57 % der Befunde sind Extraktionsfehler. Ein Modell hat bewertet, ein Mensch hat die Bewertung noch nicht geprüft.

### Linter

- Befunde zu `STG-1.1` nennen jetzt den ersten Satz mit dem Wort und die Zahl der Sätze mit dem Wort (`occurrences`).
- `•`, `‣`, `◦`, `▪`, `▸`, `→` und `–` am Zeilenanfang gelten als Listenpunkte.
- Abkürzungen wie `bzw.`, `z. B.`, `ca.`, `Nr. 5`, `Abb. 3` und Datumsangaben wie `31. Dezember` beenden keinen Satz mehr. Linter und Analysewerkzeug verwenden dieselbe Satztrennung aus `stg_markdown.py`.
- Der Linter wertet das Feld `surface_forms` der Sperrliste aus. 20 gesperrte Adjektive haben gebeugte Formen erhalten, zum Beispiel `aktuellen` und `einfache`.

## 0.3.0 — 2026-11-12

Diese Version macht STG-DE in OpenAI Codex nutzbar und automatisiert Release und Aufräumen auf GitHub. Regeln, Wörterbuch und Werkzeuge bleiben inhaltlich gleich.

### OpenAI Codex

- Das Repository ist ein Codex-Plugin: `.codex-plugin/plugin.json` und der Marketplace `.agents/plugins/marketplace.json`.
- `agents/openai.yaml` folgt den Vorgaben von Codex: kurze Beschreibung mit 25 bis 64 Zeichen und ein Standard-Prompt mit `$simplified-technical-german`.
- `SKILL.md` nennt die Pfade der Skripte relativ zum Ordner des Skills. Codex führt Befehle im Projektverzeichnis aus.
- Das README beschreibt die Installation in Codex als Plugin, über `$skill-installer` und als Ordner in `.agents/skills/`.
- Tests prüfen Manifest, Marketplace und `agents/openai.yaml`.

### Automatisierung auf GitHub

- Der Workflow `Release` ist auch manuell startbar (`workflow_dispatch` mit `version`). Er erstellt dann den Tag auf `main` selbst. Die Notizen kommen aus dem Abschnitt der Version in `CHANGELOG.md`.
- Neuer Workflow `Clean up branches`: Er löscht den Branch eines gemergten Pull Requests automatisch. Ein manueller Start löscht alle Branches ohne eigene Commits außerhalb von `main`.

## 0.2.0 — 2026-11-12

Diese Version ist die erste Version, deren Werkzeuge und Agent Skill für den praktischen Einsatz vorgesehen sind. Die kontrollierten Bedeutungen im Wörterbuch bleiben gleich. Alle veröffentlichten Regel-IDs bleiben stabil.

### Anrede (STG-2026-001)

- `STG-5.3` erlaubt jetzt die Anredeformen `sie` (Standard), `du` und `infinitiv`. Ein Dokumentsatz verwendet genau eine Form. Die Einstellung `anrede` steht in `.stg-de.yaml`. Neuer Titel: „Anweisungen in einer festgelegten Anredeform“.
- `stg_lint.py` prüft `STG-5.3`: `error` bei einer anderen als der festgelegten Anrede, `warning` bei gemischter Anrede ohne Festlegung. Neue Option `--anrede`.
- Der Skill behält bei REWRITE die Anrede des Originals bei, wenn das Projekt keine Anrede festlegt.
- Neues Schema `schemas/project.schema.json` für `.stg-de.yaml`.

### Dokumentation auf Deutsch

- Die Prosa des Repositorys ist jetzt deutsch und folgt selbst STG-DE. Das README enthält einen kurzen Abschnitt auf Englisch.
- Die Markierungen `<!-- stg-lint: off -->` und `<!-- stg-lint: on -->` schließen absichtlich nicht konforme Beispiele von der Prüfung aus.

### Zuordnung zu ASD-STE100

- Neue Datei `mapping/ste100-issue9.yaml`: Alle 53 Schreibregeln und 8 Empfehlungen von ASD-STE100 Issue 9 sind STG-DE zugeordnet (35 gleich, 15 angepasst, 3 ersetzt). Jede STG-DE-Regel ist rückverfolgbar. Tests und `validate_release.py` prüfen die Vollständigkeit.
- Neue Datei `NOTICE.md`. Das Repository enthält keinen Regeltext, keine Beispiele und keine Wörterbucheinträge aus ASD-STE100.

### Werkzeuge

- `stg_lint.py` prüft mehrere Dateien und Verzeichnisse und gibt Zeilennummern aus. Neu sind `--fail-on {error,warning,review,never}`, `--format github` für Annotationen in Pull Requests und das automatische Laden von `./.stg-de.yaml` (`--no-project` schaltet das Laden ab).
- `stg_lint.py` und `stg_analyze.py` zerlegen Markdown korrekt in Blöcke (Codeblöcke, HTML-Kommentare, Überschriften, Listenpunkte, Tabellenzellen). Die gemeinsame Logik steht in `stg_markdown.py`. Vorher zählte eine ganze Markdown-Liste als ein Satz.
- `stg_lint.py` schützt zitierten Text vor lexikalischen Prüfungen. Zitierter Text zählt als ein Wort (`STG-8.6`).
- Korrekturen nach einem Test mit einem echten deutschen Monorepo: Befunde in Sätzen über mehrere Zeilen haben jetzt eine Zeilennummer. Technische Begriffe aus dem Projektglossar haben Vorrang vor der zentralen Sperrliste. Ein geändertes zitiertes Wort (`„Provision“` → `„Provisionen“`) ergibt jetzt `FAIL` in der Bedeutungsprüfung.
- Korrektur: Der Linter hat `man` zweimal gemeldet (`STG-DE-4.3` und `STG-1.1`). Jetzt meldet nur `STG-DE-4.3` das Wort.
- Neues Werkzeug `stg_compare.py` für die Bedeutungsprüfung von Umschreibungen. Fehlende Zahlen, Einheiten, Code, URLs, Zitate, Kennungen oder Signalwörter ergeben `FAIL`. Geänderte Verbote, Modalität, Verneinungen, Einschränkungen, Bedingungen und Grenzwerte ergeben `REVIEW`.

### Agent Skill

- Neue Modi `strikt` (`STG-T`) und `pragmatisch` (`STG-R`) mit Standardwerten je Anwendungsprofil.
- Neue Regeln für Texte, die Agenten lesen: Tool-Beschreibungen, Fehlermeldungen, Systemprompts.
- Der Skill führt nach jeder Umschreibung `stg_compare.py` aus. Konformer Text bleibt unverändert.
- Neue Beschreibung mit Auslösern auf Deutsch und Englisch und mit ausdrücklichen Ausschlüssen.
- Neue Datei `prompts/agents-md.md` mit einer kurzen und einer vollständigen Fassung für `AGENTS.md`, `CLAUDE.md`, `.cursorrules` und Systemprompts.

### Verpackung und CI

- Python-Paket `stg-de` mit dem Befehl `stg` und den Unterbefehlen `lint`, `analyze` und `compare` (aus dem früheren Branch `v0.5/tooling`). Das Paket enthält Kopien der kanonischen Werkzeuge und Daten. `tools/sync_package.py --check` prüft die Kopien.
- pre-commit-Hook `stg-de-lint` und erste Vale-Regeln in `vale/`.
- Plugin und Marketplace für Claude Code in `.claude-plugin/`.
- `tools/package_skill.py` erzeugt ein reproduzierbares ZIP des Skills mit SHA-256-Prüfsumme.
- Wiederverwendbare GitHub Action `action.yml` für STG-DE-Prüfungen in anderen Repositorys.
- Release-Workflow für Tags `v*`. Die CI erzeugt das ZIP und prüft das eigene Repository mit der Action.

### Evaluation

- `evals/`: Fälle für WRITE, REWRITE und AUDIT über alle sieben Anwendungsprofile, Prompts für die Auslöser und Referenzausgaben.
- `tools/run_evals.py`: deterministische Bewertung. Das Werkzeug erzeugt Ausgaben mit jedem CLI, das einen Prompt über stdin liest.

### Seit 0.1.0 (vorher nicht veröffentlicht)

- Matrix der automatisierten Regeln (`quality/rule-coverage.yaml`) und Golden-Audit-Fälle.
- Korpusprotokoll v0.2 mit festen Partitionen für Entwicklung, Validierung und Holdout. Das Korpus hat 139.646 Token aus 13 öffentlichen Volltextquellen (nur abgeleitete Metriken).
- Schema und Vorlage für Lexikonvorschläge, Vorlage für Änderungsvorschläge, Governance, Versionierungsrichtlinie, Release-Checkliste und `CITATION.cff`.
- Anwendungsprofile (`procedure`, `safety`, `description`, `requirement`, `support`, `consumer`, `agent`) in Linter und Skill.
- Konservatives Analysewerkzeug `stg_analyze.py` für die deutsche Sprache.

## 0.1.0 — 2026-08-22

Public repository release.

- Added a stratified public validation set with 18 German technical sources across six industries.
- Increased the central lexicon to 435 entries and 442 controlled meanings.
- Added collision-safe handling for German inflection, including the `Datum` / `Daten` case.
- Replaced capitalization-based technical-term assumptions with neutral noun-candidate routing.
- Added public per-source, per-industry, and incremental coverage metrics.
- Added a reusable Agent Skill for writing, rewriting, and auditing German text with STG-DE.
- Added a deterministic linter and project terminology configuration.
- Added repository CI and release/skill validation.

## 0.0.3

- Expanded the controlled core vocabulary and morphology model.
- Added corpus-driven lexical review and validator improvements.
- Added explicit handling for ambiguous pronominal adverbs and German contractions.

## 0.0.2

- Expanded the controlled dictionary and prohibited/review-required term list.
- Added morphology guidance, schemas, validator contracts, and conformance tests.

## 0.0.1

- Initial German controlled-language specification.
- Added the first STG-DE rule index and German-specific rules.
- Added German-specific rules for compounds, separable verbs, sentence brackets, modality, nominal style, pronouns, and negation.
