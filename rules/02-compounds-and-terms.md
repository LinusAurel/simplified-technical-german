# Section 2 — Komposita und Mehrwortterme

German technical language relies heavily on compounds. STG-DE therefore defines dedicated rules for their controlled use.

## STG-2.1 — Begrenze die semantische Dichte technischer Benennungen

**Level:** `MUST`

A newly created technical designation must be understandable without having to infer several possible internal relations between components.

Use these methods in order:

1. Use the approved official term if one exists, regardless of length.
2. For a new term, prefer at most three meaningful lexical components.
3. If a longer designation is necessary, use a grammatically clear phrase or a structured compound.
4. Use a hyphen when it materially clarifies the boundaries of a long compound or when the official orthography requires or permits it for clarity.
5. Do not create a chain of modifiers only to keep the expression to one orthographic word.

**Nicht STG**

> Kraftstoffhauptpumpenausgangsdruckprüfanschlussabdeckung

**STG**

> Abdeckung des Prüfanschlusses am Ausgang der Hauptkraftstoffpumpe

If the long compound is the official part name, keep the official name and define a controlled shorter form under STG-2.2.

## STG-2.2 — Lange offizielle Benennung zuerst vollständig

**Level:** `MUST`

When an official technical designation is long:

1. write the full official designation at first occurrence,
2. define an approved short form or abbreviation if useful,
3. use only that short form afterwards within the declared scope.

Do not introduce several short forms for the same term.

**Example**

> Die **zentrale Steuerung der Kühlmittelpumpe (Kühlmittelsteuerung)** überwacht den Druck. Die **Kühlmittelsteuerung** schaltet die Pumpe bei Überdruck aus.

## STG-DE-2.1 — Deutsche Komposita als Terminologieobjekte

**Level:** `MUST`

Treat a German compound as a terminology object, not merely as a concatenation of approved general words.

For each approved compound, a terminology database should store:

- canonical spelling,
- concept identifier,
- grammatical gender,
- plural form,
- approved short form if any,
- decomposition into meaningful components when useful for validators.

Approval of `Druck`, `Regler`, and `Ventil` does not automatically approve `Druckregelventil` as a technical term.

## STG-DE-2.2 — Bindestriche nicht als Komplexitäts-Trick verwenden

**Level:** `MUST_NOT`

Do not use hyphens solely to make a complex designation appear shorter for the word-count rule. A hyphenated compound counts as one orthographic word, but it still receives a compound-complexity check.

## STG-DE-2.3 — Abkürzungen sparsam und stabil verwenden

**Level:** `MUST`

Use an abbreviation only when it is official or explicitly introduced. At first occurrence, write the full term followed by the abbreviation in parentheses unless the abbreviation is universally required by the project.

After introduction, do not alternate between multiple abbreviations or between several shortened forms.
