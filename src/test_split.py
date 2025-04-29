import unittest

from textnode import TextNode, TextType
from split import split_nodes_delimiter, split_nodes_image, split_nodes_link

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
    
    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.NORMAL_TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.NORMAL_TEXT),
            TextNode("image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.NORMAL_TEXT),
            TextNode(
                "second image", TextType.IMAGE_TEXT, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

    def test_split_links(self):
        node = TextNode("This is text with a [link](https://www.boot.dev) and another [second link](https://google.com)", TextType.NORMAL_TEXT,)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("link", TextType.LINK_TEXT, "https://www.boot.dev"),
            TextNode(" and another ", TextType.NORMAL_TEXT),
            TextNode(
                "second link", TextType.LINK_TEXT, "https://google.com"
            ),
        ],
        new_nodes,
    )

    def test_split_link_and_image(self):
        node = TextNode("This is text with a [link](https://www.boot.dev) and an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.NORMAL_TEXT,)
        new_nodes = split_nodes_link([node])
        new_nodes = split_nodes_image(new_nodes)

if __name__ == "__main__":
    unittest.main()


    