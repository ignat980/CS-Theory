class Node(object):
    def __init__(self, data):
        self.data = data


class MinHeap(object):
    """Your classic implementation of a Heap"""
    def __init__(self, data):
        self.size = 0
        self._items = []
        for datum in data:
            self.insert(datum)

    def insert(self, data):
        self.size += 1

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
        pass

    def _bubble_down(self, index):
        pass

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2
