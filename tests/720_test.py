import unittest
import sys
import re
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        code = open("blackjack.py").read()
        pattern = re.compile("card_value = int\(card.rank\[\"value\"\]\)")
        found_pattern = pattern.search(code)
        self.assertTrue(found_pattern, "card_value should be an integer.")
if __name__ == '__main__':
    unittest.main() 