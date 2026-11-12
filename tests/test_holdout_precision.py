import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import holdout_precision  # noqa: E402


class HoldoutPrecisionTests(unittest.TestCase):
    def test_score_computes_precision_without_storing_text(self):
        sheet = {"seed": 1, "positives": [
            {"id": "a", "source": "S", "rule": "STG-1.1", "excerpt": "geheimer Quelltext", "label": "tp"},
            {"id": "b", "source": "S", "rule": "STG-1.1", "excerpt": "geheimer Quelltext", "label": "fp"},
            {"id": "c", "source": "S", "rule": "STG-6.3", "excerpt": "geheimer Quelltext", "label": "extraction"},
        ], "negatives": [{"id": "d", "source": "S", "excerpt": "geheimer Quelltext", "label": "fn"}]}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, "sheet.yaml")
            path.write_text(yaml.safe_dump(sheet, allow_unicode=True), encoding="utf-8")
            out = Path(tmp, "out.yaml")
            with mock.patch.object(holdout_precision, "OUTPUT", out):
                holdout_precision.score(path, "Test")
            text = out.read_text(encoding="utf-8")
        report = yaml.safe_load(text)
        self.assertNotIn("geheimer Quelltext", text)
        self.assertEqual(report["positives"]["precision_excluding_extraction"], 0.5)
        self.assertEqual(report["rules"]["STG-6.3"]["precision_excluding_extraction"], None)
        self.assertEqual(report["negatives"]["missed_violation"], 1)

    def test_published_report_contains_no_source_text(self):
        report = yaml.safe_load((ROOT / "corpus" / "holdout-precision.yaml").read_text(encoding="utf-8"))
        allowed_keys = {"id", "rule", "label"}
        for item in report["labels"]:
            self.assertEqual(set(item), allowed_keys)
            self.assertRegex(item["id"], r"^[0-9a-f]{16}$")
        self.assertEqual(report["positives"]["sampled"], report["positives"]["tp"] + report["positives"]["fp"]
                         + report["positives"]["extraction"])

    def test_sample_refuses_output_inside_repository(self):
        with mock.patch.object(sys, "argv", ["holdout_precision.py", "sample", "--out", str(ROOT / "tmp")]):
            with self.assertRaises(SystemExit):
                holdout_precision.main()


if __name__ == "__main__":
    unittest.main()
