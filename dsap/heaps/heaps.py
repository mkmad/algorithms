from build_heap import BuildHeap as bh


class MinHeap(object):

    def __init__(self):
        self.myHeap = []

    def get_parent(self, index):
        """
        gets the parent based on zero index
        """
        if index:
            return ((index + 1) / 2) - 1
        else:
            return 0

    def get_left_child(self, node):
        """
        Get the left child based on zero index
        2i

        note the + 1 and -1 this is done because
        in a zero based index 2i will be 2 * 0 and
        that is not the left node
        """
        index = ((node + 1) * 2) - 1
        if index <= len(self.myHeap) - 1:
            return index

    def get_right_child(self, node):
        """
        Get the right child 2i + 1
        Note the -2
        """
        index = ((node + 2) * 2) - 2
        if index <= len(self.myHeap) - 1:
            return index

    def get_small_child(self, node):
        """
        Its safe to assume that if a node has child/children
        it will always fill the left child first.
        """
        left = self.get_left_child(node)
        right = self.get_right_child(node)
        small = None
        if left:
            small = left
            if right and self.myHeap[right] < self.myHeap[left]:
                small = right
        return small

    def swap(self, a, b):
        self.myHeap[a], self.myHeap[b] = \
            self.myHeap[b], self.myHeap[a]

    def upheap(self, index):
        """
        Called when inserting, basically bubble the inserted node upward
        to satisfy parent <= children
        """
        if index and not index > len(self.myHeap) -1:
            if self.myHeap[index] < self.myHeap[self.get_parent(index)]:
                self.swap(index, self.get_parent(index))
                self.upheap(self.get_parent(index))

    def downheap(self, index):
        """
        Used when removing min, this is opposite of upheap ie bubble the
        root node downwards untill it satisfies parent <= children.

        Make sure you swap only when the heap property is violated
        """
        if not index > len(self.myHeap) -1:
            small = self.get_small_child(index)
            # Todo: I missed this condition, so be carefull
            if small and self.myHeap[index] > self.myHeap[small]:
                self.swap(index, small)
                self.downheap(small)

    def get_min(self):
        if self.myHeap:
            return self.myHeap[0]

    def get_min_data(self):
        return self.get_min().data

    def remove_min(self):
        """
        Remove the min, copy the last node to root, pop the last node
        and call downheap on root

        Make sure you swap only when the heap property is violated
        """
        if self.myHeap:
            min_ = self.get_min()
            if len(self.myHeap) > 1:
                self.swap(0, len(self.myHeap) - 1)
                self.myHeap.pop()
                self.downheap(0)
            else:
                self.myHeap.pop()
            return min_
        else:
            raise Exception('Empty Heap')

    def insert(self, val):
        """
        Insert in the last node and call upheap on that
        """
        self.myHeap.append(val)
        if len(self.myHeap) > 1:
            self.upheap(len(self.myHeap) - 1)

    def initialize_heap(self):
        self.myHeap = bh().build_val_heap()
