from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = []
    split_markdown = markdown.split("\n\n")
    for block in split_markdown:
        block = block.strip()
        if not block:
            continue
        blocks.append(block)
    
    return blocks

def block_to_block_type(block):
    if block.startswith("#") and " " in block and block.index(" ") <= 6:
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    if len(lines) > 0:
        for i, line in enumerate(lines, 1):
            if not line.startswith(f"{i}. "):
                break
        else:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
