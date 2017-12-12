class Queue(object):

    def __init__(self):
        self.myQueue = []
        self.head = 0

    def enqueue(self, val):
        self.myQueue.append(val)

    def dequeue(self):
        if not self.myQueue or self.head > len(self.myQueue) -1:
            raise Exception('Empty Queue')
        self.head += 1
        return self.myQueue[self.head -1]

    def return_head(self):
        if self.myQueue:
            return self.myQueue[self.head]

    def return_tail(self):
        if self.myQueue:
            return self.myQueue[-1]

    def print_queue(self):
        print self.myQueue




