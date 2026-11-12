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
