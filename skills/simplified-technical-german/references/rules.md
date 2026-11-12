# STG-DE-Schreibregeln

Erzeugt aus dem kanonischen Verzeichnis `rules/`. Bearbeiten Sie diese Datei nicht direkt.

---

<!-- source: rules/01-words.md -->

# Abschnitt 1 — Wörter und Terminologie

## STG-1.1 — Zulässiger Wortschatz

**Level:** `MUST`

Verwenden Sie nur Wörter, die zu mindestens einer freigegebenen Klasse gehören:

1. ein Wort im zentralen STG-Lexikon,
2. ein freigegebenes technisches Substantiv,
3. ein freigegebenes technisches Verb,
4. gesperrter externer Text, wenn eine Änderung des Textes nicht zulässig ist.

Unbekannte allgemeinsprachliche Wörter sind nicht automatisch technische Terme.

<!-- stg-lint: off -->
**Nicht STG**

> Die Komponente ist irgendwie falsch positioniert.
<!-- stg-lint: on -->

**STG**

> Die Komponente ist in der falschen Position.

## STG-1.2 — Wortart

**Level:** `MUST`

Verwenden Sie ein freigegebenes lexikalisches Element nur mit der freigegebenen Wortart. Die deutsche Wortbildung erzeugt nicht automatisch einen neuen freigegebenen Eintrag.

Wenn `Prüfung` als Substantiv freigegeben ist, ist `prüfen` nicht automatisch als Verb freigegeben. Jede Kombination aus Lexem und Wortart ist ein eigener Wörterbucheintrag. Eine Ausnahme gilt, wenn das Lexikon die Einträge ausdrücklich verknüpft.

## STG-1.3 — Kontrollierte Bedeutung

**Level:** `MUST`

Verwenden Sie ein freigegebenes Wort nur mit einer freigegebenen Bedeutung. Wenn die beabsichtigte Bedeutung nicht freigegeben ist, wählen Sie ein anderes freigegebenes Wort oder formulieren Sie den Satz neu.

**Beispiel:** Wenn `lösen` nur für das Lösen einer mechanischen Verbindung freigegeben ist, verwenden Sie `lösen` nicht für `ein Problem lösen`. Eine Ausnahme gilt, wenn diese zweite Bedeutung separat freigegeben ist.

## STG-1.4 — Zulässige Flexionsformen

**Level:** `MUST`

Verwenden Sie nur grammatisch korrekte Formen, die das Schema des Wörterbuchs für den Eintrag zulässt.

Für Deutsch darf das Lexikon diese Angaben festlegen:

- Genus und Plural von Substantiven,
- Flexionsklasse und Regel für die Steigerung von Adjektiven,
- Formen von Verben nach Person und Numerus,
- Imperativform,
- Partizipformen,
- trennbares Präfix,
- Wahl des Hilfsverbs, wenn diese Wahl relevant ist.

Eine generierte Form ist nur zulässig, wenn die Form der deklarierten Morphologie folgt. Zusätzlich darf das Regelwerk die syntaktische Verwendung der Form nicht verbieten.

## STG-1.5 — Technische Substantive

**Level:** `MUST`

Ein technisches Substantiv ist ein Term für ein definiertes Konzept in einem technischen Fachgebiet. Verwenden Sie ein Wort oder einen Mehrwortterm nur dann als technisches Substantiv, wenn zwei Bedingungen gelten. Das Wort passt zu einer freigegebenen Kategorie für technische Substantive. Die anwendbare Terminologiequelle akzeptiert das Wort.

Das Kategoriemodell steht in `dictionary/technical-nouns.yaml`.

## STG-1.6 — Nicht-zentrale Wörter als technische Terme

**Level:** `MUST`

Ein Wort, das im zentralen Lexikon nicht freigegeben ist, dürfen Sie nur als Teil eines freigegebenen technischen Terms oder einer geschützten externen Benennung verwenden.

Ein Wort kann in einem technischen Term vorkommen. Dieses Vorkommen gibt Ihnen keine Erlaubnis, das Wort mit der normalen allgemeinsprachlichen Bedeutung zu verwenden.

## STG-1.7 — Technisches Substantiv ist nicht automatisch Verb

**Level:** `MUST`

Bilden Sie aus einem technischen Substantiv kein Verb. Eine Ausnahme gilt, wenn das Verb selbst als technisches Verb oder als zentraler lexikalischer Eintrag freigegeben ist.

<!-- stg-lint: off -->
**Nicht STG**

> Ölen Sie die Führung.
<!-- stg-lint: on -->

**STG**

> Tragen Sie Öl auf die Führung auf.

Wenn `ölen` ausdrücklich als technisches Verb des Projekts freigegeben ist, hat der Eintrag des Projekts Vorrang.

## STG-1.8 — Offizielle technische Benennungen

**Level:** `MUST`

Verwenden Sie die technische Benennung, die eine dieser Quellen freigibt: Unternehmen, Produkt, Branche, Vertrag, Zeichnung, Ersatzteilkatalog, Datenmodell oder Terminologiedatenbank. Ersetzen Sie eine offizielle Benennung nicht nur mit dem Ziel, die Benennung zu kürzen.

## STG-1.9 — Neue technische Benennungen kurz halten

**Level:** `SHOULD`

Wenn keine freigegebene technische Benennung existiert, empfehlen wir die kürzeste Benennung, die das Konzept eindeutig kennzeichnet.

Für ein neu gebildetes deutsches Kompositum empfehlen wir höchstens drei bedeutungstragende lexikalische Bestandteile, wenn diese Zahl technisch ausreicht. Wenn mehr Bestandteile notwendig sind, wenden Sie die Regeln für Komposita in Abschnitt 2 an.

Entfernen Sie keine unterscheidende Information, die für die technische Korrektheit notwendig ist.

## STG-1.10 — Keine regionale Sprache, Umgangssprache oder Jargon

**Level:** `MUST_NOT`

Verwenden Sie diese Ausdrücke nicht als allgemeine technische Sprache: regionale Ausdrücke, Umgangssprache, Werkstattjargon, Internetjargon und unerklärten Fachjargon.

Projektspezifische technische Terme sind nur nach einer Freigabe der Terminologie zulässig.

<!-- stg-lint: off -->
**Nicht STG**

> Wenn das Update fehlschlägt, darf das Gerät nicht gebrickt werden.
<!-- stg-lint: on -->

**STG**

> Wenn das Update fehlschlägt, darf das Gerät nicht funktionsunfähig werden.

Empfehlung: Nennen Sie die genaue Fehlerbedingung, wenn die Fehlerbedingung bekannt ist.

## STG-1.11 — Ein Konzept, eine Benennung

**Level:** `MUST`

Verwenden Sie für dasselbe Konzept im definierten Geltungsbereich des Dokuments immer dieselbe freigegebene technische Benennung.

Verwenden Sie für dieselbe Komponente nicht abwechselnd Synonyme wie `Steuergerät`, `Controller` und `Regler`. Eine Ausnahme gilt, wenn das Terminologiemodell diese Benennungen als unterschiedliche Konzepte definiert.

## STG-1.12 — Technische Verben

**Level:** `MUST`

Ein technisches Verb bezeichnet einen definierten technischen Prozess oder eine definierte technische Handlung in einem Fachgebiet. Verwenden Sie ein technisches Verb nur, wenn alle diese Bedingungen gelten:

1. Die Handlung hat eine fachspezifische Bedeutung.
2. Die anwendbare Terminologiequelle gibt das Verb frei.
3. Ein einfacheres zentrales STG-Verb drückt dieselbe technische Handlung nicht genau aus.

Das Kategoriemodell steht in `dictionary/technical-verbs.yaml`.

## STG-1.13 — Technisches Verb ist nicht automatisch Substantiv

**Level:** `MUST`

Nominalisieren Sie ein freigegebenes technisches Verb nicht, um das Ergebnis als freigegebenes technisches Substantiv zu verwenden. Eine Ausnahme gilt, wenn das Substantiv separat freigegeben ist.

Diese Regel ist für Deutsch wichtig. Die produktive Nominalisierung kann formal korrekte, aber unkontrollierte Terme erzeugen.

<!-- stg-lint: off -->
**Nicht STG**

> Das Reamen des Lochs erfolgt danach.
<!-- stg-lint: on -->

**STG**

> Reiben Sie danach das Loch auf.

Wenn `Reiben` in einer Überschrift ein offizieller Prozessname ist, geben Sie `Reiben` als Eintrag für ein technisches Substantiv frei.

## STG-1.14 — Deutsche Standardschreibung

**Level:** `MUST`

Verwenden Sie das deklarierte Rechtschreibprofil für Deutsch. Das Standardprofil `de-DE` folgt der amtlichen deutschen Rechtschreibung von 2024.

Für `de-DE` gilt:

- Behalten Sie `ä`, `ö`, `ü` und `ß`, wenn die Standardschreibung diese Zeichen verlangt.
- Ersetzen Sie diese Zeichen nicht durch `ae`, `oe`, `ue` oder `ss`. Eine Ausnahme gilt, wenn eine technische Kennung oder eine Systemgrenze den Ersatz verlangt.
- Schreiben Sie deutsche Substantive groß.
- Behalten Sie die offizielle Schreibung von Produktnamen, Kennungen, Zeichenketten der Benutzeroberfläche und zitiertem Text.

Ein Projekt darf `de-CH` oder ein anderes freigegebenes Profil deklarieren. Wir empfehlen, in einem Dokument keine Profile zu mischen.

---

<!-- source: rules/02-compounds-and-terms.md -->

# Abschnitt 2 — Komposita und Mehrwortterme

Die deutsche Fachsprache verwendet Komposita in großem Umfang. Deshalb definiert STG-DE eigene Regeln für die kontrollierte Verwendung von Komposita.

## STG-2.1 — Semantische Dichte technischer Benennungen begrenzen

**Level:** `MUST`

Eine neu gebildete technische Benennung muss verständlich sein, ohne dass der Leser mehrere mögliche interne Beziehungen zwischen den Bestandteilen erschließen muss.

Verwenden Sie diese Methoden in dieser Reihenfolge:

1. Verwenden Sie den freigegebenen offiziellen Term, wenn ein solcher Term existiert. Die Länge des Terms ist in diesem Fall nicht relevant.
2. Für einen neuen Term empfehlen wir höchstens drei bedeutungstragende lexikalische Bestandteile.
3. Wenn eine längere Benennung notwendig ist, verwenden Sie eine grammatisch klare Wortgruppe oder ein strukturiertes Kompositum.
4. Verwenden Sie einen Bindestrich, wenn der Bindestrich die Grenzen in einem langen Kompositum deutlich klarer macht. Verwenden Sie einen Bindestrich auch, wenn die amtliche Rechtschreibung den Bindestrich zur Klarheit verlangt oder erlaubt.
5. Bilden Sie keine Kette von Bestimmungswörtern, nur damit der Ausdruck ein orthografisches Wort bleibt.

<!-- stg-lint: off -->
**Nicht STG**

> Kraftstoffhauptpumpenausgangsdruckprüfanschlussabdeckung
<!-- stg-lint: on -->

**STG**

> Abdeckung des Prüfanschlusses am Ausgang der Hauptkraftstoffpumpe

Wenn das lange Kompositum der offizielle Name des Teils ist, behalten Sie den offiziellen Namen. Definieren Sie dann nach STG-2.2 eine kontrollierte kürzere Form.

## STG-2.2 — Lange offizielle Benennung zuerst vollständig

**Level:** `MUST`

Wenn eine offizielle technische Benennung lang ist, gilt:

1. Schreiben Sie beim ersten Vorkommen die vollständige offizielle Benennung.
2. Definieren Sie eine freigegebene Kurzform oder Abkürzung, wenn die Kurzform hilfreich ist.
3. Verwenden Sie danach im deklarierten Geltungsbereich nur diese Kurzform.

Legen Sie für denselben Term nicht mehrere Kurzformen fest.

**Beispiel**

> Die **zentrale Steuerung der Kühlmittelpumpe (Kühlmittelsteuerung)** überwacht den Druck. Die **Kühlmittelsteuerung** schaltet die Pumpe bei Überdruck aus.

## STG-DE-2.1 — Deutsche Komposita als Terminologieobjekte

**Level:** `MUST`

Betrachten Sie ein deutsches Kompositum als Terminologieobjekt, nicht nur als Verbindung von freigegebenen allgemeinen Wörtern.

Für jedes freigegebene Kompositum empfehlen wir, diese Angaben in einer Terminologiedatenbank zu speichern:

- kanonische Schreibung,
- Kennung des Konzepts,
- grammatisches Genus,
- Pluralform,
- freigegebene Kurzform, wenn eine Kurzform existiert,
- Zerlegung in bedeutungstragende Bestandteile, wenn diese Zerlegung für Validatoren hilfreich ist.

Die Freigabe von `Druck`, `Regler` und `Ventil` gibt `Druckregelventil` nicht automatisch als technischen Term frei.

## STG-DE-2.2 — Bindestriche nicht zur scheinbaren Verkürzung verwenden

**Level:** `MUST_NOT`

Verwenden Sie Bindestriche nicht nur mit dem Ziel, eine komplexe Benennung für die Regel zur Wortzählung kürzer erscheinen zu lassen. Ein Kompositum mit Bindestrich zählt als ein orthografisches Wort. Das Kompositum erhält trotzdem eine Prüfung auf die Komplexität von Komposita.

## STG-DE-2.3 — Abkürzungen sparsam und stabil verwenden

**Level:** `MUST`

Verwenden Sie eine Abkürzung nur, wenn die Abkürzung offiziell ist oder ausdrücklich eingeführt ist. Schreiben Sie beim ersten Vorkommen den vollständigen Term und danach die Abkürzung in Klammern. Eine Ausnahme gilt, wenn das Projekt die Abkürzung allgemein verlangt.

Verwenden Sie nach der Einführung nicht abwechselnd mehrere Abkürzungen oder mehrere Kurzformen.

---

<!-- source: rules/03-verbs.md -->

# Abschnitt 3 — Verben

## STG-3.1 — Nur freigegebene Verbformen

**Level:** `MUST`

Verwenden Sie nur Verbformen, die der lexikalische Eintrag und dieser Abschnitt zulassen. Die deutsche Konjugation ist produktiv. Eine grammatisch mögliche Form ist aber nicht automatisch in STG freigegeben.

## STG-3.2 — Kontrollierte Tempora und Modi

**Level:** `MUST`

Verwenden Sie diese Standardformen:

### Anleitungen

- formeller Imperativ: `Entfernen Sie ...`
- Infinitiv nur in einer freigegebenen Infinitivkonstruktion, nicht als Standardstil für Anweisungen.

### Beschreibungen

- Präsens für derzeitige Zustände, Funktionen und allgemeine technische Fakten,
- Präteritum oder Perfekt nur, wenn der Text ein vergangenes Ereignis berichten muss,
- Präsens mit expliziter Zeitangabe für geplante zukünftige Zustände, wenn diese Form möglich ist.

Vermeiden Sie das Futur I, wenn das Präsens gleich klar ist.

<!-- stg-lint: off -->
**Nicht STG**

> Der Test wird morgen durchgeführt werden.
<!-- stg-lint: on -->

**STG**

> Das Personal prüft das System morgen.

Alternative, wenn der Akteur nicht relevant ist, aber der Zeitplan die zentrale Information ist:

> Der Test ist für morgen geplant.

## STG-3.3 — Partizip II für Zustand oder Attribut

**Level:** `MUST`

Ein Partizip II darf als Adjektiv oder als Beschreibung eines Zustands stehen, wenn das Partizip einen Zustand beschreibt und keine ausgelassene Handlung.

**STG**

> Die Abdeckung ist geschlossen.

**STG**

> Prüfen Sie die gereinigte Fläche.

Wenn der Satz beschreibt, wer eine Handlung ausführt, verwenden Sie das Aktiv.

## STG-3.4 — Keine unnötigen Hilfsverbketten

**Level:** `MUST_NOT`

Verwenden Sie keine komplexen Konstruktionen mit Hilfsverben oder Modalverben, wenn ein direktes Verb dieselbe Information ausdrückt.

<!-- stg-lint: off -->
**Nicht STG**

> Die Dichtung muss ersetzt worden sein, bevor die Prüfung durchgeführt werden kann.
<!-- stg-lint: on -->

**STG**

> Ersetzen Sie die Dichtung vor der Prüfung.

Wenn der abgeschlossene Zustand selbst die Anforderung ist:

> Vor der Prüfung muss die Dichtung ersetzt sein.

## STG-3.5 — Keine englische `-ing`-Sonderregel; kontrolliere deutsche Nominalisierung

**Level:** `MUST`

Das Deutsche hat keine direkte Entsprechung zur Mehrdeutigkeit der englischen Form auf `-ing`. Das entsprechende Risiko im Deutschen ist die produktive Nominalisierung.

Verwenden Sie Nominalisierungen nur, wenn die Nominalisierung eines dieser Elemente bezeichnet: ein freigegebenes technisches Konzept, eine Überschrift im Dokument, einen Prozessnamen oder ein Ergebnis. Für Handlungen in Sätzen empfehlen wir ein finites Verb oder einen Imperativ.

<!-- stg-lint: off -->
**Nicht STG**

> Nach Durchführung der Reinigung erfolgt die Prüfung der Oberfläche.
<!-- stg-lint: on -->

**STG**

> Reinigen Sie die Oberfläche. Prüfen Sie danach die Oberfläche.

## STG-3.6 — Aktiv bevorzugen

**Level:** `MUST`

Verwenden Sie das Aktiv, wenn der Akteur bekannt ist oder Sie den Akteur korrekt nennen können.

Verwenden Sie in Anleitungen den Imperativ statt Anweisungen im Passiv.

<!-- stg-lint: off -->
**Nicht STG**

> Die Sicherung wird entfernt.
<!-- stg-lint: on -->

**STG**

> Entfernen Sie die Sicherung.

In Beschreibungen ist das Passiv nur in diesen Fällen zulässig: Der Akteur ist wirklich unbekannt. Der Akteur ist für die technische Bedeutung nicht relevant. Eine anwendbare rechtliche Regel oder Publikationsregel verlangt, dass der Text den Akteur nicht nennt.

Verwechseln Sie einen Zustand nicht mit dem Passiv:

> Die Sicherung ist entfernt.

Dieser Satz kann eine gültige Beschreibung eines Zustands sein, wenn `entfernt` den geforderten Zustand beschreibt.

## STG-3.7 — Handlungen mit direkten Verben ausdrücken

**Level:** `MUST`

Wenn ein freigegebenes direktes Verb die Handlung ausdrückt, verwenden Sie dieses Verb statt einer Konstruktion mit vielen Substantiven.

<!-- stg-lint: off -->
**Nicht STG**

> Führen Sie eine Prüfung des Steckers durch.
<!-- stg-lint: on -->

**STG**

> Prüfen Sie den Stecker.

<!-- stg-lint: off -->
**Nicht STG**

> Nehmen Sie eine Einstellung des Drucks vor.
<!-- stg-lint: on -->

**STG**

> Stellen Sie den Druck ein.

## STG-DE-3.1 — Trennbare Verben prüfen und begrenzen

**Level:** `SHOULD`

Trennbare Verben sind zulässig, wenn das trennbare Verb das freigegebene technische oder allgemeine Verb ist. Wir empfehlen, die Satzklammer kurz zu halten.

Wenn zwischen dem finiten Verb und dem trennbaren Präfix mehr als ungefähr 12 Wörter stehen, empfehlen wir, den Satz neu zu formulieren. Eine Ausnahme gilt, wenn die Terminologie oder die Syntax die längere Satzklammer deutlich besser macht.

<!-- stg-lint: off -->
**Schwer lesbar**

> Schalten Sie nach dem Ende der automatischen Kalibrierung die externe 24-V-Stromversorgung am hinteren Bedienfeld vollständig aus.
<!-- stg-lint: on -->

**Besser**

> Schalten Sie nach der Kalibrierung die externe 24-V-Stromversorgung aus.

## STG-DE-3.2 — Modalität eindeutig kodieren

**Level:** `MUST`

Verwenden Sie die Modalität konsistent:

| Bedeutung | STG-Form |
|---|---|
| Verbindliche Handlung in einer Anleitung | Imperativ |
| Verbindlicher Zustand oder verbindliche Anforderung | `muss` |
| Verbot | `darf nicht` oder negativer Imperativ, abhängig von der Textart |
| Erlaubnis | `darf` |
| Physische oder technische Fähigkeit oder tatsächliche Möglichkeit | `kann` |
| Empfehlung | ausdrückliche Formulierung als Empfehlung, nur wenn Empfehlungen zulässig sind |

Verwenden Sie nicht `soll`, `sollte` oder `müsste`, wenn die beabsichtigte Stärke verbindlich, erlaubt oder nur möglich ist.

<!-- stg-lint: off -->
**Mehrdeutig**

> Die Schraube sollte ersetzt werden.
<!-- stg-lint: on -->

Die möglichen Umformulierungen in STG hängen von der Absicht ab:

> Ersetzen Sie die Schraube.  
> Die Schraube muss ersetzt sein.  
> Wir empfehlen, die Schraube zu ersetzen.

Wenn die beabsichtigte Modalität unbekannt ist, geben Sie `NEEDS_MODALITY_INPUT` zurück.

## STG-DE-3.3 — `werden` restriktiv verwenden

**Level:** `SHOULD_NOT`

Wir empfehlen, `werden` nicht zu verwenden, wenn `werden` nur ein Passiv oder ein Futur I bildet. Für eine tatsächliche Änderung eines Zustands dürfen Sie `werden` verwenden, wenn diese Bedeutung klar ist.

**STG**

> Das Gehäuse wird warm.

<!-- stg-lint: off -->
**Nicht bevorzugt**

> Die Leitung wird vom Steuergerät überwacht.
<!-- stg-lint: on -->

**STG**

> Das Steuergerät überwacht die Leitung.

---

<!-- source: rules/04-sentences.md -->

# Abschnitt 4 — Sätze

## STG-4.1 — Kurze, eindeutige Sätze

**Level:** `MUST`

Schreiben Sie kurze Sätze mit einer primären Aussage. In beschreibendem Text empfehlen wir ein Hauptthema je Satz. Verdichten Sie nicht mehrere unabhängige Fakten in einem Satz.

<!-- stg-lint: off -->
**Nicht STG**

> Der Sensor sitzt am Gehäuse, misst den Druck und sendet die Werte an das Steuergerät, das bei einem Grenzwertfehler die Pumpe abschaltet.
<!-- stg-lint: on -->

**STG**

> Der Sensor sitzt am Gehäuse. Der Sensor misst den Druck. Das Steuergerät empfängt die Messwerte. Bei einem Grenzwertfehler schaltet das Steuergerät die Pumpe aus.

## STG-4.2 — Keine bedeutungstragenden Auslassungen

**Level:** `MUST_NOT`

Lassen Sie kein Subjekt, kein Objekt, kein Verb, keinen Artikel und keinen Bezug aus, wenn die Auslassung eine Mehrdeutigkeit erzeugen kann. Verwenden Sie keine Fragmente im Telegrammstil als normalen Fließtext.

<!-- stg-lint: off -->
**Nicht STG**

> Schalter auf EIN.
<!-- stg-lint: on -->

**STG**

> Stellen Sie den Schalter auf EIN.

Überschriften, Tabellenzellen, Beschriftungen und andere kontrollierte Fragmente können nach dem jeweiligen Inhaltsmodell von dieser Regel ausgenommen sein.

## STG-4.3 — Vertikale Listen für komplexe Aufzählungen

**Level:** `MUST`

Verwenden Sie eine vertikale Liste, wenn ein Satz viele parallele Elemente, Bedingungen oder Handlungen enthält.

Regeln:

- Leiten Sie die Liste mit einem grammatisch vollständigen Einleitungssatz und einem Doppelpunkt ein.
- Halten Sie alle Listenelemente grammatisch parallel.
- Mischen Sie in derselben Liste keine Befehle aus Anleitungen und keine beschreibenden Aussagen.
- Schließen Sie ein Listenelement, das ein vollständiger Satz ist, mit einem Punkt ab.
- Verwenden Sie Kommas oder Semikolons nicht als Endzeichen, nur um Listenelemente zu verketten.

## STG-4.4 — Logische Verknüpfungen explizit angeben

**Level:** `MUST`

Verwenden Sie stabile Verknüpfungswörter, wenn die logische Beziehung zwischen Sätzen wichtig ist.

Zu den bevorzugten kontrollierten Verknüpfungswörtern gehören:

- `und` — Addition,
- `aber` — Gegensatz,
- `dann` / `danach` — Reihenfolge,
- `deshalb` — Folge,
- `weil` — Ursache,
- `wenn` — Bedingung,
- `bevor` — früheres Ereignis,
- `während` — gleichzeitiger Zeitraum.

Variieren Sie Verknüpfungswörter nicht nur aus stilistischen Gründen.

## STG-4.5 — Artikel und Demonstrativa eindeutig verwenden

**Level:** `MUST`

Verwenden Sie Artikel und Demonstrativa nach der deutschen Grammatik. Verwenden Sie Artikel und Demonstrativa, um den Status des Bezugs eindeutig anzugeben. Stellen Sie die Kongruenz in Kasus, Genus und Numerus sicher.

Verwenden Sie kein alleinstehendes Demonstrativpronomen, wenn mehr als ein Bezugswort möglich ist. Wir empfehlen ein Demonstrativadjektiv mit Substantiv oder die Wiederholung des technischen Substantivs.

<!-- stg-lint: off -->
**Mehrdeutig**

> Entfernen Sie den Sensor aus dem Halter. Dieser ist beschädigt.
<!-- stg-lint: on -->

**STG**

> Entfernen Sie den Sensor aus dem Halter. Der Sensor ist beschädigt.

oder

> Entfernen Sie den Sensor aus dem Halter. Der Halter ist beschädigt.

## STG-DE-4.1 — Nebensatzverschachtelung begrenzen

**Level:** `MUST`

Verschachteln Sie in anleitendem Text und in Sicherheitshinweisen keine Nebensätze in Nebensätzen. In beschreibendem Text ist eine Ebene der Unterordnung das Standardmaximum.

Formulieren Sie tiefere Strukturen als getrennte Sätze neu.

## STG-DE-4.2 — Pronomen nur mit eindeutigem Bezug

**Level:** `MUST`

Ein Pronomen muss im lokalen Kontext genau ein plausibles Bezugswort haben. Wenn das Pronomen auf mehr als ein Substantiv verweisen kann, wiederholen Sie das Substantiv.

<!-- stg-lint: off -->
**Mehrdeutig**

> Verbinden Sie den Sensor mit dem Adapter, wenn er trocken ist.
<!-- stg-lint: on -->

**STG**

> Wenn der Sensor trocken ist, verbinden Sie den Sensor mit dem Adapter.

## STG-DE-4.3 — `man` nicht als technischer Akteur verwenden

**Level:** `MUST_NOT`

Verwenden Sie das Indefinitpronomen `man` nicht, um den Akteur in technischen Anweisungen oder Anforderungen zu verbergen oder zu verallgemeinern.

Verwenden Sie stattdessen:

- den Imperativ, wenn der Leser handelt,
- eine benannte Rolle, wenn ein festgelegter Akteur handelt,
- das verantwortliche System oder die verantwortliche Komponente, wenn das System oder die Komponente automatisch handelt.

## STG-DE-4.4 — Negationsbereich eindeutig festlegen

**Level:** `MUST`

Positionieren Sie `nicht`, `kein` und andere negative Ausdrücke so, dass nur eine Interpretation plausibel ist. Wenn der Bereich der Negation komplex ist, formulieren Sie den Satz mit einer expliziten Bedingung neu.

<!-- stg-lint: off -->
**Mehrdeutig**

> Schalten Sie das Gerät nicht mit geöffnetem Gehäuse ein.
<!-- stg-lint: on -->

**STG**

> Wenn das Gehäuse offen ist, schalten Sie das Gerät nicht ein.

Vermeiden Sie doppelte Negation.


## STG-DE-4.5 — Pronominaladverbien nur mit eindeutigem Bezug

**Level:** `MUST`

Deutsche Pronominaladverbien wie `dabei`, `dazu`, `daraus`, `davon`, `darüber`, `dafür` und `hierfür` können einen Bezug verdichten. Der Bezug kann auf ein Objekt, eine Handlung, eine Ursache, einen Zweck oder einen vorherigen Satz verweisen. Verwenden Sie eine solche Form nur, wenn genau ein lokales Bezugswort und genau eine semantische Beziehung möglich sind.

Wiederholen Sie beim strengen Schreiben nach `STG-C-core` das technische Substantiv, die Handlung oder die Bedingung, wenn der Bezug mehrere Interpretationen zulässt.

<!-- stg-lint: off -->
**Mehrdeutig**

> Verbinden Sie den Sensor mit dem Adapter. Dabei darf die Dichtung nicht beschädigt werden.
<!-- stg-lint: on -->

`Dabei` kann auf das Verbinden, auf den Adapter oder auf die vollständige vorherige Situation verweisen.

**STG**

> Wenn Sie den Sensor mit dem Adapter verbinden, beschädigen Sie die Dichtung nicht.

Wir empfehlen, dass ein Validator ein ungeklärtes Pronominaladverb als `NEEDS_REFERENCE_INPUT` meldet. Der Validator darf das Bezugswort nicht erfinden.

---

<!-- source: rules/05-procedures.md -->

# Abschnitt 5 — Anleitungen

## STG-5.1 — Maximal 20 Wörter je Satz in anleitendem Text

**Level:** `MUST`

Ein Satz in einem anleitenden Text hat maximal **20 Wörter** nach den Zählregeln in Abschnitt 8. Diese Grenze gilt auch für eine Anweisung in einem Sicherheitshinweis.

Ein Hinweis ist beschreibender Text. Ein Satz in einem Hinweis darf maximal 25 Wörter haben.

## STG-5.2 — Eine Anweisung je Satz

**Level:** `MUST`

Schreiben Sie eine Anweisung je Satz.

Mehr als eine Handlung in einem Satz ist nur zulässig, wenn die Handlungen eine dieser Bedingungen erfüllen:

- Die Handlungen finden gleichzeitig statt.
- Die Handlungen sind ein einziger untrennbarer physischer Vorgang.
- Eine Handlung ist eine direkte Abnahme- oder Ergebnisaussage, die zu demselben Arbeitsschritt gehört.

<!-- stg-lint: off -->
**Nicht STG**

> Öffnen Sie die Abdeckung und entfernen Sie danach den Filter.
<!-- stg-lint: on -->

**STG**

> 1. Öffnen Sie die Abdeckung.  
> 2. Entfernen Sie den Filter.

**Zulässige gleichzeitige Handlung**

> Halten Sie die Leitung fest und lösen Sie die Mutter.

## STG-5.3 — Anweisungen in einer festgelegten Anredeform

**Level:** `MUST`

Schreiben Sie erforderliche Handlungen des Lesers in der Anredeform des Projekts. Das Projekt legt die Anredeform mit der Einstellung `anrede` in `.stg-de.yaml` fest.

| `anrede` | Form der Anweisung | Beispiel |
|---|---|---|
| `sie` (Standard) | formaler Imperativ mit „Sie“ | „Prüfen Sie die Leitung auf Schäden.“ |
| `du` | Imperativ der 2. Person Singular | „Prüfe die Leitung auf Schäden.“ |
| `infinitiv` | Infinitiv am Satzende | „Leitung auf Schäden prüfen.“ |

Wenn das Projekt keine Anredeform festlegt, gilt `sie`.

**STG** (`anrede: sie`)

> Entfernen Sie die Abdeckung.  
> Stellen Sie den Druck auf 2 bar ein.  
> Prüfen Sie die Leitung auf Schäden.

Ein kontrollierter Dokumentsatz verwendet genau eine Anredeform. Anweisungen, Pronomen und Possessivpronomen der Anrede folgen dieser Form. Ein Dokumentsatz schreibt „du“ oder „Du“ einheitlich.

<!-- stg-lint: off -->
**Nicht STG**

> Prüfen Sie den Druck. Wenn du fertig bist, schließe das Ventil.
<!-- stg-lint: on -->

Verwenden Sie für eine Anweisung kein Passiv, kein `soll` und keine Fragmente, die nur aus Substantiven bestehen. Diese Vorgabe gilt für jede Anredeform.

Der Änderungsvorschlag `proposals/STG-2026-001-anrede.md` begründet diese Regel.

## STG-5.4 — Bedingung vor Anweisung

**Level:** `MUST`

Wenn der Leser eine Bedingung vor einer Handlung kennen muss, schreiben Sie die Bedingung zuerst. Trennen Sie die Bedingung mit einem Komma von der Anweisung.

<!-- stg-lint: off -->
**Nicht STG**

> Entfernen Sie die Sicherung, wenn die Anzeige rot ist.
<!-- stg-lint: on -->

**STG**

> Wenn die Anzeige rot ist, entfernen Sie die Sicherung.

## STG-5.5 — Hinweise enthalten keine Anweisungen

**Level:** `MUST`

Ein Hinweis darf nur nützlichen Kontext geben. Ein Hinweis darf diese Inhalte nicht enthalten:

- eine Anweisung,
- eine Schutzhandlung,
- eine verbindliche Anforderung,
- ein Abnahmekriterium,
- einen Grenzwert oder eine Toleranz, die für die korrekte Ausführung des Arbeitsschritts erforderlich ist.

Prüfung: Entfernen Sie jeden Hinweis aus der Anleitung. Der Leser muss die Anleitung auch ohne Hinweise korrekt und sicher ausführen können.

<!-- stg-lint: off -->
**Nicht STG**

> HINWEIS: Ziehen Sie die Schraube mit 8 Nm fest.
<!-- stg-lint: on -->

**STG**

> Ziehen Sie die Schraube mit 8 Nm fest.

---

<!-- source: rules/06-descriptions.md -->

# Abschnitt 6 — Beschreibungen

## STG-6.1 — Informationen schrittweise geben

**Level:** `MUST`

Nennen Sie zuerst ein Thema. Geben Sie danach verwandte Informationen in einer logischen Reihenfolge. Der Leser darf nicht mehrere neue Begriffe in demselben Satz entschlüsseln müssen.

## STG-6.2 — Schlüsselwörter und feste Verknüpfungen wiederverwenden

**Level:** `MUST`

Verwenden Sie dieselben Schlüsselbegriffe und dieselben Verknüpfungswörter wieder, um Beziehungen explizit zu zeigen. Ersetzen Sie einen Schlüsselbegriff nicht durch ein Synonym, nur um den Stil zu variieren.

## STG-6.3 — Maximal 25 Wörter je beschreibendem Satz

**Level:** `MUST`

Ein beschreibender Satz hat maximal **25 Wörter** nach den Zählregeln in Abschnitt 8.

Wenn ein Satz die Grenze überschreitet, teilen Sie den Satz nach Thema oder logischer Beziehung. Entfernen Sie nicht nur Artikel und komprimieren Sie nicht nur Begriffe.

## STG-6.4 — Verwandte Informationen in Absätzen gruppieren

**Level:** `MUST`

Verwenden Sie Absätze als logische Einheiten. Starten Sie einen Absatz mit einem Thema-Satz, wenn die Inhaltsart diese Struktur zulässt.

## STG-6.5 — Ein Thema je Absatz

**Level:** `MUST`

Ein Absatz hat ein Hauptthema. Starten Sie einen neuen Absatz, wenn das Thema wechselt.

Eine nützliche Prüfung: Lesen Sie nur den ersten Satz von jedem Absatz. Wir empfehlen, dass diese Sätze zusammen eine sinnvolle Gliederung des Abschnitts ergeben.

## STG-6.6 — Maximal sechs Sätze je Absatz

**Level:** `MUST`

Ein beschreibender Absatz hat maximal sechs Sätze. Wenn mehr Sätze notwendig sind, prüfen Sie, ob der Absatz mehr als ein Thema enthält. Wenn ja, teilen Sie den Absatz.

---

<!-- source: rules/07-safety.md -->

# Abschnitt 7 — Sicherheitshinweise

STG-DE regelt die Sprache eines Sicherheitshinweises. Die zutreffende Sicherheitsnorm regelt die Risikoklassifikation, die Signalwörter, die Farben, die Symbole und das Layout.

## STG-7.1 — Risikostufe eindeutig kennzeichnen

**Level:** `MUST`

Verwenden Sie das Signalwort oder das Symbol, das das Sicherheitsklassifikationssystem des Projekts verlangt. Ein Dokument muss eine einheitliche Sicherheitsklassifikation verwenden.

Leiten Sie eine niedrigere Risikokategorie nicht nur aus einer alten Formulierung ab. Wenn die korrekte Kategorie unbekannt ist, geben Sie `NEEDS_SAFETY_INPUT` zurück.

## STG-7.2 — Schutzhandlung oder Bedingung zuerst

**Level:** `MUST`

Nennen Sie direkt nach dem Signalwort die Schutzhandlung oder die notwendige Bedingung. Der Leser muss die erforderliche Handlung kennen, bevor er sekundäre Erklärungen liest.

**STG-Muster**

> WARNUNG: Schalten Sie die Stromversorgung aus. ...

oder

> WARNUNG: Wenn die Abdeckung offen ist, berühren Sie keine spannungsführenden Teile. ...

## STG-7.3 — Gefahr oder Folge nennen

**Level:** `MUST`

Wenn die Folge bekannt ist, erklären Sie die Gefahr oder das mögliche Ergebnis konkret.

Vermeiden Sie abstrakte Formulierungen wie `Vorsicht ist geboten` oder `besondere Sorgfalt ist erforderlich`.

<!-- stg-lint: off -->
**Nicht STG**

> WARNUNG: Arbeiten Sie vorsichtig.
<!-- stg-lint: on -->

**STG**

> WARNUNG: Schalten Sie die Stromversorgung aus. Eine elektrische Spannung kann schwere Verletzungen verursachen.

Der technische Sicherheitsinhalt muss aus einer freigegebenen Sicherheitsbewertung kommen. Die Sprachregel erfindet keine Gefahren.

---

<!-- source: rules/08-punctuation-and-counting.md -->

# Abschnitt 8 — Zeichensetzung und Wortzählung

## STG-8.1 — Standardsatzzeichen und kein Semikolon zum Verbinden von Aussagen

**Level:** `MUST_NOT`

Verwenden Sie die Standardzeichensetzung des Deutschen. Verbinden Sie unabhängige technische Aussagen nicht mit einem Semikolon (`;`). Schreiben Sie stattdessen getrennte Sätze.

Diese Einschränkung ist absichtlich strenger als die normalen deutschen Zeichensetzungsregeln. Der Grund: Die Einschränkung begrenzt die Komplexität der Sätze.

## STG-8.2 — Bindestriche nur für echte Wortstruktur

**Level:** `MUST`

Verwenden Sie Bindestriche nach der deutschen Rechtschreibung und nach der freigegebenen Terminologie. Verwenden Sie Bindestriche in diesen Fällen:

- Ein Bindestrich zeigt die Grenzen in einem Kompositum deutlich.
- Ein Bindestrich verbindet Buchstaben oder Zahlen mit Wörtern, wenn die Rechtschreibung diese Verbindung verlangt.
- Ein Bindestrich ist ein Teil eines offiziellen Begriffs.

Verwenden Sie Bindestriche nicht, um syntaktische Komplexität zu verstecken. Verwenden Sie Bindestriche auch nicht, um eine lange Wortgruppe in ein einziges gezähltes Wort zu zwingen.

## STG-8.3 — Klammern restriktiv verwenden

**Level:** `MUST`

Klammern dürfen diese Inhalte enthalten:

- Verweise auf Abbildungen oder Textstellen,
- Kennungen,
- Kennungen von Arbeitsschritten,
- Abkürzungen nach der vollständigen Form,
- kurze Erläuterungen,
- kontrollierte Alternativen, wenn das Projektformat diese Alternativen ausdrücklich zulässt.

Schreiben Sie eine erforderliche Anweisung, eine Schutzhandlung oder eine primäre technische Bedingung nicht nur in Klammern.

## STG-8.4 — Doppelpunkt beendet die Einleitung einer vertikalen Liste

**Level:** `MUST`

Für die Wortzählung gilt: Der Text vor einem Doppelpunkt, der eine vertikale Liste einleitet, zählt als ein Satz. Jeder Listenpunkt wird separat geprüft.

Grenzen:

- 20 Wörter für Listenpunkte in anleitendem Text,
- 25 Wörter für Listenpunkte in beschreibendem Text.

## STG-8.5 — Klammertext separat prüfen

**Level:** `MUST`

Text in Klammern zählt im äußeren Satz als ein Wort. Der Text in den Klammern wird zusätzlich separat auf Klarheit und auf die zutreffende Satzlänge geprüft.

Diese Zählregel erlaubt keine komplexen Anweisungen in Klammern.

## STG-8.6 — Geschützte Einheiten zählen als ein Wort

**Level:** `MUST`

Für die Zählung der Satzlänge zählt jedes dieser Elemente im umgebenden Satz als ein Wort:

- eine Zahl,
- eine Zahl, die direkt mit ihrer Einheit verbunden ist,
- eine Abkürzung,
- eine alphanumerische Kennung,
- zitierter oder gesperrter Text,
- ein offizieller Titel, eine offizielle Überschrift oder eine offizielle Beschriftung,
- ein geschützter Eigenname.

Zählen Sie keine Nummerierung, die nur einen Arbeitsschritt kennzeichnet.

## STG-8.7 — Bindestrichkomposita zählen orthografisch als ein Wort

**Level:** `MUST`

Ein deutsches Kompositum mit Bindestrich zählt für die Satzlänge als ein orthografisches Wort. Für das Kompositum gelten trotzdem die Komplexitätsregeln in Abschnitt 2.

## STG-DE-8.1 — Schrägstrichkombinationen vermeiden

**Level:** `SHOULD_NOT`

Wir empfehlen, Formen wie `und/oder`, `der/die`, `ein-/ausschalten` und komprimierte Alternativen mit Schrägstrich in technischem Fließtext zu vermeiden. Diese Empfehlung gilt, wenn diese Formen mehr als eine Interpretation zulassen.

Verwenden Sie ein explizites `und`, ein explizites `oder`, eine vertikale Liste oder getrennte Sätze.

Ausnahmen sind gesperrte Kennungen und kompakte Tabellennotationen, die das Projekt definiert.

---

<!-- source: rules/09-writing-practices.md -->

# Abschnitt 9 — Schreibpraxis

## STG-9.1 — Satz neu bauen, wenn Wortersatz nicht reicht

**Level:** `MUST`

Ersetzen Sie ein nicht freigegebenes Wort nicht mechanisch, wenn der Ersatz die Grammatik, die Bedeutung oder die Modalität ändert. Schreiben Sie den vollständigen Satz neu und behalten Sie die technische Bedeutung.

Wenn die beabsichtigte Bedeutung unklar ist, muss ein Sprachwerkzeug `NEEDS_DOMAIN_INPUT` zurückgeben und keine erfundene Umformulierung.

## STG-9.2 — Freigegebene Wörter korrekt verwenden

**Level:** `MUST`

Bevor Sie ein freigegebenes Wort verwenden, prüfen Sie die freigegebene Bedeutung, die Wortart, die Einschränkungen und das Domänenprofil des Worts.

Wenn ein Wort mehrere freigegebene Bedeutungen hat, muss das Lexikon diese Bedeutungen mit getrennten Bedeutungs-IDs unterscheiden.

## STG-9.3 — Keine idiomatischen Verbgefüge als Ersatz für direkte Verben

**Level:** `MUST_NOT`

Im Deutschen kommen Mehrdeutigkeit und unnötige Länge oft von Redewendungen und Funktionsverbgefügen.

Verwenden Sie keine idiomatische oder substantivlastige Verbalphrase, wenn ein direktes freigegebenes Verb dieselbe technische Bedeutung gibt.

<!-- stg-lint: off -->
**Nicht STG**

> Nehmen Sie eine Prüfung vor.
<!-- stg-lint: on -->

**STG**

> Prüfen Sie das Bauteil.

<!-- stg-lint: off -->
**Nicht STG**

> Bringen Sie die Änderung zur Anwendung.
<!-- stg-lint: on -->

**STG**

> Wenden Sie die Änderung an.

Lexikalisierte technische Mehrwortverben dürfen als einzelne Wörterbucheinträge freigegeben werden, wenn die Domäne diese Verben verlangt.

## STG-9.4 — Terminologie und Formulierungen konsistent halten

**Level:** `MUST`

Verwenden Sie für dieselbe Handlung in demselben Kontext dieselbe freigegebene Formulierung. Ändern Sie das Satzmuster nicht, um den Stil zu variieren.

Wir empfehlen Vorlagen für wiederkehrende Arbeitsschritte.

---

# Allgemeine Empfehlungen

Diese Empfehlungen sind standardmäßig nicht verbindlich. Ein Projekt darf jede dieser Empfehlungen als verbindlich festlegen.

## STG-GR-1 — Nebensatzmarker explizit und korrekt


Verwenden Sie explizite Konjunktionen wie `dass`, `wenn`, `weil` und `bevor`, wenn diese Konjunktionen die Beziehungen zwischen Sätzen klar zeigen. Vermeiden Sie in Fließtext komprimierte Auslassungen im Stil von Schlagzeilen.

## STG-GR-2 — `mit` auf Mehrdeutigkeit prüfen


Die Präposition `mit` kann ein Werkzeug, eine Begleitung, eine Zuordnung oder eine Bedingung ausdrücken. Wenn mehr als eine Lesart plausibel ist, schreiben Sie den Satz neu.

**Mehrdeutig**

> Montieren Sie die Abdeckung mit den roten Schrauben.

Mögliche beabsichtigte Bedeutungen sind zum Beispiel:

- Montieren Sie die Abdeckung, die rote Schrauben hat.
- Montieren Sie die Abdeckung zusammen mit den roten Schrauben.
- Verwenden Sie die roten Schrauben als Befestigungselemente.

Nennen Sie die beabsichtigte Beziehung explizit.

## STG-GR-3 — Pronomen sparsam verwenden


Verwenden Sie ein Pronomen nur, wenn das Bezugswort eindeutig ist. Eine Wiederholung des technischen Substantivs ist besser als ein mehrdeutiger Bezug.

## STG-GR-4 — Demonstrativa mit Nomen verwenden


Verwenden Sie bevorzugt `diese Leitung`, `dieser Wert` oder `diese Methode` statt eines alleinstehenden `dies` oder `diese`. Diese Empfehlung ist besonders wichtig, wenn mehrere Bezugswörter möglich sind.

## STG-GR-5 — Lehnübersetzungen und falsche Freunde prüfen


Autoren und Übersetzungssysteme dürfen Bedeutungen nicht aus dem Englischen übertragen, nur weil ein deutsches Wort ähnlich aussieht. Beispiele, die eine Prüfung des Kontexts verlangen, sind `realisieren`, `kontrollieren`, `eventuell` und `aktuell`. Diese Prüfung gilt für Übersetzungen aus dem Englischen und in das Englische.

Diese Regel schreibt ohne Kontext keinen Ersatz vor.

## STG-GR-6 — Abkürzungen in Fließtext reduzieren


Verwenden Sie bevorzugt vollständige deutsche Ausdrücke statt allgemeiner Abkürzungen wie `z. B.`, `d. h.`, `ggf.`, `bzw.` und `usw.`. Diese Empfehlung gilt, wenn die Abkürzung die Klarheit verringern kann.

Die Wortschatzrichtlinie des Basislexikons verbietet `ggf.` und `bzw.`, weil diese Abkürzungen oft eine Bedingung oder eine Beziehung verstecken.

## STG-GR-7 — Neutrale Personenbezeichnungen bevorzugen


Verwenden Sie nach Möglichkeit neutrale und technisch präzise Rollen- oder Funktionsbezeichnungen. Beispiele sind `Personal`, `Fachkraft`, `Bedienperson`, `Prüfperson` oder eine Rollenbezeichnung, die das Projekt definiert.

Vermeiden Sie geschlechtsspezifische Pronomen, wenn diese Pronomen nicht notwendig sind. Die zutreffende Sprach- oder Stilrichtlinie regelt besondere orthografische Genderzeichen. STG-DE selbst verlangt diese Zeichen nicht.

## STG-GR-8 — Genitivketten vermeiden


Ein einfacher deutscher Genitiv ist zulässig. Vermeiden Sie lange Ketten von Besitz- oder Genitivbeziehungen. Solche Ketten zwingen den Leser, mehrere verschachtelte Abhängigkeiten aufzulösen.

**Schwer lesbar**

> die Prüfung der Dichtung des Ausgangs des Reglers

**Besser**

> die Prüfung der Dichtung am Reglerausgang

## STG-DE-9.1 — Modalpartikeln und rhetorische Füllwörter vermeiden

**Level:** `MUST_NOT`

Verwenden Sie keine Modalpartikeln und keine Füllwörter aus der Umgangssprache, wenn diese Wörter keine präzise technische Bedeutung haben. Beispiele sind `mal`, `doch`, `eben`, `halt`, `wohl`, `eigentlich` und `einfach`.

## STG-DE-9.2 — Vage Qualitäts- und Zeitangaben ersetzen

**Level:** `MUST`

Ersetzen Sie vage Ausdrücke durch beobachtbare Kriterien, wenn das Kriterium für die Aufgabe wichtig ist.

Beispiele für Ausdrücke, die im Normalfall eine Umformulierung verlangen:

- `möglichst schnell`,
- `zeitnah`,
- `ordnungsgemäß`,
- `fachgerecht`,
- `ausreichend`,
- `bei Bedarf`,
- `gegebenenfalls`.

<!-- stg-lint: off -->
**Nicht STG**

> Ziehen Sie die Schraube ausreichend fest.
<!-- stg-lint: on -->

**STG**

> Ziehen Sie die Schraube mit 8 Nm fest.

Wenn kein messbares Kriterium verfügbar ist, fordern Sie Domäneninformationen an und erfinden Sie kein Kriterium.
