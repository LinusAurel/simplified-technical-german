import json
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def load_schema(name):
    return Draft202012Validator(json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8")))


class SchemaTests(unittest.TestCase):
    def test_dictionary_conforms_to_schema(self):
        data = yaml.safe_load((ROOT / "dictionary" / "approved-words.yaml").read_text(encoding="utf-8"))
        load_schema("dictionary-entry.schema.json").validate(data)

    def test_rule_index_conforms_to_schema(self):
        validator = load_schema("rule.schema.json")
        rules = yaml.safe_load((ROOT / "rules" / "rule-index.yaml").read_text(encoding="utf-8"))["rules"]
        for rule in rules:
            with self.subTest(rule=rule["id"]):
                validator.validate(rule)


if __name__ == "__main__":
    unittest.main()
