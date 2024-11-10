import unittest

def plus(x, y):
    return x + y

class Testplus(unittest.TestCase):
    def test_plus_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_plus_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_zero(self):
        result = add(0, 5)
        self.assertEqual(result, 5)
        
    def test_add_float_numbers(self):
      result = add(2.5, 3.7)
        self.assertEqual(result, 6.2)

    def test_add_different_data_types(self):
        with self.assertRaises(TypeError):
            add("hello", 2)

if _name_ == '_main_':
    unittest.main()
