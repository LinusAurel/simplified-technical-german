# Changelog

## 0.5.0 — 2026-11-12

First release intended for production use of the tools and the Agent Skill. The rule set and dictionary are unchanged in meaning. All published rule IDs are stable.

### Source traceability

- Added `mapping/ste100-issue9.yaml`: all 53 ASD-STE100 Issue 9 writing rules and 8 general recommendations mapped to STG-DE (35 equivalent, 15 adapted, 3 replaced). Every STG-DE rule is traceable. Tests and `validate_release.py` enforce completeness.
- Added `NOTICE.md`. The repository contains no ASD-STE100 rule text, examples, or dictionary entries.

### Tools

- `stg_lint.py`: accepts several files and directories, adds line numbers, `--fail-on {error,warning,review,never}`, `--format github` for pull-request annotations, and loads `./.stg-de.yaml` automatically (`--no-project` disables this).
- `stg_lint.py` and `stg_analyze.py`: Markdown-aware segmentation (fenced code, HTML comments, headings, list items, table cells) in the shared `stg_markdown.py`. Before, a whole Markdown list could count as one sentence.
- `stg_lint.py`: quoted text is protected from lexical checks and counts as one word (`STG-8.6`).
- Fixed after a test on a real German monorepo: findings in sentences that wrap lines now carry line numbers; project technical terms override the central prohibited list; a changed quoted word (`„Provision“` → `„Provisionen“`) now fails the meaning check.
- Fixed: `man` was reported twice (`STG-DE-4.3` and `STG-1.1`). It is now reported once, by `STG-DE-4.3`.
- New `stg_compare.py`: meaning-preservation check for rewrites. Lost numbers, units, code, URLs, quoted text, identifiers, or safety signal words fail. Changed prohibitions, modality, negations, restrictions, conditions, and limits are review evidence.

### Agent Skill

- Added the modes `strikt` (`STG-T`) and `pragmatisch` (`STG-R`), with defaults by profile.
- Added guidance for text that agents read: tool descriptions, error messages, system prompts.
- The skill runs `stg_compare.py` after every rewrite and leaves compliant text unchanged.
- Rewrote the description with German and English triggers and explicit exclusions.
- Added `prompts/agents-md.md` with short and full snippets for `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, and system prompts.

### Packaging and CI

- Claude Code plugin and marketplace in `.claude-plugin/`.
- `tools/package_skill.py` builds a reproducible skill ZIP and SHA-256 checksum.
- Reusable GitHub Action `action.yml` for STG-DE checks in other repositories.
- Release workflow for `v*` tags. CI builds the ZIP and runs the action on this repository.

### Evaluation

- `evals/`: 12 WRITE, REWRITE, and AUDIT cases across all seven profiles, trigger prompts, and reference outputs.
- `tools/run_evals.py`: deterministic scorer. It can generate outputs with any CLI that reads a prompt on stdin.

### Since 0.4.0 (previously unreleased)

- Rule automation matrix (`quality/rule-coverage.yaml`) and golden audit fixtures.
- v0.5 corpus protocol with fixed development, validation, and holdout partitions; 139,646 tokens from 13 public full-text sources (derived metrics only).
- Lexical proposal schema and template, change-proposal template, governance, versioning policy, release checklist, and `CITATION.cff`.
- Application profiles (`procedure`, `safety`, `description`, `requirement`, `support`, `consumer`, `agent`) in linter and skill.
- Conservative German review analyzer `stg_analyze.py`.

## 0.4.0 — 2026-08-22

Public repository release.

- Added a stratified public validation set with 18 German technical sources across six industries.
- Increased the central lexicon to 435 entries and 442 controlled meanings.
- Added collision-safe handling for German inflection, including the `Datum` / `Daten` case.
- Replaced capitalization-based technical-term assumptions with neutral noun-candidate routing.
- Added public per-source, per-industry, and incremental coverage metrics.
- Added a reusable Agent Skill for writing, rewriting, and auditing German text with STG-DE.
- Added a deterministic linter and project terminology configuration.
- Added repository CI and release/skill validation.

## 0.3.0

- Expanded the controlled core vocabulary and morphology model.
- Added corpus-driven lexical review and validator improvements.
- Added explicit handling for ambiguous pronominal adverbs and German contractions.

## 0.2.0

- Expanded the controlled dictionary and prohibited/review-required term list.
- Added morphology guidance, schemas, validator contracts, and conformance tests.

## 0.1.0

- Initial German controlled-language specification.
- Added the first STG-DE rule index and German-specific rules.
- Added German-specific rules for compounds, separable verbs, sentence brackets, modality, nominal style, pronouns, and negation.
