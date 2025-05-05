import unittest

from textnode import TextNode, TextType
from main import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_rpr(self):
        print_node = TextNode("This is a node",TextType.ITALIC)
        print(print_node)
    def test_not_eq(self):
        nodee = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("Blues",TextType.CODE)
        self.assertNotEqual(nodee,node3)
        print(nodee)
    def test_url(self):
        texts = TextNode("Text",TextType.CODE,"Hrttp") 
        print(texts)
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    


if __name__ == "__main__":
    unittest.main()