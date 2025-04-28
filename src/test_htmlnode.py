import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from convert import text_node_to_html_node


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
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    def test_leaf_novalue(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )
    def test_to_html_no_children(self):
        node = ParentNode("div", children=None)
        with self.assertRaises(ValueError):
            node.to_html()
    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            node.to_html()
    def test_with_mixed_child_types(self):
        leaf_child = LeafNode("b", "leaf content")
        parent_child = ParentNode("div", [LeafNode("span", "nested content")])
        parent = ParentNode("section", [leaf_child, parent_child])
        self.assertEqual(
            parent.to_html(),
            "<section><b>leaf content</b><div><span>nested content</span></div></section>"
            )

    def test_with_props(self):
        node = ParentNode("div", [LeafNode("span", "content")], {"class": "container", "id": "main"})
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold_text(self):
        node = TextNode("This is bold text", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic_text(self):
        node = TextNode("This is italic text", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code_text(self):
        node = TextNode("This is code text", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code text")
    
    def test_link_text(self):
        node = TextNode("This is a link", TextType.LINK_TEXT, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props["href"], "https://www.boot.dev")
        

if __name__ == "__main__":
    unittest.main()