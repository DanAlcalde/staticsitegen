from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from split import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL_TEXT:
        return LeafNode(tag=None, value=text_node.text)
    if text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode(tag="b", value=text_node.text)
    if text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode(tag="i", value=text_node.text)
    if text_node.text_type == TextType.CODE_TEXT:
        return LeafNode(tag="code", value=text_node.text)
    if text_node.text_type == TextType.LINK_TEXT:
        if text_node.url is None:
            raise ValueError("URL must be provided for link text")
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    if text_node.text_type == TextType.IMAGE_TEXT:
        if text_node.url is None:
            raise ValueError("URL must be provided for image text")
        return LeafNode(tag="img", value=None, props={"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Unknown text type: {text_node.text_type}")

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL_TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC_TEXT)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

