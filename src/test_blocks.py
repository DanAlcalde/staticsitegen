import unittest

from blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

class TestMarkdownToBlocks(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(markdown_to_blocks(""), [])

    def test_single_paragraph(self):
        self.assertEqual(markdown_to_blocks("This is a single paragraph."), ["This is a single paragraph."])

    def test_multiple_paragraphs(self):
        self.assertEqual(markdown_to_blocks("This is the first paragraph.\n\nThis is the second paragraph."), ["This is the first paragraph.", "This is the second paragraph."])

    def test_leading_trailing_newlines(self):
        self.assertEqual(markdown_to_blocks("\n\nThis is a paragraph with leading and trailing newlines.\n\n"), ["This is a paragraph with leading and trailing newlines."])
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )
    
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Subheading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### H6"), BlockType.HEADING)
        # Test invalid heading (no space)
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)
        
    def test_code(self):
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.CODE)
        # Test invalid code (missing end backticks)
        self.assertEqual(block_to_block_type("```\ncode"), BlockType.PARAGRAPH)
        
    def test_quote(self):
        self.assertEqual(block_to_block_type("> quote"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- item 1\n- item 2"), BlockType.UNORDERED_LIST)
        # Test invalid unordered list (missing dash)
        self.assertEqual(block_to_block_type("item 1\n- item 2"), BlockType.PARAGRAPH)
    
    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. item 1\n2. item 2"), BlockType.ORDERED_LIST)
        # Test invalid ordered list (missing number)
        self.assertEqual(block_to_block_type("item 1\n2. item 2"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("1. item 1\n3. item 2"), BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
    
    
    def test_headings(self):
        md = """
# Heading 1

## Heading 2

### Heading 3 with **bold**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3 with <b>bold</b></h3></div>"
    )

    def test_quotes(self):
        md = """
    > This is a quote
    > with multiple lines
    > and **formatting**
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with multiple lines and <b>formatting</b></blockquote></div>"
    )




if __name__ == "__main__":
    unittest.main()