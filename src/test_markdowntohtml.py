
import unittest
from markdowntohtml import *

class TestMarkdownToHtml(unittest.TestCase):
    def test_markdown_to_html_node(self):
        tcs = [
                ("I a just a plain paragraph in one line",
                 "<div><p>I a just a plain paragraph in one line</p></div>"),
                ("I am just a **bold** paragraph in one line",
                 "<div><p>I am just a <b>bold</b> paragraph in one line</p></div>"),
                (
"""I am
a multi
line with _italic_
and some `one line code`
""", "<div><p>I am\na multi\nline with <i>italic</i>\nand some <code>one line code</code></p></div>"
)
                ]
        for tc in tcs:
            self.assertEqual(markdown_to_html_node(tc[0]).to_html(),
                             tc[1])


