import unittest
import sys
sys.path.append('..')
import re

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        card1 = Card("diamonds", {"rank": "A", "value": 11})
        text = card1.__str__()
        self.assertEqual(text, "A of diamonds", "__str__ should return the correct string.")
    def test_python2(self):
        code = open("blackjack.py").read()
        pattern = re.compile("f[\'\"]")
        found_pattern = pattern.search(code)
        self.assertTrue(found_pattern, "Code should contain f string.")
    def test_python3(self):
        text_found = open("blackjack.py").read().find('" of " + self.suit')
        self.assertFalse(text_found > 0, '''Code should not contain '" of " + self.suit'.''')

if __name__ == '__main__':
    unittest.main() 