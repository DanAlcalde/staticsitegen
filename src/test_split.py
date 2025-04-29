import unittest

from textnode import TextNode, TextType
from split import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_bold(self):
        old_nodes = {TextNode("This is a **bold** text", TextType.NORMAL_TEXT)}
        expected_nodes = [
            TextNode("This is a ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_split_nodes_italic(self):
        old_nodes = {TextNode("This is an _italic_ text", TextType.NORMAL_TEXT)}
        expected_nodes = [
            TextNode("This is an ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, expected_nodes)
 
    def test_mult_delimiters(self):
        old_nodes = {TextNode("This **text** has multiple **bold** words", TextType.NORMAL_TEXT)}
        expected_nodes = [
            TextNode("This ", TextType.NORMAL_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" has multiple ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" words", TextType.NORMAL_TEXT),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_code(self):
        old_nodes = {TextNode("This is a `code` text", TextType.NORMAL_TEXT)}
        expected_nodes = [
            TextNode("This is a ", TextType.NORMAL_TEXT),
            TextNode("code", TextType.CODE_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_missing_closed(self):
        old_nodes = {TextNode("This is a **bold text", TextType.NORMAL_TEXT)}
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD_TEXT)
        self.assertTrue("No closing delimiter found for ** in This is a **bold text" in str(context.exception))
        
if __name__ == "__main__":
    unittest.main()


    