class Node(object):

    def __init__(self, val):
        self.data = val
        self.next = None


class CircularLinkedList(object):

    """
    You enqueue in the tail and dequeue from head
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        n = Node(val)

        if not self.head:
            self.head = self.tail = n
            self.tail.next = self.head
        else:
            self.tail.next = n
            self.tail = self.tail.next
            self.tail.next = self.head

    def dequeue(self):

        if not self.head:
            raise Exception('Queue empty')
        res = self.head.data
        """
        If there is a single element in the queue
        and if you do 
        
            self.tail.next = self.head.next
            self.head = None
            
        Then only the reference to self.head is set
        to None whereas self.tail.next is still 
        pointing to that old object, so you have to
        be carefull to set all the references to None
        
        
        Also, since tail is pointing to an old obj, the
        next of that old obj is still pointing to another
        old obj so when you dequeue you'll still be getting
        all old objs
        """

        if self.head.next is self.head:
            self.tail.next = None
            self.head = None
        else:
            self.tail.next = self.head.next
            self.head = self.head.next
        return res