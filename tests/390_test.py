# import unittest
# import subprocess
# import sys
# import re
# sys.path.append('..')
# import random
# random.seed(1)

# from blackjack import *

# class PythonTest(unittest.TestCase):
#     def test_python2(self):
#         code = open("blackjack.py").read()
#         pattern = re.compile("rank_dict\[[\"\']rank[\"\']\]\,\s?rank_dict\[[\"\']value[\"\']\]")
#         found_pattern = pattern.search(code)
#         self.assertTrue(found_pattern, "Code print items from dictionary.")

# if __name__ == '__main__':
#     unittest.main() 