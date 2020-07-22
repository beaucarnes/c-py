# import unittest
# import sys
# import re
# sys.path.append('..')

# from blackjack import *

# class PythonTest(unittest.TestCase):
#     def test_python(self):
#         code = open("blackjack.py").read()
#         pattern = re.compile("for card in self.cards:\s+card_value = card.rank\[\"value\"\]")
#         found_pattern = pattern.search(code)
#         self.assertTrue(found_pattern, "Code should contain for loop.")
# if __name__ == '__main__':
#     unittest.main() 