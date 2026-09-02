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

    def test_extract_markdown_images(self):
        images = extract_markdown_images(
                "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
                "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(len(images), 2)
        self.assertListEqual(images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                                      ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])


    def test_extract_markdown_images_2(self):
        images = extract_markdown_images(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) "
                "and another ![second image](https://i.imgur.com/3elNhQu.png)")
        self.assertEqual(len(images), 2)
        self.assertListEqual(images, [("image", "https://i.imgur.com/zjjcJKZ.png"),
                                      ("second image", "https://i.imgur.com/3elNhQu.png")])

    def test_extract_markdown_links(self):
        links = extract_markdown_links(
                "a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
                "This is text with a link [to boot dev](https://www.boot.dev)"
                "and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertEqual(len(links), 2)
        self.assertListEqual(links, [("to boot dev", "https://www.boot.dev"),
                                     ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_split_nodes_image(self):
        node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) "
                "and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.PLAIN,
            )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )


    def test_split_nodes_image_2(self):
        node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
                "![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.PLAIN,
            )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )


    def test_split_nodes_links(self):
        node = TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) "
                "and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.PLAIN,
                )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
                new_nodes,
                [
                    TextNode("This is text with a link ", TextType.PLAIN),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                    TextNode(" and ", TextType.PLAIN),
                    TextNode(
                        "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                    ),
                ]
            )


    def test_split_nodes_links_2(self):
        node = TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev)"
                "[to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.PLAIN,
                )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
                new_nodes,
                [
                    TextNode("This is text with a link ", TextType.PLAIN),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                    TextNode(
                        "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                    ),
                ]
            )

    
if __name__ == "__main__":
    unittest.main()
