import unittest

from textnode import TextNode, TextType
from convert import text_to_textnodes

class TestConvert(unittest.TestCase):
    def test_no_markdown(self):
        text = "This is a simple text."
        result = text_to_textnodes(text)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This is a simple text.")

    def test_bold_markdown(self):
        text = "This is a **bold** text."
        result = text_to_textnodes(text)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is a ")
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[2].text, " text.")
        self.assertEqual(result[1].text_type, TextType.BOLD_TEXT)

    def test_italic_markdown(self):
        text = "This is an _italic_ text."
        result = text_to_textnodes(text)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is an ")
        self.assertEqual(result[1].text, "italic")
        self.assertEqual(result[2].text, " text.")
        self.assertEqual(result[1].text_type, TextType.ITALIC_TEXT)


if __name__ == "__main__":
    unittest.main()