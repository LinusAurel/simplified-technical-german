import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINTER = ROOT / "stg_de" / "stg_lint.py"


def cli(*args, text=None, cwd=None):
    return subprocess.run([sys.executable, str(LINTER), *args], input=text, text=True,
                          capture_output=True, cwd=cwd)


class LintCliTests(unittest.TestCase):
    def test_man_is_reported_once(self):
        cp = cli("-", "--format", "json", text="Man prüft den Stecker.")
        findings = json.loads(cp.stdout)["findings"]
        self.assertEqual([f["rule"] for f in findings if f.get("term") == "man"], ["STG-DE-4.3"])

    def test_findings_carry_line_numbers(self):
        cp = cli("-", "--format", "json", text="Prüfen Sie das Gerät.\n\nMan prüft den Stecker.\n")
        finding = json.loads(cp.stdout)["findings"][0]
        self.assertEqual(finding["line"], 3)

    def test_fail_on_thresholds(self):
        review_only = "Wählen Sie die Option A und/oder B."
        self.assertEqual(cli("-", text=review_only).returncode, 0)
        self.assertEqual(cli("-", "--fail-on", "error", text=review_only).returncode, 0)
        self.assertEqual(cli("-", "--fail-on", "warning", text=review_only).returncode, 1)
        self.assertEqual(cli("-", "--fail-on-error", text="Man prüft den Stecker.").returncode, 1)

    def test_directory_input_and_aggregate_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "a.md").write_text("Prüfen Sie das Gerät.\n", encoding="utf-8")
            Path(tmp, "b.txt").write_text("Man prüft den Stecker.\n", encoding="utf-8")
            Path(tmp, "ignored.yaml").write_text("x: 1\n", encoding="utf-8")
            cp = cli(tmp, "--format", "json")
            data = json.loads(cp.stdout)
            self.assertEqual(data["result"], "FAIL")
            self.assertEqual(sorted(Path(r["path"]).name for r in data["files"]), ["a.md", "b.txt"])

    def test_github_annotations(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = Path(tmp, "doc.md")
            doc.write_text("Prüfen Sie das Gerät.\nMan prüft den Stecker.\n", encoding="utf-8")
            cp = cli(str(doc), "--format", "github")
            self.assertIn(f"::error file={doc},line=2,title=STG-DE-4.3::", cp.stdout)

    def test_project_file_is_loaded_from_working_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, ".stg-de.yaml").write_text(
                "preferred_terms:\n  - preferred: Steuergerät\n    avoid: [Controller]\n", encoding="utf-8")
            cp = cli("-", "--format", "json", text="Prüfen Sie den Controller.", cwd=tmp)
            self.assertIn("STG-9.4", {f["rule"] for f in json.loads(cp.stdout)["findings"]})
            cp = cli("-", "--format", "json", "--no-project", text="Prüfen Sie den Controller.", cwd=tmp)
            self.assertNotIn("STG-9.4", {f["rule"] for f in json.loads(cp.stdout)["findings"]})


if __name__ == "__main__":
    unittest.main()


class LexicalContextTests(unittest.TestCase):
    def test_lexical_finding_carries_sentence_and_count(self):
        cp = cli("-", "--format", "json", text="Das Gerät ist aktuell aus.\n\nPrüfen Sie aktuell den Druck.\n")
        finding = [f for f in json.loads(cp.stdout)["findings"] if f.get("term") == "aktuell"][0]
        self.assertEqual(finding["original"], "Das Gerät ist aktuell aus.")
        self.assertEqual((finding["occurrences"], finding["line"]), (2, 1))


class PlatformRegressionTests(unittest.TestCase):
    """Regressions found by running the linter on a real German monorepo."""

    def test_wrapped_sentence_gets_line_number(self):
        text = ("Erste Zeile.\n\nDer Job startet um 3 Uhr und schreibt danach die Ergebnisse in die Datenbank, damit\n"
                "der Bericht am Morgen bereit ist und alle Teams die Zahlen ohne weiteren Schritt sehen können.\n")
        cp = cli("-", "--format", "json", "--profile", "procedure", text=text)
        finding = json.loads(cp.stdout)["findings"][0]
        self.assertEqual((finding["rule"], finding["line"]), ("STG-5.1", 3))

    def test_project_technical_verb_overrides_central_prohibited_list(self):
        text = "Die Jobs laufen jede Nacht."
        self.assertIn("laufen", {f.get("term") for f in json.loads(cli("-", "--format", "json", text=text).stdout)["findings"]})
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, ".stg-de.yaml").write_text(
                "technical_verbs:\n  - term: laufen\n    definition: Software wird ausgeführt\n", encoding="utf-8")
            cp = cli("-", "--format", "json", text=text, cwd=tmp)
            self.assertEqual(json.loads(cp.stdout)["findings"], [])
