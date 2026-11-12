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
