import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"href": "https://www,boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://www,boot.dev"')  

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://www,boot.dev", "target": "_blank"})
        result = node.props_to_html()
        self.assertIn(' href="https://www,boot.dev"', result)
        self.assertIn(' target="_blank"', result)
        self.assertEqual(len(result), len(' href="https://www,boot.dev" target="_blank"'))
    def test_repr_empty_node(self):
        node = HTMLNode()
        expected = "HTMLNode(tag=None, value=None, props={}, children=[])"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main()