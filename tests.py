from linkedList import LinkedList
from hashTable import HashBrownTable
import unittest


class testLinkedList(unittest.TestCase):
    def testInit(self):
        print('=====LINKED LIST TEST=====')
        ll1 = LinkedList()
        self.assertTrue(ll1.is_empty())
        print('Head:', ll1.head)
        print('Tail:', ll1.tail)
        ll2 = LinkedList('This')
        self.assertFalse(ll2.is_empty())
        print('Head:', testLL.head)
        print('Tail:', testLL.tail)

    def testHeadInsert(self):
        ll = LinkedList()
        ll.insert_at_head('is')
        self.assertEqual(ll.get_at_head, 'is')
        testLL.insert_at_head('backwards')
        testLL.insert_at_head('blank')
        print('Multiple items:', testLL)
        testLL.remove_item('blank')
        print('Removed an item:', testLL)
        print('Value at index 1:', repr(testLL.get_at_index(1)))
        print('Iterated:', [item for item in testLL])
        print('Reversed:', [item for item in reversed([item for item in testLL])])
        print('Counted size:', str(testLL.size) + "; Calculated size:", testLL.calculate_size())


def hashTableTest():
    print('=====HASH TABLE TEST=====')
    testHT = HashBrownTable()
    print('Empty hash table:', testHT)
    testHT.set('Key', 7)
    print('Hash table has one element:', testHT)
    testHT.set('OtherKey', 14)
    testHT.set('ThirdKey', 28)
    print('Hash table has three elements:', testHT)
    testHT.set('FourthKey', 56)
    testHT.set('FifthKey', 112)
    testHT.set('SixthKey', 224)
    testHT.set('SeventhKey', 448)
    print('Hash table should have expanded')
    print('Hash table keys:', testHT.keys())
    print('Hash table values:', testHT.values())
    testHT.remove_item('Key')
    print('Hash table removed items:', testHT)
    testHT.remove_item('key')
    print('Hash table should be the same:', testHT)
    testHT.set('OtherKey', 5)
    print('\'OtherKey\' should be different:', testHT)


def queueTest():
    ...


def test():
    unittest.main()

if __name__ == '__main__':
    test()
