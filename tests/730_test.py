# import unittest
# import sys
# import re
# sys.path.append('..')

# from blackjack import *

# class PythonTest(unittest.TestCase):
#     def test_python(self):
#         text_found = open("blackjack.py").read().find('+=')
#         self.assertEqual(text_found > 0, "Code should contain '+='.")
#     def test_python2(self):
#         hand2 = Hand()
#         hand2.add_card([Card('hearts', {"rank": "A", "value": 11})])
#         hand2.add_card([Card('hearts', {"rank": "8", "value": 8})])
#         hand2.calculate_value()
#         self.assertEqual(hand2.value, 19, "calculate_value() should work correctly.")
# if __name__ == '__main__':
#     unittest.main() 
