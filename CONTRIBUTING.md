# Contributing to STG-DE

STG-DE is intended to work across industries and communication types. Contributions should therefore separate general German from domain-specific terminology.

## Before you propose a central word

1. Confirm that the word is useful across more than one narrow domain.
2. Define one controlled meaning for each proposed entry.
3. State the part of speech.
4. Provide a short approved example.
5. If the word is ambiguous, prefer a restricted entry or add it to the review/prohibited list.
6. Keep product names and narrow industry terminology in a project dictionary instead of the central core.

## Rule changes

A rule change should include:

- the problem it solves,
- at least one non-compliant and compliant example,
- the expected effect on existing texts,
- validator implications when applicable.

## Tests

Run:

```bash
python tools/validate_release.py
python -m unittest discover -s tests -v
python tools/sync_skill.py --check
```

Do not commit third-party full-text corpus documents. Add only metadata and derived metrics to `corpus/`.
