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

- Präsens für aktuelle Zustände, Funktionen und allgemeine technische Fakten,
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
