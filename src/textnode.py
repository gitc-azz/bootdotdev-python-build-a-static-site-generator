from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    PLAIN= "plain"
    BOLD= "bold"
    ITALIC= "italic"
    ONE_LINE_CODE= "one_line_code"
    MULTI_LINE_CODE= "multi_line_code"
    LINK= "link"
    IMAGE= "image"

class TextNode:
    def __init__(self, text: Str, text_type: TextType, url: Str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other: TextNode):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self) -> Str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.PLAIN:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.ONE_LINE_CODE | TextType.MULTI_LINE_CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":f"{text_node.url}"})
        case TextType.IMAGE:
            return LeafNode("img", None, {"src":f"{text_node.url}", "alt":f"text_node.text"})
        case _: # default:
            raise Exception("unhandled TextType of TextNode")
