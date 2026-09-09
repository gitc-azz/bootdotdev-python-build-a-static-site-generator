import unittest
from strpreprocess import *

class TestStrPreProcess(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_extract_title(self):
        tcs = [("# title", "title"),
               ("#    title     ", "title"),
               ("""


# title two
                """, "title two")]

        for tc in tcs:
            #print(f"input:{tc[0]} -> {extract_title(tc[0])} vs {tc[1]}")
            self.assertEqual(extract_title(tc[0]), tc[1])


    def test_extract_title_fails(self):
        tcs = ["""
        # not a title""",
               "# ",
               " # not",
               " ## not"]

        for tc in tcs:
            #print(f"{tc}")
            with self.assertRaises(ValueError):
                ret = extract_title(tc)
                #print(f"{ret}")

