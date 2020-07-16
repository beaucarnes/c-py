import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        card = Card()
        self.assertEqual(card.suit, "hearts", "card.suit should be 'hearts'")

if __name__ == '__main__':
    unittest.main() 