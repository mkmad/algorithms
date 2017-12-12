class Node(object):

    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        n = Node(val)
        if not self.head:
            self.head = self.tail = n

        else:
            self.tail.next = n
            self.tail.next.prev = self.tail
            self.tail = n

    def dequeue(self):
        if not self.head:
            raise Exception('Queue Empty')
        data = self.head.data
        self.head = self.head.next
        if self.head:                # Note: self.head might be None
            self.head.prev = None
        return data

    def del_node(self, val):
        cur = self.head
        if not self.head:
            raise Exception('Empty queue')
        while cur.data != val:
            cur = cur.next
            if cur is None:
                break
        if cur:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur = None
        else:
            raise Exception('Element not found')

    def print_queue(self):
        if not self.head:
            raise Exception('Empty queue')
        cur = self.head
        while cur:
            print cur.data
            cur = cur.next