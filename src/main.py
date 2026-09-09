import os
import shutil
import pathlib
from textnode import TextNode, TextType
from strpreprocess import extract_title
from markdowntohtml import markdown_to_html_node

def rm_clean_public():
    files = os.listdir("public")
    files.remove(".gitignore")
    for f in files:
        file = os.path.join("public", f)
        if os.path.isfile(file):
            os.remove(file)
        else:
            shutil.rmtree(file)
        print(f"removed: {file} ")

def copy_files_to_public_from(directory: str):
    files = os.listdir(directory)
    destination = directory[len("static"):]
    destination = "public" + destination
    if not os.path.exists(destination):
        os.mkdir(destination)
    print(f"destination={destination}")
    for f in files:
        file = os.path.join(directory, f)
        if os.path.isfile(file):
            shutil.copy(file, os.path.join(destination, f))
            print(f"copied: {file}, to public")
        else:
            copy_files_to_public_from(file)

def copy_static_to_public():
    copy_files_to_public_from("static")

def update_public_from_static():
    rm_clean_public()
    copy_static_to_public()

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = pathlib.Path(from_path).read_text()
    template = pathlib.Path(template_path).read_text()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    pathlib.Path(dest_path).write_text(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path) -> None:
    files = os.listdir(dir_path_content)
    # destination = dest_dir_path[len("content"):]
    # destination = "public" + destination
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
            generate_page(os.path.join(dir_path_content, f), template_path, output_file)
            print(f"generated: {file}, to {output_file}")
        else: # here file is a directory for simplicity sake
            generate_pages_recursive(os.path.join(dir_path_content, f), template_path, os.path.join(dest_dir_path, f))
            # copy_files_to_public_from(file)

def main():
    update_public_from_static()
    generate_pages_recursive("content", "template.html", "public")
    #generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
