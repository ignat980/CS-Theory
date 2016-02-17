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


class LinkedList(object):
    """A singly linked list data structure, it contains a string of nodes that store data."""
    def __init__(self, data=None):
        # empty LinkedList
        self.head = None
        self.size = 0
        self.tail = None
        if isinstance(data, list):
            for item in data:
                self.insert_at_tail(item)
        elif data:
            self.insert_at_head(data)

    def __repr__(self):
        """String Representation of Linked List"""
        string = 'LinkedList('
        data = [item for item in self]
        dataLength = len(self)
        if dataLength == 0:
            return string + ')'
        for index, item in enumerate(data):
            string += repr(item)
            if index < self.size - 1:
                string += ', '
        return string + ')'

    # Makes the list an iterable
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

    # Old method of iteration
    # def _node_generator(self):
    #     current = self.head
    #     while current is not None:
    #         yield current
    #         current = current.next

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_at_head(self, data):
        """Creates a node at the beginning of the linked list"""
        # create a new node with the data
        new_node = Node(data)
        new_node.next = self.head
        # reassign head reference
        self.head = new_node
        self.size += 1
        if self.size == 1:
            self.tail = self.head

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
        if idx >= self.size:
            raise IndexError('Index out of bounds')
        if self.is_empty():
            raise ValueError('List is empty')
        current_node = self.head
        for i in range(0, idx):
            current_node = current_node.next
        return current_node.data

    def get_at_head(self):
        """Returns the data at the head"""
        return self.head.data

    def get_at_tail(self):
        """Returns the data at the tail"""
        return self.tail.data

    def _get_node_at_index(self, idx):
        if idx > len(self):
            raise IndexError('Index out of bounds')
        current_node = self.head
        for i in range(0, idx):
            current_node = current_node.next
        return current_node

    def set_at_index(self, data, idx):
        if idx > len(self):
            raise IndexError('Index out of bounds')
        if self.is_empty():
            self.insert_at_head(data)
        else:
            self._get_node_at_index(idx).data = data

    def remove_head(self):
        """Pops the item at head, and return it"""
        if self.is_empty():
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
        for item in self:
            if value == item.data:
                previousNode.next = item.next
                self.size -= 1
                return item.data
            previousNode = item

    def calculate_size(self):
        count = 0
        for node in self:
            count += 1
        return count
