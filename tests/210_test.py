import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        self.assertNotEqual(cards, [['spades', 'A'], ['spades', '2'], ['spades', '3'], ['spades', '4'], ['spades', '5'], ['spades', '6'], ['spades', '7'], ['spades', '8'], ['spades', '9'], ['spades', '10'], ['spades', 'J'], ['spades', 'Q'], ['spades', 'K'], ['clubs', 'A'], ['clubs', '2'], ['clubs', '3'], ['clubs', '4'], ['clubs', '5'], ['clubs', '6'], ['clubs', '7'], ['clubs', '8'], ['clubs', '9'], ['clubs', '10'], ['clubs', 'J'], ['clubs', 'Q'], ['clubs', 'K'], ['hearts', 'A'], ['hearts', '2'], ['hearts', '3'], ['hearts', '4'], ['hearts', '5'], ['hearts', '6'], ['hearts', '7'], ['hearts', '8'], ['hearts', '9'], ['hearts', '10'], ['hearts', 'J'], ['hearts', 'Q'], ['hearts', 'K'], ['diamonds', 'A'], ['diamonds', '2'], ['diamonds', '3'], ['diamonds', '4'], ['diamonds', '5'], ['diamonds', '6'], ['diamonds', '7'], ['diamonds', '8'], ['diamonds', '9'], ['diamonds', '10'], ['diamonds', 'J'], ['diamonds', 'Q'], ['diamonds', 'K']], 'cards list should not be order.')
    def test_python2(self):
        self.assertEqual(len(cards), 52, "cards list should have 52 items.")
if __name__ == '__main__':
    unittest.main() 