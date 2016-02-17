from linked_list import LinkedList
import unittest


class TestLinkedList(unittest.TestCase):
    def test_init(self):
        ll = LinkedList()
        self.assertTrue(ll.is_empty())
        ll = LinkedList('Data')
        self.assertFalse(ll.is_empty())
        ll = LinkedList(['Data', 'Data2'])
        self.assertFalse(ll.is_empty())

    def test_insert_at_head(self):
        ll = LinkedList()
        ll.insert_at_head('is')
        self.assertEqual(ll.get_at_head(), 'is')
        self.assertEqual(ll.get_at_tail(), 'is')
        ll.insert_at_head('backwards')
        ll.insert_at_head('blank')
        self.assertEqual(ll.get_at_head(), 'blank')
        self.assertEqual(ll.get_at_tail(), 'is')

    def test_linked_list_representation(self):
        ll = LinkedList()
        self.assertEqual(repr(ll), 'LinkedList()')
        ll = LinkedList(1)
        self.assertEqual(repr(ll), 'LinkedList(1)')
        ll = LinkedList([1, 2, 3, 4])
        self.assertEqual(repr(ll), 'LinkedList(1, 2, 3, 4)')
        # ll.remove_item('blank')
        # print('Removed an item:', ll)
        # print('Value at index 1:', repr(testLL.get_at_index(1)))
        # print('Iterated:', [item for item in testLL])
        # print('Reversed:', [item for item in reversed([item for item in testLL])])
        # print('Counted size:', str(testLL.size) + "; Calculated size:", testLL.calculate_size())
