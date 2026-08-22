import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

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


class LintTests(unittest.TestCase):
    def test_semicolon_uses_published_rule_id(self):
        r = run("Öffnen Sie die Abdeckung; prüfen Sie den Stecker.", "--text-type", "procedure")
        self.assertEqual(r["result"], "FAIL")
        self.assertTrue(any(f["rule"] == "STG-8.1" for f in r["findings"]))

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
            self.assertTrue(any(f["rule"] == "STG-9.4" for f in r["findings"]))

    def test_procedure_sentence_cap_uses_published_rule_id(self):
        text = "Prüfen Sie jetzt bitte alle vorhandenen elektrischen Verbindungen an diesem Gerät sehr sorgfältig auf sichtbare Schäden und lose Kontakte vor dem Start."
        r = run(text, "--text-type", "procedure")
        self.assertTrue(any(f["rule"] == "STG-5.1" for f in r["findings"]))

    def test_description_sentence_cap_uses_published_rule_id(self):
        text = "Das System verarbeitet die eingehenden Daten und speichert die Ergebnisse nach der vollständigen Prüfung automatisch in einem lokalen Verzeichnis, damit andere Anwendungen die Informationen später ohne zusätzlichen Verarbeitungsschritt verwenden können."
        r = run(text, "--text-type", "description")
        self.assertTrue(any(f["rule"] == "STG-6.3" for f in r["findings"]))

    def test_unknown_not_error(self):
        r = run("Das Quantenflussteil ist aktiv.", "--lexicon-report")
        self.assertNotEqual(r["result"], "FAIL")
        self.assertTrue(any(term == "quantenflussteil" for term, _ in r["unknown_lexicon"]))

    def test_all_emitted_rule_ids_exist_in_rule_index(self):
        import yaml

        index = yaml.safe_load((ROOT / "rules" / "rule-index.yaml").read_text(encoding="utf-8"))
        valid_ids = {item["id"] for item in index["rules"]}

        samples = [
            run("Öffnen Sie die Abdeckung; prüfen Sie den Stecker.", "--text-type", "procedure"),
            run("Prüfen Sie gegebenenfalls den Stecker."),
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
