import unittest
import sys
sys.path.append('..')
import re

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        hand = Hand()
        hand.display(show_all_dealer_cards=True)
        text = open("blackjack.py").read()
        text_found = text.find('show_all_dealer_cards=False') or text.find('show_all_dealer_cards = False')
        self.assertTrue(text_found > 0, "Code should contain 'show_all_dealer_cards=False'.")

if __name__ == '__main__':
    unittest.main() 