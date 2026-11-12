# Projektterminologie

Verwenden Sie ein Projektwörterbuch, wenn ein Text Begriffe zu Produkten, Unternehmen, Wissenschaft, Recht, Medizin, Software oder einer Branche enthält. Diese Begriffe gehören nicht in das zentrale Lexikon von STG-DE.

Empfohlene Struktur von `.stg-de.yaml`:

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

Reihenfolge der Auflösung:

1. geschützter oder zitierter Text,
2. bevorzugte Terminologie des Projekts,
3. technische Substantive und technische Verben des Projekts,
4. zentrales Wörterbuch von STG-DE,
5. Prüfung.

Technische Substantive, technische Verben, geschützte Begriffe und bevorzugte Begriffe des Projekts haben Vorrang vor der zentralen Liste der verbotenen Wörter. Ein Beispiel: Ein Softwareprojekt kann `laufen` (Software wird ausgeführt) als technisches Verb festlegen. Danach meldet der Linter dieses Wort nicht mehr.

Geben Sie einen Fachbegriff nie nur deshalb frei, weil er großgeschrieben ist. Die deutsche Großschreibung ist ein grammatischer Beleg, kein terminologischer Beleg.
