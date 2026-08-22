# STG-DE Versioning Policy

STG-DE uses semantic versions for public releases: `MAJOR.MINOR.PATCH`.

The specification, dictionary, validator, and bundled Agent Skill ship as one repository release while they remain tightly coupled. Individual tools may later expose their own package versions, but every packaged artifact must declare the STG-DE specification version it targets.

## Before 1.0

The project is experimental. Minor releases can contain normative additions or restrictions, but every incompatible change must be called out in `CHANGELOG.md`.

- **PATCH**: editorial fixes, tests, tooling fixes, validator corrections that make behavior match already-published rules.
- **MINOR**: new rules, new application profiles, central dictionary additions, new validator capabilities, or documented normative refinements.
- **MAJOR**: reserved for 1.0 or a deliberate compatibility break after 1.0.

## After 1.0

### PATCH

No intended normative compatibility break. Examples:

- typo/documentation corrections;
- bug fixes where implementation contradicted the published rule;
- additional tests;
- performance improvements;
- new non-normative examples.

### MINOR

Backward-compatible capability additions. Examples:

- new optional application profile;
- new approved central word that does not alter existing meanings;
- additional validator warnings/review evidence;
- new tooling or integrations.

### MAJOR

A change that can make previously conforming text non-conforming or changes the controlled interpretation of existing text. Examples:

- restricting or prohibiting an existing approved meaning;
- changing a mandatory sentence threshold;
- changing the controlled meaning of an existing entry;
- changing profile semantics incompatibly;
- removing a supported public interface.

## Rule IDs

Rule IDs are more stable than file layout. Renaming or moving a rule section does not justify renumbering IDs.

A deprecated rule ID remains reserved.

## Dictionary compatibility

Every normative lexical change should be classified in its proposal as:

- `compatible_addition`;
- `clarification`;
- `restriction`;
- `meaning_change`;
- `deprecation`;
- `prohibition`.

Restrictions, meaning changes, deprecations, and prohibitions must appear prominently in the changelog.

## Validator severity

Promoting an existing finding from `review`/`warning` to deterministic `error` is a normative compatibility change unless the published rule already unambiguously required that behavior and the previous severity was an implementation bug.

## Agent Skill

Changes that only improve prompt routing or implementation quality are usually PATCH changes. A skill change that intentionally alters STG-DE output semantics follows the same compatibility rules as the underlying standard.
