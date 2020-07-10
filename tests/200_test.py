import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        self.assertTrue("random" in sys.modules, 'The random module should be imported.')
if __name__ == '__main__':
    unittest.main() 