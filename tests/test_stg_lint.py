import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LINTER = ROOT / "tools/stg_lint.py"


def run(text, *args):
    cp = subprocess.run(
        [sys.executable, str(LINTER), "-", "--format", "json", *args],
        input=text,
        text=True,
        capture_output=True,
        check=True,
    )
    return json.loads(cp.stdout)


def rules(result):
    return {f["rule"] for f in result["findings"]}


class LintTests(unittest.TestCase):
    def test_semicolon_uses_published_rule_id(self):
        r = run("Öffnen Sie die Abdeckung; prüfen Sie den Stecker.", "--text-type", "procedure")
        self.assertEqual(r["result"], "FAIL")
        self.assertIn("STG-8.1", rules(r))

    def test_semicolon_free_text_does_not_trigger_rule(self):
        r = run("Öffnen Sie die Abdeckung. Prüfen Sie den Stecker.", "--text-type", "procedure")
        self.assertNotIn("STG-8.1", rules(r))

    def test_prohibited_term_uses_vocabulary_rule_id(self):
        r = run("Prüfen Sie gegebenenfalls den Stecker.")
        findings = [f for f in r["findings"] if (f.get("term") or "").casefold() == "gegebenenfalls"]
        self.assertTrue(findings)
        self.assertTrue(all(f["rule"] == "STG-1.1" for f in findings))

    def test_project_preference_uses_consistency_rule_id(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / ".stg-de.yaml"
            p.write_text(
                "version: 1\npreferred_terms:\n  - preferred: Fehler\n    avoid: [Problemfall]\n",
                encoding="utf-8",
            )
            r = run("Der Problemfall ist dokumentiert.", "--project", str(p))
            self.assertIn("STG-9.4", rules(r))

    def test_procedure_sentence_cap_uses_published_rule_id(self):
        text = "Prüfen Sie jetzt bitte alle vorhandenen elektrischen Verbindungen an diesem Gerät sehr sorgfältig auf sichtbare Schäden und lose Kontakte vor dem Start."
        r = run(text, "--text-type", "procedure")
        self.assertIn("STG-5.1", rules(r))

    def test_short_procedure_sentence_passes_length_check(self):
        r = run("Prüfen Sie den Stecker.", "--text-type", "procedure")
        self.assertNotIn("STG-5.1", rules(r))

    def test_description_sentence_cap_uses_published_rule_id(self):
        text = "Das System verarbeitet die eingehenden Daten und speichert die Ergebnisse nach der vollständigen Prüfung automatisch in einem lokalen Verzeichnis, damit andere Anwendungen die Informationen später ohne zusätzlichen Verarbeitungsschritt verwenden können."
        r = run(text, "--text-type", "description")
        self.assertIn("STG-6.3", rules(r))

    def test_man_is_rejected_as_technical_actor(self):
        r = run("Man prüft danach den Stecker.", "--text-type", "procedure")
        self.assertIn("STG-DE-4.3", rules(r))
        self.assertEqual(r["result"], "FAIL")

    def test_mann_does_not_trigger_man_rule(self):
        r = run("Der Mann prüft den Stecker.")
        self.assertNotIn("STG-DE-4.3", rules(r))

    def test_ambiguous_slash_is_warning(self):
        r = run("Wählen Sie die Option A und/oder B.")
        self.assertIn("STG-DE-8.1", rules(r))
        self.assertEqual(r["result"], "PASS WITH REVIEW")

    def test_url_does_not_trigger_slash_rule(self):
        r = run("Öffnen Sie https://example.com/a/b.")
        self.assertNotIn("STG-DE-8.1", rules(r))

    def test_paragraph_sentence_cap(self):
        text = "Satz eins. Satz zwei. Satz drei. Satz vier. Satz fünf. Satz sechs. Satz sieben."
        r = run(text, "--text-type", "description")
        self.assertIn("STG-6.6", rules(r))
        self.assertEqual(r["result"], "FAIL")

    def test_six_sentence_paragraph_passes_paragraph_cap(self):
        text = "Satz eins. Satz zwei. Satz drei. Satz vier. Satz fünf. Satz sechs."
        r = run(text, "--text-type", "description")
        self.assertNotIn("STG-6.6", rules(r))

    def test_separate_paragraphs_are_counted_separately(self):
        text = "Eins. Zwei. Drei. Vier. Fünf. Sechs.\n\nSieben. Acht. Neun."
        r = run(text, "--text-type", "description")
        self.assertNotIn("STG-6.6", rules(r))

    def test_unknown_not_error(self):
        r = run("Das Quantenflussteil ist aktiv.", "--lexicon-report")
        self.assertNotEqual(r["result"], "FAIL")
        self.assertTrue(any(term == "quantenflussteil" for term, _ in r["unknown_lexicon"]))

    def test_all_emitted_rule_ids_exist_in_rule_index(self):
        index = yaml.safe_load((ROOT / "rules" / "rule-index.yaml").read_text(encoding="utf-8"))
        valid_ids = {item["id"] for item in index["rules"]}

        samples = [
            run("Öffnen Sie die Abdeckung; prüfen Sie den Stecker.", "--text-type", "procedure"),
            run("Prüfen Sie gegebenenfalls den Stecker."),
            run("Man wählt A und/oder B.", "--text-type", "procedure"),
            run("Eins. Zwei. Drei. Vier. Fünf. Sechs. Sieben.", "--text-type", "description"),
            run(
                "Prüfen Sie jetzt bitte alle vorhandenen elektrischen Verbindungen an diesem Gerät sehr sorgfältig auf sichtbare Schäden und lose Kontakte vor dem Start.",
                "--text-type",
                "procedure",
            ),
        ]
        emitted = {f["rule"] for result in samples for f in result["findings"]}
        self.assertTrue(emitted)
        self.assertTrue(emitted <= valid_ids, f"Unknown rule IDs emitted: {sorted(emitted - valid_ids)}")


if __name__ == "__main__":
    unittest.main()
