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
    2) Implement the above alogithm with limits (min and max)



    I choose the min max approach below:

        At any given node, it checks if

        left is in:
        min=node's min < left.data < max=node.data

        right is in:

        min=node.data < right.data < max=node's max


        The above range handles two tricky cases (along with the obvious
        ones):

        if the node is right to its parent and we are checking the
        range of the node's left

        and if the node is left to its parent and we are checking
        the range of the node's right

    """

    def __init__(self):
        self.root = None

    class Node(object):

        def __init__(self):
            self.data = None
            self.left = None
            self.right = None

    def check_valid_bst(self, root, min=None, max=None):
        if root:
            if root.left:
                """
                If there is a minimum check if the left node
                falls in the range else check if the left node
                obeys bst property
                
                When calling the function recursively, the max
                the child node can be is root.data and min is min
                (if its not None)
                
                The max val in now like a check point where all the
                node's children and grand children is made sure they
                don't cross this max point later in the recursion
                
                In a way the highest max point is the root node's
                predecessor
                """
                if min:
                    if min <= root.left.data <= root.data:
                        self.check_valid_bst(root.left, min=min, max=root.data)
                    else:
                        print 'Not a valid BST'
                        sys.exit(-1)

                else:
                    if root.left.data <= root.data:
                        self.check_valid_bst(root.left, min=min, max=root.data)
                    else:
                        print 'Not a valid BST'
                        sys.exit(-1)

            if root.right:
                """
                If there is a maximum check if the right node
                falls in the range else check if the right node
                obeys bst property
                
                When calling the function recursively, the min
                the child node can be is root.data and max is max
                (if its not None)
                
                The min val in now like a check point where all the
                node's children and grand children is made sure they
                don't cross this min point later in the recursion
                
                In a way the lowest min point is the root node's successor
                """
                if max:
                    if root.data < root.right.data < max:
                        # Note the +1 on the min value
                        self.check_valid_bst(root.right, min=root.data + 1, max=max)
                    else:
                        print 'Not Valid BST'
                        sys.exit(-1)
                else:
                    if root.data < root.right.data:
                        # Note the +1 on the minimum value
                        self.check_valid_bst(root.right, min=root.data + 1, max=max)
                    else:
                        print 'Not a valid BST'
                        sys.exit(-1)

    def populate_tree(self):
        """
        Populate this tree:

               20
              /  \
            10   30
           /  \
          5   25

        """

        self.root = self.Node()
        self.root.data = 20

        self.root.left = self.Node()
        self.root.left.data = 10

        self.root.right = self.Node()
        self.root.right.data = 30

        self.root.left.left = self.Node()
        self.root.left.left.data = 5

        self.root.left.right = self.Node()
        self.root.left.right.data = 25

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
    v = ValidBST()
    print "\nBFS traversal of tree is:"
    v.populate_tree()
    v.print_tree()
    print "\n"
    v.check_valid_bst(v.root)


