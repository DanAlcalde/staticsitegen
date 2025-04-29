from textnode import TextNode, TextType 

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

















