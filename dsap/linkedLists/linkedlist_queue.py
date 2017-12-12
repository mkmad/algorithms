class Node(object):

    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedListQueue(object):
    '''
    Note the difference in how you grow the linked list
    between queue and stack
    '''
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        n = Node(val)
        if not self.head:
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = self.tail.next

    def dequeue(self):
        if not self.head:
            raise Exception('Queue empty')
        res = self.head.data
        self.head = self.head.next
        return res