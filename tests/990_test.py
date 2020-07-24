# import unittest
# from unittest import mock
# import sys
# sys.path.append('..')

# from blackjack import *

# class PythonTest(unittest.TestCase):

#     def test_python(self):
#         code = open("blackjack.py").read()
#         code = code.replace('g = Game()', '        return locals()\ng = Game()')
#         with unittest.mock.patch('builtins.input', side_effect=[1, "f", 'h', 1]): # side_effects is the list of mocked inputs
#             exec(code)
#             g = locals()["Game"]()
#             local_variables = g.play()
#         print(local_variables)

#         cards1 = [str(card) for card in local_variables['deck'].cards] 
#         cards2 = [str(card) for card in Deck().cards] 

#         self.assertTrue(isinstance(local_variables['deck'], Deck), "deck should be Deck class.")
#         self.assertNotEqual(cards1, cards2, "Cards in deck should be shuffled.")

# if __name__ == '__main__':
#     unittest.main() 




