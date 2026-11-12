import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from run_evals import prompt_for, score_case  # noqa: E402

CASES = {c["id"]: c for c in yaml.safe_load((ROOT / "evals" / "cases.yaml").read_text(encoding="utf-8"))["cases"]}


class EvalSuiteTests(unittest.TestCase):
    def test_reference_outputs_pass_every_check(self):
        for case_id, case in CASES.items():
            output = (ROOT / "evals" / "reference" / f"{case_id}.md").read_text(encoding="utf-8")
            result = score_case(case, output)
            self.assertTrue(result["ok"], (case_id, result["checks"], result["details"]))

    def test_cases_cover_all_operations_and_profiles(self):
        self.assertEqual({c["operation"] for c in CASES.values()}, {"WRITE", "REWRITE", "AUDIT"})
        profiles = yaml.safe_load((ROOT / "profiles" / "profiles.yaml").read_text(encoding="utf-8"))["profiles"]
        names = set(profiles) if isinstance(profiles, dict) else {p["id"] for p in profiles}
        self.assertEqual({c["profile"] for c in CASES.values()}, names)

    def test_negative_controls_fail(self):
        bad = {
            "rewrite-procedure-housing": "Hier ist der Text:\nMan zieht den Netzstecker; dann löst man die Schrauben am Gehäuse.",
            "rewrite-support-password": "Klicken Sie auf „Passwort zurücksetzen“. Der Link ist 12 Stunden gültig.",
            "rewrite-requirement-vague-time": "Das System muss Anfragen innerhalb von 2 s im Protokoll beantworten.",
            "rewrite-already-compliant": "1. Schalten Sie das Gerät aus.\n2. Ziehen Sie den Stecker.\n3. Warten Sie 5 Minuten.",
            "audit-violations": "Ergebnis: PASS",
            "rewrite-consumer-keeps-du": "Wenn Sie Ihren Zählerstand melden, senden Sie ein Foto vom Zähler mit.",
            "rewrite-requirement-ears-overvoltage": "Die Steuerung muss bei mehr als 30 V den Ausgang in 10 ms abschalten und ggf. einen Log-Eintrag schreiben.",
            "rewrite-vulnerability-notice": "Eine Schwachstelle betrifft Versionen vor 3.2.0. Aktualisieren Sie auf Version 3.2.0.",
            "rewrite-safety-requirement-sil": "SF-02 (SIL 2) muss in 50 ms den sicheren Zustand herstellen.",
            "audit-requirement-iot": "Ergebnis: PASS WITH REVIEW",
        }
        for case_id, output in bad.items():
            self.assertFalse(score_case(CASES[case_id], output)["ok"], case_id)

    def test_prompts_name_operation_and_profile(self):
        prompt = prompt_for(CASES["audit-violations"])
        self.assertIn("AUDIT", prompt)
        self.assertIn("`procedure`", prompt)


if __name__ == "__main__":
    unittest.main()
