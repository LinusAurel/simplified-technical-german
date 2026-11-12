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

    def test_score_ignores_skipped_items_and_uses_sheet_sources(self):
        sheet = {"seed": 1, "linter": "0.6.0", "sources": [{"id": "OLD", "sha256": "x"}], "positives": [
            {"id": "a", "source": "OLD", "rule": "STG-1.1", "excerpt": "t", "label": "tp"},
            {"id": "b", "source": "OLD", "rule": "STG-1.1", "excerpt": "t", "label": "skip"},
        ], "negatives": [{"id": "c", "source": "OLD", "excerpt": "t", "label": "skip"}]}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, "sheet.yaml")
            path.write_text(yaml.safe_dump(sheet), encoding="utf-8")
            out = Path(tmp, "out.yaml")
            with mock.patch.object(holdout_precision, "OUTPUT", out):
                holdout_precision.score(path, "Test")
            report = yaml.safe_load(out.read_text(encoding="utf-8"))
        self.assertEqual(report["sources"], ["OLD"])
        self.assertEqual(report["linter"], "0.6.0")
        self.assertEqual(report["positives"]["sampled"], 1)
        self.assertEqual(report["negatives"]["sampled"], 0)

    def test_sample_never_counts_a_sentence_with_a_reported_term_as_clean(self):
        # "ggf." occurs twice. The linter reports the term once, with the first sentence.
        text = ("Prüfen Sie ggf. den Druck im System. Öffnen Sie ggf. das Ventil am Gerät. "
                "Schließen Sie das Ventil am Gerät.")
        source = {"id": "S", "partition": "holdout", "type": "text", "url": "u"}
        with tempfile.TemporaryDirectory() as tmp, \
                mock.patch.object(holdout_precision, "holdout_sources", return_value=[source]), \
                mock.patch.object(holdout_precision, "download", return_value=(text.encode(), "text/plain")):
            holdout_precision.sample(Path(tmp), per_source=10, negatives=10)
            sheet = yaml.safe_load(Path(tmp, "holdout-labels.yaml").read_text(encoding="utf-8"))
        clean = [x["excerpt"] for x in sheet["negatives"]]
        self.assertEqual(clean, ["Schließen Sie das Ventil am Gerät."])
        self.assertEqual(sheet["sources"][0]["id"], "S")

    def test_sample_refuses_output_inside_repository(self):
        with mock.patch.object(sys, "argv", ["holdout_precision.py", "sample", "--out", str(ROOT / "tmp")]):
            with self.assertRaises(SystemExit):
                holdout_precision.main()


if __name__ == "__main__":
    unittest.main()
