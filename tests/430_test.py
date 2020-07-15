import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python1(self):
        text_found = open("blackjack.py").read().find("print(card)")
        self.assertTrue(text_found > 0, "Code should contain 'print(card)'.")

if __name__ == '__main__':
    unittest.main() 