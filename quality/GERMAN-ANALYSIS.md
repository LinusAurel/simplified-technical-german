# German Analysis Layer

`tools/stg_analyze.py` adds a conservative review layer for German structures that the deterministic linter cannot prove reliably.

It is deliberately separate from `tools/stg_lint.py`.

## Contract

The analyzer returns **review evidence only**. Its findings do not by themselves make a document non-conforming.

Each finding contains:

- STG-DE rule ID;
- evidence kind;
- confidence (`high`, `medium`, or `low`);
- triggering token/pattern;
- source sentence;
- optional review guidance.

The current fallback analyzer has no downloaded language model and performs no dependency parsing or coreference resolution.

## Current evidence

The analyzer can surface candidates for:

- ambiguous modal forms such as `sollte`/`müsste` (`STG-DE-3.2`);
- modal observations for `muss`, `darf`, and `kann` (`STG-DE-3.2`);
- possible passive constructions (`STG-3.6`);
- restrictive review of `werden` (`STG-DE-3.3`);
- multiple/long subordinate-clause markers (`STG-DE-4.1`);
- possible ambiguous pronoun references (`STG-DE-4.2`);
- pronominal adverbs (`STG-DE-4.5`);
- nominalization candidates (`STG-3.5`);
- long separable-verb brackets (`STG-DE-3.1`);
- potentially ambiguous negation/focus scope (`STG-DE-4.4`);
- very long German compound candidates (`STG-DE-2.1`).

## Usage

```bash
python tools/stg_analyze.py document.md
python tools/stg_analyze.py document.md --format json
```

Use the deterministic linter and the review analyzer together:

```bash
python tools/stg_lint.py document.md --profile procedure --format json
python tools/stg_analyze.py document.md --format json
```

## Confidence semantics

`high` means the trigger is mechanically clear, not that the STG-DE rule is definitely violated. For example, `sollte` is clearly present and is an intentionally ambiguous normative form, but the correct rewrite still depends on author intent.

`medium` means the structure is a plausible review target with bounded pattern evidence.

`low` means the signal is useful for prioritizing human/agent review but has a substantial false-positive surface.

## Future parser adapter

A future parser-backed implementation can improve:

- morphology and lemmatization;
- dependency-based passive detection;
- subordinate-clause depth;
- separable-verb reconstruction;
- pronoun/coreference evidence;
- negation scope;
- compound segmentation.

Parser-assisted checks must keep confidence and evidence visible. They must not silently promote semantic/heuristic rules to deterministic errors without measured precision on held-out data.
