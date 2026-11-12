# Analyseschicht für Deutsch

`tools/stg_analyze.py` fügt eine konservative Review-Schicht für deutsche Strukturen hinzu, die der deterministische Linter nicht zuverlässig nachweisen kann.

Diese Schicht ist absichtlich von `tools/stg_lint.py` getrennt.

## Vertrag

Der Analyzer gibt **nur Belege für das Review** zurück. Die Befunde des Analyzers allein sind kein Grund für die Nichtkonformität eines Dokuments.

Jeder Befund enthält diese Angaben:

- STG-DE-Regel-ID,
- Art des Belegs,
- Konfidenz (`high`, `medium` oder `low`),
- auslösendes Token oder Muster,
- Quellsatz,
- optionale Hinweise für das Review.

Der derzeitige Fallback-Analyzer hat kein heruntergeladenes Sprachmodell. Er führt kein Dependency-Parsing und keine Koreferenzauflösung aus.

## Derzeitige Belege

Der Analyzer kann Kandidaten für diese Fälle anzeigen:

- mehrdeutige Modalformen wie `sollte` oder `müsste` (`STG-DE-3.2`),
- Beobachtungen zu den Modalverben `muss`, `darf` und `kann` (`STG-DE-3.2`),
- mögliche Passivkonstruktionen (`STG-3.6`),
- restriktives Review von `werden` (`STG-DE-3.3`),
- mehrere oder lange Marker für Nebensätze (`STG-DE-4.1`),
- mögliche mehrdeutige Pronomenbezüge (`STG-DE-4.2`),
- Pronominaladverbien (`STG-DE-4.5`),
- Kandidaten für Nominalisierungen (`STG-3.5`),
- lange Klammern durch trennbare Verben (`STG-DE-3.1`),
- Geltungsbereich von Negation oder Fokus, der mehrdeutig sein kann (`STG-DE-4.4`),
- Kandidaten für sehr lange deutsche Komposita (`STG-DE-2.1`).

## Verwendung

```bash
python tools/stg_analyze.py document.md
python tools/stg_analyze.py document.md --format json
```

Verwenden Sie den deterministischen Linter und den Review-Analyzer zusammen:

```bash
python tools/stg_lint.py document.md --profile procedure --format json
python tools/stg_analyze.py document.md --format json
```

## Semantik der Konfidenz

`high` bedeutet: Der Auslöser ist maschinell eindeutig. Es bedeutet nicht, dass ein Verstoß gegen die STG-DE-Regel sicher ist. Ein Beispiel ist `sollte`. Das Wort ist eindeutig vorhanden und ist eine absichtlich mehrdeutige normative Form. Die korrekte Umformulierung hängt trotzdem von der Absicht der schreibenden Person ab.

`medium` bedeutet: Die Struktur ist ein plausibles Ziel für ein Review, mit begrenzten Belegen aus Mustern.

`low` bedeutet: Das Signal hilft, das Review durch Menschen oder Agenten zu priorisieren. Das Signal hat aber ein großes Risiko für falsch positive Befunde.

## Zukünftiger Parser-Adapter

Eine zukünftige Implementierung mit Parser kann diese Bereiche verbessern:

- Morphologie und Lemmatisierung,
- Erkennung von Passiv auf Basis von Dependenzen,
- Tiefe von Nebensätzen,
- Rekonstruktion trennbarer Verben,
- Belege für Pronomen und Koreferenz,
- Geltungsbereich von Negationen,
- Segmentierung von Komposita.

Prüfungen mit Parser-Unterstützung müssen Konfidenz und Belege sichtbar halten. Ohne gemessene Präzision mit Holdout-Daten dürfen diese Prüfungen semantische oder heuristische Regeln nicht unbemerkt zu deterministischen Fehlern hochstufen.
