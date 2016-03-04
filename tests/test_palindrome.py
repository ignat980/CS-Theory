import unittest
from algorithms.palindrome import PalindromeChecker


class TestPalindrome(unittest.TestCase):
    """TestPalindrome is the class for testing plaindrome.py"""

    def setUp(self):
        self.checker = PalindromeChecker()

    def test_palindrome(self):
        self.assertEqual(self.checker("radar"), True)
        self.assertEqual(self.checker("taco cat"), True)
        self.assertEqual(self.checker("race fast, safe car"), True)
        self.assertEqual(self.checker("ignat"), False)
        self.assertEqual(self.checker("ig n, at"), False)
