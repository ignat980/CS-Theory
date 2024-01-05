class Node(object):
    def __init__(self, data):
        self.data = data


class MinHeap(object):
    """Your classic implementation of a Heap"""
    def __init__(self, data=None):
        self.size = 0
        self._items = []
        if data is not None:
            for datum in data:
                self.insert(datum)

    def __repr__(self):
        return repr(self._items)

    def __eq__(self, other):
        return self._items == other._items

    def __bool__(self):
        return bool(self.size)

    def insert(self, data):
        self.size += 1
        self._items.append(data)
        self._bubble_up(self.size)

    def pop(self):
        if self.size == 0:
            raise IndexError("Cannot pop on an empty heap")
        end = self._items.pop()
        top, self._items[0] = self._items[0], end
        self._bubble_down(0)
        self.size -= 1
        return top

    def peek(self):
        if self.size == 0:
            raise IndexError("Cannot peek on an empty heap")
        return self._items[0]

    def _bubble_up(self, index):
        while index // 2 > 0:
            if self._items[index] < self._items[index // 2]:
                self._items[index], self._items[index // 2] = self._items[index // 2], self._items[index]
            index = index // 2

    def _bubble_down(self, index):
        pass

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2
