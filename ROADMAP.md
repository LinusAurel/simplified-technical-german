# STG-DE-Roadmap

Diese Roadmap beschreibt den Weg vom aktuellen experimentellen Release (0.3.0) zu einem stabilen STG-DE 1.0. Prioritäten können sich ändern. Das gilt, wenn Belege aus dem Korpus, Rückmeldungen von Benutzern oder Befunde aus der Implementierung eine andere Reihenfolge als nützlicher zeigen.

## Leitprinzipien

1. Halten Sie den Sprachstandard unabhängig vom Agent Skill und von den Werkzeugen der Implementierung.
2. Halten Sie Regel-IDs nach der Veröffentlichung stabil, außer wenn eine Korrektur unvermeidbar ist.
3. Trennen Sie deterministische Verstöße von heuristischen oder semantischen Befunden für das Review.
4. Fügen Sie zentrales Vokabular nur hinzu, wenn Belege eine domänenübergreifende Verwendung stützen.
5. Halten Sie Domänenterminologie in Projektwörterbüchern, statt den Kern ohne Notwendigkeit zu erweitern.
6. Erhalten Sie bei Umformulierungen Bedeutung, Modalität, Sicherheitsbedingungen, Zahlen und Geltungsbereich.
7. Validieren Sie Änderungen mit maschinellen Tests und mit echtem deutschem Text.

## Rückverfolgbarkeit der Quellen (0.2.0)

- [x] Alle 53 Schreibregeln und 8 allgemeinen Empfehlungen aus ASD-STE100 Issue 9 auf STG-DE abbilden (`mapping/ste100-issue9.yaml`).
- [x] Sicherstellen, dass jede STG-DE-Regel rückverfolgbar ist und jedes Ziel der Abbildung existiert.
- [x] Die Grenze des Urheberrechts von ASD-STE100 dokumentieren (`NOTICE.md`).
- [x] Die Dokumentation des Repositorys auf Deutsch schreiben. Die Dokumentation folgt selbst STG-DE.

## v0.2 — Belege und Zuverlässigkeit

### Qualität von Regeln und Validator

- [x] Eine Matrix von Regeln zu Tests für alle veröffentlichten STG-DE-Regeln erstellen.
- [x] Für jede deterministisch testbare Regel mindestens einen positiven und einen negativen Fall hinzufügen.
- [x] Prüfen, dass jeder Befund des Validators eine vorhandene Regel-ID referenziert.
- [x] Regressionstests für die Stabilität der Regel-IDs hinzufügen.
- [x] Golden-Audit-Fixtures mit erwarteten Befund-IDs, Schweregraden und Ausgabestatus hinzufügen.
- [x] Dokumentieren, welche Regeln deterministisch, heuristisch, semantisch oder nur durch Menschen prüfbar sind.
- [x] Die Tests von der minimalen Menge zu einer aussagekräftigen Konformitätssuite erweitern.
- [x] Markdown-Struktur in Linter und Analyzer erkennen (Codeblöcke, Überschriften, Listen, Tabellen).
- [x] Zitierten Text vor lexikalischen Prüfungen schützen (STG-8.6).

### Korpusmethodik

- [x] Entwicklungs-, Validierungs- und Holdout-Partitionen für das Korpus definieren.
- [x] Von kurzen Belegproben zu einem größeren öffentlichen deutschen Korpus erweitern (139.646 Token, 13 Volltextquellen).
- [x] Für die erste größere Evaluation mindestens 100.000 Token erreichen.
- [ ] Mehr als 500.000 Token mit einem Partitionsdesign erreichen, das nach Token ausgewogen ist.
- [x] Über technische Handbücher hinaus auf Texte aus öffentlicher Verwaltung, Software, Energie, Logistik und Telekommunikation erweitern.
- [x] Exakte Dokument-URLs, Hashes und Stichprobenmethoden speichern.
- [x] Die Abdeckung je Domäne und die Verteilung unbekannter Token verfolgen.
- [ ] Falsch positive und falsch negative Befunde mit einem manuell geprüften Holdout-Set messen.
- [x] Quelltexte von Dritten aus dem Repository fernhalten.

### Grundlage der Wörterbuch-Governance

- [x] Anforderungen an Belege für einen neuen lexikalischen Kerneintrag definieren.
- [x] Ein maschinenlesbares Format für lexikalische Vorschläge hinzufügen.
- [x] Geprüfte Alternativen, Risiko der Mehrdeutigkeit, Korpusbelege und Begründung der Entscheidung dokumentieren.
- [x] In den Hinweisen für Beiträge Kernvokabular von Projekt- und Domänenterminologie unterscheiden.

### Abschlusskriterien für v0.2

- [x] Deterministische Regel-IDs sind intern konsistent und durch Regressionstests geprüft.
- [x] Die Matrix für die Regelabdeckung ist veröffentlicht.
- [x] Eine größere, reproduzierbare Korpusmethodik existiert.
- [x] Die Holdout-Evaluation ist von der Wörterbuchentwicklung getrennt.
- [x] Bekannte Einschränkungen des Validators sind ausdrücklich klassifiziert.

## v0.3 — Engine für die deutsche Sprache

**Ziel:** Die Analyse deutscher Morphologie und Syntax verbessern. Unsichere NLP-Ergebnisse dürfen nicht zu falscher Sicherheit werden.

- [ ] Eine robuste deutsche Lemmatisierung hinzufügen.
- [ ] Die Behandlung der Flexion und die Erkennung von Kollisionen über die kuratierte Kollisionsliste hinaus verbessern.
- [ ] Eine Analyse von Komposita und ein Routing für Terminologie hinzufügen.
- [ ] POS-Tagging hinzufügen, wenn es die Prüfungen der kontrollierten Bedeutung verbessert.
- [x] Die Tiefe von Nebensätzen und lange Satzklammern erkennen (heuristisch, `stg_analyze.py`).
- [x] Kandidaten für Passiv erkennen, auch Konstruktionen mit `werden` (heuristisch).
- [x] Wahrscheinlichen Nominalstil erkennen (heuristisch).
- [x] Heuristische Prüfungen der Bezüge von Pronomen und Pronominaladverbien hinzufügen.
- [x] Review-Prüfungen für Modalität und für den Geltungsbereich von Negationen hinzufügen.
- [x] Ausdrückliche Konfidenzstufen für Befunde aus NLP einführen.
- [ ] Die Präzision des Analyzers mit dem Holdout-Set messen, bevor eine Prüfung zur deterministischen Prüfung hochgestuft wird.

## v0.4 — Anwendungsprofile

- [x] Formales Profilschema.
- [x] Matrix der Anwendbarkeit von Regeln je Profil.
- [x] Profilabhängiges Verhalten von CLI und Agent Skill.
- [x] Konformitätsbeispiele für jedes Profil (`evals/cases.yaml` deckt alle sieben ab).
- [x] Strikter und pragmatischer Skill-Modus, abgebildet auf `STG-T` und `STG-R`.
- [x] Anredeform je Projekt (`sie`, `du`, `infinitiv`) nach STG-2026-001, mit Prüfung im Linter und Verhalten im Skill.

## v0.5 — Werkzeug-Ökosystem

- [x] `stg_lint.py` für Dateien und Verzeichnisse, mit Zeilennummern und `--fail-on`.
- [x] Wiederverwendbare GitHub Action mit Annotationen in Pull Requests (`action.yml`).
- [x] Prüfung der Bedeutungserhaltung bei Umformulierungen (`stg_compare.py`).
- [x] Claude-Code-Plugin und Marketplace (`.claude-plugin/`).
- [x] Reproduzierbares Skill-ZIP mit Prüfsumme für claude.ai und andere Skill-Loader.
- [x] Kopiervorlagen für `AGENTS.md`, `CLAUDE.md` und System-Prompts (`prompts/agents-md.md`).
- [x] Python-Paket `stg-de` mit einer CLI `stg` (`lint`, `analyze`, `compare`).
- [x] pre-commit-Hook `stg-de-lint`.
- [x] Erste Vale-Regeln für deterministisch abbildbare Fälle (`STG-8.1`, `STG-DE-4.3`, `STG-DE-8.1`).
- [ ] Veröffentlichung des Pakets auf PyPI.
- [ ] Adapter für das Language Server Protocol und Diagnosen in VS Code.
- [ ] Optionaler MCP-Server für Integrationen in Editoren und Agenten.

Werkzeuge müssen die kanonischen Regel- und Wörterbuchdaten des Repositorys verwenden. Sie dürfen keine unabhängigen Kopien pflegen.

## Bereich Agent Skill

### Evaluationssuite

- [x] Evaluationssets für WRITE, REWRITE und AUDIT mit einem deterministischen Bewertungswerkzeug erstellen (`evals/`, `tools/run_evals.py`).
- [x] Anleitungen, Anforderungen, Support, Verbrauchertexte, Sicherheitstexte, Fehlermeldungen und Anweisungen für Agenten abdecken.
- [x] Regelkonformität, verlorene geschützte Inhalte, erfundene Zahlen, Änderungen der Modalität und Genauigkeit von Audits messen.
- [ ] Die Suite mit mehreren Modellen ausführen, mit und ohne Skill, und die Ergebnisse veröffentlichen.
- [ ] Messungen der Trigger-Genauigkeit für `evals/triggers.yaml` hinzufügen.
- [ ] Regressionsfälle für Fehler aus der realen Verwendung hinzufügen.

### Verhalten des Skills

- [x] Die Standardausgabe für WRITE und REWRITE auf den fertigen Text begrenzen.
- [x] Detaillierte Regelausgaben nur in AUDIT oder auf ausdrückliche Anforderung ausgeben.
- [x] Deterministische Ergebnisse des Validators verwenden, wenn Werkzeuge ausführbar sind.
- [x] Heuristische Befunde nie als stärkeren Beleg als die Bedeutung des Satzes bewerten.
- [x] Projektterminologie in allen Agentenumgebungen einheitlich unterstützen.

## v0.6 — Governance und Disziplin bei Releases

- [x] Vorlage für STG-Änderungsvorschläge hinzufügen.
- [x] Vorlage für lexikalische Vorschläge hinzufügen.
- [x] Richtlinie für Regeländerungen und Abkündigungen definieren.
- [x] Richtlinie für semantische Versionierung von Spezifikation, Wörterbuch, Validator und Skill definieren.
- [x] Erwartungen an Maintainer und Reviews definieren.
- [x] `CITATION.cff` hinzufügen.
- [x] Release-Artefakte veröffentlichen, die mit Prüfsummen überprüfbar sind (Release-Workflow).
- [x] Eine dokumentierte Release-Checkliste erstellen.

## v1.0 — Stabile kontrollierte Sprache

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

## Reihenfolge der nächsten Schritte

1. Führen Sie `tools/run_evals.py` mit mindestens zwei Modellen aus, mit und ohne Skill. Veröffentlichen Sie die Ergebnisse.
2. Prüfen Sie manuell eine Holdout-Stichprobe. Veröffentlichen Sie die Präzision von Linter und Analyzer.
3. Veröffentlichen Sie das Paket `stg-de` auf PyPI.
4. Erweitern Sie das Korpus in Richtung 500.000 Token mit ausgewogenen Partitionen.
5. Fügen Sie Lemmatisierung und Analyse von Komposita hinzu, innerhalb der Grenze „nur Review“.
