import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class RuleTitleTests(unittest.TestCase):
    def test_every_rule_heading_matches_rule_index(self):
        index = yaml.safe_load((ROOT / "rules" / "rule-index.yaml").read_text(encoding="utf-8"))["rules"]
        for rule in index:
            text = (ROOT / rule["file"]).read_text(encoding="utf-8")
            self.assertIn(f"## {rule['id']} — {rule['title']}\n", text, rule["id"])


if __name__ == "__main__":
    unittest.main()
