class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = data

    def __repr__(self):
        return 'Node(' + repr(self.data) + ')'


class Stack(object):
    def __init__(self, *data):
        self.size = 0
        self.head = None
        for datum in reversed(data):
            self.push(datum)

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
        self.size += 1

    def pop(self):
        if self.head is None:
            raise ("Stack is empty")
        else:
            data = self.head.data
            self.head = self.head.next
        self.size -= 1
        return data

    def peek(self):
        return self.head.data


def fix_stack(stack):
    if stack.size == 2:
        before_last = stack.pop()
        last = stack.pop()
        stack.push(before_last)
        stack.push(last)
        print("Swapping", before_last, "and", last)
    else:
        element = stack.pop()
        fix_stack(stack)
        stack.push(element)


def test():
    stack = Stack(1, 2, 3, 4, 5, 6, 8, 7)
    fix_stack(stack)

if __name__ == '__main__':
    test()
