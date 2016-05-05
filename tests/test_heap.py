import unittest
from data_structures.heap import MinHeap


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()

    def test_init(self):
        self.heap.size == 0
        with self.assertRaises(IndexError, msg="Peek or pop on an empty heap should raise IndexError"):
            self.peek()
            self.pop()
