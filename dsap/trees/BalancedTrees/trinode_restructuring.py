from mycode.dsap.trees import populate_tree as pt
from mycode.dsap.trees.bst_operations import BSTOperations as bsto


class TriNodeRestructuring(object):

    def __init__(self):
        self.root = None

    def restructure(self, node):
        """
        The concept is pretty straightforward, however you
        need to be careful about the self.root pointer. Since
        self.root might still be pointing to the old root even
        after restructuring

        Another case is: what if z is not the root pointer, then
        after trinode restructuring the parent of z will still
        be pointing to z. Hence we need to update the parent of
        z to whichever node (x or y, depending on the case) has
        taken z's previous position. So, for this case we need
        an additional pointer to z'parent
        """
        x = node
        y = x.parent
        z = y.parent
        p = z.parent

        if z:
            if y is z.left:

                if x is y.left:
                    self.right_rotation(y, z)
                    # TODO: Update root pointer, is z is root
                    if z is self.root:
                        self.root = y
                    # TODO: Update z'parent if z is not root
                    else:
                        if z is p.left:
                            p.left = y
                        else:
                            p.right = y
                    return y

                elif x is y.right:
                    self.left_rotation(x, y)
                    self.right_rotation(x, z)
                    # TODO: Update root pointer, if z is root
                    if z is self.root:
                        self.root = x
                    # TODO: Update z'parent if z is not root
                    else:
                        if z is p.left:
                            p.left = x
                        else:
                            p.right = x
                    return x

            elif y is z.right:

                if x is y.right:
                    self.left_rotation(y, z)
                    # TODO: Update root pointer, if z is root
                    if z is self.root:
                        self.root = y
                    # TODO: Update z'parent if z is not root
                    else:
                        if z is p.left:
                            p.left = y
                        else:
                            p.right = y
                    return y

                elif x is y.left:
                    self.right_rotation(x, y)
                    self.left_rotation(x, z)
                    # TODO: Update root pointer, is z is root
                    if z is self.root:
                        self.root = x
                    # TODO: Update z'parent if z is not root
                    else:
                        if z is p.left:
                            p.left = x
                        else:
                            p.right = x
                    return x
        else:
            if y:
                if x is y.left:
                    self.right_rotation(x, y)
                elif x is y.right:
                    self.left_rotation(x, y)

                # TODO: Update root pointer
                if y is self.root:
                    self.root = x
                return x
            else:
                return

    def left_rotation(self, a, b):
        if a.left:
            temp = a.left
            a.left = b
            b.right = temp
        else:
            a.left = b
            b.right = None

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

        # TODO: Make sure to update the parent of a and b
        a.parent = b.parent
        b.parent = a

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

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root


if __name__ == '__main__':
    tri = TriNodeRestructuring()
    tri.set_root(pt.populate())
    print '\nBefore Restructuring'
    tri.print_tree()
    print '\nRestructuring e with value 5'
    root = tri.get_root()
    x, y = bsto().find_node(5, root)
    tri.restructure(x)
    tri.print_tree()
    print '\nRestructuring i with value 3'
    root = tri.get_root()
    x, y = bsto().find_node(3, root)
    tri.restructure(x)
    tri.print_tree()
