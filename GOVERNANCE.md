# STG-DE Governance

STG-DE is an open controlled-language project. The specification is the authority; the validator and Agent Skill implement or assist with it but do not redefine it.

## Maintainer responsibilities

Maintainers are responsible for:

- preserving stable published rule IDs;
- reviewing normative language changes separately from implementation convenience;
- keeping central vocabulary cross-domain and evidence-based;
- requiring tests for machine-checkable behavior;
- protecting holdout evaluation from development leakage;
- documenting incompatible changes;
- keeping the standalone Agent Skill synchronized with canonical rules and dictionary data.

## Change classes

### Editorial

Spelling, formatting, examples, or explanation changes that do not change normative behavior.

### Lexical

Changes to approved words, controlled meanings, forms, prohibited/review terms, or preferred replacements. Follow `dictionary/GOVERNANCE.md`.

### Rule

Changes to a normative rule, recommendation, threshold, applicability condition, or conformance interpretation. Use `proposals/STG-CHANGE-TEMPLATE.md`.

### Implementation

Validator, tooling, packaging, or Agent Skill changes that do not change the standard itself. Implementation must reference existing rule IDs and document known limitations.

## Review expectations

A normative change should normally include:

1. the problem statement;
2. the proposed behavior;
3. compliant and non-compliant examples;
4. compatibility impact;
5. corpus or linguistic evidence where applicable;
6. validator/skill implications;
7. tests when the behavior is mechanically testable.

No numeric vote threshold is defined while the project has a small maintainer group. Maintainers should record the rationale for contested normative decisions in the proposal or pull request.

## Rule-ID stability

Published rule IDs are public identifiers. Do not renumber a rule for cosmetic organization.

If a rule is removed, reserve its ID and mark it deprecated. If a rule is split, preserve the original ID when possible and add new IDs only for genuinely new normative units.

## Compatibility

Compatibility and versioning rules are defined in `VERSIONING.md`.

## Releases

Use `RELEASE-CHECKLIST.md`. A release must pass the repository test suite, skill synchronization, structured-data validation, and release-manifest integrity check.

## Security and unsafe behavior

The project is a language specification and text-analysis tool. A contribution must not add hidden network access, credential collection, telemetry, or automatic execution of text being analyzed.

Corpus tooling may download explicitly declared public sources for transient analysis. It must not commit raw third-party corpora unless redistribution rights are explicit.

## External review

For 1.0, the project should obtain review from people with technical-writing and/or linguistic expertise and should document evidence of use outside the original development context. These criteria cannot be satisfied by automated CI alone.
