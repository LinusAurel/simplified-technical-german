# Abschnitt 5 — Anleitungen

## STG-5.1 — Maximal 20 Wörter je Satz in anleitendem Text

**Level:** `MUST`

Ein Satz in einem anleitenden Text hat maximal **20 Wörter** nach den Zählregeln in Abschnitt 8. Diese Grenze gilt auch für eine Anweisung in einem Sicherheitshinweis.

Ein Hinweis ist beschreibender Text. Ein Satz in einem Hinweis darf maximal 25 Wörter haben.

## STG-5.2 — Eine Anweisung je Satz

**Level:** `MUST`

Schreiben Sie eine Anweisung je Satz.

Mehr als eine Handlung in einem Satz ist nur zulässig, wenn die Handlungen eine dieser Bedingungen erfüllen:

- Die Handlungen finden gleichzeitig statt.
- Die Handlungen sind ein einziger untrennbarer physischer Vorgang.
- Eine Handlung ist eine direkte Abnahme- oder Ergebnisaussage, die zu demselben Arbeitsschritt gehört.

<!-- stg-lint: off -->
**Nicht STG**

> Öffnen Sie die Abdeckung und entfernen Sie danach den Filter.
<!-- stg-lint: on -->

**STG**

> 1. Öffnen Sie die Abdeckung.  
> 2. Entfernen Sie den Filter.

**Zulässige gleichzeitige Handlung**

> Halten Sie die Leitung fest und lösen Sie die Mutter.

## STG-5.3 — Anweisungen in einer festgelegten Anredeform

**Level:** `MUST`

Schreiben Sie erforderliche Handlungen des Lesers in der Anredeform des Projekts. Das Projekt legt die Anredeform mit der Einstellung `anrede` in `.stg-de.yaml` fest.

| `anrede` | Form der Anweisung | Beispiel |
|---|---|---|
| `sie` (Standard) | formaler Imperativ mit „Sie“ | „Prüfen Sie die Leitung auf Schäden.“ |
| `du` | Imperativ der 2. Person Singular | „Prüfe die Leitung auf Schäden.“ |
| `infinitiv` | Infinitiv am Satzende | „Leitung auf Schäden prüfen.“ |

Wenn das Projekt keine Anredeform festlegt, gilt `sie`.

**STG** (`anrede: sie`)

> Entfernen Sie die Abdeckung.  
> Stellen Sie den Druck auf 2 bar ein.  
> Prüfen Sie die Leitung auf Schäden.

Ein kontrollierter Dokumentsatz verwendet genau eine Anredeform. Anweisungen, Pronomen und Possessivpronomen der Anrede folgen dieser Form. Ein Dokumentsatz schreibt „du“ oder „Du“ einheitlich.

<!-- stg-lint: off -->
**Nicht STG**

> Prüfen Sie den Druck. Wenn du fertig bist, schließe das Ventil.
<!-- stg-lint: on -->

Verwenden Sie für eine Anweisung kein Passiv, kein `soll` und keine Fragmente, die nur aus Substantiven bestehen. Diese Vorgabe gilt für jede Anredeform.

Der Änderungsvorschlag `proposals/STG-2026-001-form-of-address.md` begründet diese Regel.

## STG-5.4 — Bedingung vor Anweisung

**Level:** `MUST`

Wenn der Leser eine Bedingung vor einer Handlung kennen muss, schreiben Sie die Bedingung zuerst. Trennen Sie die Bedingung mit einem Komma von der Anweisung.

<!-- stg-lint: off -->
**Nicht STG**

> Entfernen Sie die Sicherung, wenn die Anzeige rot ist.
<!-- stg-lint: on -->

**STG**

> Wenn die Anzeige rot ist, entfernen Sie die Sicherung.

## STG-5.5 — Hinweise enthalten keine Anweisungen

**Level:** `MUST`

Ein Hinweis darf nur nützlichen Kontext geben. Ein Hinweis darf diese Inhalte nicht enthalten:

- eine Anweisung,
- eine Schutzhandlung,
- eine verbindliche Anforderung,
- ein Abnahmekriterium,
- einen Grenzwert oder eine Toleranz, die für die korrekte Ausführung des Arbeitsschritts erforderlich ist.

Prüfung: Entfernen Sie jeden Hinweis aus der Anleitung. Der Leser muss die Anleitung auch ohne Hinweise korrekt und sicher ausführen können.

<!-- stg-lint: off -->
**Nicht STG**

> HINWEIS: Ziehen Sie die Schraube mit 8 Nm fest.
<!-- stg-lint: on -->

**STG**

> Ziehen Sie die Schraube mit 8 Nm fest.
