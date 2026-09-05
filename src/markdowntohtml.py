from htmlnode import ParentNode, LeafNode
from strpreprocess import markdown_to_blocks
from block import BlockType, block_to_block_type
from textnode import text_to_textnodes, text_nodes_to_html_nodes


def create_paragraph(block: str) -> HTMLNode:
    text_nodes = text_to_textnodes(block)
    children = text_nodes_to_html_nodes(text_nodes)
    return ParentNode("p", children)
        
def create_heading(block: str) -> HTMLNode:
    n = 0
    while block[n] == '#':
        n += 1
    text = block[n+1:]
    return LeafNode(f"h{n}", text, None)

def create_unordered_list(block: str) -> HTMLNode:
    children = []
    items = block.split("\n")
    for item in items:
        if len(item) == 0:
            continue
        text_nodes = text_to_textnodes(item[2:])
        grand_children = text_nodes_to_html_nodes(text_nodes)
        children.append(ParentNode("li", grand_children))
    return ParentNode("ul", children)

def create_ordered_list(block: str) -> HTMLNode:
    children = []
    items = block.split("\n")
    for item in items:
        if len(item) == 0:
            continue
        text_nodes = text_to_textnodes(item[3:])
        grand_children = text_nodes_to_html_nodes(text_nodes)
        children.append(ParentNode("li", grand_children))
    return ParentNode("ol", children)

def create_code_block(block: str) -> HTMLNode:
    inner = LeafNode("code", block[4:-4])
    return ParentNode("pre", [inner])

def create_quote(block: str) -> HTMLNode:
    children = []
    items = block.split("\n")
    offset = 1
    paragraph = ""
    for item in items:
        extra = 0
        if item.startswith("> "): # deal with optional leading space after '<'
            extra += 1
        if item.strip() == ">":
            if paragraph != "":
                children.append(create_paragraph(paragraph))
                paragraph = ""
        else:
            if paragraph != "":
                paragraph += '\n'
            paragraph += item[offset + extra:]
    if paragraph != "":
        children.append(create_paragraph(paragraph))
    return ParentNode("blockquote", children)

def block_to_html_node(block: str) -> HTMLNode:
    btype = block_to_block_type(block)
    match btype:
        case BlockType.PARAGRAPH:
            return create_paragraph(block)
        case BlockType.HEADING:
            return create_heading(block)
        case BlockType.UNORDERED_LIST:
            return create_unordered_list(block)
        case BlockType.ORDERED_LIST:
            return create_ordered_list(block)
        case BlockType.CODE:
            return create_code_block(block)
        case BlockType.QUOTE:
            return create_quote(block)

def markdown_to_html_node(markdown: str) -> HTMLNode:
    children = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        children.append(block_to_html_node(block))

    all_father = ParentNode("div", children, None)
    return all_father
