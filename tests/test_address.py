import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from stg_lint import audit_text  # noqa: E402

LINTER = ROOT / "tools" / "stg_lint.py"


def address(text, form=None, project=None):
    return [(f["severity"], f["line"]) for f in audit_text(text, ROOT, project=project, address=form)["findings"]
            if f["rule"] == "STG-5.3"]


class AddressTests(unittest.TestCase):
    def test_undeclared_single_form_passes(self):
        self.assertEqual(address("Prüfen Sie den Druck. Schließen Sie das Ventil."), [])
        self.assertEqual(address("Prüfe den Druck. Wenn du fertig bist, schließe das Ventil."), [])
        self.assertEqual(address("Druck prüfen. Ventil schließen."), [])

    def test_undeclared_mixed_forms_warn_once(self):
        found = address("Wir senden Ihnen eine E-Mail.\nSparst du nichts, zahlst du nichts.")
        self.assertEqual(found, [("warning", 2)])

    def test_declared_form_makes_other_form_an_error(self):
        self.assertEqual(address("Prüfe den Druck. Wenn du fertig bist, schließe das Ventil.", "sie"), [("error", 1)])
        self.assertEqual(address("Prüfen Sie den Druck.", "du"), [("error", 1)])
        self.assertEqual(address("Druck prüfen. Prüfen Sie das Ventil.", "infinitiv"), [("error", 1)])

    def test_third_person_sie_is_not_formal_address(self):
        self.assertEqual(address("Die Jobs starten, wenn sie bereit sind. Sie laufen nachts.", "du"), [])

    def test_quoted_and_code_text_is_ignored(self):
        self.assertEqual(address("Schreibe nicht „Prüfen Sie“ in die Vorlage.", "du"), [])

    def test_project_setting_and_cli(self):
        self.assertEqual(address("Prüfen Sie den Druck.", project={"anrede": "du"}), [("error", 1)])
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, ".stg-de.yaml").write_text("anrede: du\n", encoding="utf-8")
            cp = subprocess.run([sys.executable, str(LINTER), "-", "--format", "json"], input="Prüfen Sie den Druck.",
                                text=True, capture_output=True, cwd=tmp)
            data = json.loads(cp.stdout)
            self.assertEqual(data["address"], "du")
            self.assertIn("STG-5.3", {f["rule"] for f in data["findings"]})
            cp = subprocess.run([sys.executable, str(LINTER), "-", "--format", "json", "--anrede", "sie"],
                                input="Prüfen Sie den Druck.", text=True, capture_output=True, cwd=tmp)
            self.assertNotIn("STG-5.3", {f["rule"] for f in json.loads(cp.stdout)["findings"]})

    def test_unknown_form_is_rejected(self):
        with self.assertRaises(ValueError):
            audit_text("Text.", ROOT, project={"anrede": "ihr"})


class ProjectSchemaTests(unittest.TestCase):
    def test_example_project_file_matches_schema(self):
        import jsonschema
        import yaml
        schema = json.loads((ROOT / "schemas" / "project.schema.json").read_text(encoding="utf-8"))
        example = yaml.safe_load((ROOT / ".stg-de.example.yaml").read_text(encoding="utf-8"))
        jsonschema.validate(example, schema)
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate({"anrede": "ihr"}, schema)

    def test_example_glossaries_match_schema_and_keep_prohibited_words(self):
        import jsonschema
        import yaml
        schema = json.loads((ROOT / "schemas" / "project.schema.json").read_text(encoding="utf-8"))
        prohibited = yaml.safe_load((ROOT / "dictionary" / "prohibited-words.yaml").read_text(encoding="utf-8"))
        banned = {str(e.get("term") or e.get("lemma") or e.get("word")).casefold()
                  for e in (prohibited.get("entries") or prohibited.get("terms") or [])}
        files = sorted((ROOT / "examples" / "glossaries").glob("*.stg-de.yaml"))
        self.assertGreaterEqual(len(files), 4)
        for path in files:
            glossary = yaml.safe_load(path.read_text(encoding="utf-8"))
            jsonschema.validate(glossary, schema)
            terms = [t["term"] if isinstance(t, dict) else t
                     for key in ("technical_nouns", "technical_verbs") for t in glossary.get(key, [])]
            terms += glossary.get("protected_terms", []) + [x["preferred"] for x in glossary.get("preferred_terms", [])]
            # A glossary term overrides the central prohibited list. Examples must not do that.
            self.assertFalse([t for t in terms if t.casefold() in banned], path.name)


if __name__ == "__main__":
    unittest.main()
