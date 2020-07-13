import unittest
import sys
sys.path.append('..')
import random
random.seed(100)

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        print(card)
        self.assertEqual(card, cards_dealt[0], "card should be the first item in the cards list.")
    def test_python2(self):
        text_found = open("blackjack.py").read().count("print(card)")
        self.assertEqual(text_found, 1, 'Code ends with print(card)')

if __name__ == '__main__':
    unittest.main() 