from generate import generate_page, generate_pages_recursive
from copy_files_recursive import copy_from_dir

import sys
import shutil
import os

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"
static_path = "./static"
content_path = "./content"
template_path = "./template.html"
public_path = "./docs"



def main():
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    copy_from_dir(static_path, public_path)
    
    generate_pages_recursive(content_path, template_path, public_path, basepath)

if __name__ == "__main__":
    main()