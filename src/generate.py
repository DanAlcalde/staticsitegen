from convert import text_node_to_html_node, text_to_textnodes
from htmlnode import ParentNode, LeafNode, HTMLNode


def extract_title(markdown):
    lines = markdown.split('\n')
    if lines[0].startswith('#'):
        return lines[0][1:].strip()
    else:
        raise Exception("No title found in the markdown file.")
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} using template {template_path} to {dest_path}")
    markdown = open(from_path).read()
    if not markdown:
        raise Exception("Empty markdown file.")
    template = open(template_path).read()
    if not template:
        raise Exception("Empty template file.")
    text = text_to_textnodes(markdown)
    title = extract_title(markdown)
    text_nodes = [text_node_to_html_node(node) for node in text]
    html_nodes = []
    for node in text_nodes:
            html_nodes.append(node)
    
    