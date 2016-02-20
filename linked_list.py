class Node(object):
    """A node that is used by a linked list, it contains data and a pointer to another node."""
    count = 0

    @classmethod
    def totalCount(cls):
        return cls.count

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node(' + repr(self.data) + ')'

    def set_next(self, node):
        self.next = node
        return self


class LinkedList(object):
    """
    A singly linked list data structure, it contains a string of nodes that store data.

    You can:
    * initalize from a list, or just pass your list as arguments
    * iterate through the list with `for item in list:` syntax
    * check if the linked list is empty with `if list.is_empty():`,
    although `if not list: ` is preferred
    * set, get, and remove values at the head, tail, or an index
    """
    def __init__(self, *datum):
        """Initalizes a linked list from a list of data

        If you give an array, it will be converted into a linked list
        You can also pass a list of arguments to initalize the linked list
        """
        # empty LinkedList
        self.head = None
        self.size = 0
        self.tail = None
        if isinstance(datum[0], list):
            for item in datum[0]:
                self.insert_at_tail(item)
        for data in datum:
            self.insert_at_tail(data)

    def __repr__(self):
        """String Representation of Linked List"""
        string = 'LinkedList('
        dataLength = len(self)
        if dataLength == 0:
            return string + ')'
        for node in self._node_iterator():
            string += repr(node.data)
            if node != self.tail:
                string += ', '
        return string + ')'

    def __eq__(self, other):
        if other is None:
            return False
        left_current = self.head
        right_current = other.head
        if left_current is None and right_current is None:
            return True
        else:
            while left_current is not None and right_current is not None:
                if left_current.data != right_current.data:
                    return False
                left_current = left_current.next
                right_current = right_current.next
                if left_current is None and right_current is None:
                    return True
                elif left_current is None and right_current is not None:
                    return False
                elif left_current is not None and right_current is None:
                    return False
        return False

    # Makes the list an iterable with for..in syntax
    def __iter__(self):
        self.__current = self.head
        return self

    # Used by iterable to implement iteration
    def __next__(self):
        returned = self.__current
        if returned is None:
            raise StopIteration()
        else:
            self.__current = self.__current.next
        return returned.data

    # Generator iteration
    def _node_iterator(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __len__(self):
        return self.size

    def __setitem__(self, idx, value):
        self.set_at_index(idx, value)

    def __getitem__(self, idx):
        """Returns the item at the given index

        It accepts ints, 'head', and 'tail'
        and returns the repective data
        """
        if isinstance(idx, str):
            if idx == 'head':
                return self.get_at_index(0)
            elif idx == 'tail':
                return self.get_at_index(-1)
        elif isinstance(idx, int):
            return self.get_at_index(idx)
        elif isinstance(idx, slice):
            l = LinkedList()
            if idx.step is None:
                if idx.start is None and idx.stop is None:
                    for item in self:
                        l[-1] = item
                elif idx.start is not None and idx.stop is None:
                    current = None
                    try:
                        current = self.__get_node_at_index(idx.start)
                    except IndexError:
                        pass
                    while current is not None:
                        l[-1] = current.data
                        current = current.next
                elif idx.start is None and idx.stop is not None:
                    count = -1
                    current = self.head
                    while current is not None and count != idx.stop:
                        l[-1] = current.data
                        current = current.next
                        count += 1
                else:
                    current = None
                    try:
                        current = self.__get_node_at_index(idx.start)
                    except IndexError:
                        pass
                    while current is not None:
                        l[-1] = current.data
                        current = current.next
            return l
        else:
            raise KeyError('Key {} not defined for linked list'.format(idx))

    def __delitem__(self, idx):
        if isinstance(idx, str):
            if idx == 'head':
                return self.get_at_index(0)
            elif idx == 'tail':
                return self.get_at_index(-1)
        elif isinstance(idx, int):
            return self.get_at_index(idx)
        else:
            raise KeyError

    def calculate_size(self):
        count = 0
        for node in self:
            count += 1
        return count

    def is_empty(self):
        return not bool(self.size)

    def insert_at_index(self, idx, data):
        if idx == 0:
            return self.insert_at_head(data)
        if idx == -1 or idx == len(self) - 1:
            return self.insert_at_tail(data)
        before_node = self.__get_node_at_index(idx - 1)
        before_node.next = Node(data).set_next(before_node.next)
        self.size += 1

    def insert_at_head(self, data):
        """Creates a node at the beginning of the linked list"""
        # reassign head reference
        self.head = Node(data).set_next(self.head)
        if not self:
            self.tail = self.head
        self.size += 1

    def insert_at_tail(self, data):
        """Creates a node at the end of the linked list"""
        if self.size == 0:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.size += 1

    def get_at_index(self, idx):
        """Returns the data of a node at a given index"""
        return self.__get_node_at_index(idx).data

    def get_at_head(self):
        """Returns the data at the head"""
        return self.__get_node_at_index(0).data

    def get_at_tail(self):
        """Returns the data at the tail"""
        return self.__get_node_at_index(-1).data

    def __get_node_at_index(self, idx):
        """Returns the node object at a given index"""
        if idx < 0:
            idx = len(self) + idx
        if idx >= len(self) or idx < 0:
            raise IndexError('Index out of bounds: ' + repr(idx))
        if idx == len(self) - 1:
            return self.tail
        current_node = self.head
        for i in range(0, idx):
            current_node = current_node.next
        return current_node

    def set_at_index(self, idx, value):
        """Sets the value at a given index in the linked list"""
        if idx == len(self) or idx == -1:
            self.insert_at_tail(value)
        else:
            self.__get_node_at_index(idx).data = value

    def remove_head(self):
        """Pops the item at head, and return it"""
        if not self:
            raise ValueError('List is empty')
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def remove_item(self, value):
        """Removes the value from the linked list"""
        previousNode = self.head
        if value == self.head.data:
            self.remove_head()
            return
        for node in self._node_iterator():
            if value == node.data:
                previousNode.next = node.next
                self.size -= 1
                return node.data
            previousNode = node
        raise ValueError('Value not in linked list')

    def remove_tail(self):
        """Removes the tail and returns the tail data"""
        if not self:
            raise ValueError('List is empty')
        data = self.tail.data
        self.tail = self.__get_node_at_index(-2)
        self.tail.next = None
        return data

    def contains(self, value):
        """Searches for the value in the linked list"""
        for item in self:
            if item == value:
                return True
        return False

    def as_list(self):
        l = []
        for item in self:
            l.append(item)
        return l
