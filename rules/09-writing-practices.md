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
