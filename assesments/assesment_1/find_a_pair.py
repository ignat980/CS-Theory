def find_pair(numbers=[], target=0):
    pairs = []
    for idx, first in enumerate(numbers):
        for second in numbers[idx:]:
            if first + second == target:
                pairs.append((first, second))
    if len(pairs) == 0:
        pairs = "not found"
    return pairs


def test():
    print("Your 🍐  is", find_pair([1, 5, 4, 1, 7, -2], 3))
    print("Your 🍐  is", find_pair([3, 5, 7, 2, 0, -2], 3))
    print("Your 🍐  is", find_pair([3, 5, 7, 2, 10, 2], 3))
    print("Your 🍐  is", find_pair([1, 2, 3, 4, 5], 5))

if __name__ == '__main__':
    test()
