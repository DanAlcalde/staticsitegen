from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from generate import generate_page, generate_pages_recursive
from copy_files_recursive import copy_files_recursive

import shutil
import os

def copy_from_dir(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    file_list = os.listdir(source)
    for file in file_list:
        source_path = os.path.join(source, file)
        dest_path = os.path.join(destination, file)
        if os.path.isfile(os.path.join(source, file)):
            print(f"Copying {source_path} to {dest_path}")
            shutil.copy(source_path, dest_path)  
        elif os.path.isdir(os.path.join(source, file)):
            print(f"Copying directory {source_path} to {dest_path}")
            copy_from_dir(source_path, dest_path)
    return

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    copy_from_dir("static", "public")
    
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()