# import unittest
# import sys
# import re
# sys.path.append('..')

# from blackjack import *

# class PythonTest(unittest.TestCase):
#     def test_python(self):
#         code = open("blackjack.py").read()
#         pattern = re.compile("try:\s+games_to_play = int\(input\(\"How many games do you want to play\?: \"\)\)\s+except:\s+print\(\"You must enter a number.\"\)")
#         found_pattern = pattern.search(code)
#         self.assertTrue(found_pattern, "Code should contain try-catch block")
# if __name__ == '__main__':
#     unittest.main() 