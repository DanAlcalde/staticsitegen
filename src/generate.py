from convert import text_node_to_html_node, text_to_textnodes
from htmlnode import ParentNode, LeafNode, HTMLNode
import os



def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
         stripped = line.lstrip()
         if stripped.startswith("# "):
            return stripped[2:].strip()
    else:
        raise Exception("No title found in the markdown file.")
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} using template {template_path} to {dest_path}")
    with open(from_path) as f:
         markdown = f.read()
    if not markdown:
        raise Exception("Empty markdown file.")
    with open(template_path) as f:
         template = f.read()
    if not template:
        raise Exception("Empty template file.")
    text = text_to_textnodes(markdown)
    html_nodes = [text_node_to_html_node(node) for node in text]
    title = extract_title(markdown)
    html_result = template.replace("{{ Title }}", title).replace("{{ Content }}", ParentNode(html_nodes).to_html()) 
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
         f.write(html_result)    