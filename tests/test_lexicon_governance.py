import unittest
from pathlib import Path

import json
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "lexicon-proposal.schema.json"
TEMPLATE = ROOT / "dictionary" / "proposals" / "TEMPLATE.yaml"


class LexiconGovernanceTests(unittest.TestCase):
    def test_template_conforms_to_schema(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        proposal = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
        Draft202012Validator(schema).validate(proposal)

    def test_schema_rejects_unknown_action(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        proposal = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
        proposal["action"] = "make_it_common"
        errors = list(Draft202012Validator(schema).iter_errors(proposal))
        self.assertTrue(errors)

    def test_schema_requires_evidence_and_decision(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        proposal = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
        proposal.pop("evidence")
        proposal.pop("decision")
        errors = list(Draft202012Validator(schema).iter_errors(proposal))
        missing = " ".join(error.message for error in errors)
        self.assertIn("evidence", missing)
        self.assertIn("decision", missing)


if __name__ == "__main__":
    unittest.main()
