import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        text = open("blackjack.py").read()
        text_found = text.find('games_to_play = input("How many games do you want to play? ")')
        self.assertTrue(text_found > 0, "Code should contain correct input method.")
if __name__ == '__main__':
    unittest.main() 