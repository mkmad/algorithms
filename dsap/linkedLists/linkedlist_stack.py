class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack(object):

    """
    Its easier to push/extend/grow from head because
    when you pop you need to maintain a previous pointer
    pointer otherwise.
    """
    def __init__(self):
        self.head = None

    def push(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
        else:
            n.next = self.head
            self.head = n

    def pop(self):
        if not self.head:
            raise Exception('Stack empty')
        res = self.head.data
        self.head = self.head.next
        return res
