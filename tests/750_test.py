import unittest
import sys
import re
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        hand2 = Hand()
        hand2.add_card([Card('spades', {"rank": "9", "value": 9})])
        hand2.add_card([Card('hearts', {"rank": "A", "value": 11})])
        hand2.add_card([Card('hearts', {"rank": "8", "value": 8})])
        hand2.calculate_value()
        self.assertEqual(hand2.value, 18, "calculate_value() should work correctly when there is an ace.")
if __name__ == '__main__':
    unittest.main() 
