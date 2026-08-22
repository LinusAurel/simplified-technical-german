# Section 8 — Zeichensetzung und Wortzählung

## STG-8.1 — Standardsatzzeichen; kein Semikolon zum Verbinden von Aussagen

**Level:** `MUST_NOT`

Use standard German punctuation. Do not use the semicolon (`;`) to connect independent technical propositions. Write separate sentences instead.

This restriction is intentionally stronger than ordinary German punctuation rules because it limits sentence complexity.

## STG-8.2 — Bindestriche nur für echte Wortstruktur

**Level:** `MUST`

Use hyphens according to German orthography and approved terminology. Use them when they clarify compound boundaries, connect letters/numbers with words where required, or are part of an official term.

Do not use hyphens to hide syntactic complexity or to force a long phrase into one counted word.

## STG-8.3 — Klammern restriktiv verwenden

**Level:** `MUST`

Parentheses may be used for:

- figure/text references,
- identifiers,
- work-step identifiers,
- abbreviations after the full form,
- short clarifications,
- controlled alternatives where the project format explicitly permits them.

Do not put a required instruction, safety action, or primary technical condition only in parentheses.

## STG-8.4 — Doppelpunkt beendet die Einleitung einer vertikalen Liste

**Level:** `MUST`

For word counting, the text before a colon that introduces a vertical list is counted as one sentence. Each list item is checked separately.

Limits:

- 20 words for procedural items,
- 25 words for descriptive items.

## STG-8.5 — Klammertext separat prüfen

**Level:** `MUST`

Parenthetical text counts as one word in the outer sentence. The text inside parentheses is also checked separately for clarity and applicable sentence length.

This counting rule does not permit complex instructions inside parentheses.

## STG-8.6 — Geschützte Einheiten zählen als ein Wort

**Level:** `MUST`

For sentence-length counting, each of these counts as one word in the surrounding sentence:

- a number,
- a number directly combined with its unit,
- an abbreviation,
- an alphanumeric identifier,
- quoted/locked text,
- an official title/heading/label,
- a protected proper name.

Do not count numbering that only identifies a work step.

## STG-8.7 — Bindestrichkomposita zählen orthografisch als ein Wort

**Level:** `MUST`

A hyphenated German compound counts as one orthographic word for sentence length. The compound is still subject to Section 2 complexity rules.

## STG-DE-8.1 — Schrägstrichkombinationen vermeiden

**Level:** `SHOULD_NOT`

Avoid forms such as `und/oder`, `der/die`, `ein-/ausschalten`, and compressed slash alternatives in running technical text when they can have more than one interpretation.

Use an explicit `und`, `oder`, a vertical list, or separate sentences.

Exceptions are locked identifiers and project-defined compact table notation.
