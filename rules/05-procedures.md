# Section 5 — Prozedurales Schreiben

## STG-5.1 — Maximal 20 Wörter pro prozeduralem Satz

**Level:** `MUST`

A procedural sentence, including a safety command, has a maximum of **20 words** under the counting rules in Section 8.

A note is descriptive text and may contain up to 25 words per sentence.

## STG-5.2 — Eine Anweisung pro Satz

**Level:** `MUST`

Write one instruction per sentence.

More than one action is permitted in one sentence only when the actions:

- occur at the same time,
- are a single inseparable physical operation,
- or one action is an immediate acceptance/result statement belonging to the same work step.

**Nicht STG**

> Öffnen Sie die Abdeckung und entfernen Sie danach den Filter.

**STG**

> 1. Öffnen Sie die Abdeckung.  
> 2. Entfernen Sie den Filter.

**Permitted simultaneous action**

> Halten Sie die Leitung fest und lösen Sie die Mutter.

## STG-5.3 — Anweisungen im formalen Imperativ

**Level:** `MUST`

Use the formal German imperative with `Sie` for required reader actions.

**STG**

> Entfernen Sie die Abdeckung.  
> Stellen Sie den Druck auf 2 bar ein.  
> Prüfen Sie die Leitung auf Schäden.

Do not use passive voice, `soll`, or noun-only fragments to encode a command.

A project may adopt an infinitive instruction profile only by explicit directive; mixed imperative profiles are not permitted within one controlled document set.

## STG-5.4 — Bedingung vor Anweisung

**Level:** `MUST`

If the reader must know a condition before an action, place the condition first and separate it from the command with a comma.

**Nicht STG**

> Entfernen Sie die Sicherung, wenn die Anzeige rot ist.

**STG**

> Wenn die Anzeige rot ist, entfernen Sie die Sicherung.

## STG-5.5 — Hinweise enthalten keine Anweisungen

**Level:** `MUST`

A note may provide useful context only. It must not contain:

- a command,
- a safety action,
- a mandatory requirement,
- an acceptance criterion,
- a limit or tolerance that is required to complete the work step correctly.

Test: Remove every note from the procedure. The reader must still be able to perform the procedure correctly and safely.

**Nicht STG**

> HINWEIS: Ziehen Sie die Schraube mit 8 Nm fest.

**STG**

> Ziehen Sie die Schraube mit 8 Nm fest.
