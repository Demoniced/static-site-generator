from textnode import *
from htmlnode import *
from conversions import *


def main():
    Word = TextNode("This is some anchor text", TextType.LINKS, "https://www.boot.dev")
    print(Word)

main()

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
           return LeafNode(None,text_node.text,None)
        case TextType.BOLD:
           return LeafNode("b",text_node.text,None)
        case TextType.ITALIC:
           return LeafNode("i",text_node.text,None)
        case TextType.CODE:
            return LeafNode("code",text_node.text,None)
        case TextType.LINKS:
            return LeafNode("a",text_node.text,{"href":text_node.url})
        case TextType.IMAGES:
            return LeafNode("img","",{"src":text_node.url,
                                                  "alt":text_node.text})
        case _:
            raise Exception("invalid type")
        