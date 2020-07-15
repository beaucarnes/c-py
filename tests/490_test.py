import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        self.assertTrue(isinstance(deck1, Deck), "deck1 should be instance of Deck.")

if __name__ == '__main__':
    unittest.main() 