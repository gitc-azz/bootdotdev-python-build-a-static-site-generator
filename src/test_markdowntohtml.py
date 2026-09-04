
import unittest
from markdowntohtml import *

class TestMarkdownToHtml(unittest.TestCase):
    def test_markdown_to_html_node(self):
        md = "I a just a plain paragraph in one line"
        self.assertEqual(markdown_to_html_node(md).to_html(),
                         "<div><p>I a just a plain paragraph in one line</p></div>")


