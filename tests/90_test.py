import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        self.assertEqual(suit, 'clubs', 'The suit variable should equal clubs.')
if __name__ == '__main__':
    unittest.main() 