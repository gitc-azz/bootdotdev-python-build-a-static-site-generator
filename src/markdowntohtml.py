from htmlnode import ParentNode
from strpreprocess import markdown_to_blocks
from block import BlockType, block_to_block_type
from textnode import text_to_textnodes, text_nodes_to_html_nodes


def create_paragraph(block: str) -> HTMLNode:
    text_nodes = text_to_textnodes(block)
    children = text_nodes_to_html_nodes(text_nodes)
    return ParentNode("p", children)
        

def block_to_html_node(block: str) -> HTMLNode:
    btype = block_to_block_type(block)
    match btype:
        case BlockType.PARAGRAPH:
            return create_paragraph(block)

def markdown_to_html_node(markdown: str) -> HTMLNode:
    children = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        children.append(block_to_html_node(block))

    all_father = ParentNode("div", children, None)
    return all_father
