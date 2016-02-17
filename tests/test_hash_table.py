from hash_table import HashTable
import unittest


class TestHashTable(unittest.TestCase):
    def test_init(self):
        hs = HashTable()
        self.assertTrue(hs.is_empty())

    def hashTableTest():
        print('=====HASH TABLE TEST=====')
        testHT = HashTable()
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


# if __name__ == '__main__':
# unittest.main()
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestLinkedList)
#     unittest.TextTestRunner(verbosity=2).run(suite)
