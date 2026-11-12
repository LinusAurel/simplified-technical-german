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
