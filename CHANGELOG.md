# Änderungsprotokoll

## 0.5.0 — 2026-11-12

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

- Plugin und Marketplace für Claude Code in `.claude-plugin/`.
- `tools/package_skill.py` erzeugt ein reproduzierbares ZIP des Skills mit SHA-256-Prüfsumme.
- Wiederverwendbare GitHub Action `action.yml` für STG-DE-Prüfungen in anderen Repositorys.
- Release-Workflow für Tags `v*`. Die CI erzeugt das ZIP und prüft das eigene Repository mit der Action.

### Evaluation

- `evals/`: Fälle für WRITE, REWRITE und AUDIT über alle sieben Anwendungsprofile, Prompts für die Auslöser und Referenzausgaben.
- `tools/run_evals.py`: deterministische Bewertung. Das Werkzeug erzeugt Ausgaben mit jedem CLI, das einen Prompt über stdin liest.

### Seit 0.4.0 (vorher nicht veröffentlicht)

- Matrix der automatisierten Regeln (`quality/rule-coverage.yaml`) und Golden-Audit-Fälle.
- Korpusprotokoll v0.5 mit festen Partitionen für Entwicklung, Validierung und Holdout. Das Korpus hat 139.646 Token aus 13 öffentlichen Volltextquellen (nur abgeleitete Metriken).
- Schema und Vorlage für Lexikonvorschläge, Vorlage für Änderungsvorschläge, Governance, Versionierungsrichtlinie, Release-Checkliste und `CITATION.cff`.
- Anwendungsprofile (`procedure`, `safety`, `description`, `requirement`, `support`, `consumer`, `agent`) in Linter und Skill.
- Konservatives Analysewerkzeug `stg_analyze.py` für die deutsche Sprache.

## 0.4.0 — 2026-08-22

Public repository release.

- Added a stratified public validation set with 18 German technical sources across six industries.
- Increased the central lexicon to 435 entries and 442 controlled meanings.
- Added collision-safe handling for German inflection, including the `Datum` / `Daten` case.
- Replaced capitalization-based technical-term assumptions with neutral noun-candidate routing.
- Added public per-source, per-industry, and incremental coverage metrics.
- Added a reusable Agent Skill for writing, rewriting, and auditing German text with STG-DE.
- Added a deterministic linter and project terminology configuration.
- Added repository CI and release/skill validation.

## 0.3.0

- Expanded the controlled core vocabulary and morphology model.
- Added corpus-driven lexical review and validator improvements.
- Added explicit handling for ambiguous pronominal adverbs and German contractions.

## 0.2.0

- Expanded the controlled dictionary and prohibited/review-required term list.
- Added morphology guidance, schemas, validator contracts, and conformance tests.

## 0.1.0

- Initial German controlled-language specification.
- Added the first STG-DE rule index and German-specific rules.
- Added German-specific rules for compounds, separable verbs, sentence brackets, modality, nominal style, pronouns, and negation.
