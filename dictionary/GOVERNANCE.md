# STG-DE Core Lexicon Governance

The central STG-DE dictionary is a cross-domain controlled vocabulary. It is not a collection of all words that occur frequently in German documentation.

This document defines how entries are proposed, reviewed, accepted, restricted, deprecated, or rejected.

## Scope

The central core should contain words that are broadly useful for controlled German across multiple domains or that provide necessary grammatical/technical functions.

Narrow product, company, industry, legal, medical, software, or engineering terminology normally belongs in project terminology (`.stg-de.yaml`) rather than the central core.

## Decision principles

A proposal is evaluated in this order:

1. **Meaning necessity** — Does STG-DE need this concept in the central language?
2. **Cross-domain utility** — Is the concept useful beyond one narrow domain?
3. **Ambiguity risk** — Can the lemma be restricted to a clear controlled meaning and part of speech?
4. **Replacement quality** — Is an existing approved word already sufficient?
5. **Corpus evidence** — Does independent evidence show recurring real use or need?
6. **Consistency** — Does the entry fit existing lexical decisions and terminology patterns?
7. **Teachability** — Can a writer and an agent apply the decision without hidden context?

Frequency alone is not sufficient for admission.

## Evidence classes

Evidence can be supplied from these sources:

- `development_corpus`: observations from the development partition;
- `validation_corpus`: observations from the validation partition;
- `external_public`: independently cited public examples;
- `linguistic_rationale`: a grammatical or semantic need that does not depend on frequency;
- `user_report`: a real writing/validation case submitted by a user.

The holdout corpus must not be used to select new core vocabulary for the release that is evaluated against that holdout.

## Proposal types

A lexical proposal has one of these actions:

- `add` — add a new central entry;
- `restrict` — narrow a controlled meaning, part of speech, or form;
- `expand` — add a controlled meaning or permitted form;
- `deprecate` — keep temporarily but mark for replacement;
- `prohibit` — move a term or meaning to prohibited/review status;
- `replace` — designate a preferred central alternative;
- `clarify` — change documentation without changing normative behavior.

## Required proposal fields

Use `dictionary/proposals/TEMPLATE.yaml` and validate against `schemas/lexicon-proposal.schema.json`.

Every normative proposal must identify:

- proposal ID and action;
- lemma/term and part of speech;
- proposed controlled meaning;
- rationale;
- ambiguity risk;
- alternatives considered;
- evidence across domains/sources when applicable;
- impact on existing dictionary entries;
- examples;
- validator impact;
- final decision and rationale after review.

## Admission guidance

A new general content word should normally have evidence from at least two materially different domains or a strong general-language/grammatical rationale.

This is guidance, not an automatic vote-counting rule. A word that occurs in many documents can still be rejected when it is vague, polysemous, stylistic, or better represented by an existing controlled word.

A narrow term should normally stay project-specific when any of these are true:

- it identifies a product/component unique to a domain;
- its meaning depends on one technical standard or organization;
- a project glossary can define it without weakening interoperability;
- adding it would mainly increase corpus coverage rather than language clarity.

## Ambiguity policy

When one lemma has several common meanings, prefer one of these outcomes:

1. approve one controlled meaning and prohibit/review the others;
2. use different unambiguous words for different concepts;
3. keep the word project-specific;
4. reject the lemma from the central core.

Do not approve multiple meanings merely because they are common German usage.

## Part-of-speech policy

Approval is specific to part of speech. Approval of a noun does not automatically approve the same surface form as a verb, adjective, or other class.

Inflectional forms are governed by the morphology policy. A surface form that collides with another canonical lemma must resolve according to explicit lexical precedence rules.

## Review states

A proposal moves through:

`draft` → `evidence_ready` → `review` → `accepted` | `rejected` | `deferred`

Accepted normative proposals must include tests or validation updates when the behavior is machine-checkable.

## Release handling

- Additions and clarifications can normally ship in a minor release while STG-DE is pre-1.0.
- Restrictions, prohibitions, or controlled-meaning changes must be called out in `CHANGELOG.md`.
- After 1.0, incompatible lexical changes require the compatibility policy defined by project governance.
- The release manifest records the exact dictionary artifacts used for conformance claims.

## Corpus integrity

Do not tune the dictionary against a holdout set and then report that same holdout as independent evidence.

When corpus analysis produces an unknown-token list, treat it as a review queue. Do not automatically convert unknown tokens into approved entries.

## Project terminology escape hatch

Project terminology is a first-class part of STG-DE. Rejecting a term from the central core does not mean the term is forbidden in technical content.

A precise domain term can be valid through `.stg-de.yaml` even when it should never become part of the general STG-DE dictionary.
