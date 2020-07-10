import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        deal()
        deal()
        self.assertEqual(len(cards), 50, 'cards list should be length 50 after dealing two cards.')

if __name__ == '__main__':
    unittest.main() 