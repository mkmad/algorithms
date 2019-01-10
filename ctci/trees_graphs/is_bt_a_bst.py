import sys


class ValidBST(object):
    """
    Check if a given BT is a BST.

    You can implement a simple recursive
    program that check for the BST condition
    at every node:

    left <= root < right

    This will however return valid for the
    following tree as well

                   20
                  /  \
                10   30
               /  \
              5   25 <- clearly in the wrong place

    It should have been:

                   20
                  /  \
                10   30
                /    /
               5    25

    So, there are two ways to solve this problem:-

    1) Do a in order traversal and check if the output
       is sorted
    2) Implement the above algorithm with limits (min and max)



    I choose the min max approach below:

        At any given node, it checks if

        left is in the range:
        min=node's min < left.data < max=node.data

        right is in the range:

        min=node.data < right.data < max=node's max

        Also note:

            For the nodes that are along the edges (sleeves),
            they might not have minimum (left edges) and may
            not have maximum (right edges). In these cases we just
            check if node.data is either < minimum or > maximum to
            determine the validity of the node's position in the
            tree

    """

    def __init__(self):
        self.root = None

    class Node(object):

        def __init__(self):
            self.data = None
            self.left = None
            self.right = None

    def check_child_nodes(self, node, minimum, maximum):

        if node.left:
            self.check_valid_bst(node.left, minimum, node.data)
        if node.right:
            self.check_valid_bst(node.right, node.data, maximum)

    @staticmethod
    def exit_code():
        print "Not valid tree"
        sys.exit(1)

    def check_valid_bst(self, node, minimum=None, maximum=None):

        if node:
            # case for interior nodes
            if minimum and maximum:
                if not minimum <= node.data < maximum:
                    self.exit_code()

            # cases for exterior (edge) nodes
            elif minimum:
                if node.data < minimum:
                    self.exit_code()

            elif maximum:
                if node.data > maximum:
                    self.exit_code()

            self.check_child_nodes(node, minimum, maximum)

    def populate_tree(self):
        """
        Populate this tree:

               20
              /  \
            10   30
           /  \
          5   25

        """

        # This is a hack to insert a unbalanced node
        # as the populate_tree algorithm always creates
        # a balanced node

        self.root = self.Node()
        self.root.data = 20

        self.root.left = self.Node()
        self.root.left.data = 10

        self.root.right = self.Node()
        self.root.right.data = 30

        self.root.left.left = self.Node()
        self.root.left.left.data = 5

        # Dirty node
        self.root.left.right = self.Node()
        self.root.left.right.data = 25

        # comment the dirty node and uncomment
        # the node below to get a valid tree

        # self.root.left.right = self.Node()
        # self.root.left.right.data = 15

    def bfs(self, nodes=[]):
        """
        Used just to print the tree
        """
        if nodes:
            temp = []
            for i in nodes:
                print i.data,
                # Todo: Make sure you append only if the child is present else you'll
                # Todo: have array with None values.
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            print
            self.bfs(temp)

    def print_tree(self):
        self.bfs([self.root])


if __name__ == '__main__':
    v = ValidBST()
    print "\nBFS traversal of tree is:"
    v.populate_tree()
    v.print_tree()
    print "\n"
    v.check_valid_bst(v.root)

    # This print statement will get executed only
    # if the control doesn't exit the program
    print "Tree is valid"
