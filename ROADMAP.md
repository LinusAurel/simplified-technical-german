# STG-DE Roadmap

This roadmap describes the path from the current experimental release (0.2.0) to a stable STG-DE 1.0. Priorities can change when corpus evidence, user feedback, or implementation findings show that a different order is more useful.

## Guiding principles

1. Keep the language standard independent from the Agent Skill and implementation tools.
2. Keep rule IDs stable once they are published unless a correction is unavoidable.
3. Separate deterministic violations from heuristic or semantic review findings.
4. Add central vocabulary only when evidence supports cross-domain use.
5. Keep domain terminology in project dictionaries instead of expanding the core without need.
6. Preserve meaning, modality, safety conditions, numbers, and scope during rewrites.
7. Validate changes with both machine tests and real German text.

## Source traceability (0.2.0)

- [x] Map all 53 ASD-STE100 Issue 9 writing rules and 8 general recommendations to STG-DE (`mapping/ste100-issue9.yaml`).
- [x] Enforce that every STG-DE rule is traceable and every mapping target exists.
- [x] Document the ASD-STE100 copyright boundary (`NOTICE.md`).

## v0.2 — Evidence and reliability

### Rule and validator quality

- [x] Build a rule-to-test matrix for all published STG-DE rules.
- [x] Add at least one positive and one negative case for each deterministically testable rule.
- [x] Verify that every validator finding references an existing rule ID.
- [x] Add regression tests for rule-ID stability.
- [x] Add golden audit fixtures with expected finding IDs, severities, and output status.
- [x] Document which rules are deterministic, heuristic, semantic, or human-review-only.
- [x] Expand tests from the minimal set to a meaningful conformance suite.
- [x] Make the linter and analyzer Markdown-aware (fenced code, headings, lists, tables).
- [x] Protect quoted text from lexical checks (STG-8.6).

### Corpus methodology

- [x] Define development, validation, and holdout corpus splits.
- [x] Expand from short evidence samples to a larger public German corpus (139,646 tokens, 13 full-text sources).
- [x] Reach at least 100,000 tokens for the first larger evaluation.
- [ ] Reach 500,000+ tokens with a token-balanced partition design.
- [x] Expand beyond technical manuals into public-sector, software, energy, logistics, and telecom text.
- [x] Store exact document URLs, hashes, and sampling methods.
- [x] Track per-domain coverage and unknown-token distributions.
- [ ] Measure false positives and false negatives on a manually reviewed holdout set.
- [x] Keep third-party source text out of the repository.

### Dictionary governance foundation

- [x] Define evidence requirements for adding a core lexical entry.
- [x] Add a machine-readable lexical proposal format.
- [x] Record alternatives considered, ambiguity risk, corpus evidence, and decision rationale.
- [x] Distinguish core vocabulary from project/domain terminology in contribution guidance.

### v0.2 exit criteria

- [x] Deterministic rule IDs are internally consistent and regression-tested.
- [x] The rule coverage matrix is published.
- [x] A larger, reproducible corpus methodology exists.
- [x] Holdout evaluation is separated from dictionary development.
- [x] Known validator limitations are explicitly classified.

## v0.3 — German language engine

**Goal:** improve analysis of German morphology and syntax without turning uncertain NLP output into false certainty.

- [ ] Add robust German lemmatization.
- [ ] Improve inflection handling and collision detection beyond the curated collision list.
- [ ] Add compound-noun analysis and terminology routing.
- [ ] Add POS tagging where it improves controlled-meaning checks.
- [x] Detect subordinate-clause depth and long sentence brackets (heuristic, `stg_analyze.py`).
- [x] Detect passive-voice candidates, including `werden` constructions (heuristic).
- [x] Detect likely nominal style (heuristic).
- [x] Add heuristic pronoun and pronominal-adverb reference checks.
- [x] Add modality and negation-scope review checks.
- [x] Introduce explicit confidence levels for NLP-derived findings.
- [ ] Measure analyzer precision on the holdout set before any promotion to deterministic checks.

## v0.4 — Application profiles

- [x] Formal profile schema.
- [x] Rule-applicability matrix by profile.
- [x] Profile-aware CLI and Agent Skill behavior.
- [x] Conformance examples for each profile (`evals/cases.yaml` covers all seven).
- [x] Strict and pragmatic skill modes mapped to `STG-T` and `STG-R`.

## v0.5 — Tool ecosystem

- [x] `stg_lint.py` for files and directories, with line numbers and `--fail-on`.
- [x] Reusable GitHub Action with pull-request annotations (`action.yml`).
- [x] Meaning-preservation check for rewrites (`stg_compare.py`).
- [x] Claude Code plugin and marketplace (`.claude-plugin/`).
- [x] Reproducible skill ZIP with checksum for claude.ai and other skill loaders.
- [x] Copy-paste snippets for `AGENTS.md`, `CLAUDE.md`, and system prompts (`prompts/agents-md.md`).
- [ ] Python package with an `stg` CLI (`pip install`).
- [ ] pre-commit hook (needs the Python package).
- [ ] Vale rules where deterministic mapping is appropriate.
- [ ] Language Server Protocol adapter and VS Code diagnostics.
- [ ] Optional MCP server for editor and agent integrations.

Tooling must consume the repository's canonical rule and dictionary data rather than maintain independent copies.

## Agent Skill track

### Evaluation suite

- [x] Create WRITE, REWRITE, and AUDIT evaluation sets with a deterministic scorer (`evals/`, `tools/run_evals.py`).
- [x] Cover procedures, requirements, support, consumer text, safety text, error messages, and agent instructions.
- [x] Measure rule compliance, lost protected content, invented numbers, modality changes, and audit accuracy.
- [ ] Run the suite against multiple models, with and without the skill, and publish the results.
- [ ] Add trigger-accuracy measurements for `evals/triggers.yaml`.
- [ ] Add regression cases for failures found in real use.

### Skill behavior

- [x] Keep default WRITE/REWRITE output limited to the finished text.
- [x] Keep detailed rule output in AUDIT or when explicitly requested.
- [x] Use deterministic validator results when tool execution is available.
- [x] Never treat heuristic findings as stronger evidence than sentence meaning.
- [x] Support project terminology consistently across agent environments.

## v0.6 — Governance and release discipline

- [x] Add STG Change Proposal template.
- [x] Add lexical proposal template.
- [x] Define rule-change and deprecation policy.
- [x] Define semantic versioning policy for specification, dictionary, validator, and skill changes.
- [x] Define maintainer and review expectations.
- [x] Add `CITATION.cff`.
- [x] Publish checksum-verifiable release artifacts (release workflow).
- [x] Create a documented release checklist.

## v1.0 — Stable controlled language

STG-DE 1.0 is reached by evidence and stability, not by a target dictionary size.

- [ ] Rule set stable across multiple releases.
- [ ] Published rule IDs treated as stable public identifiers.
- [ ] Large independent holdout corpus evaluated.
- [ ] Acceptable false-positive rate documented for deterministic and NLP checks.
- [ ] Broad coverage of general German function and action language.
- [ ] Domain terminology cleanly separated from the core.
- [ ] Deterministically testable rules have comprehensive automated coverage.
- [ ] Agent Skill evaluated across multiple models and text domains.
- [ ] Human review from technical-writing and/or linguistic specialists.
- [ ] Evidence of real use outside the original project.
- [ ] Governance and change process documented and active.

## Near-term execution order

1. Run `tools/run_evals.py` against at least two models, with and without the skill, and publish the results.
2. Manually review a holdout sample and publish linter and analyzer precision.
3. Package the tools as a Python package with an `stg` CLI and a pre-commit hook.
4. Expand the corpus toward 500,000 tokens with balanced partitions.
5. Add lemmatization and compound analysis behind the review-only boundary.
