import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYZER = ROOT / "tools" / "stg_analyze.py"


def analyze(text):
    cp = subprocess.run(
        [sys.executable, str(ANALYZER), "-", "--format", "json"],
        input=text,
        text=True,
        capture_output=True,
        check=True,
    )
    return json.loads(cp.stdout)


def kinds(result):
    return {item["kind"] for item in result["evidence"]}


def rules(result):
    return {item["rule"] for item in result["evidence"]}


class AnalyzerTests(unittest.TestCase):
    def test_ambiguous_modal_is_high_confidence_review(self):
        result = analyze("Der Bediener sollte den Stecker prüfen.")
        matches = [item for item in result["evidence"] if item["kind"] == "ambiguous_modality"]
        self.assertTrue(matches)
        self.assertEqual(matches[0]["rule"], "STG-DE-3.2")
        self.assertEqual(matches[0]["confidence"], "high")
        self.assertEqual(result["status"], "REVIEW EVIDENCE ONLY")

    def test_muss_is_observation_not_violation(self):
        result = analyze("Der Bediener muss den Stecker prüfen.")
        self.assertIn("modality_observation", kinds(result))
        self.assertNotIn("ambiguous_modality", kinds(result))

    def test_passive_candidate(self):
        result = analyze("Der Stecker wird geprüft.")
        self.assertIn("passive_candidate", kinds(result))
        self.assertIn("STG-3.6", rules(result))

    def test_multiple_subordinators(self):
        result = analyze("Wenn die Anzeige rot ist, warten Sie, bis das System den Test beendet.")
        self.assertIn("subordinate_clause_complexity", kinds(result))

    def test_pronominal_adverb_review(self):
        result = analyze("Das Modul und der Sensor sind aktiv. Dazu gehört ein Kabel.")
        self.assertIn("pronominal_adverb", kinds(result))
        self.assertIn("STG-DE-4.5", rules(result))

    def test_nominalization_candidate(self):
        result = analyze("Die Installation erfolgt morgen.")
        self.assertIn("nominalization_candidate", kinds(result))

    def test_negation_scope(self):
        result = analyze("Verwenden Sie nicht nur den ersten Wert.")
        self.assertIn("negation_scope", kinds(result))

    def test_long_compound_review(self):
        result = analyze("Die Energieversorgungsunterbrechung ist dokumentiert.")
        self.assertIn("long_compound_candidate", kinds(result))

    def test_plain_short_sentence_has_no_required_evidence(self):
        result = analyze("Prüfen Sie den Stecker.")
        self.assertEqual(result["evidence"], [])

    def test_all_emitted_rules_exist(self):
        import yaml
        index = yaml.safe_load((ROOT / "rules" / "rule-index.yaml").read_text(encoding="utf-8"))
        valid = {item["id"] for item in index["rules"]}
        result = analyze(
            "Der Stecker sollte geprüft werden, wenn der Sensor aktiv ist, bevor die Pumpe startet. "
            "Verwenden Sie nicht nur die Energieversorgungsunterbrechung. Dazu gehört ein Kabel."
        )
        emitted = rules(result)
        self.assertTrue(emitted <= valid, emitted - valid)


if __name__ == "__main__":
    unittest.main()
