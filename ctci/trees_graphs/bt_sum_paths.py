class SumPaths(object):

    """
    Goal is to find all possible paths that
    add to a particular sum
    """

    class Node(object):
        def __init__(self):
            self.data = None
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.res = []

    def populate_tree(self):
        """
        Building this tree

                  10
                /   \
               5    -3
              /   \   \
             3    1   10
            / \    \
           3  -2    2
        """

        n1 = self.Node()
        n1.data = 10

        n2 = self.Node()
        n2.data = 5

        n3 = self.Node()
        n3.data = -3

        n1.left = n2
        n1.right = n3

        n4 = self.Node()
        n4.data = 3

        n5 = self.Node()
        n5.data = 2

        n2.left = n4
        n2.right = n5

        n6 = self.Node()
        n6.data = 10

        n3.right = n6

        n7 = self.Node()
        n7.data = 3

        n8 = self.Node()
        n8.data = -2

        n4.left = n7
        n4.right = n8

        n9 = self.Node()
        n9.data = 2

        n5.right = n9

        self.root = n1

    def bfs(self, nodes=[]):
        """
        Used just to print the tree and fetching nodes on a
        level by level basis
        """
        if nodes:
            temp = []
            nodes_ = []
            for i in nodes:
                print i.data,
                nodes_.append(i.data)
                # Todo: Make sure you append only if the child is present else you'll
                # Todo: have array with None values.
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            print
            self.bfs(temp)

    def print_tree(self):
        print '\nBst traversal of the tree:'
        self.bfs([self.root])

    def get_sum_paths(self, node, target, r_sum=0, path=""):
        """
        Maintain a running sum and running path. If you
        the running sum plus the node's val is the target then
        add the path to result
        """
        if node:
            if node.data + r_sum == target:
                self.res.append(path + str(node.data))
            elif node.data + r_sum < target:
                r_sum = node.data + r_sum
                if node.left:
                    self.get_sum_paths(node.left, target, r_sum=r_sum,
                                       path=path + str(node.data) + " ")
                if node.right:
                    self.get_sum_paths(node.right, target, r_sum=r_sum,
                                       path=path + str(node.data) + " ")


if __name__ == '__main__':
    s = SumPaths()
    s.populate_tree()
    s.print_tree()
    s.get_sum_paths(s.root, 17)
    print
    print 'All paths for 17 is:'
    print s.res

