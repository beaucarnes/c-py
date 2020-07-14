# import unittest
# import sys
# sys.path.append('..')
# import re

# from blackjack import *

# class PythonTest(unittest.TestCase):
#     def test_python(self):
#         code = open("blackjack.py").read()
#         pattern = re.compile("\nelif rank == \"J\":\s+ value = 10")
#         found_pattern = pattern.search(code)
#         self.assertTrue(found_pattern, "An elif statement should check if rank is J.")

# if __name__ == '__main__':
#     unittest.main() 