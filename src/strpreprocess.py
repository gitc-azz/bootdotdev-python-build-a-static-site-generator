def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n");
    ret = []
    for block in blocks:
        striped = block.strip()
        if len(striped) == 0:
            continue
        ret.append(striped)
    return ret
