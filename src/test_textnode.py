import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        tcs = [(TextNode("This is a text node", TextType.BOLD), TextNode("This is a text node", TextType.BOLD)),
               (TextNode("This is a text node", TextType.ITALIC), TextNode("This is a text node", TextType.ITALIC))]
        for tc in tcs:
            self.assertEqual(tc[0], tc[1])


    def test_neq(self):
        tcs = [(TextNode("ae", TextType.LINK, "ur"), TextNode("ae", TextType.IMAGE, "ur")),
               (TextNode("ae", TextType.LINK, "ur"), TextNode("ae", TextType.LINK, "r"))]

        for tc in tcs:
            self.assertNotEqual(tc[0], tc[1])


    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
