# STG-DE-Roadmap

Das derzeitige Release ist 0.6.0. Diese Roadmap zeigt die veröffentlichten Versionen, den Plan für die nächsten Releases und die Kriterien für 1.0. Prioritäten können sich ändern. Das gilt, wenn Belege aus dem Korpus, Rückmeldungen von Benutzern oder Befunde aus der Implementierung eine andere Reihenfolge als nützlicher zeigen.

## Versionen

| Version | Datum | Inhalt | Tag und Release |
|---|---|---|---|
| 0.1.0 bis 0.3.0 | vor 2026-08-22 | Entwurfsstände vor dem öffentlichen Repository | keine |
| 0.4.0 | 2026-08-22 | erster öffentlicher Stand: Spezifikation, Wörterbuch, Linter, Agent Skill | `v0.4.0`, nachträglich angelegt |
| 0.5.0 | 2026-11-12 | Korpusmethodik, Regelabdeckung, Profile, Analyzer, Werkzeuge, Paket, Evaluation | `v0.5.0` |
| 0.6.0 | 2026-11-12 | Plugin für OpenAI Codex, Automatisierung auf GitHub | `v0.6.0` |
| 0.7.0 | geplant | siehe [Nächstes Release](#nächstes-release-070) | — |

Die Änderungen jeder Version stehen in [`CHANGELOG.md`](CHANGELOG.md).

Frühere Fassungen dieser Roadmap hatten Abschnitte mit den Namen v0.6 bis v0.9. Diese Namen waren Arbeitsbereiche, keine Releases. Die meisten Punkte aus diesen Bereichen sind in 0.5.0 und 0.6.0 erschienen. Diese Roadmap ordnet erledigte Punkte deshalb nach Bereich. Versionsnummern stehen nur bei Releases.

## Leitprinzipien

1. Halten Sie den Sprachstandard unabhängig vom Agent Skill und von den Werkzeugen der Implementierung.
2. Halten Sie Regel-IDs nach der Veröffentlichung stabil, außer wenn eine Korrektur unvermeidbar ist.
3. Trennen Sie deterministische Verstöße von heuristischen oder semantischen Befunden für das Review.
4. Fügen Sie zentrales Vokabular nur hinzu, wenn Belege eine domänenübergreifende Verwendung stützen.
5. Halten Sie Domänenterminologie in Projektwörterbüchern, statt den Kern ohne Notwendigkeit zu erweitern.
6. Erhalten Sie bei Umformulierungen Bedeutung, Modalität, Sicherheitsbedingungen, Zahlen und Geltungsbereich.
7. Validieren Sie Änderungen mit maschinellen Tests und mit echtem deutschem Text.

## Nächstes Release (0.7.0)

Diese Punkte sind in `main` erledigt oder in Arbeit. Sie erscheinen mit 0.7.0.

- [x] Korpus auf Embedded und IoT, funktionale Sicherheit, Produktsicherheit, Messtechnik, Finanzen, B2B und Texte für Agenten erweitern (359.075 Token, 28 Quellen, Issue #18).
- [x] Eine Obergrenze an Token je Quelle festlegen (10.000 Token). Je Quelle Textsorte, Abrufdatum und Extraktionsmethode speichern.
- [x] Neue Holdout-Quellen festlegen. Die früheren Holdout-Quellen sind jetzt Entwicklungsquellen.
- [x] Modalität von Empfehlungen festlegen (STG-2026-002).
- [x] Evaluationsfälle und Projektglossare für Embedded, funktionale Sicherheit, Produktsicherheit und Medizintechnik hinzufügen.
- [x] Die Evaluationssuite mit zwei Modellen ausführen, mit und ohne Skill, und die Ergebnisse veröffentlichen ([`evals/results/`](evals/results/)).
- [x] Die Präzision des Linters auf den neuen Holdout-Quellen messen. Zwei Modelle bewerten jeden Befund unabhängig ([`corpus/HOLDOUT-PRECISION.md`](corpus/HOLDOUT-PRECISION.md)).
- [ ] Das Paket `stg-de` auf PyPI veröffentlichen. Der Release-Workflow enthält den Job. Das Konto auf PyPI ist noch nicht eingerichtet.

## Danach

### 0.8.0: Engine für die deutsche Sprache

**Ziel:** Die Analyse deutscher Morphologie und Syntax verbessern. Unsichere NLP-Ergebnisse dürfen nicht zu falscher Sicherheit werden.

- [ ] Eine robuste deutsche Lemmatisierung hinzufügen.
- [ ] Die Behandlung der Flexion und die Erkennung von Kollisionen über die kuratierte Kollisionsliste hinaus verbessern.
- [ ] Eine Analyse von Komposita und ein Routing für Terminologie hinzufügen.
- [ ] POS-Tagging hinzufügen, wenn es die Prüfungen der kontrollierten Bedeutung verbessert.
- [ ] Die Präzision des Analyzers mit dem Holdout-Set messen, bevor eine Prüfung zur deterministischen Prüfung hochgestuft wird.
- [ ] Extraktionsfehler bei Menüs, Tabellen und Seitenköpfen verringern. Diese Fehler verursachen die meisten falschen Befunde auf dem Holdout.
- [ ] `STG-8.1`: Semikolons in Listen von Namen und Normen nicht melden. Auf dem Holdout sind 10 von 12 Befunden dieser Art falsch.
- [ ] `STG-6.3`: Marken in Fettschrift am Satzanfang nicht mitzählen und `z.B.` ohne Leerzeichen als Abkürzung erkennen.

### 0.9.0: Integrationen und Messung

- [ ] Adapter für das Language Server Protocol und Diagnosen in VS Code.
- [ ] Optionaler MCP-Server für Integrationen in Editoren und Agenten.
- [ ] Messungen der Trigger-Genauigkeit für `evals/triggers.yaml` hinzufügen.
- [ ] Regressionsfälle für Fehler aus der realen Verwendung hinzufügen.
- [ ] Mehr als 500.000 Token mit einem Partitionsdesign erreichen, das nach Token ausgewogen ist.

Werkzeuge müssen die kanonischen Regel- und Wörterbuchdaten des Repositorys verwenden. Sie dürfen keine unabhängigen Kopien pflegen.

## 1.0: Stabile kontrollierte Sprache

STG-DE erreicht 1.0 durch Belege und Stabilität, nicht durch eine Zielgröße des Wörterbuchs.

- [ ] Regelsatz über mehrere Releases stabil.
- [ ] Veröffentlichte Regel-IDs als stabile öffentliche Kennungen behandelt.
- [ ] Großes unabhängiges Holdout-Korpus evaluiert.
- [ ] Akzeptable Rate falsch positiver Befunde für deterministische Prüfungen und NLP-Prüfungen dokumentiert.
- [ ] Breite Abdeckung der allgemeinen deutschen Funktions- und Handlungssprache.
- [ ] Domänenterminologie sauber vom Kern getrennt.
- [ ] Deterministisch testbare Regeln mit umfassender automatisierter Abdeckung.
- [ ] Agent Skill mit mehreren Modellen und Textdomänen evaluiert.
- [ ] Review durch Fachleute aus technischer Redaktion, Linguistik oder beiden Bereichen.
- [ ] Belege für eine reale Verwendung außerhalb des ursprünglichen Projekts.
- [ ] Governance und Änderungsprozess dokumentiert und aktiv.

## Erledigt

### Rückverfolgbarkeit der Quellen (0.5.0)

- [x] Alle 53 Schreibregeln und 8 allgemeinen Empfehlungen aus ASD-STE100 Issue 9 auf STG-DE abbilden (`mapping/ste100-issue9.yaml`).
- [x] Sicherstellen, dass jede STG-DE-Regel rückverfolgbar ist und jedes Ziel der Abbildung existiert.
- [x] Die Grenze des Urheberrechts von ASD-STE100 dokumentieren (`NOTICE.md`).
- [x] Die Dokumentation des Repositorys auf Deutsch schreiben. Die Dokumentation folgt selbst STG-DE.

### Qualität von Regeln und Validator (0.5.0)

- [x] Eine Matrix von Regeln zu Tests für alle veröffentlichten STG-DE-Regeln erstellen.
- [x] Für jede deterministisch testbare Regel mindestens einen positiven und einen negativen Fall hinzufügen.
- [x] Prüfen, dass jeder Befund des Validators eine vorhandene Regel-ID referenziert.
- [x] Regressionstests für die Stabilität der Regel-IDs hinzufügen.
- [x] Golden-Audit-Fixtures mit erwarteten Befund-IDs, Schweregraden und Ausgabestatus hinzufügen.
- [x] Dokumentieren, welche Regeln deterministisch, heuristisch, semantisch oder nur durch Menschen prüfbar sind.
- [x] Markdown-Struktur in Linter und Analyzer erkennen (Codeblöcke, Überschriften, Listen, Tabellen).
- [x] Zitierten Text vor lexikalischen Prüfungen schützen (STG-8.6).

### Korpusmethodik (0.5.0)

- [x] Entwicklungs-, Validierungs- und Holdout-Partitionen für das Korpus definieren.
- [x] Mindestens 100.000 Token aus öffentlichen Volltextquellen erreichen (139.646 Token, 13 Quellen).
- [x] Über technische Handbücher hinaus auf Texte aus öffentlicher Verwaltung, Software, Energie, Logistik und Telekommunikation erweitern.
- [x] Exakte Dokument-URLs, Hashes und Stichprobenmethoden speichern.
- [x] Die Abdeckung je Domäne und die Verteilung unbekannter Token verfolgen.
- [x] Erste Messung falsch positiver und falsch negativer Befunde auf dem Holdout (Linter 0.6.0, bewertet durch ein Modell).
- [x] Quelltexte von Dritten aus dem Repository fernhalten.

### Wörterbuch-Governance (0.5.0)

- [x] Anforderungen an Belege für einen neuen lexikalischen Kerneintrag definieren.
- [x] Ein maschinenlesbares Format für lexikalische Vorschläge hinzufügen.
- [x] Geprüfte Alternativen, Risiko der Mehrdeutigkeit, Korpusbelege und Begründung der Entscheidung dokumentieren.
- [x] In den Hinweisen für Beiträge Kernvokabular von Projekt- und Domänenterminologie unterscheiden.

### Analyzer (0.5.0)

- [x] Die Tiefe von Nebensätzen und lange Satzklammern erkennen (heuristisch, `stg_analyze.py`).
- [x] Kandidaten für Passiv erkennen, auch Konstruktionen mit `werden` (heuristisch).
- [x] Wahrscheinlichen Nominalstil erkennen (heuristisch).
- [x] Heuristische Prüfungen der Bezüge von Pronomen und Pronominaladverbien hinzufügen.
- [x] Review-Prüfungen für Modalität und für den Geltungsbereich von Negationen hinzufügen.
- [x] Ausdrückliche Konfidenzstufen für Befunde aus NLP einführen.

### Anwendungsprofile (0.5.0)

- [x] Formales Profilschema und Matrix der Anwendbarkeit von Regeln je Profil.
- [x] Profilabhängiges Verhalten von CLI und Agent Skill.
- [x] Konformitätsbeispiele für jedes Profil (`evals/cases.yaml` deckt alle sieben ab).
- [x] Strikter und pragmatischer Skill-Modus, abgebildet auf `STG-T` und `STG-R`.
- [x] Anredeform je Projekt (`sie`, `du`, `infinitiv`) nach STG-2026-001, mit Prüfung im Linter und Verhalten im Skill.

### Werkzeuge (0.5.0 und 0.6.0)

- [x] `stg_lint.py` für Dateien und Verzeichnisse, mit Zeilennummern und `--fail-on`.
- [x] Wiederverwendbare GitHub Action mit Annotationen in Pull Requests (`action.yml`).
- [x] Prüfung der Bedeutungserhaltung bei Umformulierungen (`stg_compare.py`).
- [x] Claude-Code-Plugin und Marketplace (`.claude-plugin/`).
- [x] Plugin für OpenAI Codex (0.6.0).
- [x] Reproduzierbares Skill-ZIP mit Prüfsumme für claude.ai und andere Skill-Loader.
- [x] Kopiervorlagen für `AGENTS.md`, `CLAUDE.md` und System-Prompts (`prompts/agents-md.md`).
- [x] Python-Paket `stg-de` mit einer CLI `stg` (`lint`, `analyze`, `compare`).
- [x] pre-commit-Hook `stg-de-lint`.
- [x] Erste Vale-Regeln für deterministisch abbildbare Fälle (`STG-8.1`, `STG-DE-4.3`, `STG-DE-8.1`).

### Agent Skill (0.5.0)

- [x] Evaluationssets für WRITE, REWRITE und AUDIT mit einem deterministischen Bewertungswerkzeug erstellen (`evals/`, `tools/run_evals.py`).
- [x] Anleitungen, Anforderungen, Support, Verbrauchertexte, Sicherheitstexte, Fehlermeldungen und Anweisungen für Agenten abdecken.
- [x] Regelkonformität, verlorene geschützte Inhalte, erfundene Zahlen, Änderungen der Modalität und Genauigkeit von Audits messen.
- [x] Die Standardausgabe für WRITE und REWRITE auf den fertigen Text begrenzen.
- [x] Detaillierte Regelausgaben nur in AUDIT oder auf ausdrückliche Anforderung ausgeben.
- [x] Deterministische Ergebnisse des Validators verwenden, wenn Werkzeuge ausführbar sind.
- [x] Heuristische Befunde nie als stärkeren Beleg als die Bedeutung des Satzes bewerten.
- [x] Projektterminologie in allen Agentenumgebungen einheitlich unterstützen.

### Governance und Releases (0.5.0)

- [x] Vorlagen für STG-Änderungsvorschläge und lexikalische Vorschläge hinzufügen.
- [x] Richtlinie für Regeländerungen und Abkündigungen definieren.
- [x] Richtlinie für semantische Versionierung von Spezifikation, Wörterbuch, Validator und Skill definieren.
- [x] Erwartungen an Maintainer und Reviews definieren.
- [x] `CITATION.cff` hinzufügen.
- [x] Release-Artefakte veröffentlichen, die mit Prüfsummen überprüfbar sind (Release-Workflow).
- [x] Eine dokumentierte Release-Checkliste erstellen.
