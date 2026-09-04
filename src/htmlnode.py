class HTMLNode:
    def __init__(self, tag: str | None = None,
                 value: str | None = None, 
                 children: ["HTMLNode"] | None = None,
                 props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        ret = ""
        for key, value in self.props.items():
            ret += f' {key}="{value}"'

        return ret

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None,
                 value: str | None, 
                 props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value must not be None")
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag: str | None,
                 children: ["HTMLNode"] | None,
                 props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag should not be None")
        if self.children is None:
            return ValueError("children must not be None")
        
        ret = f"<{self.tag}>"
        for child in self.children:
            ret += child.to_html()
        ret += f"</{self.tag}>"

        return ret

