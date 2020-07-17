import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        hand = Hand()
        self.assertEqual(hand.value, 0, "The Hand class has a values attribute that is 0.")

if __name__ == '__main__':
    unittest.main() 