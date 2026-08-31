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

    def test_split_nodes_delimiter_01(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.ONE_LINE_CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.PLAIN))
        self.assertEqual(new_nodes[1], TextNode("code block", TextType.ONE_LINE_CODE))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.PLAIN))

    def test_split_nodes_delimiter_02(self):
        node = TextNode("This `is text` with two `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.ONE_LINE_CODE)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0], TextNode("This ", TextType.PLAIN))
        self.assertEqual(new_nodes[1], TextNode("is text", TextType.ONE_LINE_CODE))
        self.assertEqual(new_nodes[2], TextNode(" with two ", TextType.PLAIN))
        self.assertEqual(new_nodes[3], TextNode("code block", TextType.ONE_LINE_CODE))
        self.assertEqual(new_nodes[4], TextNode(" word", TextType.PLAIN))

    def test_split_nodes_delimiter_03(self):
        node = TextNode("This `is text`` with` three `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.ONE_LINE_CODE)
        self.assertEqual(len(new_nodes), 6)
        self.assertEqual(new_nodes[0], TextNode("This ", TextType.PLAIN))
        self.assertEqual(new_nodes[1], TextNode("is text", TextType.ONE_LINE_CODE))
        self.assertEqual(new_nodes[2], TextNode(" with", TextType.ONE_LINE_CODE))
        self.assertEqual(new_nodes[3], TextNode(" three ", TextType.PLAIN))
        self.assertEqual(new_nodes[4], TextNode("code block", TextType.ONE_LINE_CODE))
        self.assertEqual(new_nodes[5], TextNode(" word", TextType.PLAIN))



if __name__ == "__main__":
    unittest.main()
