import unittest
import sys
import io
import re
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        hand2 = Hand()
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        hand2.display()                                 # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), "Your hand:\n", "display() should print 'Your hand:'.")
if __name__ == '__main__':
    unittest.main() 
