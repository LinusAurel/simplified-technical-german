---
name: simplified-technical-german
description: "Write, rewrite, or audit German text with STG-DE (Simplified Technical German), the German counterpart of ASD-STE100. Use when German text must be unambiguous for humans or AI agents: procedures, safety notes, requirements, support answers, UI and error messages, tool descriptions, system prompts, AGENTS.md or inter-agent instructions. Triggers: STG-DE, STE100 auf Deutsch, vereinfachtes technisches Deutsch, kontrollierte Sprache, eindeutig formulieren, so umschreiben, dass ein Agent es nicht missversteht, Terminologie vereinheitlichen, technische Redaktion prüfen. Preserves facts, numbers, modality, and domain terms. Not for creative, literary, or Leichte-Sprache texts."
---

# Simplified Technical German

Wenden Sie STG-DE auf deutschen Text an. Geben Sie eindeutiger Bedeutung, einheitlicher Terminologie, kurzen Strukturen und expliziten Beziehungen Vorrang. Erhalten Sie die Fakten, die Modalität, den Geltungsbereich, die Zahlen, die Warnungen, die Produktnamen und die technische Bedeutung des Benutzers.

## Den Workflow auswählen

Bestimmen Sie die angeforderte Operation, bevor Sie Text ändern:

1. **WRITE** — Erstellen Sie neuen deutschen Text in STG-DE.
2. **REWRITE** — Formen Sie den gelieferten deutschen Text in STG-DE um.
3. **AUDIT** — Ermitteln Sie Verstöße und schlagen Sie Korrekturen vor. Ersetzen Sie den Ausgangstext des Benutzers nicht stillschweigend.

Wenn der Benutzer zu vorhandenem Text nur „wende STG-DE an“ sagt, verwenden Sie REWRITE. Verwenden Sie AUDIT, wenn der Benutzer eine dieser Anfragen stellt:

- Er fragt, ob der Text konform ist.
- Er fordert Regel-IDs an.
- Er fordert einen Diff an.
- Er fragt, was falsch ist.

## Ein Anwendungsprofil auswählen

Verwenden Sie ein Profil, wenn der Zweck des Texts klar ist. Lesen Sie `references/profiles.yaml` für die Konfiguration der Profile.

- `procedure` — operative Arbeitsschritte und Anweisungen.
- `safety` — Warnungen, Vorsichtshinweise, Gefährdungen und Schutzmaßnahmen.
- `description` — technische oder sachliche erklärende Prosa.
- `requirement` — Spezifikationen, Abnahmekriterien und normative Anforderungen.
- `support` — Anweisungen und Erklärungen für Kunden-Support und internen Support.
- `consumer` — Kommunikation zu Produkten und Dienstleistungen im B2C-Bereich.
- `agent` — Prompts, Tool-Beschreibungen, Anweisungen zwischen Agenten und Prosa für Maschinen.

Wenn der Benutzer ein Profil nennt, verwenden Sie dieses Profil. Leiten Sie sonst das Profil nur ab, wenn der Zweck klar ist. Wenn kein Profil sicher passt, wenden Sie die Basisregeln von STG-DE an. Erfinden Sie kein Profil.

Profile definieren kein anderes Vokabular und keine andere Sprache. Profile definieren für dieselben STG-DE-Regeln die Anwendbarkeit, die Satzgrenzen und die Prioritäten der Prüfung.

## Den Modus auswählen

Wählen Sie, wie streng die lexikalischen Regeln gelten. Die strukturellen Regeln gelten in beiden Modi: Satzlänge, eine Anweisung je Satz, Aktiv, explizite Bedingungen, kein Semikolon, kein `man`.

| Modus | Verwendung | Lexikalische Regeln | Konformitätsziel |
|---|---|---|---|
| `strikt` | Anleitungen, Sicherheitshinweise, Anforderungen, Fehlermeldungen, Tool-Beschreibungen, Anweisungen für Agenten | Bevorzugen Sie zentrale STG-DE-Wörter mit ihrer kontrollierten Bedeutung. Lösen Sie jedes unklare allgemeine Wort auf oder markieren Sie es. | `STG-T` |
| `pragmatisch` | Beschreibungen, Support-Antworten, Verbrauchertexte, READMEs, PR-Beschreibungen, Erklärungen | Richtung: Verwenden Sie das schlichteste präzise Wort und verwenden Sie es einheitlich. | `STG-R` |

Wenn der Benutzer einen Modus nennt, verwenden Sie diesen Modus. Verwenden Sie sonst `strikt` für die Profile `procedure`, `safety`, `requirement` und `agent`. Verwenden Sie `pragmatisch` für alle anderen Texte.

## Die Anredeform festlegen

Anweisungen stehen in genau einer Anredeform (`STG-5.3`): `sie` („Prüfen Sie …“), `du` („Prüfe …“) oder `infinitiv` („… prüfen.“). Bestimmen Sie die Anredeform in dieser Reihenfolge:

1. Verwenden Sie die Anredeform, die der Benutzer nennt.
2. Verwenden Sie sonst die Einstellung `anrede` aus `.stg-de.yaml`.
3. Behalten Sie bei REWRITE sonst die Anredeform des Originals bei. Wenn das Original Anredeformen mischt, verwenden Sie die häufigste Form und schreiben Sie eine Zeile `Hinweis:`.
4. Verwenden Sie bei WRITE sonst `sie`.

Ändern Sie die Anredeform nicht, um eine Regel zu erfüllen. Die Anredeform gehört zum Ton und zur Marke des Texts. Übergeben Sie die Anredeform an den Linter: `--anrede du`.

## Referenzen schrittweise laden

Lesen Sie nur das Material, das die aktuelle Aufgabe benötigt:

- Lesen Sie `references/profiles.yaml`, wenn die Auswahl des Profils wichtig ist.
- Lesen Sie `references/rules.md` für Schreibregeln und Beispiele.
- Lesen Sie `references/dictionary-guide.md` für Morphologie, Terminologie und das Verhalten des Lexikons.
- Durchsuchen Sie `references/approved-words.yaml`, wenn die lexikalische Freigabe oder die Bedeutung wichtig ist.
- Durchsuchen Sie `references/prohibited-words.yaml` für verbotene und prüfpflichtige Begriffe und Hinweise zur Umformulierung.
- Lesen Sie `references/project-terminology.md`, wenn ein Projektglossar vorhanden ist oder Fachbegriffe ungelöst sind.
- Lesen Sie `references/validator-contract.md`, wenn Sie die Ausgabe des Validators oder Konformitätsprofile interpretieren.

Laden Sie nicht das vollständige Wörterbuch, wenn eine gezielte Suche genügt.

## Werkzeuge verwenden, wenn verfügbar

Wenn Code-Ausführung verfügbar ist, verwenden Sie diese Ebenen dort, wo sie zum Ergebnis beitragen:

1. Führen Sie `scripts/stg_lint.py` für deterministische und kontrollierte Prüfungen aus.
2. Führen Sie für AUDIT oder für ein schwieriges REWRITE auch `scripts/stg_analyze.py` aus. Das Analysewerkzeug liefert Belege für die Prüfung der deutschen Sprache.
3. Führen Sie nach jedem REWRITE `scripts/stg_compare.py` mit dem Ausgangstext und der Umformulierung aus.

Die Bedeutungsprüfung erkennt verlorene Zahlen, Einheiten, Bezeichner, Code, URLs, zitierte UI-Texte und Signalwörter für Sicherheit. Die Bedeutungsprüfung erkennt auch geänderte Modalität, Verbote, Verneinungen, Bedingungen und Grenzen.

Beispiele:

```bash
python scripts/stg_lint.py input.txt --profile procedure --format json
python scripts/stg_lint.py input.md --profile support --project .stg-de.yaml --format json
python scripts/stg_analyze.py input.md --format json
python scripts/stg_compare.py original.txt rewrite.txt --format json
```

Ein `FAIL` von `stg_compare.py` bedeutet: Geschützter Inhalt ist verloren oder geändert. Stellen Sie diesen Inhalt wieder her, bevor Sie die Umformulierung zurückgeben. Werten Sie die `REVIEW`-Befunde der Bedeutungsprüfung als Aufforderung, die betroffenen Sätze zu vergleichen. Diese Befunde sind kein Beweis für eine Änderung der Bedeutung.

Werten Sie deterministische `error`-Befunde des Linters als Verstöße. Werten Sie `warning`- und `review`-Befunde des Linters und **alle** Belege von `stg_analyze.py` als Kontext, der eine Interpretation erfordert. Das Analysewerkzeug dient nur der Prüfung, auch wenn seine Konfidenz `high` ist.

Formulieren Sie einen Satz nie nur deshalb um, weil eine Heuristik ihn als falsch meldet. Bestätigen Sie die tatsächliche Regel und erhalten Sie die Bedeutung des Ausgangstexts.

Wenn keine Code-Ausführung verfügbar ist, fahren Sie ohne Code-Ausführung fort. Wenden Sie die mitgelieferten Regeln, das ausgewählte Profil und das Wörterbuch direkt an.

## Den Kernprozess anwenden

1. Lesen Sie die vollständige Eingabe einmal, um die Bedeutung zu verstehen.
2. Ermitteln Sie geschützte Inhalte: Zahlen, Einheiten, Bezeichner, zitierte UI-Texte, rechtliche Namen, Produktnamen, Code, URLs und Fachterminologie.
3. Wählen Sie das Anwendungsprofil aus, wenn der Zweck des Texts klar ist. Bestimmen Sie die Anredeform.
4. Erhalten Sie die Modalität. Ändern Sie Möglichkeit nicht in Gewissheit, Erlaubnis nicht in Pflicht und Empfehlung nicht in Anforderung.
5. Lösen Sie die Terminologie auf. Verwenden Sie den Projektbegriff, wenn ein Projektwörterbuch einen Begriff festlegt. Erhalten Sie sonst notwendige Fachbegriffe. Markieren Sie ungelöste Begriffe nur im AUDIT-Modus.
6. Wenden Sie die strukturellen Regeln vor der lexikalischen Optimierung an.
7. Wenden Sie die lexikalischen Regeln mit der kontrollierten Bedeutung und der Wortart an.
8. Verwenden Sie Belege für die Prüfung, wenn diese Belege relevant sind: Passiv, mehrdeutige Modalität, komplexe Satzgefüge, Pronomenbezug, Reichweite der Verneinung, Nominalstil, Komposita und trennbare Verben.
9. Lesen Sie das Ergebnis erneut und vergleichen Sie es mit dem Ausgangstext. Prüfen Sie, dass sich kein Fakt, keine Bedingung, keine Ausnahme, kein Akteur, keine Grenze und keine Beziehung geändert hat. Führen Sie `stg_compare.py` aus, wenn Werkzeuge verfügbar sind.
10. Führen Sie den deterministischen Linter erneut aus, wenn Werkzeuge verfügbar sind. Korrigieren Sie deterministische Befunde, wenn die Korrektur die Bedeutung nicht ändert.
11. Lassen Sie konformen Text unverändert. Formulieren Sie Text nicht nur aus stilistischen Gründen um.

## Prioritäten beim Schreiben

Verwenden Sie diese Prioritäten in dieser Reihenfolge:

1. **Technische Korrektheit** — Ändern Sie nie den beabsichtigten Fakt oder die beabsichtigte Handlung.
2. **Sicherheit und rechtliche Bedeutung** — Schwächen Sie nie Warnungen, Bedingungen, Erlaubnisse, Verbote oder Pflichten ab.
3. **Eindeutige Struktur** — Bevorzugen Sie explizite Akteure, Objekte, Bedingungen und Bezüge.
4. **Einheitliche Terminologie** — Verwenden Sie im jeweiligen Geltungsbereich einen Begriff für ein Konzept.
5. **Kontrolliertes Vokabular** — Bevorzugen Sie freigegebene zentrale Wörter, wenn sie die korrekte Bedeutung ausdrücken.
6. **Prioritäten des Profils** — Wenden Sie die zusätzlichen Prioritäten des ausgewählten Profils an.
7. **Kürze** — Kürzen Sie nur, wenn die ersten sechs Prioritäten erfüllt sind.

## Text für KI-Agenten

Ein Text, den ein Agent oder ein Programm liest, hat keinen Leser, der nachfragen kann. Verwenden Sie für diese Texte das Profil `agent` und den Modus `strikt`: Prompts, Tool-Beschreibungen, Fehlermeldungen, Statusberichte und Anweisungen zwischen Agenten. Beachten Sie zusätzlich diese Punkte:

- Nennen Sie den Akteur und das Objekt jeder Handlung.
- Nennen Sie jede Bedingung, jede Grenze und jede Ausnahme in einem eigenen Satz oder Listenpunkt.
- Verwenden Sie einen Begriff für ein Konzept, auch in Tool-Namen, Parametern und Prosa.
- Übernehmen Sie Bezeichner, Parameternamen, Pfade und Code genau wie angegeben, in Backticks.
- Schreiben Sie Fehlermeldungen in dieser Form: was geschehen ist, warum (wenn bekannt), was der Leser als Nächstes tut.

## Beliebiger deutscher Text

Akzeptieren Sie deutschen Text aus jedem Fachgebiet. Verlangen Sie nicht, dass der Text ein technisches Handbuch ist. Sie können STG-DE für viele Textarten verwenden: Support-Nachrichten, Anweisungen für Verbraucher, Produkttexte, interne Abläufe, UI-Texte von Software, Anforderungen, Verträge, Prompts und andere Prosa.

Entfernen Sie kein notwendiges Fachvokabular, nur damit ein Text schlichter aussieht. Eine kontrollierte Sprache kontrolliert Mehrdeutigkeit, nicht Fachwissen.

Erhalten Sie bei werbenden oder markensensiblen Texten das Kommunikationsziel. Formulieren Sie den Text aber expliziter und einheitlicher. Wenn STG-DE einen gewünschten Ton oder eine rhetorische Wirkung wesentlich entfernt, erhalten Sie die beabsichtigte Aussage. Nennen Sie den Zielkonflikt nur, wenn der Benutzer eine Analyse anfordert.

## Prüfungen für das Deutsche

Achten Sie besonders auf diese Punkte:

- lange oder mehrdeutige Komposita,
- trennbare Verben und abgetrennte Verbpartikeln,
- lange Satzklammern,
- verschachtelte Nebensätze,
- Passivkonstruktionen mit `werden`,
- nominalisierte Handlungen, wenn ein direktes Verb klarer ist,
- mehrdeutige Pronomen und Pronominaladverbien wie `dabei`, `dazu`, `daraus`, `davon` und `darüber`,
- vage modale Wörter wie `gegebenenfalls`, `möglichst`, `ordnungsgemäß` oder `zeitnah`,
- mehrdeutige Reichweite von `nicht`, `nur`, `auch` und ähnlichen Partikeln,
- uneinheitliche Synonyme für dasselbe Konzept,
- Wörter, deren flektierte Form mit einem anderen Lemma oder einer anderen Bedeutung zusammenfällt.

Verwenden Sie die tatsächlichen Regeldefinitionen in `references/rules.md` für normative Entscheidungen.

## Ausgabe

### WRITE und REWRITE

Geben Sie **standardmäßig nur den fertigen STG-DE-Text** zurück. Fügen Sie keine Einleitung, keine Ankündigung des Profils, keine Regeltabelle, keine Anzahl der Verstöße und keine abschließende Erklärung hinzu. Eine Ausnahme gilt, wenn der Benutzer eines dieser Elemente anfordert.

Wenn strikte Konformität nur mit einer Änderung der Bedeutung möglich ist, behalten Sie die notwendige Formulierung. Fügen Sie nur dann eine kurze `Hinweis:`-Zeile hinzu, wenn das ungelöste Problem für die angeforderte Ausgabe wesentlich ist.

### AUDIT

Geben Sie eine knappe Tabelle zurück:

```markdown
| Regel | Befund | Original | Vorschlag |
|---|---|---|---|
| STG-5.2 | Mehrere unabhängige Anweisungen | ... | ... |
```

Geben Sie nach der Tabelle diese Zeile an:

```text
Ergebnis: PASS | PASS WITH REVIEW | FAIL
```

Ein deterministischer Fehler des Linters ergibt das Ergebnis `FAIL`. Verwenden Sie `PASS WITH REVIEW`, wenn kein deterministischer Fehler vorhanden ist, aber relevante heuristische oder ungelöste Belege für die Prüfung bleiben. Vergeben Sie `FAIL` nicht allein auf Grund von Belegen des Analysewerkzeugs.

Wenn Sie ein Profil oder einen Modus ausgewählt haben, nennen Sie beide in einer kurzen Zeile nach dem Ergebnis. Ein Beispiel ist `Profil: procedure · Modus: strikt`.

## Projektterminologie

Wenn `.stg-de.yaml` oder ein anderes Projektglossar vorhanden ist, geben Sie diesem Glossar Vorrang. Der Vorrang gilt für technische Substantive, technische Verben, geschützte Begriffe und bevorzugte Terminologie. Die Projektterminologie erweitert den zentralen Kern. Die Projektterminologie setzt die strukturellen Schreibregeln nicht außer Kraft.

Wenn kein Projektwörterbuch vorhanden ist:

- Behalten Sie notwendige fachliche Substantive und Verben.
- Verwenden Sie denselben Begriff einheitlich.
- Erfinden Sie kein schlichteres Synonym, wenn das Synonym die technische Bedeutung ändern kann.
- Markieren Sie im AUDIT-Modus ungelöste Fachbegriffe als Prüfpunkte und nicht als automatische Fehler.

## Grenzen

- Erfinden Sie keine Fakten, um einen Text expliziter zu formulieren.
- Löschen Sie keine Einschränkungen oder Ausnahmen stillschweigend, um Wortgrenzen einzuhalten.
- Behaupten Sie keine vollständige lexikalische Konformität, wenn ungelöste Wörter bleiben.
- Klassifizieren Sie ein unbekanntes großgeschriebenes deutsches Substantiv nicht als Fachbegriff, nur weil es großgeschrieben ist.
- Werten Sie eine heuristische Analyse nicht als stärkeren Beleg als die tatsächliche Bedeutung des Satzes.
- Verlangen Sie nicht, dass Fachvokabular zum zentralen Wörterbuch gehört, wenn ein Projektbegriff passt.
- Lassen Sie nicht zu, dass ein Anwendungsprofil die Bedeutung einer Kernregel oder eines kontrollierten Worts außer Kraft setzt.
