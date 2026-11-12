import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from stg_compare import compare  # noqa: E402

SOURCE = ("WARNUNG: Sie müssen die Stromversorgung ausschalten, bevor Sie die Abdeckung öffnen. "
          "Stellen Sie den Druck auf 2,5 bar ein. Klicken Sie auf „Speichern“. "
          "Der Motor darf nicht über 80 °C laufen. Sie können optional den Filter X-200 tauschen.")


def checks(result, severity=None):
    return {f["check"] for f in result["findings"] if severity is None or f["severity"] == severity}


class CompareTests(unittest.TestCase):
    def test_faithful_rewrite_passes(self):
        rewrite = SOURCE.replace("Sie müssen die Stromversorgung ausschalten", "Schalten Sie die Stromversorgung aus") \
                        .replace("2,5", "2.5")
        result = compare(SOURCE, rewrite)
        self.assertEqual(result["result"], "PASS", result["findings"])

    def test_number_words_and_decimal_separators_are_normalized(self):
        self.assertEqual(compare("Ziehen Sie zwei Schrauben an.", "Ziehen Sie 2 Schrauben an.")["result"], "PASS")
        self.assertEqual(compare("Der Wert ist 1.500 W.", "Der Wert ist 1500 W.")["result"], "PASS")

    def test_lost_or_changed_protected_content_fails(self):
        rewrite = ("Schalten Sie die Stromversorgung aus. Öffnen Sie die Abdeckung. Stellen Sie den Druck auf 25 bar ein. "
                   "Klicken Sie auf „Sichern“. Der Motor läuft bis 80 °F. Tauschen Sie den Filter.")
        result = compare(SOURCE, rewrite)
        self.assertEqual(result["result"], "FAIL")
        self.assertTrue({"numbers", "units", "quoted_text", "identifiers", "safety_signal"} <= checks(result, "fail"))

    def test_identifier_digits_are_not_counted_as_numbers(self):
        result = compare("Tauschen Sie den Filter X-200.", "Tauschen Sie den Filter.")
        self.assertIn("identifiers", checks(result, "fail"))
        self.assertNotIn("numbers", checks(result))

    def test_meaning_shifts_are_review_not_fail(self):
        rewrite = ("WARNUNG: Schalten Sie die Stromversorgung aus. Öffnen Sie die Abdeckung. Stellen Sie den Druck auf 2,5 bar ein. "
                   "Klicken Sie auf „Speichern“. Der Motor läuft über 80 °C. Tauschen Sie den Filter X-200.")
        result = compare(SOURCE, rewrite)
        self.assertEqual(result["result"], "REVIEW")
        self.assertTrue({"prohibition", "modality", "negation", "conditions"} <= checks(result, "review"))

    def test_requirement_to_imperative_is_not_flagged(self):
        result = compare("Sie müssen den Stecker ziehen.", "Ziehen Sie den Stecker.")
        self.assertEqual(result["result"], "PASS", result["findings"])

    def test_weakened_requirement_is_flagged(self):
        result = compare("Sie müssen den Stecker ziehen.", "Sie sollten den Stecker ziehen.")
        self.assertIn("modality", checks(result, "review"))

    def test_added_numbers_are_review(self):
        result = compare("Warten Sie kurz.", "Warten Sie 5 s.")
        self.assertEqual(result["result"], "REVIEW")

    def test_code_and_urls_must_survive(self):
        result = compare("Führen Sie `make test` aus. Lesen Sie https://example.org/doku.", "Führen Sie die Tests aus.")
        self.assertTrue({"code", "urls"} <= checks(result, "fail"))

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, new = Path(tmp, "a.txt"), Path(tmp, "b.txt")
            src.write_text("Stellen Sie 2 bar ein.", encoding="utf-8")
            new.write_text("Stellen Sie den Druck ein.", encoding="utf-8")
            tool = str(ROOT / "tools" / "stg_compare.py")
            cp = subprocess.run([sys.executable, tool, str(src), str(new), "--format", "json", "--fail-on", "fail"],
                                capture_output=True, text=True)
            self.assertEqual(cp.returncode, 1)
            self.assertEqual(json.loads(cp.stdout)["result"], "FAIL")
            cp = subprocess.run([sys.executable, tool, str(src), str(src), "--fail-on", "review"], capture_output=True, text=True)
            self.assertEqual(cp.returncode, 0)


if __name__ == "__main__":
    unittest.main()
