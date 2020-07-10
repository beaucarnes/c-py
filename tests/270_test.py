import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        self.assertEqual(len(card), 2, 'card should be a list of length 2.')
    def test_python2(self):
        self.assertEqual(len(cards), 51, 'cards should be a list of length 51 after deal function is called.')
    def test_python3(self):
        text_found = open("blackjack.py").read().count("print(card)")
        self.assertEqual(text_found, 1, 'Code ends with print(card)')

if __name__ == '__main__':
    unittest.main() 