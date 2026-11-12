# STG-DE für AGENTS.md, CLAUDE.md und Systemprompts

Diese Datei enthält zwei Textbausteine für Werkzeuge ohne Skill-Unterstützung. Kopieren Sie einen Baustein in `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md` oder einen Systemprompt.

Der Skill ist genauer als diese Bausteine. Verwenden Sie den Skill, wenn Ihr Werkzeug Skills unterstützt.

## Kurzfassung

```markdown
## Deutsche Texte

Schreiben Sie deutsche Dokumentation, Fehlermeldungen und Anweisungen an Agenten in STG-DE (https://github.com/linusaurel/simplified-technical-german):

- höchstens 20 Wörter je Satz in Anleitungen,
- eine Anweisung je Satz im formalen Imperativ: „Prüfen Sie den Druck.“,
- Aktiv statt Passiv, kein `man`,
- die Bedingung vor der Anweisung,
- kein Semikolon,
- ein Begriff für ein Konzept.

Behalten Sie Zahlen, Einheiten, Kennungen, Code, Modalität und Fachbegriffe exakt bei.
```

## Vollständige Fassung

```markdown
## Deutsche Texte in STG-DE

Schreiben Sie deutsche Texte für Menschen und Agenten in STG-DE (Simplified Technical German).
STG-DE ist eine kontrollierte Sprache nach dem Vorbild von ASD-STE100.

### Anleitungen

- Schreiben Sie höchstens 20 Wörter je Satz.
- Schreiben Sie eine Anweisung je Satz.
- Verwenden Sie den formalen Imperativ: „Prüfen Sie den Druck.“
- Nennen Sie die Bedingung zuerst: „Wenn die Anzeige rot ist, ziehen Sie den Stecker.“
- Nummerieren Sie die Schritte.

### Beschreibungen

- Schreiben Sie höchstens 25 Wörter je Satz.
- Schreiben Sie höchstens sechs Sätze je Absatz.
- Schreiben Sie ein Thema je Absatz.

### Wörter

- Verwenden Sie einen Begriff für ein Konzept. Verwenden Sie keine Synonyme für dieses Konzept.
- Verwenden Sie direkte Verben: „prüfen“ statt „eine Prüfung durchführen“.
- Verwenden Sie das Aktiv. Nennen Sie den Akteur.
- Verwenden Sie nicht `man`.
- Ersetzen Sie vage Wörter wie „gegebenenfalls“, „zeitnah“ und „ordnungsgemäß“ durch eine Bedingung, eine Frist oder ein Kriterium.
- Verwenden Sie Pronomen und Wörter wie „dabei“ oder „dazu“ nur mit eindeutigem Bezug.

### Modalität

- „muss“ bezeichnet eine Pflicht.
- „darf nicht“ bezeichnet ein Verbot.
- „kann“ bezeichnet eine Möglichkeit.
- Ändern Sie die Modalität beim Umschreiben nicht.

### Zeichen

- Verwenden Sie kein Semikolon.
- Verwenden Sie nicht „und/oder“. Schreiben Sie „A oder B oder beide“ oder eine Liste.

### Schutz von Inhalten

Behalten Sie diese Inhalte exakt bei: Zahlen, Einheiten, Grenzwerte, Kennungen, Produktnamen, Code, Pfade, URLs, zitierte Beschriftungen, Warnungen und Fachbegriffe.
Erfinden Sie keine Fakten.

### Fehlermeldungen

Schreiben Sie drei Teile: was passiert ist, warum es passiert ist, was der Leser jetzt tut.
```

## Prüfung

Prüfen Sie Texte mit dem Linter und der Bedeutungsprüfung:

```bash
python tools/stg_lint.py docs/ --profile agent --fail-on error
python tools/stg_compare.py original.md umschreibung.md
```
