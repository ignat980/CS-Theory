from linked_list import LinkedList


class HashTable(object):
    """An implementation of a HashTable, stores data with key-value pairs."""
    def __init__(self, dictionary=None):
        self._bucketLength = 8
        self._buckets = [LinkedList() for i in range(self._bucketLength)]
        self.size = 0
        if isinstance(dictionary, dict):
            for key, value in dictionary:
                self.set(key, value)

    def __repr__(self):
        data = self.data()
        dataLength = len(self)
        if dataLength == 0:
            return 'HashTable{}'
        string = ''
        for i in range(0, dataLength - 1):
            string += repr(data[i]) + ", "
        string += repr(data[dataLength - 1])
        # [brian] instead of the above 4 lines you could also write:
        string = ', '.join([repr(datum) for datum in data])
        # In general, python tries very hard to prevent you from needing to
        # keep track of which iteration you're currently on. If you find
        # yourself doing a lot of -1 and +1 math with indices, it's likely
        # an easier way exists.

        return 'HashTable{' + string + '}'

    # [brian] Nice use of magic methods in this file, they're very pythonic and make your code so much
    # easier to read and write.
    def __len__(self):
        return self.size

    def __getitem__(self, key):
        """Returns the data for a given key."""
        for k, value in self._buckets[hash(key) % self._bucketLength]:
            if k == key:
                return value
        raise KeyError('Key not found')

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        ...

    def __contains__(self, key):
        ...

    # Expands the hash table so there is less chance of a collision
    def _expand(self):
        if self.size / self._bucketLength > 0.7:
            saved = self.data()
            self._bucketLength *= 2
            # keys = self.keys()
            self._buckets = [LinkedList() for i in range(0, self._bucketLength)]
            for savedItem in saved:
                self._buckets[hash(savedItem[0]) % self._bucketLength].insert_at_head(savedItem)

    # Sets the value for a given key.
    def set(self, key, data):
        bucket = self._buckets[hash(key) % self._bucketLength]
        if bucket.is_empty():
            bucket.insert_at_head((key, data))
            self.size += 1
        else:
            for i, pair in enumerate(bucket):
                if pair[0] == key:
                    bucket.set_at_index((key, data), i)
                    return
            bucket.insert_at_head((key, data))
            self.size += 1
            self._expand()

    # Removes the data for a given key.
    def remove_item(self, key):
        self.set(key, None)
        self._buckets[hash(key) % self._bucketLength].remove_item((key, None))
        self.size -= 1

    # Returns an array of keys.
    def keys(self):
        keys = []
        for pairsLL in self._buckets:
            for key, data in pairsLL:
                if key is not None:
                    keys.append(key)
        return keys

    # Returns an array of values.
    def values(self):
        vals = []
        for pairsLL in self._buckets:
            for key, value in pairsLL:
                if value is not None:
                    vals.append(value)
        return vals

    # Returns all the data as an array of key-value pairs.
    def data(self):
        data = []
        for pairsLL in self._buckets:
            for key, value in pairsLL:
                if key is not None or value is not None:
                    data.append((key, value))
        return data

    def is_empty(self):
        return self.size == 0
