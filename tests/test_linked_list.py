from linked_list import LinkedList
import unittest


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_init(self):
        ll = LinkedList()
        self.assertTrue(ll.is_empty())
        ll = LinkedList('Data')
        self.assertFalse(ll.is_empty())
        ll = LinkedList(['Data', 'Data2'])
        self.assertFalse(ll.is_empty())
        ll = LinkedList('Data', 'Data2', 'Data3')

    def test_get(self):
        with self.assertRaises(IndexError, msg="Get at head/tail from empty linked list should return IndexError"):
            self.ll.get_at_head()
            self.ll.get_at_tail()
        self.ll = LinkedList(1, 2, 3, 4)
        self.assertEqual(self.ll.get_at_head(), 1, 'Get at head should get head data')
        self.assertEqual(self.ll.get_at_tail(), 4, 'Get at tail should get tail data')
        self.assertEqual(self.ll.get_at_index(0), 1, 'Get at index 0 should get first item')
        self.assertEqual(self.ll.get_at_index(2), 3, 'Get at index 2 should get third item')
        with self.assertRaises(IndexError, msg='Get at out of bounds index should throw an IndexError'):
            self.ll.get_at_index(len(self.ll))
        self.assertEqual(self.ll.get_at_index(len(self.ll) - 1), 4, 'Get at last index should return tail item')
        self.assertEqual(self.ll.get_at_index(-1), 4, 'Get at index -1 should return tail item')
        self.assertEqual(self.ll.get_at_index(-len(self.ll)), 1, 'Get at index (-length of list) should return head item')

    def test_insert_at_head(self):
        self.ll.insert_at_head('Data1')
        self.assertEqual(self.ll.get_at_head(), 'Data1', 'Insert at head should update head pointer in linked list with no items')
        self.assertEqual(self.ll.get_at_tail(), 'Data1', 'Insert at head should update tail pointer in linked list with no items')
        self.ll.insert_at_head('Data2')
        self.ll.insert_at_head('Data3')
        self.ll.insert_at_head('Data4')
        self.ll.insert_at_head('Data5')
        self.ll.insert_at_head('Data6')
        self.assertEqual(self.ll.get_at_head(), 'Data6', 'Insert at head should update head pointer in linked list with many items')
        self.assertEqual(self.ll.get_at_tail(), 'Data1', 'Insert at head should not change tail pointer in linked list with many items')
        self.assertEqual(self.ll.get_at_index(0), 'Data6', 'Get at index 0 should return first item')
        self.assertEqual(self.ll.get_at_index(2), 'Data4', 'Get at index 2 should return third item')

    def test_insert_at_tail(self):
        self.ll.insert_at_tail('Data1')
        self.assertEqual(self.ll.get_at_head(), 'Data1', 'Insert at tail should update head pointer with no items')
        self.assertEqual(self.ll.get_at_tail(), 'Data1', 'Insert at tail should update tail pointer with no items')
        self.ll.insert_at_tail('Data2')
        self.ll.insert_at_tail('Data3')
        self.ll.insert_at_tail('Data4')
        self.ll.insert_at_tail('Data5')
        self.ll.insert_at_tail('Data6')
        self.assertEqual(self.ll.get_at_head(), 'Data1', 'Insert at tail should update head pointer in linked list with many items')
        self.assertEqual(self.ll.get_at_tail(), 'Data6', 'Insert at tail should not change tail pointer in linked list with many items')
        self.assertEqual(self.ll.get_at_index(2), 'Data3', 'Get at index 2 should return third item')

    def test_insert_at_index(self):
        self.ll = LinkedList('Data1', 'Data2', 'Data3', 'Data4', 'Data5')
        self.ll.insert_at_index(3, 'Data3.5')
        self.assertEqual(self.ll.get_at_index(3), 'Data3.5', 'Insert at index should set the data at the index')
        self.assertEqual(self.ll.get_at_index(2), 'Data3', 'Insert at index should not change the data at the index before it')
        self.assertEqual(self.ll.get_at_index(4), 'Data4', 'Insert at index should move the other data up an index')
        with self.assertRaises(IndexError, msg='Insert at out of bounds index should raise IndexError'):
            self.ll.insert_at_index(len(self.ll) + 1, 'Data7')

    def test_set(self):
        self.ll.set_at_index(0, 'Data1')
        self.assertEqual(self.ll.get_at_head(), 'Data1', 'Set at 0 should update head pointer in linked list with no items')
        self.assertEqual(self.ll.get_at_tail(), 'Data1', 'Set at 0 should update tail pointer in linked list with no items')

    def test_remove_items(self):
        self.ll = LinkedList([1, 2, 3, 4, 5, 3])
        self.ll.remove_item(2)
        self.assertFalse(self.ll.contains(2))
        self.ll.remove_item(3)
        self.assertTrue(self.ll.contains(3))
        self.ll.remove_head()
        self.assertEqual(self.ll.get_at_head(), 4)
        with self.assertRaises(ValueError):
            self.ll.remove_item('None')
        with self.assertRaises(ValueError):
            self.ll.remove_item(None)

    def test_list_comprehension(self):
        self.ll = LinkedList([1, 2, 3, 4, 5, 6])
        self.assertListEqual([item for item in self.ll], [1, 2, 3, 4, 5, 6])
        self.assertListEqual([item for item in reversed([item for item in self.ll])], [6, 5, 4, 3, 2, 1])

    def test_size(self):
        self.assertEqual(len(self.ll), 0)
        self.assertEqual(len(self.ll), self.ll.calculate_size())
        self.ll.insert_at_head(3)
        self.assertEqual(len(self.ll), 1)
        self.assertEqual(len(self.ll), self.ll.calculate_size())
        self.ll.insert_at_tail(4)
        self.assertEqual(len(self.ll), 2)
        self.assertEqual(len(self.ll), self.ll.calculate_size())
        # print('Counted size:', str(testLL.size) + "; Calculated size:", testLL.calculate_size())

    def test_text_representation(self):
        self.assertEqual(repr(self.ll), 'LinkedList()')
        self.ll = LinkedList(1)
        self.assertEqual(repr(self.ll), 'LinkedList(1)')
        self.ll = LinkedList([1, 2, 3, 4])
        self.assertEqual(repr(self.ll), 'LinkedList(1, 2, 3, 4)')
