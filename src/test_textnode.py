import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    
    def test_eq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a different text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)
    
    def test_eq_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "http://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "http://example.org")
        self.assertNotEqual(node, node2)

    def test_urlnone(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertIsNone(node.url)




if __name__ == "__main__":
    unittest.main()