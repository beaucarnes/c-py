import unittest
import sys
sys.path.append('..')
import random
random.seed(1)

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python1(self):
        variables_exist = "cards_dealt" in vars() or "card" in vars() or "rank" in vars() or "rank_dict" in vars() or "value" in vars()
        self.assertFalse(variables_exist, "Code after shuffle() should be deleted.")

if __name__ == '__main__':
    unittest.main() 