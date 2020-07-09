import unittest
import sys
import subprocess
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        result = subprocess.run(['python', 'blackjack.py'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(result,'Your card is: K\n', 'Incorrect print statement.')

if __name__ == '__main__':
    unittest.main() 