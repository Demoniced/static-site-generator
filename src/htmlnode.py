class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
            key_values = []
            if self.props != None:
                 for key in self.props:
                        key_values.append(f' {key}="{self.props[key]}"')
            return "".join(key_values)
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children},{self.props})"
    
class LeafNode(HTMLNode):
     def __init__(self,tag=None,value=None,props=None):
          super().__init__(tag,value,None,props)
    
     def to_html(self):
          if self.value == None:
               raise ValueError
          if self.tag == None:
               return self.value

          props_html = self.props_to_html()
          return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
     def __init__(self,tag,children,props=None):
          super().__init__(tag,None,children,props)
     
     def to_html(self):
          if self.tag == None:
               raise ValueError("Tag Parameter Required")
          if self.children == None:
               raise ValueError("Children Parameter Required")
          opening_tag = f'<{self.tag}>'
          for child in self.children:
               opening_tag += child.to_html()
          opening_tag += f'</{self.tag}>'
          return opening_tag
          
          
          
          
