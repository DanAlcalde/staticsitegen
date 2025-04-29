from textnode import TextNode, TextType 
from extract import extract_markdown_images, extract_markdown_links 


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        start_pos = text.find(delimiter)
        if start_pos == -1:
            new_nodes.append(node)
            continue

        end_pos = text.find(delimiter, start_pos + len(delimiter))    
        if end_pos == -1:
                raise Exception(f"No closing delimiter found for {delimiter} in {text}")
        
        before = text[:start_pos]
        content = text[start_pos + len(delimiter):end_pos]
        after = text[end_pos + len(delimiter):]

        if before:
            new_nodes.append(TextNode(before, TextType.NORMAL_TEXT))
            
        new_nodes.append(TextNode(content, text_type))
            
        if after:
            after_node = TextNode(after, TextType.NORMAL_TEXT)
            result_nodes = split_nodes_delimiter([after_node], delimiter, text_type)
            new_nodes.extend(result_nodes)
        
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        
        if not images:
            new_nodes.append(node)
            continue

        current_text = node.text
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            if image_markdown in current_text:
                sections = current_text.split(image_markdown, 1)
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL_TEXT))
                new_nodes.append(TextNode(alt_text, TextType.IMAGE_TEXT, url))
                current_text = sections[1]

        if current_text:
            new_nodes.append(TextNode(current_text, TextType.NORMAL_TEXT))
        

    return new_nodes




def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        
        if not links:
            new_nodes.append(node)
            continue

        current_text = node.text
        for alt_text, url in links:
            link_markdown = f"[{alt_text}]({url})"
            if link_markdown in current_text:
                sections = current_text.split(link_markdown, 1)
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL_TEXT))
                new_nodes.append(TextNode(alt_text, TextType.LINK_TEXT, url))
                current_text = sections[1]

        if current_text:
            new_nodes.append(TextNode(current_text, TextType.NORMAL_TEXT))
        

    return new_nodes














