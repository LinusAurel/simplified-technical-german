# STG-DE — Simplified Technical German

**STG-DE** is an open controlled-language specification for clear, consistent, and machine-readable German. It is designed for technical documentation, procedures, requirements, support content, product text, operational instructions, agent instructions, B2B communication, B2C communication, and other German text where ambiguity has a cost.

The project combines a **language standard**, a **controlled dictionary**, a **deterministic linter**, and a reusable **Agent Skill** in one repository.

> Current release: **0.4.0** — experimental. STG-DE is usable now, but the central dictionary and validator are still being expanded and validated.

## Why STG-DE

German technical writing has recurring ambiguity sources that cannot be solved by translating an English controlled language word-for-word: compound nouns, separable verbs, sentence brackets, case and gender, modal verbs, passive constructions, nominal style, pronominal adverbs, and inflection. STG-DE keeps the controlled-language model of writing rules plus controlled terminology and adapts it specifically to German.

## What is included

- **75 rules and recommendations** for German controlled writing.
- A traceable mapping of all **53 ASD-STE100 Issue 9 writing rules**.
- **435** central lexical entries with **442** controlled meanings.
- **160** prohibited or review-required words and phrases with rewrite guidance.
- German morphology and contraction handling.
- Project terminology support through `.stg-de.yaml`.
- A deterministic command-line linter.
- An Agent Skill with `WRITE`, `REWRITE`, and `AUDIT` workflows.
- Public corpus evidence from **18 sources across six industries**.

## Repository structure

```text
.
├── specification.md              # normative overview
├── rules/                        # normative writing rules
├── dictionary/                   # controlled lexicon and terminology model
├── mapping/                      # ASD-STE100 -> STG-DE traceability
├── schemas/                      # machine-readable schemas
├── examples/                     # conformance examples
├── corpus/                       # public validation metadata and metrics
├── tools/                        # linter, validators, build tools
└── skills/
    └── simplified-technical-german/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/
        └── scripts/
```

The top-level specification and dictionary are the source of truth. Skill reference files are generated copies so that the skill remains standalone when packaged.

## Agent Skill

The bundled skill accepts **arbitrary German text**. It is not limited to engineering or one industry.

It supports three workflows:

- **WRITE** — create new German text in STG-DE.
- **REWRITE** — rewrite existing German text while preserving meaning, modality, facts, numbers, constraints, and domain terms.
- **AUDIT** — report violations with STG-DE rule IDs and suggested corrections.

Default rewrite output contains only the rewritten text. Rule analysis is returned only when the user asks for an audit, diff, or explanation.

The skill runs the deterministic linter automatically when code execution is available. It still works without tools by applying the bundled rules and dictionary directly.

### Package the skill

```bash
python /path/to/skill-creator/scripts/package_skill.py skills/simplified-technical-german
```

For environments that support Agent Skills, install the `skills/simplified-technical-german/` directory or the packaged `skill.zip` according to that environment's instructions.

## CLI linter

Install the development dependency:

```bash
python -m pip install PyYAML
```

Audit a file:

```bash
python tools/stg_lint.py manual.md
```

Audit stdin and return JSON:

```bash
printf 'Prüfen Sie gegebenenfalls das Gerät.' | python tools/stg_lint.py - --format json
```

Use project terminology:

```bash
python tools/stg_lint.py manual.md --project .stg-de.yaml
```

The linter deliberately distinguishes deterministic violations from review candidates. An unknown word is **not automatically an error** and an uppercase German noun is **not automatically a technical term**.

## Project terminology

Do not put every product or industry term into the central dictionary. Add domain terminology in a project file:

```yaml
version: 1
technical_nouns:
  - term: "Drehmomentwandler"
    definition: "hydrodynamische Baugruppe zur Drehmomentübertragung"
technical_verbs:
  - term: "flashen"
    definition: "Firmware in einen Zielspeicher schreiben"
preferred_terms:
  - preferred: "Fehler"
    avoid: ["Problemfall"]
protected_terms: ["API", "DUT"]
```

This keeps the core language stable while allowing precise terminology in medicine, software, energy, automotive, consumer products, manufacturing, finance, support, and other domains.

## Conformance profiles

| Profile | Meaning |
|---|---|
| `STG-R` | Applicable writing rules are satisfied. |
| `STG-T` | `STG-R` plus project technical terminology is resolved. |
| `STG-C-core` | `STG-T` plus all remaining lexical items resolve to the shipped central core. |
| `STG-C` | Reserved for a broader, mature, human-reviewed central lexicon. |

## Public validation corpus

v0.4 uses 18 publicly accessible German technical sources, with three sources from each of six strata: Maschinenbau, Automotive, Elektrotechnik, Software/IT, Medizintechnik, and Anlagenbau. The repository contains only source metadata, hashes, and derived metrics.

On the 2,066-token stratified excerpt set, controlled central surface coverage reaches **58.1%**. This figure is not a quality target: product names, domain terms, identifiers, and intentionally disallowed wording should remain outside the general core. See [`corpus/validation-report.md`](corpus/validation-report.md).

## Development

```bash
python tools/validate_release.py
python -m unittest discover -s tests -v
python tools/sync_skill.py --check
```

## Status and roadmap

The development plan from v0.5 through v1.0 is tracked in [`ROADMAP.md`](ROADMAP.md).

The current priority is **v0.5 — Evidence and reliability**:

- strengthen validator/rule-ID consistency and regression coverage;
- publish automation coverage for all rule groups;
- expand the deterministic conformance test suite;
- separate development, validation, and holdout corpus data;
- grow the public/licensed corpus across substantially more domains;
- add evidence-based dictionary governance.

See [`quality/RULE-COVERAGE.md`](quality/RULE-COVERAGE.md) for current automation coverage and [`corpus/PROTOCOL.md`](corpus/PROTOCOL.md) for the v0.5 corpus methodology.

Contributions from technical writers, linguists, engineers, support teams, translators, terminology specialists, and agent developers are welcome.

## License

MIT. See [`LICENSE`](LICENSE).
