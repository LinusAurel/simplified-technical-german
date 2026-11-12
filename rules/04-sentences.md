# Abschnitt 4 — Sätze

## STG-4.1 — Kurze, eindeutige Sätze

**Level:** `MUST`

Schreiben Sie kurze Sätze mit einer primären Aussage. In beschreibendem Text empfehlen wir ein Hauptthema je Satz. Verdichten Sie nicht mehrere unabhängige Fakten in einem Satz.

<!-- stg-lint: off -->
**Nicht STG**

> Der Sensor sitzt am Gehäuse, misst den Druck und sendet die Werte an das Steuergerät, das bei einem Grenzwertfehler die Pumpe abschaltet.
<!-- stg-lint: on -->

**STG**

> Der Sensor sitzt am Gehäuse. Der Sensor misst den Druck. Das Steuergerät empfängt die Messwerte. Bei einem Grenzwertfehler schaltet das Steuergerät die Pumpe aus.

## STG-4.2 — Keine bedeutungstragenden Auslassungen

**Level:** `MUST_NOT`

Lassen Sie kein Subjekt, kein Objekt, kein Verb, keinen Artikel und keinen Bezug aus, wenn die Auslassung eine Mehrdeutigkeit erzeugen kann. Verwenden Sie keine Fragmente im Telegrammstil als normalen Fließtext.

<!-- stg-lint: off -->
**Nicht STG**

> Schalter auf EIN.
<!-- stg-lint: on -->

**STG**

> Stellen Sie den Schalter auf EIN.

Überschriften, Tabellenzellen, Beschriftungen und andere kontrollierte Fragmente können nach dem jeweiligen Inhaltsmodell von dieser Regel ausgenommen sein.

## STG-4.3 — Vertikale Listen für komplexe Aufzählungen

**Level:** `MUST`

Verwenden Sie eine vertikale Liste, wenn ein Satz viele parallele Elemente, Bedingungen oder Handlungen enthält.

Regeln:

- Leiten Sie die Liste mit einem grammatisch vollständigen Einleitungssatz und einem Doppelpunkt ein.
- Halten Sie alle Listenelemente grammatisch parallel.
- Mischen Sie in derselben Liste keine Befehle aus Anleitungen und keine beschreibenden Aussagen.
- Schließen Sie ein Listenelement, das ein vollständiger Satz ist, mit einem Punkt ab.
- Verwenden Sie Kommas oder Semikolons nicht als Endzeichen, nur um Listenelemente zu verketten.

## STG-4.4 — Logische Verknüpfungen explizit angeben

**Level:** `MUST`

Verwenden Sie stabile Verknüpfungswörter, wenn die logische Beziehung zwischen Sätzen wichtig ist.

Zu den bevorzugten kontrollierten Verknüpfungswörtern gehören:

- `und` — Addition,
- `aber` — Gegensatz,
- `dann` / `danach` — Reihenfolge,
- `deshalb` — Folge,
- `weil` — Ursache,
- `wenn` — Bedingung,
- `bevor` — früheres Ereignis,
- `während` — gleichzeitiger Zeitraum.

Variieren Sie Verknüpfungswörter nicht nur aus stilistischen Gründen.

## STG-4.5 — Artikel und Demonstrativa eindeutig verwenden

**Level:** `MUST`

Verwenden Sie Artikel und Demonstrativa nach der deutschen Grammatik. Verwenden Sie Artikel und Demonstrativa, um den Status des Bezugs eindeutig anzugeben. Stellen Sie die Kongruenz in Kasus, Genus und Numerus sicher.

Verwenden Sie kein alleinstehendes Demonstrativpronomen, wenn mehr als ein Bezugswort möglich ist. Wir empfehlen ein Demonstrativadjektiv mit Substantiv oder die Wiederholung des technischen Substantivs.

<!-- stg-lint: off -->
**Mehrdeutig**

> Entfernen Sie den Sensor aus dem Halter. Dieser ist beschädigt.
<!-- stg-lint: on -->

**STG**

> Entfernen Sie den Sensor aus dem Halter. Der Sensor ist beschädigt.

oder

> Entfernen Sie den Sensor aus dem Halter. Der Halter ist beschädigt.

## STG-DE-4.1 — Nebensatzverschachtelung begrenzen

**Level:** `MUST`

Verschachteln Sie in anleitendem Text und in Sicherheitshinweisen keine Nebensätze in Nebensätzen. In beschreibendem Text ist eine Ebene der Unterordnung das Standardmaximum.

Formulieren Sie tiefere Strukturen als getrennte Sätze neu.

## STG-DE-4.2 — Pronomen nur mit eindeutigem Bezug

**Level:** `MUST`

Ein Pronomen muss im lokalen Kontext genau ein plausibles Bezugswort haben. Wenn das Pronomen auf mehr als ein Substantiv verweisen kann, wiederholen Sie das Substantiv.

<!-- stg-lint: off -->
**Mehrdeutig**

> Verbinden Sie den Sensor mit dem Adapter, wenn er trocken ist.
<!-- stg-lint: on -->

**STG**

> Wenn der Sensor trocken ist, verbinden Sie den Sensor mit dem Adapter.

## STG-DE-4.3 — `man` nicht als technischer Akteur verwenden

**Level:** `MUST_NOT`

Verwenden Sie das Indefinitpronomen `man` nicht, um den Akteur in technischen Anweisungen oder Anforderungen zu verbergen oder zu verallgemeinern.

Verwenden Sie stattdessen:

- den Imperativ, wenn der Leser handelt,
- eine benannte Rolle, wenn ein festgelegter Akteur handelt,
- das verantwortliche System oder die verantwortliche Komponente, wenn das System oder die Komponente automatisch handelt.

## STG-DE-4.4 — Negationsbereich eindeutig festlegen

**Level:** `MUST`

Positionieren Sie `nicht`, `kein` und andere negative Ausdrücke so, dass nur eine Interpretation plausibel ist. Wenn der Bereich der Negation komplex ist, formulieren Sie den Satz mit einer expliziten Bedingung neu.

<!-- stg-lint: off -->
**Mehrdeutig**

> Schalten Sie das Gerät nicht mit geöffnetem Gehäuse ein.
<!-- stg-lint: on -->

**STG**

> Wenn das Gehäuse offen ist, schalten Sie das Gerät nicht ein.

Vermeiden Sie doppelte Negation.


## STG-DE-4.5 — Pronominaladverbien nur mit eindeutigem Bezug

**Level:** `MUST`

Deutsche Pronominaladverbien wie `dabei`, `dazu`, `daraus`, `davon`, `darüber`, `dafür` und `hierfür` können einen Bezug verdichten. Der Bezug kann auf ein Objekt, eine Handlung, eine Ursache, einen Zweck oder einen vorherigen Satz verweisen. Verwenden Sie eine solche Form nur, wenn genau ein lokales Bezugswort und genau eine semantische Beziehung möglich sind.

Wiederholen Sie beim strengen Schreiben nach `STG-C-core` das technische Substantiv, die Handlung oder die Bedingung, wenn der Bezug mehrere Interpretationen zulässt.

<!-- stg-lint: off -->
**Mehrdeutig**

> Verbinden Sie den Sensor mit dem Adapter. Dabei darf die Dichtung nicht beschädigt werden.
<!-- stg-lint: on -->

`Dabei` kann auf das Verbinden, auf den Adapter oder auf die vollständige vorherige Situation verweisen.

**STG**

> Wenn Sie den Sensor mit dem Adapter verbinden, beschädigen Sie die Dichtung nicht.

Wir empfehlen, dass ein Validator ein ungeklärtes Pronominaladverb als `NEEDS_REFERENCE_INPUT` meldet. Der Validator darf das Bezugswort nicht erfinden.
