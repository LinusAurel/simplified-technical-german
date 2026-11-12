# STG-DE — Vereinfachtes Technisches Deutsch (Simplified Technical German)

**STG-DE** ist eine offene Spezifikation einer kontrollierten Sprache für klares, einheitliches und maschinenlesbares Deutsch. STG-DE ist das deutsche Gegenstück zu [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org). Jede nummerierte STG-DE-Regel setzt die Absicht der ASD-STE100-Regel mit derselben Nummer aus Issue 9 um und passt sie an die deutsche Grammatik an.

<!-- stg-lint: off -->
## In English

STG-DE is an open controlled-language specification for clear, consistent, and machine-readable German. It is the German counterpart of ASD-STE100 Simplified Technical English. Every numbered STG-DE rule maps to the ASD-STE100 Issue 9 rule with the same number, adapted to German grammar. The repository works as a plugin for Claude Code and OpenAI Codex, as a standalone Agent Skill, and as a Python CLI (`stg`).
<!-- stg-lint: on -->

Verwenden Sie STG-DE für technische Dokumentation, Anleitungen, Sicherheitshinweise, Anforderungen, Support-Inhalte, UI-Texte und Fehlermeldungen. Verwenden Sie STG-DE auch für Texte, die KI-Agenten lesen: Prompts, Tool-Beschreibungen, `AGENTS.md` und Anweisungen zwischen Agenten.

Das Repository enthält einen **Sprachstandard**, ein **kontrolliertes Wörterbuch**, **deterministische Werkzeuge** und einen **Agent Skill**.

> Release: **0.4.0** — experimenteller Standard, verwendbare Werkzeuge. Die Regel-IDs sind stabil. Das zentrale Wörterbuch und das heuristische Analysewerkzeug sind noch in der Validierung.

## Schnellstart

### Claude Code (Plugin)

```bash
claude plugin marketplace add LinusAurel/simplified-technical-german
```

```bash
claude plugin install simplified-technical-german@stg-de
```

In einer Sitzung verwenden Sie `/plugin marketplace add LinusAurel/simplified-technical-german` und `/plugin install simplified-technical-german@stg-de`. Schreiben Sie danach zum Beispiel: *„Schreib diese Anleitung in STG-DE um.“*

### OpenAI Codex (Plugin)

Das Repository ist auch ein Codex-Plugin. Codex liest `.codex-plugin/plugin.json` und den Marketplace in `.agents/plugins/marketplace.json`. Fügen Sie den Marketplace hinzu:

```bash
codex plugin marketplace add LinusAurel/simplified-technical-german
```

Installieren Sie danach das Plugin `simplified-technical-german` im Plugin-Verzeichnis von Codex (`/plugins`). Codex unterstützt Plugins ab Version 0.117.

### OpenAI Codex (nur Skill)

Installieren Sie nur den Skill mit dem Skill-Installer von Codex:

```text
$skill-installer install https://github.com/LinusAurel/simplified-technical-german/tree/main/skills/simplified-technical-german
```

Starten Sie Codex danach neu. Rufen Sie den Skill mit `$simplified-technical-german` auf, zum Beispiel: *„$simplified-technical-german Schreib diese Anleitung in STG-DE um.“* Codex wählt den Skill auch ohne Aufruf, wenn die Anfrage zur Beschreibung des Skills passt.

### claude.ai, Claude Desktop und andere Skill-Loader

Laden Sie `simplified-technical-german-<version>.zip` aus den [Releases](https://github.com/LinusAurel/simplified-technical-german/releases) herunter. Laden Sie die Datei unter *Settings → Capabilities → Skills* hoch. Sie können die Datei auch selbst erstellen:

```bash
python tools/package_skill.py
```

### Den Skill-Ordner kopieren

Kopieren Sie `skills/simplified-technical-german/` in das Skill-Verzeichnis Ihres Agenten:

| Agent | Verzeichnis für alle Projekte | Verzeichnis für ein Repository |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| OpenAI Codex | `~/.agents/skills/` | `.agents/skills/` |
 Der Ordner ist eigenständig: `SKILL.md`, Referenzen und Skripte. 
Werkzeuge mit Unterstützung für die [`skills` CLI](https://skills.sh) können auch `npx skills add LinusAurel/simplified-technical-german` ausführen. Die Tests des Repositorys prüfen diesen Weg nicht.

### Werkzeuge ohne Skill-Unterstützung

Fügen Sie einen Textbaustein aus [`prompts/agents-md.md`](prompts/agents-md.md) in `AGENTS.md`, `CLAUDE.md`, `.cursorrules` oder einen System-Prompt ein. Die kurze Version hat sechs Regeln. Die vollständige Version behandelt Anleitungen, Beschreibungen, Wörter, Modalität, Zeichensetzung, geschützte Inhalte und Fehlermeldungen.

### GitHub Action

Die Action prüft deutsches Markdown in Pull Requests und zeigt Annotationen direkt im Code:

```yaml
- uses: actions/checkout@v4
- uses: LinusAurel/simplified-technical-german@v0.4.0
  with:
    paths: docs
    profile: procedure   # optional
    fail-on: error       # error | warning | review | never
```

### Kommandozeile `stg`

Installieren Sie das Paket `stg-de` direkt aus dem Repository:

```bash
python -m pip install "git+https://github.com/LinusAurel/simplified-technical-german@v0.4.0"
```

Der Befehl `stg` enthält drei Unterbefehle. Die Unterbefehle verwenden dieselben Werkzeuge wie der Skill und die Action.

| Befehl | Funktion |
|---|---|
| `stg lint docs/ --profile procedure` | deterministische Prüfung |
| `stg analyze text.md` | heuristische Belege für die Prüfung |
| `stg compare original.md umschreibung.md` | Bedeutungsprüfung einer Umschreibung |

### pre-commit

Tragen Sie den Hook in `.pre-commit-config.yaml` ein:

```yaml
repos:
  - repo: https://github.com/LinusAurel/simplified-technical-german
    rev: v0.4.0
    hooks:
      - id: stg-de-lint
```

Der Hook prüft geänderte Markdown- und Textdateien und bricht bei Fehlern ab.

## Inhalt

- **75 Regeln und Empfehlungen** für kontrolliertes Schreiben auf Deutsch, in `rules/`.
- **Rückverfolgbarkeit zu ASD-STE100 Issue 9:** alle 53 Schreibregeln und 8 allgemeinen Empfehlungen, in [`mapping/`](mapping/README.md).
- **435** zentrale lexikalische Einträge mit **442** kontrollierten Bedeutungen und **160** verbotene oder prüfpflichtige Wörter mit Hinweisen zur Umformulierung.
- Deutsche Morphologie und Behandlung von Verschmelzungen, Projektterminologie über `.stg-de.yaml`.
- Sieben **Anwendungsprofile**: `procedure`, `safety`, `description`, `requirement`, `support`, `consumer`, `agent`.
- **Werkzeuge:** deterministischer Linter, Analysewerkzeug für deutsche Texte und Bedeutungsprüfung.
- **Agent Skill** mit den Workflows `WRITE`, `REWRITE` und `AUDIT` und den Modi `strikt` und `pragmatisch`.
- **Evaluationssuite** für den Skill, mit einem deterministischen Bewertungswerkzeug.
- Öffentliche Korpusbelege: 359.075 Token aus 28 öffentlichen Volltextquellen in 16 Domänen, mit festen Partitionen für Entwicklung, Validierung und Holdout (nur Metadaten und abgeleitete Kennzahlen).

## Agent Skill

Der Skill akzeptiert beliebigen deutschen Text. Der Skill ist nicht auf Ingenieurwesen oder eine Branche begrenzt.

| Workflow | Ergebnis |
|---|---|
| `WRITE` | Neuer deutscher Text in STG-DE. |
| `REWRITE` | Vorhandener Text in STG-DE. Fakten, Zahlen, Modalität, Bedingungen und Fachbegriffe bleiben gleich. Konformer Text bleibt unverändert. |
| `AUDIT` | Eine Tabelle mit Befunden, Regel-IDs und Vorschlägen und `Ergebnis: PASS`, `PASS WITH REVIEW` oder `FAIL`. |

| Modus | Verwendung | Konformitätsziel |
|---|---|---|
| `strikt` | Anleitungen, Sicherheitshinweise, Anforderungen, Fehlermeldungen, Tool-Beschreibungen, Anweisungen für Agenten | `STG-T` |
| `pragmatisch` | Beschreibungen, Support, Verbrauchertexte, READMEs | `STG-R` |

WRITE und REWRITE geben nur den fertigen Text zurück. Wenn Code-Ausführung verfügbar ist, führt der Skill den Linter, das Analysewerkzeug und die Bedeutungsprüfung aus. Ohne Werkzeuge wendet der Skill die mitgelieferten Regeln und das Wörterbuch direkt an.

## Werkzeuge

Installieren Sie die Abhängigkeiten für die Entwicklung im Repository:

```bash
python -m pip install -r requirements-dev.txt
```

### Linter

Prüfen Sie Dateien und Verzeichnisse. Der Linter erkennt Markdown: Er ignoriert Codeblöcke und behandelt Listenpunkte und Tabellenzellen als eigene Sätze.

```bash
python stg_de/stg_lint.py docs/ README.de.md --profile procedure
```

JSON-Ausgabe aus stdin:

```bash
printf 'Prüfen Sie gegebenenfalls das Gerät.' | python stg_de/stg_lint.py - --format json
```

Einen CI-Schritt bei Fehlern scheitern lassen:

```bash
python stg_de/stg_lint.py docs/ --fail-on error
```

Der Linter lädt `./.stg-de.yaml` automatisch. Der Linter trennt deterministische Verstöße (`error`) von Kandidaten für eine Prüfung (`warning`, `review`). Ein unbekanntes Wort ist **nicht automatisch ein Fehler**. Ein großgeschriebenes deutsches Substantiv ist **nicht automatisch ein Fachbegriff**.

### Bedeutungsprüfung

Vergleichen Sie einen Ausgangstext mit seiner Umformulierung:

```bash
python stg_de/stg_compare.py original.md rewrite.md
```

Verlorene Zahlen, Einheiten, Bezeichner, Code, URLs, zitierte UI-Texte oder Signalwörter für Sicherheit ergeben `FAIL`. Geänderte Modalität, Verbote, Verneinungen, Bedingungen oder Grenzen ergeben `REVIEW`.

### Analysewerkzeug für deutsche Texte

```bash
python stg_de/stg_analyze.py input.md
```

Das Analysewerkzeug meldet Kandidaten für Passiv, Modalität, Satztiefe, Pronomen, Verneinung, Nominalstil und trennbare Verben. Jede Ausgabe des Analysewerkzeugs ist ein Beleg für eine Prüfung. Eine Ausgabe allein ist nie ein Verstoß.

## Evaluation

```bash
python tools/run_evals.py --outputs evals/reference
```

```bash
python tools/run_evals.py --outputs runs/claude --command "claude -p"
```

Die Suite prüft die Einhaltung der Regeln, verlorene geschützte Inhalte, erforderliche Fakten, Ausgabedisziplin und die Genauigkeit von Audits. Siehe [`evals/README.md`](evals/README.md).

## Projektterminologie

Fügen Sie nicht jeden Produktbegriff und jeden Branchenbegriff in das zentrale Wörterbuch ein. Fügen Sie präzise Fachterminologie in `.stg-de.yaml` ein (siehe `.stg-de.example.yaml`). Die Regeln für die Aufnahme in den zentralen Kern stehen in [`dictionary/GOVERNANCE.md`](dictionary/GOVERNANCE.md).

Beispiel-Glossare für Embedded und IoT, funktionale Sicherheit, Produktsicherheit und Medizinprodukte stehen in [`examples/glossaries/`](examples/glossaries/README.md).

## Konformitätsprofile

| Profil | Bedeutung |
|---|---|
| `STG-R` | Die anwendbaren Schreibregeln sind erfüllt. |
| `STG-T` | `STG-R` und die technische Projektterminologie ist aufgelöst. |
| `STG-C-core` | `STG-T` und alle anderen lexikalischen Einheiten gehören zum mitgelieferten zentralen Kern. |
| `STG-C` | Reserviert für ein breiteres, ausgereiftes und von Menschen geprüftes zentrales Lexikon. |

## Struktur des Repositorys

```text
.
├── specification.md              # normative Übersicht
├── rules/                        # normative Schreibregeln
├── dictionary/                   # kontrolliertes Lexikon und Terminologiemodell
├── mapping/                      # Zuordnung zu ASD-STE100 Issue 9
├── profiles/                     # Anwendungsprofile
├── schemas/                      # maschinenlesbare Schemas
├── examples/                     # Referenzaudits und Glossare
├── evals/                        # Evaluierung des Agent Skills
├── prompts/                      # Textbausteine für AGENTS.md und System-Prompts
├── proposals/                    # Änderungsvorschläge für Regeln (STG-YYYY-NNN)
├── corpus/                       # Metadaten und Kennzahlen des öffentlichen Korpus
├── quality/                      # Stand der Automatisierung der Regeln
├── tools/                        # Linter, Analysewerkzeug, Vergleich, Build- und Release-Werkzeuge
├── stg_de/                       # Python-Paket für die CLI stg (erzeugt von sync_package.py)
├── tests/                        # Unit- und Regressionstests
├── .claude-plugin/               # Plugin und Marketplace für Claude Code
├── .codex-plugin/                # Plugin für Codex
├── .agents/plugins/              # Marketplace für Codex
├── action.yml                    # wiederverwendbare GitHub Action
└── skills/simplified-technical-german/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/               # erzeugt aus den kanonischen Dateien
    └── scripts/                  # kopiert aus tools/
```

Die Spezifikation und das Wörterbuch auf der obersten Ebene sind die maßgebliche Quelle. Der Befehl `python tools/sync_skill.py` erzeugt die Referenzen und Skripte des Skills neu.

## Entwicklung

Die Befehle für die Prüfung vor einem Commit stehen in [`AGENTS.md`](AGENTS.md) im Abschnitt „Validierung“.

Für ein Release folgen Sie [`RELEASE-CHECKLIST.md`](RELEASE-CHECKLIST.md).

## Roadmap und Governance

- [`ROADMAP.md`](ROADMAP.md) — offene Arbeit und Kriterien für 1.0.
- [`GOVERNANCE.md`](GOVERNANCE.md) — Prozess für Entscheidungen und Prüfungen.
- [`VERSIONING.md`](VERSIONING.md) — Kompatibilität und semantische Versionierung.
- [`dictionary/GOVERNANCE.md`](dictionary/GOVERNANCE.md) — belegbasierte Änderungen am zentralen Lexikon.
- [`quality/RULE-COVERAGE.md`](quality/RULE-COVERAGE.md) — Stand der Automatisierung.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — Ablauf für Beiträge.

Beiträge von technischen Redakteuren, Linguisten, Ingenieuren, Support-Teams, Übersetzern, Terminologie-Fachleuten und Entwicklern von Agenten sind willkommen.

## Lizenz und Hinweis

MIT. Siehe [`LICENSE`](LICENSE).

ASD-STE100 ist ein Urheberrecht und eine Marke von ASD, Brüssel. STG-DE ist keine offizielle Veröffentlichung von ASD und enthält keinen Text aus ASD-STE100. Siehe [`NOTICE.md`](NOTICE.md).
