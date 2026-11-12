# STG-DE v0.4: Bericht zur Korpusvalidierung über mehrere Branchen

## Zusammenfassung des Ergebnisses

v0.4 validiert den Autorenkern mit einem **geschichteten Korpus aus sechs Branchen** und nicht mit einer einzelnen Ingenieursdomäne. Das öffentliche Validierungsset enthält **18 unabhängige technische Quellen**, je drei Quellen aus jeder Branche. Es enthält **2.066 analysierte Token** in kurzen deutschen Auszügen. Das Release verteilt die Auszüge und Handbücher **nicht**. Es speichert nur Metadaten der Quellen, Hashes, Häufigkeiten und aggregierte Metriken.

| Metrik | v0.3-Basis | v0.4 nur Normalisierung | v0.4 endgültig |
|---|---:|---:|---:|
| Abdeckung durch zentrale kontrollierte Oberflächenformen | 51.4% | 52.7% | **58.1%** |
| Token mit `NEEDS_LEXICON_REVIEW` | 272 | 245 | **232** |
| Rate der gerouteten oder klassifizierten Token | 86.8% | 88.1% | **88.8%** |

Die endgültige Abdeckung durch zentrale Oberflächenformen liegt bei diesem öffentlichen Set **6.7 Prozentpunkte** über der historischen v0.3-Basis. Dieser Wert ist keine Zielrate für die Akzeptanz. Fachnomen, Produktnamen, Kennungen, Domänenverben und absichtlich nicht zugelassene Sprache bleiben erwartungsgemäß außerhalb des allgemeinen Kerns.

## Design des Korpus

| Branche | Quellen | Token | v0.3-Basis | v0.4 endgültig |
|---|---:|---:|---:|---:|
| Anlagenbau | 3 | 311 | 49.2% | **58.5%** |
| Automotive | 3 | 359 | 49.6% | **58.8%** |
| Elektrotechnik | 3 | 342 | 48.8% | **55.0%** |
| Maschinenbau | 3 | 356 | 50.3% | **58.4%** |
| Medizintechnik | 3 | 334 | 52.1% | **55.4%** |
| Software/IT | 3 | 364 | 58.0% | **62.1%** |

Die sechs Strata sind Maschinenbau, Automotive, Elektrotechnik, Software/IT, Medizintechnik und Anlagenbau. Die Auswahl der Quellen bevorzugt Dokumentation von Herstellern oder Projekten, die öffentlich auf Deutsch zugänglich ist. Die Datei `corpus/sources.yaml` dokumentiert die exakten Metadaten der Quellen und die Hashes der Stichproben.

Die Token-Anzahlen sind absichtlich ähnlich, aber nicht gleich. Eine gleiche Anzahl von Dokumenten verhindert, dass eine Branche die Kuratierung dominiert. Das Release enthält keine Handbücher von Dritten. Lesen Sie dieses Release deshalb als **geschichtetes Belegkorpus** und nicht als Volltextarchiv.

## Änderungen in v0.4

### 1. Deutsche Nomenmorphologie ist Teil der lexikalischen Auflösung

v0.3 speicherte Pluralformen wie `Informationen`, `Gefahren`, `Schritte` und `Geräte` in den Metadaten der Nomen. Der Entwicklungsvalidator löste diese Formen aber nicht auf. v0.4 erkennt **deklarierte Pluralformen von Nomen** als `CENTRAL_INFLECTION`. Mit denselben öffentlichen Auszügen erhöht die Normalisierung allein die kontrollierte Abdeckung von 51.4% auf 52.7%.

Diese Änderung ist eine Korrektur des Validators und keine künstliche Vergrößerung des Vokabulars.

### 2. `Datum` und `Daten` sind nicht mehr vermischt

Das Korpus zeigte eine deutsche lexikalische Kollision: `Datum` hat den Plural `Daten`. Technische Dokumentation verwendet `Daten` aber im Normalfall in der Bedeutung „Informationen“. Ein naiver Pluralindex gibt deshalb die falsche kontrollierte Bedeutung. v0.4 fügt ein unabhängiges eingeschränktes Lemma `Daten` hinzu. Kanonische Lemmata haben in v0.4 Vorrang vor Plural-Aliasen.

Dieser Befund ist für die agentenbasierte Validierung wichtig. Gleiche Oberflächenformen genügen nicht, wenn eine deutsche Flexionsform mit einem anderen lexikalischen Konzept kollidiert.

### 3. Großschreibung bedeutet nicht mehr „Fachbegriff“

Im Deutschen sind alle Nomen großgeschrieben. Die Entwicklungsheuristik von v0.3 ordnete jedes unbekannte großgeschriebene Token `TECHNICAL_TERM_CANDIDATE` zu. Diese Zuordnung zeigt eine zu hohe Abdeckung durch Terminologie. v0.4 verwendet die neutrale Klasse `LEXICAL_NOUN_CANDIDATE`. Ein Kandidat wird nur nach der Auflösung gegen ein zugelassenes Projektglossar oder eine Kategorie für Fachnomen zu Projektterminologie.

### 4. Nur domänenübergreifendes, kontrollierbares Vokabular kam in den Kern

v0.4 fügt allgemeine Konzepte technischer Dokumente hinzu. Beispiele sind `Betriebsanleitung`, `Fachpersonal`, `Verletzung`, `Verwendung`, `Produkt`, `Version`, `Änderung`, `Kennzeichnung`, `Symbol` und `Daten`. v0.4 fügt auch direkte Verben wie `lesen`, `wählen`, `bedienen` und `benötigen` hinzu.

Häufigkeit allein genügte **nicht** für eine Zulassung. Häufige Wörter wie `führen`, `bieten`, `berücksichtigen` und `gewährleisten` gehen in das Review. Ihre technische Bedeutung ist für eine bedingungslose Zulassung zu kontextabhängig oder zu abstrakt.

### 5. Die Abdeckungskurve ist jetzt reproduzierbar

`corpus/coverage-curves.csv` beginnt mit dem historischen Ergebnis von v0.3. Danach wendet die Kurve die Normalisierungsschicht von v0.4 an. Danach fügt sie jeden neuen Kerneintrag in einer deterministischen Reihenfolge der Belege hinzu. Mit diesem Verfahren trennt die Kurve die Gewinne aus Korrekturen an Grammatik und Lemmatisierung von den Gewinnen durch neues Vokabular.

## Endgültige Verteilung nach Branchen

| Branche | Kontrolliert | Unbekannt | Review | Verboten | Lexikalische Nomenkandidaten |
|---|---:|---:|---:|---:|---:|
| Anlagenbau | 58.5% | 32 | 6 | 4 | 81 |
| Automotive | 58.8% | 39 | 7 | 5 | 85 |
| Elektrotechnik | 55.0% | 44 | 10 | 4 | 80 |
| Maschinenbau | 58.4% | 41 | 11 | 5 | 79 |
| Medizintechnik | 55.4% | 42 | 9 | 6 | 83 |
| Software/IT | 62.1% | 34 | 6 | 5 | 81 |

## Wiederkehrende Muster außerhalb von STG

Das Korpus begründet weiterhin, übliches fachsprachliches Deutsch abzulehnen oder zu prüfen, wenn es für kontrolliertes Schreiben nicht deterministisch genug ist. Wiederkehrende Beispiele sind `sowie`, `entsprechend`, `gegebenenfalls`, `ausreichend` und kontextabhängige Verben wie `führen` oder `durchführen`.

Das Ziel ist nicht, dass vorhandene Handbücher ohne Änderung bestehen. Das Ziel ist, Autorinnen, Autoren und Agenten deterministische Umformulierungen zu geben. Das Ziel ist auch, allgemeines Kernvokabular von Domänenterminologie zu trennen.


## Was v0.4 nicht beweist

v0.4 ist deutlich stärker als v0.3. Trotzdem ist v0.4 weiterhin ein experimenteller Autorenstandard. Die Version belegt keine Abdeckung der gesamten deutschen technischen Dokumentation. Die Version ersetzt diese Punkte nicht:

- Review durch Fachleute aus deutscher technischer Redaktion und Terminologie,
- Analyse lizenzierter Volltextkorpora in deutlich größerem Umfang,
- einen deterministischen morphologischen und syntaktischen Analyzer für Deutsch,
- Tests des Leseverständnisses,
- Validierung von Sicherheitsinhalten nach dem Veröffentlichungsstandard, der für ein Produkt gilt,
- Governance der Projektterminologie.

`STG-C-core` bleibt deshalb experimentell. `STG-C` bleibt für ein späteres Release reserviert, das Menschen geprüft haben.
