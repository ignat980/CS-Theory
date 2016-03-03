class MinStack(object):
    """Stack data structure, contains a `min` func to see the current smallest value in the stack"""
    def __init__(self, *data):
        self._data = []
        self._mins = []
        for datum in data:
            self.push(datum)

    def __len__(self):
        return len(self._data)

    def push(self, data):
        if not self or data < self.min():
            self._mins.append(data)
        self._data.append(data)

    def pop(self):
        if not self:
            raise IndexError
        data = self._data.pop()
        if data == self.min():
            self._mins.pop()
        return data

    def min(self):
        if not self:
            return None
        return self._mins[len(self._mins) - 1]
