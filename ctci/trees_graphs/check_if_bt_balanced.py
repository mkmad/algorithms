import math


class Balanced(object):
    """
    The concept is simple but I had some problems
    with what to return during recursion

    On one hand I wanted to return True/False based
    on the difference of left height and right height.
    But, if I do that then I wont be giving a int value
    (height) to the upper calls.

    So, this is an important example of how handle input
    and output for recursive programs

    You need to stick to one return type, or terminate the program
    mid way, you can't however, return two different types

    I chose to return inf in case I find in balance in the tree

    """
    class Node(object):
        def __init__(self):
            self.data = None
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.dirty_node = None

    def is_blanced(self, node=None, height=0):
        """
        I am sticking to only returning height
        """
        left = right = height
        if not node:
            return height
        else:
            if node.left:
                left = self.is_blanced(node.left, height=height + 1)
            if node.right:
                right = self.is_blanced(node.right, height=height + 1)

            if math.fabs(left - right) > 1:
                return float('inf')
            else:
                return max(left, right)

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
                if i.data == 1:
                    self.dirty_node = i
                print i.data,
                # Todo: Make sure you append only if the child is present else you'll
                # Todo: have array with None values.
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            self.bfs(temp)

    def add_dirty_node(self):
        if self.dirty_node:
            self.dirty_node.left = self.Node()
            self.dirty_node.left.data = 0

    def print_tree(self):
        self.bfs([self.root])


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = Balanced()

    b.populate_tree(a, None)

    print "\nBFS traversal of tree is:"
    b.print_tree()

    print "\n\nTree height is:"
    if b.is_blanced(b.root) == float('inf'):
        print 'Unbalanced'
    else:
        print 'Balanced'

    print "\n\nAdding Dirty node - 0"
    b.add_dirty_node()
    print "BFS traversal of tree after adding dirty node is:"
    b.print_tree()

    print "\n\nTree height is:"
    if b.is_blanced(b.root) == float('inf'):
        print 'Unbalanced'
    else:
        print 'Balanced'
