import json
import re
import sys
import unittest
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "simplified-technical-german"
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "stg_de"))


def release_version():
    return yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))["version"]


def frontmatter():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return yaml.safe_load(match.group(1))


class PackagingTests(unittest.TestCase):
    def test_versions_are_consistent(self):
        version = release_version()
        plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(plugin["version"], version)
        self.assertEqual(market["plugins"][0]["version"], version)
        import re as _re
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertEqual(_re.search(r'^version = "([^"]+)"', pyproject, _re.M).group(1), version)
        self.assertIn(f'__version__ = "{version}"', (ROOT / "stg_de" / "__init__.py").read_text(encoding="utf-8"))
        import stg_compare
        import stg_lint
        self.assertEqual(stg_lint.STG_VERSION, version)
        self.assertEqual(stg_compare.STG_VERSION, version)
        for rel in ["rules/rule-index.yaml", "dictionary/approved-words.yaml", "dictionary/prohibited-words.yaml"]:
            self.assertEqual(str(yaml.safe_load((ROOT / rel).read_text(encoding="utf-8"))["release"]), version, rel)

    def test_marketplace_entry_matches_plugin(self):
        plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        entry = market["plugins"][0]
        self.assertEqual(entry["name"], plugin["name"])
        self.assertEqual(entry["source"], "./")
        self.assertNotIn(market["name"], {"claude-plugins-official", "anthropic-plugins"})

    def test_codex_plugin_manifest(self):
        claude = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        codex = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(codex["name"], claude["name"])
        self.assertEqual(codex["version"], release_version())
        skills_dir = (ROOT / codex["skills"]).resolve()
        self.assertTrue((skills_dir / SKILL.name / "SKILL.md").is_file())
        interface = codex["interface"]
        for key in ("displayName", "shortDescription", "longDescription", "developerName", "category", "defaultPrompt"):
            self.assertTrue(interface.get(key), key)
        self.assertIsInstance(interface["defaultPrompt"], list)
        # Only plugin.json belongs inside .codex-plugin/.
        self.assertEqual(sorted(p.name for p in (ROOT / ".codex-plugin").iterdir()), ["plugin.json"])

    def test_codex_marketplace_entry(self):
        market = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
        codex = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        entry = market["plugins"][0]
        self.assertEqual(entry["name"], codex["name"])
        self.assertEqual(entry["source"]["source"], "local")
        plugin_root = (ROOT / entry["source"]["path"]).resolve()
        self.assertTrue((plugin_root / ".codex-plugin" / "plugin.json").is_file())
        self.assertIn(entry["policy"]["installation"], {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"})
        self.assertNotIn(market["name"], {"openai-curated"})

    def test_openai_yaml_follows_codex_conventions(self):
        text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        meta = yaml.safe_load(text)["interface"]
        self.assertTrue(25 <= len(meta["short_description"]) <= 64, len(meta["short_description"]))
        self.assertIn(f"${SKILL.name}", meta["default_prompt"])
        for key in ("display_name", "short_description", "default_prompt"):
            self.assertRegex(text, rf'{key}: "[^"]+"', f"{key} must be a quoted string")

    def test_skill_frontmatter_follows_agent_skills_spec(self):
        meta = frontmatter()
        self.assertEqual(meta["name"], SKILL.name)
        self.assertRegex(meta["name"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(meta["name"]), 64)
        self.assertLessEqual(len(meta["description"]), 1024)
        self.assertNotRegex(meta["description"], r"[<>]")

    def test_skill_body_stays_compact(self):
        words = len((SKILL / "SKILL.md").read_text(encoding="utf-8").split())
        self.assertLess(words, 2500, "Move detail into references/ to keep SKILL.md loadable")

    def test_skill_files_referenced_by_skill_md_exist(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        for rel in set(re.findall(r"`((?:references|scripts)/[\w.-]+)`", text)):
            self.assertTrue((SKILL / rel).is_file(), rel)

    def test_manifest_lists_only_tracked_files(self):
        import subprocess
        tracked = set(subprocess.run(["git", "ls-files"], cwd=ROOT, check=True, capture_output=True,
                                     text=True).stdout.splitlines())
        manifest = yaml.safe_load((ROOT / "manifest.yaml").read_text(encoding="utf-8"))
        untracked = [item["path"] for item in manifest["files"] if item["path"] not in tracked]
        self.assertEqual(untracked, [], "manifest.yaml lists files that a release checkout does not contain")

    def test_release_zip_layout(self):
        import package_skill
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            target = package_skill.build(Path(tmp))
            names = zipfile.ZipFile(target).namelist()
            self.assertIn("simplified-technical-german/SKILL.md", names)
            self.assertIn("simplified-technical-german/scripts/stg_markdown.py", names)
            self.assertTrue(all(n.startswith("simplified-technical-german/") for n in names))
            self.assertFalse(any("__pycache__" in n for n in names))


if __name__ == "__main__":
    unittest.main()
