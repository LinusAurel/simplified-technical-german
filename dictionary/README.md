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
