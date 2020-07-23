import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        variables_exist = 'deck' in globals() or 'hand' in globals()
        self.assertFalse(variables_exist, 'The deck and hand variables should be removed.')
if __name__ == '__main__':
    unittest.main() 