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

### Pflichtbeispiel: `Datum` und `Daten`

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

Ein Werkzeug für die Entwicklung des Korpus darf den deutschen Snowball-Stemmer verwenden, um `MORPHOLOGY_CANDIDATE` auszugeben. Diese Klasse ist nur ein Beleg für die Kuratierung und zählt **nie als normative Konformität**.
