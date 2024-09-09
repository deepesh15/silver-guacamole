class HTLMNode:
    def __init__(self,tag=None,children=None,value=None,props=None) -> None:
        self.tag = tag
        self.children = children
        self.value = value
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return self.props