class CommonAncestor(object):

    """
    Goal is to find the common ancestor of a binary
    tree.

    Note: This is binary tree not BST

    idea is to do two dfs and maintain the paths to
    each of the node, then we verify the paths and check
    where they have diverged
    """

    def __init__(self):
        self.root = None

    class Node(object):
        def __init__(self):
            self.data = None
            self.left = None
            self.right = None

    def dfs(self, node, target, path):
        """
        I start appending the nodes to the path
        only if I get back a True from the sub calls.

        Note: you need to remember to propagate the
        the bool value all the way to the root
        """
        if node:
            if node.data == target:
                path.append(node.data)
                return True
            else:
                if node.left:
                    if self.dfs(node.left, target, path):
                        path.append(node.data)
                        return True
                if node.right:
                    if self.dfs(node.right, target, path):
                        path.append(node.data)
                        return True

                return False

    def find_common_ancesstor(self, p, q):
        """
        Call dfs for p & q and populate the paths.
        Later use these paths to check for the
        node that diverged
        """
        path1 = []
        path2 = []

        self.dfs(self.root, p, path1)
        if not path1:
            raise Exception('Node {0} doesnt exist'.format(p))
        self.dfs(self.root, q, path2)
        if not path2:
            raise Exception('Node {0} doesnt exist'.format(q))

        l1 = len(path1) - 1
        l2 = len(path2) - 1

        print
        print '\nPath for {0} is:'.format(p)
        print path1
        print '\nPath for {0} is:'.format(q)
        print path2

        # Check where paths have diverged
        # Note: since the paths are in reverse order
        # we check it from right to left
        while l1 >= 0 and l2 >= 0:
            if path1[l1] != path2[l2]:
                print '\nCommon Ancestor is {0}'.format(path1[l1 + 1])
                break
            else:
                l1 -= 1
                l2 -= 1

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
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    c = CommonAncestor()

    c.populate_tree(a, None)
    print "\nBFS traversal of tree is:"
    c.print_tree()

    c.find_common_ancesstor(1, 4)
