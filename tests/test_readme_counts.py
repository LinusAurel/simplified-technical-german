"""The counts in README.md are the only place where the project states them.

This test keeps the counts equal to the data, so no second copy of the counts
is necessary.
"""
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(rel):
    return yaml.safe_load((ROOT / rel).read_text(encoding="utf-8"))


def number(text: str) -> int:
    return int(text.replace(".", ""))


class ReadmeCountTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")

    def find(self, pattern: str) -> re.Match:
        match = re.search(pattern, self.readme)
        self.assertIsNotNone(match, f"README.md has no line that matches {pattern!r}")
        return match

    def test_rule_count(self):
        rules = load("rules/rule-index.yaml")["rules"]
        match = self.find(r"\*\*(\d+) Regeln und Empfehlungen\*\*")
        self.assertEqual(number(match.group(1)), len(rules))

    def test_mapping_counts(self):
        mapping = load("mapping/ste100-issue9.yaml")
        match = self.find(r"alle (\d+) Schreibregeln und (\d+) allgemeinen Empfehlungen")
        self.assertEqual(number(match.group(1)), len({m["ste"] for m in mapping["mappings"]}))
        self.assertEqual(number(match.group(2)), len(mapping["general_recommendations"]))

    def test_dictionary_counts(self):
        approved = load("dictionary/approved-words.yaml")["entries"]
        prohibited = load("dictionary/prohibited-words.yaml")["entries"]
        meanings = [m for e in approved for m in e.get("meanings", [])]
        match = self.find(
            r"\*\*(\d+)\*\* zentrale lexikalische Einträge mit \*\*(\d+)\*\* kontrollierten Bedeutungen"
            r" und \*\*(\d+)\*\* verbotene oder prüfpflichtige Wörter"
        )
        self.assertEqual(number(match.group(1)), len(approved))
        self.assertEqual(number(match.group(2)), len(meanings))
        self.assertEqual(number(match.group(3)), len(prohibited))

    def test_corpus_counts(self):
        metrics = load("corpus/fulltext-metrics.yaml")
        match = self.find(r"([\d.]+) Token aus (\d+) öffentlichen Volltextquellen in (\d+) Domänen")
        self.assertEqual(number(match.group(1)), metrics["aggregate"]["tokens"])
        self.assertEqual(number(match.group(2)), metrics["aggregate"]["sources"])
        self.assertEqual(number(match.group(3)), len(metrics["domains"]))


if __name__ == "__main__":
    unittest.main()
