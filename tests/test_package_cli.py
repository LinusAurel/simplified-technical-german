import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PackageCliTests(unittest.TestCase):
    def run_module(self, *args, input_text=None):
        return subprocess.run(
            [sys.executable, "-m", "stg_de.cli", *args],
            cwd=ROOT,
            input=input_text,
            text=True,
            capture_output=True,
        )

    def test_version(self):
        cp = self.run_module("--version")
        self.assertEqual(cp.returncode, 0)
        self.assertIn("stg-de 0.4.0", cp.stdout)

    def test_packaged_lint_uses_embedded_dictionary(self):
        cp = self.run_module("lint", "-", "--format", "json", input_text="Prüfen Sie gegebenenfalls den Stecker.")
        self.assertEqual(cp.returncode, 0, cp.stderr)
        result = json.loads(cp.stdout)
        self.assertTrue(any(f["rule"] == "STG-1.1" for f in result["findings"]))

    def test_packaged_profile_data(self):
        cp = self.run_module("lint", "-", "--format", "json", "--profile", "agent", input_text="Öffnen Sie die Datei.")
        self.assertEqual(cp.returncode, 0, cp.stderr)
        result = json.loads(cp.stdout)
        self.assertEqual(result["profile"], "agent")
        self.assertEqual(result["text_type"], "procedure")

    def test_fail_on_error(self):
        cp = self.run_module("lint", "-", "--fail-on-error", input_text="Öffnen Sie die Datei; prüfen Sie den Inhalt.")
        self.assertEqual(cp.returncode, 1)

    def test_packaged_analyze(self):
        cp = self.run_module("analyze", "-", "--format", "json", input_text="Der Bediener sollte den Stecker prüfen.")
        self.assertEqual(cp.returncode, 0, cp.stderr)
        result = json.loads(cp.stdout)
        self.assertTrue(any(item["kind"] == "ambiguous_modality" for item in result["evidence"]))

    def test_directory_lint(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "a.md").write_text("Prüfen Sie den Stecker.", encoding="utf-8")
            (root / "b.txt").write_text("Öffnen Sie die Datei; prüfen Sie den Inhalt.", encoding="utf-8")
            cp = self.run_module("lint", str(root), "--format", "json")
            self.assertEqual(cp.returncode, 0, cp.stderr)
            payload = json.loads(cp.stdout)
            self.assertEqual(len(payload["results"]), 2)


if __name__ == "__main__":
    unittest.main()
