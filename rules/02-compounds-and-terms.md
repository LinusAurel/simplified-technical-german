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
