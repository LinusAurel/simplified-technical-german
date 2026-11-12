# STG-DE-Leitfaden für Wörterbuch und Morphologie

Erzeugt aus der kanonischen Dokumentation im Verzeichnis `dictionary/`. Bearbeiten Sie diese Datei nicht direkt.


---

<!-- source: dictionary/README.md -->

# Kontrolliertes Wörterbuch von STG-DE

**Release:** 0.6.0  
**Profile:** `de-DE`  
**Status:** experimenteller Autorenkern, an einem geschichteten Korpus validiert. Dieser Kern ist in diesem Release kein Wörterbuch der deutschen Allgemeinsprache, das Menschen vollständig geprüft haben.

## Inhalt

- **435** zentrale freigegebene oder eingeschränkte lexikalische Einträge,
- **442** kontrollierte Bedeutungen,
- **160** verbotene oder prüfpflichtige Wörter und Wortgruppen,
- **172** kontrollierte zentrale Verben,
- kontrollierte Kontraktionen,
- deklarierte Pluralformen von Substantiven und kuratierte unregelmäßige Oberflächenformen,
- Begriffsindex und Metadaten zur Abdeckung des Releases,
- Kategoriemodelle für technische Substantive und technische Verben in Projekten und Domänen.

Das Lexikon ist unabhängig für das Deutsche entworfen. Das Lexikon ist ein kontrolliertes Wörterbuch mit definierten Bedeutungen, Wortarten und freigegebenen Formen.

## Dateien

- `approved-words.yaml` — normative Einträge des Autorenkerns.
- `prohibited-words.yaml` — verbotene oder prüfpflichtige Formulierungen mit Hinweisen zur Umformulierung.
- `contractions.yaml` — Normalisierung von Präposition und Artikel vor der lexikalischen Suche.
- `concept-index.yaml` — Index der kontrollierten Bedeutungen für Agenten und Validatoren.
- `coverage.yaml` — Zahlen des Releases und Zusammenfassung des Korpus.
- `DECISIONS.md` — Begründungen für die Kuratierung.
- `MORPHOLOGY.md` — Auflösung von Lemma, Flexion und trennbaren Verben.
- `technical-nouns.yaml` — Kategorien für technische Substantive in Projekten und Domänen.
- `technical-verbs.yaml` — Kategorien für technische Verben in Projekten und Domänen.

## Prinzip der Auflösung

Lösen Sie die Eingabe in dieser Reihenfolge auf. Die Reihenfolge ist dieselbe wie in `dictionary/MORPHOLOGY.md` und `validator-contract.md`:

1. geschützter Text oder Kennung,
2. freigegebene Projektterminologie oder Domänenterminologie,
3. längste Wortgruppe,
4. Normalisierung von Kontraktionen,
5. lexikalische Unterscheidung nach Groß- und Kleinschreibung,
6. kanonisches zentrales Lemma oder deklarierte Oberflächenform,
7. deklarierte kontrollierte Flexion,
8. deterministische morphologische Analyse und Analyse trennbarer Verben,
9. Suche in der Liste der verbotenen und prüfpflichtigen Wörter für das aufgelöste Lemma,
10. in allen anderen Fällen `NEEDS_LEXICON_REVIEW`.

Ein kanonisches Lemma hat Vorrang vor dem Flexionsalias eines anderen Eintrags. Diese Regel verhindert, dass ein Validator `Daten` (technische Informationen oder Daten) ohne Meldung als Plural von `Datum` auflöst.

## Statuswerte

- `approved` — für die angegebene kontrollierte Bedeutung zulässig.
- `restricted` — nur zulässig, wenn alle angegebenen Einschränkungen erfüllt sind.
- `technical_only` — verlangt eine Freigabe als Projektterminologie oder Domänenterminologie.
- `prohibited` — nicht verwenden, außer in geschütztem externem Text.
- `review_required` — für eine automatische Annahme nicht sicher. Der Eintrag verlangt eine Prüfung des Kontexts oder eine Umformulierung.

## Richtlinie für das Korpus

Die Häufigkeit im Korpus ist ein Beleg für eine **Prüfung**, keine Freigabe. STG-DE nimmt ein Wort nur in den Kern auf, wenn die domänenübergreifende Bedeutung des Worts sinnvoll kontrolliert werden kann. Häufige, aber abstrakte oder mehrdeutige Verben wie `führen`, `bieten`, `berücksichtigen` und `gewährleisten` bleiben prüfpflichtig.

Domänenspezifische Bauteile, Produktnamen, medizinische Begriffe, Fahrzeugbegriffe, Software-Kennungen und ähnlicher Wortschatz gehören zur Projektterminologie oder Domänenterminologie. Diese Regel gilt auch, wenn diese Wörter häufig sind.

Siehe `../corpus/validation-report.md`.

## `STG-C-core` versus `STG-C`

`STG-C-core` ist ein experimentelles Profil mit geschlossenem Wortschatz. Dieses Profil gilt für Texte, die Autoren absichtlich mit diesem Kern und mit freigegebener Projektterminologie schreiben.

`STG-C` bleibt für ein zukünftiges, breiteres Lexikon reserviert, das Menschen geprüft haben. Dieses Release darf `STG-C` nicht beanspruchen.

---

<!-- source: dictionary/MORPHOLOGY.md -->

# Morphologie und lexikalische Auflösung in STG-DE

`STG-C-core` ist auf der Ebene **Lemma + Wortart + kontrollierte Bedeutung** definiert. Ein Validator darf nicht verlangen, dass jede flektierte deutsche Oberflächenform ein separater Wörterbucheintrag ist.

## Reihenfolge der Auflösung

1. Geschützte oder gesperrte Textabschnitte
2. Freigegebene Projektterminologie oder Domänenterminologie
3. Längster Treffer einer freigegebenen oder verbotenen Wortgruppe
4. Auflösung von Standardkontraktionen
5. Lexikalische Suche mit Unterscheidung nach Groß- und Kleinschreibung
6. Exaktes kanonisches zentrales Lemma oder deklarierte `surface_forms`
7. Deklarierte kontrollierte Flexion
8. Deterministische morphologische Analyse und Rekonstruktion trennbarer Verben
9. Suche in der Liste der verbotenen und prüfpflichtigen Wörter für das aufgelöste Lemma
10. In allen anderen Fällen `NEEDS_LEXICON_REVIEW`

Eine ungefähre Schreibweise oder ein Stemming ist kein normativer Ersatz für eine Lemmatisierung.

## Vorrang des kanonischen Lemmas

Wenn eine flektierte Form eines Eintrags auch das kanonische Lemma eines anderen Eintrags ist, hat das kanonische Lemma Vorrang.

### Required example: `Datum` / `Daten`

Im Deutschen ist `Daten` der Plural von `Datum`. Im technischen Deutsch ist `Daten` auch ein unabhängiger lexikalischer Begriff mit der Bedeutung technische Informationen oder Daten.

Deshalb gilt:

```text
Daten  -> DE-NOU-daten      # technical data/information
Datum  -> DE-NOU-datum      # calendar date
```

Ein Validator darf eine naive Pluralzuordnung `Datum -> Daten` **nicht** annehmen, bevor der Validator prüft, ob `Daten` selbst ein kanonischer Eintrag ist.

## Deutsche Kontraktionen

Standardkontraktionen aus Präposition und Artikel sind Grammatik und kein technischer Wortschatz. Normalisieren Sie Formen wie diese:

- `im` -> `in` + `dem`
- `am` -> `an` + `dem`
- `beim` -> `bei` + `dem`
- `vom` -> `von` + `dem`
- `zum` -> `zu` + `dem`
- `zur` -> `zu` + `der`

Diese Auflösung dient nur der lexikalischen Analyse. Schreiben Sie eine korrekte, eindeutige Oberflächenform nicht um, nur um die Bestandteile zu zeigen.

## Substantive

Ein freigegebenes Substantiv erlaubt die grammatischen Kasusformen und den ausdrücklich deklarierten Plural. Diese Erlaubnis gilt nicht, wenn eine Einschränkung etwas anderes festlegt.

Der Entwicklungsvalidator zählt den **deklarierten Plural** als `CENTRAL_INFLECTION`. Der Entwicklungsvalidator erfindet keine Pluralformen, die nicht in der Liste stehen.

Unbekannte großgeschriebene Wörter sind nicht automatisch technische Begriffe. Im Deutschen schreiben Autoren normale Substantive groß. Ein nicht aufgelöstes Substantiv muss zu einem dieser Ziele aufgelöst werden:

- zu einem zentralen Eintrag,
- zu Projektterminologie,
- zu einem geschützten Namen oder einer geschützten Kennung,
- zu einer Prüfung.

## Formen mit Groß- und Kleinschreibung

Lösen Sie die formalen Leserformen vor der Normalisierung der Groß- und Kleinschreibung auf:

- `Sie`, `Ihnen`
- `Ihr`, `Ihre`, `Ihren`, `Ihrem`, `Ihrer`, `Ihres`

Die Formen `sie` und `ihr` in der dritten Person sind separate eingeschränkte Einträge. Diese Formen verlangen ein eindeutiges Bezugswort.

## Artikel und Determinative

Häufige flektierte Formen stehen in `surface_forms`. Lösen Sie diese Formen vor der syntaktischen Validierung zu dem kontrollierten Eintrag für den Artikel oder den Determinativ auf.

## Verben

Wir empfehlen, dass ein normativer Validator finite und infinite Formen vor der Suche im Wörterbuch lemmatisiert.

Rekonstruieren Sie bei trennbaren Verben das Lemma aus dem Satz:

- `Schalten Sie das Gerät ein.` -> `einschalten`
- `Die Anzeige zeigt den Wert an.` -> `anzeigen`
- `Stellen Sie den Datensatz bereit.` -> `bereitstellen`
- `Legen Sie den Grenzwert fest.` -> `festlegen`

Ein Validator darf einen finiten Stamm wie `stellt` nicht isoliert bewerten, wenn eine abgetrennte Verbpartikel später im Satz das Lemma ändern kann.

## Adjektive

Regelmäßig flektierte Formen von Adjektiven werden zu dem freigegebenen Grundlemma aufgelöst. Komparativ und Superlativ verlangen eine ausdrückliche Erlaubnis oder eine Regel oder einen Eintrag, die den Vergleich zulassen. Nehmen Sie nicht an, dass jedes freigegebene Adjektiv sinnvoll gesteigert werden kann.

## Wortgruppen

Lösen Sie Einträge mit mehreren Tokens vor der Suche nach einzelnen Tokens auf. Einträge, die `...` enthalten, verlangen ein syntaktisches Muster und keinen wörtlichen Teilstring-Vergleich.

## Heuristiken für die Entwicklung

`tools/corpus_validate.py` darf den deutschen Snowball-Stemmer verwenden, um `MORPHOLOGY_CANDIDATE` auszugeben. Diese Klasse ist nur ein Beleg für die Kuratierung und zählt **nie als normative Konformität**.

---

<!-- source: dictionary/DECISIONS.md -->

# Lexikalische Entscheidungen in STG-DE

## Status

Diese Datei dokumentiert lexikalische Entscheidungen mit großer Wirkung, die bis zum Autorenkern v0.4 entstanden sind. Die Einträge sind **vorläufig**, bis Fachleute für deutsche technische Redaktion und Terminologie die Einträge prüfen.

Der Ausgangsstandard verwendet ein kontrolliertes Wörterbuch. In diesem Wörterbuch haben freigegebene Wörter eine festgelegte Wortart und eine freigegebene Bedeutung. Nicht freigegebene Wörter können auf freigegebene Alternativen oder auf eine andere Satzkonstruktion verweisen. STG-DE behält diese Architektur, übersetzt das englische Wörterbuch aber **nicht** eins zu eins.

## Ziel des Release

Die Versionen 0.3 und 0.4 definieren einen durchsetzbaren **Autorenkern** für häufige deutsche technische Texte. Das Ziel des Kerns ist ein Grad an Determinismus, mit dem Agenten und Validatoren Texte erzeugen und umformulieren können. Die Domänenterminologie bleibt bei den Quellen der Projektterminologie.

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

Konditionale oder abschwächende Formen wie `könnte`, `müsste` und `sollte` sind kein Teil der kontrollierten verbindlichen Formulierungen.

### Vague qualifiers

Wörter wie `ordnungsgemäß`, `geeignet`, `ausreichend`, `vorsichtig` und `zeitnah` sind verboten oder prüfpflichtig. Der Grund: Diese Wörter ersetzen oft ein fehlendes Kriterium. Wir empfehlen, dass ein Validator das Kriterium anfordert und kein Kriterium erfindet.

## Richtlinie für unbekannte Wörter

Für `STG-C-core` gilt: Ein nicht gesperrtes Token der Allgemeinsprache, das sich nicht zu diesem Lexikon auflösen lässt, ist **nicht automatisch ein Synonymkandidat**. Der Agent muss diese Arbeitsschritte ausführen:

1. Prüfen, ob das Token freigegebene Projektterminologie ist.
2. Prüfen, ob das Token ein geschützter Name, eine geschützte Beschriftung oder eine geschützte Kennung ist.
3. Die Liste der verbotenen Wörter und Umformulierungen prüfen.
4. In allen anderen Fällen `NEEDS_LEXICON_REVIEW` zurückgeben.

Diese Strategie ist absichtlich konservativ.


## v0.3 corpus-driven decisions

### Corpus frequency is not approval

Ein häufiges Wort in normalem technischem Deutsch kann für kontrolliertes Deutsch trotzdem ungeeignet sein. Belege aus dem Korpus erzeugen eine Pflicht zur Prüfung. Diese Belege haben keinen Vorrang vor den Präzisionsregeln. Aus diesem Grund bleiben häufige Formen wie `sowie`, `beziehungsweise`, vage Qualifikatoren und unpersönliche Konstruktionen verboten oder prüfpflichtig.

### Contractions are normalized, not prohibited

Deutsche Formen wie `im`, `am`, `beim`, `vom`, `zum` und `zur` sind regelmäßige grammatische Kontraktionen. In v0.2 hat die Behandlung dieser Formen als unabhängige unbekannte Wörter falsche lexikalische Lücken erzeugt. Version 0.3 löst diese Formen für die Suche auf und behält den Oberflächentext.

### Controlled connector set

Die Korpusanalyse hat eine große stilistische Variation bei logischen Verknüpfungswörtern gezeigt. Version 0.3 verwendet bevorzugt eine kleinere explizite Menge:

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

# Korpusentscheidungen in Release 0.4.0

## D-04-01 — Declared noun plurals are controlled inflections

**Entscheidung:** Der deklarierte Plural eines Substantivs wird als kontrollierte Flexion aufgelöst. Für diesen Plural ist kein zweiter Wörterbucheintrag notwendig.

**Grund:** Der Validator in v0.3 hat normale deklarierte Pluralformen wie `Informationen`, `Gefahren`, `Schritte` und `Geräte` falsch als unbekannte Wörter oder Begriffskandidaten eingeordnet. Diese Lücke ist eine Lücke im Validator, keine Lücke im Wortschatz.

## D-04-02 — Canonical lemma wins over an inflection alias

**Entscheidung:** Prüfen Sie vor der Annahme eines Flexionsalias, ob diese Oberflächenform selbst ein kanonisches Lemma ist.

**Grund:** `Datum` deklariert den Plural `Daten`. Technisches Deutsch verwendet `Daten` aber als unabhängigen Begriff für technische Informationen oder Daten. Deshalb fügt v0.4 `DE-NOU-daten` hinzu und verhindert, dass der Pluralalias Vorrang vor diesem Eintrag hat.

## D-04-03 — Capitalization does not establish terminology status

**Entscheidung:** Unbekannte großgeschriebene Wörter werden als `LEXICAL_NOUN_CANDIDATE` eingeordnet, nicht als `TECHNICAL_TERM_CANDIDATE`.

**Grund:** Alle deutschen Substantive sind großgeschrieben. Wenn ein Validator die Großschreibung als Beleg für Terminologie behandelt, ordnet der Validator normale allgemeine Substantive systematisch falsch ein.

## D-04-04 — Cross-domain frequency is necessary evidence, not sufficient approval

**Entscheidung:** Häufige Wörter kommen nur in das zentrale Lexikon, wenn eine enge kontrollierte Bedeutung festgelegt werden kann.

**Beispiele für freigegebene oder eingeschränkte Wörter:** `Betriebsanleitung`, `Fachpersonal`, `Verletzung`, `Produkt`, `Version`, `Daten`, `lesen`, `wählen`.

**Prüfpflichtig trotz Häufigkeit:** `führen`, `bieten`, `berücksichtigen`, `gewährleisten`.

Die zweite Gruppe ist für eine bedingungslose automatische Annahme zu mehrdeutig oder zu abstrakt.
