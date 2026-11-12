# STG-DE-Korpusprotokoll

Dieses Protokoll regelt die korpusbasierte Entwicklung ab v0.2. Das Ziel ist, Sprachmodell und Validator zu verbessern, ohne das zentrale Wörterbuch an eine kleine Menge von Dokumenten zu überanpassen.

## 1. Korpuspartitionen

Jedes Evaluationskorpus muss jedes Dokument genau einer Partition zuordnen.

### Entwicklungsset

Verwenden Sie dieses Set für diese Aufgaben:

- fehlendes Kernvokabular finden,
- wiederkehrende Muster von Mehrdeutigkeit finden,
- neue Regeln oder neue Prüfungen des Validators vorschlagen,
- Morphologie und Routing der Terminologie verbessern.

Änderungen an Wörterbuch und Regeln dürfen auf diesem Set basieren.

### Validierungsset

Verwenden Sie dieses Set während der Implementierung. Vergleichen Sie damit mögliche Änderungen und erkennen Sie Regressionen.

Fügen Sie kein Vokabular hinzu, nur weil es die Abdeckung im Validierungsset verbessert. Ein Kandidat benötigt trotzdem eine domänenübergreifende Begründung.

### Holdout-Set

Verwenden Sie dieses Set nur für die Evaluation eines Release.

Prüfen Sie keine Listen unbekannter Token aus dem Holdout, während Sie das Wörterbuch für dasselbe Release kuratieren. Die Holdout-Ergebnisse schätzen, wie gut die Ergebnisse auf unbekannten deutschen Text übertragbar sind.

Empfohlene erste Aufteilung nach Anzahl der Dokumente:

```text
70% development
15% validation
15% holdout
```

Schichten Sie die Aufteilung nach Domäne. Schichten Sie die Aufteilung auch nach herausgebender Organisation, wenn das praktisch möglich ist.

## 2. Zieldomänen

Wir empfehlen, das Korpus nicht auf Handbücher aus dem Ingenieurwesen zu begrenzen. STG-DE ist für kontrolliertes Deutsch in technischer, betrieblicher, B2B-, B2C- und agentenbezogener Kommunikation vorgesehen.

Zielstrata für v0.2:

1. Maschinenbau und Fertigung
2. Automotive und Mobilität
3. Elektrotechnik und Energie
4. Software, SaaS und IT-Betrieb
5. Medizintechnik und Anleitungen für Gesundheitsprodukte
6. Anlagenbau und Infrastruktur
7. Kundensupport und Inhalte von Hilfecentern
8. Anleitungen für Verbraucherprodukte
9. Anweisungen aus öffentlichem Sektor und Verwaltung
10. Kundenkommunikation in Finanzwesen und Versicherung
11. Logistik und Transport
12. Telekommunikation
13. Anforderungen und Spezifikationen
14. Anweisungen für Agenten, APIs, Werkzeuge und Systeme
15. Embedded-Systeme, IoT und Firmware
16. Funktionale Sicherheit
17. Produktsicherheit und Cyber Resilience Act
18. Mess- und Labortechnik

Wir empfehlen, dass kein einzelnes Stratum einen Anteil an der Token-Anzahl hat, mit dem es allein das allgemeine Kernvokabular bestimmen kann.

## 3. Zulässigkeit von Quellen

Eine Quelle ist zulässig, wenn alle diese Bedingungen zutreffen:

- Die Quelle ist öffentlich, für die vorgesehene Analyse lizenziert oder auf andere Art für eine rechtmäßige interne Evaluation verfügbar.
- Die Sprache der Quelle ist hauptsächlich Deutsch.
- Identität und Version des Dokuments sind dokumentierbar.
- Die Herkunft der Quelle ist reproduzierbar.
- Der Text ist reale Kommunikation. Er ist kein synthetischer Text, den jemand nur zur Verbesserung von STG-DE-Metriken erzeugt hat.

Verteilen Sie keinen vollständigen Text von Dritten, außer wenn das Recht zur Weitergabe ausdrücklich besteht.

## 4. Metadaten der Quelle

Dokumentieren Sie mindestens diese Angaben:

```yaml
id: unique-source-id
partition: development | validation | holdout
domain: software_it
organization: Example GmbH
title: Example Benutzerhandbuch
url: https://example.org/exact-document
version: "2.4"
published_on: 2026-01-15
accessed_on: 2026-08-22
language: de-DE
source_type: manual
text_type: manual | release_notes | update_procedure | requirement_specification | ...
license_or_access_basis: public-analysis-only
content_sha256: ...
token_count: 12345
extraction_method: html-text | pdf-text | plain-text | other
notes: ...
```

Verwenden Sie bevorzugt eine exakte Dokument-URL statt der Startseite eines Herstellers.

## 5. Stichproben und Deduplizierung

Für die Evaluation von Volltexten:

- Entfernen Sie Navigationselemente, wiederholte Kopf- und Fußzeilen, Cookie-Texte und offensichtliche Textbausteine, wo möglich.
- Behalten Sie aussagekräftige Überschriften, Warnungen, Listen, Anleitungen und Prosa.
- Erkennen Sie exakte Duplikate über den Inhalts-Hash.
- Erkennen Sie fast gleiche Handbücher oder versionierte Kopien, wo das praktisch möglich ist.
- Zählen Sie denselben Quelltext nicht mehrfach über Spiegelserver oder mehrere URLs.

Für die Evaluation von Auszügen:

- Dokumentieren Sie die Auswahlmethode, bevor Sie STG-DE-Ergebnisse prüfen.
- Wählen Sie Auszüge nicht gezielt aus, weil sie bekannte Verstöße oder bekanntes zugelassenes Vokabular enthalten.
- Halten Sie die Länge der Auszüge innerhalb desselben Benchmarks vergleichbar.

## 6. Aufnahme in das Kernvokabular

Häufigkeit im Korpus allein macht ein Wort nicht für das zentrale Wörterbuch geeignet.

Wir empfehlen, dass ein vorgeschlagener Kerneintrag im Normalfall alle diese Bedingungen erfüllt:

- Er kommt in mehreren unabhängigen Dokumenten vor.
- Er kommt in mehr als einer Domäne vor oder hat eine starke allgemeinsprachliche Funktion.
- Er hat eine kontrollierbare Bedeutung und Wortart.
- Er ist konkurrierenden Synonymen für Klarheit oder Konsistenz vorzuziehen.
- Er ist nicht hauptsächlich ein Begriff für ein Produkt, eine Organisation, einen Standard oder eine bestimmte Domäne.
- Er lässt sich mit einer stabilen kontrollierten Bedeutung dokumentieren.

Domänenspezifische Begriffe gehören in die Projektterminologie, außer wenn Belege für eine allgemeine Verwendung im Kern existieren.

## 7. Evaluationsmetriken

Melden Sie mindestens diese Metriken:

- gesamte Token-Anzahl,
- Anzahl eindeutiger normalisierter Token,
- Abdeckung durch zentrale kontrollierte Oberflächenformen,
- Rate des Routings zu Projekt- oder Domänenterminologie, wenn zutreffend,
- Rate unbekannter Token,
- Rate verbotener Begriffe und Begriffe mit Review-Pflicht,
- Anzahl deterministischer Befunde je 1.000 Wörter,
- Metriken je Domäne, je Textsorte und je Partition.

Eine Quelle darf die Kennzahlen nicht allein bestimmen. `policy.source_token_cap` in `corpus/v0.2-sources.yaml` legt eine Obergrenze an Token je Quelle fest. Die Felder `capped_tokens` und `capped_coverage` zählen von jeder Quelle höchstens diese Zahl an Token. Melden Sie die Zahlen mit und ohne Obergrenze.

Die Abdeckung ist keine Qualitätsbewertung. Eine höhere Abdeckung durch die Aufnahme von Domänenvokabular in den zentralen Kern ist nicht automatisch eine Verbesserung.

## 8. Manuelles Review des Holdouts

Kennzeichnen Sie für jeden Release-Kandidaten manuell eine Stichprobe aus dem Holdout-Set.

Dokumentieren Sie für jeden Befund des Validators mindestens diese Angaben:

```text
true positive
false positive
severity correct/incorrect
rule ID correct/incorrect
```

Prüfen Sie auch eine Stichprobe nicht markierter Sätze auf falsch negative Befunde.

Melden Sie die Präzision deterministischer Prüfungen getrennt von der Präzision heuristischer Prüfungen. Fassen Sie die Werte nicht zu einer einzigen Kennzahl für die Genauigkeit zusammen.

## 9. Disziplin bei Releases

Für ein Release, das Wörterbuch, Regeln oder Validator ändert:

1. Frieren Sie die Änderungen aus der Entwicklung ein.
2. Führen Sie das Validierungsset aus.
3. Korrigieren Sie Fehler der Implementierung, ohne Holdout-Vokabular für die Kuratierung zu verwenden.
4. Führen Sie das Holdout für den Release-Kandidaten einmal aus.
5. Veröffentlichen Sie aggregierte Holdout-Metriken.
6. Verschieben Sie altes Holdout-Material nur in die Entwicklung, wenn ein neues unabhängiges Holdout für den nächsten Zyklus ausgewählt ist.

## 10. Größenziel für v0.2

Erstes Ziel:

- mindestens 100.000 deutsche Token im gesamten Korpus,
- mindestens 10 Zielstrata, wenn geeignetes öffentliches oder lizenziertes Material existiert,
- mehrere unabhängige Organisationen je wichtigem Stratum,
- eine nicht leere Holdout-Partition auf Dokumentebene.

Bevorzugtes Ziel vor v0.3: mehr als 500.000 Token mit einer verbesserten linguistischen Analyse des Deutschen.
