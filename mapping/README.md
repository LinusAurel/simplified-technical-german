# Source-rule traceability

`ste100-issue9.yaml` maps every writing rule and general recommendation of **ASD-STE100 Issue 9 (January 2025)** to the STG-DE rule that implements the same intent for German.

## How to read the mapping

| Field | Meaning |
|---|---|
| `ste` | ASD-STE100 rule number (`1.1` … `9.4`) or general recommendation (`GR-1` … `GR-8`). |
| `stg` | Primary STG-DE rule. Numbered STG rules reuse the ASD-STE100 number: `STG-5.1` implements rule 5.1. |
| `related` | Further STG-DE rules that cover part of the same risk. |
| `relation` | `equivalent`, `adapted`, or `replaced` (see below). |
| `note` | Independently written German explanation of the adaptation. |

- `equivalent` — same intent. German wording and examples are independent.
- `adapted` — same intent, but scope, thresholds, or mechanics are adapted to German grammar.
- `replaced` — the source rule targets an English-specific phenomenon, for example the `-ing` form or phrasal verbs. STG-DE replaces it with the German phenomenon that carries the same risk, for example nominalization or function-verb constructions.

`german_extensions` lists the `STG-DE-*` rules that have no direct ASD-STE100 counterpart, with the nearest source rule.

## Summary

| Relation | Writing rules | General recommendations |
|---|---:|---:|
| equivalent | 35 | 2 |
| adapted | 15 | 4 |
| replaced | 3 | 2 |
| **total** | **53** | **8** |

All 75 STG-DE rules and recommendations are reachable from this file. `tests/test_mapping.py` enforces completeness.

## Copyright boundary

ASD-STE100 is a copyright and EU-registered trademark of ASD (Aerospace, Security and Defence Industries Association of Europe), Brussels. The standard is available free of charge from <https://www.asd-ste100.org>, but redistribution requires written permission from ASD.

This repository therefore contains **only rule numbers and independently written German text**. It does not reproduce ASD-STE100 rule wording, examples, or dictionary entries. STG-DE is not an official ASD publication and is not endorsed by ASD or the STEMG.
