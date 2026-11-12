# STG-DE-Governance

STG-DE ist ein offenes Projekt für eine kontrollierte Sprache. Die Spezifikation ist die maßgebliche Quelle. Der Validator und der Agent Skill implementieren die Spezifikation oder unterstützen ihre Anwendung. Diese Werkzeuge definieren die Spezifikation nicht neu.

## Aufgaben der Maintainer

Maintainer sind für diese Aufgaben verantwortlich:

- Sie halten veröffentlichte Regel-IDs stabil.
- Sie prüfen Änderungen an normativer Sprache getrennt von Änderungen, die nur die Implementierung vereinfachen.
- Sie halten das zentrale Vokabular domänenübergreifend und belegbar.
- Sie fordern Tests für maschinell prüfbares Verhalten.
- Sie schützen die Holdout-Evaluation vor Informationen aus der Entwicklung.
- Sie dokumentieren inkompatible Änderungen.
- Sie halten den eigenständigen Agent Skill synchron mit den kanonischen Regeln und Wörterbuchdaten.

## Änderungsklassen

### Redaktionell

Änderungen an Rechtschreibung, Formatierung, Beispielen oder Erklärungen, die das normative Verhalten nicht ändern.

### Lexikalisch

Änderungen an zugelassenen Wörtern, kontrollierten Bedeutungen, Formen, verbotenen Begriffen, Begriffen mit Prüfpflicht oder bevorzugten Ersetzungen. Befolgen Sie `dictionary/GOVERNANCE.md`.

### Regel

Änderungen an einer normativen Regel, einer Empfehlung, einem Schwellenwert, einer Anwendungsbedingung oder der Auslegung der Konformität. Verwenden Sie `proposals/STG-CHANGE-TEMPLATE.md`.

### Implementierung

Änderungen an Validator, Werkzeugen, Paketierung oder Agent Skill, die den Standard selbst nicht ändern. Eine Implementierung muss vorhandene Regel-IDs referenzieren und bekannte Einschränkungen dokumentieren.

## Erwartungen an das Review

Wir empfehlen, dass eine normative Änderung im Normalfall diese Punkte enthält:

1. die Problembeschreibung,
2. das vorgeschlagene Verhalten,
3. konforme und nicht konforme Beispiele,
4. die Auswirkung auf die Kompatibilität,
5. Belege aus dem Korpus oder linguistische Belege, wenn zutreffend,
6. die Auswirkungen auf Validator und Skill,
7. Tests, wenn das Verhalten maschinell testbar ist.

Solange die Gruppe der Maintainer klein ist, gibt es keinen numerischen Schwellenwert für Abstimmungen. Wir empfehlen, dass Maintainer bei umstrittenen normativen Entscheidungen die Begründung im Vorschlag oder im Pull Request dokumentieren.

## Stabilität der Regel-IDs

Veröffentlichte Regel-IDs sind öffentliche Kennungen. Nummerieren Sie eine Regel nicht neu, nur um die Gliederung optisch zu verbessern.

Wenn Sie eine Regel entfernen, reservieren Sie ihre ID und kennzeichnen Sie die Regel als abgekündigt. Wenn Sie eine Regel teilen, behalten Sie nach Möglichkeit die ursprüngliche ID. Fügen Sie neue IDs nur für wirklich neue normative Einheiten hinzu.

## Kompatibilität

`VERSIONING.md` definiert die Regeln für Kompatibilität und Versionierung.

## Releases

Verwenden Sie `RELEASE-CHECKLIST.md`. Ein Release muss diese Prüfungen bestehen: die Testsuite des Repositorys, die Synchronisierung des Skills, die Validierung der strukturierten Daten und die Integritätsprüfung des Release-Manifests.

## Sicherheit und unsicheres Verhalten

Das Projekt ist eine Sprachspezifikation und ein Werkzeug zur Textanalyse. Ein Beitrag darf keinen verborgenen Netzwerkzugriff, keine Erfassung von Zugangsdaten, keine Telemetrie und keine automatische Ausführung des analysierten Texts hinzufügen.

Werkzeuge für das Korpus dürfen ausdrücklich deklarierte öffentliche Quellen für eine vorübergehende Analyse herunterladen. Sie dürfen keine unbearbeiteten Korpora von Dritten in das Repository übernehmen, außer wenn die Rechte zur Weitergabe ausdrücklich bestehen.

## Externes Review

Für 1.0 empfehlen wir ein Review durch Personen mit Fachwissen in technischer Redaktion, in Linguistik oder in beiden Bereichen. Für 1.0 empfehlen wir auch, Belege für eine Verwendung außerhalb des ursprünglichen Entwicklungskontexts zu dokumentieren. Automatisierte CI allein kann diese Kriterien nicht erfüllen.
