from convert import text_node_to_html_node, text_to_textnodes
from htmlnode import ParentNode, LeafNode, HTMLNode
from blocks import markdown_to_blocks, block_to_block_type, text_to_children, markdown_to_html_node
from textnode import TextNode, TextType
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

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)
    html_result = template.replace("{{ Title }}", title).replace("{{ Content }}", html) 
    html_result = html_result.replace('href="/', 'href="{basepath}').replace('src="/', 'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
         f.write(html_result)       

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                generate_page(from_path, template_path, dest_path.replace(".md", ".html"))
               
        else:
            generate_pages_recursive(from_path, template_path, dest_path)