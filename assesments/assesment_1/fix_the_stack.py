class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = data

    def __repr__(self):
        return 'Node(' + repr(self.data) + ')'


class Stack(object):
    def __init__(self, *data):
        self.size = 0
        pass

    def push(self, data):
        self.size += 1
        pass

    def pop(self, data):
        pass

    def peek(self):
        pass


def fix_stack(stack):
    if stack.size == 2:
        before_last = stack.pop()
        last = stack.pop()
        stack.push(before_last)
        stack.push(last)
    else:
        element = stack.pop()
        fix_stack(stack)
        stack.push(element)
