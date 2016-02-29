from linkedList import LinkedList


class Queue(object):
    """Queue data structure, FIFO."""
    def __init__(self, data=None):
        """If data is a LinkedList, then it makes a shallow copy"""
        self.ll = LinkedList()
        if data is not None:
            if isinstance(data, LinkedList):
                self.ll = data
            else:
                self.ll.insert_at_head(data)

    def enqueue(self, data):
        self.ll.insert_at_tail(data)

    def dequeue(self):
        ...

    def peek(self):
        return self.ll.get_at_head

    def __len__(self):
        return len(self.ll)

    def size(self):
        return len(self.ll)
