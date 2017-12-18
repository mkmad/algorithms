from copy import deepcopy


class BuildHeap(object):

    """
    All the functions except build_val_heap and build_obj_heap
    are irrelevant, just just help the downheap function.
    """

    def __init__(self):
        self.val_heap = [4, 5, 3, 6, 7, 2, 9, 3]
        self.obj_heap = []

    class Node(object):
        def __init__(self, data):
            self.data = data

    @staticmethod
    def get_parent(index):
        """
        gets the parent based on zero index
        """
        if index:
            return ((index + 1) / 2) - 1
        else:
            return 0

    @staticmethod
    def get_left_child(node, heap):
        """
        Get the left child based on zero index
        2i
        """
        index = ((node + 1) * 2) - 1
        if index <= len(heap) - 1:
            return index

    @staticmethod
    def get_right_child(node, heap):
        """
        Get the right child 2i + 1
        Note the -2
        """
        index = ((node + 2) * 2) - 2
        if index <= len(heap) - 1:
            return index

    @staticmethod
    def swap(a, b, heap):
        heap[a], heap[b] = \
            heap[b], heap[a]

    @classmethod
    def get_small_child(cls, node, heap, isObj=False):
        """
        Its safe to assume that if a node has child/children
        it will always fill the left child first.
        """
        left = cls.get_left_child(node, heap)
        right = cls.get_right_child(node, heap)
        small = None
        if left:
            small = left
            if isObj:
                if right and heap[right].data < heap[left].data:
                    small = right
            else:
                if right and heap[right] < heap[left]:
                    small = right
        return small

    @classmethod
    def downheap(cls, index, heap, isObj=False):
        """
        Used when removing min, this is opposite of upheap ie bubble the
        root node downwards untill it satisfies parent <= children.

        Make sure you swap only when the heap property is violated
        """
        if not index > len(heap) -1:
            small = cls.get_small_child(index, heap, isObj)
            # Todo: I missed this condition, so be carefull
            if isObj:
                if small and heap[index].data > heap[small].data:
                    cls.swap(index, small, heap)
                    cls.downheap(small, heap, isObj)
            else:
                if small and heap[index] > heap[small]:
                    cls.swap(index, small, heap)
                    cls.downheap(small, heap)

    def build_val_heap(self):
        # TODO: Note how you call downheap from last index down to first index
        """
        You could say that the run time is nlog(n) but a tighter bound
        is o(n) since n is not the same for each iteration.
        """
        # TODO: ^^

        temp = deepcopy(self.val_heap)
        # call downheap with isObj=False
        for val in range(len(temp), -1, -1):
            self.downheap(val, temp, isObj=False)
        return temp

    def build_node_heap(self):
        # TODO: Note how you call downheap from last index down to first index
        """
        You could say that the run time is nlog(n) but a tighter bound
        is o(n) since n is not the same for each iteration.
        """
        # TODO: ^^

        temp = deepcopy(self.val_heap)
        temp_obj = []

        # Create a list of objects
        for val in temp:
            temp_obj.append(self.Node(val))

        # call downheap with isObj=True
        for val in range(len(temp_obj), -1, -1):
            self.downheap(val, temp_obj, isObj=True)
        return temp_obj


if __name__ == '__main__':
    bh = BuildHeap()
    print '\nInitial array'
    print bh.val_heap
    print '\nHeap'
    print bh.build_val_heap()
    print '\nNode Heap'
    for val in bh.build_node_heap():
        print val.data,
