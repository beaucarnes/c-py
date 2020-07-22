import unittest
import sys
sys.path.append('..')
import re

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        text_found = open("blackjack.py").read().find('for index, card in enumerate(self.cards):')
        self.assertTrue(text_found > 0, "Code should contain 'for index, card in enumerate(self.cards):'.")

if __name__ == '__main__':
    unittest.main() 