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
