from copy import deepcopy


class HeapSort(object):

    """
    All the functions except heapsort are irrelevant,
    just just help the downheap function.
    """

    def __init__(self):
        self.val_heap = [4, 5, 3, 6, 7, 2, 9, 3]
        self.obj_heap = []
        self.limit = len(self.val_heap) - 1

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

    def get_left_child(self, node):
        """
        Get the left child based on zero index
        2i
        """
        index = ((node + 1) * 2) - 1
        if index <= self.limit:
            return index

    def get_right_child(self, node):
        """
        Get the right child 2i + 1
        Note the -2
        """
        index = ((node + 2) * 2) - 2
        if index <= self.limit:
            return index

    @staticmethod
    def swap(a, b, heap):
        heap[a], heap[b] = \
            heap[b], heap[a]

    def get_big_child(self, node, heap, isObj=False):
        """
        Its safe to assume that if a node has child/children
        it will always fill the left child first.
        """
        left = self.get_left_child(node)
        right = self.get_right_child(node)
        big = None
        if left:
            big = left
            if isObj:
                if right and heap[right].data > heap[left].data:
                    big = right
            else:
                if right and heap[right] > heap[left]:
                    big = right
        # TODO: This is the sentinal variable.
        # TODO: I missed this condition, I was relying on the get_child_x
        # TODO: functions to ignore the sorted elements, but they just
        # TODO: check if index < self.limit where index is parent's index
        if big < self.limit:
            return big

    def downheap(self, index, heap, isObj=False):
        """
        Used when removing min, this is opposite of upheap ie bubble the
        root node downwards untill it satisfies parent <= children.

        Make sure you swap only when the heap property is violated
        """
        if not index > self.limit:
            big = self.get_big_child(index, heap, isObj)
            # Todo: I missed this condition, so be carefull
            if isObj:
                if big and heap[index].data < heap[big].data:
                    self.swap(index, big, heap)
                    self.downheap(big, heap, isObj)
            else:
                if big and heap[index] < heap[big]:
                    self.swap(index, big, heap)
                    self.downheap(big, heap)

    def build_max_heap(self):
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

    def heapsort(self):
        """
        This is basically like remove max function, except poping the
        value from the right, you just ignore the last sorted index
        for the next down heap call. This will ensure that all the
        large values will be stored at the end of the array

        Runtime: nlog(n)
        Space: o(n)
        """
        array_ = self.build_max_heap()
        print array_
        for val in range(len(array_) - 1, -1, -1):
            self.swap(val, 0, array_)
            # This variable  will let downheap/get_big_child function
            # know to ignore the sorted element.
            self.limit -= 1
            self.downheap(0, array_)
        print array_


if __name__ == '__main__':
    hs = HeapSort()
    hs.heapsort()
