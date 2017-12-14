class MinHeap(object):

    def __init__(self):
        self.myHeap = []

    def get_parent(self, index):
        if index:
            return ((index + 1) / 2) - 1
        else:
            return 0

    def get_left_child(self, node):
        index = ((node + 1) * 2) - 1
        if index <= len(self.myHeap) - 1:
            return index

    def get_right_child(self, node):
        index = ((node + 2) * 2) - 2
        if index <= len(self.myHeap) - 1:
            return index

    def get_small_child(self, node):
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
        if index and not index > len(self.myHeap) -1:
            if self.myHeap[index] < self.myHeap[self.get_parent(index)]:
                self.swap(index, self.get_parent(index))
                self.upheap(self.get_parent(index))

    def downheap(self, index):
        if not index > len(self.myHeap) -1:
            small = self.get_small_child(index)
            if small:
                self.swap(index, small)
                self.downheap(small)

    def get_min(self):
        if self.myHeap:
            return self.myHeap[0]

    def remove_min(self):
        if self.myHeap:
            min = self.get_min()
            if len(self.myHeap) > 1:
                self.swap(0, len(self.myHeap) -1)
                self.myHeap.pop()
                self.downheap(0)
            else:
                self.myHeap.pop()
            return min

    def insert(self, val):
        self.myHeap.append(val)
        if len(self.myHeap) > 1:
            self.upheap(len(self.myHeap) - 1)

