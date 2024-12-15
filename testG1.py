import unittest

from Grammar import ContextFreeGrammar
from Parser import Parser
import os

class TestParser(unittest.TestCase):

    def setUp(self):
        self.grammar_file = "g1.txt"
        self.sequence_file = "seq.txt"
        self.output_file = "outg1.txt"
        self.grammar = ContextFreeGrammar()
        self.grammar.load_grammar(self.grammar_file)
        self.parser = Parser(self.grammar, self.output_file, self.sequence_file)

    def test_momentaryInsucces(self):
        self.parser.momentaryInsuccess()
        self.assertEqual(self.parser.getState(), 'b')

    def test_advance(self):
        self.parser.setInputStack(['a', 'A'])
        self.parser.setWorkingStack([('S', 1)])
        self.parser.setIndex(1)
        self.parser.advance()
        self.assertEqual(self.parser.getIndex(), 2)
        self.assertEqual(self.parser.getInputStack(), ['A'])
        self.assertEqual(self.parser.getWorkingStack(), [('S', 1), 'a'])

    def test_expand(self):
        self.parser.setInputStack(['S'])
        self.parser.setWorkingStack([])
        self.parser.setIndex(1)
        self.parser.expand()
        self.assertEqual(self.parser.getInputStack(), ['a', 'A'])
        self.assertEqual(self.parser.getWorkingStack(), [('S', 1)])
        self.assertEqual(self.parser.getIndex(), 1)

    def test_success(self):
        self.parser.success()
        self.assertEqual(self.parser.getState(), "f")

    def test_back(self):
        self.parser.setState("b")
        self.parser.setIndex(2)
        self.parser.setWorkingStack([("S", 1), "a"])
        self.parser.setInputStack(["b", "c"])
        self.parser.back()

        self.assertEqual(self.parser.getWorkingStack(), [("S", 1)])
        self.assertEqual(self.parser.getInputStack(), ["a", "b", "c"])

    def test_anotherTry(self):
        self.parser.setState("b")
        self.parser.setIndex(2)
        self.parser.setWorkingStack([("S", 1), "a", ("A", 2)])
        self.parser.setInputStack(["a", "A"])
        self.parser.anotherTry()

        self.assertEqual(self.parser.getWorkingStack(), [("S", 1), "a", ("A", 3)])
        self.assertEqual(self.parser.getInputStack(), ["b", "A"])
        self.assertEqual(self.parser.getState(), 'q')


if __name__ == "__main__":
    unittest.main()
