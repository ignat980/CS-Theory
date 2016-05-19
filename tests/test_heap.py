import unittest
from data_structures.heap import MinHeap


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()

    def test_init(self):
        self.heap.size == 0
        with self.assertRaises(IndexError, msg="Peek on an empty heap should raise IndexError"):
            self.peek()
        with self.assertRaises(IndexError, msg="Pop on an empty heap should raise IndexError"):
            self.pop()
        self.heap.insert(5)
        self.assertEqual(self.heap.size, 1, msg="Insert should increase the size property of heap")
        self.assertEqual(self.heap.peek(), 5, msg="Peek should return smallest item in heap")
        # self.assertEqual(self.heap.pop(), 5, msg="Pop should return smallest item in heap")
        # self.assertEqual(self.heap.size, 0, msg="Pop should decrease the size property of heap")
        self.heap.insert(3)
        self.assertEqual(self.heap.peek(), 3, msg="Insert should move smallest value to top of heap")
        self.heap.insert(7)
        self.heap.insert(10)
        self.heap.insert(13)
        self.heap.insert(9)
        self.heap.insert(8)
        self.heap.insert(6)
        self.assertListEqual(self.heap._items, [3, 5, 7, 6, 13, 9, 8, 10])
