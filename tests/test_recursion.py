import unittest
from ..algorithms import *


class TestRecursion(unittest.TestCase):
    def test_factorial(self):
        # factorial should return the product n * (n-1) * ... * 2 * 1 for n >= 0
        self.assertEqual(factorial(0), 1)  # base case
        self.assertEqual(factorial(1), 1)  # base case
        self.assertEqual(factorial(2), 2 * 1)
        self.assertEqual(factorial(3), 3 * 2 * 1)
        self.assertEqual(factorial(4), 4 * 3 * 2 * 1)
        self.assertEqual(factorial(5), 5 * 4 * 3 * 2 * 1)
        self.assertEqual(factorial(6), 6 * 5 * 4 * 3 * 2 * 1)
        self.assertEqual(factorial(7), 7 * 6 * 5 * 4 * 3 * 2 * 1)
        self.assertEqual(factorial(8), 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
        self.assertEqual(factorial(9), 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
        self.assertEqual(factorial(10), 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
        # factorial should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for n < 0'):
            factorial(-1)
            factorial(-5)
            factorial(-20)
        # factorial should raise a ValueError for non-integer n
        with self.assertRaises(ValueError, msg='function undefined for float'):
            factorial(3.14159)

    def test_fibonacci(self):
        # fibonacci should return fibonacci(n-1) + fibonacci(n-2) for n >= 0
        self.assertEqual(fibonacci(0), 0)  # base case
        self.assertEqual(fibonacci(1), 1)  # base case
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)
        # these could run for a long time...
        # self.assertEqual(fibonacci(15), 610)
        # self.assertEqual(fibonacci(20), 6765)
        # self.assertEqual(fibonacci(25), 75025)
        # self.assertEqual(fibonacci(30), 832040)
        # self.assertEqual(fibonacci(35), 9227465)  # you'll need to be patient
        # fibonacci should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for n < 0'):
            fibonacci(-1)
            fibonacci(-5)
            fibonacci(-20)
        # fibonacci should raise a ValueError for non-integer n
        with self.assertRaises(ValueError, msg='function undefined for float'):
            fibonacci(3.14159)

    def test_linear_search(self):
        # linear search can find items regardless of list order
        names = ['Adrian', 'Josh', 'Ignat', 'Jacob', 'Kevin', 'Dan', 'Alan']
        # linear search should return the index of each item in the list
        self.assertEqual(linear_search(names, 'Adrian'), 0)
        self.assertEqual(linear_search(names, 'Josh'), 1)
        self.assertEqual(linear_search(names, 'Ignat'), 2)
        self.assertEqual(linear_search(names, 'Jacob'), 3)
        self.assertEqual(linear_search(names, 'Kevin'), 4)
        self.assertEqual(linear_search(names, 'Dan'), 5)
        self.assertEqual(linear_search(names, 'Alan'), 6)
        # linear search should return None for any item not in the list
        self.assertIsNone(linear_search(names, 'Jeremy'))
        self.assertIsNone(linear_search(names, 'nobody'))

    def test_binary_search(self):
        # binary search requires list values to be in sorted order
        names = ['Adrian', 'Alan', 'Dan', 'Ignat', 'Jacob', 'Josh', 'Kevin']
        # binary search should return the index of each item in the list
        self.assertEqual(binary_search(names, 'Adrian'), 0)
        self.assertEqual(binary_search(names, 'Alan'), 1)
        self.assertEqual(binary_search(names, 'Dan'), 2)
        self.assertEqual(binary_search(names, 'Ignat'), 3)
        self.assertEqual(binary_search(names, 'Jacob'), 4)
        self.assertEqual(binary_search(names, 'Josh'), 5)
        self.assertEqual(binary_search(names, 'Kevin'), 6)
        # binary search should return None for any item not in the list
        self.assertIsNone(binary_search(names, 'Jeremy'))
        self.assertIsNone(binary_search(names, 'nobody'))
