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
        """
        Initalizes a linked list from a list of data
        If you give an array, it will be converted into a linked list
        You can also pass a list of arguments to initalize the linked list
        """
        # empty LinkedList
        self.head = None
        self.size = 0
        self.tail = None
        for data in datum:
            if isinstance(data, list):
                for item in data:
                    self.insert_at_tail(item)
            else:
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

    # Makes the list an iterable with for..in syntax
    def __iter__(self):
        self.current = self.head
        return self

    # Used by iterable to implement iteration
    def __next__(self):
        returned = self.current
        if returned is None:
            raise StopIteration()
        else:
            self.current = self.current.next
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
        before_node = self._get_node_at_index(idx - 1)
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
        return self._get_node_at_index(idx).data

    def get_at_head(self):
        """Returns the data at the head"""
        return self._get_node_at_index(0).data

    def get_at_tail(self):
        """Returns the data at the tail"""
        return self._get_node_at_index(-1).data

    def _get_node_at_index(self, idx):
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
        if not self:
            self.insert_at_head(value)
        else:
            self._get_node_at_index(idx).data = value

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
        self.tail = self._get_node_at_index(-2)
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
