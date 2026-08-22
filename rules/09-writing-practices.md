# Section 9 — Schreibpraxis

## STG-9.1 — Satz neu bauen, wenn Wortersatz nicht reicht

**Level:** `MUST`

Do not replace an unapproved word mechanically when the replacement changes grammar, meaning, or modality. Rewrite the complete sentence while preserving technical meaning.

A language tool must prefer `NEEDS_DOMAIN_INPUT` to an invented rewrite when the intended meaning is unclear.

## STG-9.2 — Freigegebene Wörter korrekt verwenden

**Level:** `MUST`

Before using an approved word, check its approved meaning, word class, restrictions, and domain profile.

If a word has several approved meanings, the lexicon must distinguish them with separate meaning IDs.

## STG-9.3 — Keine idiomatischen Verbgefüge als Ersatz für direkte Verben

**Level:** `MUST_NOT`

In German, ambiguity and verbosity often come from idioms and function-verb constructions.

Do not use an idiomatic or noun-heavy verb phrase when a direct approved verb gives the same technical meaning.

**Nicht STG**

> Nehmen Sie eine Prüfung vor.

**STG**

> Prüfen Sie das Bauteil.

**Nicht STG**

> Bringen Sie die Änderung zur Anwendung.

**STG**

> Wenden Sie die Änderung an.

Lexicalized technical multiword verbs may be approved as single dictionary entries when the domain requires them.

## STG-9.4 — Terminologie und Formulierungen konsistent halten

**Level:** `MUST`

For the same action in the same context, use the same approved wording. Do not alternate sentence patterns for stylistic variety.

Templates are encouraged for recurrent work steps.

---

# General recommendations

These recommendations are not mandatory by default. A project may promote any of them to mandatory status.

## STG-GR-1 — Nebensatzmarker explizit und korrekt


Use explicit conjunctions such as `dass`, `wenn`, `weil`, and `bevor` when they make clause relations clear. Avoid compressed headline-style omission in running text.

## STG-GR-2 — `mit` auf Mehrdeutigkeit prüfen


The preposition `mit` can express instrument, accompaniment, association, or condition. If more than one reading is plausible, rewrite the sentence.

**Ambiguous**

> Montieren Sie die Abdeckung mit den roten Schrauben.

Possible intended meanings include:

- the cover already has red screws,
- install the cover together with the red screws,
- use the red screws as fasteners.

State the intended relation explicitly.

## STG-GR-3 — Pronomen sparsam verwenden


Use a pronoun only when its antecedent is unmistakable. Repetition of a technical noun is preferable to ambiguous reference.

## STG-GR-4 — Demonstrativa mit Nomen verwenden


Prefer `diese Leitung`, `dieser Wert`, `diese Methode` to a bare `dies` or `diese`, especially after several possible antecedents.

## STG-GR-5 — Lehnübersetzungen und falsche Freunde prüfen


Writers and translation systems must not transfer meanings from English merely because a German word looks similar. Examples requiring context checks include `realisieren`, `kontrollieren`, `eventuell`, and `aktuell` when translating to/from English.

The rule does not prescribe a replacement without context.

## STG-GR-6 — Abkürzungen in Fließtext reduzieren


Prefer full German expressions to general prose abbreviations such as `z. B.`, `d. h.`, `ggf.`, `bzw.`, and `usw.` when the abbreviation could reduce clarity.

`ggf.` and `bzw.` are prohibited by the seed vocabulary policy because they often hide a condition or relation.

## STG-GR-7 — Neutrale Personenbezeichnungen bevorzugen


Use role or function terms that are neutral and technically precise where possible, for example `Personal`, `Fachkraft`, `Bedienperson`, `Prüfperson`, or a project-defined role name.

Avoid gender-specific pronouns when they are unnecessary. Special orthographic gender markers are governed by the applicable language/style directive; STG-DE itself does not require them.

## STG-GR-8 — Genitivketten vermeiden


A simple German genitive is permitted. Avoid long chains of possessive/genitive relations that force the reader to resolve several nested dependencies.

**Schwer lesbar**

> die Prüfung der Dichtung des Ausgangs des Reglers

**Besser**

> die Prüfung der Dichtung am Reglerausgang

## STG-DE-9.1 — Modalpartikeln und rhetorische Füllwörter vermeiden

**Level:** `MUST_NOT`

Do not use modal particles or conversational fillers such as `mal`, `doch`, `eben`, `halt`, `wohl`, `eigentlich`, `einfach` when they do not have a precise technical meaning.

## STG-DE-9.2 — Vage Qualitäts- und Zeitangaben ersetzen

**Level:** `MUST`

Replace vague expressions with observable criteria whenever the criterion matters to the task.

Examples of terms that normally require rewriting:

- `möglichst schnell`,
- `zeitnah`,
- `ordnungsgemäß`,
- `fachgerecht`,
- `ausreichend`,
- `bei Bedarf`,
- `gegebenenfalls`.

**Nicht STG**

> Ziehen Sie die Schraube ausreichend fest.

**STG**

> Ziehen Sie die Schraube mit 8 Nm fest.

If no measurable criterion is available, request domain input instead of inventing one.
