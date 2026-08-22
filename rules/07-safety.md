# Section 7 — Sicherheitsanweisungen

STG-DE controls the language of a safety instruction. The applicable safety standard controls the risk taxonomy, signal-word set, colors, symbols, and layout.

## STG-7.1 — Risikostufe eindeutig kennzeichnen

**Level:** `MUST`

Use the signal word or symbol required by the project's safety classification system. A document must use one consistent safety taxonomy.

Do not infer a lower risk category merely from legacy wording. If the correct category is unknown, return `NEEDS_SAFETY_INPUT`.

## STG-7.2 — Mit Schutzhandlung oder Bedingung beginnen

**Level:** `MUST`

After the signal word, state the preventive action or the necessary condition immediately. The reader must know what to do before reading secondary explanation.

**STG pattern**

> WARNUNG: Schalten Sie die Stromversorgung aus. ...

or

> WARNUNG: Wenn die Abdeckung offen ist, berühren Sie keine spannungsführenden Teile. ...

## STG-7.3 — Gefahr oder Folge nennen

**Level:** `MUST`

When the consequence is known, explain the hazard or possible result in concrete terms.

Avoid abstract formulations such as `Vorsicht ist geboten` or `besondere Sorgfalt ist erforderlich`.

**Nicht STG**

> WARNUNG: Arbeiten Sie vorsichtig.

**STG**

> WARNUNG: Schalten Sie die Stromversorgung aus. Eine elektrische Spannung kann schwere Verletzungen verursachen.

The technical safety content must come from an approved safety assessment; the language rule does not invent hazards.
