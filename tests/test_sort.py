import unittest
from ..algorithms import insertion_sort, selection_sort, sort_by


class TestSort(unittest.TestCase):

    def test_inserstion_sort(self):
        self.assertListEqual(insertion_sort([10, 6, 18, 13, 16, 0, 7, 3, 11, 15]), [0, 3, 6, 7, 10, 11, 13, 15, 16, 18])
        self.assertListEqual(insertion_sort([10, 5, 17, 55, 34, 61, 6, 18]), [5, 6, 10, 17, 18, 34, 55, 61])
        self.assertListEqual(insertion_sort([34, 8, 9, 5, 43, 38, 37, 14, 19, 25, 7, 43, 32, 30, 0, 17, 14, 13, 21, 43]), [0, 5, 7, 8, 9, 13, 14, 14, 17, 19, 21, 25, 30, 32, 34, 37, 38, 43, 43, 43])
        self.assertListEqual(insertion_sort([10, 23, 30, 45, 40, 35, 28, 34, 11, 32, 29, 23, 26, 0, 21, 31, 27, 7, 2, 24]), [0, 2, 7, 10, 11, 21, 23, 23, 24, 26, 27, 28, 29, 30, 31, 32, 34, 35, 40, 45])
        self.assertListEqual(insertion_sort([23, 42, 4, 16, 8, 15]), [4, 8, 15, 16, 23, 42])
        self.assertListEqual(insertion_sort([-2, 1, 3, 18, 20, -28, 0]), [-28, -2, 0, 1, 3, 18, 20])
        self.assertListEqual(insertion_sort([19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_selection_sort(self):
        self.assertListEqual(selection_sort([3, 2, 8, 4, 10]), [2, 3, 4, 8, 10])
        self.assertListEqual(selection_sort([10, 6, 18, 13, 16, 0, 7, 3, 11, 15]), [0, 3, 6, 7, 10, 11, 13, 15, 16, 18])
        self.assertListEqual(selection_sort([10, 5, 17, 55, 34, 61, 6, 18]), [5, 6, 10, 17, 18, 34, 55, 61])
        self.assertListEqual(selection_sort([34, 8, 9, 5, 43, 38, 37, 14, 19, 25, 7, 43, 32, 30, 0, 17, 14, 13, 21, 43]), [0, 5, 7, 8, 9, 13, 14, 14, 17, 19, 21, 25, 30, 32, 34, 37, 38, 43, 43, 43])
        self.assertListEqual(selection_sort([10, 23, 30, 45, 40, 35, 28, 34, 11, 32, 29, 23, 26, 0, 21, 31, 27, 7, 2, 24]), [0, 2, 7, 10, 11, 21, 23, 23, 24, 26, 27, 28, 29, 30, 31, 32, 34, 35, 40, 45])
        self.assertListEqual(selection_sort([23, 42, 4, 16, 8, 15]), [4, 8, 15, 16, 23, 42])
        self.assertListEqual(selection_sort([-2, 1, 3, 18, 20, -28, 0]), [-28, -2, 0, 1, 3, 18, 20])
        self.assertListEqual(selection_sort([19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_sort_by(self):
        data = [
            {'origin': 'SFO', 'dest': 'JFK', 'duration': 5.5, 'price': '$249', 'airline': 'JetBlue'},
            {'origin': 'SFO', 'dest': 'LGA', 'duration': 7.75, 'price': '$201', 'airline': 'Spirit'},
            {'origin': 'OAK', 'dest': 'LGA', 'duration': 5.83, 'price': '$225', 'airline': 'Delta'},
            {'origin': 'OAK', 'dest': 'NWK', 'duration': 8.13, 'price': '$189', 'airline': 'United'},
            {'origin': 'OAK', 'dest': 'JFK', 'duration': 5.32, 'price': '$244', 'airline': 'Virgin America'}
        ]
        self.assertEqual(sort_by(data, 'duration')[0]['duration'], 5.32)
        self.assertEqual(sort_by(data, 'price')[0]['price'], '$189')
