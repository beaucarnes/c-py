import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        result = deal(2)
        self.assertEqual(len(result), 0, 'deal function should return and empty list')

if __name__ == '__main__':
    unittest.main() 