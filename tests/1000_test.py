import unittest
from unittest import mock
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):

    def test_python(self):
        code = open("blackjack.py").read()
        code = code.replace('g = Game()', '        return locals()\ng = Game()')
        with unittest.mock.patch('builtins.input', side_effect=[1, "f", 'h', 1]): # side_effects is the list of mocked inputs
            exec(code)
            g = locals()["Game"]()
            local_variables = g.play()
        print(local_variables)

        self.assertTrue(isinstance(local_variables['player_hand'], Hand), "deck should be Deck class.")

if __name__ == '__main__':
    unittest.main() 




