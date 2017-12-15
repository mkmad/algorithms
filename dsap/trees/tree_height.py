import populate_tree


class Height(object):

    def __init__(self):
        pass

    # Todo: Make a note of the return type and make sure that you are handling that type
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # Todo: Always call the recursive function from another function
    def get_height(self):
        root = populate_tree.populate()
        print 'Height: {0}'.format(self.height(root))

    def node_depth(self, node):
        """
        Height of a node is max of all the heights of its children
        Depth of a node is the the number of ancestors it has.

        So, to implement depth the node should also have the parent
        pointer
        """
        if node:
            return 1 + self.node_depth(node.parent)
        else:
            return 0
