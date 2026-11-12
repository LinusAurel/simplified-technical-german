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


class SuppressionTests(unittest.TestCase):
    def test_lint_off_region_is_ignored_and_lines_are_kept(self):
        text = "<!-- stg-lint: off -->\n> Man prüft das; fertig.\n<!-- stg-lint: on -->\nMan prüft den Stecker.\n"
        result = audit_text(text, ROOT)
        self.assertEqual([(f["rule"], f["line"]) for f in result["findings"]], [("STG-DE-4.3", 4)])


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
