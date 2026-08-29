from enum import Enum

class TextType(Enum):
    Plain= "plain"
    Bold= "bold"
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
