from enum import Enum
from htmlnode import ParentNode, LeafNode
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from convert import text_node_to_html_node, text_to_textnodes
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if block.startswith("#") and " " in block and block.index(" ") <= 6:
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    if any(line.lstrip().startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    if len(lines) > 0:
        for i, line in enumerate(lines, 1):
            if not line.startswith(f"{i}. "):
                break
        else:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            paragraph_text = re.sub(r'\n', ' ', block)
            html_nodes.append(ParentNode(tag="p", children=text_to_children(paragraph_text)))
        elif block_type == BlockType.HEADING:
            level = block.index(" ")
            heading_text = block[level + 1:]
            html_nodes.append(ParentNode(tag=f"h{level}", children=text_to_children(heading_text)))
        elif block_type == BlockType.CODE:
            lines = block.split("\n")
            code_content = '\n'.join(lines[1:])
            if code_content.endswith("```"):
                code_content = code_content[:-3]
            text_node = TextNode(code_content, TextType.NORMAL_TEXT)
            code_html = text_node_to_html_node(text_node)
            html_nodes.append(ParentNode(tag="pre", children=[ParentNode(tag="code", children=[code_html])]))
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            quote_content = " ".join([line.lstrip()[1:].lstrip() for line in lines if line.lstrip().startswith(">")])
            html_nodes.append(ParentNode(tag="blockquote", children=text_to_children(quote_content)))
        elif block_type == BlockType.UNORDERED_LIST:
            items = [line[2:] for line in block.split("\n") if line.startswith("- ")]
            list_items = [ParentNode(tag="li", children=text_to_children(item)) for item in items]
            html_nodes.append(ParentNode(tag="ul", children=list_items))
        elif block_type == BlockType.ORDERED_LIST:
            items = [line[3:] for line in block.split("\n") if re.match(r"\d+\. ", line)]
            list_items = [ParentNode(tag="li", children=text_to_children(item)) for item in items]
            html_nodes.append(ParentNode(tag="ol", children=list_items))
    return ParentNode(tag="div", children=html_nodes)



