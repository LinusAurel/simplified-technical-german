# STG-DE — Vereinfachtes Technisches Deutsch

Eigenständige Fassung der Spezifikation für Release 0.3.0. Die Dateien im Repository bleiben die kanonische Quelle.

---

<!-- source: specification.md -->

# Normative Spezifikation von STG-DE

## 1. Anwendungsbereich

STG-DE ist eine kontrollierte Form des geschriebenen Deutsch für technische Dokumentation. STG-DE ist für diese Inhalte vorgesehen:

- Anleitungen,
- Wartungsinformationen,
- Betriebsinformationen,
- Systembeschreibungen,
- Servicedokumentation,
- technische Berichte,
- Sicherheitshinweise,
- ähnliche technische Inhalte.

STG-DE kontrolliert den **Ausdruck**, nicht das Layout des Dokuments. Für diese Themen gilt der anwendbare Publikationsstandard oder die anwendbare Unternehmensrichtlinie: Typografie, Nummerierungssysteme, Seitengestaltung, produktspezifische Warngrafiken, Regeln für Einheiten und Dokumentarchitektur.

## 2. Gestaltungsprinzipien

STG-DE beruht auf diesen Prinzipien:

1. **Ein Term — ein Konzept.** Verwenden Sie in einem definierten Geltungsbereich eine freigegebene Benennung für ein technisches Konzept.
2. **Ein allgemeines Wort — eine kontrollierte Bedeutung.** Ein zentrales Lexikon kann ein allgemeinsprachliches Wort auf eine Bedeutung und eine Wortart beschränken.
3. **Handlungen mit Verben ausdrücken.** Bevorzugen Sie direkte Verben statt Nominalisierungen und Funktionsverbgefügen.
4. **Bekannter Akteur zuerst.** Verwenden Sie das Aktiv, wenn der Akteur bekannt ist. Verwenden Sie für Anweisungen den formellen Imperativ.
5. **Eine Anweisung je Satz.** Kombinieren Sie Handlungen nur, wenn die Handlungen gleichzeitig sind oder eine untrennbare physische Handlung bilden.
6. **Bedingungen vor Befehlen.** Der Leser sieht die Bedingung vor der Handlung, die von dieser Bedingung abhängt.
7. **Kurze Sätze.** Befehle in Anleitungen und Sicherheitshinweisen haben höchstens 20 Wörter. Beschreibungen und Hinweise haben höchstens 25 Wörter je Satz.
8. **Ein Thema je Satz und Absatz.** Fügen Sie Informationen schrittweise hinzu.
9. **Keine stilistische Variation mit Synonymen.** Wiederholung hat Vorrang vor lexikalischer Variation.
10. **Keine versteckte Modalität.** Unterscheiden Sie Anforderung, Erlaubnis, Fähigkeit oder Möglichkeit, Empfehlung und Verbot.
11. **Kein ungeklärter Bezug.** Pronomen, Demonstrativa, Ellipsen und Negationen müssen einen eindeutigen Bezugsbereich haben.
12. **Deutsche Morphologie ist explizit erfasst.** Wörterbucheinträge enthalten Genus, Plural, Flexion, Trennbarkeit und freigegebene Formen, wenn diese Angaben zutreffen.

## 3. Deutsche Grundlage

Das Standardprofil für die Rechtschreibung ist `de-DE`. Grundlage dieses Profils ist das **Amtliche Regelwerk der deutschen Rechtschreibung (2024)**. Eine Ausnahme gilt, wenn eine anwendbare offizielle Richtlinie ein anderes nationales oder organisatorisches Rechtschreibprofil für Deutsch verlangt.

Die Projektkonfiguration darf ein anderes Profil festlegen, zum Beispiel `de-CH`. Ein Dokument darf Rechtschreibprofile nicht ohne ausdrücklichen Grund mischen.

## 4. Textarten

### 4.1 Anleitung

Eine Anleitung sagt dem Leser, welche Handlungen der Leser ausführt. Anweisungen verwenden den formellen Imperativ mit `Sie`. Eine Ausnahme gilt, wenn eine verbindliche Projektrichtlinie ein anderes kontrolliertes Imperativprofil festlegt.

Standard:

> Entfernen Sie die Abdeckung.

<!-- stg-lint: off -->
Nicht Standard:

> Abdeckung entfernen.
<!-- stg-lint: on -->

Den Infinitivstil für Anweisungen dürfen Sie nur als Projektprofil aktivieren. Wenn ein Projekt diesen Stil aktiviert, muss das Projekt den Infinitivstil konsistent verwenden.

### 4.2 Beschreibung

Eine Beschreibung gibt Informationen und gibt dem Leser keine Befehle. Die Standardzeitform für Beschreibungen ist das Präsens. Jeder Satz hat ein Hauptthema.

### 4.3 Sicherheitshinweis

Ein Sicherheitshinweis enthält:

1. das Signalwort oder eine andere projektdefinierte Kennzeichnung des Risikos,
2. den vorbeugenden Befehl oder die Bedingung,
3. die Folge oder das Risiko, wenn die Folge oder das Risiko bekannt ist.

Die Taxonomie der Risiken kommt aus der anwendbaren Sicherheitsnorm, nicht aus STG-DE.

### 4.4 Hinweis

Ein Hinweis gibt optionale unterstützende Informationen. Ein Hinweis darf keine Anweisung, keine verbindliche Anforderung, keinen Abnahmegrenzwert, keine Toleranz und keine sicherheitskritische Handlung enthalten.

### 4.5 Gesperrter externer Text

Diese Texte dürfen außerhalb von STG-DE liegen:

- rechtliche Namen,
- Beschriftungen der Benutzeroberfläche,
- Schilder,
- Dokumenttitel,
- Kennungen,
- Formeln,
- zitiertes Material,
- extern kontrollierte Zeichenketten.

Der umgebende Satz muss den STG-Regeln trotzdem folgen, wo das möglich ist.

## 5. Konformität

### 5.1 `STG-R`

Ein Text ist konform zu `STG-R`, wenn der Text alle anwendbaren verbindlichen Schreibregeln erfüllt.

### 5.2 `STG-T`

Ein Text ist konform zu `STG-T`, wenn der Text konform zu `STG-R` ist. Zusätzlich muss die anwendbare Terminologiequelle jedes technische Substantiv und jedes technische Verb freigeben.

### 5.3 `STG-C-core`

Ein Text ist konform zu `STG-C-core`, wenn der Text konform zu `STG-T` ist. Zusätzlich muss das zentrale Kernlexikon v0.1 für das Schreiben jedes andere nicht gesperrte lexikalische Element freigeben. Diese Freigabe muss für die verwendete Bedeutung und die verwendete Wortart gelten. Unbekannte allgemeinsprachliche Wörter sind nicht automatisch akzeptiert.

### 5.4 `STG-C`

Ein Text ist konform zu `STG-C`, wenn der Text konform zu `STG-T` ist. Zusätzlich muss ein umfassendes, von Menschen geprüftes zentrales kontrolliertes Lexikon jedes andere lexikalische Element freigeben. Diese Freigabe muss für die verwendete Bedeutung und die verwendete Wortart gelten.

`STG-C-core` ist ein Profil mit geschlossenem Wortschatz. Dieses Profil ist für kontrolliertes Schreiben mit dem mitgelieferten Kernlexikon v0.1 vorgesehen. `STG-C` bleibt für ein umfassenderes, von Menschen geprüftes zentrales Lexikon reserviert. In diesem Release ist `STG-C` kein allgemeiner Anspruch auf Zertifizierung.


### 5.5 Kanonische Lemmata und Kollisionen von Flexionsformen

Die lexikalische Auflösung muss kanonische Lemmata prüfen, bevor die Auflösung einen Flexionsalias aus einem anderen Eintrag akzeptiert. Wenn dieselbe Oberflächenform zwei kontrollierte Konzepte darstellen kann, muss das Lexikon die Unterscheidung explizit kodieren. Der Validator muss in diesem Fall Kontext, Wortart und Vorrang der Einträge verwenden.

Normatives Beispiel: `Daten` ist ein unabhängiges, eingeschränktes Substantiv für technische Daten oder Informationen. Die lexikalische Auflösung darf `Daten` nicht automatisch als Plural von `Datum` einstufen.

## 6. Terminologiequellen

Die Reihenfolge für die Auflösung der Terminologie ist:

1. Regulatorische oder vertragliche Terminologie, die nicht änderbar ist
2. Freigegebene Unternehmens- oder Produktterminologie
3. Freigegebene Branchen- oder Fachgebietsterminologie
4. Zentrales STG-Lexikon
5. Vorschlag für einen neuen Term, der eine Prüfung erfordert

Ein Agent darf eine offizielle technische Benennung nicht nur deshalb ersetzen, weil ein kürzeres oder häufigeres Synonym existiert.

## 7. Wortzählung

Für die Grenzwerte der Regeln gilt:

- Ein orthografisches Wort zwischen Leerzeichen zählt als ein Wort, wenn keine der folgenden Regeln gilt.
- Eine Zahl mit der direkt zugehörigen Einheit zählt als ein Wort.
- Eine Abkürzung oder alphanumerische Kennung zählt als ein Wort.
- Ein geschützter Eigenname, Titel, eine geschützte Beschriftung oder eine zitierte Zeichenkette zählt im umgebenden Satz als ein Wort.
- Text in Klammern zählt im äußeren Satz als ein Wort. Die Prüfung prüft diesen Text zusätzlich als eigenen Satz oder eigenes Fragment.
- Ein Kompositum mit Bindestrich zählt als ein orthografisches Wort. Die Regel für die Komplexität von Komposita gilt trotzdem.
- Eine Nummerierung, die nur einen Arbeitsschritt kennzeichnet, zählt nicht.

Die Regeln für die Wortzählung sind Kompatibilitätsregeln. Diese Regeln erlauben nicht, syntaktisch dichte Komposita zu bilden.

## 8. Prinzipien der maschinellen Prüfung

Die Regeln haben diese Klassen:

- `deterministic` — Die Prüfung ist im Regelfall mechanisch möglich, zum Beispiel für die Wortanzahl oder ein verbotenes Semikolon.
- `heuristic` — Wertvolle Heuristiken können die Fälle erkennen, zum Beispiel Passiv oder vage Wörter.
- `semantic` — Die Prüfung erfordert eine Analyse von Terminologie oder Bedeutung, zum Beispiel für „ein Term, ein Konzept“ oder mehrdeutige Pronomen.
- `domain` — Die Prüfung erfordert freigegebene Terminologie oder Fachwissen.

Ein Validator muss einen harten Verstoß von einem heuristischen Befund unterscheiden.


## 8.1 Korpusbelege und lexikalische Steuerung

Die Häufigkeit im Korpus ist ein Beleg für die lexikalische Prüfung, keine automatische Freigabe. Ein häufiger Ausdruck kann verboten bleiben oder eine Prüfung erfordern, wenn der Ausdruck vage, mehrdeutig, stilistisch redundant oder deterministisch schwer auflösbar ist.

Ein Korpus-Audit muss mindestens diese Gruppen unterscheiden:

- Lücken im allgemeinsprachlichen Wortschatz,
- Lücken bei der Auflösung von Flexionsformen und Kontraktionen,
- Kandidaten für freigegebene Projektterminologie,
- geschützte Kennungen, Namen und Beschriftungen,
- verbotene Formulierungen und Formulierungen, die eine Prüfung erfordern.

STG-DE darf unbekannte Wörter nicht stillschweigend als technische Terme einstufen, um die Abdeckung der Allgemeinsprache zu erhöhen.

## 9. Rückverfolgbarkeit der Regeln

`rules/rule-index.yaml` ist der kanonische Index für jede Regel und jede Empfehlung von STG-DE. Regel-IDs sind innerhalb einer Hauptversionslinie stabil. Ein Regeldatensatz nennt den Geltungsbereich, die Stufe, den Titel und die kanonische Markdown-Datei mit dem normativen Wortlaut.

## 10. Änderungssteuerung

Eine Änderung an einer verbindlichen Regel oder an einer Bedeutung im Wörterbuch muss diese Angaben enthalten:

- Kennung,
- alter Wortlaut oder alte Bedeutung,
- vorgeschlagener Wortlaut oder vorgeschlagene Bedeutung,
- technischer Grund,
- Beispiele,
- Auswirkung auf Validatoren,
- Hinweis zur Migration.

Die Versionierung folgt Semantic Versioning, solange das Projekt experimentell ist. Eine veröffentlichte Regel-ID muss auch vor Release 1.0 stabil bleiben. Eine Regel-ID darf nur mit einem angenommenen Änderungsvorschlag ihre Bedeutung ändern oder entfallen. Eine entfallene Regel-ID bleibt reserviert.

Eine Regel mit der Stufe `RECOMMENDATION` ist als Ganzes eine Empfehlung. In einer Regel mit der Stufe `MUST` sind Sätze im Imperativ und Sätze mit „muss“ oder „darf nicht“ verbindlich. Ein Satz mit „Wir empfehlen“ oder „Empfehlung:“ ist auch in einer Regel mit der Stufe `MUST` eine Empfehlung.

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

Schreiben Sie kurze Sätze mit einer primären Aussage. Empfehlung: Geben Sie in beschreibendem Text jedem Satz ein Hauptthema. Verdichten Sie nicht mehrere unabhängige Fakten in einem Satz.

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

Ein Validator muss ein Pronominaladverb mit ungeklärtem Bezug als Befund zur Prüfung melden, zum Beispiel mit dem Status `NEEDS_REFERENCE_INPUT` (siehe `validator-contract.md`). Der Validator darf das Bezugswort nicht erfinden.

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


Prüfen Sie die Bedeutung eines deutschen Worts, das einem englischen Wort ähnlich sieht. Übertragen Sie eine englische Bedeutung nicht nur wegen dieser Ähnlichkeit. Diese Empfehlung gilt für Autoren und für Übersetzungssysteme. Beispiele, die eine Prüfung des Kontexts verlangen, sind `realisieren`, `kontrollieren`, `eventuell` und `aktuell`. Diese Prüfung gilt für Übersetzungen aus dem Englischen und in das Englische.

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

---

<!-- source: dictionary/README.md -->

# STG-DE controlled dictionary — v0.1

**Release:** 0.3.0  
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

- `approved-words.yaml` — normative Einträge des Autorenkerns v0.1.
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

Die Häufigkeit im Korpus ist ein Beleg für eine **Prüfung**, keine Freigabe. Version 0.1 nimmt ein Wort nur in den Kern auf, wenn die domänenübergreifende Bedeutung des Worts sinnvoll kontrolliert werden kann. Häufige, aber abstrakte oder mehrdeutige Verben wie `führen`, `bieten`, `berücksichtigen` und `gewährleisten` bleiben prüfpflichtig.

Domänenspezifische Bauteile, Produktnamen, medizinische Begriffe, Fahrzeugbegriffe, Software-Kennungen und ähnlicher Wortschatz gehören zur Projektterminologie oder Domänenterminologie. Diese Regel gilt auch, wenn diese Wörter häufig sind.

Siehe `../corpus/validation-report.md`.

## `STG-C-core` versus `STG-C`

`STG-C-core` ist ein experimentelles Profil mit geschlossenem Wortschatz. Dieses Profil gilt für Texte, die Autoren absichtlich mit diesem Kern und mit freigegebener Projektterminologie schreiben.

`STG-C` bleibt für ein zukünftiges, breiteres Lexikon reserviert, das Menschen geprüft haben. Dieses Release darf `STG-C` nicht beanspruchen.

---

<!-- source: dictionary/MORPHOLOGY.md -->

# STG-DE morphology and lexical resolution — v0.1

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

# STG-DE lexical decisions — through v0.1

## Status

Diese Datei dokumentiert lexikalische Entscheidungen mit großer Wirkung, die bis zum Autorenkern v0.1 entstanden sind. Die Einträge sind **vorläufig**, bis Fachleute für deutsche technische Redaktion und Terminologie die Einträge prüfen.

Der Ausgangsstandard verwendet ein kontrolliertes Wörterbuch. In diesem Wörterbuch haben freigegebene Wörter eine festgelegte Wortart und eine freigegebene Bedeutung. Nicht freigegebene Wörter können auf freigegebene Alternativen oder auf eine andere Satzkonstruktion verweisen. STG-DE behält diese Architektur, übersetzt das englische Wörterbuch aber **nicht** eins zu eins.

## Ziel des Release

Die Versionen 0.0.3 und 0.1 definieren einen durchsetzbaren **Autorenkern** für häufige deutsche technische Texte. Das Ziel des Kerns ist ein Grad an Determinismus, mit dem Agenten und Validatoren Texte erzeugen und umformulieren können. Die Domänenterminologie bleibt bei den Quellen der Projektterminologie.

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

---

<!-- source: mapping/README.md -->

# Rückverfolgbarkeit zu den Quellregeln

`ste100-issue9.yaml` ordnet jede Schreibregel und jede allgemeine Empfehlung von **ASD-STE100 Issue 9 (Januar 2025)** der STG-DE-Regel zu, die dieselbe Absicht für das Deutsche umsetzt.

## Die Zuordnung lesen

| Feld | Bedeutung |
|---|---|
| `ste` | Regelnummer von ASD-STE100 (`1.1` … `9.4`) oder allgemeine Empfehlung (`GR-1` … `GR-8`). |
| `stg` | Primäre STG-DE-Regel. Nummerierte STG-Regeln verwenden die Nummer von ASD-STE100: `STG-5.1` setzt Regel 5.1 um. |
| `related` | Andere STG-DE-Regeln, die einen Teil desselben Risikos abdecken. |
| `relation` | `equivalent`, `adapted` oder `replaced` (siehe unten). |
| `note` | Unabhängig geschriebene deutsche Erklärung der Anpassung. |

- `equivalent` — dieselbe Absicht. Die deutschen Formulierungen und Beispiele sind unabhängig.
- `adapted` — dieselbe Absicht, aber Geltungsbereich, Schwellenwerte oder Mechanik sind an die deutsche Grammatik angepasst.
- `replaced` — die Quellregel betrifft ein Phänomen des Englischen, zum Beispiel die `-ing`-Form oder Phrasal Verbs. STG-DE ersetzt die Quellregel durch das deutsche Phänomen mit demselben Risiko, zum Beispiel Nominalisierung oder Funktionsverbgefüge.

`german_extensions` nennt die `STG-DE-*`-Regeln ohne direktes Gegenstück in ASD-STE100, mit der nächstliegenden Quellregel.

## Zusammenfassung

| Beziehung | Schreibregeln | Allgemeine Empfehlungen |
|---|---:|---:|
| equivalent | 35 | 2 |
| adapted | 15 | 4 |
| replaced | 3 | 2 |
| **gesamt** | **53** | **8** |

Alle 75 STG-DE-Regeln und -Empfehlungen sind von dieser Datei aus erreichbar. `tests/test_mapping.py` prüft die Vollständigkeit.

## Grenze des Urheberrechts

ASD-STE100 ist ein Urheberrecht und eine in der EU eingetragene Marke von ASD (Aerospace, Security and Defence Industries Association of Europe), Brüssel. Der Standard ist kostenlos unter <https://www.asd-ste100.org> erhältlich. Eine Weitergabe erfordert aber eine schriftliche Genehmigung von ASD.

Aus diesem Grund enthält dieses Repository **nur Regelnummern und unabhängig geschriebenen deutschen Text**. Das Repository gibt keine Formulierungen von Regeln, keine Beispiele und keine Wörterbucheinträge aus ASD-STE100 wieder. STG-DE ist keine offizielle Veröffentlichung von ASD. STG-DE hat keine Billigung (Endorsement) durch ASD oder die STEMG.

---

<!-- source: corpus/validation-report.md -->

# STG-DE v0.1: Bericht zur Korpusvalidierung über mehrere Branchen

## Zusammenfassung des Ergebnisses

v0.1 validiert den Autorenkern mit einem **geschichteten Korpus aus sechs Branchen** und nicht mit einer einzelnen Ingenieursdomäne. Das öffentliche Validierungsset enthält **18 unabhängige technische Quellen**, je drei Quellen aus jeder Branche. Es enthält **2.066 analysierte Token** in kurzen deutschen Auszügen. Das Release verteilt die Auszüge und Handbücher **nicht**. Es speichert nur Metadaten der Quellen, Hashes, Häufigkeiten und aggregierte Metriken.

| Metrik | v0.0.3-Basis | v0.1 nur Normalisierung | v0.1 endgültig |
|---|---:|---:|---:|
| Abdeckung durch zentrale kontrollierte Oberflächenformen | 51.4% | 52.7% | **58.1%** |
| Token mit `NEEDS_LEXICON_REVIEW` | 272 | 245 | **232** |
| Rate der gerouteten oder klassifizierten Token | 86.8% | 88.1% | **88.8%** |

Die endgültige Abdeckung durch zentrale Oberflächenformen liegt bei diesem öffentlichen Set **6.7 Prozentpunkte** über der historischen v0.0.3-Basis. Dieser Wert ist keine Zielrate für die Akzeptanz. Fachnomen, Produktnamen, Kennungen, Domänenverben und absichtlich nicht zugelassene Sprache bleiben erwartungsgemäß außerhalb des allgemeinen Kerns.

## Design des Korpus

| Branche | Quellen | Token | v0.0.3-Basis | v0.1 endgültig |
|---|---:|---:|---:|---:|
| Anlagenbau | 3 | 311 | 49.2% | **58.5%** |
| Automotive | 3 | 359 | 49.6% | **58.8%** |
| Elektrotechnik | 3 | 342 | 48.8% | **55.0%** |
| Maschinenbau | 3 | 356 | 50.3% | **58.4%** |
| Medizintechnik | 3 | 334 | 52.1% | **55.4%** |
| Software/IT | 3 | 364 | 58.0% | **62.1%** |

Die sechs Strata sind Maschinenbau, Automotive, Elektrotechnik, Software/IT, Medizintechnik und Anlagenbau. Die Auswahl der Quellen bevorzugt Dokumentation von Herstellern oder Projekten, die öffentlich auf Deutsch zugänglich ist. Die Datei `corpus/sources.yaml` dokumentiert die exakten Metadaten der Quellen und die Hashes der Stichproben.

Die Token-Anzahlen sind absichtlich ähnlich, aber nicht gleich. Eine gleiche Anzahl von Dokumenten verhindert, dass eine Branche die Kuratierung dominiert. Das Release enthält keine Handbücher von Dritten. Lesen Sie dieses Release deshalb als **geschichtetes Belegkorpus** und nicht als Volltextarchiv.

## Änderungen in v0.1

### 1. Deutsche Nomenmorphologie ist Teil der lexikalischen Auflösung

v0.0.3 speicherte Pluralformen wie `Informationen`, `Gefahren`, `Schritte` und `Geräte` in den Metadaten der Nomen. Der Entwicklungsvalidator löste diese Formen aber nicht auf. v0.1 erkennt **deklarierte Pluralformen von Nomen** als `CENTRAL_INFLECTION`. Mit denselben öffentlichen Auszügen erhöht die Normalisierung allein die kontrollierte Abdeckung von 51.4% auf 52.7%.

Diese Änderung ist eine Korrektur des Validators und keine künstliche Vergrößerung des Vokabulars.

### 2. `Datum` und `Daten` sind nicht mehr vermischt

Das Korpus zeigte eine deutsche lexikalische Kollision: `Datum` hat den Plural `Daten`. Technische Dokumentation verwendet `Daten` aber im Normalfall in der Bedeutung „Informationen“. Ein naiver Pluralindex gibt deshalb die falsche kontrollierte Bedeutung. v0.1 fügt ein unabhängiges eingeschränktes Lemma `Daten` hinzu. Kanonische Lemmata haben in v0.1 Vorrang vor Plural-Aliasen.

Dieser Befund ist für die agentenbasierte Validierung wichtig. Gleiche Oberflächenformen genügen nicht, wenn eine deutsche Flexionsform mit einem anderen lexikalischen Konzept kollidiert.

### 3. Großschreibung bedeutet nicht mehr „Fachbegriff“

Im Deutschen sind alle Nomen großgeschrieben. Die Entwicklungsheuristik von v0.0.3 ordnete jedes unbekannte großgeschriebene Token `TECHNICAL_TERM_CANDIDATE` zu. Diese Zuordnung zeigt eine zu hohe Abdeckung durch Terminologie. v0.1 verwendet die neutrale Klasse `LEXICAL_NOUN_CANDIDATE`. Ein Kandidat wird nur nach der Auflösung gegen ein zugelassenes Projektglossar oder eine Kategorie für Fachnomen zu Projektterminologie.

### 4. Nur domänenübergreifendes, kontrollierbares Vokabular kam in den Kern

v0.1 fügt allgemeine Konzepte technischer Dokumente hinzu. Beispiele sind `Betriebsanleitung`, `Fachpersonal`, `Verletzung`, `Verwendung`, `Produkt`, `Version`, `Änderung`, `Kennzeichnung`, `Symbol` und `Daten`. v0.1 fügt auch direkte Verben wie `lesen`, `wählen`, `bedienen` und `benötigen` hinzu.

Häufigkeit allein genügte **nicht** für eine Zulassung. Häufige Wörter wie `führen`, `bieten`, `berücksichtigen` und `gewährleisten` gehen in das Review. Ihre technische Bedeutung ist für eine bedingungslose Zulassung zu kontextabhängig oder zu abstrakt.

### 5. Die Abdeckungskurve ist jetzt reproduzierbar

`corpus/coverage-curves.csv` beginnt mit dem historischen Ergebnis von v0.0.3. Danach wendet die Kurve die Normalisierungsschicht von v0.1 an. Danach fügt sie jeden neuen Kerneintrag in einer deterministischen Reihenfolge der Belege hinzu. Mit diesem Verfahren trennt die Kurve die Gewinne aus Korrekturen an Grammatik und Lemmatisierung von den Gewinnen durch neues Vokabular.

## Endgültige Verteilung nach Branchen

| Branche | Kontrolliert | Unbekannt | Review | Verboten | Lexikalische Nomenkandidaten |
|---|---:|---:|---:|---:|---:|
| Anlagenbau | 58.5% | 32 | 6 | 4 | 81 |
| Automotive | 58.8% | 39 | 7 | 5 | 85 |
| Elektrotechnik | 55.0% | 44 | 10 | 4 | 80 |
| Maschinenbau | 58.4% | 41 | 11 | 5 | 79 |
| Medizintechnik | 55.4% | 42 | 9 | 6 | 83 |
| Software/IT | 62.1% | 34 | 6 | 5 | 81 |

## Wiederkehrende Muster außerhalb von STG

Das Korpus begründet weiterhin, übliches fachsprachliches Deutsch abzulehnen oder zu prüfen, wenn es für kontrolliertes Schreiben nicht deterministisch genug ist. Wiederkehrende Beispiele sind `sowie`, `entsprechend`, `gegebenenfalls`, `ausreichend` und kontextabhängige Verben wie `führen` oder `durchführen`.

Das Ziel ist nicht, dass vorhandene Handbücher ohne Änderung bestehen. Das Ziel ist, Autorinnen, Autoren und Agenten deterministische Umformulierungen zu geben. Das Ziel ist auch, allgemeines Kernvokabular von Domänenterminologie zu trennen.


## Was v0.1 nicht beweist

v0.1 ist deutlich stärker als v0.0.3. Trotzdem ist v0.1 weiterhin ein experimenteller Autorenstandard. Die Version belegt keine Abdeckung der gesamten deutschen technischen Dokumentation. Die Version ersetzt diese Punkte nicht:

- Review durch Fachleute aus deutscher technischer Redaktion und Terminologie,
- Analyse lizenzierter Volltextkorpora in deutlich größerem Umfang,
- einen deterministischen morphologischen und syntaktischen Analyzer für Deutsch,
- Tests des Leseverständnisses,
- Validierung von Sicherheitsinhalten nach dem Veröffentlichungsstandard, der für ein Produkt gilt,
- Governance der Projektterminologie.

`STG-C-core` bleibt deshalb experimentell. `STG-C` bleibt für ein späteres Release reserviert, das Menschen geprüft haben.

---

## Strukturierter Anhang: `rules/rule-index.yaml`

```yaml
schema_version: '0.1'
release: 0.3.0
rule_or_recommendation_count: 75
mandatory_or_normative_rule_count: 67
general_recommendation_count: 8
rules:
- id: STG-1.1
  title: Zulässiger Wortschatz
  file: rules/01-words.md
  level: MUST
- id: STG-1.2
  title: Wortart
  file: rules/01-words.md
  level: MUST
- id: STG-1.3
  title: Kontrollierte Bedeutung
  file: rules/01-words.md
  level: MUST
- id: STG-1.4
  title: Zulässige Flexionsformen
  file: rules/01-words.md
  level: MUST
- id: STG-1.5
  title: Technische Substantive
  file: rules/01-words.md
  level: MUST
- id: STG-1.6
  title: Nicht-zentrale Wörter als technische Terme
  file: rules/01-words.md
  level: MUST
- id: STG-1.7
  title: Technisches Substantiv ist nicht automatisch Verb
  file: rules/01-words.md
  level: MUST
- id: STG-1.8
  title: Offizielle technische Benennungen
  file: rules/01-words.md
  level: MUST
- id: STG-1.9
  title: Neue technische Benennungen kurz halten
  file: rules/01-words.md
  level: SHOULD
- id: STG-1.10
  title: Keine regionale Sprache, Umgangssprache oder Jargon
  file: rules/01-words.md
  level: MUST_NOT
- id: STG-1.11
  title: Ein Konzept, eine Benennung
  file: rules/01-words.md
  level: MUST
- id: STG-1.12
  title: Technische Verben
  file: rules/01-words.md
  level: MUST
- id: STG-1.13
  title: Technisches Verb ist nicht automatisch Substantiv
  file: rules/01-words.md
  level: MUST
- id: STG-1.14
  title: Deutsche Standardschreibung
  file: rules/01-words.md
  level: MUST
- id: STG-2.1
  title: Semantische Dichte technischer Benennungen begrenzen
  file: rules/02-compounds-and-terms.md
  level: MUST
- id: STG-2.2
  title: Lange offizielle Benennung zuerst vollständig
  file: rules/02-compounds-and-terms.md
  level: MUST
- id: STG-DE-2.1
  title: Deutsche Komposita als Terminologieobjekte
  file: rules/02-compounds-and-terms.md
  level: MUST
- id: STG-DE-2.2
  title: Bindestriche nicht zur scheinbaren Verkürzung verwenden
  file: rules/02-compounds-and-terms.md
  level: MUST_NOT
- id: STG-DE-2.3
  title: Abkürzungen sparsam und stabil verwenden
  file: rules/02-compounds-and-terms.md
  level: MUST
- id: STG-3.1
  title: Nur freigegebene Verbformen
  file: rules/03-verbs.md
  level: MUST
- id: STG-3.2
  title: Kontrollierte Tempora und Modi
  file: rules/03-verbs.md
  level: MUST
- id: STG-3.3
  title: Partizip II für Zustand oder Attribut
  file: rules/03-verbs.md
  level: MUST
- id: STG-3.4
  title: Keine unnötigen Hilfsverbketten
  file: rules/03-verbs.md
  level: MUST_NOT
- id: STG-3.5
  title: Keine englische `-ing`-Sonderregel; kontrolliere deutsche Nominalisierung
  file: rules/03-verbs.md
  level: MUST
- id: STG-3.6
  title: Aktiv bevorzugen
  file: rules/03-verbs.md
  level: MUST
- id: STG-3.7
  title: Handlungen mit direkten Verben ausdrücken
  file: rules/03-verbs.md
  level: MUST
- id: STG-DE-3.1
  title: Trennbare Verben prüfen und begrenzen
  file: rules/03-verbs.md
  level: SHOULD
- id: STG-DE-3.2
  title: Modalität eindeutig kodieren
  file: rules/03-verbs.md
  level: MUST
- id: STG-DE-3.3
  title: '`werden` restriktiv verwenden'
  file: rules/03-verbs.md
  level: SHOULD_NOT
- id: STG-4.1
  title: Kurze, eindeutige Sätze
  file: rules/04-sentences.md
  level: MUST
- id: STG-4.2
  title: Keine bedeutungstragenden Auslassungen
  file: rules/04-sentences.md
  level: MUST_NOT
- id: STG-4.3
  title: Vertikale Listen für komplexe Aufzählungen
  file: rules/04-sentences.md
  level: MUST
- id: STG-4.4
  title: Logische Verknüpfungen explizit angeben
  file: rules/04-sentences.md
  level: MUST
- id: STG-4.5
  title: Artikel und Demonstrativa eindeutig verwenden
  file: rules/04-sentences.md
  level: MUST
- id: STG-DE-4.1
  title: Nebensatzverschachtelung begrenzen
  file: rules/04-sentences.md
  level: MUST
- id: STG-DE-4.2
  title: Pronomen nur mit eindeutigem Bezug
  file: rules/04-sentences.md
  level: MUST
- id: STG-DE-4.3
  title: '`man` nicht als technischer Akteur verwenden'
  file: rules/04-sentences.md
  level: MUST_NOT
- id: STG-DE-4.4
  title: Negationsbereich eindeutig festlegen
  file: rules/04-sentences.md
  level: MUST
- id: STG-DE-4.5
  title: Pronominaladverbien nur mit eindeutigem Bezug
  file: rules/04-sentences.md
  level: MUST
- id: STG-5.1
  title: Maximal 20 Wörter je Satz in anleitendem Text
  file: rules/05-procedures.md
  level: MUST
- id: STG-5.2
  title: Eine Anweisung je Satz
  file: rules/05-procedures.md
  level: MUST
- id: STG-5.3
  title: Anweisungen in einer festgelegten Anredeform
  file: rules/05-procedures.md
  level: MUST
- id: STG-5.4
  title: Bedingung vor Anweisung
  file: rules/05-procedures.md
  level: MUST
- id: STG-5.5
  title: Hinweise enthalten keine Anweisungen
  file: rules/05-procedures.md
  level: MUST
- id: STG-6.1
  title: Informationen schrittweise geben
  file: rules/06-descriptions.md
  level: MUST
- id: STG-6.2
  title: Schlüsselwörter und feste Verknüpfungen wiederverwenden
  file: rules/06-descriptions.md
  level: MUST
- id: STG-6.3
  title: Maximal 25 Wörter je beschreibendem Satz
  file: rules/06-descriptions.md
  level: MUST
- id: STG-6.4
  title: Verwandte Informationen in Absätzen gruppieren
  file: rules/06-descriptions.md
  level: MUST
- id: STG-6.5
  title: Ein Thema je Absatz
  file: rules/06-descriptions.md
  level: MUST
- id: STG-6.6
  title: Maximal sechs Sätze je Absatz
  file: rules/06-descriptions.md
  level: MUST
- id: STG-7.1
  title: Risikostufe eindeutig kennzeichnen
  file: rules/07-safety.md
  level: MUST
- id: STG-7.2
  title: Schutzhandlung oder Bedingung zuerst
  file: rules/07-safety.md
  level: MUST
- id: STG-7.3
  title: Gefahr oder Folge nennen
  file: rules/07-safety.md
  level: MUST
- id: STG-8.1
  title: Standardsatzzeichen und kein Semikolon zum Verbinden von Aussagen
  file: rules/08-punctuation-and-counting.md
  level: MUST_NOT
- id: STG-8.2
  title: Bindestriche nur für echte Wortstruktur
  file: rules/08-punctuation-and-counting.md
  level: MUST
- id: STG-8.3
  title: Klammern restriktiv verwenden
  file: rules/08-punctuation-and-counting.md
  level: MUST
- id: STG-8.4
  title: Doppelpunkt beendet die Einleitung einer vertikalen Liste
  file: rules/08-punctuation-and-counting.md
  level: MUST
- id: STG-8.5
  title: Klammertext separat prüfen
  file: rules/08-punctuation-and-counting.md
  level: MUST
- id: STG-8.6
  title: Geschützte Einheiten zählen als ein Wort
  file: rules/08-punctuation-and-counting.md
  level: MUST
- id: STG-8.7
  title: Bindestrichkomposita zählen orthografisch als ein Wort
  file: rules/08-punctuation-and-counting.md
  level: MUST
- id: STG-DE-8.1
  title: Schrägstrichkombinationen vermeiden
  file: rules/08-punctuation-and-counting.md
  level: SHOULD_NOT
- id: STG-9.1
  title: Satz neu bauen, wenn Wortersatz nicht reicht
  file: rules/09-writing-practices.md
  level: MUST
- id: STG-9.2
  title: Freigegebene Wörter korrekt verwenden
  file: rules/09-writing-practices.md
  level: MUST
- id: STG-9.3
  title: Keine idiomatischen Verbgefüge als Ersatz für direkte Verben
  file: rules/09-writing-practices.md
  level: MUST_NOT
- id: STG-9.4
  title: Terminologie und Formulierungen konsistent halten
  file: rules/09-writing-practices.md
  level: MUST
- id: STG-GR-1
  title: Nebensatzmarker explizit und korrekt
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-2
  title: '`mit` auf Mehrdeutigkeit prüfen'
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-3
  title: Pronomen sparsam verwenden
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-4
  title: Demonstrativa mit Nomen verwenden
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-5
  title: Lehnübersetzungen und falsche Freunde prüfen
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-6
  title: Abkürzungen in Fließtext reduzieren
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-7
  title: Neutrale Personenbezeichnungen bevorzugen
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-GR-8
  title: Genitivketten vermeiden
  file: rules/09-writing-practices.md
  level: RECOMMENDATION
- id: STG-DE-9.1
  title: Modalpartikeln und rhetorische Füllwörter vermeiden
  file: rules/09-writing-practices.md
  level: MUST_NOT
- id: STG-DE-9.2
  title: Vage Qualitäts- und Zeitangaben ersetzen
  file: rules/09-writing-practices.md
  level: MUST

```

---

## Strukturierter Anhang: `mapping/ste100-issue9.yaml`

```yaml
# Traceability: ASD-STE100 Issue 9 -> STG-DE
#
# This file records which STG-DE rule implements the intent of each ASD-STE100
# Issue 9 (January 2025) writing rule and general recommendation.
#
# Copyright boundary: this file contains only ASD-STE100 rule numbers and
# independently written German notes. It does not reproduce rule wording,
# examples, or dictionary content from ASD-STE100. ASD-STE100 is a copyright and
# trademark of ASD, Brussels. Obtain the official standard free of charge from
# https://www.asd-ste100.org.
#
# relation values:
#   equivalent  - same intent; German wording and examples are independent.
#   adapted     - same intent; scope, thresholds, or mechanics adapted to German.
#   replaced    - the source rule targets an English-specific phenomenon; STG-DE
#                 replaces it with the German phenomenon that carries the same risk.
schema_version: '0.2'
source:
  standard: ASD-STE100
  issue: '9'
  date: '2025-01-15'
  official_url: https://www.asd-ste100.org
  writing_rule_count: 53
  general_recommendation_count: 8
sections:
  '1': Wörter
  '2': Mehrwortbenennungen
  '3': Verben
  '4': Sätze
  '5': Prozeduren
  '6': Beschreibungen
  '7': Sicherheitshinweise
  '8': Zeichensetzung und Wortzählung
  '9': Schreibpraxis
mappings:
- ste: '1.1'
  stg: [STG-1.1]
  relation: equivalent
  note: Zentraler Wortschatz plus technische Substantive und Verben aus dem Projektglossar.
- ste: '1.2'
  stg: [STG-1.2]
  relation: equivalent
  note: Die Wortart ist Teil jedes Lexikoneintrags.
- ste: '1.3'
  stg: [STG-1.3]
  relation: equivalent
  note: Jede Bedeutung hat eine eigene ID im Lexikon (meanings[].id).
- ste: '1.4'
  stg: [STG-1.4]
  relation: adapted
  note: Deutsche Flexion (Kasus, Genus, Numerus, Konjugation) statt weniger englischer Formen; Kollisionen zwischen Flexionsformen werden im Lexikon geführt.
- ste: '1.5'
  stg: [STG-1.5]
  relation: equivalent
  note: Kategorien technischer Substantive werden für das Deutsche beibehalten.
- ste: '1.6'
  stg: [STG-1.6]
  relation: equivalent
  note: Nicht-zentrale Wörter nur als technische Benennung oder Teil davon.
- ste: '1.7'
  stg: [STG-1.7]
  relation: equivalent
  note: Gilt im Deutschen auch für Konversion (z. B. Substantiv zu Verb auf -ieren).
- ste: '1.8'
  stg: [STG-1.8]
  relation: equivalent
  note: Firmen-, Branchen- und Fachterminologie hat Vorrang; im Projekt über .stg-de.yaml.
- ste: '1.9'
  stg: [STG-1.9]
  relation: equivalent
  note: STG-DE führt die Regel als SHOULD, weil Kürze bei deutschen Komposita mit Eindeutigkeit konkurriert.
- ste: '1.10'
  stg: [STG-1.10]
  relation: equivalent
  note: Regionale Varianten, Umgangssprache und Jargon sind ausgeschlossen.
- ste: '1.11'
  stg: [STG-1.11]
  related: [STG-9.4]
  relation: equivalent
  note: Ein Konzept, eine Benennung; im Linter teilweise über preferred_terms prüfbar.
- ste: '1.12'
  stg: [STG-1.12]
  relation: equivalent
  note: Kategorien technischer Verben werden für das Deutsche beibehalten.
- ste: '1.13'
  stg: [STG-1.13]
  relation: equivalent
  note: Gilt im Deutschen besonders für substantivierte Infinitive.
- ste: '1.14'
  stg: [STG-1.14]
  relation: replaced
  note: Statt amerikanischer Schreibung gilt die deklarierte deutsche Rechtschreibung (Standard de-DE).
- ste: '2.1'
  stg: [STG-2.1]
  related: [STG-DE-2.1, STG-DE-2.2]
  relation: adapted
  note: Deutsche Komposita schreiben Mehrwortbenennungen zusammen; STG-DE begrenzt deshalb die Zahl der Bedeutungsbestandteile statt der Wortzahl.
- ste: '2.2'
  stg: [STG-2.2]
  related: [STG-DE-2.3]
  relation: equivalent
  note: Lange Benennung zuerst vollständig, danach eine stabile Kurzform.
- ste: '3.1'
  stg: [STG-3.1]
  relation: equivalent
  note: Nur Verbformen, die das Lexikon für den Eintrag erlaubt.
- ste: '3.2'
  stg: [STG-3.2]
  related: [STG-DE-3.3]
  relation: adapted
  note: Formaler Imperativ für Anweisungen, Präsens für Beschreibungen; Präteritum, Perfekt und Futur nur bei echtem Zeitbezug.
- ste: '3.3'
  stg: [STG-3.3]
  relation: equivalent
  note: Partizip II für Zustand oder Attribut.
- ste: '3.4'
  stg: [STG-3.4]
  related: [STG-DE-3.3]
  relation: adapted
  note: Gilt für deutsche Hilfs- und Modalverbketten (z. B. "muss geprüft worden sein").
- ste: '3.5'
  stg: [STG-3.5]
  relation: replaced
  note: Das Deutsche hat keine -ing-Form; das gleiche Risiko liegt in produktiver Nominalisierung.
- ste: '3.6'
  stg: [STG-3.6]
  related: [STG-DE-3.3, STG-DE-4.3]
  relation: adapted
  note: Aktiv als Standard; Vorgangspassiv mit "werden" nur bei unbekanntem oder irrelevantem Akteur in Beschreibungen.
- ste: '3.7'
  stg: [STG-3.7]
  related: [STG-9.3]
  relation: adapted
  note: Gilt im Deutschen besonders für Funktionsverbgefüge ("zur Anwendung bringen").
- ste: '4.1'
  stg: [STG-4.1]
  related: [STG-DE-4.1]
  relation: adapted
  note: Ergänzt um die Begrenzung von Nebensatzverschachtelung und langen Satzklammern.
- ste: '4.2'
  stg: [STG-4.2]
  relation: adapted
  note: Kontraktionen sind im Deutschen vor allem Präposition plus Artikel (am, im, zum); sie sind zulässig, wenn das Lexikon sie führt.
- ste: '4.3'
  stg: [STG-4.3]
  related: [STG-8.4]
  relation: equivalent
  note: Vertikale Listen für komplexe Aufzählungen und Bedingungen.
- ste: '4.4'
  stg: [STG-4.4]
  related: [STG-DE-4.5]
  relation: adapted
  note: Logische Verknüpfungen explizit; Pronominaladverbien als Verknüpfung brauchen einen eindeutigen Bezug.
- ste: '4.5'
  stg: [STG-4.5]
  related: [STG-GR-4]
  relation: adapted
  note: Neu in Issue 9. Im Deutschen tragen Artikel zusätzlich Kasus und Genus und machen den Bezug eindeutig.
- ste: '5.1'
  stg: [STG-5.1]
  relation: equivalent
  note: Höchstens 20 Wörter je Satz in Prozeduren; deterministisch geprüft.
- ste: '5.2'
  stg: [STG-5.2]
  relation: equivalent
  note: Eine Anweisung je Satz, außer bei gleichzeitigen Handlungen.
- ste: '5.3'
  stg: [STG-5.3]
  relation: adapted
  note: Imperativ in der Anredeform des Projekts (sie, du oder infinitiv; Standard sie). Ein Dokumentsatz verwendet genau eine Form (STG-2026-001).
- ste: '5.4'
  stg: [STG-5.4]
  relation: equivalent
  note: Bedingung vor der Anweisung, getrennt durch Komma.
- ste: '5.5'
  stg: [STG-5.5]
  relation: equivalent
  note: Hinweise informieren und enthalten keine Anweisungen.
- ste: '6.1'
  stg: [STG-6.1]
  relation: equivalent
  note: Informationen schrittweise geben.
- ste: '6.2'
  stg: [STG-6.2]
  relation: equivalent
  note: Schlüsselwörter und feste Verknüpfungen wiederverwenden.
- ste: '6.3'
  stg: [STG-6.3]
  relation: equivalent
  note: Höchstens 25 Wörter je Satz in Beschreibungen; deterministisch geprüft.
- ste: '6.4'
  stg: [STG-6.4]
  relation: equivalent
  note: Verwandte Informationen in Absätzen gruppieren.
- ste: '6.5'
  stg: [STG-6.5]
  relation: equivalent
  note: Ein Thema je Absatz.
- ste: '6.6'
  stg: [STG-6.6]
  relation: equivalent
  note: Höchstens sechs Sätze je Absatz; deterministisch geprüft.
- ste: '7.1'
  stg: [STG-7.1]
  relation: adapted
  note: Deutsche Signalwörter (GEFAHR, WARNUNG, VORSICHT, HINWEIS) nach der geltenden Norm des Projekts, z. B. ISO 3864 oder ANSI Z535.
- ste: '7.2'
  stg: [STG-7.2]
  relation: equivalent
  note: Sicherheitshinweis beginnt mit Schutzhandlung oder Bedingung.
- ste: '7.3'
  stg: [STG-7.3]
  relation: equivalent
  note: Gefahr oder Folge nennen.
- ste: '8.1'
  stg: [STG-8.1]
  relation: adapted
  note: Deutsche Standardzeichensetzung ohne Semikolon; Kommaregeln der deutschen Rechtschreibung bleiben unberührt.
- ste: '8.2'
  stg: [STG-8.2]
  related: [STG-DE-2.2]
  relation: adapted
  note: Bindestriche nur für echte Wortstruktur, nicht zum Zerlegen unklarer Komposita.
- ste: '8.3'
  stg: [STG-8.3]
  relation: equivalent
  note: Klammern nur für die zulässigen Zwecke.
- ste: '8.4'
  stg: [STG-8.4]
  relation: equivalent
  note: Doppelpunkt vor vertikaler Liste wirkt beim Zählen wie ein Satzende.
- ste: '8.5'
  stg: [STG-8.5]
  relation: adapted
  note: Klammertext zählt als ein Wort; STG-DE prüft den Klammerinhalt zusätzlich separat.
- ste: '8.6'
  stg: [STG-8.6]
  relation: equivalent
  note: Zahlen, Zahl plus Einheit, Abkürzungen, Kennungen, Zitate, Titel und Eigennamen zählen je als ein Wort.
- ste: '8.7'
  stg: [STG-8.7]
  relation: equivalent
  note: Bindestrichkomposita zählen als ein Wort.
- ste: '9.1'
  stg: [STG-9.1]
  relation: equivalent
  note: Satz neu bauen, wenn ein Wortersatz nicht reicht.
- ste: '9.2'
  stg: [STG-9.2]
  relation: equivalent
  note: Freigegebene Wörter korrekt verwenden.
- ste: '9.3'
  stg: [STG-9.3]
  related: [STG-DE-3.1]
  relation: replaced
  note: Englische Phrasal Verbs entsprechen im Deutschen idiomatischen Verbgefügen und Funktionsverbgefügen; trennbare Verben regelt STG-DE-3.1.
- ste: '9.4'
  stg: [STG-9.4]
  related: [STG-1.11]
  relation: equivalent
  note: Terminologie und Formulierungen konsistent halten.
general_recommendations:
- ste: GR-1
  stg: [STG-GR-1]
  relation: replaced
  note: Statt des englischen "that" geht es um explizite deutsche Nebensatzmarker (dass, ob, wenn, weil).
- ste: GR-2
  stg: [STG-GR-2]
  relation: equivalent
  note: '"mit" auf Mehrdeutigkeit prüfen (Werkzeug, Begleitung, Eigenschaft).'
- ste: GR-3
  stg: [STG-GR-3]
  related: [STG-DE-4.2]
  relation: equivalent
  note: Pronomen sparsam und nur mit eindeutigem Bezug.
- ste: GR-4
  stg: [STG-GR-4]
  related: [STG-4.5]
  relation: adapted
  note: Demonstrativa (dieser, diese, dieses) immer mit Nomen.
- ste: GR-5
  stg: [STG-GR-5]
  relation: adapted
  note: Falsche Freunde und Lehnübersetzungen aus dem Englischen prüfen.
- ste: GR-6
  stg: [STG-GR-6]
  related: [STG-DE-2.3]
  relation: adapted
  note: Abkürzungen im Fließtext reduzieren, auch deutsche (z. B. bzw., ggf., u. a.).
- ste: GR-7
  stg: [STG-GR-7]
  relation: adapted
  note: Neutrale Personenbezeichnungen, ohne die Lesbarkeit zu verschlechtern.
- ste: GR-8
  stg: [STG-GR-8]
  relation: replaced
  note: Statt der englischen Possessivform geht es um deutsche Genitivketten.
# STG-DE rules without a direct ASD-STE100 counterpart. They cover ambiguity
# sources that are specific to German or that STE100 handles only implicitly.
german_extensions:
- stg: STG-DE-2.1
  nearest_ste: ['2.1']
  reason: Komposita sind Terminologieobjekte und werden im Projektglossar geführt.
- stg: STG-DE-2.2
  nearest_ste: ['8.2']
  reason: Bindestriche dürfen unklare Komposita nicht verstecken.
- stg: STG-DE-2.3
  nearest_ste: ['2.2']
  reason: Abkürzungen stabil und sparsam einführen.
- stg: STG-DE-3.1
  nearest_ste: ['9.3']
  reason: Abgetrennte Verbpartikeln am Satzende erzeugen lange Klammern.
- stg: STG-DE-3.2
  nearest_ste: ['3.4']
  reason: Deutsche Modalverben (muss, soll, sollte, kann, darf) brauchen eine feste Bedeutung.
- stg: STG-DE-3.3
  nearest_ste: ['3.2', '3.6']
  reason: werden ist zugleich Futur-, Passiv- und Vollverb.
- stg: STG-DE-4.1
  nearest_ste: ['4.1']
  reason: Verschachtelte Nebensätze und lange Satzklammern.
- stg: STG-DE-4.2
  nearest_ste: [GR-3]
  reason: Genus und Kasus machen Pronomenbezüge im Deutschen oft mehrdeutig.
- stg: STG-DE-4.3
  nearest_ste: ['3.6']
  reason: man versteckt den Akteur wie ein Passiv.
- stg: STG-DE-4.4
  nearest_ste: ['4.1']
  reason: Die Stellung von nicht, kein und nur ändert den Bezugsbereich.
- stg: STG-DE-4.5
  nearest_ste: ['4.4', GR-3]
  reason: Pronominaladverbien (dabei, dazu, davon) haben oft keinen eindeutigen Bezug.
- stg: STG-DE-8.1
  nearest_ste: ['8.1']
  reason: Schrägstrichformen wie und/oder sind logisch mehrdeutig.
- stg: STG-DE-9.1
  nearest_ste: ['9.1']
  reason: Modalpartikeln (ja, eben, halt, mal) tragen keine technische Information.
- stg: STG-DE-9.2
  nearest_ste: ['1.3']
  reason: Vage Angaben (zeitnah, ordnungsgemäß, ausreichend) ohne messbares Kriterium.

```

---

## Strukturierter Anhang: `dictionary/approved-words.yaml`

```yaml
schema_version: '0.1'
release: 0.3.0
status: multi_industry_corpus_validated_authoring_core
language: de-DE
normative_for_profile: STG-C-core
design_basis:
  source: independent German lexical design
  human_linguistic_review: not_yet_completed
  corpus_validation: v0.1_stratified_multi_industry_public_excerpt_corpus
entries:
- entry_id: DE-PRE-ab
  lemma: ab
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.from_starting_point
    definition: kennzeichnet einen ausdrücklich genannten zeitlichen, räumlichen oder numerischen Ausgangspunkt
  review_status: corpus_candidate_v0.0.3
  restrictions:
  - Ausgangspunkt ausdrücklich nennen.
- entry_id: DE-VER-abbrechen
  lemma: abbrechen
  part_of_speech: verb
  status: approved
  meanings:
  - id: abort
    definition: einen laufenden Vorgang vor seinem regulären Ende beenden
  review_status: provisional_v0.0.2
  separable: true
  prefix: ab
  approved_examples:
  - Brechen Sie den Test ab, wenn die Temperatur 80 °C überschreitet.
- entry_id: DE-VER-abdichten
  lemma: abdichten
  part_of_speech: verb
  status: restricted
  meanings:
  - id: seal
    definition: eine Verbindung oder Oberfläche so herstellen, dass das festgelegte Medium innerhalb der spezifizierten
      Leckagegrenze nicht austritt
  review_status: provisional_v0.0.2
  separable: true
  prefix: ab
  restrictions:
  - Dichtheitskriterium muss aus Verfahren oder Spezifikation hervorgehen.
- entry_id: DE-CON-aber
  lemma: aber
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.but
    definition: kennzeichnet einen direkten Gegensatz oder eine Einschränkung zur vorherigen Aussage
  review_status: provisional_v0.0.2
- entry_id: DE-VER-abkuehlen
  lemma: abkühlen
  part_of_speech: verb
  status: approved
  meanings:
  - id: cool.down
    definition: die Temperatur eines Objekts oder Mediums verringern oder sinken lassen
  review_status: corpus_candidate_v0.0.3
  separable: true
  prefix: ab
  surface_forms:
  - abgekühlt
  approved_examples:
  - Lassen Sie das Gerät auf 40 °C abkühlen.
- entry_id: DE-VER-ablassen
  lemma: ablassen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: drain.release
    definition: Flüssigkeit, Gas oder Druck kontrolliert aus einem System ausströmen lassen
  review_status: provisional_v0.0.2
  separable: true
  prefix: ab
  restrictions:
  - 'Objekt nennen: Flüssigkeit, Gas oder Druck.'
- entry_id: DE-VER-abschlie-en
  lemma: abschließen
  part_of_speech: verb
  status: approved
  meanings:
  - id: complete.finish
    definition: einen Vorgang regulär beenden und als beendet kennzeichnen
  review_status: provisional_v0.0.2
  separable: true
  prefix: ab
  restrictions:
  - Nicht mit verriegeln oder verschließen verwechseln.
- entry_id: DE-NOU-abschnitt
  lemma: Abschnitt
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.section
    definition: klar abgegrenzter Teil eines Dokuments oder einer Struktur
  review_status: provisional_v0.0.2
  gender: masc
  plural: Abschnitte
- entry_id: DE-NOU-abstand
  lemma: Abstand
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.distance
    definition: räumliche Entfernung zwischen zwei ausdrücklich bestimmten Punkten, Flächen oder Objekten
  review_status: provisional_v0.0.2
  gender: masc
  plural: Abstände
- entry_id: DE-VER-abziehen
  lemma: abziehen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: pull.remove
    definition: einen Steckverbinder, eine Abdeckung oder ein vergleichbares Teil durch Ziehen von seiner Verbindung
      entfernen
  review_status: corpus_candidate_v0.0.3
  separable: true
  prefix: ab
  surface_forms:
  - abgezogen
  restrictions:
  - Objekt und Verbindung müssen eindeutig sein. Für mathematische Subtraktion subtrahieren verwenden.
- entry_id: DE-QUA-acht
  lemma: acht
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.eight
    definition: bezeichnet die Zahl 8 in ausgeschriebener Form
  review_status: corpus_candidate_v0.0.3
- entry_id: DE-VER-addieren
  lemma: addieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: add.math
    definition: zwei oder mehr numerische Werte mathematisch zusammenzählen
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-aktiv
  lemma: aktiv
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.active
    definition: in einem freigegebenen eingeschalteten oder wirksamen Zustand
  review_status: provisional_v0.0.2
- entry_id: DE-VER-aktivieren
  lemma: aktivieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: activate
    definition: eine Funktion oder ein System in den freigegebenen aktiven Zustand bringen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-aktualisieren
  lemma: aktualisieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: update
    definition: Daten oder Software auf einen ausdrücklich bezeichneten neueren Stand bringen
  review_status: provisional_v0.0.2
  restrictions:
  - Zielversion oder Quelle nennen, wenn für die Aufgabe relevant.
- entry_id: DE-DET-alle
  lemma: alle
  part_of_speech: determiner
  status: approved
  meanings:
  - id: determiner.all
    definition: bezeichnet die Gesamtheit einer klar bestimmten Menge
  review_status: provisional_v0.0.2
  surface_forms:
  - alle
  - aller
  - allen
  approved_examples:
  - Entfernen Sie alle Schrauben.
- entry_id: DE-CON-als
  lemma: als
  part_of_speech: conjunction
  status: restricted
  meanings:
  - id: conj.comparison
    definition: kennzeichnet den Vergleich nach einer ausdrücklich genannten Vergleichsgröße
  - id: conj.role
    definition: kennzeichnet die ausdrücklich benannte Funktion oder Rolle eines Objekts
  review_status: corpus_candidate_v0.0.3
  restrictions:
  - Nicht als unspezifischen zeitlichen Erzähler verwenden. Vergleichsgröße oder Rolle muss eindeutig sein.
  approved_examples:
  - Der Druck muss größer als 5 bar sein.
  - Verwenden Sie Anschluss X1 als Referenz.
- entry_id: DE-PRE-an
  lemma: an
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.at_on
    definition: kennzeichnet Kontakt, unmittelbare Nähe oder eine definierte Position an einem Objekt
  review_status: provisional_v0.0.2
- entry_id: DE-VER-analysieren
  lemma: analysieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: analyze
    definition: Daten, Material oder einen Fehler systematisch in Bestandteile oder Ursachen untersuchen
  review_status: provisional_v0.0.2
  restrictions:
  - Analyseziel und Datenbasis angeben, wenn sie nicht aus dem Kontext eindeutig sind.
- entry_id: DE-NOU-anfang
  lemma: Anfang
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.start
    definition: erster Punkt oder erste Phase eines ausdrücklich bestimmten Ablaufs oder Bereichs
  review_status: provisional_v0.0.2
  gender: masc
  plural: Anfänge
- entry_id: DE-NOU-angabe
  lemma: Angabe
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.angabe
    definition: ausdrücklich genannter technischer Wert oder dokumentierte Information
  review_status: multi_industry_candidate_v0.1
  plural: Angaben
  restrictions:
  - Wenn möglich den konkreten Informationstyp nennen, zum Beispiel Wert, Maß oder Datum.
- entry_id: DE-NOU-anleitung
  lemma: Anleitung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.anleitung
    definition: Dokument oder abgegrenzter Dokumentteil mit Informationen oder Anweisungen zur Verwendung eines
      Produkts
  review_status: multi_industry_candidate_v0.1
  plural: Anleitungen
  restrictions:
  - Wenn ein offizieller Dokumenttitel vorhanden ist, diesen Titel verwenden.
- entry_id: DE-VER-anpassen
  lemma: anpassen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: adapt.adjust
    definition: einen Parameter, eine Verbindung oder ein Objekt an eine ausdrücklich genannte Anforderung oder
      Referenz angleichen
  review_status: provisional_v0.0.2
  restrictions:
  - Referenz oder Zielzustand nennen.
  surface_forms:
  - angepasst
- entry_id: DE-VER-anschliessen
  lemma: anschließen
  part_of_speech: verb
  status: approved
  meanings:
  - id: connect.interface
    definition: ein Kabel, einen Steckverbinder oder ein Gerät mit einer ausdrücklich genannten Schnittstelle elektrisch
      oder funktional verbinden
  review_status: corpus_candidate_v0.0.3
  separable: true
  prefix: an
  surface_forms:
  - angeschlossen
  approved_examples:
  - Schließen Sie das Kabel an Anschluss X1 an.
- entry_id: DE-VER-anwenden
  lemma: anwenden
  part_of_speech: verb
  status: approved
  meanings:
  - id: apply.method
    definition: ein Verfahren, eine Regel oder ein Mittel für den vorgesehenen Zweck verwenden
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-anzahl
  lemma: Anzahl
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.count
    definition: gezählte Menge diskreter Elemente
  review_status: provisional_v0.0.2
  gender: fem
  plural: Anzahlen
- entry_id: DE-VER-anzeigen
  lemma: anzeigen
  part_of_speech: verb
  status: approved
  meanings:
  - id: display
    definition: Information auf einem Display, Instrument oder einer Benutzeroberfläche sichtbar ausgeben
  review_status: provisional_v0.0.2
  separable: true
  prefix: an
- entry_id: DE-NOU-art
  lemma: Art
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.type
    definition: klar definierte Kategorie oder Klasse von Elementen
  review_status: provisional_v0.0.2
  gender: fem
  plural: Arten
- entry_id: DE-ADV-auch
  lemma: auch
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.also
    definition: fügt ein weiteres ausdrücklich genanntes Element mit derselben Aussage hinzu
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht verwenden, wenn unklar ist, auf welchen Satzteil sich auch bezieht.
- entry_id: DE-PRE-auf
  lemma: auf
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.on_to
    definition: kennzeichnet eine Position auf einer Oberfläche oder ein festgelegtes Ziel einer Einstellung
  review_status: provisional_v0.0.2
- entry_id: DE-VER-aufbewahren
  lemma: aufbewahren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: store.physical
    definition: einen Gegenstand oder ein Dokument an einem ausdrücklich festgelegten Ort für spätere Verwendung
      lagern
  review_status: corpus_candidate_v0.0.3
  separable: true
  prefix: auf
  surface_forms:
  - aufbewahrt
  restrictions:
  - Ort oder Aufbewahrungsanforderung nennen, wenn sie für die Sicherheit oder Funktion relevant ist.
- entry_id: DE-VER-auffangen
  lemma: auffangen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: collect.flow
    definition: austretende Flüssigkeit, Partikel oder Material in einem geeigneten Behälter oder Hilfsmittel sammeln
  review_status: corpus_candidate_v0.0.3
  separable: true
  prefix: auf
  surface_forms:
  - aufgefangen
  restrictions:
  - Medium und Auffangmittel nennen, wenn sie nicht aus dem Arbeitsschritt eindeutig sind.
- entry_id: DE-NOU-aufgabe
  lemma: Aufgabe
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.task
    definition: abgegrenzte technische Tätigkeit mit einem definierten Ziel
  review_status: provisional_v0.0.2
  gender: fem
  plural: Aufgaben
- entry_id: DE-VER-aufladen
  lemma: aufladen
  part_of_speech: verb
  status: approved
  meanings:
  - id: charge.battery
    definition: einen elektrischen Energiespeicher mit Energie laden
  review_status: provisional_v0.0.2
  separable: true
  prefix: auf
- entry_id: DE-VER-auflisten
  lemma: auflisten
  part_of_speech: verb
  status: approved
  meanings:
  - id: list
    definition: mehrere Elemente in einer ausdrücklich strukturierten Liste nennen
  review_status: provisional_v0.0.2
  separable: true
  prefix: auf
- entry_id: DE-VER-auftragen
  lemma: auftragen
  part_of_speech: verb
  status: approved
  meanings:
  - id: apply.material
    definition: Material kontrolliert auf eine Oberfläche bringen
  review_status: provisional_v0.0.2
  separable: true
  prefix: auf
- entry_id: DE-VER-auftreten
  lemma: auftreten
  part_of_speech: verb
  status: restricted
  meanings:
  - id: occur
    definition: als Ereignis, Fehler oder Zustand entstehen oder vorhanden werden
  review_status: provisional_v0.0.2
  separable: true
  prefix: auf
  restrictions:
  - Nicht für räumliches Auftreten einer Person verwenden.
- entry_id: DE-VER-aufzeichnen
  lemma: aufzeichnen
  part_of_speech: verb
  status: approved
  meanings:
  - id: record
    definition: Messwerte, Ereignisse oder Signale fortlaufend als Daten speichern
  review_status: provisional_v0.0.2
  separable: true
  prefix: auf
- entry_id: DE-PRE-aus
  lemma: aus
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.from_out_of
    definition: kennzeichnet Herkunft aus einem Inneren oder Materialzusammensetzung
  review_status: provisional_v0.0.2
  restrictions:
  - Nur verwenden, wenn Herkunft oder Materialbezug eindeutig ist.
- entry_id: DE-PHR-aus-bestehen
  lemma: aus ... bestehen
  part_of_speech: phrase
  status: approved
  meanings:
  - id: consist.of
    definition: gibt die vollständig oder teilweise genannten Bestandteile eines Objekts an
  review_status: provisional_v0.0.2
- entry_id: DE-VER-ausbauen
  lemma: ausbauen
  part_of_speech: verb
  status: approved
  meanings:
  - id: remove.installed
    definition: ein eingebautes Bauteil aus seiner Einbauposition entfernen
  review_status: provisional_v0.0.2
  separable: true
  prefix: aus
- entry_id: DE-VER-ausf-hren
  lemma: ausführen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: execute.software
    definition: einen Softwarebefehl, ein Programm oder ein Skript starten und abarbeiten lassen
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht als allgemeines Füllverb für Tätigkeiten verwenden.
  surface_forms:
  - ausgeführt
- entry_id: DE-ADJ-ausgeschaltet
  lemma: ausgeschaltet
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.off
    definition: nicht im aktiven Energie- oder Betriebszustand
  review_status: provisional_v0.0.2
- entry_id: DE-VER-ausladen
  lemma: ausladen
  part_of_speech: verb
  status: approved
  meanings:
  - id: unload.cargo
    definition: Material oder Gegenstände aus einem Transport- oder Aufnahmeobjekt entfernen
  review_status: provisional_v0.0.2
  separable: true
  prefix: aus
- entry_id: DE-VER-ausrichten
  lemma: ausrichten
  part_of_speech: verb
  status: approved
  meanings:
  - id: align
    definition: ein Objekt in eine festgelegte geometrische Lage oder Richtung bringen
  review_status: provisional_v0.0.2
  separable: true
  prefix: aus
- entry_id: DE-VER-ausschalten
  lemma: ausschalten
  part_of_speech: verb
  status: approved
  meanings:
  - id: switch.off
    definition: ein Gerät, System oder eine Funktion aus dem aktiven Energie- oder Betriebszustand bringen
  review_status: provisional_v0.0.2
  separable: true
  prefix: aus
  prohibited_synonyms:
  - ausmachen
- entry_id: DE-VER-ausschneiden
  lemma: ausschneiden
  part_of_speech: verb
  status: approved
  meanings:
  - id: cut.ui
    definition: ein markiertes digitales Element entfernen und für späteres Einfügen zwischenspeichern
  review_status: provisional_v0.0.2
  separable: true
  prefix: aus
- entry_id: DE-ADV-au-en
  lemma: außen
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.outside
    definition: kennzeichnet die Außenseite oder den Außenraum eines definierten Objekts
  review_status: provisional_v0.0.2
- entry_id: DE-PHR-au-er-betrieb-sein
  lemma: außer Betrieb sein
  part_of_speech: phrase
  status: restricted
  meanings:
  - id: state.out_of_operation
    definition: kennzeichnet, dass ein System nicht für den vorgesehenen Betrieb verfügbar ist
  review_status: provisional_v0.0.2
- entry_id: DE-VER-ausw-hlen
  lemma: auswählen
  part_of_speech: verb
  status: approved
  meanings:
  - id: select
    definition: eine Option aus mehreren Optionen bestimmen
  review_status: provisional_v0.0.2
  separable: true
  prefix: aus
- entry_id: DE-NOU-baugruppe
  lemma: Baugruppe
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.assembly
    definition: aus mehreren Teilen bestehende technische Einheit
  review_status: provisional_v0.0.2
  gender: fem
  plural: Baugruppen
  restrictions:
  - Offizielle Produktbenennung hat Vorrang.
- entry_id: DE-NOU-bauteil
  lemma: Bauteil
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.component
    definition: einzelnes technisch abgegrenztes Teil eines Systems oder einer Baugruppe
  review_status: provisional_v0.0.2
  gender: neut
  plural: Bauteile
  restrictions:
  - Offizielle Produktbenennung hat Vorrang.
- entry_id: DE-VER-beachten
  lemma: beachten
  part_of_speech: verb
  status: restricted
  meanings:
  - id: heed
    definition: einen ausdrücklich genannten Hinweis, Grenzwert oder Umstand bei einer Handlung berücksichtigen
  review_status: provisional_v0.0.2
  restrictions:
  - In Arbeitsanweisungen nach Möglichkeit direkte Handlung formulieren statt beachten.
- entry_id: DE-VER-bedienen
  lemma: bedienen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: verb.bedienen
    definition: ein technisches Produkt mit den vorgesehenen Bedienelementen steuern
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - bediene
  - bedienst
  - bedient
  - bedienen
  - bediente
  - bedienten
  restrictions:
  - Nicht als allgemeines Synonym für verwenden einsetzen.
- entry_id: DE-NOU-bedienung
  lemma: Bedienung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.bedienung
    definition: Interaktion einer Person mit Bedienelementen oder einer Benutzeroberfläche
  review_status: multi_industry_candidate_v0.1
  restrictions:
  - In Verfahren das direkte Bedienverb verwenden.
- entry_id: DE-NOU-bedingung
  lemma: Bedingung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.condition
    definition: ausdrücklich definierter Zustand, der für eine Aussage oder Handlung erfüllt sein muss
  review_status: provisional_v0.0.2
  gender: fem
  plural: Bedingungen
- entry_id: DE-VER-befestigen
  lemma: befestigen
  part_of_speech: verb
  status: approved
  meanings:
  - id: attach
    definition: ein Teil so verbinden, dass es in der vorgesehenen Position gehalten wird
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-befestigt
  lemma: befestigt
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.attached
    definition: in der vorgesehenen Position mechanisch gehalten
  review_status: provisional_v0.0.2
- entry_id: DE-VER-befolgen
  lemma: befolgen
  part_of_speech: verb
  status: approved
  meanings:
  - id: obey
    definition: die Anweisungen oder Regeln eines ausdrücklich genannten Dokuments ausführen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-beheben
  lemma: beheben
  part_of_speech: verb
  status: restricted
  meanings:
  - id: correct.fault
    definition: einen ausdrücklich identifizierten Fehler oder eine ausdrücklich identifizierte Störung korrigieren
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - behebe
  - behebst
  - behebt
  - beheben
  - behob
  - behoben
  restrictions:
  - Fehler oder Störung nennen. Nicht für physisches Entfernen von Material verwenden.
- entry_id: DE-PRE-bei
  lemma: bei
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.at
    definition: kennzeichnet eine definierte Position, einen Betriebszustand oder einen Messwert
  review_status: provisional_v0.0.2
  restrictions:
  - Für Bedingungen mit Handlung nach Möglichkeit einen wenn-Satz verwenden.
- entry_id: DE-DET-beide
  lemma: beide
  part_of_speech: determiner
  status: approved
  meanings:
  - id: determiner.both
    definition: bezeichnet genau zwei zuvor bestimmte Elemente
  review_status: provisional_v0.0.2
  surface_forms:
  - beide
  - beider
  - beiden
  restrictions:
  - Nur verwenden, wenn die Menge nachweislich genau zwei Elemente enthält.
- entry_id: DE-NOU-beispiel
  lemma: Beispiel
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.beispiel
    definition: konkreter Fall, der eine Regel, Funktion oder Verwendung erläutert
  review_status: multi_industry_candidate_v0.1
  plural: Beispiele
- entry_id: DE-VER-beladen
  lemma: beladen
  part_of_speech: verb
  status: approved
  meanings:
  - id: load.cargo
    definition: Material oder Gegenstände in oder auf ein Transport- oder Aufnahmeobjekt bringen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-belueften
  lemma: belüften
  part_of_speech: verb
  status: restricted
  meanings:
  - id: ventilate
    definition: einem Bereich kontrolliert Luft zuführen oder Luft austauschen
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - belüftet
  restrictions:
  - Erforderlichen Luftstrom oder das maßgebliche Kriterium nennen, wenn relevant.
- entry_id: DE-VER-benachrichtigen
  lemma: benachrichtigen
  part_of_speech: verb
  status: approved
  meanings:
  - id: notify
    definition: einer bestimmten Person oder Stelle eine Information gezielt übermitteln
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-benennung
  lemma: Benennung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.designation
    definition: freigegebener sprachlicher Ausdruck für einen technischen Begriff
  review_status: provisional_v0.0.2
  gender: fem
  plural: Benennungen
- entry_id: DE-NOU-benutzer
  lemma: Benutzer
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.user
    definition: Person oder Systemrolle, die eine Benutzeroberfläche oder Funktion verwendet
  review_status: provisional_v0.0.2
  gender: masc
  plural: Benutzer
  restrictions:
  - Wenn Geschlechtsneutralität oder Rollenbezeichnung projektseitig anders geregelt ist, offizielle Rollenbezeichnung
    verwenden.
- entry_id: DE-VER-benoetigen
  lemma: benötigen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: verb.benoetigen
    definition: eine ausdrücklich genannte Voraussetzung, Ressource oder Komponente für eine Handlung erfordern
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - benötige
  - benötigst
  - benötigt
  - benötigen
  - benötigte
  - benötigten
  restrictions:
  - In Verfahren Voraussetzungen möglichst vor den Arbeitsschritten auflisten.
- entry_id: DE-VER-berechnen
  lemma: berechnen
  part_of_speech: verb
  status: approved
  meanings:
  - id: calculate
    definition: einen Wert mit einer festgelegten mathematischen Beziehung bestimmen
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-bereich
  lemma: Bereich
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.area
    definition: räumlich, funktional oder dokumentarisch abgegrenzter Teil
  review_status: provisional_v0.0.2
  gender: masc
  plural: Bereiche
  restrictions:
  - Art des Bereichs nennen, wenn nicht eindeutig.
- entry_id: DE-VER-bereitstellen
  lemma: bereitstellen
  part_of_speech: verb
  status: approved
  meanings:
  - id: provide.available
    definition: ein ausdrücklich genanntes Objekt, Signal, eine Ressource oder Funktion für die Verwendung verfügbar
      machen
  review_status: corpus_candidate_v0.0.3
  separable: true
  prefix: bereit
  surface_forms:
  - bereitgestellt
- entry_id: DE-VER-ber-hren
  lemma: berühren
  part_of_speech: verb
  status: approved
  meanings:
  - id: touch
    definition: physischen Kontakt mit einem Objekt oder einer Oberfläche herstellen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-beschreiben
  lemma: beschreiben
  part_of_speech: verb
  status: approved
  meanings:
  - id: describe
    definition: Eigenschaften, Aufbau, Funktion oder Ablauf eines ausdrücklich genannten Gegenstands sachlich darstellen
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - beschreibe
  - beschreibst
  - beschreibt
  - beschreiben
  - beschrieb
  - beschrieben
- entry_id: DE-NOU-beschreibung
  lemma: Beschreibung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.description
    definition: Text, der technische Information gibt und keine direkte Arbeitsanweisung ist
  review_status: provisional_v0.0.2
  gender: fem
  plural: Beschreibungen
- entry_id: DE-ADJ-besch-digt
  lemma: beschädigt
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.damaged
    definition: weist einen Schaden auf, der im anwendbaren Prüf- oder Reparaturkriterium als Schaden gilt
  review_status: provisional_v0.0.2
  restrictions:
  - Bei Akzeptanzentscheidungen Schadenskriterium oder Referenz angeben.
- entry_id: DE-VER-bestehen
  lemma: bestehen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: verb.consist_with_aus
    definition: zusammen mit der Präposition aus die Bestandteile eines ausdrücklich genannten Objekts angeben
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - bestehe
  - bestehst
  - besteht
  - bestehen
  - bestand
  - bestanden
  restrictions:
  - Nur im Muster „X besteht aus Y“ für Zusammensetzung verwenden. Andere Bedeutungen sind nicht zentral freigegeben.
- entry_id: DE-VER-best-tigen
  lemma: bestätigen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: confirm
    definition: eine Information oder Auswahl ausdrücklich als erhalten, korrekt oder akzeptiert kennzeichnen
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht verwenden, wenn eigentlich prüfen oder genehmigen gemeint ist.
- entry_id: DE-VER-betreiben
  lemma: betreiben
  part_of_speech: verb
  status: approved
  meanings:
  - id: operate.transitive
    definition: ein Gerät oder System aktiv bedienen oder in seinem vorgesehenen Betriebszustand halten
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-betreiber
  lemma: Betreiber
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.operator
    definition: Organisation oder Rolle, die ein System verantwortlich betreibt
  review_status: provisional_v0.0.2
  gender: masc
  plural: Betreiber
  restrictions:
  - Offizielle Rollenbezeichnung hat Vorrang.
- entry_id: DE-NOU-betrieb
  lemma: Betrieb
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.operation
    definition: Zustand oder Tätigkeit, in der ein System seine vorgesehene Funktion ausführt
  review_status: provisional_v0.0.2
  gender: masc
- entry_id: DE-NOU-betriebsanleitung
  lemma: Betriebsanleitung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.betriebsanleitung
    definition: offizielle Anleitung für sicheren Betrieb, Bedienung oder Instandhaltung eines Produkts
  review_status: multi_industry_candidate_v0.1
  plural: Betriebsanleitungen
- entry_id: DE-CON-bevor
  lemma: bevor
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.before
    definition: ordnet eine Handlung oder einen Zustand zeitlich vor einer anderen Handlung an
  review_status: provisional_v0.0.2
- entry_id: DE-VER-bewegen
  lemma: bewegen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: move
    definition: die Position eines Objekts ändern
  review_status: provisional_v0.0.2
  restrictions:
  - Richtung oder Ziel nennen, wenn relevant.
- entry_id: DE-VER-biegen
  lemma: biegen
  part_of_speech: verb
  status: approved
  meanings:
  - id: bend
    definition: die Form eines Werkstücks durch Biegung verändern
  review_status: provisional_v0.0.2
- entry_id: DE-VER-bilden
  lemma: bilden
  part_of_speech: verb
  status: restricted
  meanings:
  - id: form.constitute
    definition: ausdrücken, dass ausdrücklich genannte Teile zusammen eine klar bezeichnete Einheit oder Struktur
      ergeben
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - bilde
  - bildest
  - bildet
  - bilden
  - bildete
  - gebildet
  restrictions:
  - Nur für eine konkrete Zusammensetzung oder Struktur verwenden. Für „darstellen“ oder „erzeugen“ das präzisere
    Verb verwenden.
- entry_id: DE-CON-bis
  lemma: bis
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.until
    definition: kennzeichnet den Endzustand oder Endzeitpunkt einer fortgesetzten Handlung
  review_status: provisional_v0.0.2
- entry_id: DE-PRE-bis
  lemma: bis
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.up_to
    definition: kennzeichnet eine obere räumliche, zeitliche oder numerische Grenze
  review_status: provisional_v0.0.2
- entry_id: DE-VER-bleiben
  lemma: bleiben
  part_of_speech: verb
  status: approved
  meanings:
  - id: remain.state
    definition: in einem Zustand oder an einer Position fortbestehen
  review_status: provisional_v0.0.2
  surface_forms:
  - bleibe
  - bleibst
  - bleibt
  - bleiben
  - blieb
  - blieben
  - geblieben
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-ADJ-breit
  lemma: breit
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.wide
    definition: hat eine große Ausdehnung in Breitenrichtung relativ zur ausdrücklich genannten Referenz
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-breite
  lemma: Breite
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.width
    definition: lineare Abmessung in der festgelegten Breitenrichtung
  review_status: provisional_v0.0.2
  gender: fem
  plural: Breiten
- entry_id: DE-CON-damit
  lemma: damit
  part_of_speech: conjunction
  status: restricted
  meanings:
  - id: conj.so_that
    definition: leitet den ausdrücklich genannten Zweck einer Handlung ein
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht als Pronomen verwenden. Bei langen Sätzen den Zweck in einen eigenen Satz aufteilen.
- entry_id: DE-ADV-danach
  lemma: danach
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.afterwards
    definition: kennzeichnet eine Handlung oder einen Zustand nach dem unmittelbar vorher genannten Ereignis
  review_status: provisional_v0.0.2
- entry_id: DE-ADV-dann
  lemma: dann
  part_of_speech: adverb
  status: approved
  meanings:
  - id: sequence.then
    definition: kennzeichnet den ausdrücklich nächsten Schritt oder Zustand in einer zeitlichen Reihenfolge
  review_status: corpus_candidate_v0.0.3
- entry_id: DE-VER-darstellen
  lemma: darstellen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: represent.show
    definition: Information in einer Abbildung, Tabelle, Anzeige oder strukturierten Darstellung sichtbar wiedergeben
  review_status: corpus_candidate_v0.0.3
  separable: true
  prefix: dar
  surface_forms:
  - dargestellt
  restrictions:
  - Darstellung oder Informationsquelle nennen. Nicht als stilistisches Synonym für sein, bilden oder beschreiben
    verwenden.
- entry_id: DE-CON-dass
  lemma: dass
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.that
    definition: leitet einen Inhaltssatz ein, der den Inhalt einer Aussage, Prüfung oder Feststellung angibt
  review_status: provisional_v0.0.2
  approved_examples:
  - Stellen Sie sicher, dass das Ventil geschlossen ist.
- entry_id: DE-NOU-daten
  lemma: Daten
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.daten
    definition: digital oder analog dargestellte technische Informationen, Messwerte oder gespeicherte Inhalte
  review_status: multi_industry_candidate_v0.1
  plural: Daten
  restrictions:
  - Nicht als Plural von Datum interpretieren. Kontext muss technische Informationen oder Werte bezeichnen.
  approved_examples:
  - Speichern Sie die Daten.
- entry_id: DE-NOU-datum
  lemma: Datum
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.date
    definition: Kalenderangabe eines bestimmten Tages
  review_status: corrected_v0.1_lexical_collision
  gender: neut
  plural: Daten
  restrictions:
  - Im technischen Informationskontext bezeichnet Daten das eigene Lemma Daten und nicht den Plural von Datum.
- entry_id: DE-NOU-dauer
  lemma: Dauer
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.duration
    definition: Zeitspanne zwischen Beginn und Ende eines Ereignisses
  review_status: provisional_v0.0.2
  gender: fem
  plural: Dauern
- entry_id: DE-ADV-davor
  lemma: davor
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.beforehand
    definition: kennzeichnet eine Handlung oder einen Zustand vor dem unmittelbar danach genannten oder zuvor referenzierten
      Ereignis
  review_status: provisional_v0.0.2
  restrictions:
  - Nur verwenden, wenn der Bezug eindeutig ist.
- entry_id: DE-VER-deaktivieren
  lemma: deaktivieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: deactivate
    definition: eine Funktion oder ein System in den freigegebenen inaktiven Zustand bringen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-definieren
  lemma: definieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: define
    definition: Bedeutung, Grenze, Parameter oder Eigenschaft eines ausdrücklich genannten Elements verbindlich
      festlegen
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - definiere
  - definierst
  - definiert
  - definieren
  - definierte
- entry_id: DE-VER-deinstallieren
  lemma: deinstallieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: uninstall.software
    definition: installierte Software kontrolliert aus einem System entfernen
  review_status: provisional_v0.0.2
- entry_id: DE-ART-der
  lemma: der
  part_of_speech: article
  status: approved
  meanings:
  - id: article.definite
    definition: bestimmter Artikel für ein bereits bestimmtes oder eindeutig identifiziertes Substantiv
  review_status: provisional_v0.0.2
  surface_forms:
  - der
  - die
  - das
  - den
  - dem
  - des
- entry_id: DE-ADV-derzeit
  lemma: derzeit
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.currently
    definition: kennzeichnet den zum Dokumentzeitpunkt geltenden Zustand
  review_status: provisional_v0.0.2
  restrictions:
  - Bei versionskritischen Informationen zusätzlich Version oder Datum nennen.
- entry_id: DE-ADV-deshalb
  lemma: deshalb
  part_of_speech: adverb
  status: approved
  meanings:
  - id: result.therefore
    definition: kennzeichnet einen direkten Folgezusammenhang zur vorherigen Aussage
  review_status: corpus_candidate_v0.0.3
- entry_id: DE-VER-dienen
  lemma: dienen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: serve.function
    definition: die ausdrücklich festgelegte technische Funktion oder den Zweck eines Objekts angeben
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - diene
  - dienst
  - dient
  - dienen
  - diente
  - gedient
  restrictions:
  - Funktion oder Zweck konkret nennen; nicht für allgemeine Nutzenbehauptungen verwenden.
- entry_id: DE-PRO-dies
  lemma: dies
  part_of_speech: pronoun
  status: restricted
  meanings:
  - id: pronoun.this
    definition: verweist auf einen eindeutig bestimmten vorherigen Sachverhalt
  review_status: provisional_v0.0.2
  surface_forms:
  - dies
  restrictions:
  - Wenn der Bezug nicht eindeutig ein Satz oder Sachverhalt ist, das Substantiv wiederholen.
- entry_id: DE-DET-dieser
  lemma: dieser
  part_of_speech: determiner
  status: restricted
  meanings:
  - id: determiner.this
    definition: verweist auf ein eindeutig bestimmtes, bereits genanntes Substantiv
  review_status: provisional_v0.0.2
  surface_forms:
  - dieser
  - diese
  - dieses
  - diesen
  - diesem
  restrictions:
  - Nur verwenden, wenn genau ein möglicher Bezug besteht. Das Substantiv nach dem Determinierer nennen.
- entry_id: DE-ADJ-direkt
  lemma: direkt
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.direct
    definition: ohne Zwischenstufe, Umlenkung oder vermittelndes Element
  review_status: provisional_v0.0.2
- entry_id: DE-ADV-direkt
  lemma: direkt
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.directly
    definition: kennzeichnet eine unmittelbare Verbindung, Lage oder Folge ohne Zwischenstufe
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht als bloße Verstärkung verwenden.
- entry_id: DE-VER-dividieren
  lemma: dividieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: divide.math
    definition: einen numerischen Wert mathematisch durch einen anderen teilen
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-dokument
  lemma: Dokument
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.document
    definition: abgegrenzte Informationsquelle mit eigener Identifikation oder Funktion
  review_status: provisional_v0.0.2
  gender: neut
  plural: Dokumente
- entry_id: DE-NOU-dokumentation
  lemma: Dokumentation
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.dokumentation
    definition: geordnete Menge technischer Dokumente oder aufgezeichneter technischer Informationen
  review_status: multi_industry_candidate_v0.1
  plural: Dokumentationen
  restrictions:
  - Für ein einzelnes Dokument den konkreten Dokumenttyp verwenden.
- entry_id: DE-VER-dokumentieren
  lemma: dokumentieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: document
    definition: eine technische Tatsache, Entscheidung oder ein Ergebnis in einem vorgesehenen Dokumentationssystem
      festhalten
  review_status: provisional_v0.0.2
- entry_id: DE-ADV-dort
  lemma: dort
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.there
    definition: verweist auf einen zuvor eindeutig identifizierten Ort
  review_status: provisional_v0.0.2
  restrictions:
  - Ort wiederholen, wenn mehr als ein möglicher Bezug besteht.
- entry_id: DE-VER-drehen
  lemma: drehen
  part_of_speech: verb
  status: approved
  meanings:
  - id: turn.rotate
    definition: ein Objekt um eine Achse oder einen Punkt bewegen
  review_status: provisional_v0.0.2
- entry_id: DE-QUA-drei
  lemma: drei
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.three
    definition: bezeichnet die Zahl 3 in ausgeschriebener Form
  review_status: corpus_candidate_v0.0.3
- entry_id: DE-VER-dr-cken
  lemma: drücken
  part_of_speech: verb
  status: approved
  meanings:
  - id: push.press
    definition: eine Kraft auf eine Fläche oder in Richtung weg vom Kraftausübenden ausüben
  review_status: provisional_v0.0.2
- entry_id: DE-PRE-durch
  lemma: durch
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.through
    definition: kennzeichnet einen Weg durch einen Raum, eine Öffnung oder ein Material
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht als unklaren Ersatz für eine Ursache oder ein Werkzeug verwenden.
- entry_id: DE-VER-d-rfen
  lemma: dürfen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: may.permission
    definition: Erlaubnis ausdrücken
  - id: may.prohibition
    definition: mit nicht ein Verbot ausdrücken
  review_status: provisional_v0.0.2
  surface_forms:
  - darf
  - darfst
  - dürfen
  - dürft
  - durfte
  - durften
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-ART-ein
  lemma: ein
  part_of_speech: article
  status: approved
  meanings:
  - id: article.indefinite
    definition: unbestimmter Artikel für ein neu eingeführtes einzelnes zählbares Substantiv
  review_status: provisional_v0.0.2
  surface_forms:
  - ein
  - eine
  - einen
  - einem
  - einer
  - eines
- entry_id: DE-VER-einbauen
  lemma: einbauen
  part_of_speech: verb
  status: approved
  meanings:
  - id: install.mechanical
    definition: ein mechanisches oder elektrisches Bauteil in seine vorgesehene Einbauposition bringen
  review_status: provisional_v0.0.2
  separable: true
  prefix: ein
  surface_forms:
  - eingebaut
- entry_id: DE-VER-einf-gen
  lemma: einfügen
  part_of_speech: verb
  status: approved
  meanings:
  - id: paste.insert
    definition: digitale Daten oder ein Element an einer bestimmten Position ergänzen
  review_status: provisional_v0.0.2
  separable: true
  prefix: ein
- entry_id: DE-ADJ-eingebaut
  lemma: eingebaut
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.installed
    definition: in der vorgesehenen Einbauposition vorhanden
  review_status: provisional_v0.0.2
- entry_id: DE-VER-eingeben
  lemma: eingeben
  part_of_speech: verb
  status: approved
  meanings:
  - id: enter.data
    definition: Daten in ein System übertragen oder erfassen
  review_status: provisional_v0.0.2
  separable: true
  prefix: ein
- entry_id: DE-ADJ-eingeschaltet
  lemma: eingeschaltet
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.on
    definition: im aktiven Energie- oder Betriebszustand
  review_status: provisional_v0.0.2
- entry_id: DE-VER-einhalten
  lemma: einhalten
  part_of_speech: verb
  status: restricted
  meanings:
  - id: comply.limit
    definition: einen ausdrücklich genannten Grenzwert, Abstand, Zeitraum oder eine Anforderung nicht überschreiten
      oder unterschreiten
  review_status: corpus_candidate_v0.0.3
  separable: true
  prefix: ein
  surface_forms:
  - eingehalten
  restrictions:
  - Grenzwert oder referenzierte Anforderung muss eindeutig identifiziert sein.
- entry_id: DE-NOU-einheit
  lemma: Einheit
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.unit
    definition: definierte funktionale oder physische Einheit oder Maßeinheit
  review_status: provisional_v0.0.2
  gender: fem
  plural: Einheiten
  restrictions:
  - Bedeutung muss aus Kontext eindeutig sein.
- entry_id: DE-QUA-einige
  lemma: einige
  part_of_speech: quantifier
  status: restricted
  meanings:
  - id: quantifier.some
    definition: bezeichnet eine nicht genau bestimmte Teilmenge
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht in Anweisungen verwenden, wenn die genaue Menge bekannt oder sicherheitsrelevant ist.
- entry_id: DE-VER-einrasten
  lemma: einrasten
  part_of_speech: verb
  status: restricted
  meanings:
  - id: latch
    definition: in eine definierte Rast- oder Verriegelungsposition gelangen oder gebracht werden
  review_status: provisional_v0.0.2
  separable: true
  prefix: ein
- entry_id: DE-QUA-eins
  lemma: eins
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.one
    definition: bezeichnet die Zahl 1 in ausgeschriebener Form
  review_status: provisional_v0.0.2
- entry_id: DE-VER-einschalten
  lemma: einschalten
  part_of_speech: verb
  status: approved
  meanings:
  - id: switch.on
    definition: ein Gerät, System oder eine Funktion in den aktiven Energie- oder Betriebszustand bringen
  review_status: provisional_v0.0.2
  separable: true
  prefix: ein
  prohibited_synonyms:
  - anmachen
- entry_id: DE-VER-einstellen
  lemma: einstellen
  part_of_speech: verb
  status: approved
  meanings:
  - id: set.adjust
    definition: einen Parameter oder ein Bedienelement auf einen festgelegten Wert oder Zustand bringen
  review_status: provisional_v0.0.2
  separable: true
  prefix: ein
  surface_forms:
  - eingestellt
- entry_id: DE-NOU-einstellung
  lemma: Einstellung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.einstellung
    definition: festgelegter oder auswählbarer Wert oder Zustand eines Systems oder Parameters
  review_status: multi_industry_candidate_v0.1
  plural: Einstellungen
  restrictions:
  - Nicht für die allgemeine Haltung oder Meinung einer Person verwenden.
- entry_id: DE-VER-empfangen
  lemma: empfangen
  part_of_speech: verb
  status: approved
  meanings:
  - id: receive
    definition: übertragene Daten, ein Signal oder eine Nachricht aufnehmen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-empfehlen
  lemma: empfehlen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: recommend
    definition: eine nicht verbindliche bevorzugte Handlung ausdrücklich als Empfehlung kennzeichnen
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht verwenden, wenn eine Pflicht oder Sicherheitsanforderung gemeint ist.
- entry_id: DE-NOU-ende
  lemma: Ende
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.end
    definition: letzter Punkt oder Abschluss eines ausdrücklich bestimmten Ablaufs oder Bereichs
  review_status: provisional_v0.0.2
  gender: neut
  plural: Enden
- entry_id: DE-ADJ-eng
  lemma: eng
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.narrow
    definition: hat eine geringe lichte Weite oder einen kleinen Abstand relativ zur ausdrücklich genannten Referenz
  review_status: provisional_v0.0.2
- entry_id: DE-VER-entfalten
  lemma: entfalten
  part_of_speech: verb
  status: approved
  meanings:
  - id: unfold
    definition: ein gefaltetes Teil in seine vorgesehene offene Form bringen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-entfernen
  lemma: entfernen
  part_of_speech: verb
  status: approved
  meanings:
  - id: remove
    definition: ein Objekt von einer Position, Oberfläche oder Verbindung wegnehmen
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-entfernt
  lemma: entfernt
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.removed
    definition: nicht mehr an der zuvor bezeichneten Position vorhanden
  review_status: provisional_v0.0.2
- entry_id: DE-VER-enthalten
  lemma: enthalten
  part_of_speech: verb
  status: approved
  meanings:
  - id: contain
    definition: ausdrücken, dass ein Objekt, Dokument oder Datensatz ausdrücklich genannte Bestandteile oder Informationen
      umfasst
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - enthalte
  - enthältst
  - enthält
  - enthalten
  - enthielt
- entry_id: DE-VER-entladen
  lemma: entladen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: discharge.electrical
    definition: elektrische Ladung oder gespeicherte elektrische Energie kontrolliert verringern oder entfernen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-entleeren
  lemma: entleeren
  part_of_speech: verb
  status: approved
  meanings:
  - id: empty
    definition: Material, Flüssigkeit oder Gas vollständig aus einem Behälter oder Raum entfernen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-entl-ften
  lemma: entlüften
  part_of_speech: verb
  status: approved
  meanings:
  - id: bleed.vent
    definition: Luft oder Gas kontrolliert aus einem System oder einer Leitung entfernen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-entriegeln
  lemma: entriegeln
  part_of_speech: verb
  status: approved
  meanings:
  - id: unlock
    definition: eine mechanische oder logische Verriegelung aus dem gesicherten Zustand freigeben
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-entriegelt
  lemma: entriegelt
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.unlocked
    definition: nicht verriegelt und für die vorgesehene Bewegung freigegeben
  review_status: provisional_v0.0.2
- entry_id: DE-VER-entsprechen
  lemma: entsprechen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: conform.reference
    definition: mit einer ausdrücklich genannten Anforderung, Spezifikation oder Referenz übereinstimmen
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - entspreche
  - entsprichst
  - entspricht
  - entsprechen
  - entsprach
  - entsprochen
  restrictions:
  - Referenz oder Anforderung ausdrücklich nennen.
- entry_id: DE-PHR-entweder-oder
  lemma: entweder ... oder
  part_of_speech: phrase
  status: approved
  meanings:
  - id: alternative.exclusive_or_open
    definition: kennzeichnet zwei ausdrücklich genannte Alternativen
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - entweder ... oder
  restrictions:
  - Wenn beide Alternativen gleichzeitig möglich sind, diese Möglichkeit ausdrücklich nennen.
- entry_id: DE-VER-erden
  lemma: erden
  part_of_speech: verb
  status: restricted
  meanings:
  - id: ground
    definition: eine elektrische Verbindung zur festgelegten Erde oder Masse herstellen
  review_status: provisional_v0.0.2
  restrictions:
  - Nur im elektrischen Sinn verwenden.
- entry_id: DE-ADJ-erforderlich
  lemma: erforderlich
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.necessary
    definition: für die Erfüllung einer ausdrücklich genannten Anforderung notwendig
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht als versteckte Anweisung verwenden; in Verfahren direkte Anweisung geben.
- entry_id: DE-NOU-ergebnis
  lemma: Ergebnis
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.result
    definition: festgestellter Wert oder Zustand, der aus einer Handlung, Prüfung oder Berechnung folgt
  review_status: provisional_v0.0.2
  gender: neut
  plural: Ergebnisse
- entry_id: DE-VER-erh-hen
  lemma: erhöhen
  part_of_speech: verb
  status: approved
  meanings:
  - id: increase.transitive
    definition: einen numerischen Wert größer machen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-erkennen
  lemma: erkennen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: detect
    definition: durch Sensorik, Messung oder eindeutige Merkmale das Vorhandensein eines Zustands feststellen
  review_status: provisional_v0.0.2
  restrictions:
  - Bei formaler Sensor- oder Erkennungsfunktion als technisches Verb im Projektterminologiebestand führen.
- entry_id: DE-ADV-erneut
  lemma: erneut
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.again
    definition: kennzeichnet die Wiederholung derselben Handlung oder Prüfung
  review_status: provisional_v0.0.2
- entry_id: DE-VER-erreichen
  lemma: erreichen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: reach.threshold_position
    definition: einen ausdrücklich genannten Wert, Grenzwert, Zustand oder eine Position erreichen
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - erreiche
  - erreichst
  - erreicht
  - erreichen
  - erreichte
  restrictions:
  - Zielwert, Zustand oder Position nennen.
- entry_id: DE-VER-ersetzen
  lemma: ersetzen
  part_of_speech: verb
  status: approved
  meanings:
  - id: replace
    definition: ein vorhandenes Objekt durch ein anderes Objekt mit derselben vorgesehenen Funktion austauschen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-erweitern
  lemma: erweitern
  part_of_speech: verb
  status: restricted
  meanings:
  - id: expand
    definition: Größe, Umfang oder Funktionsumfang in eine ausdrücklich genannte Richtung vergrößern
  review_status: provisional_v0.0.2
  restrictions:
  - Art und Ziel der Erweiterung nennen.
- entry_id: DE-VER-erzeugen
  lemma: erzeugen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: generate.output
    definition: ein ausdrücklich genanntes physisches, elektrisches oder informationstechnisches Ergebnis hervorbringen
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - erzeuge
  - erzeugst
  - erzeugt
  - erzeugen
  - erzeugte
  restrictions:
  - Ergebnis oder Ausgangsgröße nennen.
- entry_id: DE-PRO-es
  lemma: es
  part_of_speech: pronoun
  status: restricted
  meanings:
  - id: pronoun.it
    definition: ersetzt ein eindeutig identifiziertes neutrales Substantiv oder dient in unpersönlichen Konstruktionen
  review_status: provisional_v0.0.2
  surface_forms:
  - es
  restrictions:
  - Nicht verwenden, wenn mehr als ein plausibler Bezug besteht.
- entry_id: DE-PHR-es-gibt
  lemma: es gibt
  part_of_speech: phrase
  status: restricted
  meanings:
  - id: exist.there_is
    definition: drückt aus, dass ein ausdrücklich genanntes Objekt oder ein Zustand vorhanden ist
  review_status: provisional_v0.0.2
  restrictions:
  - Nur verwenden, wenn der Existenzbezug klarer ist als vorhanden sein.
- entry_id: DE-ADJ-extern
  lemma: extern
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.external
    definition: außerhalb des ausdrücklich genannten Systems, Geräts oder organisatorischen Bereichs
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-fachpersonal
  lemma: Fachpersonal
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.fachpersonal
    definition: Personen mit der für eine ausdrücklich genannte technische Tätigkeit erforderlichen Qualifikation
  review_status: multi_industry_candidate_v0.1
  plural: Fachpersonal
  restrictions:
  - Erforderliche Qualifikation oder Rollenbezeichnung angeben, wenn sie sicherheitsrelevant ist.
- entry_id: DE-ADJ-falsch
  lemma: falsch
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.incorrect
    definition: entspricht einer eindeutig festgelegten Tatsache, Auswahl oder Anforderung nicht
  review_status: provisional_v0.0.2
- entry_id: DE-VER-falten
  lemma: falten
  part_of_speech: verb
  status: approved
  meanings:
  - id: fold
    definition: Material oder ein flexibles Teil entlang einer Linie umlegen
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-fehlend
  lemma: fehlend
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.missing
    definition: an der erwarteten Stelle nicht vorhanden
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-fehler
  lemma: Fehler
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.error_fault
    definition: Abweichung von einer definierten Funktion, Anforderung oder korrekten Information
  review_status: provisional_v0.0.2
  gender: masc
  plural: Fehler
  restrictions:
  - Fehlertyp nennen, wenn mehrere Bedeutungen möglich sind.
- entry_id: DE-ADJ-fehlerhaft
  lemma: fehlerhaft
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.faulty
    definition: erfüllt eine definierte funktionale oder Datenanforderung nicht
  review_status: provisional_v0.0.2
  restrictions:
  - Konkrete Abweichung nennen, wenn möglich.
- entry_id: DE-ADJ-fern
  lemma: fern
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.far
    definition: hat einen großen Abstand zur ausdrücklich genannten Referenz
  review_status: provisional_v0.0.2
  restrictions:
  - Wenn der Abstand relevant ist, Grenzwert nennen.
- entry_id: DE-ADJ-fest
  lemma: fest
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.tight
    definition: mechanisch so gehalten oder angezogen, dass die definierte Bewegung oder Lockerung nicht auftritt
  review_status: provisional_v0.0.2
  restrictions:
  - Bei Schraubverbindungen bevorzugt Drehmoment oder Prüfkriterium angeben.
- entry_id: DE-VER-festlegen
  lemma: festlegen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: specify.set
    definition: einen Wert, Zustand, Ablauf oder eine Anforderung ausdrücklich und verbindlich bestimmen
  review_status: corpus_candidate_v0.0.3
  separable: true
  prefix: fest
  surface_forms:
  - festgelegt
  restrictions:
  - Festgelegtes Element und Wert/Regel nennen.
- entry_id: DE-VER-festziehen
  lemma: festziehen
  part_of_speech: verb
  status: approved
  meanings:
  - id: tighten
    definition: eine Schraub- oder Klemmverbindung bis zum festgelegten Zustand oder Drehmoment anziehen
  review_status: provisional_v0.0.2
  separable: true
  prefix: fest
- entry_id: DE-VER-finden
  lemma: finden
  part_of_speech: verb
  status: approved
  meanings:
  - id: find
    definition: das Vorhandensein eines gesuchten oder unerwarteten Elements oder Zustands feststellen
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-folge
  lemma: Folge
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.consequence
    definition: Wirkung oder Ergebnis, das aus einer ausdrücklich genannten Ursache entsteht
  review_status: provisional_v0.0.2
  gender: fem
  plural: Folgen
- entry_id: DE-ADJ-folgend
  lemma: folgend
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.folgend
    definition: im Dokument oder in einer festgelegten Reihenfolge unmittelbar danach kommend
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - folgende
  - folgenden
  - folgender
  - folgendes
  - folgendem
  restrictions:
  - Nur verwenden, wenn die Reihenfolge eindeutig ist.
- entry_id: DE-NOU-form
  lemma: Form
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.form
    definition: geometrische Gestalt oder festgelegte sprachliche/strukturelle Ausprägung
  review_status: provisional_v0.0.2
  gender: fem
  plural: Formen
- entry_id: DE-VER-formatieren
  lemma: formatieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: format
    definition: ein digitales Speichermedium oder Datenobjekt nach einer festgelegten Struktur vorbereiten
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht im Sinn von Textgestaltung verwenden, sofern dies nicht ausdrücklich gemeint ist.
- entry_id: DE-VER-fortsetzen
  lemma: fortsetzen
  part_of_speech: verb
  status: approved
  meanings:
  - id: continue
    definition: einen unterbrochenen Vorgang ab seinem Unterbrechungspunkt weiterführen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-freigeben
  lemma: freigeben
  part_of_speech: verb
  status: restricted
  meanings:
  - id: release.approve
    definition: ein zuvor gesperrtes Objekt, Signal, Verfahren oder einen Zustand ausdrücklich zur Verwendung zulassen
  review_status: provisional_v0.0.2
  separable: true
  prefix: frei
  restrictions:
  - Nicht mit mechanischem loslassen verwechseln. Freigabeart muss aus dem Kontext eindeutig sein.
- entry_id: DE-NOU-funktion
  lemma: Funktion
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.function
    definition: vorgesehene technische Aufgabe oder Wirkung eines Systems, Bauteils oder Prozesses
  review_status: provisional_v0.0.2
  gender: fem
  plural: Funktionen
- entry_id: DE-VER-funktionieren
  lemma: funktionieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: operate.correctly
    definition: die vorgesehene Funktion ohne den beschriebenen Fehler erfüllen
  review_status: provisional_v0.0.2
  restrictions:
  - Wenn ein konkretes Leistungskriterium existiert, dieses Kriterium angeben.
- entry_id: DE-VER-f-llen
  lemma: füllen
  part_of_speech: verb
  status: approved
  meanings:
  - id: fill
    definition: Material, Flüssigkeit oder Gas in einen Behälter oder Raum einbringen
  review_status: provisional_v0.0.2
- entry_id: DE-QUA-fuenf
  lemma: fünf
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.five
    definition: bezeichnet die Zahl 5 in ausgeschriebener Form
  review_status: corpus_candidate_v0.0.3
- entry_id: DE-PRE-f-r
  lemma: für
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.for
    definition: kennzeichnet Zweck, Zielgruppe oder Zuordnung
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-gebraucht
  lemma: gebraucht
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.used
    definition: bereits verwendet und nicht als neu klassifiziert
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-gefahr
  lemma: Gefahr
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.hazard
    definition: Quelle oder Situation mit möglichem Schaden für Personen, Objekte oder Umwelt
  review_status: provisional_v0.0.2
  gender: fem
  plural: Gefahren
  restrictions:
  - Risikoklassifikation richtet sich nach anwendbarem Sicherheitsstandard.
- entry_id: DE-PRE-gegen
  lemma: gegen
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.against
    definition: kennzeichnet physischen Kontakt, entgegengesetzte Richtung oder eine definierte Gegenkraft
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-ger-t
  lemma: Gerät
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.device
    definition: technische Einheit, die eine oder mehrere vorgesehene Funktionen ausführt
  review_status: provisional_v0.0.2
  gender: neut
  plural: Geräte
  restrictions:
  - Offizielle Produktbenennung hat Vorrang.
- entry_id: DE-ADJ-geschlossen
  lemma: geschlossen
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.closed
    definition: in einem definierten geschlossenen Zustand
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-getrennt
  lemma: getrennt
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.disconnected
    definition: nicht mit dem ausdrücklich genannten Objekt verbunden
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-gleich
  lemma: gleich
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.equal
    definition: hat denselben ausdrücklich verglichenen Wert, Zustand oder dieselbe Identität
  review_status: provisional_v0.0.2
  restrictions:
  - Vergleichsmerkmal muss eindeutig sein.
- entry_id: DE-ADV-gleichzeitig
  lemma: gleichzeitig
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.simultaneously
    definition: kennzeichnet Handlungen oder Zustände, die im selben Zeitraum stattfinden
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-grenze
  lemma: Grenze
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.limit
    definition: Wert oder Position, die einen zulässigen oder definierten Bereich begrenzt
  review_status: provisional_v0.0.2
  gender: fem
  plural: Grenzen
- entry_id: DE-ADJ-gro
  lemma: groß
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.large
    definition: hat eine größere physische Abmessung als die ausdrücklich genannte Referenz
  review_status: provisional_v0.0.2
  restrictions:
  - Wenn möglich konkrete Abmessung nennen.
- entry_id: DE-NOU-grund
  lemma: Grund
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.reason
    definition: ausdrücklich genannte Ursache oder Begründung für eine Aussage oder Handlung
  review_status: provisional_v0.0.2
  gender: masc
  plural: Gründe
  restrictions:
  - Für technische Kausalität bevorzugt Ursache verwenden.
- entry_id: DE-VER-haben
  lemma: haben
  part_of_speech: verb
  status: approved
  meanings:
  - id: have.possess
    definition: etwas besitzen, enthalten oder als Teil aufweisen
  review_status: provisional_v0.0.2
  surface_forms:
  - habe
  - hast
  - hat
  - haben
  - habt
  - hatte
  - hatten
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-VER-halten
  lemma: halten
  part_of_speech: verb
  status: approved
  meanings:
  - id: hold
    definition: ein Objekt oder einen Zustand an einer Position oder einem Wert beibehalten
  review_status: provisional_v0.0.2
- entry_id: DE-VER-heben
  lemma: heben
  part_of_speech: verb
  status: approved
  meanings:
  - id: lift
    definition: ein Objekt in eine höhere Position bewegen
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-hersteller
  lemma: Hersteller
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.manufacturer
    definition: Organisation, die ein Produkt herstellt und als Hersteller verantwortlich zeichnet
  review_status: provisional_v0.0.2
  gender: masc
  plural: Hersteller
- entry_id: DE-VER-herunterladen
  lemma: herunterladen
  part_of_speech: verb
  status: approved
  meanings:
  - id: download
    definition: Daten von einem entfernten System auf das lokale System übertragen
  review_status: provisional_v0.0.2
  separable: true
  prefix: herunter
- entry_id: DE-ADV-hier
  lemma: hier
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.here
    definition: verweist auf den unmittelbar aktuellen Dokument- oder Ortskontext
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht verwenden, wenn der Referenzort nicht eindeutig ist.
- entry_id: DE-PRE-hinter
  lemma: hinter
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.behind
    definition: kennzeichnet eine Position auf der Rückseite oder weiter hinten als ein Referenzobjekt
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-hinweis
  lemma: Hinweis
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.note
    definition: zusätzliche Information, die keine Anweisung, Grenze oder Sicherheitsmaßnahme enthält
  review_status: provisional_v0.0.2
  gender: masc
  plural: Hinweise
- entry_id: DE-ADJ-hoch
  lemma: hoch
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.high
    definition: hat im definierten Bezugssystem eine große räumliche Position oder einen als hoch bezeichneten Zustand
  review_status: provisional_v0.0.2
  restrictions:
  - Für numerische Werte bevorzugt konkreten Wert oder mehr als verwenden.
- entry_id: DE-VER-hochladen
  lemma: hochladen
  part_of_speech: verb
  status: approved
  meanings:
  - id: upload
    definition: Daten vom lokalen System an ein entferntes System übertragen
  review_status: provisional_v0.0.2
  separable: true
  prefix: hoch
- entry_id: DE-ADV-h-chstens
  lemma: höchstens
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.maximum
    definition: kennzeichnet einen eingeschlossenen oberen Grenzwert
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-h-he
  lemma: Höhe
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.height
    definition: lineare Abmessung oder Position in vertikaler Richtung
  review_status: provisional_v0.0.2
  gender: fem
  plural: Höhen
- entry_id: DE-DET-Ihr
  lemma: Ihr
  part_of_speech: determiner
  status: restricted
  meanings:
  - id: determiner.de_det_ihr
    definition: bezeichnet den Besitz oder Bezug zur formal angesprochenen lesenden Person
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - Ihr
  - Ihre
  - Ihren
  - Ihrem
  - Ihrer
  - Ihres
  case_sensitive: true
  restrictions:
  - Bezugsobjekt nach dem Determinierer nennen.
- entry_id: DE-ADV-immer
  lemma: immer
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.always
    definition: kennzeichnet, dass eine Aussage ohne Ausnahme in allen Fällen des definierten Geltungsbereichs gilt
  review_status: provisional_v0.0.2
  restrictions:
  - Nur verwenden, wenn tatsächlich keine Ausnahme existiert.
- entry_id: DE-PRE-in
  lemma: in
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.in_into
    definition: kennzeichnet eine Position innerhalb eines Bereichs oder eine Bewegung in einen Bereich
  review_status: provisional_v0.0.2
- entry_id: DE-PHR-in-betrieb-sein
  lemma: in Betrieb sein
  part_of_speech: phrase
  status: restricted
  meanings:
  - id: state.in_operation
    definition: kennzeichnet, dass ein System in seinem vorgesehenen Betriebszustand ist
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-information
  lemma: Information
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.information
    definition: technischer Inhalt, der einen Sachverhalt, Zustand, Wert oder Zusammenhang beschreibt
  review_status: provisional_v0.0.2
  gender: fem
  plural: Informationen
- entry_id: DE-NOU-inhalt
  lemma: Inhalt
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.content
    definition: Information oder Material innerhalb eines ausdrücklich genannten Behälters, Dokuments oder Datenobjekts
  review_status: provisional_v0.0.2
  gender: masc
  plural: Inhalte
- entry_id: DE-ADV-innen
  lemma: innen
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.inside
    definition: kennzeichnet die Innenseite oder den Innenraum eines definierten Objekts
  review_status: provisional_v0.0.2
- entry_id: DE-PRE-innerhalb
  lemma: innerhalb
  part_of_speech: preposition
  status: approved
  meanings:
  - id: within.bound
    definition: kennzeichnet eine ausdrücklich genannte räumliche, zeitliche oder numerische Grenze
  review_status: corpus_candidate_v0.0.3
- entry_id: DE-NOU-installation
  lemma: Installation
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.installation
    definition: Vorgang oder Ergebnis des Einbauens, Anschließens oder Einrichtens eines technischen Systems
  review_status: multi_industry_candidate_v0.1
  plural: Installationen
  restrictions:
  - In Verfahren bevorzugt installieren, einbauen, anschließen oder einrichten entsprechend der konkreten Handlung
    verwenden.
- entry_id: DE-VER-installieren
  lemma: installieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: install.software
    definition: Software oder ein digitales Paket in einem System einrichten
  - id: install.system
    definition: ein System nach offizieller Terminologie in Betrieb setzen
  review_status: provisional_v0.0.2
  restrictions:
  - Für mechanische Bauteile bevorzugt einbauen verwenden.
  surface_forms:
  - installiert
- entry_id: DE-ADJ-intern
  lemma: intern
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.internal
    definition: innerhalb des ausdrücklich genannten Systems, Geräts oder organisatorischen Bereichs
  review_status: provisional_v0.0.2
- entry_id: DE-VER-isolieren
  lemma: isolieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: isolate
    definition: ein Objekt elektrisch, thermisch, stofflich oder logisch von seiner Umgebung trennen
  review_status: provisional_v0.0.2
  restrictions:
  - Art der Isolation nennen, wenn nicht eindeutig.
- entry_id: DE-QUA-je
  lemma: je
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: per.each
    definition: kennzeichnet eine Menge oder einen Wert pro ausdrücklich genannter Einheit
  review_status: corpus_candidate_v0.0.3
  approved_examples:
  - Der maximale Strom beträgt 500 mA je Kanal.
- entry_id: DE-DET-jeder
  lemma: jeder
  part_of_speech: determiner
  status: approved
  meanings:
  - id: determiner.each
    definition: bezeichnet jedes einzelne Element einer klar bestimmten Menge
  review_status: provisional_v0.0.2
  surface_forms:
  - jeder
  - jede
  - jedes
  - jeden
  - jedem
  approved_examples:
  - Prüfen Sie jede Verbindung.
- entry_id: DE-VER-kalibrieren
  lemma: kalibrieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: calibrate
    definition: ein Messsystem mit einer festgelegten Referenz vergleichen und nach dem freigegebenen Verfahren
      justieren
  review_status: provisional_v0.0.2
  restrictions:
  - Nur verwenden, wenn ein formales Kalibrierverfahren gemeint ist.
- entry_id: DE-DET-kein
  lemma: kein
  part_of_speech: determiner
  status: approved
  meanings:
  - id: determiner.none
    definition: verneint das Vorhandensein oder die Zugehörigkeit eines Substantivs
  review_status: provisional_v0.0.2
  surface_forms:
  - kein
  - keine
  - keinen
  - keinem
  - keiner
  - keines
  approved_examples:
  - Stellen Sie sicher, dass keine Leckage vorhanden ist.
- entry_id: DE-NOU-kenntnis
  lemma: Kenntnis
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.kenntnis
    definition: fachliches Wissen, das für eine ausdrücklich genannte Tätigkeit vorausgesetzt wird
  review_status: multi_industry_candidate_v0.1
  plural: Kenntnisse
  restrictions:
  - Bei sicherheitsrelevanten Voraussetzungen erforderliche Qualifikation konkret nennen.
- entry_id: DE-VER-kennzeichnen
  lemma: kennzeichnen
  part_of_speech: verb
  status: approved
  meanings:
  - id: label.mark
    definition: ein Objekt, einen Zustand oder einen Bereich mit einer eindeutigen Kennzeichnung versehen
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-kennzeichnung
  lemma: Kennzeichnung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.kennzeichnung
    definition: sichtbare oder maschinenlesbare Markierung zur Identifikation oder Klassifikation
  review_status: multi_industry_candidate_v0.1
  plural: Kennzeichnungen
- entry_id: DE-ADJ-klein
  lemma: klein
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.small
    definition: hat eine kleinere physische Abmessung als die ausdrücklich genannte Referenz
  review_status: provisional_v0.0.2
  restrictions:
  - Wenn möglich konkrete Abmessung nennen.
- entry_id: DE-VER-klicken
  lemma: klicken
  part_of_speech: verb
  status: restricted
  meanings:
  - id: click
    definition: eine Zeigeraktion mit einer Maustaste ausführen
  review_status: provisional_v0.0.2
  restrictions:
  - Nur für Benutzeroberflächen verwenden, bei denen ein Klick tatsächlich die Bedienhandlung ist.
- entry_id: DE-VER-komprimieren
  lemma: komprimieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: compress
    definition: Volumen oder digitale Daten nach einem definierten Verfahren verkleinern
  review_status: provisional_v0.0.2
  restrictions:
  - Physische und digitale Bedeutung müssen aus dem Objekt eindeutig sein.
- entry_id: DE-VER-konfigurieren
  lemma: konfigurieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: configure
    definition: freigegebene Parameter eines Systems auf eine definierte Konfiguration einstellen
  review_status: provisional_v0.0.2
  restrictions:
  - Konfiguration oder Referenz nennen, wenn sie nicht eindeutig vorgegeben ist.
- entry_id: DE-VER-kopieren
  lemma: kopieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: copy
    definition: eine identische digitale oder dokumentarische Kopie erstellen
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-korrekt
  lemma: korrekt
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.correct
    definition: entspricht der ausdrücklich geltenden Anforderung, Referenz oder Sollvorgabe
  review_status: provisional_v0.0.2
  restrictions:
  - Referenz muss aus Kontext oder Dokument eindeutig sein.
- entry_id: DE-VER-korrigieren
  lemma: korrigieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: correct
    definition: einen nachweislich falschen Wert, Text oder Zustand in den festgelegten korrekten Zustand bringen
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-kurz
  lemma: kurz
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.short
    definition: hat eine geringe Ausdehnung in Längsrichtung oder Dauer relativ zur ausdrücklich genannten Referenz
  review_status: provisional_v0.0.2
  restrictions:
  - Wenn möglich konkreten Wert nennen.
- entry_id: DE-VER-k-nnen
  lemma: können
  part_of_speech: verb
  status: restricted
  meanings:
  - id: can.capability
    definition: technische oder physische Fähigkeit ausdrücken
  - id: can.possibility
    definition: faktische Möglichkeit ausdrücken
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht als Ersatz für Erlaubnis verwenden; dafür dürfen verwenden.
  surface_forms:
  - kann
  - kannst
  - können
  - könnt
  - konnte
  - konnten
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-ADJ-lang
  lemma: lang
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.long
    definition: hat eine große Ausdehnung in Längsrichtung oder Dauer relativ zur ausdrücklich genannten Referenz
  review_status: provisional_v0.0.2
  restrictions:
  - Wenn möglich konkreten Wert nennen.
- entry_id: DE-ADV-langsam
  lemma: langsam
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.slowly
    definition: kennzeichnet eine geringe Geschwindigkeit
  review_status: provisional_v0.0.2
  restrictions:
  - Wenn die Geschwindigkeit sicherheits- oder qualitätskritisch ist, einen messbaren Grenzwert angeben.
- entry_id: DE-VER-lassen
  lemma: lassen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: allow.process
    definition: einen ausdrücklich genannten physikalischen Prozess ohne weitere aktive Handlung fortlaufen lassen
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - lasse
  - lässt
  - lassen
  - ließ
  - ließen
  - gelassen
  restrictions:
  - Nur verwenden, wenn der Leser einen natürlichen oder automatischen Prozess abwartet, zum Beispiel Abkühlen.
    Nicht verwenden, um den verantwortlichen Akteur zu verschleiern.
- entry_id: DE-ADJ-leer
  lemma: leer
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.empty
    definition: enthält keine relevante Menge des ausdrücklich genannten Inhalts
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-lesbar
  lemma: lesbar
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.readable
    definition: mit dem vorgesehenen Medium ohne zusätzliche Rekonstruktion erkennbar und interpretierbar
  review_status: provisional_v0.0.2
- entry_id: DE-VER-lesen
  lemma: lesen
  part_of_speech: verb
  status: approved
  meanings:
  - id: verb.lesen
    definition: geschriebenen oder angezeigten Text aufnehmen und inhaltlich erfassen
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - lese
  - liest
  - lesen
  - las
  - lasen
  - gelesen
  approved_examples:
  - Lesen Sie die Betriebsanleitung.
- entry_id: DE-NOU-leser
  lemma: Leser
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.reader
    definition: Person, für die der technische Text bestimmt ist
  review_status: provisional_v0.0.2
  gender: masc
  plural: Leser
  restrictions:
  - In inklusiven Unternehmensrichtlinien kann eine andere neutrale Rollenbezeichnung vorgeschrieben sein.
- entry_id: DE-VER-liegen
  lemma: liegen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: lie.position
    definition: sich an einer ausdrücklich bestimmten räumlichen Position befinden
  - id: value.in_range
    definition: einen Messwert oder Parameter innerhalb eines ausdrücklich genannten Bereichs haben
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - liege
  - liegst
  - liegt
  - liegen
  - lag
  - lagen
  - gelegen
  restrictions:
  - Nicht in abstrakten Wendungen wie „die Ursache liegt in“ verwenden; Ursache direkt nennen.
- entry_id: DE-ADV-links
  lemma: links
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.left
    definition: kennzeichnet die linke Seite relativ zum festgelegten Bezugssystem
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-lokal
  lemma: lokal
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.local
    definition: am ausdrücklich genannten Gerät, Ort oder System selbst statt über eine entfernte Verbindung
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-lose
  lemma: lose
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.loose
    definition: nicht ausreichend befestigt oder nicht in der vorgesehenen festen Verbindung
  review_status: provisional_v0.0.2
- entry_id: DE-VER-loslassen
  lemma: loslassen
  part_of_speech: verb
  status: approved
  meanings:
  - id: release.hand
    definition: ein zuvor gehaltenes Objekt freigeben
  review_status: provisional_v0.0.2
  separable: true
  prefix: los
- entry_id: DE-NOU-l-nge
  lemma: Länge
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.length
    definition: lineare Abmessung in der festgelegten Längsrichtung
  review_status: provisional_v0.0.2
  gender: fem
  plural: Längen
- entry_id: DE-VER-l-schen
  lemma: löschen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: delete.data
    definition: Daten oder einen digitalen Eintrag entfernen
  review_status: provisional_v0.0.2
  restrictions:
  - Für Feuer löschen nur verwenden, wenn der Kontext eindeutig Brandbekämpfung ist; sonst Feuer löschen als feste
    Wortgruppe verwenden.
- entry_id: DE-VER-l-sen
  lemma: lösen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: release.mechanical
    definition: eine mechanische Befestigung, Verriegelung oder Verbindung lockern oder freigeben
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht für das abstrakte Lösen eines Problems verwenden.
- entry_id: DE-VER-markieren
  lemma: markieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: mark.select
    definition: ein Element sichtbar oder logisch als ausgewählt oder gekennzeichnet festlegen
  review_status: provisional_v0.0.2
- entry_id: DE-PHR-mehr-als
  lemma: mehr als
  part_of_speech: phrase
  status: approved
  meanings:
  - id: phrase.more_than
    definition: kennzeichnet einen Wert oder eine Menge oberhalb einer nicht eingeschlossenen Grenze
  review_status: provisional_v0.0.2
- entry_id: DE-QUA-mehrere
  lemma: mehrere
  part_of_speech: quantifier
  status: restricted
  meanings:
  - id: quantifier.several
    definition: bezeichnet mehr als zwei Elemente ohne genaue Anzahl
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht verwenden, wenn die genaue Anzahl bekannt oder für die Aufgabe relevant ist.
- entry_id: DE-VER-melden
  lemma: melden
  part_of_speech: verb
  status: approved
  meanings:
  - id: report
    definition: einen Zustand, Fehler oder ein Ergebnis an eine vorgesehene Stelle übermitteln
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-menge
  lemma: Menge
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.quantity
    definition: bestimmte oder messbare Quantität eines Stoffes oder einer nicht diskreten Größe
  review_status: provisional_v0.0.2
  gender: fem
  plural: Mengen
- entry_id: DE-VER-messen
  lemma: messen
  part_of_speech: verb
  status: approved
  meanings:
  - id: measure
    definition: den quantitativen Wert einer physikalischen oder technischen Größe bestimmen
  review_status: provisional_v0.0.2
  surface_forms:
  - gemessen
- entry_id: DE-NOU-methode
  lemma: Methode
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.method
    definition: festgelegte Art, eine Aufgabe oder Analyse auszuführen
  review_status: provisional_v0.0.2
  gender: fem
  plural: Methoden
- entry_id: DE-ADV-mindestens
  lemma: mindestens
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.minimum
    definition: kennzeichnet einen eingeschlossenen unteren Grenzwert
  review_status: provisional_v0.0.2
- entry_id: DE-VER-mischen
  lemma: mischen
  part_of_speech: verb
  status: approved
  meanings:
  - id: mix
    definition: zwei oder mehr Stoffe zu einer Mischung zusammenbringen
  review_status: provisional_v0.0.2
- entry_id: DE-PRE-mit
  lemma: mit
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.with
    definition: kennzeichnet ein Werkzeug, Mittel, Material oder eine eindeutige gemeinsame Beteiligung
  review_status: provisional_v0.0.2
  restrictions:
  - Satz neu formulieren, wenn mit mehr als eine plausible Beziehung ausdrücken kann.
- entry_id: DE-NOU-mitte
  lemma: Mitte
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.middle
    definition: geometrischer oder funktionaler Zentralbereich zwischen festgelegten Grenzen
  review_status: provisional_v0.0.2
  gender: fem
  plural: Mitten
- entry_id: DE-VER-multiplizieren
  lemma: multiplizieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: multiply.math
    definition: numerische Werte mathematisch miteinander multiplizieren
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-m-glich
  lemma: möglich
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.possible
    definition: unter den genannten technischen Bedingungen realisierbar oder eintretbar
  review_status: provisional_v0.0.2
  restrictions:
  - Wenn die Wahrscheinlichkeit oder Bedingung relevant ist, diese explizit nennen.
- entry_id: DE-VER-m-ssen
  lemma: müssen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: must.requirement
    definition: eine verbindliche Anforderung oder zwingende Bedingung ausdrücken
  review_status: provisional_v0.0.2
  restrictions:
  - In direkten Arbeitsanweisungen nach Möglichkeit Imperativ verwenden.
  surface_forms:
  - muss
  - musst
  - müssen
  - müsst
  - musste
  - mussten
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-PRE-nach
  lemma: nach
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.after_toward
    definition: kennzeichnet eine zeitlich spätere Position oder eine eindeutig bezeichnete Richtung
  review_status: provisional_v0.0.2
  restrictions:
  - Zeit- und Richtungsbedeutung dürfen im selben Satz nicht konkurrieren.
- entry_id: DE-CON-nachdem
  lemma: nachdem
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.after
    definition: ordnet eine Handlung oder einen Zustand zeitlich nach einer abgeschlossenen Handlung an
  review_status: provisional_v0.0.2
- entry_id: DE-ADV-nacheinander
  lemma: nacheinander
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.sequentially
    definition: kennzeichnet Handlungen oder Elemente in einer ausdrücklich geordneten Folge
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-nah
  lemma: nah
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.near
    definition: hat einen kleinen Abstand zur ausdrücklich genannten Referenz
  review_status: provisional_v0.0.2
  restrictions:
  - Wenn der Abstand sicherheits- oder funktionsrelevant ist, Grenzwert nennen.
- entry_id: DE-NOU-name
  lemma: Name
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.name
    definition: offizielle oder eindeutig festgelegte sprachliche Identifikation eines Objekts, Dokuments oder Elements
  review_status: provisional_v0.0.2
  gender: masc
  plural: Namen
- entry_id: DE-ADJ-nass
  lemma: nass
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.wet
    definition: weist sichtbare oder relevante Flüssigkeit auf
  review_status: provisional_v0.0.2
- entry_id: DE-PRE-neben
  lemma: neben
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.next_to
    definition: kennzeichnet eine Position unmittelbar seitlich eines Referenzobjekts
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-neu
  lemma: neu
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.new
    definition: noch nicht verwendet oder ausdrücklich als neues Ersatzteil vorgesehen
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht als Synonym für neueste Version verwenden.
- entry_id: DE-QUA-neun
  lemma: neun
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.nine
    definition: bezeichnet die Zahl 9 in ausgeschriebener Form
  review_status: corpus_candidate_v0.0.3
- entry_id: DE-ADV-nicht
  lemma: nicht
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.not
    definition: verneint genau das unmittelbar zugeordnete Prädikat, Merkmal oder Element
  review_status: provisional_v0.0.2
  restrictions:
  - Negationsbereich muss eindeutig sein.
- entry_id: DE-ADV-nie
  lemma: nie
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.never
    definition: kennzeichnet, dass eine Handlung oder ein Zustand im definierten Geltungsbereich in keinem Fall
      zulässig oder möglich ist
  review_status: provisional_v0.0.2
  restrictions:
  - Für direkte Verbote in Verfahren bevorzugt nicht + Imperativ verwenden.
- entry_id: DE-ADJ-niedrig
  lemma: niedrig
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.low
    definition: hat im definierten Bezugssystem eine geringe räumliche Position oder einen als niedrig bezeichneten
      Zustand
  review_status: provisional_v0.0.2
  restrictions:
  - Für numerische Werte bevorzugt konkreten Wert oder weniger als verwenden.
- entry_id: DE-QUA-null
  lemma: 'null'
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.zero
    definition: bezeichnet die Zahl 0 in ausgeschriebener Form
  review_status: corpus_candidate_v0.0.3
- entry_id: DE-NOU-nummer
  lemma: Nummer
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.number
    definition: numerische oder alphanumerische Identifikation
  review_status: provisional_v0.0.2
  gender: fem
  plural: Nummern
- entry_id: DE-ADV-nur
  lemma: nur
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.only
    definition: beschränkt eine Aussage auf das ausdrücklich genannte Element oder die ausdrücklich genannte Bedingung
  review_status: provisional_v0.0.2
- entry_id: DE-CON-ob
  lemma: ob
  part_of_speech: conjunction
  status: restricted
  meanings:
  - id: whether.check
    definition: leitet eine Ja/Nein-Bedingung ein, deren Ergebnis ausdrücklich geprüft oder bestimmt wird
  review_status: corpus_candidate_v0.0.3
  restrictions:
  - Nur verwenden, wenn genau zwei klar unterscheidbare Zustände oder ein klares Ja/Nein-Kriterium vorliegen.
- entry_id: DE-ADV-oben
  lemma: oben
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.up
    definition: kennzeichnet eine höhere Position im festgelegten Bezugssystem
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-oberfl-che
  lemma: Oberfläche
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.surface
    definition: äußere oder definierte Grenzfläche eines Materials oder Objekts
  review_status: provisional_v0.0.2
  gender: fem
  plural: Oberflächen
- entry_id: DE-CON-oder
  lemma: oder
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.or
    definition: verbindet echte Alternativen
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht verwenden, wenn inklusive und exklusive Alternative unterschieden werden muss; dann die Auswahl explizit
    beschreiben.
- entry_id: DE-ADJ-offen
  lemma: offen
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.open
    definition: in einem definierten geöffneten Zustand
  review_status: provisional_v0.0.2
- entry_id: DE-PRE-ohne
  lemma: ohne
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.without
    definition: kennzeichnet das Fehlen eines ausdrücklich genannten Elements oder Zustands
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-option
  lemma: Option
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.option
    definition: ausdrücklich angebotene auswählbare Alternative
  review_status: provisional_v0.0.2
  gender: fem
  plural: Optionen
  restrictions:
  - Alternativen vollständig nennen, wenn sie für die Entscheidung relevant sind.
- entry_id: DE-NOU-person
  lemma: Person
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.person
    definition: ein einzelner Mensch ohne geschlechtsspezifische Benennung
  review_status: provisional_v0.0.2
  gender: fem
  plural: Personen
- entry_id: DE-NOU-position
  lemma: Position
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.position
    definition: definierte räumliche Lage oder definierter Zustand eines Bedienelements
  review_status: provisional_v0.0.2
  gender: fem
  plural: Positionen
  restrictions:
  - Räumliche und Schalterzustandsbedeutung müssen aus Kontext eindeutig sein.
- entry_id: DE-VER-positionieren
  lemma: positionieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: position
    definition: ein Objekt in eine ausdrücklich definierte Position bringen
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-prim-r
  lemma: primär
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.primary
    definition: als erste, wichtigste oder vorgesehene Hauptfunktion in der anwendbaren Terminologie definiert
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht als bloßes Synonym für wichtig verwenden.
- entry_id: DE-NOU-problem
  lemma: Problem
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.problem
    definition: Zustand, der die vorgesehene Funktion oder Ausführung einer Aufgabe verhindert oder beeinträchtigt
  review_status: provisional_v0.0.2
  gender: neut
  plural: Probleme
  restrictions:
  - Wenn möglich konkreten Fehler oder Zustand nennen.
- entry_id: DE-NOU-produkt
  lemma: Produkt
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.produkt
    definition: technische Einheit oder Ware, auf die sich die Dokumentation bezieht
  review_status: multi_industry_candidate_v0.1
  plural: Produkte
  restrictions:
  - Offizielle Produkt- oder Komponentenbezeichnung hat Vorrang.
- entry_id: DE-NOU-prozess
  lemma: Prozess
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.process
    definition: geordnete Folge von Zuständen oder Vorgängen mit definiertem Zweck
  review_status: provisional_v0.0.2
  gender: masc
  plural: Prozesse
- entry_id: DE-VER-pr-fen
  lemma: prüfen
  part_of_speech: verb
  status: approved
  meanings:
  - id: check
    definition: feststellen, ob ein definierter Zustand, ein Merkmal oder eine Anforderung erfüllt ist
  review_status: provisional_v0.0.2
  approved_examples:
  - Prüfen Sie den Druck.
  prohibited_synonyms:
  - überprüfen
  - kontrollieren
  - checken
  surface_forms:
  - geprüft
- entry_id: DE-NOU-pr-fung
  lemma: Prüfung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.check
    definition: festgelegte Handlung zur Feststellung, ob ein Zustand oder Kriterium erfüllt ist
  review_status: provisional_v0.0.2
  gender: fem
  plural: Prüfungen
- entry_id: DE-ADV-rechts
  lemma: rechts
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.right
    definition: kennzeichnet die rechte Seite relativ zum festgelegten Bezugssystem
  review_status: provisional_v0.0.2
- entry_id: DE-VER-reduzieren
  lemma: reduzieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: reduce
    definition: einen Umfang, eine Menge oder eine Größe kleiner machen
  review_status: provisional_v0.0.2
  restrictions:
  - Für reine numerische Werte bevorzugt verringern verwenden.
- entry_id: DE-VER-referenzieren
  lemma: referenzieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: reference
    definition: eine eindeutig bezeichnete Quelle oder ein Objekt als Referenz angeben
  review_status: provisional_v0.0.2
  restrictions:
  - In Lesertexten bevorzugt auf ... verweisen.
- entry_id: DE-VER-regeln
  lemma: regeln
  part_of_speech: verb
  status: restricted
  meanings:
  - id: regulate
    definition: eine Größe automatisch oder manuell auf einen Sollwert oder innerhalb eines Bereichs halten
  review_status: provisional_v0.0.2
  restrictions:
  - Nur im technischen Regelungs-Sinn verwenden.
- entry_id: DE-VER-reinigen
  lemma: reinigen
  part_of_speech: verb
  status: approved
  meanings:
  - id: clean
    definition: unerwünschtes Material von einem Objekt oder einer Oberfläche entfernen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-reparieren
  lemma: reparieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: repair
    definition: einen beschädigten oder fehlerhaften Gegenstand nach einem freigegebenen Verfahren wieder in den
      zulässigen Zustand bringen
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-richtung
  lemma: Richtung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.direction
    definition: orientierte räumliche oder logische Bewegungsrichtung
  review_status: provisional_v0.0.2
  gender: fem
  plural: Richtungen
- entry_id: DE-NOU-risiko
  lemma: Risiko
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.risk
    definition: Kombination aus Möglichkeit eines schädlichen Ereignisses und dessen Auswirkung nach anwendbarem
      Sicherheitsmodell
  review_status: provisional_v0.0.2
  gender: neut
  plural: Risiken
- entry_id: DE-ADJ-sauber
  lemma: sauber
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.clean
    definition: frei von dem im Verfahren nicht zulässigen Schmutz oder Fremdmaterial
  review_status: provisional_v0.0.2
  restrictions:
  - Bei kritischer Sauberkeit messbares oder referenziertes Kriterium verwenden.
- entry_id: DE-NOU-schaden
  lemma: Schaden
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.damage
    definition: physische, funktionale oder materielle Beeinträchtigung eines Objekts oder einer Person
  review_status: provisional_v0.0.2
  gender: masc
  plural: Schäden
- entry_id: DE-VER-schieben
  lemma: schieben
  part_of_speech: verb
  status: approved
  meanings:
  - id: push.slide
    definition: ein Objekt durch eine geradlinige Druckbewegung zu einer ausdrücklich genannten Position bewegen
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - schiebe
  - schiebst
  - schiebt
  - schieben
  - schob
  - schoben
  - geschoben
- entry_id: DE-VER-schlie-en
  lemma: schließen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: close
    definition: ein Teil, eine Öffnung, Datei oder Funktion aus dem offenen Zustand in den geschlossenen Zustand
      bringen
  review_status: provisional_v0.0.2
  restrictions:
  - Bei Software und Mechanik muss der Kontext eindeutig sein.
  surface_forms:
  - geschlossen
- entry_id: DE-VER-schmieren
  lemma: schmieren
  part_of_speech: verb
  status: restricted
  meanings:
  - id: lubricate
    definition: ein freigegebenes Schmiermittel auf eine Reib- oder Kontaktstelle aufbringen
  review_status: provisional_v0.0.2
  restrictions:
  - Schmiermittel nennen oder auf freigegebene Spezifikation verweisen.
- entry_id: DE-VER-schneiden
  lemma: schneiden
  part_of_speech: verb
  status: approved
  meanings:
  - id: cut.material
    definition: Material mit einem dafür vorgesehenen Schneidwerkzeug trennen
  review_status: provisional_v0.0.2
- entry_id: DE-ADV-schnell
  lemma: schnell
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.quickly
    definition: kennzeichnet eine hohe Geschwindigkeit
  review_status: provisional_v0.0.2
  restrictions:
  - Wenn die Geschwindigkeit sicherheits- oder qualitätskritisch ist, einen messbaren Grenzwert angeben.
- entry_id: DE-NOU-schritt
  lemma: Schritt
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.step
    definition: einzelne abgegrenzte Handlung oder Anweisung innerhalb eines Verfahrens
  review_status: provisional_v0.0.2
  gender: masc
  plural: Schritte
- entry_id: DE-VER-sch-tzen
  lemma: schützen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: protect
    definition: ein Objekt oder eine Person durch eine ausdrücklich genannte Maßnahme vor einer definierten Gefahr
      oder Einwirkung bewahren
  review_status: provisional_v0.0.2
  restrictions:
  - Gefahr oder Einwirkung nennen, wenn sie nicht eindeutig ist.
- entry_id: DE-VER-scrollen
  lemma: scrollen
  part_of_speech: verb
  status: approved
  meanings:
  - id: scroll.ui
    definition: den sichtbaren Ausschnitt einer digitalen Ansicht verschieben
  review_status: provisional_v0.0.2
- entry_id: DE-QUA-sechs
  lemma: sechs
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.six
    definition: bezeichnet die Zahl 6 in ausgeschriebener Form
  review_status: corpus_candidate_v0.0.3
- entry_id: DE-VER-sein
  lemma: sein
  part_of_speech: verb
  status: approved
  meanings:
  - id: be.state
    definition: einen Zustand, eine Eigenschaft, Identität oder Existenz ausdrücken
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht als Hilfsverb für eine unnötige Passivkonstruktion verwenden.
  surface_forms:
  - bin
  - bist
  - ist
  - sind
  - seid
  - war
  - waren
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-PRE-seit
  lemma: seit
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.since
    definition: kennzeichnet den Beginn eines Zeitraums, der bis zum Bezugszeitpunkt andauert
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-seite
  lemma: Seite
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.side_page
    definition: räumliche Seite eines Objekts oder Seite eines Dokuments
  review_status: provisional_v0.0.2
  gender: fem
  plural: Seiten
  restrictions:
  - Räumliche und dokumentarische Bedeutung müssen aus Kontext eindeutig sein.
- entry_id: DE-ADJ-sekund-r
  lemma: sekundär
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.secondary
    definition: als zweite oder unterstützende Funktion in der anwendbaren Terminologie definiert
  review_status: provisional_v0.0.2
- entry_id: DE-VER-senden
  lemma: senden
  part_of_speech: verb
  status: approved
  meanings:
  - id: send
    definition: Daten, ein Signal oder eine Nachricht zu einem Empfänger übertragen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-senken
  lemma: senken
  part_of_speech: verb
  status: approved
  meanings:
  - id: lower.position
    definition: ein Objekt in eine tiefere Position bewegen
  review_status: provisional_v0.0.2
- entry_id: DE-PRO-sich
  lemma: sich
  part_of_speech: pronoun
  status: restricted
  meanings:
  - id: pron.reflexive
    definition: reflexives Pronomen, das eindeutig auf das grammatische Subjekt derselben Klausel verweist
  review_status: corpus_candidate_v0.0.3
  restrictions:
  - Nur bei eindeutigem reflexivem Bezug verwenden. Bei möglichem Bezug auf mehrere Objekte den technischen Begriff
    wiederholen.
- entry_id: DE-ADJ-sicher
  lemma: sicher
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.sicher
    definition: ohne eine nach dem anwendbaren Risikokriterium unzulässige Gefahr
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - sichere
  - sicheren
  - sicherer
  - sicheres
  - sicherem
  restrictions:
  - Nicht als unquantifizierte Qualitätsbehauptung verwenden.
- entry_id: DE-VER-sicherstellen
  lemma: sicherstellen
  part_of_speech: verb
  status: approved
  meanings:
  - id: ensure
    definition: durch eine Prüfung oder eindeutige Feststellung bestätigen, dass eine genannte Bedingung erfüllt
      ist
  review_status: provisional_v0.0.2
  separable: true
  prefix: sicher
  approved_examples:
  - Stellen Sie sicher, dass das Ventil geschlossen ist.
  forms:
    imperative_formal: Stellen Sie sicher, dass ...
- entry_id: DE-ADJ-sichtbar
  lemma: sichtbar
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.visible
    definition: mit dem vorgesehenen visuellen Verfahren erkennbar
  review_status: provisional_v0.0.2
  restrictions:
  - Für Prüfhandlungen bevorzugt Stellen Sie sicher, dass Sie ... sehen können, wenn Beobachterbezug relevant ist.
- entry_id: DE-PRO-SIE-READER
  lemma: Sie
  part_of_speech: pronoun
  status: approved
  meanings:
  - id: pronoun.reader_formal
    definition: bezeichnet die lesende oder handelnde Person in formalen Anweisungen
  review_status: provisional_v0.0.2
  surface_forms:
  - Sie
  - Ihnen
  approved_examples:
  - Entfernen Sie die Abdeckung.
  case_sensitive: true
- entry_id: DE-PRO-sie
  lemma: sie
  part_of_speech: pronoun
  status: restricted
  meanings:
  - id: pronoun.she_they
    definition: ersetzt ein eindeutig identifiziertes feminines Singular- oder Pluralreferenzobjekt
  review_status: provisional_v0.0.2
  surface_forms:
  - sie
  - ihnen
  restrictions:
  - Nicht verwenden, wenn Numerus oder Bezug mehrdeutig ist.
  case_sensitive: true
- entry_id: DE-QUA-sieben
  lemma: sieben
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.seven
    definition: bezeichnet die Zahl 7 in ausgeschriebener Form
  review_status: corpus_candidate_v0.0.3
- entry_id: DE-NOU-signal
  lemma: Signal
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.signal
    definition: physikalische oder digitale Größe, die Information überträgt
  review_status: provisional_v0.0.2
  gender: neut
  plural: Signale
- entry_id: DE-VER-sinken
  lemma: sinken
  part_of_speech: verb
  status: approved
  meanings:
  - id: decrease.intransitive
    definition: von selbst oder durch einen Prozess einen niedrigeren numerischen Wert annehmen
  review_status: provisional_v0.0.2
- entry_id: DE-PHR-so-viel-wie
  lemma: so viel wie
  part_of_speech: phrase
  status: restricted
  meanings:
  - id: phrase.equal_amount
    definition: kennzeichnet Gleichheit einer Menge oder eines Werts
  review_status: provisional_v0.0.2
- entry_id: DE-CON-sobald
  lemma: sobald
  part_of_speech: conjunction
  status: restricted
  meanings:
  - id: conj.as_soon_as
    definition: kennzeichnet den ersten Zeitpunkt, an dem eine eindeutig definierte Bedingung erfüllt ist
  review_status: provisional_v0.0.2
  restrictions:
  - Nur verwenden, wenn die Reaktion tatsächlich unmittelbar beim Eintritt der Bedingung erfolgen soll.
- entry_id: DE-ADV-sofort
  lemma: sofort
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.immediately
    definition: kennzeichnet, dass keine absichtliche Verzögerung zulässig ist
  review_status: provisional_v0.0.2
- entry_id: DE-CON-sondern
  lemma: sondern
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.but_rather
    definition: ersetzt nach einer Verneinung ein ausgeschlossenes Element durch das korrekte Element
  review_status: provisional_v0.0.2
- entry_id: DE-VER-sortieren
  lemma: sortieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: sort
    definition: Elemente nach einem ausdrücklich genannten Kriterium in eine Reihenfolge bringen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-speichern
  lemma: speichern
  part_of_speech: verb
  status: approved
  meanings:
  - id: save.data
    definition: Daten dauerhaft oder für spätere Verwendung ablegen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-sp-len
  lemma: spülen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: flush
    definition: ein System oder eine Oberfläche mit einem Flüssigkeits- oder Gasstrom reinigen oder auswaschen
  review_status: provisional_v0.0.2
  restrictions:
  - Spülmedium und Ziel nennen, wenn nicht durch Verfahren festgelegt.
- entry_id: DE-ADJ-stabil
  lemma: stabil
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.stable
    definition: ändert den relevanten Zustand oder Wert innerhalb des definierten Beobachtungszeitraums nicht außerhalb
      der zulässigen Grenze
  review_status: provisional_v0.0.2
  restrictions:
  - Kriterium oder Zeitraum nennen, wenn für Entscheidung relevant.
- entry_id: DE-VER-starten
  lemma: starten
  part_of_speech: verb
  status: approved
  meanings:
  - id: start
    definition: einen Prozess, Test, Motor oder Ablauf beginnen lassen
  review_status: provisional_v0.0.2
  prohibited_synonyms:
  - beginnen
  - anfangen
  surface_forms:
  - gestartet
- entry_id: DE-VER-steigen
  lemma: steigen
  part_of_speech: verb
  status: approved
  meanings:
  - id: increase.intransitive
    definition: von selbst oder durch einen Prozess einen höheren numerischen Wert annehmen
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-stelle
  lemma: Stelle
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.location
    definition: genau bezeichneter räumlicher Punkt, Dokumentort oder organisatorischer Empfänger
  review_status: provisional_v0.0.2
  gender: fem
  plural: Stellen
  restrictions:
  - Art der Stelle nennen, wenn nicht eindeutig.
- entry_id: DE-VER-steuern
  lemma: steuern
  part_of_speech: verb
  status: approved
  meanings:
  - id: control
    definition: den Zustand oder Ablauf eines Systems durch Signale oder Befehle beeinflussen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-stoppen
  lemma: stoppen
  part_of_speech: verb
  status: approved
  meanings:
  - id: stop
    definition: einen laufenden Prozess oder eine Bewegung gezielt anhalten
  review_status: provisional_v0.0.2
- entry_id: DE-VER-subtrahieren
  lemma: subtrahieren
  part_of_speech: verb
  status: approved
  meanings:
  - id: subtract.math
    definition: einen numerischen Wert mathematisch von einem anderen abziehen
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-symbol
  lemma: Symbol
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.symbol
    definition: grafisches Zeichen mit festgelegter technischer oder sicherheitsbezogener Bedeutung
  review_status: multi_industry_candidate_v0.1
  plural: Symbole
- entry_id: DE-NOU-system
  lemma: System
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.system
    definition: funktional zusammengehörige Menge von Elementen mit einer definierten Aufgabe
  review_status: provisional_v0.0.2
  gender: neut
  plural: Systeme
- entry_id: DE-NOU-tabelle
  lemma: Tabelle
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.table
    definition: strukturierte Darstellung von Daten in Zeilen und Spalten
  review_status: provisional_v0.0.2
  gender: fem
  plural: Tabellen
- entry_id: DE-ADJ-technisch
  lemma: technisch
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.technisch
    definition: auf Technik, ein technisches Produkt oder einen technischen Prozess bezogen
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - technische
  - technischen
  - technischer
  - technisches
  - technischem
  restrictions:
  - Nur verwenden, wenn die Bezugsart für den Leser relevant ist.
- entry_id: DE-NOU-teil
  lemma: Teil
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.part
    definition: abgegrenztes Element eines größeren Ganzen
  review_status: provisional_v0.0.2
  gender: neut
  plural: Teile
  restrictions:
  - Offizielle technische Benennung bevorzugen.
- entry_id: DE-ADV-teilweise
  lemma: teilweise
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.partly
    definition: kennzeichnet, dass nur ein ausdrücklich bestimmter Teil betroffen ist
  review_status: provisional_v0.0.2
  restrictions:
  - Den betroffenen Teil nennen, wenn er für die Aufgabe relevant ist.
- entry_id: DE-VER-testen
  lemma: testen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: test
    definition: mit einem definierten Test feststellen, ob eine Funktion oder ein System festgelegte Kriterien erfüllt
  review_status: provisional_v0.0.2
  restrictions:
  - Nur verwenden, wenn ein definierter Test gemeint ist; sonst prüfen verwenden.
- entry_id: DE-NOU-text
  lemma: Text
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.text
    definition: geschriebene sprachliche Information
  review_status: provisional_v0.0.2
  gender: masc
  plural: Texte
- entry_id: DE-VER-tippen
  lemma: tippen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: tap.ui
    definition: eine Touch-Oberfläche kurz berühren, um eine Bedienhandlung auszuführen
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht im Sinn von Text mit Tastatur eingeben verwenden.
- entry_id: DE-VER-trennen
  lemma: trennen
  part_of_speech: verb
  status: approved
  meanings:
  - id: disconnect
    definition: eine bestehende mechanische, elektrische oder logische Verbindung aufheben
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-trocken
  lemma: trocken
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.dry
    definition: weist keine für die Aufgabe relevante freie Feuchtigkeit oder Flüssigkeit auf
  review_status: provisional_v0.0.2
- entry_id: DE-VER-trocknen
  lemma: trocknen
  part_of_speech: verb
  status: approved
  meanings:
  - id: dry
    definition: Feuchtigkeit oder Flüssigkeit von einem Objekt oder aus einem Bereich entfernen
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-typ
  lemma: Typ
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.type_class
    definition: definierte technische oder dokumentarische Klasse
  review_status: provisional_v0.0.2
  gender: masc
  plural: Typen
- entry_id: DE-NOU-taetigkeit
  lemma: Tätigkeit
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.taetigkeit
    definition: abgegrenzte menschliche technische Handlung oder Arbeitsaufgabe
  review_status: multi_industry_candidate_v0.1
  plural: Tätigkeiten
  restrictions:
  - In Verfahren die konkrete Handlung mit einem direkten Verb formulieren.
- entry_id: DE-PRE-um
  lemma: um
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.around
    definition: kennzeichnet eine Bewegung oder Position um eine ausdrücklich genannte Achse oder ein Objekt
  - id: prep.delta
    definition: kennzeichnet eine ausdrücklich genannte Änderung um einen numerischen Betrag
  - id: prep.time
    definition: kennzeichnet einen ausdrücklich genannten Zeitpunkt
  review_status: corpus_candidate_v0.0.3
  restrictions:
  - Die Konstruktion „um ... zu“ ist nicht durch diesen Eintrag freigegeben; Zweck besser als eigener Satz oder
    mit einer eindeutigen Zweckangabe ausdrücken.
- entry_id: DE-CON-und
  lemma: und
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.and
    definition: verbindet gleichrangige Elemente, Aussagen oder gleichzeitig geltende Bedingungen
  review_status: provisional_v0.0.2
- entry_id: DE-ADV-ungef-hr
  lemma: ungefähr
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: adv.approximately
    definition: kennzeichnet einen Näherungswert, für den keine exakte Grenze gemeint ist
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht für Akzeptanzgrenzen, Toleranzen oder sicherheitskritische Werte verwenden.
- entry_id: DE-ADJ-unm-glich
  lemma: unmöglich
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.impossible
    definition: unter den genannten technischen Bedingungen nicht realisierbar oder nicht eintretbar
  review_status: provisional_v0.0.2
- entry_id: DE-ADV-unten
  lemma: unten
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.down
    definition: kennzeichnet eine tiefere Position im festgelegten Bezugssystem
  review_status: provisional_v0.0.2
- entry_id: DE-PRE-unter
  lemma: unter
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.below_under
    definition: kennzeichnet eine räumlich tiefere Position oder eine Lage unter einem Objekt
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht für numerische Grenzwerte verwenden; dafür weniger als verwenden.
- entry_id: DE-ADJ-unterschiedlich
  lemma: unterschiedlich
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.different
    definition: hat im ausdrücklich verglichenen Merkmal nicht denselben Wert oder Zustand
  review_status: provisional_v0.0.2
- entry_id: DE-VER-untersuchen
  lemma: untersuchen
  part_of_speech: verb
  status: approved
  meanings:
  - id: examine
    definition: ein Objekt oder einen Bereich systematisch auf Schäden, Fehler oder andere festgelegte Merkmale
      ansehen oder prüfen
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-unvollst-ndig
  lemma: unvollständig
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.incomplete
    definition: enthält nicht alle für den definierten Umfang erforderlichen Teile oder Daten
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-unzul-ssig
  lemma: unzulässig
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.not_permitted
    definition: durch eine ausdrücklich geltende Anforderung, Grenze oder Freigabe nicht erlaubt
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-ursache
  lemma: Ursache
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.cause
    definition: Ereignis oder Zustand, der eine ausdrücklich genannte Wirkung hervorruft
  review_status: provisional_v0.0.2
  gender: fem
  plural: Ursachen
- entry_id: DE-VER-verbinden
  lemma: verbinden
  part_of_speech: verb
  status: approved
  meanings:
  - id: connect
    definition: zwei oder mehr Teile, Leitungen, Systeme oder Datenpfade funktional miteinander koppeln
  review_status: provisional_v0.0.2
  surface_forms:
  - verbunden
- entry_id: DE-NOU-verbindung
  lemma: Verbindung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.connection
    definition: mechanische, elektrische, stoffliche oder logische Kopplung zwischen ausdrücklich genannten Elementen
  review_status: provisional_v0.0.2
  gender: fem
  plural: Verbindungen
- entry_id: DE-ADJ-verboten
  lemma: verboten
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.forbidden
    definition: durch eine Regel oder Sicherheitsanforderung ausdrücklich nicht erlaubt
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-verbunden
  lemma: verbunden
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.connected
    definition: mit dem ausdrücklich genannten Objekt mechanisch, elektrisch oder logisch gekoppelt
  review_status: provisional_v0.0.2
  restrictions:
  - Art der Verbindung muss aus dem Kontext eindeutig sein.
- entry_id: DE-NOU-verfahren
  lemma: Verfahren
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.procedure
    definition: festgelegte Folge von Handlungen zur Erreichung eines technischen Ziels
  review_status: provisional_v0.0.2
  gender: neut
  plural: Verfahren
- entry_id: DE-ADJ-verf-gbar
  lemma: verfügbar
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.available
    definition: für die vorgesehene Verwendung oder Auswahl vorhanden und zugänglich
  review_status: provisional_v0.0.2
  restrictions:
  - Zeit- oder Systembezug nennen, wenn veränderlich.
- entry_id: DE-NOU-verfuegbarkeit
  lemma: Verfügbarkeit
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.verfuegbarkeit
    definition: Zustand, in dem eine ausdrücklich genannte Funktion, Ressource oder Komponente zur vorgesehenen
      Nutzung bereitsteht
  review_status: multi_industry_candidate_v0.1
  restrictions:
  - Nicht als unquantifizierte Zuverlässigkeitskennzahl verwenden.
- entry_id: DE-VER-vergleichen
  lemma: vergleichen
  part_of_speech: verb
  status: approved
  meanings:
  - id: compare
    definition: zwei oder mehr Werte, Zustände oder Merkmale gegenüberstellen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-verhindern
  lemma: verhindern
  part_of_speech: verb
  status: approved
  meanings:
  - id: prevent
    definition: eine ausdrücklich genannte unerwünschte Wirkung oder Handlung unmöglich machen
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-verletzung
  lemma: Verletzung
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.verletzung
    definition: körperliche Schädigung einer Person
  review_status: multi_industry_candidate_v0.1
  plural: Verletzungen
- entry_id: DE-VER-verriegeln
  lemma: verriegeln
  part_of_speech: verb
  status: approved
  meanings:
  - id: lock
    definition: eine mechanische oder logische Verriegelung in den gesicherten Zustand bringen
  review_status: provisional_v0.0.2
- entry_id: DE-ADJ-verriegelt
  lemma: verriegelt
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.locked
    definition: in einem definierten Verriegelungszustand
  review_status: provisional_v0.0.2
- entry_id: DE-VER-verringern
  lemma: verringern
  part_of_speech: verb
  status: approved
  meanings:
  - id: decrease.transitive
    definition: einen numerischen Wert kleiner machen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-verschieben
  lemma: verschieben
  part_of_speech: verb
  status: approved
  meanings:
  - id: move.relocate
    definition: ein Objekt oder Datenelement von einer Position an eine andere Position bewegen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-verschliessen
  lemma: verschließen
  part_of_speech: verb
  status: approved
  meanings:
  - id: close.seal_opening
    definition: eine Öffnung mit dem vorgesehenen Verschlusselement schließen
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - verschließe
  - verschließt
  - verschließen
  - verschloss
  - verschlossen
  restrictions:
  - Nicht mit verriegeln verwechseln.
- entry_id: DE-NOU-version
  lemma: Version
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.version
    definition: eindeutig identifizierter Entwicklungs- oder Ausgabestand eines Produkts, Dokuments oder Softwareelements
  review_status: multi_industry_candidate_v0.1
  plural: Versionen
- entry_id: DE-VER-verursachen
  lemma: verursachen
  part_of_speech: verb
  status: approved
  meanings:
  - id: cause
    definition: eine ausdrücklich genannte Wirkung als Ursache hervorrufen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-verweisen
  lemma: verweisen
  part_of_speech: verb
  status: approved
  meanings:
  - id: refer
    definition: den Leser auf eine eindeutig bezeichnete Stelle, Quelle oder Referenz lenken
  review_status: provisional_v0.0.2
- entry_id: DE-VER-verwenden
  lemma: verwenden
  part_of_speech: verb
  status: approved
  meanings:
  - id: use
    definition: ein Werkzeug, Material, Bauteil oder Hilfsmittel für einen ausdrücklich genannten Zweck einsetzen
  review_status: provisional_v0.0.2
  prohibited_synonyms:
  - benutzen
  - nutzen
  - gebrauchen
  surface_forms:
  - verwendet
- entry_id: DE-NOU-verwendung
  lemma: Verwendung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.verwendung
    definition: Einsatz eines Produkts, Werkzeugs, Stoffes oder Verfahrens für einen ausdrücklich genannten Zweck
  review_status: multi_industry_candidate_v0.1
  plural: Verwendungen
  restrictions:
  - In Anweisungen bevorzugt das direkte Verb verwenden.
- entry_id: DE-QUA-vier
  lemma: vier
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.four
    definition: bezeichnet die Zahl 4 in ausgeschriebener Form
  review_status: corpus_candidate_v0.0.3
- entry_id: DE-ADJ-voll
  lemma: voll
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.full
    definition: enthält die definierte maximale oder vorgesehene Füllmenge
  review_status: provisional_v0.0.2
  restrictions:
  - Bei Messbehältern nach Möglichkeit Füllgrenze nennen.
- entry_id: DE-ADJ-vollst-ndig
  lemma: vollständig
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.complete
    definition: enthält alle für den definierten Umfang erforderlichen Teile oder Daten
  review_status: provisional_v0.0.2
- entry_id: DE-ADV-vollst-ndig
  lemma: vollständig
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.completely
    definition: kennzeichnet, dass kein Teil oder Rest der beschriebenen Menge oder Handlung fehlt
  review_status: provisional_v0.0.2
- entry_id: DE-PRE-von
  lemma: von
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.from_of
    definition: kennzeichnet Ausgangspunkt, Urheber oder eindeutige Zuordnung
  review_status: provisional_v0.0.2
- entry_id: DE-PRE-vor
  lemma: vor
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.before_in_front
    definition: kennzeichnet eine räumlich vordere Position oder einen früheren Zeitpunkt
  review_status: provisional_v0.0.2
  restrictions:
  - Bei komplexen Zeitbedingungen einen bevor-Satz verwenden.
- entry_id: DE-ADJ-vorhanden
  lemma: vorhanden
  part_of_speech: adjective
  status: approved
  meanings:
  - id: adj.present
    definition: an der ausdrücklich genannten Stelle oder im System existent
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-vorschrift
  lemma: Vorschrift
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.vorschrift
    definition: verbindliche dokumentierte Regel oder Anforderung aus einer ausdrücklich identifizierten Quelle
  review_status: multi_industry_candidate_v0.1
  plural: Vorschriften
  restrictions:
  - Quelle oder Dokument nennen, wenn sie für die Handlung oder Konformität erforderlich ist.
- entry_id: DE-NOU-warnung
  lemma: Warnung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.warnung
    definition: Sicherheitsinformation, die auf eine Gefahr für Personen hinweist
  review_status: multi_industry_candidate_v0.1
  plural: Warnungen
  restrictions:
  - Risikokategorie muss mit dem anwendbaren Sicherheitsstandard übereinstimmen.
- entry_id: DE-VER-warten
  lemma: warten
  part_of_speech: verb
  status: restricted
  meanings:
  - id: wait
    definition: eine Handlung bis zum Eintritt eines ausdrücklich genannten Zeitpunkts oder Zustands nicht fortsetzen
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht im Sinn von Instandhaltung verwenden. Für Instandhaltung Projektterminologie verwenden.
- entry_id: DE-PRE-wegen
  lemma: wegen
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.because_of
    definition: kennzeichnet eine ausdrücklich benannte Ursache
  review_status: provisional_v0.0.2
  restrictions:
  - Bei komplexer Ursache einen weil-Satz verwenden.
- entry_id: DE-CON-weil
  lemma: weil
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.because
    definition: leitet eine ausdrücklich genannte Ursache oder Begründung ein
  review_status: provisional_v0.0.2
- entry_id: DE-PHR-weniger-als
  lemma: weniger als
  part_of_speech: phrase
  status: approved
  meanings:
  - id: phrase.less_than
    definition: kennzeichnet einen Wert oder eine Menge unterhalb einer nicht eingeschlossenen Grenze
  review_status: provisional_v0.0.2
- entry_id: DE-CON-wenn
  lemma: wenn
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.if
    definition: leitet eine ausdrücklich genannte Bedingung ein
  review_status: provisional_v0.0.2
  approved_examples:
  - Wenn die Anzeige rot ist, stoppen Sie den Test.
- entry_id: DE-VER-werden
  lemma: werden
  part_of_speech: verb
  status: restricted
  meanings:
  - id: become.future
    definition: den Übergang in einen neuen Zustand oder eine ausdrücklich notwendige Zukunft ausdrücken
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht für vermeidbares Vorgangspassiv verwenden. Zukunft nach Möglichkeit mit Präsens und Zeitangabe ausdrücken.
  surface_forms:
  - werde
  - wirst
  - wird
  - werden
  - werdet
  - wurde
  - wurden
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-NOU-wert
  lemma: Wert
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.value
    definition: quantitative oder eindeutig codierte Ausprägung einer Größe oder eines Parameters
  review_status: provisional_v0.0.2
  gender: masc
  plural: Werte
- entry_id: DE-ADJ-wichtig
  lemma: wichtig
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.wichtig
    definition: für Sicherheit, korrekte Funktion oder das Ergebnis wesentlich
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - wichtige
  - wichtigen
  - wichtiger
  - wichtiges
  - wichtigem
  restrictions:
  - Wenn möglich den konkreten Grund oder die Folge nennen.
- entry_id: DE-CON-wie
  lemma: wie
  part_of_speech: conjunction
  status: restricted
  meanings:
  - id: comparison.like
    definition: kennzeichnet einen ausdrücklich benannten Vergleich oder eine ausdrücklich benannte Referenz
  review_status: corpus_candidate_v0.0.3
  restrictions:
  - Vergleich oder Referenz muss eindeutig sein. Nicht als vage Art-und-Weise-Angabe verwenden.
- entry_id: DE-VER-wiederholen
  lemma: wiederholen
  part_of_speech: verb
  status: approved
  meanings:
  - id: repeat
    definition: dieselbe ausdrücklich bestimmte Handlung oder Prüfung erneut ausführen
  review_status: provisional_v0.0.2
- entry_id: DE-PRO-wir
  lemma: wir
  part_of_speech: pronoun
  status: restricted
  meanings:
  - id: pronoun.organization
    definition: bezeichnet die herausgebende Organisation oder den Hersteller
  review_status: provisional_v0.0.2
  surface_forms:
  - wir
  - uns
  restrictions:
  - Nur verwenden, wenn der Autor eindeutig für die herausgebende Organisation spricht.
- entry_id: DE-VER-waehlen
  lemma: wählen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: verb.waehlen
    definition: eine Option aus einer ausdrücklich vorhandenen Menge auswählen
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - wähle
  - wählst
  - wählt
  - wählen
  - wählte
  - wählten
  - gewählt
  restrictions:
  - Auswahlmenge oder Benutzeroberflächenoption muss eindeutig sein.
  approved_examples:
  - Wählen Sie die Funktion aus.
- entry_id: DE-CON-w-hrend
  lemma: während
  part_of_speech: conjunction
  status: approved
  meanings:
  - id: conj.while
    definition: kennzeichnet zwei Zustände oder Handlungen, die im selben Zeitraum gelten
  review_status: provisional_v0.0.2
- entry_id: DE-PRE-w-hrend
  lemma: während
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.during
    definition: kennzeichnet einen Zeitraum, in dem ein Zustand oder eine Handlung gilt
  review_status: provisional_v0.0.2
- entry_id: DE-QUA-zehn
  lemma: zehn
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.ten
    definition: bezeichnet die Zahl 10 in ausgeschriebener Form
  review_status: corpus_candidate_v0.0.3
- entry_id: DE-VER-zeigen
  lemma: zeigen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: show
    definition: Information oder einen sichtbaren Zustand für den Leser erkennbar machen
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht im Sinn von beweisen oder hinweisen verwenden.
  surface_forms:
  - zeige
  - zeigst
  - zeigt
  - zeigen
  - zeigte
  - zeigten
  - gezeigt
  morphology_note: Surface forms support lexical resolution; tense/mode remains constrained by STG-3.2.
- entry_id: DE-NOU-zeit
  lemma: Zeit
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.time
    definition: Zeitpunkt oder Zeitgröße im ausdrücklich genannten Kontext
  review_status: provisional_v0.0.2
  gender: fem
  plural: Zeiten
- entry_id: DE-VER-zerlegen
  lemma: zerlegen
  part_of_speech: verb
  status: approved
  meanings:
  - id: disassemble
    definition: eine Baugruppe nach einem vorgesehenen Verfahren in ihre Teile trennen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-ziehen
  lemma: ziehen
  part_of_speech: verb
  status: approved
  meanings:
  - id: pull
    definition: eine Kraft in Richtung zum Kraftausübenden oder entlang einer definierten Richtung ausüben
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-ziel
  lemma: Ziel
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.target
    definition: ausdrücklich festgelegter gewünschter Endzustand oder Zweck
  review_status: provisional_v0.0.2
  gender: neut
  plural: Ziele
- entry_id: DE-PRE-zu
  lemma: zu
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.to
    definition: kennzeichnet eine Richtung zu einem Ziel oder eine feste Beziehung in einer freigegebenen Wortgruppe
  review_status: provisional_v0.0.2
- entry_id: DE-ADV-zuerst
  lemma: zuerst
  part_of_speech: adverb
  status: approved
  meanings:
  - id: adv.first
    definition: kennzeichnet den ersten Schritt einer ausdrücklich geordneten Folge
  review_status: provisional_v0.0.2
- entry_id: DE-NOU-zugriff
  lemma: Zugriff
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.access
    definition: technische Möglichkeit, auf ein Objekt, einen Bereich oder Daten zuzugreifen
  review_status: provisional_v0.0.2
  gender: masc
  plural: Zugriffe
- entry_id: DE-ADJ-zul-ssig
  lemma: zulässig
  part_of_speech: adjective
  status: restricted
  meanings:
  - id: adj.permitted
    definition: durch eine ausdrücklich geltende Anforderung, Grenze oder Freigabe erlaubt
  review_status: provisional_v0.0.2
  restrictions:
  - Geltende Anforderung oder Grenzwert muss bestimmbar sein.
- entry_id: DE-PHR-zum-beispiel
  lemma: zum Beispiel
  part_of_speech: phrase
  status: restricted
  meanings:
  - id: example.nonexhaustive
    definition: leitet ausdrücklich eine nicht vollständige Menge von Beispielen ein
  review_status: corpus_candidate_v0.0.3
  surface_forms:
  - zum Beispiel
  restrictions:
  - Nicht verwenden, wenn die Liste vollständig sein muss.
- entry_id: DE-VER-zusammenbauen
  lemma: zusammenbauen
  part_of_speech: verb
  status: approved
  meanings:
  - id: assemble
    definition: mehrere Teile nach einer festgelegten Struktur zu einer Baugruppe verbinden
  review_status: provisional_v0.0.2
  separable: true
  prefix: zusammen
- entry_id: DE-NOU-zustand
  lemma: Zustand
  part_of_speech: noun
  status: approved
  meanings:
  - id: noun.state
    definition: feststellbare Ausprägung eines Systems, Objekts oder Parameters zu einem Zeitpunkt
  review_status: provisional_v0.0.2
  gender: masc
  plural: Zustände
- entry_id: DE-ADV-zusaetzlich
  lemma: zusätzlich
  part_of_speech: adverb
  status: restricted
  meanings:
  - id: addition.additional
    definition: kennzeichnet ein weiteres, ausdrücklich identifiziertes Element neben bereits genannten Elementen
  review_status: corpus_candidate_v0.0.3
  restrictions:
  - Das zusätzliche Element muss konkret genannt sein.
- entry_id: DE-QUA-zwei
  lemma: zwei
  part_of_speech: quantifier
  status: approved
  meanings:
  - id: quantifier.two
    definition: bezeichnet die Zahl 2 in ausgeschriebener Form
  review_status: provisional_v0.0.2
- entry_id: DE-PRE-zwischen
  lemma: zwischen
  part_of_speech: preposition
  status: approved
  meanings:
  - id: prep.between
    definition: kennzeichnet eine Position oder Beziehung zwischen zwei klar identifizierten Grenzen oder Objekten
  review_status: provisional_v0.0.2
- entry_id: DE-VER-z-hlen
  lemma: zählen
  part_of_speech: verb
  status: approved
  meanings:
  - id: count
    definition: die Anzahl diskreter Elemente bestimmen
  review_status: provisional_v0.0.2
- entry_id: DE-VER-ndern
  lemma: ändern
  part_of_speech: verb
  status: restricted
  meanings:
  - id: change
    definition: einen ausdrücklich bezeichneten Wert, Zustand oder Inhalt in einen anderen Wert, Zustand oder Inhalt
      überführen
  review_status: provisional_v0.0.2
  restrictions:
  - Zielzustand oder geänderten Parameter nennen.
- entry_id: DE-NOU-aenderung
  lemma: Änderung
  part_of_speech: noun
  status: restricted
  meanings:
  - id: noun.aenderung
    definition: feststellbare Abweichung eines Zustands, Werts, Produkts oder Dokuments gegenüber einem vorherigen
      Stand
  review_status: multi_industry_candidate_v0.1
  plural: Änderungen
  restrictions:
  - Geändertes Objekt oder Merkmal nennen.
- entry_id: DE-VER-ffnen
  lemma: öffnen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: open
    definition: ein Teil, eine Öffnung, Datei oder Funktion aus dem geschlossenen Zustand zugänglich machen
  review_status: provisional_v0.0.2
  restrictions:
  - Bei Software und Mechanik muss der Kontext eindeutig sein.
  surface_forms:
  - geöffnet
- entry_id: DE-PRE-ber
  lemma: über
  part_of_speech: preposition
  status: restricted
  meanings:
  - id: prep.above_over
    definition: kennzeichnet eine räumlich höhere Position oder eine Bewegung über ein Objekt
  review_status: provisional_v0.0.2
  restrictions:
  - Nicht für numerische Grenzwerte verwenden; dafür mehr als verwenden.
- entry_id: DE-VER-bertragen
  lemma: übertragen
  part_of_speech: verb
  status: restricted
  meanings:
  - id: transmit
    definition: Daten, Energie, Kraft oder ein Signal von einer Quelle zu einem Ziel weitergeben
  review_status: provisional_v0.0.2
  restrictions:
  - Die Art der übertragenen Größe muss aus dem Satz eindeutig sein.
- entry_id: DE-VER-berwachen
  lemma: überwachen
  part_of_speech: verb
  status: approved
  meanings:
  - id: monitor
    definition: einen Zustand oder Wert fortlaufend beobachten oder erfassen
  review_status: provisional_v0.0.2

```

---

## Strukturierter Anhang: `dictionary/prohibited-words.yaml`

```yaml
schema_version: '0.1'
release: 0.3.0
status: corpus_validated_authoring_core
entries:
- term: abklemmen
  status: prohibited
  reason: fach-/umgangssprachlich für unterschiedliche Trennvorgänge
  rewrite: trennen und Objekt/Verbindung nennen oder als technischen Term freigeben.
  approved_alternatives:
  - trennen
- term: aktuell
  status: prohibited
  reason: mehrdeutig zwischen derzeit gültig und neueste Version
  rewrite: derzeit, gültig oder konkrete Version/Datum nennen.
  approved_alternatives:
  - derzeit
  surface_forms: [aktuelle, aktuellen, aktueller, aktuelles, aktuellem]
- term: anfangen
  status: prohibited
  reason: Synonymvariation zu starten
  rewrite: starten verwenden.
  approved_alternatives:
  - starten
- term: angemessen
  status: prohibited
  reason: Bewertungskriterium bleibt ungenannt
  rewrite: Messbares oder referenziertes Kriterium nennen.
- term: anhand
  status: review_required
  reason: die Datenbasis oder das Mittel kann implizit bleiben
  rewrite: Datenbasis ausdrücklich nennen; wenn möglich mit oder aus verwenden.
- term: anmachen
  status: prohibited
  reason: umgangssprachlich und mehrdeutig
  rewrite: einschalten verwenden.
  approved_alternatives:
  - einschalten
- term: anschließend
  status: prohibited
  reason: stilistische Sequenzvariante zu danach
  rewrite: danach verwenden.
  approved_alternatives:
  - danach
  surface_forms: [anschließende, anschließenden, anschließender, anschließendes, anschließendem]
- term: arbeiten
  status: review_required
  reason: kann menschliche Tätigkeit oder Maschinenfunktion bedeuten
  rewrite: Konkrete Tätigkeit oder funktionieren/betreiben verwenden.
- term: aufspüren
  status: prohibited
  reason: stilistische oder bildhafte Variante für finden/prüfen
  rewrite: finden oder prüfen entsprechend der beabsichtigten Handlung verwenden.
  approved_alternatives:
  - finden
  - prüfen
- term: ausmachen
  status: prohibited
  reason: umgangssprachlich und mehrdeutig
  rewrite: ausschalten verwenden.
  approved_alternatives:
  - ausschalten
- term: ausreichend
  status: review_required
  reason: Kriterium für ausreichend bleibt häufig ungenannt
  rewrite: Grenzwert oder Referenz nennen.
  surface_forms: [ausreichende, ausreichenden, ausreichender, ausreichendes, ausreichendem]
- term: ausschließlich
  status: review_required
  reason: starke Exklusivitätsaussage; der ausgeschlossene Bereich muss klar sein
  rewrite: Nur verwenden, wenn die Exklusivität technisch oder normativ belegt ist; sonst konkrete Einschränkung
    nennen.
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - ausschliesslich
- term: austauschen
  status: prohibited
  reason: kann ersetzen oder gegenseitig vertauschen bedeuten
  rewrite: ersetzen verwenden, wenn ein Ersatzteil eingesetzt wird.
  approved_alternatives:
  - ersetzen
- term: automatisch
  status: review_required
  reason: kann Systemfunktion oder bloße Erwartung bedeuten
  rewrite: Nur als freigegebene technische Funktion verwenden; sonst Akteur/Trigger nennen.
  surface_forms: [automatische, automatischen, automatischer, automatisches, automatischem]
- term: bald
  status: prohibited
  reason: Zeitgrenze ist nicht messbar
  rewrite: Frist oder Zeitpunkt nennen.
- term: baldmöglichst
  status: prohibited
  reason: Zeitgrenze ist nicht messbar
  rewrite: Frist oder Zeitpunkt nennen.
- term: bearbeiten
  status: review_required
  reason: mehrdeutig zwischen mechanisch bearbeiten, Daten bearbeiten und administrativ bearbeiten
  rewrite: Konkrete technische Handlung oder als Domainterm freigeben.
- term: beginnen
  status: prohibited
  reason: Synonymvariation zu starten
  rewrite: starten verwenden.
  approved_alternatives:
  - starten
- term: behandeln
  status: review_required
  reason: mehrdeutig zwischen verarbeiten, medizinisch behandeln, chemisch behandeln und thematisieren
  rewrite: Konkretes technisches Verb verwenden.
- term: behutsam
  status: prohibited
  reason: Handlung oder Grenzwert bleibt unbestimmt
  rewrite: Konkrete Geschwindigkeit, Kraft oder Abstand nennen.
  surface_forms: [behutsame, behutsamen, behutsamer, behutsames, behutsamem]
- term: bei Bedarf
  status: prohibited
  reason: Bedingung für den Bedarf ist nicht definiert
  rewrite: Bedingung mit wenn ausdrücklich nennen.
- term: benutzen
  status: prohibited
  reason: Synonymvariation zu verwenden
  rewrite: verwenden verwenden.
  approved_alternatives:
  - verwenden
- term: bereits
  status: review_required
  reason: unspezifischer Zeitbezug; häufig entbehrlich
  rewrite: weglassen oder einen konkreten Zeitpunkt/Zustand nennen.
- term: berücksichtigen
  status: review_required
  reason: kann eine relevante Bedingung nennen, ohne zu sagen, welche konkrete Handlung daraus folgt
  rewrite: Bedingung ausdrücklich formulieren und die daraus erforderliche Handlung nennen.
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - berücksichtigt
  - berücksichtigte
  - berücksichtigten
- term: beseitigen
  status: review_required
  reason: kann physisches Entfernen oder Fehlerbehebung bedeuten
  rewrite: entfernen für Material/Teil oder beheben für einen identifizierten Fehler verwenden.
  approved_alternatives:
  - entfernen
  - beheben
- term: bestmöglich
  status: prohibited
  reason: nennt kein überprüfbares Zielkriterium
  rewrite: Messbares oder referenziertes Kriterium nennen.
  surface_forms: [bestmögliche, bestmöglichen, bestmöglicher, bestmögliches, bestmöglichem]
- term: beziehungsweise
  status: prohibited
  reason: kann oder, und, genauer gesagt oder eine Zuordnung bedeuten
  rewrite: Exakte Relation mit und, oder oder getrennten Sätzen ausdrücken.
  approved_alternatives:
  - und
  - oder
- term: bieten
  status: review_required
  reason: abstraktes Besitz- oder Leistungsverb; technische Beziehung bleibt häufig unpräzise
  rewrite: Je nach Bedeutung haben, geben, bereitstellen oder enthalten verwenden.
  review_status: multi_industry_candidate_v0.1
  approved_alternatives:
  - haben
  - geben
  - bereitstellen
  - enthalten
  surface_forms:
  - bietet
  - bot
  - boten
  - geboten
- term: bringen
  status: review_required
  reason: kann physische Bewegung oder Zustandsänderung bedeuten
  rewrite: bewegen, positionieren oder Zustandsverb verwenden.
- term: bzw.
  status: prohibited
  reason: mehrdeutige Kurzform von beziehungsweise
  rewrite: Exakte Relation ausschreiben.
  approved_alternatives:
  - und
  - oder
- term: ca.
  status: review_required
  reason: Abkürzung und unklare Genauigkeit
  rewrite: ungefähr nur für echte Näherungswerte verwenden; sonst exakten Wert nennen.
  approved_alternatives:
  - ungefähr
- term: checken
  status: prohibited
  reason: Umgangssprache/Anglizismus für mehrere mögliche Prüfhandlungen
  rewrite: prüfen verwenden.
  approved_alternatives:
  - prüfen
- term: circa
  status: review_required
  reason: Näherungsangabe kann bei Grenzwerten unzulässig sein
  rewrite: ungefähr nur für echte Näherungswerte verwenden; sonst exakten Wert nennen.
  approved_alternatives:
  - ungefähr
- term: da
  status: review_required
  reason: kann Ort, Ursache oder Verweis bedeuten
  rewrite: dort für einen eindeutigen Ort, weil für eine Ursache oder das konkrete Bezugsnomen verwenden.
- term: dabei
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Bezugsnomen, Handlung oder Bedingung wiederholen; siehe STG-DE-4.5.
- term: dafür
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Bezugsnomen, Zweck oder Handlung ausdrücklich nennen; siehe STG-DE-4.5.
- term: daher
  status: prohibited
  reason: stilistische Ergebnisvariante zu deshalb
  rewrite: deshalb verwenden.
  approved_alternatives:
  - deshalb
- term: daraus
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Quelle, Ursache oder Bestandteil ausdrücklich nennen; siehe STG-DE-4.5.
- term: darüber
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Bezugsobjekt oder Thema ausdrücklich nennen; siehe STG-DE-4.5.
- term: davon
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Bezugsobjekt ausdrücklich nennen; siehe STG-DE-4.5.
- term: dazu
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Bezugsobjekt, Zweck oder Handlung ausdrücklich nennen; siehe STG-DE-4.5.
- term: detailliert
  status: review_required
  reason: unspezifische Aussage über Informationsumfang
  rewrite: Konkrete Information geben oder den relevanten Abschnitt nennen.
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - detaillierte
  - detaillierten
  - detaillierter
  - detailliertes
  - detailliertem
- term: doch
  status: prohibited
  reason: Modalpartikel oder unspezifischer Kontrast
  rewrite: aber oder explizite Gegenaussage verwenden.
- term: durchführen
  status: review_required
  reason: Funktionsverb kann eine spezifische Handlung verdecken
  rewrite: Direktes Verb verwenden; nur bei offiziell benanntem Verfahren/Test ohne präziseres Verb zulassen.
- term: eben
  status: prohibited
  reason: Modalpartikel oder mehrdeutige Bedeutung
  rewrite: Entfernen; nur als technischer Begriff für geometrisch eben zulassen, wenn als Terminologie freigegeben.
- term: einfach
  status: review_required
  reason: kann Füllwort oder unprüfbare Bewertung bedeuten
  rewrite: Entfernen oder als definierte Eigenschaft ausdrücklich qualifizieren.
  surface_forms: [einfache, einfachen, einfacher, einfaches, einfachem]
- term: einsetzen
  status: review_required
  reason: mehrdeutig zwischen verwenden, einbauen, einfügen und Personal zuweisen
  rewrite: verwenden, einbauen oder einfügen gemäß der konkreten Handlung verwenden.
  approved_alternatives:
  - verwenden
  - einbauen
  - einfügen
- term: entsprechend
  status: review_required
  reason: Bezug oder Zuordnung kann fehlen
  rewrite: Bezugsobjekt oder Regel ausdrücklich nennen.
  surface_forms: [entsprechende, entsprechenden, entsprechender, entsprechendes, entsprechendem]
- term: entsprechend den Vorschriften
  status: prohibited
  reason: Vorschriften sind nicht identifiziert
  rewrite: Dokument, Abschnitt oder konkrete Anforderung nennen.
- term: erfassen
  status: prohibited
  reason: mehrdeutig zwischen eingeben, messen, erkennen und dokumentieren
  rewrite: eingeben, messen, erkennen oder dokumentieren entsprechend der Bedeutung verwenden.
- term: erfolgen
  status: prohibited
  reason: unpersönliche/passivische Form verschleiert den Akteur
  rewrite: Akteur und direktes Verb nennen.
  surface_forms:
  - erfolgt
  - erfolgte
  - erfolgten
  - erfolgend
- term: ermöglichen
  status: review_required
  reason: abstrakte Fähigkeitskonstruktion kann den eigentlichen Akteur und die Handlung verdecken
  rewrite: Akteur + direktes Verb oder können + direktes Verb verwenden.
- term: erst
  status: prohibited
  reason: mehrdeutig zwischen zuerst, erst ab und nur
  rewrite: zuerst, frühestens oder nur entsprechend der Bedeutung verwenden.
- term: etc.
  status: prohibited
  reason: offene Aufzählung lässt relevante Elemente ungenannt
  rewrite: Vollständige Liste geben oder mit andere + definierter Kategorie abschließen.
- term: etwa
  status: review_required
  reason: mehrdeutig zwischen ungefähr und beispielsweise
  rewrite: ungefähr oder Beispielkonstruktion entsprechend der Bedeutung verwenden.
- term: eventuell
  status: prohibited
  reason: unspezifische Möglichkeit
  rewrite: kann mit klarer Bedingung oder Ursache verwenden.
  surface_forms: [eventuelle, eventuellen, eventueller, eventuelles, eventuellem]
- term: extrem
  status: review_required
  reason: unspezifische Verstärkung ohne Grenze
  rewrite: Messwert oder definierte Sicherheitskategorie nennen.
- term: fachgerecht
  status: prohibited
  reason: verweist auf ungenannte Fachregeln
  rewrite: Anwendbare Spezifikation oder konkrete Handlung nennen.
- term: fahren
  status: review_required
  reason: kann Fahrzeugbewegung, Maschinenhub oder Softwarezustand bedeuten
  rewrite: Konkrete Bewegungs- oder Systemaktion verwenden.
- term: falls erforderlich
  status: prohibited
  reason: Bedingung für erforderlich ist nicht definiert
  rewrite: Bedingung mit wenn und messbarem Kriterium nennen.
- term: falls möglich
  status: prohibited
  reason: Bedingung für möglich ist nicht definiert
  rewrite: Technische Bedingung ausdrücklich nennen.
- term: falls nötig
  status: prohibited
  reason: Bedingung für nötig ist nicht definiert
  rewrite: Bedingung mit wenn nennen.
- term: festmachen
  status: prohibited
  reason: umgangssprachliche Alternative zu befestigen
  rewrite: befestigen verwenden.
  approved_alternatives:
  - befestigen
- term: fixieren
  status: prohibited
  reason: kann befestigen, chemisch fixieren oder gedanklich festlegen bedeuten
  rewrite: befestigen oder technische Spezialbedeutung als Terminologie freigeben.
  approved_alternatives:
  - befestigen
- term: führen
  status: review_required
  reason: hochgradig mehrdeutig zwischen physischer Bewegung, Leitung, Ergebnisbeziehung und Bedienhandlung
  rewrite: Konkretes Verb oder eine explizite Ursache-Folge-Konstruktion verwenden.
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - führt
  - führte
  - führten
  - geführt
- term: gebrauchen
  status: prohibited
  reason: Synonymvariation zu verwenden und teilweise veraltet
  rewrite: verwenden verwenden.
  approved_alternatives:
  - verwenden
- term: geeignet
  status: review_required
  reason: Eignungskriterium bleibt häufig ungenannt
  rewrite: Eignungskriterium oder freigegebene Spezifikation nennen.
- term: gegebenen Bedingungen
  status: prohibited
  reason: Bedingungen sind nicht identifiziert
  rewrite: Konkrete Bedingungen nennen.
- term: gegebenenfalls
  status: prohibited
  reason: versteckt eine nicht genannte Bedingung
  rewrite: Bedingung mit wenn ausdrücklich nennen.
  approved_alternatives:
  - wenn
- term: genügend
  status: review_required
  reason: Kriterium für genügend bleibt häufig ungenannt
  rewrite: Grenzwert oder Referenz nennen.
  surface_forms: [genügende, genügenden, genügender, genügendes, genügendem]
- term: gerade
  status: prohibited
  reason: mehrdeutig zwischen aktuell, genau jetzt, geometrisch gerade und Verstärkung
  rewrite: Exakte Bedeutung ausdrücken oder als freigegebenen technischen Term führen.
- term: gewährleisten
  status: review_required
  reason: abstrakte Ergebniszusage ohne sichtbare Prüfhandlung oder messbares Kriterium
  rewrite: Prüfbare Bedingung und konkrete Maßnahme nennen; falls passend sicherstellen mit prüfbarer Bedingung
    verwenden.
  review_status: multi_industry_candidate_v0.1
  approved_alternatives:
  - sicherstellen
  surface_forms:
  - gewährleistet
  - gewährleistete
  - gewährleisteten
- term: ggf.
  status: prohibited
  reason: Abkürzung von gegebenenfalls; die Bedingung bleibt implizit
  rewrite: Bedingung mit wenn ausdrücklich nennen.
  approved_alternatives:
  - wenn
- term: grundsätzlich
  status: prohibited
  reason: Geltungsbereich und Ausnahmen können unklar sein
  rewrite: Geltungsbereich und Ausnahmen ausdrücklich nennen.
  surface_forms: [grundsätzliche, grundsätzlichen, grundsätzlicher, grundsätzliches, grundsätzlichem]
- term: halt
  status: prohibited
  reason: Modalpartikel ohne technische Information
  rewrite: Entfernen.
- term: handhaben
  status: review_required
  reason: vage oder jargonartige Sammelbezeichnung
  rewrite: Konkrete Handlungen nennen.
- term: hierfür
  status: review_required
  reason: Pronominaladverb mit möglichem mehrdeutigem Bezug
  rewrite: Bezugsobjekt oder Zweck ausdrücklich nennen; siehe STG-DE-4.5.
- term: hochfahren
  status: prohibited
  reason: kann Booten, Starten oder Erhöhen bedeuten
  rewrite: starten oder Wert erhöhen entsprechend der Bedeutung verwenden.
- term: hochgradig
  status: prohibited
  reason: unspezifischer Grad
  rewrite: Messwert oder definierte Kategorie nennen.
  surface_forms: [hochgradige, hochgradigen, hochgradiger, hochgradiges, hochgradigem]
- term: im Allgemeinen
  status: prohibited
  reason: Geltungsbereich und Ausnahmen können unklar sein
  rewrite: Konkreten Geltungsbereich nennen.
- term: in Betrieb nehmen
  status: review_required
  reason: kann mehrere technische Einzelschritte zusammenfassen
  rewrite: Konkrete Start-/Aktivierungsanweisung oder freigegebenes Inbetriebnahmeverfahren nennen.
- term: in der Regel
  status: prohibited
  reason: Ausnahmen bleiben ungenannt
  rewrite: Regel und Ausnahmen ausdrücklich nennen.
- term: insbesondere
  status: review_required
  reason: kann einen offenen, nicht vollständigen Umfang erzeugen
  rewrite: vollständige Menge nennen oder ausdrücklich als Beispiel kennzeichnen.
- term: irgendwann
  status: prohibited
  reason: Zeitpunkt ist unbestimmt
  rewrite: Konkreten Zeitpunkt oder Bedingung nennen.
- term: irgendwelche
  status: prohibited
  reason: Menge und Auswahl sind unbestimmt
  rewrite: Konkrete Elemente oder Kategorie nennen.
- term: irgendwie
  status: prohibited
  reason: Methode ist unbestimmt
  rewrite: Konkrete Methode nennen.
- term: irgendwo
  status: prohibited
  reason: Ort ist unbestimmt
  rewrite: Konkreten Ort nennen.
- term: jederzeit
  status: review_required
  reason: unbegrenzte zeitliche Aussage kann technisch oder vertraglich zu stark sein
  rewrite: Gültigen Zeitraum oder Systemzustand nennen, wenn die Verfügbarkeit nicht wirklich uneingeschränkt ist.
  review_status: multi_industry_candidate_v0.1
- term: jedoch
  status: prohibited
  reason: stilistische Kontrastvariante zu aber
  rewrite: aber verwenden.
  approved_alternatives:
  - aber
- term: jeweils
  status: review_required
  reason: Zuordnung kann unklar sein, wenn mehrere Mengen oder Objekte vorkommen
  rewrite: Zuordnung pro Objekt oder Einheit ausdrücklich angeben; je verwenden, wenn eine Rate gemeint ist.
  approved_alternatives:
  - je
- term: kontrollieren
  status: prohibited
  reason: kann prüfen oder steuern bedeuten
  rewrite: prüfen für Inspektion; steuern/regeln für Systemkontrolle verwenden.
  approved_alternatives:
  - prüfen
  - steuern
  - regeln
- term: koppeln
  status: prohibited
  reason: kann mechanische, elektrische oder logische Spezialbedeutung haben
  rewrite: verbinden verwenden oder als technischen Term freigeben.
  approved_alternatives:
  - verbinden
- term: könnte
  status: prohibited
  reason: unspezifische hypothetische Möglichkeit
  rewrite: kann mit klarer Bedingung oder explizite Wahrscheinlichkeit verwenden.
  approved_alternatives:
  - können
- term: könnten
  status: prohibited
  reason: unspezifische hypothetische Möglichkeit
  rewrite: können mit klarer Bedingung verwenden.
  approved_alternatives:
  - können
- term: laufen
  status: prohibited
  reason: kann funktionieren, sich bewegen oder Software ausführen bedeuten
  rewrite: funktionieren, bewegen oder ausführen entsprechend der Bedeutung verwenden.
- term: lediglich
  status: prohibited
  reason: stilistische Variante zu nur
  rewrite: nur verwenden.
  approved_alternatives:
  - nur
- term: leicht
  status: review_required
  reason: mehrdeutig zwischen geringem Gewicht, geringer Kraft und einfach
  rewrite: Messwert oder eindeutiges Adjektiv verwenden.
- term: letzte
  status: review_required
  reason: mehrdeutig zwischen vorherige und endgültige
  rewrite: vorherige oder endgültige entsprechend der Bedeutung verwenden.
- term: machen
  status: prohibited
  reason: zu allgemeines Verb für technische Handlungen
  rewrite: Präzises direktes Verb verwenden.
- term: mal
  status: prohibited
  reason: umgangssprachliche Modalpartikel
  rewrite: Entfernen; mathematische Multiplikation separat als Symbol oder multiplizieren ausdrücken.
- term: man
  status: prohibited
  reason: Akteur bleibt unbestimmt
  rewrite: Formalen Imperativ oder konkreten Akteur verwenden.
- term: meistens
  status: prohibited
  reason: Häufigkeit ist unbestimmt
  rewrite: Häufigkeit quantifizieren oder Bedingungen nennen.
- term: möglicherweise
  status: prohibited
  reason: unspezifische Möglichkeit
  rewrite: kann mit klarer Bedingung oder Ursache verwenden.
- term: möglichst
  status: prohibited
  reason: nennt kein überprüfbares Ziel oder Grenzkriterium
  rewrite: Messbaren Zielwert, Grenzwert oder konkrete Handlung nennen.
- term: müsste
  status: prohibited
  reason: verbindliche Anforderung und Unsicherheit werden vermischt
  rewrite: muss oder klare Möglichkeitsaussage verwenden.
  approved_alternatives:
  - müssen
- term: müssten
  status: prohibited
  reason: verbindliche Anforderung und Unsicherheit werden vermischt
  rewrite: müssen oder klare Möglichkeitsaussage verwenden.
  approved_alternatives:
  - müssen
- term: nach Bedarf
  status: prohibited
  reason: Bedingung für den Bedarf ist nicht definiert
  rewrite: Bedingung und Handlung ausdrücklich nennen.
- term: neueste
  status: review_required
  reason: relative Version ohne Referenzzeitpunkt
  rewrite: Konkrete Version oder Datum nennen.
- term: noch
  status: review_required
  reason: mehrdeutiger Zeit-, Mengen- oder Fortsetzungsbezug
  rewrite: konkreten Zeitpunkt, Restwert oder Zustand nennen.
- term: normalerweise
  status: prohibited
  reason: Ausnahmen bleiben ungenannt
  rewrite: Normalzustand definieren oder konkrete Bedingung nennen.
- term: nutzen
  status: prohibited
  reason: kann verwenden oder einen Vorteil ziehen bedeuten
  rewrite: verwenden für Gebrauch; Vorteil explizit beschreiben.
  approved_alternatives:
  - verwenden
- term: nächste
  status: review_required
  reason: kann räumlich oder zeitlich gemeint sein
  rewrite: Richtung, Schritt oder Zeitpunkt ausdrücklich nennen.
- term: optimal
  status: prohibited
  reason: behauptet ein Optimum ohne definiertes Optimierungskriterium
  rewrite: Konkretes Ziel oder Grenzkriterium nennen.
- term: ordnungsgemäß
  status: prohibited
  reason: verweist auf eine nicht genannte Norm oder korrekte Ausführung
  rewrite: Konkrete Anforderung oder Referenz nennen.
  surface_forms: [ordnungsgemäße, ordnungsgemäßen, ordnungsgemäßer, ordnungsgemäßes, ordnungsgemäßem]
- term: pro
  status: prohibited
  reason: Synonymvariation zu je bei Mengen pro Einheit
  rewrite: je verwenden.
  approved_alternatives:
  - je
- term: problemlos
  status: prohibited
  reason: behauptet das Fehlen von Problemen ohne Kriterium
  rewrite: Konkrete Bedingung oder erwartetes Ergebnis nennen.
  surface_forms: [problemlose, problemlosen, problemloser, problemloses, problemlosem]
- term: realisieren
  status: prohibited
  reason: mehrdeutig zwischen umsetzen und erkennen
  rewrite: konkretes Verb verwenden.
- term: relativ
  status: review_required
  reason: Vergleichsmaßstab fehlt häufig
  rewrite: Vergleichsmaßstab oder Messwert ausdrücklich nennen.
- term: rund
  status: review_required
  reason: kann geometrisch oder ungefähr bedeuten
  rewrite: ungefähr oder konkrete Geometrie ausdrücken.
- term: runterfahren
  status: prohibited
  reason: kann Stoppen, Herunterfahren oder Verringern bedeuten
  rewrite: System stoppen/beenden oder Wert verringern ausdrücklich formulieren.
- term: sachgemäß
  status: prohibited
  reason: verweist auf eine nicht genannte korrekte Methode
  rewrite: Konkrete Handlung oder Referenz nennen.
  surface_forms: [sachgemäße, sachgemäßen, sachgemäßer, sachgemäßes, sachgemäßem]
- term: schon
  status: prohibited
  reason: mehrdeutig zwischen bereits, Betonung und Einschränkung
  rewrite: bereits nur verwenden, wenn der Zeitbezug relevant ist; sonst entfernen.
- term: schwach
  status: review_required
  reason: unspezifischer Grad oder Kraft
  rewrite: Messwert oder definierte Kategorie nennen.
- term: sehr
  status: review_required
  reason: unspezifische Verstärkung
  rewrite: Messwert oder definierte Kategorie nennen.
- term: setzen
  status: review_required
  reason: sehr viele Bedeutungen
  rewrite: einstellen, positionieren, aktivieren oder anderes präzises Verb verwenden.
- term: sichern
  status: prohibited
  reason: mehrdeutig zwischen befestigen, speichern, verriegeln und absichern
  rewrite: befestigen, speichern, verriegeln oder schützen entsprechend der Bedeutung verwenden.
- term: so
  status: review_required
  reason: kann Art und Weise, Grad, Folge oder anaphorischen Verweis ausdrücken
  rewrite: konkrete Art, Wert, Bedingung oder Folge nennen.
- term: so schnell wie möglich
  status: prohibited
  reason: Geschwindigkeit oder Frist ist nicht definiert
  rewrite: Konkrete Frist, Geschwindigkeit oder unverzügliche Handlung mit sofort angeben.
- term: sodass
  status: review_required
  reason: kausale/resultative Nebensatzkette kann Handlung und Folge verdichten
  rewrite: bei komplexen Sätzen Folge als neuen Satz mit deshalb formulieren.
  approved_alternatives:
  - deshalb
- term: sollte
  status: prohibited
  reason: Modalität zwischen Empfehlung und Anforderung ist unklar
  rewrite: Beabsichtigte Modalität als Imperativ, muss, darf, kann oder ausdrücklich als Empfehlung formulieren.
- term: sollten
  status: prohibited
  reason: Modalität zwischen Empfehlung und Anforderung ist unklar
  rewrite: Beabsichtigte Modalität ausdrücklich formulieren.
- term: sowie
  status: prohibited
  reason: stilistische und teilweise mehrdeutige Aufzählungsvariante zu und
  rewrite: und verwenden oder die Aufzählung in getrennte Punkte aufteilen.
  approved_alternatives:
  - und
- term: sowohl ... als auch
  status: prohibited
  reason: unnötig komplexe koordinierende Konstruktion
  rewrite: und verwenden oder zwei parallele Sätze schreiben.
  approved_alternatives:
  - und
- term: stark
  status: review_required
  reason: unspezifischer Grad oder Kraft
  rewrite: Messwert oder definierte Kategorie nennen.
- term: stattfinden
  status: review_required
  reason: nennt nur das Eintreten, nicht die technische Handlung
  rewrite: Konkrete Handlung oder Prozessverb nennen.
- term: stellen
  status: review_required
  reason: sehr viele räumliche und funktionale Bedeutungen
  rewrite: positionieren, einstellen oder präzises Verb verwenden.
- term: tun
  status: prohibited
  reason: zu allgemeines Verb für technische Handlungen
  rewrite: Präzises direktes Verb verwenden.
- term: typischerweise
  status: prohibited
  reason: Kriterium für typisch ist nicht definiert
  rewrite: Konkrete Bedingung, Verteilung oder Häufigkeit nennen.
- term: u. a.
  status: prohibited
  reason: macht unklar, welche weiteren Elemente gelten
  rewrite: Vollständige relevante Elemente nennen.
- term: usw.
  status: prohibited
  reason: offene Aufzählung lässt relevante Elemente ungenannt
  rewrite: Vollständige Liste geben.
- term: vernünftig
  status: prohibited
  reason: subjektive Bewertung
  rewrite: Technisches Kriterium nennen.
  surface_forms: [vernünftige, vernünftigen, vernünftiger, vernünftiges, vernünftigem]
- term: verschieden
  status: review_required
  reason: kann Unterschiede behaupten, ohne das unterscheidende Merkmal zu nennen
  rewrite: Unterschied oder konkrete Varianten nennen.
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - verschiedene
  - verschiedenen
  - verschiedener
  - verschiedenes
  - verschiedenem
- term: vgl.
  status: prohibited
  reason: Abkürzung in Fließtext und unklare Handlungsart
  rewrite: einen expliziten Dokumentverweis formulieren oder vergleichen als direktes Verb verwenden.
- term: vornehmen
  status: prohibited
  reason: Funktionsverb ohne konkrete Handlung
  rewrite: Direktes Verb verwenden.
- term: vorsichtig
  status: prohibited
  reason: Handlung oder Grenzwert bleibt unbestimmt
  rewrite: Konkrete Geschwindigkeit, Kraft, Abstand oder verbotene Handlung nennen.
  surface_forms: [vorsichtige, vorsichtigen, vorsichtiger, vorsichtiges, vorsichtigem]
- term: wahrscheinlich
  status: review_required
  reason: Wahrscheinlichkeit ist nicht quantifiziert oder begründet
  rewrite: Wenn relevant, definierte Wahrscheinlichkeit oder beobachtbare Bedingung nennen.
  surface_forms: [wahrscheinliche, wahrscheinlichen, wahrscheinlicher, wahrscheinliches, wahrscheinlichem]
- term: warten (Instandhaltung)
  status: prohibited
  reason: Homonym zu zeitlichem warten und dadurch lexikalisch mehrdeutig
  rewrite: Instand halten oder projektseitige technische Benennung verwenden.
  exceptions_or_contexts:
  - Zeitliches warten ist als eingeschränkter zentraler Eintrag zugelassen.
- term: wechseln
  status: prohibited
  reason: kann ersetzen, ändern oder zwischen Zuständen umschalten bedeuten
  rewrite: ersetzen, ändern oder auswählen entsprechend der Bedeutung verwenden.
- term: weiter
  status: prohibited
  reason: mehrdeutig zwischen räumlich weiter, zusätzlich und fortsetzen
  rewrite: Beabsichtigte Bedeutung explizit formulieren.
- term: wohl
  status: prohibited
  reason: unspezifische Wahrscheinlichkeit
  rewrite: Klare Möglichkeits- oder Wahrscheinlichkeitsaussage verwenden.
- term: würde
  status: prohibited
  reason: Konjunktiv II verschleiert Zeit, Bedingung oder Modalität
  rewrite: Präsens, klare wenn-Bedingung oder ausdrücklich notwendige Zukunft verwenden.
- term: würden
  status: prohibited
  reason: Konjunktiv II verschleiert Zeit, Bedingung oder Modalität
  rewrite: Präsens, klare wenn-Bedingung oder ausdrücklich notwendige Zukunft verwenden.
- term: z. B.
  status: review_required
  reason: Abkürzung und Beispielcharakter können Anforderungen verwischen
  rewrite: In normativen Anweisungen vollständige relevante Liste geben.
- term: zeitnah
  status: prohibited
  reason: Zeitgrenze ist nicht messbar
  rewrite: Frist oder Zeitpunkt nennen.
  surface_forms: [zeitnahe, zeitnahen, zeitnaher, zeitnahes, zeitnahem]
- term: ziemlich
  status: prohibited
  reason: unspezifischer Grad
  rewrite: Messwert oder definierte qualitative Kategorie nennen.
  surface_forms: [ziemliche, ziemlichen, ziemlicher, ziemliches, ziemlichem]
- term: zugehörig
  status: review_required
  reason: Bezug kann unklar sein, wenn mehrere Systeme oder Dokumentteile möglich sind
  rewrite: Zugehöriges System, Objekt oder Dokument ausdrücklich nennen.
  review_status: multi_industry_candidate_v0.1
  surface_forms:
  - zugehörige
  - zugehörigen
  - zugehöriger
  - zugehöriges
  - zugehörigem
- term: zur Anwendung kommen
  status: prohibited
  reason: Funktionsverbkonstruktion
  rewrite: anwenden oder verwenden verwenden.
  approved_alternatives:
  - anwenden
  - verwenden
- term: zuvor
  status: prohibited
  reason: stilistische Sequenzvariante; Bezugspunkt kann unklar sein
  rewrite: bevor + konkrete Handlung oder davor + eindeutigen Bezug verwenden.
  approved_alternatives:
  - bevor
- term: überprüfen
  status: prohibited
  reason: Synonymvariation zu prüfen ohne zusätzlichen Bedeutungsgewinn
  rewrite: prüfen verwenden.
  approved_alternatives:
  - prüfen
- term: üblicherweise
  status: prohibited
  reason: Ausnahmen bleiben ungenannt
  rewrite: Konkrete Bedingung oder definierte Häufigkeit nennen.

```
