import re

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n");
    ret = []
    for block in blocks:
        striped = block.strip()
        if len(striped) == 0:
            continue
        ret.append(striped)
    return ret


def extract_title(markdown: str) -> str:
    matched = re.findall(r"^# (.+)?$", markdown, re.MULTILINE)
    if len(matched) != 1:
        raise ValueError(f"markdown must have exactly one h1 -> matched: {matched}")
    ret = matched[0].strip()
    if len(ret) == 0:
        raise ValueError("title is empty")
    return ret
