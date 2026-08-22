# STG-DE Roadmap

This roadmap describes the path from the current experimental v0.4 release to a stable STG-DE 1.0. Priorities can change when corpus evidence, user feedback, or implementation findings show that a different order is more useful.

## Guiding principles

1. Keep the language standard independent from the Agent Skill and implementation tools.
2. Keep rule IDs stable once they are published unless a correction is unavoidable.
3. Separate deterministic violations from heuristic or semantic review findings.
4. Add central vocabulary only when evidence supports cross-domain use.
5. Keep domain terminology in project dictionaries instead of expanding the core without need.
6. Preserve meaning, modality, safety conditions, numbers, and scope during rewrites.
7. Validate changes with both machine tests and real German text.

## v0.5 — Evidence and reliability

**Goal:** make the current specification and validator measurably reliable before expanding the tool ecosystem.

### Rule and validator quality

- [ ] Build a rule-to-test matrix for all published STG-DE rules.
- [ ] Add at least one positive and one negative case for each deterministically testable rule.
- [ ] Verify that every validator finding references an existing rule ID.
- [ ] Add regression tests for rule-ID stability.
- [ ] Add golden audit fixtures with expected finding IDs, severities, and output status.
- [ ] Document which rules are deterministic, heuristic, semantic, or human-review-only.
- [ ] Expand tests from the current minimal set to a meaningful conformance suite.

### Corpus methodology

- [ ] Define development, validation, and holdout corpus splits.
- [ ] Expand from short evidence samples to a substantially larger public or licensed German corpus.
- [ ] Target at least 100,000 tokens for the first larger evaluation; prefer 500,000+ when suitable sources are available.
- [ ] Expand beyond technical manuals into B2B and B2C text such as support, product communication, public-sector instructions, SaaS documentation, finance, energy, logistics, and telecom.
- [ ] Store exact document URLs, document identifiers, versions, dates, and sampling methods where possible.
- [ ] Track per-domain coverage and unknown-token distributions.
- [ ] Measure false positives and false negatives on a manually reviewed holdout set.
- [ ] Keep third-party source text out of the repository unless redistribution rights are explicit.

### Dictionary governance foundation

- [ ] Define evidence requirements for adding a core lexical entry.
- [ ] Add a machine-readable lexical proposal format.
- [ ] Record alternatives considered, ambiguity risk, corpus evidence, and decision rationale.
- [ ] Distinguish core vocabulary from project/domain terminology in contribution guidance.

### v0.5 exit criteria

- Deterministic rule IDs are internally consistent and regression-tested.
- The rule coverage matrix is published.
- A larger, reproducible corpus methodology exists.
- Holdout evaluation is separated from dictionary development.
- Known validator limitations are explicitly classified.

## v0.6 — German language engine

**Goal:** improve analysis of German morphology and syntax without turning uncertain NLP output into false certainty.

- [ ] Add robust German lemmatization.
- [ ] Improve inflection handling and collision detection.
- [ ] Add compound-noun analysis and terminology routing.
- [ ] Add POS tagging where it improves controlled-meaning checks.
- [ ] Detect subordinate-clause depth and long sentence brackets.
- [ ] Improve passive-voice detection, including `werden` constructions.
- [ ] Detect likely nominal style and function-verb constructions.
- [ ] Add heuristic pronoun and pronominal-adverb reference checks.
- [ ] Add modality and negation-scope review checks.
- [ ] Introduce explicit confidence/severity rules for NLP-derived findings.

Preferred architecture:

```text
STG-DE validator
├── deterministic checks  -> error/pass where mechanically provable
├── NLP checks            -> warning/review with evidence
└── semantic checks       -> review only unless a rule can be proven
```

## v0.7 — Application profiles

**Goal:** apply one standard across different communication contexts without creating incompatible dialects of STG-DE.

Planned profiles:

- `procedure`
- `safety`
- `description`
- `requirement`
- `support`
- `consumer`
- `agent`

Profiles can change rule applicability, thresholds, or severity. They must not change the controlled meaning of core vocabulary.

Deliverables:

- [ ] Formal profile schema.
- [ ] Rule-applicability matrix by profile.
- [ ] Profile-aware CLI and Agent Skill behavior.
- [ ] Conformance examples for each profile.

## v0.8 — Tool ecosystem

**Goal:** make STG-DE easy to use where people and agents already write.

Potential deliverables:

- [ ] Python package and `stg` CLI.
- [ ] `stg lint` for files and directories.
- [ ] pre-commit integration.
- [ ] reusable GitHub Action.
- [ ] Vale rules where deterministic mapping is appropriate.
- [ ] Language Server Protocol implementation or adapter.
- [ ] VS Code diagnostics/extension.
- [ ] optional MCP server for editor and agent integrations.

Tooling must consume the repository's canonical rule and dictionary data rather than maintain independent copies.

## Agent Skill track

The Agent Skill evolves in parallel with the standard but does not define the standard.

### Evaluation suite

- [ ] Create WRITE, REWRITE, and AUDIT evaluation sets.
- [ ] Cover procedures, requirements, support, consumer text, UI text, B2B communication, safety text, and agent instructions.
- [ ] Evaluate multiple capable models where practical.
- [ ] Measure meaning preservation, rule compliance, missed violations, false positives, invented information, and modality changes.
- [ ] Add regression cases for failures found in real use.

### Skill behavior

- [ ] Keep default WRITE/REWRITE output limited to the finished text.
- [ ] Keep detailed rule output in AUDIT or when explicitly requested.
- [ ] Use deterministic validator results when tool execution is available.
- [ ] Never treat heuristic findings as stronger evidence than sentence meaning.
- [ ] Support project terminology consistently across agent environments.

## v0.9 — Governance and release discipline

**Goal:** make external contribution and long-term maintenance predictable.

- [ ] Add STG Change Proposal template.
- [ ] Add lexical proposal template.
- [ ] Define rule-change and deprecation policy.
- [ ] Define semantic versioning policy for specification, dictionary, validator, and skill changes.
- [ ] Define maintainer and review expectations.
- [ ] Add `CITATION.cff`.
- [ ] Publish signed or checksum-verifiable release artifacts.
- [ ] Create a documented release checklist.

## v1.0 — Stable controlled language

STG-DE 1.0 is reached by evidence and stability, not by a target dictionary size.

Expected release criteria:

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

1. Fix validator/rule-ID inconsistencies and add regression tests.
2. Publish the rule coverage/classification matrix.
3. Expand the deterministic conformance test suite.
4. Define the v0.5 corpus protocol and holdout methodology.
5. Add exact/reproducible source metadata where available.
6. Expand the public corpus and manually review a holdout sample.
7. Add lexical-change governance and proposal schemas.
8. Re-evaluate the Agent Skill against the strengthened validator and test set.
