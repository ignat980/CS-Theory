import unittest
from min_stack import MinStack


class TestMinStack(unittest.TestCase):

    def setUp(self):
        self.stack = MinStack()

    def test_min_set(self):
        self.assertEqual(self.stack.min(), None)
        self.stack.push(3)
        self.assertEqual(self.stack.min(), 3)
        self.stack.push(24)
        self.assertEqual(self.stack.min(), 3)
        self.stack.push(5)
        self.stack.push(1)
        self.assertEqual(self.stack.min(), 1)
        self.stack.push(0)
        self.assertEqual(self.stack.min(), 0)
        self.stack.push(10)
        self.assertEqual(self.stack.min(), 0)
        self.stack.pop()
        self.assertEqual(self.stack.min(), 0)
        self.stack.pop()
        self.assertEqual(self.stack.min(), 1)
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.min(), 3)
