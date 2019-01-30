from dsap.heaps.priorityQueue import PriorityQueue as pq
from dsap.heaps.build_heap import BuildHeap as bh


class HuffmanCoding(object):

    """
    Huffman coding is a data compression algorithm, it compresses
    data in a loss less form.

    The algorithm takes a list of words and its frequencies.
    The frequencies become the data in the priority
    queue node. The actual word itself is the label of the node

    The algorithm takes all the nodes and puts it into a priority
    heap, extract min is done twice and a new node is created such
    that the data = min1.data + min2.data. New node's left = min1 and
    right = min2. This new node is again put back into the priority
    queue

    The above step is repeated until there is only one element in the
    priority queue (i.e. only min1 exists). Return the last node

    The actual huffman coding is done by traversing the tree created
    above, if you go left its 0 and if you go right its 1

    Note: only the leaf nodes will actually contain the words (node
    with label). All the other nodes will only have values (the
    combined frequencies). So, traversing the tree for a word will
    result in going to a left node, witch in turn will result in the
    huffman code

    For info on how the actual bits are compressed checkout
    https://www.youtube.com/watch?v=dM6us854Jk0

    """

    class Node(object):
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.label = None

    def __init__(self):
        self.my_pq = pq()
        self.frequency = {
            'the': 10,
            'moon': 7,
            'saturn': 4,
            'space': 15,
            'galaxy': 3
        }

    def build_node_lists(self):
        heap = []

        for k, v in self.frequency.items():
            node = self.Node(v)
            node.label = k
            heap.append(node)

        return heap

    def build_huffman_tree(self):

        """
        Remove nodes from the priority queue and
        make a new sub tree and insert the root of
        the subtree back into the queue

        If there more than one node in the priority
        queue then continue the process else if there
        is only one node left then that's the root
        of the master tree so return that

        """

        if self.my_pq.myHeap:
            min2 = None
            min1 = self.my_pq.remove_min()
            if self.my_pq.myHeap:
                min2 = self.my_pq.remove_min()

            if min2:
                node = self.Node(min1.data + min2.data)
                node.left = min1
                node.right = min2
                self.my_pq.insert(node)
                self.build_huffman_tree()
            else:
                return min1

    def huffman_coding(self, root, code=''):
        if root:
            if not root.left and not root.right:
                print '{0} has code: {1}'.format(root.label, code)
                return
            if root.left:
                self.huffman_coding(root.left, code=code + '0')
            if root.right:
                self.huffman_coding(root.right, code=code + '1')


if __name__ == '__main__':
    hc = HuffmanCoding()
    b = bh()
    heap = hc.build_node_lists()
    # heapify
    hc.my_pq.myHeap = b.build_heap(heap)
    root = hc.build_huffman_tree()
    print root.data
    hc.huffman_coding(root)









