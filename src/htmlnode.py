
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.props = props if props is not None else {}
        self.children = children if children is not None else []

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        if not self.props:
            return ""
        return "".join([f' {key}="{value}"' for key, value in self.props.items() if value is not None])

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props}, children={self.children})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode requires a value")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}>{self.value}{self.props_to_html()}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode requires a tag")
        if not self.children:
            raise ValueError("ParentNode requires children")
        children_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"