import unittest
from unittest import mock
import sys
sys.path.append('..')

class PythonTest(unittest.TestCase):

    def test_python(self):
        code = open("blackjack.py").read()
        code = code.replace('g = Game()', '        return locals()\ng = Game()')
        with unittest.mock.patch('builtins.input', side_effect=[1, "f", 'h', 9]): # side_effects is the list of mocked inputs
            exec(code)
            g = locals()["Game"]()
            local_variables = g.play()
        print(local_variables)
        self.assertEqual(local_variables['game_number'], 9, "game_number should increment to be equal to games_to_play.")


if __name__ == '__main__':
    unittest.main() 




