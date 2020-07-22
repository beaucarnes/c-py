import unittest
import sys
import re
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        text_found = open("blackjack.py").read().find('has_ace = False')
        self.assertTrue(text_found > 0, "Code should contain 'has_ace = False'.")

if __name__ == '__main__':
    unittest.main() 