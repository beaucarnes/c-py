import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        game = Game()
        game.play()
        text = open("blackjack.py").read()
        text_found = text.find('game_number = 0') or text.find('game_number=0')
        self.assertTrue(text_found > 0, "Code should contain Game class with play method and 'game_number = 0'.")
if __name__ == '__main__':
    unittest.main() 