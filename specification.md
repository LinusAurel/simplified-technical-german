# STG-DE normative specification

## 1. Scope

STG-DE is a controlled form of written German for technical documentation. It is intended for procedures, maintenance information, operating information, system descriptions, service documentation, technical reports, safety instructions, and similar technical content.

STG-DE controls **expression**, not document layout. Typography, numbering systems, page design, product-specific warning graphics, units policy, and document architecture remain subject to the applicable publication standard or company directive.

## 2. Design principles

STG-DE is based on these principles:

1. **One term — one concept.** Use one approved designation for one technical concept within a defined scope.
2. **One general word — one controlled meaning.** A central lexicon can restrict a general-language word to one meaning and one word class.
3. **Actions use verbs.** Prefer direct verbs to nominalizations and function-verb constructions.
4. **Known agent first.** Use active voice when the agent is known. Use the formal imperative for instructions.
5. **One instruction per sentence.** Combine actions only when they are simultaneous or form one inseparable physical action.
6. **Conditions before commands.** The reader sees the condition before the action it controls.
7. **Short sentences.** Maximum 20 words for procedure/safety commands; maximum 25 words for descriptions and notes.
8. **One topic per sentence and paragraph.** Add information progressively.
9. **No stylistic synonym variation.** Repetition is preferred to lexical variation.
10. **No hidden modality.** Distinguish requirement, permission, capability/possibility, recommendation, and prohibition.
11. **No unresolved reference.** Pronouns, demonstratives, ellipses, and negation must have an unambiguous scope.
12. **German morphology is explicit data.** Dictionary entries carry gender, plural, inflection, separability, and approved forms as applicable.

## 3. German baseline

The default spelling profile is `de-DE` and follows the **Amtliches Regelwerk der deutschen Rechtschreibung (2024)** unless an applicable official directive requires another German national or organizational spelling profile.

Project configuration may declare a different profile, for example `de-CH`. A document must not mix spelling profiles without an explicit reason.

## 4. Text types

### 4.1 Procedure

A procedure tells the reader what to do. Instructions use the formal imperative with `Sie` unless a mandatory project directive specifies a different controlled imperative profile.

Default:

> Entfernen Sie die Abdeckung.

Not default:

> Abdeckung entfernen.

The infinitive instruction style can be enabled only as a project profile and must then be used consistently.

### 4.2 Description

A description gives information and does not command the reader. Descriptions normally use Präsens. Each sentence has one main topic.

### 4.3 Safety instruction

A safety instruction contains:

1. the signal word or other project-defined risk identifier,
2. the preventive command or the condition,
3. the consequence/risk when known.

The risk taxonomy comes from the applicable safety standard, not from STG-DE.

### 4.4 Note

A note gives optional supporting information. A note must not contain an instruction, mandatory requirement, acceptance limit, tolerance, or safety-critical action.

### 4.5 Locked external text

Legal names, UI labels, placards, document titles, identifiers, formulas, quoted material, and externally controlled strings may be outside STG-DE. The surrounding sentence must still obey STG rules where possible.

## 5. Conformance

### 5.1 `STG-R`

A text conforms to `STG-R` when all applicable mandatory writing rules are satisfied.

### 5.2 `STG-T`

A text conforms to `STG-T` when it conforms to `STG-R` and every technical noun and technical verb is approved in the applicable terminology source.

### 5.3 `STG-C-core`

A text conforms to `STG-C-core` when it conforms to `STG-T` and every other non-locked lexical item is approved for its used meaning and word class in the central v0.4 authoring-core lexicon. Unknown general-language words are not accepted automatically.

### 5.4 `STG-C`

A text conforms to `STG-C` when it conforms to `STG-T` and every other lexical item is approved for its used meaning and word class in a broad, human-reviewed central controlled lexicon.

`STG-C-core` is a closed-vocabulary profile for constrained authoring with the shipped v0.4 core lexicon. `STG-C` remains reserved for a broader, human-reviewed central lexicon and is not a general certification claim in this release.


### 5.5 Canonical lemma and inflection collisions

Lexical resolution must check canonical lemmas before accepting an inflection alias from another entry. If the same surface form can represent two controlled concepts, the lexicon must encode the distinction explicitly and the validator must use context/word class/entry precedence.

Normative example: `Daten` is an independent restricted noun for technical data/information. It must not be resolved automatically as the plural of `Datum`.

## 6. Terminology sources

The terminology resolution order is:

1. Regulatory or contractual terminology that cannot be changed
2. Approved company/product terminology
3. Approved industry/domain terminology
4. STG central lexicon
5. New term proposal subject to review

An agent must not replace an official technical designation merely because a shorter or more common synonym exists.

## 7. Word counting

For rule limits:

- A whitespace-delimited orthographic word normally counts as one word.
- A number with its directly associated unit counts as one word.
- An abbreviation or alphanumeric identifier counts as one word.
- A protected proper name, title, label, or quoted string counts as one word in the surrounding sentence.
- Parenthetical text counts as one word in the outer sentence and is also checked as its own sentence/fragment.
- A hyphenated compound counts as one orthographic word, but the compound-complexity rule still applies.
- Numbering that only identifies a work step does not count.

The word-count rules are compatibility rules, not a license to build syntactically dense compounds.

## 8. Machine-checking philosophy

Rules are classified as:

- `deterministic` — can normally be checked mechanically, for example word count or prohibited semicolon.
- `heuristic` — can be detected with high-value heuristics, for example passive voice or vague words.
- `semantic` — requires terminology or meaning analysis, for example one term/one concept or pronoun ambiguity.
- `domain` — requires approved terminology or subject-matter knowledge.

A validator must distinguish a hard violation from a heuristic finding.


## 8.1 Corpus evidence and lexical governance

Corpus frequency is evidence for lexical review, not automatic approval. A common expression can remain prohibited or review-required when it is vague, polysemous, stylistically redundant, or difficult to resolve deterministically.

A corpus audit must distinguish at least:

- general-language lexical gaps,
- inflection/contraction resolution gaps,
- approved project terminology candidates,
- protected identifiers/names/labels,
- prohibited or review-required wording.

STG-DE must not increase general-language coverage by silently classifying unknown words as technical terms.

## 9. Rule traceability

`rules/rule-index.yaml` is the canonical index for every STG-DE rule and recommendation. Rule IDs are stable within a major release line. A rule record identifies its scope, level, title, and the canonical Markdown file that contains its normative wording.

## 10. Change control

A change to a mandatory rule or dictionary meaning must include:

- identifier,
- old wording/meaning,
- proposed wording/meaning,
- technical reason,
- examples,
- impact on validators,
- migration note.

Versioning follows semantic versioning while the project is experimental. Before a stable 1.0 release, rule IDs should remain stable whenever possible.
