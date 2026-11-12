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
