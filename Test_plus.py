import unittest
from plus import *

class Testplus(unittest.TestCase):
    def test_plus_positive_numbers(self):
        result = plus(2, 3)
        self.assertEqual(result, 5)
        
    def test_plus_negative_numbers(self):
        result = plus(-2, -3)
        self.assertEqual(result, -5)
        
    def test_add_zero(self):
        result = plus(0, 5)
        self.assertEqual(result, 5)
        
    def test_add_float_numbers(self):
        result = plus(2.5, 3.7)
        self.assertEqual(result, 6.2)
        
if _name_ == '_main_':
    unittest.main()
