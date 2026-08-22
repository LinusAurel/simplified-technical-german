# Section 4 — Sätze

## STG-4.1 — Kurze, eindeutige Sätze

**Level:** `MUST`

Write short sentences with one primary proposition. In descriptive text, each sentence should have one main topic. Do not compress several independent facts into one sentence.

**Nicht STG**

> Der Sensor sitzt am Gehäuse, misst den Druck und sendet die Werte an das Steuergerät, das bei einem Grenzwertfehler die Pumpe abschaltet.

**STG**

> Der Sensor sitzt am Gehäuse. Der Sensor misst den Druck. Das Steuergerät empfängt die Messwerte. Bei einem Grenzwertfehler schaltet das Steuergerät die Pumpe aus.

## STG-4.2 — Keine bedeutungstragenden Auslassungen

**Level:** `MUST_NOT`

Do not omit a subject, object, verb, article, or reference when the omission can create ambiguity. Do not use telegraphic fragments as normal running text.

**Nicht STG**

> Schalter auf EIN.

**STG**

> Stellen Sie den Schalter auf EIN.

Headings, table cells, labels, and other controlled fragments may be exempt under their content model.

## STG-4.3 — Vertikale Listen für komplexe Aufzählungen

**Level:** `MUST`

Use a vertical list when a sentence contains many parallel items, conditions, or actions.

Rules:

- introduce the list with a grammatically complete lead-in and colon,
- keep all list items grammatically parallel,
- do not mix procedural commands and descriptive statements in the same list,
- use a full stop for a list item that is a complete sentence,
- do not use commas or semicolons as end punctuation merely to chain list items.

## STG-4.4 — Logische Verknüpfungen explizit machen

**Level:** `MUST`

Use stable connecting words when the logical relation between sentences matters.

Preferred controlled connectors include:

- `und` — addition,
- `aber` — contrast,
- `dann` / `danach` — sequence,
- `deshalb` — result,
- `weil` — cause,
- `wenn` — condition,
- `bevor` — earlier event,
- `während` — simultaneous period.

Do not vary connectors merely for style.

## STG-4.5 — Artikel und Demonstrativa eindeutig verwenden

**Level:** `MUST`

Use articles and demonstratives according to German grammar and to make reference status clear. Ensure agreement in case, gender, and number.

Do not use a bare demonstrative pronoun when more than one antecedent is possible. Prefer a demonstrative adjective plus noun or repeat the technical noun.

**Ambiguous**

> Entfernen Sie den Sensor aus dem Halter. Dieser ist beschädigt.

**STG**

> Entfernen Sie den Sensor aus dem Halter. Der Sensor ist beschädigt.

or

> Entfernen Sie den Sensor aus dem Halter. Der Halter ist beschädigt.

## STG-DE-4.1 — Nebensatzverschachtelung begrenzen

**Level:** `MUST`

Do not nest subordinate clauses inside subordinate clauses in procedural or safety text. In descriptive text, one level of subordination is the default maximum.

Rewrite deeper structures as separate sentences.

## STG-DE-4.2 — Pronomen nur mit eindeutigem Bezug

**Level:** `MUST`

A pronoun must have exactly one plausible antecedent in the local context. If it can refer to more than one noun, repeat the noun.

**Ambiguous**

> Verbinden Sie den Sensor mit dem Adapter, wenn er trocken ist.

**STG**

> Wenn der Sensor trocken ist, verbinden Sie den Sensor mit dem Adapter.

## STG-DE-4.3 — `man` nicht als technischer Akteur verwenden

**Level:** `MUST_NOT`

Do not use the indefinite pronoun `man` to hide or generalize the actor in technical instructions or requirements.

Use:

- the imperative when the reader acts,
- a named role when a specified actor acts,
- the responsible system/component when it acts automatically.

## STG-DE-4.4 — Negationsbereich eindeutig machen

**Level:** `MUST`

Place `nicht`, `kein`, and other negative expressions so that only one interpretation is plausible. When the scope is complex, rewrite with an explicit condition.

**Ambiguous**

> Schalten Sie das Gerät nicht mit geöffnetem Gehäuse ein.

**STG**

> Wenn das Gehäuse offen ist, schalten Sie das Gerät nicht ein.

Avoid double negation.


## STG-DE-4.5 — Pronominaladverbien nur mit eindeutigem Bezug

**Level:** `MUST`

German pronominal adverbs such as `dabei`, `dazu`, `daraus`, `davon`, `darüber`, `dafür` and `hierfür` can compress a reference to an object, action, cause, purpose, or previous sentence. Use such a form only when exactly one local antecedent and exactly one semantic relation are possible.

In strict `STG-C-core` authoring, repeat the technical noun, action, or condition when the reference could be interpreted in more than one way.

**Mehrdeutig**

> Verbinden Sie den Sensor mit dem Adapter. Dabei darf die Dichtung nicht beschädigt werden.

`Dabei` can refer to connecting, to the adapter, or to the complete previous situation.

**STG**

> Wenn Sie den Sensor mit dem Adapter verbinden, beschädigen Sie die Dichtung nicht.

A validator should report an unresolved pronominal adverb as `NEEDS_REFERENCE_INPUT`; it must not invent the antecedent.
