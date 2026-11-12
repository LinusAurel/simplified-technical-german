# STG-DE skill evaluation

This directory measures how well an agent applies STG-DE with the bundled skill.

| File | Purpose |
|---|---|
| `cases.yaml` | 12 WRITE, REWRITE, and AUDIT cases across all seven profiles, with machine-checkable expectations. |
| `triggers.yaml` | Requests that should and should not load the skill. Use them to check the skill `description`. |
| `reference/` | Reference outputs. They pass every check and prove that the scorer works. |

## What is measured

All checks are deterministic:

- **Rule compliance:** no deterministic linter errors in WRITE and REWRITE output, with the case profile.
- **Fidelity:** `stg_compare.py` must not report lost protected content (numbers, units, identifiers, code, URLs, quoted UI text, safety signal words).
- **Facts:** required strings are present, prohibited strings are absent.
- **Output discipline:** no preamble, a `Hinweis:` line when the source cannot be made compliant without new facts, and compliant input stays unchanged.
- **Audit accuracy:** the audit names the expected rule IDs and the correct `Ergebnis:` line.

The checks do not prove that meaning is preserved. Review `REVIEW` findings from `stg_compare.py` and a sample of outputs manually.

## Run

Score the reference outputs:

```bash
python tools/run_evals.py --outputs evals/reference
```

Generate and score outputs with any CLI that reads a prompt on stdin:

```bash
python tools/run_evals.py --outputs runs/claude --command "claude -p"
```

Compare runs with and without the skill installed, and across models. Store run outputs outside the repository or in a dated directory. Add a case to `cases.yaml` for every failure that you find in real use.
