import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MAPPING = ROOT / "mapping" / "ste100-issue9.yaml"

# ASD-STE100 Issue 9 has 53 writing rules in nine sections.
EXPECTED_RULES_PER_SECTION = {1: 14, 2: 2, 3: 7, 4: 5, 5: 5, 6: 6, 7: 3, 8: 7, 9: 4}
RELATIONS = {"equivalent", "adapted", "replaced"}


def load():
    return yaml.safe_load(MAPPING.read_text(encoding="utf-8"))


def stg_ids():
    index = yaml.safe_load((ROOT / "rules" / "rule-index.yaml").read_text(encoding="utf-8"))
    return {rule["id"] for rule in index["rules"]}


class Ste100MappingTests(unittest.TestCase):
    def test_all_53_issue9_rules_are_mapped_once(self):
        data = load()
        expected = [f"{s}.{n}" for s, count in EXPECTED_RULES_PER_SECTION.items() for n in range(1, count + 1)]
        mapped = [m["ste"] for m in data["mappings"]]
        self.assertEqual(len(mapped), len(set(mapped)), "duplicate ASD-STE100 rule in mapping")
        self.assertEqual(sorted(mapped), sorted(expected))
        self.assertEqual(data["source"]["writing_rule_count"], 53)

    def test_all_general_recommendations_are_mapped(self):
        data = load()
        self.assertEqual([m["ste"] for m in data["general_recommendations"]], [f"GR-{i}" for i in range(1, 9)])

    def test_mapping_targets_exist_and_relations_are_known(self):
        data = load()
        known = stg_ids()
        for item in data["mappings"] + data["general_recommendations"]:
            self.assertIn(item["relation"], RELATIONS, item["ste"])
            self.assertTrue(item["stg"], item["ste"])
            for rule_id in item["stg"] + item.get("related", []):
                self.assertIn(rule_id, known, f"{item['ste']} -> unknown {rule_id}")
            self.assertTrue(item.get("note"), item["ste"])

    def test_every_stg_rule_is_traceable(self):
        data = load()
        traced = set()
        for item in data["mappings"] + data["general_recommendations"]:
            traced |= set(item["stg"]) | set(item.get("related", []))
        traced |= {item["stg"] for item in data["german_extensions"]}
        self.assertEqual(traced, stg_ids())

    def test_german_extensions_are_stg_de_rules(self):
        data = load()
        for item in data["german_extensions"]:
            self.assertTrue(item["stg"].startswith("STG-DE-"), item["stg"])
            self.assertTrue(item["reason"])

    def test_numbered_stg_rules_follow_ste_numbering(self):
        # STG-x.y deliberately reuses the ASD-STE100 rule number x.y.
        for item in load()["mappings"]:
            self.assertEqual(item["stg"][0], f"STG-{item['ste']}")


if __name__ == "__main__":
    unittest.main()
