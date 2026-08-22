# Project terminology

Use a project dictionary when text contains product, company, scientific, legal, medical, software, or industry-specific terms that should not enter the central STG-DE lexicon.

Recommended `.stg-de.yaml` structure:

```yaml
version: 1
technical_nouns:
  - term: "Drehmomentwandler"
    definition: "hydrodynamische Baugruppe zur Drehmomentübertragung"
technical_verbs:
  - term: "flashen"
    definition: "Firmware in einen Zielspeicher schreiben"
preferred_terms:
  - preferred: "Fehler"
    avoid:
      - "Problemfall"
protected_terms:
  - "API"
  - "DUT"
```

Resolution order:

1. protected or quoted text,
2. project preferred terminology,
3. project technical nouns and technical verbs,
4. central STG-DE dictionary,
5. review.

Never approve a domain term merely because it is capitalized. German capitalization is grammatical, not terminological evidence.
