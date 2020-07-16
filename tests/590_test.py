import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        card1 = Card("diamonds", {"rank": "A", "value": 11})
        text = card1.__str__()
        self.assertEqual(text, "A of diamonds", "__str__ should be defined correctly")

if __name__ == '__main__':
    unittest.main() 