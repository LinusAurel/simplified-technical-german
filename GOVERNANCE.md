# STG-DE-Governance

STG-DE ist ein offenes Projekt für eine kontrollierte Sprache. Die Spezifikation ist die maßgebliche Quelle. Der Validator und der Agent Skill implementieren die Spezifikation oder unterstützen ihre Anwendung. Diese Werkzeuge definieren die Spezifikation nicht neu.

## Aufgaben der Maintainer

Maintainer sind für diese Aufgaben verantwortlich:

- Sie halten veröffentlichte Regel-IDs stabil.
- Sie prüfen Änderungen an normativer Sprache getrennt von Änderungen, die nur die Implementierung vereinfachen.
- Sie halten das zentrale Vokabular domänenübergreifend und belegbar.
- Sie fordern Tests für maschinell prüfbares Verhalten.
- Sie schützen die Holdout-Evaluation vor Informationen aus der Entwicklung.
- Sie dokumentieren inkompatible Änderungen.
- Sie halten den eigenständigen Agent Skill synchron mit den kanonischen Regeln und Wörterbuchdaten.

## Änderungsklassen

### Redaktionell

Änderungen an Rechtschreibung, Formatierung, Beispielen oder Erklärungen, die das normative Verhalten nicht ändern.

### Lexikalisch

Änderungen an zugelassenen Wörtern, kontrollierten Bedeutungen, Formen, verbotenen Begriffen, Begriffen mit Prüfpflicht oder bevorzugten Ersetzungen. Befolgen Sie den Abschnitt „Lexikalische Änderungen“.

### Regel

Änderungen an einer normativen Regel, einer Empfehlung, einem Schwellenwert, einer Anwendungsbedingung oder der Auslegung der Konformität. Verwenden Sie `proposals/STG-CHANGE-TEMPLATE.md`.

### Implementierung

Änderungen an Validator, Werkzeugen, Paketierung oder Agent Skill, die den Standard selbst nicht ändern. Eine Implementierung muss vorhandene Regel-IDs referenzieren und bekannte Einschränkungen dokumentieren.

## Erwartungen an das Review

Wir empfehlen, dass eine normative Änderung im Normalfall diese Punkte enthält:

1. die Problembeschreibung,
2. das vorgeschlagene Verhalten,
3. konforme und nicht konforme Beispiele,
4. die Auswirkung auf die Kompatibilität,
5. Belege aus dem Korpus oder linguistische Belege, wenn zutreffend,
6. die Auswirkungen auf Validator und Skill,
7. Tests, wenn das Verhalten maschinell testbar ist.

Solange die Gruppe der Maintainer klein ist, gibt es keinen numerischen Schwellenwert für Abstimmungen. Wir empfehlen, dass Maintainer bei umstrittenen normativen Entscheidungen die Begründung im Vorschlag oder im Pull Request dokumentieren.

## Stabilität der Regel-IDs

Veröffentlichte Regel-IDs sind öffentliche Kennungen. Nummerieren Sie eine Regel nicht neu, nur um die Gliederung optisch zu verbessern.

Wenn Sie eine Regel entfernen, reservieren Sie ihre ID und kennzeichnen Sie die Regel als abgekündigt. Wenn Sie eine Regel teilen, behalten Sie nach Möglichkeit die ursprüngliche ID. Fügen Sie neue IDs nur für wirklich neue normative Einheiten hinzu.

## Kompatibilität

`VERSIONING.md` definiert die Regeln für Kompatibilität und Versionierung.

## Releases

Verwenden Sie `RELEASE-CHECKLIST.md`. Ein Release muss diese Prüfungen bestehen: die Testsuite des Repositorys, die Synchronisierung des Skills, die Validierung der strukturierten Daten und die Integritätsprüfung des Release-Manifests.

## Sicherheit und unsicheres Verhalten

Das Projekt ist eine Sprachspezifikation und ein Werkzeug zur Textanalyse. Ein Beitrag darf keinen verborgenen Netzwerkzugriff, keine Erfassung von Zugangsdaten, keine Telemetrie und keine automatische Ausführung des analysierten Texts hinzufügen.

Werkzeuge für das Korpus dürfen ausdrücklich deklarierte öffentliche Quellen für eine vorübergehende Analyse herunterladen. Sie dürfen keine unbearbeiteten Korpora von Dritten in das Repository übernehmen, außer wenn die Rechte zur Weitergabe ausdrücklich bestehen.

## Lexikalische Änderungen

Das zentrale STG-DE-Wörterbuch ist ein domänenübergreifendes kontrolliertes Vokabular. Es ist keine Sammlung aller Wörter, die in deutscher Dokumentation häufig vorkommen.

Dieser Abschnitt definiert, wie Beitragende Personen Einträge vorschlagen und wie Maintainer Einträge prüfen, annehmen, einschränken, abkündigen oder ablehnen.

### Geltungsbereich

Wir empfehlen, dass der zentrale Kern Wörter enthält, die für kontrolliertes Deutsch in mehreren Domänen allgemein nützlich sind. Wir empfehlen auch Wörter, die notwendige grammatische oder technische Funktionen erfüllen.

Enge Terminologie für Produkte, Unternehmen, Branchen, Recht, Medizin, Software oder Ingenieurwesen gehört im Normalfall in die Projektterminologie (`.stg-de.yaml`). Sie gehört im Normalfall nicht in den zentralen Kern.

### Prinzipien für Entscheidungen

Maintainer bewerten einen Vorschlag in dieser Reihenfolge:

1. **Notwendigkeit der Bedeutung**: Benötigt STG-DE dieses Konzept in der zentralen Sprache?
2. **Domänenübergreifende Verwendbarkeit**: Ist das Konzept außerhalb einer engen Domäne nützlich?
3. **Risiko der Mehrdeutigkeit**: Lässt sich das Lemma auf eine klare kontrollierte Bedeutung und eine Wortart einschränken?
4. **Qualität der Ersetzung**: Genügt ein vorhandenes zugelassenes Wort?
5. **Korpusbelege**: Zeigen unabhängige Belege eine wiederkehrende reale Verwendung oder einen Bedarf?
6. **Konsistenz**: Passt der Eintrag zu vorhandenen lexikalischen Entscheidungen und Terminologiemustern?
7. **Lehrbarkeit**: Können eine schreibende Person und ein Agent die Entscheidung ohne verborgenen Kontext anwenden?

Häufigkeit allein genügt nicht für eine Aufnahme.

### Belegklassen

Belege können aus diesen Quellen kommen:

- `development_corpus`: Beobachtungen aus der Entwicklungspartition,
- `validation_corpus`: Beobachtungen aus der Validierungspartition,
- `external_public`: unabhängig zitierte öffentliche Beispiele,
- `linguistic_rationale`: ein grammatischer oder semantischer Bedarf, der nicht von der Häufigkeit abhängt,
- `user_report`: ein realer Fall aus Schreiben oder Validierung, den eine benutzende Person eingereicht hat.

Das Holdout-Korpus darf nicht zur Auswahl von neuem Kernvokabular für das Release dienen, das Sie mit diesem Holdout evaluieren.

### Arten von Vorschlägen

Ein lexikalischer Vorschlag hat eine dieser Aktionen:

- `add`: einen neuen zentralen Eintrag hinzufügen,
- `restrict`: eine kontrollierte Bedeutung, eine Wortart oder eine Form einschränken,
- `expand`: eine kontrollierte Bedeutung oder eine zulässige Form hinzufügen,
- `deprecate`: vorübergehend behalten, aber zur Ersetzung kennzeichnen,
- `prohibit`: einen Begriff oder eine Bedeutung in den Status „verboten“ oder „Review“ verschieben,
- `replace`: eine bevorzugte zentrale Alternative festlegen,
- `clarify`: die Dokumentation ändern, ohne das normative Verhalten zu ändern.

### Pflichtfelder eines Vorschlags

Verwenden Sie `proposals/LEX-CHANGE-TEMPLATE.yaml`. Validieren Sie den Vorschlag gegen `schemas/lexicon-proposal.schema.json`.

Jeder normative Vorschlag muss diese Angaben enthalten:

- ID und Aktion des Vorschlags,
- Lemma oder Begriff und Wortart,
- vorgeschlagene kontrollierte Bedeutung,
- Begründung,
- Risiko der Mehrdeutigkeit,
- geprüfte Alternativen,
- Belege aus mehreren Domänen und Quellen, wenn zutreffend,
- Auswirkung auf vorhandene Wörterbucheinträge,
- Beispiele,
- Auswirkung auf den Validator,
- endgültige Entscheidung und Begründung nach dem Review.

### Hinweise zur Aufnahme

Wir empfehlen für ein neues allgemeines Inhaltswort im Normalfall Belege aus mindestens zwei deutlich unterschiedlichen Domänen. Eine starke allgemeinsprachliche oder grammatische Begründung ist eine Alternative zu diesen Belegen.

Dieser Hinweis ist eine Empfehlung und keine automatische Regel zum Zählen von Stimmen. Maintainer können ein Wort ablehnen, auch wenn es in vielen Dokumenten vorkommt. Gründe für eine Ablehnung sind: Das Wort ist vage, polysem oder stilistisch. Oder ein vorhandenes kontrolliertes Wort drückt das Konzept besser aus.

Wir empfehlen, einen engen Begriff im Normalfall projektspezifisch zu halten, wenn eine dieser Bedingungen zutrifft:

- Der Begriff bezeichnet ein Produkt oder eine Komponente, die nur in einer Domäne vorkommt.
- Seine Bedeutung hängt von einem technischen Standard oder einer Organisation ab.
- Ein Projektglossar kann den Begriff definieren, ohne die Interoperabilität zu schwächen.
- Die Aufnahme des Begriffs erhöht hauptsächlich die Korpus-Abdeckung und nicht die Klarheit der Sprache.

### Richtlinie für Mehrdeutigkeit

Wenn ein Lemma mehrere übliche Bedeutungen hat, empfehlen wir eines dieser Ergebnisse:

1. Eine kontrollierte Bedeutung zulassen und die anderen Bedeutungen verbieten oder zum Review markieren.
2. Für unterschiedliche Konzepte unterschiedliche eindeutige Wörter verwenden.
3. Das Wort projektspezifisch halten.
4. Das Lemma für den zentralen Kern ablehnen.

Lassen Sie nicht mehrere Bedeutungen zu, nur weil diese Bedeutungen in der deutschen Gemeinsprache üblich sind.

### Richtlinie für Wortarten

Eine Zulassung gilt für eine bestimmte Wortart. Wenn ein Nomen zugelassen ist, ist dieselbe Oberflächenform nicht automatisch als Verb, Adjektiv oder andere Wortart zugelassen.

Die Morphologierichtlinie regelt die Flexionsformen. Eine Oberflächenform kann mit einem anderen kanonischen Lemma kollidieren. Diese Kollision muss nach ausdrücklichen Regeln für den lexikalischen Vorrang aufgelöst werden.

### Review-Status

Ein Vorschlag durchläuft diese Status:

`draft` → `evidence_ready` → `review` → `accepted` | `rejected` | `deferred`

Angenommene normative Vorschläge müssen Tests oder Aktualisierungen der Validierung enthalten, wenn das Verhalten maschinell prüfbar ist.

### Behandlung in Releases

- Solange STG-DE vor 1.0 ist, können Ergänzungen und Klarstellungen im Normalfall in einem Minor-Release erscheinen.
- Einschränkungen, Verbote und Änderungen kontrollierter Bedeutungen müssen in `CHANGELOG.md` ausdrücklich genannt sein.
- Nach 1.0 gilt für inkompatible lexikalische Änderungen die Kompatibilitätsrichtlinie aus `VERSIONING.md`.
- Das Release-Manifest dokumentiert die exakten Wörterbuchartefakte, auf die sich Aussagen zur Konformität beziehen.

### Integrität des Korpus

Stimmen Sie das Wörterbuch nicht mit einem Holdout-Set ab, um danach dasselbe Holdout als unabhängigen Beleg zu melden.

Wenn eine Korpusanalyse eine Liste unbekannter Token erzeugt, verwenden Sie diese Liste als Warteschlange für das Review. Wandeln Sie unbekannte Token nicht automatisch in zugelassene Einträge um.

### Ausweg über Projektterminologie

Projektterminologie ist ein vollwertiger Teil von STG-DE. Wenn Maintainer einen Begriff für den zentralen Kern ablehnen, ist der Begriff in technischen Inhalten nicht verboten.

Ein präziser Domänenbegriff kann über `.stg-de.yaml` gültig sein. Das gilt auch, wenn wir empfehlen, ihn nie in das allgemeine STG-DE-Wörterbuch aufzunehmen.

## Externes Review

Für 1.0 empfehlen wir ein Review durch Personen mit Fachwissen in technischer Redaktion, in Linguistik oder in beiden Bereichen. Für 1.0 empfehlen wir auch, Belege für eine Verwendung außerhalb des ursprünglichen Entwicklungskontexts zu dokumentieren. Automatisierte CI allein kann diese Kriterien nicht erfüllen.
