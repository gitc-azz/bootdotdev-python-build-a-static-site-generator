import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        hnode = HTMLNode("h1", "I am a title")
        self.assertEqual(repr(hnode), "HTMLNode(h1, I am a title, None, None)")
class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        lnode = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(lnode.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html(),
                         '<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        
        self.assertEqual(
                node.to_html(), 
                "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


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
                "<div><span><b>grandchild</b></span></div>",
            )
