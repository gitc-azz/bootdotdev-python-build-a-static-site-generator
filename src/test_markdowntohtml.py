
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
),
                ("# heading 1", "<div><h1>heading 1</h1></div>"),
                ("## heading 2", "<div><h2>heading 2</h2></div>"),
                ("### heading 3", "<div><h3>heading 3</h3></div>"),
                ("#### heading 4", "<div><h4>heading 4</h4></div>"),
                ("##### heading 5", "<div><h5>heading 5</h5></div>"),
                ("###### heading 6", "<div><h6>heading 6</h6></div>"),
                (
"""###### heading 6

followed by simple paragraph
""", "<div><h6>heading 6</h6><p>followed by simple paragraph</p></div>"),
                (
"""
- simple
- unordered
- list
""",
"<div><ul><li>simple</li><li>unordered</li><li>list</li></ul></div>"),
                (
"""
- not simple with `one line code`
- unordered _italic_ and ** bold **
- list and finally a [link to](https://url/to/y) blabla
""",
"<div><ul><li>not simple with <code>one line code</code></li><li>unordered "
'<i>italic</i> and <b> bold </b></li><li>list and finally a <a href="https://url/to/y">'
"link to</a> blabla</li></ul></div>"),
                 (
"""
1. not simple with `one line code`
2. ordered _italic_ and ** bold **
3. list and finally a [link to](https://url/to/y) blabla
""",
"<div><ol><li>not simple with <code>one line code</code></li><li>ordered "
'<i>italic</i> and <b> bold </b></li><li>list and finally a <a href="https://url/to/y">'
"link to</a> blabla</li></ol></div>"),
                 (
"""
```
let y = Some(8);
let x = y.take();
```
""", "<div><pre><code>let y = Some(8);\nlet x = y.take();</code></pre></div>"),
                (
"""
> multi
> line
>quote
""", "<div><blockquote><p>multi\nline\nquote</p></blockquote></div>"),
                 (
"""
> multi
> line
> 
> and multi-paragraph
>quote
""", "<div><blockquote><p>multi\nline</p><p>and multi-paragraph\nquote</p></blockquote></div>"),
                 (
r"""
> multi
> line
> 
> and multi-paragraph
> 
>quote
""", "<div><blockquote><p>multi\nline</p><p>and multi-paragraph</p><p>quote</p></blockquote></div>")
                ]
        for tc in tcs:
            self.assertEqual(markdown_to_html_node(tc[0]).to_html(),
                             tc[1])


