import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from stg_lint import audit_text, prose_blocks  # noqa: E402


def rules(text, **kw):
    return [f["rule"] for f in audit_text(text, ROOT, **kw)["findings"]]


class MarkdownTests(unittest.TestCase):
    def test_fenced_code_is_ignored(self):
        text = "Prüfen Sie das Gerät.\n\n```bash\nman ls; echo ok\n```\n"
        self.assertEqual(rules(text), [])

    def test_list_items_and_headings_are_separate_sentences(self):
        items = "\n".join(f"- Prüfen Sie den Anschluss Nummer {i} am Gerät" for i in range(10))
        text = f"# Prüfung der Anschlüsse am Gerät\n\n{items}\n"
        self.assertNotIn("STG-5.1", rules(text, profile="procedure"))
        self.assertEqual(len(prose_blocks(text)), 11)

    def test_table_cells_are_separate_blocks(self):
        text = "| Regel | Beschreibung |\n|---|---|\n| A | Prüfen Sie den Druck. |\n"
        self.assertEqual(prose_blocks(text), ["Regel", "Beschreibung", "A", "Prüfen Sie den Druck."])

    def test_violation_inside_list_item_is_still_found(self):
        text = "1. Man prüft den Stecker.\n2. Prüfen Sie den Druck.\n"
        self.assertEqual(rules(text), ["STG-DE-4.3"])

    def test_semicolon_in_inline_code_is_ignored(self):
        self.assertEqual(rules("Geben Sie `a; b` ein.\n"), [])

    def test_html_comment_is_ignored(self):
        self.assertEqual(rules("<!-- man; -->\nPrüfen Sie das Gerät.\n"), [])


class HoldoutRegressionTests(unittest.TestCase):
    """Linter weaknesses found by the holdout precision measurement (corpus/holdout-precision.yaml)."""

    def test_abbreviations_and_ordinal_dates_do_not_end_sentences(self):
        from stg_markdown import split_sentences
        text = ("Teilen Sie den Stand dem neuen Strom- bzw. Gasanbieter mit. Das ist z. B. wichtig. "
                "Siehe Abb. 3 und Nr. 5. Max. 5 bar sind erlaubt. Lieferung zum 31. Dezember. Sprache usw. Die Auswahl gilt.")
        self.assertEqual(split_sentences(text), [
            "Teilen Sie den Stand dem neuen Strom- bzw. Gasanbieter mit.", "Das ist z. B. wichtig.",
            "Siehe Abb. 3 und Nr. 5.", "Max. 5 bar sind erlaubt.", "Lieferung zum 31. Dezember.",
            "Sprache usw.", "Die Auswahl gilt."])

    def test_plain_text_bullets_are_list_items(self):
        self.assertEqual(prose_blocks("Einleitung.\n• Punkt eins\n‣ Punkt zwei\n→ Menü"),
                         ["Einleitung.", "Punkt eins", "Punkt zwei", "Menü"])
        items = "\n".join(f"• Prüfen Sie den Anschluss Nummer {i} am Gerät sorgfältig" for i in range(6))
        self.assertNotIn("STG-6.3", rules(items))

    def test_inflected_prohibited_adjectives_are_found(self):
        found = {f["term"] for f in audit_text("Das sind einfache Tipps zu Ihrem aktuellen Vertrag.", ROOT)["findings"]}
        self.assertTrue({"aktuell", "einfach"} <= found)
        self.assertNotIn("weiter", {f["term"] for f in audit_text("Alle weiteren Sprachen sind Übersetzungen.", ROOT)["findings"]})


class SuppressionTests(unittest.TestCase):
    def test_lint_off_region_is_ignored_and_lines_are_kept(self):
        text = "<!-- stg-lint: off -->\n> Man prüft das; fertig.\n<!-- stg-lint: on -->\nMan prüft den Stecker.\n"
        result = audit_text(text, ROOT)
        self.assertEqual([(f["rule"], f["line"]) for f in result["findings"]], [("STG-DE-4.3", 4)])


class FrontMatterTests(unittest.TestCase):
    def test_yaml_front_matter_is_ignored_and_lines_are_kept(self):
        text = "---\nname: x\ndescription: man; one two\n---\n\nMan prüft den Stecker.\n"
        self.assertEqual([(f["rule"], f["line"]) for f in audit_text(text, ROOT)["findings"]], [("STG-DE-4.3", 6)])


class PromptSnippetTests(unittest.TestCase):
    def test_agents_md_snippets_comply_with_agent_profile(self):
        doc = (ROOT / "prompts" / "agents-md.md").read_text(encoding="utf-8")
        snippets = re.findall(r"```markdown\n(.*?)```", doc, re.S)
        self.assertEqual(len(snippets), 2)
        for snippet in [doc] + snippets:
            result = audit_text(snippet, ROOT, profile="agent")
            errors = [f for f in result["findings"] if f["severity"] == "error"]
            self.assertEqual(errors, [], snippet[:80])


if __name__ == "__main__":
    unittest.main()
