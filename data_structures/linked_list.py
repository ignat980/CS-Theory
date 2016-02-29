from warnings import warn


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
    def __init__(self, *data):
        """Initalizes a linked list from a list of data
        """
        # empty LinkedList
        self.head = None
        self.size = 0
        self.tail = None
        for datum in data:
            self['new tail'] = datum

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
        if isinstance(idx, str):
            if idx == 'head':
                return self.set_at_index(0, value)
            elif idx == 'new head':
                return self.insert_at_head(value)
            elif idx == 'tail':
                return self.set_at_index(-1, value)
            elif idx == 'new tail':
                return self.insert_at_tail(value)
            else:
                raise LookupError('{} is not defined for set'.format(idx))
        elif isinstance(idx, int):
            return self.set_at_index(idx, value)

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
            # Make copy
            l = LinkedList()
            if not self:
                return l
            start = idx.start or 0
            end = idx.stop or len(self)
            if start < 0:
                start = len(self) + start
                if start < 0:
                    start = 0
            if start >= len(self):
                return l
            if end < 0:
                end = len(self) + end
                if end < 0:
                    end = 0
            if end > len(self):
                end = len(self)
            count = start
            if idx.step is None:
                current = self._get_node_at_index(start)
                while count < end:
                    l['new tail'] = current.data
                    current = current.next
                    count += 1
            elif idx.step == -1:
                current = self._get_node_at_index(start)
                while count < end:
                    l['new head'] = current.data
                    current = current.next
                    count += 1
            else:
                warn('Stepping more than 1 at a time is discouraged,'
                     ' turn into python list then use negative slice',
                     RuntimeWarning)
                #  TODO: implement stepping more than once through
            return l
        else:
            raise LookupError('{} not defined for geting in linked list'.format(idx))

    def __delitem__(self, idx):
        if isinstance(idx, str):
            if idx == 'head':
                return self.remove_head()
            elif idx == 'tail':
                return self.remove_tail()
            else:
                raise LookupError("{} not defined for removing in linked list".format(idx))
        elif isinstance(idx, int):
            return self.remove_at_index(idx)
        else:
            raise LookupError("{} not defined for removing in linked list")

    def calculate_size(self):
        count = 0
        for node in self:
            count += 1
        return count

    def is_empty(self):
        return not bool(self.size)

    def __bool__(self):
        return bool(self.size)

    def insert_at_index(self, idx, data):
        if idx == 0:
            return self.insert_at_head(data)
        if idx == -1 or idx == len(self):
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
        if idx == len(self) or not self and idx is -1:
            self.insert_at_tail(value)
        elif idx == -1:
            self.tail.data = value
        elif idx < -1:
            if idx == -len(self):
                return self.insert_at_head(value)
            idx = len(self) + idx
            print(idx, value)
            self._get_node_at_index(idx).data = value
        else:
            self._get_node_at_index(idx).data = value

    def remove_head(self):
        """Removes the value at head"""
        if not self:
            raise ValueError('List is empty')
        self.head = self.head.next
        self.size -= 1

    def pop_head(self):
        """Removes the value at head, and returns it"""
        if not self:
            raise ValueError('List is empty')
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def remove_tail(self):
        """Removes the value at tail"""
        if not self:
            raise ValueError('List is empty')
        self.tail = self._get_node_at_index(-2)
        self.tail.next = None
        self.size -= 1

    def pop_tail(self):
        """Removes the value at tail and returns it"""
        if not self:
            raise ValueError('List is empty')
        data = self.tail.data
        self.tail = self._get_node_at_index(-2)
        self.tail.next = None
        self.size -= 1
        return data

    def remove_at_index(self, idx):
        if idx == 0:
            return self.remove_head()
        if idx == -1 or idx == len(self):
            return self.remove_tail()
        before_node = self._get_node_at_index(idx - 1)
        del before_node.data
        before_node.next = before_node.next.next
        self.size -= 1

    def remove_item(self, value):
        """Removes the value from the list"""
        if not self:
            raise ValueError('List is empty')
        previousNode = self.head
        if value == self.head.data:
            self.remove_head()
            return
        for node in self._node_iterator():
            if value == node.data:
                previousNode.next = node.next
                self.size -= 1
                return
            previousNode = node
        raise ValueError('Value not in linked list')

    def pop_item(self, value):
        """Removes the value from the list and returns it"""
        if not self:
            raise ValueError('List is empty')
        previousNode = self.head
        if value == self.head.data:
            return self.pop_head()
        for node in self._node_iterator():
            if value == node.data:
                previousNode.next = node.next
                self.size -= 1
                return node.data
            previousNode = node
        raise ValueError('Value not in linked list')

    def _remove_node(self, node):
        if node == self.head:
            self.head = self.head.next
        if node.next is None:
            raise ValueError("Node {} can not be removed".format(node))
        node.data = node.next.data
        node.next = node.next.next

    def __contains__(self, value):
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
