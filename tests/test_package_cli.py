import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PackageCliTests(unittest.TestCase):
    def run_module(self, *args, input_text=None, cwd=None):
        return subprocess.run([sys.executable, "-m", "stg_de.cli", *args], cwd=cwd or ROOT,
                              input=input_text, text=True, capture_output=True,
                              env={"PYTHONPATH": str(ROOT), "PATH": ""})

    def test_version_matches_release(self):
        import yaml
        version = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))["version"]
        cp = self.run_module("--version")
        self.assertEqual(cp.returncode, 0)
        self.assertEqual(cp.stdout.strip(), f"stg-de {version}")

    def test_help_and_unknown_command(self):
        self.assertIn("compare", self.run_module("--help").stdout)
        self.assertEqual(self.run_module("frobnicate").returncode, 2)

    def test_packaged_lint_uses_embedded_dictionary(self):
        with tempfile.TemporaryDirectory() as tmp:
            cp = self.run_module("lint", "-", "--format", "json", input_text="Prüfen Sie gegebenenfalls den Stecker.", cwd=tmp)
        self.assertEqual(cp.returncode, 0, cp.stderr)
        self.assertTrue(any(f["rule"] == "STG-1.1" for f in json.loads(cp.stdout)["findings"]))

    def test_packaged_profile_and_address(self):
        cp = self.run_module("lint", "-", "--format", "json", "--profile", "agent", "--anrede", "du",
                             input_text="Öffnen Sie die Datei.")
        result = json.loads(cp.stdout)
        self.assertEqual((result["profile"], result["text_type"], result["address"]), ("agent", "procedure", "du"))
        self.assertIn("STG-5.3", {f["rule"] for f in result["findings"]})

    def test_fail_on(self):
        cp = self.run_module("lint", "-", "--fail-on", "error", input_text="Öffnen Sie die Datei; prüfen Sie den Inhalt.")
        self.assertEqual(cp.returncode, 1)

    def test_packaged_analyze(self):
        cp = self.run_module("analyze", "-", "--format", "json", input_text="Der Bediener sollte den Stecker prüfen.")
        self.assertEqual(cp.returncode, 0, cp.stderr)
        self.assertTrue(any(item["kind"] == "ambiguous_modality" for item in json.loads(cp.stdout)["evidence"]))

    def test_packaged_compare(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp, "a.txt")
            src.write_text("Stellen Sie 2 bar ein.", encoding="utf-8")
            cp = self.run_module("compare", str(src), "-", "--format", "json", input_text="Stellen Sie den Druck ein.")
        self.assertEqual(json.loads(cp.stdout)["result"], "FAIL")

    def test_directory_lint(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "a.md").write_text("Prüfen Sie den Stecker.", encoding="utf-8")
            (root / "b.txt").write_text("Öffnen Sie die Datei; prüfen Sie den Inhalt.", encoding="utf-8")
            payload = json.loads(self.run_module("lint", str(root), "--format", "json").stdout)
            self.assertEqual(len(payload["files"]), 2)

    def test_package_copies_are_in_sync(self):
        cp = subprocess.run([sys.executable, str(ROOT / "tools" / "sync_package.py"), "--check"], capture_output=True, text=True)
        self.assertEqual(cp.returncode, 0, cp.stdout)


if __name__ == "__main__":
    unittest.main()
