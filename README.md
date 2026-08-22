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
- Public corpus evidence from **18 sources across six industries** in v0.4, plus the reproducible v0.5 corpus work tracked in the roadmap.

## Repository structure

```text
.
├── specification.md              # normative overview
├── rules/                        # normative writing rules
├── dictionary/                   # controlled lexicon and terminology model
├── mapping/                      # source-rule traceability
├── schemas/                      # machine-readable schemas
├── examples/                     # conformance and golden examples
├── corpus/                       # public validation metadata and metrics
├── quality/                      # rule automation inventory
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

Default WRITE/REWRITE output contains only the finished text. Rule analysis is returned only for AUDIT or when explicitly requested.

When code execution is available, the skill runs the deterministic linter. It still works without tools by applying the bundled rules and dictionary directly.

## CLI linter

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
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

The linter distinguishes deterministic violations from review candidates. An unknown word is **not automatically an error** and an uppercase German noun is **not automatically a technical term**.

## Project terminology

Do not put every product or industry term into the central dictionary. Add precise domain terminology in `.stg-de.yaml`. See [`dictionary/GOVERNANCE.md`](dictionary/GOVERNANCE.md) for central-core admission rules.

## Conformance profiles

| Profile | Meaning |
|---|---|
| `STG-R` | Applicable writing rules are satisfied. |
| `STG-T` | `STG-R` plus project technical terminology is resolved. |
| `STG-C-core` | `STG-T` plus all remaining lexical items resolve to the shipped central core. |
| `STG-C` | Reserved for a broader, mature, human-reviewed central lexicon. |

## Public validation corpus

v0.4 uses 18 publicly accessible German technical sources, with three sources from each of six strata. The repository contains only source metadata, hashes, and derived metrics.

On the 2,066-token stratified excerpt set, controlled central surface coverage reaches **58.1%**. This is not a quality target: product names, domain terms, identifiers, and intentionally disallowed wording should remain outside the general core. See [`corpus/validation-report.md`](corpus/validation-report.md).

The v0.5 corpus work uses fixed development, validation, and holdout partitions and transient full-text extraction. See [`corpus/PROTOCOL.md`](corpus/PROTOCOL.md).

## Development

```bash
python -m unittest discover -s tests -v
python tools/sync_skill.py --check
python tools/validate_release.py --skip-manifest
```

For a release, rebuild the manifest and run the full integrity check as documented in [`RELEASE-CHECKLIST.md`](RELEASE-CHECKLIST.md).

## Roadmap and governance

- [`ROADMAP.md`](ROADMAP.md) — development plan through 1.0.
- [`GOVERNANCE.md`](GOVERNANCE.md) — decision and review process.
- [`VERSIONING.md`](VERSIONING.md) — compatibility and semantic versioning.
- [`dictionary/GOVERNANCE.md`](dictionary/GOVERNANCE.md) — evidence-based core lexicon changes.
- [`quality/RULE-COVERAGE.md`](quality/RULE-COVERAGE.md) and [`quality/rule-coverage.yaml`](quality/rule-coverage.yaml) — automation status.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow.

Contributions from technical writers, linguists, engineers, support teams, translators, terminology specialists, and agent developers are welcome.

## License

MIT. See [`LICENSE`](LICENSE).
