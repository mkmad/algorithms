class BSTSequences(object):

    def __init__(self):
        self.root = None

    class Node(object):
        def __init__(self):
            self.data = None
            self.left = None
            self.right = None

    @staticmethod
    def select_val_from_sequences(array_):
        """
        Note how I can select the value from an array/string

        For any given array/string if I pick a value/char at
        position i then the remainder of the array/string can
        be calculated as:

        array[:i] + array[i + 1:]

        Eg:

        a = ['cat', 'dog', 'fish']

        If I pick 'cat' at position 0 then:
        a[:0] + a[1:] -> ['dog', 'fish']


        If I pick 'dog' at position 1 then:
        a[:1] + a[2:] -> ['cat', 'fish']

        Another eg:

        a = "mohan"

        a[:2] + a[3:] -> 'moan'

        """
        for i in range(len(array_)):
            yield (array_[i], array_[:i] + array_[i + 1:])

    def generate_permutations(self):
        pass

    def select_val_from_sequences_demo(self, array_):
        print '\nArray is:'
        print array_
        print '\nDemo of Selecting values from the array:'
        print
        for val in self.select_val_from_sequences(array_):
            print 'Selecting {0}'.format(val[0])
            print val[1]
            print

    def populate_tree(self, a, root):
        """
        I am trying to populate the tree from a sorted list.
        Goal is to get the mid value and add it to the current
        node, if there are values to the left of mid then I pass
        the left array and the current node (which becomes the parent
        in the next call). The same goes to values to the right of
        mid (if any)

        Couple of things to note:

        while calculating mid, you need to be careful if len(a) is
        1 and 0 because len(a) / 2 will be 0 for both the lengths.
        If the length is 0 then there is no point in moving forward

        Secondly, when you are recursively calling the function for
        values that are in the left and the right of mid you need to
        make sure you pass array[:mid] for left and array[mid + 1:] for
        right. This is because the upper limit is automatically ignored
        and the lower limit is not. There will be complications if the
        mid value is passed (especially when calling with right values)

        """
        mid = (len(a) / 2)
        if mid >= 0 and len(a) >= 1:
            if not root:
                if not self.root:
                    self.root = self.Node()
                    self.root.data = a[mid]
                    self.populate_tree(a[:mid], self.root)
                    self.populate_tree(a[mid + 1:], self.root)
            else:
                if a[mid] < root.data:
                    root.left = self.Node()
                    root.left.data = a[mid]
                    self.populate_tree(a[:mid], root.left)
                    self.populate_tree(a[mid + 1:], root.left)
                else:
                    root.right = self.Node()
                    root.right.data = a[mid]
                    self.populate_tree(a[:mid], root.right)
                    self.populate_tree(a[mid + 1:], root.right)

    def bfs(self, nodes=[]):
        """
        Used just to print the tree
        """
        if nodes:
            temp = []
            for i in nodes:
                # This is a hack to insert a unbalanced node
                # as the populate_tree algorithm always creates
                # a balanced node
                print i.data,
                # Todo: Make sure you append only if the child is present else you'll
                # Todo: have array with None values.
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            self.bfs(temp)

    def print_tree(self):
        self.bfs([self.root])


if __name__ == '__main__':
    b = BSTSequences()
    inp = [1, 2, 3, 4, 5, 6, 7, 8]
    b.populate_tree(inp, None)
    b.select_val_from_sequences_demo(inp)
