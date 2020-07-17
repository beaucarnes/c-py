import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        found = False
        try:
            hand = Hand()
        except Exception as e:
            found = str(e).find("dealer") > 0
        self.assertTrue(found, "Hand should take a default argument of dealer when initialized.")

if __name__ == '__main__':
    unittest.main() 