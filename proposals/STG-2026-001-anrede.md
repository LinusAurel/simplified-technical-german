# STG-Änderungsvorschlag STG-2026-001: Anredeform für Anweisungen

**Vorschlags-ID:** STG-2026-001
**Status:** accepted
**Änderungsklasse:** rule
**Ziel-Release:** 0.5.0
**Betroffene Regel:** `STG-5.3`

## Problem

`STG-5.3` verlangt für Anweisungen den formalen Imperativ mit „Sie“. Ein Infinitivstil ist nur per ausdrücklicher Projektvorgabe zulässig. Die Anrede mit „du“ ist nicht zulässig.

Viele deutsche Texte verwenden die Anrede mit „du“ mit Absicht:

- B2C-Kommunikation, Chatbots und Support-Antworten mit einer festgelegten Markenstimme,
- Anweisungen an Agenten in `AGENTS.md`, `CLAUDE.md` und Systemprompts,
- interne Entwicklerdokumentation.

Für diese Texte erzwingt `STG-5.3` einen Wechsel der Anrede. Dieser Wechsel ändert den Ton, aber nicht die Eindeutigkeit. Die eigentliche Ursache von Mehrdeutigkeit ist eine **gemischte** Anrede im selben Dokumentsatz.

## Aktuelles Verhalten

- `STG-5.3` (`MUST`): Anweisungen im formalen Imperativ mit „Sie“.
- Ein Infinitivprofil ist nur per Projektvorgabe zulässig. Gemischte Imperativprofile sind in einem Dokumentsatz nicht zulässig.
- Der Linter prüft `STG-5.3` nicht.

## Neues Verhalten

1. Ein Projekt legt die Anredeform für Anweisungen fest: `sie`, `du` oder `infinitiv`. Die Einstellung heißt `anrede` und steht in `.stg-de.yaml`.
2. Ohne Festlegung gilt `sie`.
3. Ein Dokumentsatz verwendet genau eine Anredeform. Anweisungen, Pronomen und Possessivpronomen der Anrede folgen dieser Form.
4. Die Wahl der Anrede ändert keine andere Regel. Passiv, „soll“ und reine Substantivfragmente bleiben in Anweisungen unzulässig.
5. Die Schreibweise „du“ oder „Du“ ist frei. Ein Dokumentsatz verwendet eine Schreibweise einheitlich.

## Beispiele

### Konform

```text
anrede: sie   → Prüfen Sie den Druck. Wenn der Druck unter 2 bar liegt, schließen Sie das Ventil.
anrede: du    → Prüfe den Druck. Wenn der Druck unter 2 bar liegt, schließe das Ventil.
anrede: infinitiv → Druck prüfen. Wenn der Druck unter 2 bar liegt, Ventil schließen.
```

### Nicht konform

```text
Prüfen Sie den Druck. Wenn du fertig bist, schließe das Ventil.
```

## Auswirkung auf die Kompatibilität

- Bisher konformer Text bleibt konform. Ohne Festlegung gilt `sie`.
- Keine kontrollierte Bedeutung ändert sich.
- Der Linter meldet neu:
  - `error` für `STG-5.3`, wenn eine Anrede festgelegt ist und ein Satz eine andere Form verwendet,
  - `warning` für `STG-5.3`, wenn keine Anrede festgelegt ist und ein Dokument „Sie“ und „du“ mischt.
- Der Agent Skill behält bei REWRITE die Anrede des Originals bei, wenn das Projekt keine Anrede festlegt. Bisher hat der Skill jede Anrede zu „Sie“ geändert.

## Evidenz

Ein Test mit einem privaten deutschen B2C-Monorepo (85 Markdown-Dateien) hat diese Muster gezeigt:

- Die Kunden-FAQ und der Prompt des Chatbots verwenden durchgehend „du“. Diese Anrede ist eine Entscheidung der Marke.
- Die Anweisungen an Agenten verwenden „du“ und den Infinitiv.
- Mehrere Passagen ließen sich mit „du“ vollständig konform umschreiben. Die Bedeutungsprüfung `stg_compare.py` hat keine Abweichung gemeldet.

Die Evidenz kommt aus einer Quelle. Die Holdout-Partition des Korpus wurde für diese Entscheidung nicht verwendet.

## Betrachtete Alternativen

- **Nur „Sie“ (bisher):** Diese Alternative verhindert die Verwendung in vielen B2C- und Agentenkontexten. Sie verbessert die Eindeutigkeit nicht.
- **Anrede je Anwendungsprofil:** Profile ändern nach `profiles/README.md` keine Bedeutung und sind nach dem Zweck eines Textes gewählt. Die Anrede ist eine Entscheidung des Projekts und gilt für alle Profile. Deshalb steht die Einstellung in `.stg-de.yaml`.
- **Freie Anrede ohne Festlegung:** Diese Alternative lässt gemischte Anrede zu. Gemischte Anrede macht unklar, wer angesprochen ist.

## Umsetzung

- Regeln: `rules/05-procedures.md` (`STG-5.3`), Titel in `rules/rule-index.yaml`.
- Zuordnung: Hinweis zu ASD-STE100 5.3 in `mapping/ste100-issue9.yaml`.
- Validator: `tools/stg_lint.py` (Option `--anrede`, Einstellung `anrede`).
- Schema: `schemas/project.schema.json`, Beispiel `.stg-de.example.yaml`.
- Agent Skill: Abschnitt zur Anrede in `SKILL.md`.
- Tests: `tests/test_address.py`.
- Dokumentation: `quality/RULE-COVERAGE.md`, `CHANGELOG.md`.

## Grenzen der automatischen Prüfung

Der Linter erkennt die formale Anrede an „Sie“, „Ihnen“ und „Ihr…“ innerhalb eines Satzes und am formalen Imperativ („Prüfen Sie“). Er erkennt die Anrede mit „du“ an den Pronomen „du“, „dich“, „dir“ und „dein…“.

Ein Imperativ mit „du“ ohne Pronomen („Prüfe den Druck.“) ist nicht sicher erkennbar. Die Form „prüfe“ ist auch die erste Person Singular. Der Linter erkennt den Infinitivstil nicht. Zitierter Text und Code sind von der Prüfung ausgenommen.

## Entscheidung

Der Maintainer hat den Vorschlag am 2026-11-12 angenommen.
