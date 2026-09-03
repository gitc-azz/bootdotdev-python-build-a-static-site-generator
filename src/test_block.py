import unittest
from block import *


class TestBlock(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### heading 4"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### heading 5"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### heading 6"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("####### not a heading 7"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("g##### not a heading 8"), BlockType.PARAGRAPH)


    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type(
"""```
multi
line
code
```"""), BlockType.CODE)
        self.assertEqual(block_to_block_type(
"""```
not a multi
line
code```"""), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(
"""
```
not a multi
line
code```"""), BlockType.PARAGRAPH)


    def test_block_to_block_type_QUOTE(self):
        self.assertEqual(block_to_block_type("> I am a quote >"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(">I am a quote>"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> I am a quote > "), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> I am a quote> "), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("""> I am 
>a multi
> line
>quote> """), BlockType.QUOTE)
        
        self.assertEqual(block_to_block_type("""> I am 
>Not a multi
> line
> 
>quote> """), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("""> I am 
>Not a multi
> line
geth
>quote> """), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("t< I am NOT a quote> "), BlockType.PARAGRAPH)


    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(block_to_block_type("- unordered list"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("""- unordered
- list"""), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("""- unordered
- list
- last item"""), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("""- unordered
- list -egth
- last item"""), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("""- unordered
- list

- last item"""), BlockType.PARAGRAPH)


    def test_block_to_block_type_ordered_list(self):
        self.assertEqual(block_to_block_type("1. ordered list"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("""1. ordered
2. list"""), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("""1. ordered
2. list
3. last item"""), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("""1. ordered
2. list 1.egth
3. last item"""), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("""1. ordered
2. list

3. last item"""), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("""1. ordered
3. list
2. last item"""), BlockType.PARAGRAPH)



