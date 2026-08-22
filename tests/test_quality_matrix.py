import json
import subprocess
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LINTER = ROOT / "tools" / "stg_lint.py"


class RuleMatrixTests(unittest.TestCase):
    def test_matrix_covers_every_published_rule_exactly_once(self):
        index = yaml.safe_load((ROOT / "rules" / "rule-index.yaml").read_text(encoding="utf-8"))
        matrix = yaml.safe_load((ROOT / "quality" / "rule-coverage.yaml").read_text(encoding="utf-8"))
        published = [item["id"] for item in index["rules"]]
        covered = [item["id"] for item in matrix["rules"]]
        self.assertEqual(len(covered), len(set(covered)), "Duplicate rule IDs in quality/rule-coverage.yaml")
        self.assertEqual(set(covered), set(published))
        self.assertEqual(len(covered), 75)

    def test_matrix_uses_known_classes(self):
        matrix = yaml.safe_load((ROOT / "quality" / "rule-coverage.yaml").read_text(encoding="utf-8"))
        allowed = {"deterministic", "partial", "heuristic", "semantic", "human-review"}
        self.assertTrue(all(item["class"] in allowed for item in matrix["rules"]))

    def test_golden_audits(self):
        suite = yaml.safe_load((ROOT / "examples" / "golden-audits.yaml").read_text(encoding="utf-8"))
        for case in suite["cases"]:
            cp = subprocess.run(
                [
                    sys.executable,
                    str(LINTER),
                    "-",
                    "--format",
                    "json",
                    "--text-type",
                    case["text_type"],
                ],
                input=case["text"],
                text=True,
                capture_output=True,
                check=True,
            )
            result = json.loads(cp.stdout)
            emitted = {finding["rule"] for finding in result["findings"]}
            with self.subTest(case=case["id"]):
                self.assertEqual(result["result"], case["expected_result"])
                self.assertEqual(emitted, set(case["expected_rules"]))


if __name__ == "__main__":
    unittest.main()
