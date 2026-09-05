import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def is_ordered(block: str) -> bool:
    lines = block.split("\n")
    for i, line in enumerate(lines):
        if not line.startswith(f"{i+1}. "):
            return False
    return True

def block_to_block_type(block: str) -> BlockType:
    if re.match(r"^#{1,6} .+$", block) is not None:
        return BlockType.HEADING
    if re.match(r"^```\n(.*\n)*?```$", block) is not None:
        return BlockType.CODE
    if re.match(r"^(\> ?.*\n?)+$", block) is not None:
        return BlockType.QUOTE
    if re.match(r"^(\- .+\n?)+$", block) is not None:
        return BlockType.UNORDERED_LIST
    if re.match(r"^(\d+\. .+\n?)+$", block) is not None and is_ordered(block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
