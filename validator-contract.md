# STG-DE-Validatorvertrag

## 1. Zweck

Diese Datei definiert einen praktischen Vertrag für Linter, Autorenwerkzeuge, LLM-Reviewer, CI-Gates und Integrationen in Editoren.

## 2. Eingabe

Minimale Eingabe:

```yaml
text: "..."
text_type: procedure | description | safety | note
locale: de-DE
conformance_target: STG-R | STG-T | STG-C-core | STG-C
```

Empfohlene zusätzliche Eingabe:

```yaml
terminology_sources:
  - project-terms.yaml
locked_spans:
  - start: 120
    end: 145
    type: ui_label
safety_profile: project-safety-v2
instruction_profile: formal-sie-imperative
```

## 3. Ausgabe

```yaml
status: pass | fail | needs_input
metrics:
  sentences: 8
  max_words_in_sentence: 19
  passive_candidates: 1
  terminology_unknown: 0
diagnostics:
  - rule: STG-3.6
    severity: error
    confidence: 0.97
    span: "Die Sicherung wird entfernt."
    message: "Passive instruction."
    proposed_fix: "Entfernen Sie die Sicherung."
```

## 4. Schweregrad

- `error`: deterministischer Verstoß gegen eine verbindliche Regel oder semantischer Verstoß mit hoher Konfidenz.
- `warning`: heuristischer Befund, der ein Review erfordert.
- `info`: nicht verbindliche Empfehlung.
- `needs_input`: Eine sichere Umformulierung erfordert Informationen zu Domäne, Sicherheit oder Modalität.

## 5. Empfohlene Pipeline für Regeln

### Phase A: geschützte Bereiche

Erkennen Sie diese Elemente und schützen Sie die Elemente vor Änderungen:

- Kennungen,
- Formeln,
- Teilenummern,
- Bezeichnungen der Benutzeroberfläche,
- Eigennamen,
- zitierte Texte und Rechtstexte,
- Titel von Dokumenten.

### Phase B: Segmentierung und Zählungen

Prüfen Sie diese Elemente:

- Satzgrenzen,
- Listenstruktur,
- Grenzen von 20 und 25 Wörtern,
- Anzahl der Sätze in einem Absatz,
- Semikolons,
- Regeln für Klammern.

### Phase C: deterministische lexikalische Prüfungen

Prüfen Sie diese Elemente:

- verbotene Begriffe und Wendungen,
- nicht zugelassene Abkürzungen,
- Profil für regionale Schreibweisen, wenn die Werkzeuge es unterstützen,
- bekannte Varianten der Projektterminologie.

### Phase D: syntaktische Heuristiken

Erkennen Sie diese Elemente:

- Passivkandidaten (`werden` + Partizip II),
- lange Satzklammern durch trennbare Verben,
- Nominalisierungen und Funktionsverbgefüge,
- verschachtelte Nebensätze,
- `man`,
- mehrdeutige Modalverben,
- mehrdeutige Negationen.

Ein Parser muss Zustandskonstruktionen wie `ist geschlossen` von Vorgangspassiven unterscheiden, wo das möglich ist.

### Phase E: semantische und domänenbezogene Prüfungen

Prüfen Sie diese Elemente:

- ein Begriff je Konzept,
- Mehrdeutigkeit des Bezugsworts eines Pronomens,
- Zulassung von Fachbegriffen,
- Zulassung von Fachverben,
- Absicht der Modalität,
- Konsistenz von Sicherheitsfolge und Sicherheitskategorie.

## 6. Heuristik für die Komplexität von Komposita

Für neue oder nicht zugelassene Komposita darf ein Validator ein Nomen mit einem Kompositazerleger zerlegen. Geben Sie eine Warnung aus, wenn eine dieser Bedingungen zutrifft:

- Der Zerleger erkennt mehr als drei bedeutungstragende lexikalische Bestandteile.
- Es gibt mehr als eine plausible Zerlegung.
- Das Kompositum ist länger als 30 Zeichen und ist kein zugelassener Begriff.

Das ist eine Heuristik und keine verbindliche lexikalische Regel für offizielle Begriffe.

## 7. Erkennung von Passiv

Muster mit hohem Wert:

- `werden` + Partizip II → wahrscheinlich Vorgangspassiv,
- Modalverb + Partizip II + `werden` → komplexes Passiv,
- `sein` + Partizip II → Kandidat für Zustand oder Adjektiv, nicht automatisch ein Verstoß.

In einem Text vom Typ `procedure` empfehlen wir, einen Passivkandidaten im Normalfall als Fehler zu melden. In einem Text vom Typ `description` ist ein Passivkandidat eine Warnung, außer wenn der Agent oder Akteur eindeutig bekannt ist.

## 8. Erkennung von Modalität

Markieren Sie diese Formen:

- `soll`, `sollen`, `sollte`, `sollten`,
- `müsste`, `müssten`,
- `könnte`, `könnten`,
- `gegebenenfalls`, `ggf.`.

Das Werkzeug darf diese Formen nicht automatisch in `muss` oder einen Imperativ umwandeln, wenn es die beabsichtigte Verbindlichkeit nicht kennt.

## 9. Auflösung von Pronomen

Ein Pronomen der dritten Person oder ein Demonstrativum kann im vorherigen Satz oder Teilsatz mehr als ein plausibles Bezugswort haben. Ein plausibles Bezugswort passt in Numerus und Genus zum Pronomen. Wenn mehr als ein plausibles Bezugswort existiert, geben Sie eine Warnung oder einen Fehler aus.

Wiederholen Sie in vorgeschlagenen Korrekturen bevorzugt das Nomen.

## 10. Unbekannte Wörter

Für `STG-R` ist ein unbekanntes allgemeines Wort nicht automatisch ein Fehler, außer wenn es gegen eine bestimmte Regel verstößt.

Für `STG-T` sind unbekannte Begriffe, die technisch aussehen, Fehler oder `needs_input`, bis sie zugelassen sind.

Für `STG-C-core` muss jedes nicht gesperrte lexikalische Element zu einem dieser Einträge aufgelöst werden:

- ein zugelassener oder eingeschränkter zentraler Eintrag von v0.4,
- ein zugelassener technischer Eintrag.

Eingeschränkte Einträge müssen ihre Einschränkungen erfüllen. Unbekannte allgemeine Wörter erzeugen `needs_input` oder `NEEDS_LEXICON_REVIEW`.

Für `STG-C` muss jedes nicht gesperrte lexikalische Element zu einem zukünftigen zentralen oder technischen Eintrag aufgelöst werden. Dieser Eintrag muss zu einem breiten Wortschatz gehören, den Menschen geprüft haben. v0.4 beansprucht keine allgemeine Zertifizierung für `STG-C`.


## 11. Lexikalische Auflösung in v0.4

Empfohlene Reihenfolge der Auflösung für `STG-C-core`:

1. gesperrte und geschützte Bereiche,
2. zugelassene Projektterminologie,
3. längste zugelassene und verbotene Muster für Wendungen,
4. Auflösung deutscher Kontraktionen aus `dictionary/contractions.yaml`,
5. lexikalische Unterscheidungen nach Groß- und Kleinschreibung (`Sie` gegenüber `sie`),
6. kanonisches zentrales Lemma mit korrekter Wortart und zugelassener Bedeutung,
7. deklarierte Oberflächenformen und kontrollierte Flexionsformen, mit Vorrang des kanonischen Lemmas bei Kollisionen,
8. deterministische Morphologie und Rekonstruktion trennbarer Verben,
9. Liste der verbotenen Wörter und der Wörter mit Review-Pflicht für das aufgelöste Lemma,
10. unbekannt -> `NEEDS_LEXICON_REVIEW`.

Ein zentrales Wort mit dem Status `restricted` besteht nur, wenn seine Einschränkung erfüllt ist. Ein Validator darf `review_required` nicht in ein automatisches Bestehen umwandeln.

Die lexikalische Suche basiert auf Lemmata. Wenden Sie die morphologische Analyse vor der Suche an. Rekonstruieren Sie die Lemmata trennbarer Verben, wo das möglich ist. Siehe `dictionary/MORPHOLOGY.md`.


## 12. Pronominaladverbien

Erkennen Sie deutsche Pronominaladverbien wie `dabei`, `dazu`, `daraus`, `davon`, `darüber`, `dafür` und `hierfür`. Eine solche Form kann sich auf mehr als ein Objekt, eine Handlung, eine Ursache, einen Zweck oder eine vorherige Aussage beziehen. In diesem Fall geben Sie `NEEDS_REFERENCE_INPUT` unter STG-DE-4.5 zurück. Wählen Sie nicht automatisch ein Bezugswort aus.

## 13. Modus für die Korpusentwicklung

Ein Entwicklungswerkzeug darf nicht aufgelöste Token als `MORPHOLOGY_CANDIDATE`, `LEXICAL_NOUN_CANDIDATE` oder `PROTECTED_TOKEN_CANDIDATE` klassifizieren. Diese Kennzeichnungen sind Status für die Sichtung. Sie bedeuten kein Bestehen der Konformitätsprüfung. Siehe `tools/corpus_validate.py`.

## 14. Routing deutscher Nomenkandidaten

Leiten Sie `technical noun` nicht aus der Großschreibung ab. Im Deutschen sind alle Nomen großgeschrieben. Ein unbekanntes großgeschriebenes Token ist ein `LEXICAL_NOUN_CANDIDATE`, bis es zu einem dieser Ziele aufgelöst ist: zentrales Lexikon, zugelassene Projekt- oder Domänenterminologie, geschützter Bereich oder Review.

Akzeptieren Sie für deklarierte Pluralformen von Nomen nur die Pluralformen, die das Lexikon deklariert. Prüfen Sie vor der Anwendung eines Plural-Alias, ob die Oberflächenform selbst ein kanonisches Lemma ist. `Daten` muss zu `DE-NOU-daten` in der Bedeutung „technische Daten“ aufgelöst werden. Der Plural-Alias von `Datum` darf `Daten` nicht übernehmen.
