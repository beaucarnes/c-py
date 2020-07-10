import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        card = deal(2)
        self.assertEqual(len(card), 2, 'card should be a list of length 2.')
    def test_python2(self):
        self.assertEqual(len(cards_dealt), 2, 'card_delt should be a list of length 2.')

if __name__ == '__main__':
    unittest.main() 