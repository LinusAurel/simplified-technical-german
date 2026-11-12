# STG-DE lexical decisions — through v0.1

## Status

Diese Datei dokumentiert lexikalische Entscheidungen mit großer Wirkung, die bis zum Autorenkern v0.1 entstanden sind. Die Einträge sind **vorläufig**, bis Fachleute für deutsche technische Redaktion und Terminologie die Einträge prüfen.

Der Ausgangsstandard verwendet ein kontrolliertes Wörterbuch. In diesem Wörterbuch haben freigegebene Wörter eine festgelegte Wortart und eine freigegebene Bedeutung. Nicht freigegebene Wörter können auf freigegebene Alternativen oder auf eine andere Satzkonstruktion verweisen. STG-DE behält diese Architektur, übersetzt das englische Wörterbuch aber **nicht** eins zu eins.

## Ziel des Release

Version 0.0.3 definiert einen durchsetzbaren **Autorenkern** für häufige deutsche technische Texte. Das Ziel des Kerns ist ein Grad an Determinismus, mit dem Agenten und Validatoren Texte erzeugen und umformulieren können. Die Domänenterminologie bleibt bei den Quellen der Projektterminologie.

### Selection order

1. Behalten Sie die offizielle technische Terminologie.
2. Verwenden Sie bevorzugt ein kurzes, häufiges Lemma der deutschen Allgemeinsprache für eine beabsichtigte Bedeutung.
3. Teilen Sie Bedeutungen, wenn das Deutsche eine präzisere lexikalische Wahl hat.
4. Verbieten Sie stilistische Synonyme, wenn diese Synonyme keine technische Unterscheidung hinzufügen.
5. Markieren Sie ein Wort als `restricted`, wenn das Wort nützlich ist, aber Kontext oder ein explizites Kriterium verlangt.
6. Geben Sie domänenspezifische Verben aus Fertigung, Recht, Medizin, Militär und Wissenschaft an die Projektterminologie, außer wenn diese Verben allgemein notwendig sind.

## Wichtige lexikalische Entscheidungen

### `verwenden` instead of `benutzen`, `nutzen`, `gebrauchen`

`verwenden` ist das bevorzugte allgemeine Verb für die Verwendung von Werkzeug, Material, Bauteil oder Hilfsmittel. `anwenden` ist für Methoden, Regeln und Verfahren reserviert. Diese Trennung behält zwei nützliche Begriffe und entfernt die stilistische Variation mit Synonymen.

### `prüfen` versus `testen` versus `untersuchen`

- `prüfen`: feststellen, ob eine explizite Bedingung oder Anforderung erfüllt ist.
- `testen`: einen definierten Test mit Kriterien ausführen.
- `untersuchen`: systematisch nach Schäden, Fehlern oder festgelegten Merkmalen suchen.

### `erhöhen` / `verringern` versus `steigen` / `sinken`

Verwenden Sie das transitive Paar, wenn ein Akteur einen Wert ändert. Verwenden Sie das intransitive Paar, wenn sich der Wert als Ergebnis eines Prozesses ändert.

### `einbauen` versus `installieren`

Verwenden Sie `einbauen` für mechanische oder elektrische Bauteile in einer Einbaulage. Verwenden Sie `installieren` hauptsächlich für Software. Verwenden Sie `installieren` auch, wenn die offizielle Terminologie die Installation eines vollständigen Systems definiert.

### `warten`

Das zeitliche Verb `warten` ist zulässig. Die Bedeutung Instandhaltung ist absichtlich nicht im zentralen Lexikon, weil dieses Homonym sehr mehrdeutig ist. Verwenden Sie für Instandhaltung freigegebene Projektterminologie, zum Beispiel `instand halten`, wenn das Projekt diesen Begriff freigibt.

### `sichern`

Das allgemeine Verb ist nicht freigegeben. Das Verb kann befestigen, eine Datensicherung erstellen, verriegeln, schützen oder einen sicheren Zustand herstellen bedeuten. Verwenden Sie das präzise Verb: `befestigen`, `speichern`, `verriegeln`, `schützen` oder einen technischen Begriff des Projekts.

### `können`, `dürfen`, `müssen`

- `können`: Fähigkeit oder faktische Möglichkeit.
- `dürfen`: Erlaubnis. `nicht dürfen`: Verbot.
- `müssen`: explizite Anforderung.

Konditionale oder vorsichtige Formen wie `könnte`, `müsste` und `sollte` sind kein Teil der kontrollierten verbindlichen Formulierungen.

### Vague qualifiers

Wörter wie `ordnungsgemäß`, `geeignet`, `ausreichend`, `vorsichtig` und `zeitnah` sind verboten oder prüfpflichtig. Der Grund: Diese Wörter ersetzen oft ein fehlendes Kriterium. Wir empfehlen, dass ein Validator das Kriterium anfordert und kein Kriterium erfindet.

## Richtlinie für unbekannte Wörter

Für `STG-C-core` gilt: Ein nicht gesperrtes Token der Allgemeinsprache, das sich nicht zu diesem Lexikon auflösen lässt, ist **nicht automatisch ein Synonymkandidat**. Der Agent muss diese Arbeitsschritte ausführen:

1. Prüfen, ob das Token freigegebene Projektterminologie ist.
2. Prüfen, ob das Token ein geschützter Name, eine geschützte Beschriftung oder eine geschützte Kennung ist.
3. Die Liste der verbotenen Wörter und Umformulierungen prüfen.
4. In allen anderen Fällen `NEEDS_LEXICON_REVIEW` zurückgeben.

Diese Strategie ist absichtlich konservativ.


## v0.0.3 corpus-driven decisions

### Corpus frequency is not approval

Ein häufiges Wort in normalem technischem Deutsch kann für kontrolliertes Deutsch trotzdem ungeeignet sein. Belege aus dem Korpus erzeugen eine Pflicht zur Prüfung. Diese Belege haben keinen Vorrang vor den Präzisionsregeln. Aus diesem Grund bleiben häufige Formen wie `sowie`, `beziehungsweise`, vage Qualifikatoren und unpersönliche Konstruktionen verboten oder prüfpflichtig.

### Contractions are normalized, not prohibited

Deutsche Formen wie `im`, `am`, `beim`, `vom`, `zum` und `zur` sind regelmäßige grammatische Kontraktionen. In v0.0.2 hat die Behandlung dieser Formen als unabhängige unbekannte Wörter falsche lexikalische Lücken erzeugt. Version 0.0.3 löst diese Formen für die Suche auf und behält den Oberflächentext.

### Controlled connector set

Die Korpusanalyse hat eine große stilistische Variation bei logischen Verknüpfungswörtern gezeigt. Version 0.0.3 verwendet bevorzugt eine kleinere explizite Menge:

- Addition: `und`
- Gegensatz: `aber`
- Reihenfolge: `dann` / `danach`
- Ergebnis: `deshalb`
- Bedingung: `wenn`
- Ursache: `weil`
- früheres Ereignis: `bevor`
- gleichzeitiger Zeitraum: `während`

Deshalb werden `sowie`, `jedoch`, `daher` und `anschließend` zu kontrollierten Alternativen normalisiert, wenn die Bedeutung erhalten bleibt.

### Pronominal adverbs

`dabei`, `dazu`, `daraus`, `davon`, `darüber`, `dafür` und `hierfür` sind nützliche deutsche Formen. Diese Formen können aber ein Bezugswort und eine semantische Beziehung gleichzeitig komprimieren. Deshalb sind diese Formen im strengen Kern `review_required`. Für diese Formen gilt STG-DE-4.5.

### Cross-domain direct verbs

Die Belege aus dem öffentlichen Korpus haben die Aufnahme enger zentraler Bedeutungen für bestimmte Verben gestützt. Diese Verben kommen in mehreren technischen Domänen vor und beschreiben konkrete Handlungen oder Beziehungen. Beispiele sind `anschließen`, `abziehen`, `abkühlen`, `verschließen`, `beheben`, `bereitstellen`, `enthalten` und `entsprechen`.

Dieselben Belege haben die Aufnahme produktspezifischer Verben oder Verben aus Ingenieurdomänen in das zentrale Lexikon **nicht** gerechtfertigt. Diese Verben bleiben technische Verben des Projekts.

### `bestehen`

Nur die Bedeutung Zusammensetzung ist zentral kontrolliert: `X besteht aus Y`. Andere Bedeutungen von `bestehen` sind außerhalb des zentralen Eintrags. Beispiele für diese Bedeutungen sind eine Prüfung erfolgreich abschließen, fortbestehen oder auf etwas beharren.

### `lassen`

`lassen` ist auf Konstruktionen eingeschränkt, in denen der Leser einen explizit genannten physischen oder automatischen Prozess fortsetzen lässt, zum Beispiel das Abkühlen. Autoren dürfen `lassen` nicht verwenden, um den verantwortlichen Akteur zu verstecken.

---

# Korpusentscheidungen für v0.1

## D-04-01 — Declared noun plurals are controlled inflections

**Entscheidung:** Der deklarierte Plural eines Substantivs wird als kontrollierte Flexion aufgelöst. Für diesen Plural ist kein zweiter Wörterbucheintrag notwendig.

**Grund:** Der Validator in v0.0.3 hat normale deklarierte Pluralformen wie `Informationen`, `Gefahren`, `Schritte` und `Geräte` falsch als unbekannte Wörter oder Begriffskandidaten eingeordnet. Diese Lücke ist eine Lücke im Validator, keine Lücke im Wortschatz.

## D-04-02 — Canonical lemma wins over an inflection alias

**Entscheidung:** Prüfen Sie vor der Annahme eines Flexionsalias, ob diese Oberflächenform selbst ein kanonisches Lemma ist.

**Grund:** `Datum` deklariert den Plural `Daten`. Technisches Deutsch verwendet `Daten` aber als unabhängigen Begriff für technische Informationen oder Daten. Deshalb fügt v0.1 `DE-NOU-daten` hinzu und verhindert, dass der Pluralalias Vorrang vor diesem Eintrag hat.

## D-04-03 — Capitalization does not establish terminology status

**Entscheidung:** Unbekannte großgeschriebene Wörter werden als `LEXICAL_NOUN_CANDIDATE` eingeordnet, nicht als `TECHNICAL_TERM_CANDIDATE`.

**Grund:** Alle deutschen Substantive sind großgeschrieben. Wenn ein Validator die Großschreibung als Beleg für Terminologie behandelt, ordnet der Validator normale allgemeine Substantive systematisch falsch ein.

## D-04-04 — Cross-domain frequency is necessary evidence, not sufficient approval

**Entscheidung:** Häufige Wörter kommen nur in das zentrale Lexikon, wenn eine enge kontrollierte Bedeutung festgelegt werden kann.

**Beispiele für freigegebene oder eingeschränkte Wörter:** `Betriebsanleitung`, `Fachpersonal`, `Verletzung`, `Produkt`, `Version`, `Daten`, `lesen`, `wählen`.

**Prüfpflichtig trotz Häufigkeit:** `führen`, `bieten`, `berücksichtigen`, `gewährleisten`.

Die zweite Gruppe ist für eine bedingungslose automatische Annahme zu mehrdeutig oder zu abstrakt.
