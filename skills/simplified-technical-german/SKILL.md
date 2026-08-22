---
name: simplified-technical-german
description: "Write, rewrite, simplify, or audit German text with STG-DE (Simplified Technical German), a controlled-language system for reducing ambiguity and improving consistency for humans and AI agents. Use when a user asks for STG-DE, controlled German, simplified technical German, unambiguous German, machine-readable German prose, consistent terminology, a German technical-writing audit, or a rewrite that must preserve facts and constraints. Accept arbitrary German text across industries and B2B/B2C contexts, including procedures, requirements, support content, product text, documentation, messages, prompts, and agent instructions."
---

# Simplified Technical German

Apply STG-DE to German text. Prioritize unambiguous meaning, consistent terminology, short structures, and explicit relationships. Preserve the user's facts, modality, scope, numbers, warnings, product names, and technical meaning.

## Select the workflow

Determine the requested operation before changing text:

1. **WRITE** — create new German text in STG-DE.
2. **REWRITE** — transform supplied German text into STG-DE.
3. **AUDIT** — identify violations and suggest corrections without silently replacing the user's source.

If the user only says "apply STG-DE" to existing text, use REWRITE. If the user asks whether text complies, requests rule IDs, asks for a diff, or asks what is wrong, use AUDIT.

## Load references progressively

Read only the material needed for the current task:

- Read `references/rules.md` for all writing rules and examples.
- Read `references/dictionary-guide.md` for morphology, terminology, and lexicon behavior.
- Search `references/approved-words.yaml` when lexical approval or meaning matters.
- Search `references/prohibited-words.yaml` for prohibited/review-required terms and rewrite guidance.
- Read `references/project-terminology.md` when a project glossary exists or domain terms are unresolved.
- Read `references/validator-contract.md` when interpreting deterministic validator output or conformance profiles.

Do not load the complete dictionary when a focused lookup is sufficient.

## Use tools when available

When code execution is available, run `scripts/stg_lint.py` on the input before the final rewrite or audit. Pass a project terminology file when one is available.

Examples:

```bash
python scripts/stg_lint.py input.txt --format json
python scripts/stg_lint.py input.md --project .stg-de.yaml --format json
```

Treat deterministic `error` findings as violations. Treat `warning` and `review` findings as evidence that requires context. Never rewrite a sentence only because a heuristic says it is wrong.

If code execution is unavailable, continue without it. Apply the bundled rules and dictionary directly.

## Apply the core process

1. Read the complete input once for meaning.
2. Identify protected content: numbers, units, identifiers, quoted UI text, legal names, product names, code, URLs, and domain terminology.
3. Preserve modality. Do not convert possibility into certainty, permission into obligation, or recommendation into requirement.
4. Resolve terminology. Use the project term when a project dictionary specifies one. Otherwise preserve necessary domain terms and flag unresolved terms only in AUDIT mode.
5. Apply structural rules before lexical optimization.
6. Apply lexical rules with the controlled meaning and part of speech.
7. Re-read the result against the source. Verify that no fact, condition, exception, actor, limit, or relationship changed.
8. Check sentence length, instruction count, pronoun references, negation scope, passive voice, nominal style, compounds, separable verbs, and ambiguous linking words.
9. Run the linter again when tools are available. Fix deterministic findings that do not alter meaning.

## Writing priorities

Use these priorities in order:

1. **Technical correctness** — never change the intended fact or action.
2. **Safety and legal meaning** — never weaken warnings, conditions, permissions, prohibitions, or obligations.
3. **Unambiguous structure** — prefer explicit actors, objects, conditions, and references.
4. **Terminology consistency** — use one term for one concept within the applicable scope.
5. **Controlled vocabulary** — prefer approved central words where they express the correct meaning.
6. **Brevity** — shorten only after the first five priorities are satisfied.

## Arbitrary German text

Accept German text from any domain. Do not require that the text is an engineering manual. STG-DE can be used for support messages, consumer instructions, product copy, internal operations, software UI text, requirements, contracts, prompts, and other prose.

Do not remove necessary domain vocabulary to make a text look simpler. A controlled language controls ambiguity, not expertise.

For persuasive or brand-sensitive text, preserve the communication goal but make the language more explicit and consistent. If STG-DE materially removes a requested tone or rhetorical effect, preserve the intended message and mention the trade-off only when the user asks for analysis.

## German-specific checks

Pay special attention to:

- long or ambiguous compound nouns;
- separable verbs and separated verb particles;
- long sentence brackets;
- nested subordinate clauses;
- passive constructions with `werden`;
- nominalized actions where a direct verb is clearer;
- ambiguous pronouns and pronominal adverbs such as `dabei`, `dazu`, `daraus`, `davon`, and `darüber`;
- vague modal words such as `gegebenenfalls`, `möglichst`, `ordnungsgemäß`, or `zeitnah`;
- ambiguous scope of `nicht`, `nur`, `auch`, and similar particles;
- inconsistent synonyms for the same concept;
- words whose inflected form collides with a separate lemma or meaning.

Use the actual rule definitions in `references/rules.md` for normative decisions.

## Output

### WRITE and REWRITE

Return **only the finished STG-DE text by default**. Do not add a preamble, rule table, violation count, or closing explanation unless the user asks for one.

If strict compliance cannot be achieved without changing meaning, keep the necessary wording. Add one short `Hinweis:` line only when the unresolved issue is material to the requested output.

### AUDIT

Return a concise table:

```markdown
| Regel | Befund | Original | Vorschlag |
|---|---|---|---|
| STG-DE-5.2 | Mehrere unabhängige Anweisungen | ... | ... |
```

After the table, give:

```text
Ergebnis: PASS | PASS WITH REVIEW | FAIL
```

Use `PASS WITH REVIEW` when no deterministic violation remains but terminology, context, or a heuristic needs human review.

## Project terminology

If `.stg-de.yaml` or another project glossary is present, give it precedence for technical nouns, technical verbs, protected terms, and preferred terminology. Project terminology extends the central core; it does not override structural writing rules.

When no project dictionary exists:

- keep necessary domain nouns and verbs;
- use the same term consistently;
- do not invent a simpler synonym when it could change technical meaning;
- in AUDIT mode, mark unresolved domain terms as review items rather than automatic errors.

## Boundaries

- Do not invent facts to make text more explicit.
- Do not silently delete qualifications or exceptions to meet word limits.
- Do not claim full lexical conformance when unresolved words remain.
- Do not classify an unknown capitalized German noun as a technical term solely because it is capitalized.
- Do not treat a linter heuristic as stronger evidence than the actual sentence meaning.
- Do not require specialized vocabulary to be part of the central dictionary when a project term is appropriate.
