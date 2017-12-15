class CircularQueue(object):

    """

    This queue will only take in a limited number of
    values, because if we simply keep inserting the values
    then there is no point in wrapping around.
    To help with this we need two pointers a head and a tail.

    On the other hand we can do enqueue with resize, this
    will ensure there are fixed number of values and we know
    when the head/tail will wrap around.

    We enqueue using the head and dequeue using the
    tail. Both tail and head will wrap around.

    self.count will help in deciding whether a queue
    is full or not. Because if I rely on head or
    tail to decide whether a queue is full or not then
    there are some complexities eg:

    How to say if a queue is empty/full when head and tail
    both are 0, since both the values are wrapping
    around and we don't know.

    """

    def __init__(self):
        self.Queue_size = 10
        self.myQueue = [None] * self.Queue_size
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, val):
        if self.count == self.Queue_size:
            raise Exception('Queue is full')
        self.myQueue[self.tail] = val
        self.tail = (self.tail + 1) % self.Queue_size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception('Queue is empty')
        res, self.myQueue[self.head] = self.myQueue[self.head], None
        self.head = (self.head + 1) % self.Queue_size
        self.count -= 1
        return res

    def print_queue(self):
        print self.myQueue
        print self.count

    def enqueue_with_resize(self, val):
        temp = [None] * self.Queue_size
        self.myQueue.extend(temp)
        self.Queue_size *= 2
        # Tail needs to be declared before writing the value into the
        # queue because value of tail would already have been wrapped
        # Todo: Watch for all the variables in any function, I screwed up the tail
        # Todo: value couple of times here before getting it right
        self.tail = self.Queue_size / 2
        self.myQueue[self.tail] = val

    @property
    def getQueueSize(self):
        return self.Queue_size


