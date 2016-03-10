"""
Human sort: (Let's say we are sorting a deck of cards)
1. Find the lowest card O(n)
2. Put it in a new stack O(1)
3. Find the next highest card o(n)
4. Put it in front of the previous sorted card O(1)
5. Repeat 3 and 4 until you have all the cards sorted in the new set O(n^2)
"""


def selection_sort(array):
    copy = array[:]
    sorted = []
    size = len(array)
    for _ in range(size):
        smallest_index = 0
        for i in range(len(copy)):
            if copy[i] < copy[smallest_index]:
                smallest_index = i
        sorted.append(copy[smallest_index])
        del copy[smallest_index]
    return sorted

# [10, 6, 18, 13, 16, 0, 7, 3, 11, 15]
# [10] [6, 18, 13, 16, 0, 7, 3, 11, 15] max:10 min:10
# 1st
# [6, 10] [18, 13, 16, 0, 7, 3, 11, 15] max:10 min:6
# < max
# [6, 10, 18] [13, 16, 0, 7, 3, 11, 15] max:18 min:6
# > max
# [6, 10, 13, 18] [16, 0, 7, 3, 11, 15] max:18 min:6
#     ^
# % = 58% , idx = 1.75, sort >
# [6, 10, 13, 16, 18] [0, 7, 3, 11, 15] max:18 min:6
#                 ^
# % = 83.3% , idx = 3.33, sort <
# [0, 6, 10, 13, 16, 18] [7, 3, 11, 15] max:18 min:0
# < min
# [0, 6, 7, 10, 13, 16, 18] [3, 11, 15] max:18 min:0
#           ^
# % = 38.8% , idx = 2.33, sort <
# [0, 3, 6, 7, 10, 13, 16, 18] [11, 15] max:18 min:0
#        ^
# % = 16.6% , idx = 1.16, sort <
# [0, 3, 6, 7, 10, 11, 13, 16, 18] [15] max:18 min:0
#              ^
# % = 61.1% , idx = 4.8, sort >
# [0, 3, 6, 7, 10, 11, 13, 15, 16, 18] max:18 min:0
#                       ^
# % = 83.3% , idx = 7.5, sort >


def insertion_sort(array):
    """A bit faster insertion sort

    This variation decides where the index should be before inserting.
    Ω(n), O(n^2)
    """
    if not array:
        return []
    end = start = array[0]
    sort = [start]  # The returned array; TODO optimize to be in-place
    for val in array[1:]:
        # print(sort, start, end, val)  # Debug
        # insert at beginning if < min
        if val < start or val == start:
            sort.insert(0, val)
            start = val
        # insert at end if > max
        elif val > end or val == end:
            sort.append(val)
            end = val
        else:
            # Figure out what the index should be
            num = len(sort) * (val - start) / (end - start)
            # print(num)  # Debug
            idx = int(num)
            # print("pre idx:", idx)  # Debug
            # Insertion sort from the index
            if val < sort[idx]:
                while val < sort[idx - 1]:
                    idx -= 1
                # print("< idx:", idx)  # Debug
                # O(N) time to insert :(
                sort.insert(idx, val)
            elif val > sort[idx]:
                while val > sort[idx + 1]:
                    idx += 1
                # print("> idx:", idx)  # Debug
                sort.insert(idx + 1, val)
            else:
                sort.insert(idx, val)
    return sort
