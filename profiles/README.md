# STG-DE Application Profiles

Application profiles adapt one STG-DE standard to different communication purposes. They do not create separate dialects and do not change controlled word meanings.

The machine-readable definitions are in `profiles.yaml`.

## Profiles

| Profile | Typical content | Structural basis |
|---|---|---|
| `procedure` | installation, operation, maintenance steps | procedure, 20-word sentence limit |
| `safety` | warnings, cautions, protective actions | procedure, 20-word sentence limit + Section 7 priority |
| `description` | technical explanations and factual descriptions | description, 25-word sentence limit |
| `requirement` | specifications and acceptance criteria | description, explicit modality/scope priority |
| `support` | troubleshooting and customer/internal support | description, actionable/consistent terminology priority |
| `consumer` | B2C instructions and service information | description, plain explicit language priority |
| `agent` | prompts, tool descriptions, inter-agent instructions | procedure, 20-word sentence limit + machine-parse priority |

## Selection

Writers and tools should select a profile from the purpose of the text, not from the industry.

A medical device can contain `procedure`, `safety`, and `description` content. A software product can contain all three plus `support` and `agent` content.

If no profile is clearly applicable, use base STG-DE without inventing one.

## Applicability

`primary_rules` identifies rules that deserve special attention in a profile. It does not disable the rest of STG-DE.

A profile can make a structural limit explicit, but it cannot weaken safety/legal meaning or change a controlled lexical meaning.

## CLI

```bash
python tools/stg_lint.py instructions.md --profile procedure
python tools/stg_lint.py warning.md --profile safety --format json
python tools/stg_lint.py prompt.md --profile agent --format json
```

The legacy `--text-type` option remains available as an explicit structural override. When it is `auto`, the selected profile supplies the structural type.
