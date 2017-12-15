class DoubleEndedQueue(object):

    """
    Maintain two stacks, one for enqueue from front
    and one for enqueue from back.

    Be careful of the array indices, especially
    when the array is not initialized

    """
    def __init__(self):
        self.front_queue = []
        self.back_queue = []
        self.fq_head, self.fq_tail = 0, 0
        self.bq_head, self.bq_tail = 0, 0

    def enqueue_front(self, val):
        if self.fq_head == 0 and self.bq_tail == 0 or self.fq_head:
            self.front_queue.append(val)
            self.fq_head += 1
        elif self.fq_head == 0 and self.bq_tail != 0:
            self.bq_tail -= 1
            self.back_queue[self.bq_tail] = val

    def enqueue_back(self, val):
        if self.bq_head == 0 and self.fq_tail == 0 or self.bq_head:
            self.back_queue.append(val)
            self.bq_head += 1
        elif self.bq_head == 0 and self.fq_tail != 0:
            self.fq_tail -= 1
            self.front_queue[self.fq_tail] = val

    def dequeue_front(self):
        if self.fq_head == 0 and self.bq_head == self.bq_tail:
            raise Exception('Queue Empty')
        elif self.fq_head == 0:
            res = self.back_queue[self.bq_tail]
            self.bq_tail += 1
            return res
        else:
            res = self.front_queue[self.fq_head - 1]
            self.fq_head -= 1
            return res

    def dequeue_back(self):
        if self.bq_head == 0 and self.fq_head == self.fq_tail:
            raise Exception('Queue Empty')
        elif self.bq_head == 0:
            res = self.front_queue[self.fq_tail]
            self.fq_tail += 1
            return res
        else:
            res = self.back_queue[self.bq_head -1]
            self.bq_head -= 1
            return res

    def print_queue(self):
        print '{0} {1}'.format(self.back_queue, self.front_queue)
