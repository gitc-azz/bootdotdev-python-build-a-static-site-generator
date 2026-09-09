import os
import shutil
import pathlib
import sys
from textnode import TextNode, TextType
from strpreprocess import extract_title
from markdowntohtml import markdown_to_html_node

def rm_clean_public(dest_dir: str):
    files = os.listdir(dest_dir)
    if ".gitignore" in files:
        files.remove(".gitignore")
    for f in files:
        file = os.path.join(dest_dir, f)
        if os.path.isfile(file):
            os.remove(file)
        else:
            shutil.rmtree(file)
        print(f"removed: {file} ")

def copy_files_to_public_from(directory: str, dest_dir: str):
    files = os.listdir(directory)
    destination = directory[len("static"):]
    destination = dest_dir + destination
    if not os.path.exists(destination):
        os.mkdir(destination)
    print(f"destination={destination}")
    for f in files:
        file = os.path.join(directory, f)
        if os.path.isfile(file):
            shutil.copy(file, os.path.join(destination, f))
            print(f"copied: {file}, to {dest_dir}")
        else:
            copy_files_to_public_from(file, dest_dir)

def copy_static_to_public(dest_dir):
    copy_files_to_public_from("static", dest_dir)

def update_public_from_static(dest_dir):
    rm_clean_public(dest_dir)
    copy_static_to_public(dest_dir)

def generate_page(from_path, template_path, dest_path, basename):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = pathlib.Path(from_path).read_text()
    template = pathlib.Path(template_path).read_text()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basename}')
    template = template.replace('src="/', f'src="{basename}')
    pathlib.Path(dest_path).write_text(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basename) -> None:
    files = os.listdir(dir_path_content)
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    print(f"files: {files}, dest_dir_path={dest_dir_path}")
    for f in files:
        file = os.path.join(dir_path_content, f)
        print(f"to query: {file}, to {dest_dir_path}")
        if os.path.isfile(file):
            if pathlib.Path(f).suffix != ".md":
                continue
            output_file = pathlib.Path(os.path.join(dest_dir_path, f)).with_suffix(".html")
            generate_page(os.path.join(dir_path_content, f), template_path, output_file, basename)
            print(f"generated: {file}, to {output_file}")
        else: # here file is a directory for simplicity sake
            generate_pages_recursive(os.path.join(dir_path_content, f), template_path, os.path.join(dest_dir_path, f), basename)


def main():
    basename = "/"
    dest_dir = "public"
    if len(sys.argv) >= 2:
        basename = sys.argv[1]
    if basename != "/":
        dest_dir = "docs"
    update_public_from_static(dest_dir)
    generate_pages_recursive("content", "template.html", dest_dir, basename)


if __name__ == "__main__":
    main()
