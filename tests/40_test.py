import unittest
import sys
sys.path.append('./tests')

from utils import *

class PythonTest(unittest.TestCase):
    def test_command(self):
        self.assertEqual(getLastCommand(), "python blackjack.py", "entered correct last command")
    def test_cwd(self):
        self.assertEqual(getCwd(), "/home/strove/project", "entered in correct directory")

if __name__ == '__main__':
    unittest.main()