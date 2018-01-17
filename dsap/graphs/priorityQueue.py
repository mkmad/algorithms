
class PriorityQueue(object):
    """
    This is the same code as heap, instead of inserting
    values, I am inserting nodes and expect each node
    has a value associated with it.

    I also have a location dict that store the location/index
    of a given node at any given point of time. This dict
    can be used to retrieve nodes/check if nodes exist in
    constant time
    """

    def __init__(self):
        self.myHeap = []
        self.location = {}

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

    def get_small_child(self, index):
        """
        Its safe to assume that if a node has child/children
        it will always fill the left child first.
        """
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        small = None
        if left:
            small = left
            if right and self.myHeap[right].data < self.myHeap[left].data:
                small = right
        return small

    def swap(self, a, b):
        """
        Note: Update the location dict after swap
        """
        self.myHeap[a], self.myHeap[b] = \
            self.myHeap[b], self.myHeap[a]

        # Update the location dict accordingly
        if self.myHeap[a].label and self.myHeap[b].label:
            self.location[self.myHeap[a].label] = b
            self.location[self.myHeap[b].label] = a

    def upheap(self, index):
        """
        Called when inserting, basically bubble the inserted node upward
        to satisfy parent <= children
        """
        if index and not index > len(self.myHeap) -1:
            if self.myHeap[index].data < self.myHeap[self.get_parent(index)].data:
                self.swap(index, self.get_parent(index))
                self.upheap(self.get_parent(index))

    def downheap(self, index):
        """
        Used when removing min, this is opposite of upheap ie bubble the
        root node downwards untill it satisfies parent <= children.

        Make sure you swap only when the heap property is violated
        """
        if not index > len(self.myHeap) - 1:
            small = self.get_small_child(index)
            # Todo: I missed this condition, so be carefull
            if small and self.myHeap[index].data > self.myHeap[small].data:
                self.swap(index, small)
                self.downheap(small)

    def get_min(self):
        if self.myHeap:
            return self.myHeap[0]

    def remove_min(self):
        """
        Remove the min, copy the last node to root, pop the last node
        and call downheap on root. Make sure you swap only when the
        heap property is violated

        Note: Update the location dict after remove min

        """
        if self.myHeap:
            min_ = self.get_min()
            if len(self.myHeap) > 1:
                self.swap(0, len(self.myHeap) - 1)
                self.myHeap.pop()
                self.downheap(0)

                # Delete the poped node
                del self.location[min_.label]

                # update the location dict after downheap
                for i, v in enumerate(self.myHeap):
                    self.location[v.label] = i
            else:
                self.myHeap.pop()
                del self.location[min_.label]

            return min_
        else:
            raise Exception('Empty Heap')

    def insert(self, node):
        """
        Insert in the last node and call upheap on that

        Note: Update the location dict after insert
        """
        self.myHeap.append(node)

        if len(self.myHeap) > 1:
            self.upheap(len(self.myHeap) - 1)

            # update the location dict after upheap
            for i, v in enumerate(self.myHeap):
                self.location[v.label] = i

    def update(self, vertex, value):
        """
        Update any given node's value and call downhep/upheap
        accordingly
        """

        if vertex in self.location:
            self.myHeap[self.location[vertex]].data = value
            small = self.get_small_child(self.location[vertex])
            parent = self.get_parent(self.location[vertex])
            if small:
                if value > self.myHeap[small].data:
                    self.downheap(self.location[vertex])
            if parent:
                if value < self.myHeap[parent].data:
                    self.upheap(self.location[vertex])
