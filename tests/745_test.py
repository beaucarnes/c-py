import unittest
import sys
import re
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        code = open("blackjack.py").read()
        pattern = re.compile("if card\.rank\[\"rank\"\] == \"A\":\s+has_ace = True")
        found_pattern = pattern.search(code)
        self.assertTrue(found_pattern, "Code should check for ace.")
if __name__ == '__main__':
    unittest.main() 