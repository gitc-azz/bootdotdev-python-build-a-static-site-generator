import os
import shutil
from textnode import TextNode, TextType

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

def main():
    update_public_from_static()
    tn = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(tn)

if __name__ == "__main__":
    main()

