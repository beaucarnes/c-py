import unittest
import sys
import re
import io
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        hand2 = Hand(True)
        hand2.add_card([Card('spades', {"rank": "K", "value": 10})])
        hand2.add_card([Card('hearts', {"rank": "A", "value": 11})])
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        hand2.display()                                 # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), "Dealer's hand:\nK of spades\nA of hearts\n\n", "display() should print correct string when dealer.")
if __name__ == '__main__':
    unittest.main() 
