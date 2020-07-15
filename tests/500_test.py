import unittest
import sys
import subprocess
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        result = subprocess.run(['python', 'blackjack.py'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        prints_correctly = result == "[['spades', {'value': 11, 'rank': 'A'}], ['spades', {'value': 2, 'rank': '2'}], ['spades', {'value': 3, 'rank': '3'}], ['spades', {'value': 4, 'rank': '4'}], ['spades', {'value': 5, 'rank': '5'}], ['spades', {'value': 6, 'rank': '6'}], ['spades', {'value': 7, 'rank': '7'}], ['spades', {'value': 8, 'rank': '8'}], ['spades', {'value': 9, 'rank': '9'}], ['spades', {'value': 10, 'rank': '10'}], ['spades', {'value': 10, 'rank': 'J'}], ['spades', {'value': 10, 'rank': 'Q'}], ['spades', {'value': 10, 'rank': 'K'}], ['clubs', {'value': 11, 'rank': 'A'}], ['clubs', {'value': 2, 'rank': '2'}], ['clubs', {'value': 3, 'rank': '3'}], ['clubs', {'value': 4, 'rank': '4'}], ['clubs', {'value': 5, 'rank': '5'}], ['clubs', {'value': 6, 'rank': '6'}], ['clubs', {'value': 7, 'rank': '7'}], ['clubs', {'value': 8, 'rank': '8'}], ['clubs', {'value': 9, 'rank': '9'}], ['clubs', {'value': 10, 'rank': '10'}], ['clubs', {'value': 10, 'rank': 'J'}], ['clubs', {'value': 10, 'rank': 'Q'}], ['clubs', {'value': 10, 'rank': 'K'}], ['hearts', {'value': 11, 'rank': 'A'}], ['hearts', {'value': 2, 'rank': '2'}], ['hearts', {'value': 3, 'rank': '3'}], ['hearts', {'value': 4, 'rank': '4'}], ['hearts', {'value': 5, 'rank': '5'}], ['hearts', {'value': 6, 'rank': '6'}], ['hearts', {'value': 7, 'rank': '7'}], ['hearts', {'value': 8, 'rank': '8'}], ['hearts', {'value': 9, 'rank': '9'}], ['hearts', {'value': 10, 'rank': '10'}], ['hearts', {'value': 10, 'rank': 'J'}], ['hearts', {'value': 10, 'rank': 'Q'}], ['hearts', {'value': 10, 'rank': 'K'}], ['diamonds', {'value': 11, 'rank': 'A'}], ['diamonds', {'value': 2, 'rank': '2'}], ['diamonds', {'value': 3, 'rank': '3'}], ['diamonds', {'value': 4, 'rank': '4'}], ['diamonds', {'value': 5, 'rank': '5'}], ['diamonds', {'value': 6, 'rank': '6'}], ['diamonds', {'value': 7, 'rank': '7'}], ['diamonds', {'value': 8, 'rank': '8'}], ['diamonds', {'value': 9, 'rank': '9'}], ['diamonds', {'value': 10, 'rank': '10'}], ['diamonds', {'value': 10, 'rank': 'J'}], ['diamonds', {'value': 10, 'rank': 'Q'}], ['diamonds', {'value': 10, 'rank': 'K'}]]\n" or result == "[['spades', {'rank': 'A', 'value': 11}], ['spades', {'rank': '2', 'value': 2}], ['spades', {'rank': '3', 'value': 3}], ['spades', {'rank': '4', 'value': 4}], ['spades', {'rank': '5', 'value': 5}], ['spades', {'rank': '6', 'value': 6}], ['spades', {'rank': '7', 'value': 7}], ['spades', {'rank': '8', 'value': 8}], ['spades', {'rank': '9', 'value': 9}], ['spades', {'rank': '10', 'value': 10}], ['spades', {'rank': 'J', 'value': 10}], ['spades', {'rank': 'Q', 'value': 10}], ['spades', {'rank': 'K', 'value': 10}], ['clubs', {'rank': 'A', 'value': 11}], ['clubs', {'rank': '2', 'value': 2}], ['clubs', {'rank': '3', 'value': 3}], ['clubs', {'rank': '4', 'value': 4}], ['clubs', {'rank': '5', 'value': 5}], ['clubs', {'rank': '6', 'value': 6}], ['clubs', {'rank': '7', 'value': 7}], ['clubs', {'rank': '8', 'value': 8}], ['clubs', {'rank': '9', 'value': 9}], ['clubs', {'rank': '10', 'value': 10}], ['clubs', {'rank': 'J', 'value': 10}], ['clubs', {'rank': 'Q', 'value': 10}], ['clubs', {'rank': 'K', 'value': 10}], ['hearts', {'rank': 'A', 'value': 11}], ['hearts', {'rank': '2', 'value': 2}], ['hearts', {'rank': '3', 'value': 3}], ['hearts', {'rank': '4', 'value': 4}], ['hearts', {'rank': '5', 'value': 5}], ['hearts', {'rank': '6', 'value': 6}], ['hearts', {'rank': '7', 'value': 7}], ['hearts', {'rank': '8', 'value': 8}], ['hearts', {'rank': '9', 'value': 9}], ['hearts', {'rank': '10', 'value': 10}], ['hearts', {'rank': 'J', 'value': 10}], ['hearts', {'rank': 'Q', 'value': 10}], ['hearts', {'rank': 'K', 'value': 10}], ['diamonds', {'rank': 'A', 'value': 11}], ['diamonds', {'rank': '2', 'value': 2}], ['diamonds', {'rank': '3', 'value': 3}], ['diamonds', {'rank': '4', 'value': 4}], ['diamonds', {'rank': '5', 'value': 5}], ['diamonds', {'rank': '6', 'value': 6}], ['diamonds', {'rank': '7', 'value': 7}], ['diamonds', {'rank': '8', 'value': 8}], ['diamonds', {'rank': '9', 'value': 9}], ['diamonds', {'rank': '10', 'value': 10}], ['diamonds', {'rank': 'J', 'value': 10}], ['diamonds', {'rank': 'Q', 'value': 10}], ['diamonds', {'rank': 'K', 'value': 10}]]\n"
        print(result, prints_correctly)
        self.assertTrue(prints_correctly, 'Should print all cards.') 
        
if __name__ == '__main__':
    unittest.main() 