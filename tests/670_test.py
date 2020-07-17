import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        hand = Hand()
        self.assertFalse(hand.dealer, "dealer should default to False.")

if __name__ == '__main__':
    unittest.main() 