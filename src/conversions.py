from textnode import *
from htmlnode import *


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
        
"""
needs to split the old_node into three parts. Before delimiter, at, and after.
needs to creat a TextNode of each 
TextNode type needs to match the delimiter type
TextNode type befoer and after delimiter will always be TextType.TEXT

function accepts three parameters. old_nodes is a LIST of TextNodes.
Delimiter is the markdown syntax to look for 
text_type is the type of text we are splitting
"""
def split_nodes_delimiter(old_nodes,delimiter,text_type):
    before = ""
    after = ""
    delimited = ""
    for node in old_nodes:
        for item in node.text.split(" "):
            if item.startswith(delimiter) or item.endswith(delimiter):
                delimited.append(item)
            if item.endswith(delimiter):
                after += node.text.split(" ")[node.text.split(" ").index(item) + 1:]
            
            
            print(item)
        print(node.text.split(" "))

    for node in old_nodes:
        for item in node.text.split(" "):
            if item.startswith(delimiter):
                break
            before.append(item)
    for node in old_nodes:
        for item in node.text.split(" "):
            if item.endswith(delimiter):
                after += node.text.split(" ")[node.text.split(" ").index(item) + 1:]
    before.append(node.text_type) 
    after.append(node.text_type)
    delimited.append(text_type)      
            
            
    print(delimited)
    print(before)
    print(after)
    
    
node = TextNode("This is text with a `code block` word and a blue black bobby", TextType.TEXT)
split_nodes_delimiter([node],"`",TextType.CODE)