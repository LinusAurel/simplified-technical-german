import json
import subprocess
import sys
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
LINTER = ROOT / "tools" / "stg_lint.py"


def lint(text, profile):
    cp = subprocess.run(
        [sys.executable, str(LINTER), "-", "--format", "json", "--profile", profile],
        input=text,
        text=True,
        capture_output=True,
        check=True,
    )
    return json.loads(cp.stdout)


class ProfileTests(unittest.TestCase):
    def test_profiles_conform_to_schema(self):
        schema = json.loads((ROOT / "schemas" / "profile.schema.json").read_text(encoding="utf-8"))
        profiles = yaml.safe_load((ROOT / "profiles" / "profiles.yaml").read_text(encoding="utf-8"))
        Draft202012Validator(schema).validate(profiles)

    def test_all_profile_rule_ids_exist(self):
        profiles = yaml.safe_load((ROOT / "profiles" / "profiles.yaml").read_text(encoding="utf-8"))["profiles"]
        index = yaml.safe_load((ROOT / "rules" / "rule-index.yaml").read_text(encoding="utf-8"))["rules"]
        valid = {item["id"] for item in index}
        referenced = {rule for profile in profiles.values() for rule in profile["primary_rules"]}
        self.assertTrue(referenced <= valid, sorted(referenced - valid))

    def test_expected_profile_names(self):
        profiles = yaml.safe_load((ROOT / "profiles" / "profiles.yaml").read_text(encoding="utf-8"))["profiles"]
        self.assertEqual(set(profiles), {"procedure", "safety", "description", "requirement", "support", "consumer", "agent"})

    def test_procedure_profile_uses_20_word_limit(self):
        result = lint("Prüfen Sie jetzt alle vorhandenen elektrischen Verbindungen an diesem Gerät sehr sorgfältig auf sichtbare Schäden und lose Kontakte vor dem Start.", "procedure")
        self.assertEqual(result["profile"], "procedure")
        self.assertEqual(result["sentence_word_limit"], 20)
        self.assertEqual(result["text_type"], "procedure")
        self.assertTrue(any(f["rule"] == "STG-5.1" for f in result["findings"]))

    def test_description_profile_uses_25_word_limit(self):
        result = lint("Das System ist aktiv.", "description")
        self.assertEqual(result["sentence_word_limit"], 25)
        self.assertEqual(result["text_type"], "description")

    def test_agent_profile_is_procedural(self):
        result = lint("Öffnen Sie die Datei.", "agent")
        self.assertEqual(result["text_type"], "procedure")
        self.assertIn("single_interpretation", result["profile_priorities"])

    def test_unknown_profile_exits_nonzero(self):
        cp = subprocess.run(
            [sys.executable, str(LINTER), "-", "--profile", "unknown-profile"],
            input="Text.",
            text=True,
            capture_output=True,
        )
        self.assertNotEqual(cp.returncode, 0)
        self.assertIn("Unknown STG-DE profile", cp.stderr)


if __name__ == "__main__":
    unittest.main()
