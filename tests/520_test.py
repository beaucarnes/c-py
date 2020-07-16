import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        text_found = open("blackjack.py").read().find("deck2.shuffle()")
        self.assertTrue(text_found > 0, "Code should contain 'deck2.shuffle()'.")

if __name__ == '__main__':
    unittest.main() 