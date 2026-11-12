# STG-DE — Simplified Technical German

**STG-DE** is an open controlled-language specification for clear, consistent, and machine-readable German. It is the German counterpart of [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org): every numbered STG-DE rule implements the intent of the ASD-STE100 Issue 9 rule with the same number, adapted to German grammar.

Use it for technical documentation, procedures, safety notes, requirements, support content, UI and error messages, and for text that AI agents read: prompts, tool descriptions, `AGENTS.md`, and inter-agent instructions.

The repository combines a **language standard**, a **controlled dictionary**, **deterministic tools**, and an **Agent Skill**.

> Current release: **0.5.0** — experimental standard, usable tools. Rule IDs are stable. The central dictionary and the heuristic analyzer are still being validated.

## Quick start

### Claude Code (plugin)

```bash
claude plugin marketplace add LinusAurel/simplified-technical-german
```

```bash
claude plugin install simplified-technical-german@stg-de
```

Inside a session, use `/plugin marketplace add LinusAurel/simplified-technical-german` and `/plugin install simplified-technical-german@stg-de`. Then ask, for example: *„Schreib diese Anleitung in STG-DE um.“*

### claude.ai, Claude Desktop, and other skill loaders

Download `simplified-technical-german-<version>.zip` from the [releases](https://github.com/LinusAurel/simplified-technical-german/releases) and upload it under *Settings → Capabilities → Skills*. You can also build it yourself:

```bash
python tools/package_skill.py
```

### Copy the skill folder

Copy `skills/simplified-technical-german/` into your agent's skills directory, for example `~/.claude/skills/` for Claude Code. The folder is self-contained: `SKILL.md`, references, and scripts. Tools that support the [`skills` CLI](https://skills.sh) can also run `npx skills add LinusAurel/simplified-technical-german` (this path is not covered by the repository's tests).

### Tools without skill support

Paste a snippet from [`prompts/agents-md.md`](prompts/agents-md.md) into `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or a system prompt. The short version has six rules. The full version covers procedures, descriptions, words, modality, punctuation, protected content, and error messages.

### GitHub Action

Check German Markdown in pull requests and get inline annotations:

```yaml
- uses: actions/checkout@v4
- uses: LinusAurel/simplified-technical-german@v0.5.0
  with:
    paths: docs
    profile: procedure   # optional
    fail-on: error       # error | warning | review | never
```

## What is included

- **75 rules and recommendations** for German controlled writing, in `rules/`.
- **Traceability to ASD-STE100 Issue 9:** all 53 writing rules and 8 general recommendations, in [`mapping/`](mapping/README.md).
- **435** central lexical entries with **442** controlled meanings, and **160** prohibited or review-required words with rewrite guidance.
- German morphology and contraction handling, and project terminology through `.stg-de.yaml`.
- Seven **application profiles**: `procedure`, `safety`, `description`, `requirement`, `support`, `consumer`, `agent`.
- **Tools:** deterministic linter, German review analyzer, and meaning-preservation check.
- **Agent Skill** with `WRITE`, `REWRITE`, and `AUDIT` workflows and the modes `strikt` and `pragmatisch`.
- **Evaluation suite** for the skill, with a deterministic scorer.
- Public corpus evidence: 139,646 tokens from 13 public full-text sources with fixed development, validation, and holdout partitions (metadata and derived metrics only).

## Agent Skill

The skill accepts arbitrary German text. It is not limited to engineering or one industry.

| Workflow | Result |
|---|---|
| `WRITE` | New German text in STG-DE. |
| `REWRITE` | Existing text in STG-DE. Facts, numbers, modality, conditions, and domain terms stay the same. Compliant text stays unchanged. |
| `AUDIT` | A table of findings with rule IDs and suggestions, and `Ergebnis: PASS`, `PASS WITH REVIEW`, or `FAIL`. |

| Mode | Use for | Conformance target |
|---|---|---|
| `strikt` | procedures, safety notes, requirements, error messages, tool descriptions, agent instructions | `STG-T` |
| `pragmatisch` | descriptions, support, consumer text, READMEs | `STG-R` |

WRITE and REWRITE return only the finished text. When code execution is available, the skill runs the linter, the analyzer, and the meaning-preservation check. Without tools, it applies the bundled rules and dictionary directly.

## Tools

Install the only dependency:

```bash
python -m pip install -r requirements-dev.txt
```

### Linter

Check files and directories (Markdown-aware: code blocks are ignored, list items and table cells are separate sentences):

```bash
python tools/stg_lint.py docs/ README.de.md --profile procedure
```

JSON output from stdin:

```bash
printf 'Prüfen Sie gegebenenfalls das Gerät.' | python tools/stg_lint.py - --format json
```

Fail a CI step on errors:

```bash
python tools/stg_lint.py docs/ --fail-on error
```

The linter loads `./.stg-de.yaml` automatically. It separates deterministic violations (`error`) from review candidates (`warning`, `review`). An unknown word is **not automatically an error**, and an uppercase German noun is **not automatically a technical term**.

### Meaning-preservation check

Compare a source text with its rewrite:

```bash
python tools/stg_compare.py original.md rewrite.md
```

Lost numbers, units, identifiers, code, URLs, quoted UI text, or safety signal words give `FAIL`. Changed modality, prohibitions, negations, conditions, or limits give `REVIEW`.

### German review analyzer

```bash
python tools/stg_analyze.py input.md
```

Reports passive, modality, clause-depth, pronoun, negation, nominal-style, and separable-verb candidates. All analyzer output is review evidence, never a violation by itself.

## Evaluation

```bash
python tools/run_evals.py --outputs evals/reference
```

```bash
python tools/run_evals.py --outputs runs/claude --command "claude -p"
```

The suite checks rule compliance, lost protected content, required facts, output discipline, and audit accuracy. See [`evals/README.md`](evals/README.md).

## Project terminology

Do not put every product or industry term into the central dictionary. Add precise domain terminology in `.stg-de.yaml` (see `.stg-de.example.yaml`). See [`dictionary/GOVERNANCE.md`](dictionary/GOVERNANCE.md) for central-core admission rules.

## Conformance profiles

| Profile | Meaning |
|---|---|
| `STG-R` | Applicable writing rules are satisfied. |
| `STG-T` | `STG-R` plus project technical terminology is resolved. |
| `STG-C-core` | `STG-T` plus all remaining lexical items resolve to the shipped central core. |
| `STG-C` | Reserved for a broader, mature, human-reviewed central lexicon. |

## Repository structure

```text
.
├── specification.md              # normative overview
├── rules/                        # normative writing rules
├── dictionary/                   # controlled lexicon and terminology model
├── mapping/                      # ASD-STE100 Issue 9 traceability
├── profiles/                     # application profiles
├── schemas/                      # machine-readable schemas
├── examples/                     # conformance and golden examples
├── evals/                        # Agent Skill evaluation suite
├── prompts/                      # snippets for AGENTS.md and system prompts
├── corpus/                       # public validation metadata and metrics
├── quality/                      # rule automation inventory
├── tools/                        # linter, analyzer, compare, build and release tools
├── .claude-plugin/               # Claude Code plugin and marketplace
├── action.yml                    # reusable GitHub Action
└── skills/simplified-technical-german/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/               # generated from the canonical files
    └── scripts/                  # copied from tools/
```

The top-level specification and dictionary are the source of truth. `python tools/sync_skill.py` regenerates the skill references and scripts.

## Development

```bash
python -m unittest discover -s tests -v
```

```bash
python tools/sync_skill.py --check
```

```bash
python tools/validate_release.py --skip-manifest
```

For a release, follow [`RELEASE-CHECKLIST.md`](RELEASE-CHECKLIST.md).

## Roadmap and governance

- [`ROADMAP.md`](ROADMAP.md) — development plan through 1.0.
- [`GOVERNANCE.md`](GOVERNANCE.md) — decision and review process.
- [`VERSIONING.md`](VERSIONING.md) — compatibility and semantic versioning.
- [`dictionary/GOVERNANCE.md`](dictionary/GOVERNANCE.md) — evidence-based core lexicon changes.
- [`quality/RULE-COVERAGE.md`](quality/RULE-COVERAGE.md) — automation status.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow.

Contributions from technical writers, linguists, engineers, support teams, translators, terminology specialists, and agent developers are welcome.

## License and notice

MIT. See [`LICENSE`](LICENSE).

ASD-STE100 is a copyright and trademark of ASD, Brussels. STG-DE is not an official ASD publication and contains no ASD-STE100 text. See [`NOTICE.md`](NOTICE.md).
