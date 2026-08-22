# STG-DE Vale rules

This directory exposes a small, conservative Vale subset for editor/documentation pipelines.

The Vale rules are **not** a full STG-DE validator. They cover only conditions that map cleanly to Vale's pattern model.

Included:

- `STG-DE.Semicolon` -> `STG-8.1` deterministic error.
- `STG-DE.IndefiniteMan` -> `STG-DE-4.3` deterministic error.
- `STG-DE.AmbiguousSlash` -> `STG-DE-8.1` warning for `und/oder` and `oder/und`.

Use `stg lint` for the canonical deterministic implementation and `stg analyze` for review-only German-language evidence.

## Example `.vale.ini`

```ini
StylesPath = ./vale
MinAlertLevel = suggestion

[*.{md,txt,rst}]
BasedOnStyles = STG-DE
```

Copy/symlink the `STG-DE` directory into your Vale `StylesPath`, or configure `StylesPath` to the repository `vale/` directory.

Do not add broad regex rules here unless their false-positive behavior is bounded and tested against the canonical rule semantics.
