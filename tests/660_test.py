import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        hand = Hand(True)
        self.assertTrue(hand.dealer, "Hand should assign dealer when initialized.")

if __name__ == '__main__':
    unittest.main() 