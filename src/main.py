from generate import generate_page, generate_pages_recursive
from copy_files_recursive import copy_from_dir

import sys
import shutil
import os

if sys.argv[1]:
    basepath = sys.argv[1]
else:
    basepath = "/"
static_path = os.path.join(basepath, "static")
content_path = os.path.join(basepath, "content")
template_path = os.path.join(basepath, "template")
public_path = os.path.join(basepath, "public")



def main():
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    copy_from_dir(static_path, public_path)
    
    generate_pages_recursive(content_path, template_path, public_path)

if __name__ == "__main__":
    main()