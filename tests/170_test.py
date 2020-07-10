# import unittest
# import sys
# import subprocess
# sys.path.append('..')

# from blackjack import *

# class PythonTest(unittest.TestCase):
#     def test_python(self):
#         result = subprocess.run(['python', 'blackjack.py'], stdout=subprocess.PIPE).stdout.decode('utf-8')
#         self.assertEqual(result,"['spades', 'A']\n['spades', '2']\n['spades', '3']\n['spades', '4']\n['spades', '5']\n['spades', '6']\n['spades', '7']\n['spades', '8']\n['spades', '9']\n['spades', '10']\n['spades', 'J']\n['spades', 'Q']\n['spades', 'K']\n['clubs', 'A']\n['clubs', '2']\n['clubs', '3']\n['clubs', '4']\n['clubs', '5']\n['clubs', '6']\n['clubs', '7']\n['clubs', '8']\n['clubs', '9']\n['clubs', '10']\n['clubs', 'J']\n['clubs', 'Q']\n['clubs', 'K']\n['hearts', 'A']\n['hearts', '2']\n['hearts', '3']\n['hearts', '4']\n['hearts', '5']\n['hearts', '6']\n['hearts', '7']\n['hearts', '8']\n['hearts', '9']\n['hearts', '10']\n['hearts', 'J']\n['hearts', 'Q']\n['hearts', 'K']\n['diamonds', 'A']\n['diamonds', '2']\n['diamonds', '3']\n['diamonds', '4']\n['diamonds', '5']\n['diamonds', '6']\n['diamonds', '7']\n['diamonds', '8']\n['diamonds', '9']\n['diamonds', '10']\n['diamonds', 'J']\n['diamonds', 'Q']\n['diamonds', 'K']\n", 'Should print 52 lists, all representing different cards.')

# if __name__ == '__main__':
#     unittest.main() 