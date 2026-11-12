# STG-DE-Roadmap

Diese Roadmap nennt nur offene Arbeit. Was erledigt ist, steht in [`CHANGELOG.md`](CHANGELOG.md). Die Reihenfolge der Abschnitte ist die Priorität. Die Priorität kann sich ändern, wenn Belege aus dem Korpus, Rückmeldungen von Benutzern oder Befunde aus der Implementierung eine andere Reihenfolge zeigen.

## Leitprinzipien

1. Halten Sie den Sprachstandard unabhängig vom Agent Skill und von den Werkzeugen der Implementierung.
2. Halten Sie Regel-IDs nach der Veröffentlichung stabil, außer wenn eine Korrektur unvermeidbar ist.
3. Trennen Sie deterministische Verstöße von heuristischen oder semantischen Befunden für das Review.
4. Fügen Sie zentrales Vokabular nur hinzu, wenn Belege eine domänenübergreifende Verwendung stützen.
5. Halten Sie Domänenterminologie in Projektwörterbüchern, statt den Kern ohne Notwendigkeit zu erweitern.
6. Erhalten Sie bei Umformulierungen Bedeutung, Modalität, Sicherheitsbedingungen, Zahlen und Geltungsbereich.
7. Validieren Sie Änderungen mit maschinellen Tests und mit echtem deutschem Text.

Werkzeuge müssen die kanonischen Regel- und Wörterbuchdaten des Repositorys verwenden. Werkzeuge dürfen keine unabhängigen Kopien pflegen.

## Präzision des Linters

Grundlage ist die Messung in [`corpus/HOLDOUT-PRECISION.md`](corpus/HOLDOUT-PRECISION.md).

- [ ] `STG-8.1`: Semikolons in Listen von Namen und Normen nicht melden. Auf dem Holdout sind 10 von 12 Befunden dieser Art falsch.
- [ ] `STG-6.3`: Marken in Fettschrift am Satzanfang nicht mitzählen. `z.B.` ohne Leerzeichen als Abkürzung erkennen.
- [ ] Extraktionsfehler bei Menüs, Tabellen und Seitenköpfen verringern. Diese Fehler verursachen fast die Hälfte der Befunde auf dem Holdout.
- [ ] Nach den Korrekturen mit neuen Holdout-Quellen erneut messen.

## Engine für die deutsche Sprache

Unsichere NLP-Ergebnisse dürfen nicht zu falscher Sicherheit werden.

- [ ] Eine robuste deutsche Lemmatisierung hinzufügen.
- [ ] Die Behandlung der Flexion und die Erkennung von Kollisionen über die kuratierte Kollisionsliste hinaus verbessern.
- [ ] Eine Analyse von Komposita und ein Routing für Terminologie hinzufügen.
- [ ] POS-Tagging hinzufügen, wenn es die Prüfungen der kontrollierten Bedeutung verbessert.
- [ ] Die Präzision des Analyzers auf dem Holdout messen, bevor eine Prüfung zur deterministischen Prüfung hochgestuft wird.

## Korpus

- [ ] Mehr als 500.000 Token mit einem Partitionsdesign erreichen, das nach Token ausgewogen ist.

## Agent Skill

- [ ] Die Trigger-Genauigkeit für `evals/triggers.yaml` messen.
- [ ] Für jeden Fehler aus der realen Verwendung einen Regressionsfall hinzufügen.
- [ ] Die Evaluation nach jeder Änderung am Skill wiederholen und in [`evals/results/`](evals/results/) veröffentlichen.

## Integrationen

- [ ] Adapter für das Language Server Protocol und Diagnosen in VS Code.
- [ ] Optionaler MCP-Server für Integrationen in Editoren und Agenten.

## Kriterien für 1.0

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
