from mycode.dsap.trees.bst_operations import BSTOperations as bsto
from mycode.dsap.trees import populate_tree as pt


class SplayTree(object):

    """
    Refer to page 490, its pretty straightforward
    """
    def __init__(self):
        self.root = None
        self.bsto = bsto()

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.parent = None
            # label is just for my reference
            self.lable = None

    def findNode(self, val, node):
        """
        Find the node and splay on that node
        """
        if node:
            if node.data == val:
                self.splay(node)
            else:
                if val < node.data:
                    if node.left:
                        self.findNode(val, node.left)
                    else:
                        self.splay(node)
                else:
                    if node.right:
                        self.findNode(val, node.right)
                    else:
                        self.splay(node)
        else:
            raise Exception('Node required')

    def insert(self, val):
        """
        Insert and then splay on the inserted node
        """
        if val:
            node = self.Node(val)
            self.bsto.insert_node(node, self.root)
            self.splay(node)
        else:
            raise Exception('Value is required')

    def delete(self, val):
        """
        Delete and then splay on the successor's parent or
        leaf's parent (depending on the case)
        """
        if val:
            node = self.bsto.delete(val, self.root)
            self.splay(node)
        else:
            raise Exception('Value required')

    def left_rotation(self, a, b):
        if a.left:
            temp = a.left
            a.left = b
            b.right = temp
        else:
            a.left = b
            b.right = None

        # TODO: Update the parent's reference to a
        if b.parent:
            if b is b.parent.left:
                b.parent.left = a
            else:
                b.parent.right = a

        # TODO: Make sure to update the parent of a and b
        a.parent = b.parent
        b.parent = a

    def right_rotation(self, a, b):
        if a.right:
            temp = a.right
            a.right = b
            b.left = temp
        else:
            a.right = b
            b.left = None

        # TODO: Update the parent's reference to a
        if b.parent:
            if b is b.parent.left:
                b.parent.left = a
            else:
                b.parent.right = a

        # TODO: Make sure to update the parent of a and b
        a.parent = b.parent
        b.parent = a

    def restructure(self, x, y, z):
        # Zig-Zig or Zig-Zag
        if all([x, y, z]):
            if x is y.left:
                if y is z.left:
                    # Zig-Zig
                    self.right_rotation(y, z)
                    self.right_rotation(x, y)
                else:
                    # Zig-Zag
                    self.right_rotation(x, y)
                    self.left_rotation(x, z)
            else:
                if y is z.left:
                    # Zig-Zag
                    self.left_rotation(x, y)
                    self.right_rotation(x, z)

                else:
                    # Zig-Zig
                    self.left_rotation(y, z)
                    self.left_rotation(x, y)
        # Zig
        elif all([x, y]):
            if x is y.left:
                self.right_rotation(x, y)
            else:
                self.left_rotation(x, y)

    def splay(self, node):
        if node:
            x = node
            y = None
            z = None

            if node.parent:
                y = node.parent
            if y:
                if y.parent:
                    z = y.parent

            if z:
                # tri node restructure for splay
                self.restructure(x, y, z)
                # Splay all the way upto root
                self.splay(x)
            else:
                if y:
                    # Dual node restructure if there is no z
                    self.restructure(x, y, None)
                    # In this case we need one more splay
                    self.splay(x)
                else:
                    # If there is no y, then root is reached
                    self.root = x
                    return

    def bfs(self, nodes=[]):
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
            self.bfs(temp)

    def print_tree(self):
        self.bfs([self.root])


if __name__ == '__main__':
    st = SplayTree()
    st.root = pt.populate()
    print '\nTree before any operation'
    st.print_tree()
    print '\nFind 7'
    st.findNode(7, st.root)
    st.print_tree()
    print '\nInsert 10'
    st.insert(10)
    st.print_tree()
    print '\nDelete 2'
    st.delete(2)
    st.print_tree()
