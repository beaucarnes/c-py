import unittest
import sys
sys.path.append('..')
import random
random.seed(1)

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python1(self):
        text_found = open("blackjack.py").read().find("card = deal(1)[0]")
        self.assertTrue(text_found > 0, "Code should contain 'card = deal(1)[0]'.")

if __name__ == '__main__':
    unittest.main() 