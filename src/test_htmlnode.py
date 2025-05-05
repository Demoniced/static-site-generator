import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_creation(self):
        node = HTMLNode("p","text text text",None,{"href":"Black","target":"Yellow.com"})
    def test_pros_two(self):
        testing = HTMLNode("p","text text text",None,{"href":"Black","target":"Yellow.com","link":"eww"})
        testss = HTMLNode("p","text text text")
        self.assertEqual(testing.props_to_html(),' href="Black" target="Yellow.com" link="eww"')
    def test_pros(self):
        test = HTMLNode("p","text text text",None,{"href":"Black","target":"Yellow.com"})
        

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_a(self):
        nodee = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(nodee.to_html(),'<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",)
    def test_if_list(self):
        grand_child4 = LeafNode("li","new")
        parent2 = ParentNode("ul",[grand_child4])
        grand_child3 = LeafNode("li","li3")
        grand_child2 = LeafNode("li","li2")
        grand_child = LeafNode("li","li1")
        child_node = ParentNode("ul",[grand_child,grand_child2,grand_child3,parent2])
        parent_node = ParentNode("p",[child_node])
        self.assertEqual(parent_node.to_html(),
                "<p><ul><li>li1</li><li>li2</li><li>li3</li><ul><li>new</li></ul></ul></p>"         )
        