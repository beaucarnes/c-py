import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        text_found = open("blackjack.py").read().find("if len(self.cards) > 1:")
        self.assertTrue(text_found > 0, "Code should contain 'if len(self.cards) > 1:'.")

if __name__ == '__main__':
    unittest.main() 