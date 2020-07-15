import unittest
import sys
import re
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        deck_instance = Deck()
        correct_ranks = [{'rank': 'A', 'value': 11}, {'rank': '2', 'value': 2}, {'rank': '3', 'value': 3}, {'rank': '4', 'value': 4}, {'rank': '5', 'value': 5}, {'rank': '6', 'value': 6}, {'rank': '7', 'value': 7}, {'rank': '8', 'value': 8}, {'rank': '9', 'value': 9}, {'rank': '10', 'value': 10}, {'rank': 'J', 'value': 10}, {'rank': 'Q', 'value': 10}, {'rank': 'K', 'value': 10}]
        self.assertEqual(deck_instance.ranks, correct_ranks, "There should be a Deck class.")
    def test_python2(self):
        self.assertFalse('card' in locals(), "card variable should not exist.")
    def test_python3(self):
        code = open("blackjack.py").read()
        pattern = re.compile("print\(card\[1\]\[[\"\']value[\"\']\]\)")
        found_pattern = pattern.search(code)
        self.assertFalse(found_pattern, "Code should not print card value.")
if __name__ == '__main__':
    unittest.main() 