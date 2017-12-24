from trinode_restructuring import TriNodeRestructuring as tri
from mycode.dsap.trees.bst_operations import BSTOperations as bsto
from mycode.dsap.trees import populate_tree as pt

import math


class AVL(object):
    """
    AVL property: ht of a node is max(ht of left child, ht of right child)

    Insert: Insert like bst, after that yoy need to recalculate
    the heights. You do that by calculating the heights of all the
    node's ancestors (parents). After recalculating, check for avl
    violations up the ancestor chain all the way upto root.

    Delete: Same as BST delete, recalculate the heights and check for
    violations in the ancestor chain all the way upto ancestor root.

    Checking Violations: For insert, you need to do a tri node/ dual node
    restructuring just at the first node that violates the avl property
    i.e. the nearest ancestor from the inserted node.

    For delete, you need to recursively do a trinode/dual node restructuring
    to all the nodes that violate the property untill you reach the root node.
    """

    def __init__(self):
        self.root = None
        self.bsto = bsto()
        self.tri = tri()

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.parent = None
            self.height = None
            # lable is just for my reference
            self.lable = None

    def recalculate_heights(self, node):
        """
        Straightforward, recursively recalculate the heights
        all the way upto root. This takes the height's of the
        children into consideration before it modifies the node's
        height
        """
        if node:
            l_height = 0
            r_height = 0
            if node.left:
                l_height = node.left.height
            if node.right:
                r_height = node.right.height
            node.height = max(l_height, r_height) + 1
            if node.parent:
                self.recalculate_heights(node.parent)
            else:
                return
        else:
            raise Exception('Node required')

    def check_for_violations(self, node, recurssive=False):
        """
        You need 3 vars to keep track for node, its child and
        grandchild.

        There are 2 cases (if the node is in violation):

        1) node has 2 children, in that case, one of the children
           will have a greater height, i.e. the diff between the
           child heights will be grater than 1 (only then the current
           node is in violation) so node will be x and the greater
           child will be y. Also, y will have atleast one child
           of its own (only then its height will be large)
           so, that child will be z

        2) node just has a single child, and if the node is in violation
           that child's height will be atleat 2 (since the empty child has
           height 0). The node's child will be y. We can also be sure that
           y will atleast have one child of its own (only then its
           height will be atleast 2)

        In either of the cases z will not be None, I use this insight to call
        tri node restructuring (i.e. only if z is not None)

        If z is None, then there is no violations in the current node

        """
        if node:
            x = node
            y = None
            z = None

            # If node has both children
            if x.left and x.right:
                if math.fabs(x.left.height - x.right.height) > 1:
                    print 'Node {} is in violation'.format(x.lable)
                    if x.left.height > x.right.height:
                        y = x.left
                    else:
                        y = x.right
                    if y.left and y.right:
                        if y.left.height > y.right.height:
                            z = y.left
                        else:
                            z = y.right
                    elif y.left:
                        z = y.left
                    elif y.right:
                        z = y.right

            # If node, just has a left child
            elif x.left:
                if math.fabs(x.left.height - 0) > 1:
                    print 'Node {} is in violation'.format(x.lable)
                    y = x.left
                    if y.left:
                        z = y.left
                    if y.right:
                        if y.right.height > y.left.height:
                            z = y.right

            # If the node just has a right child
            elif x.right:
                if math.fabs(x.right.height - 0) > 1:
                    print 'Node {} is in violation'.format(x.lable)
                    y = x.right
                    if y.right:
                        z = y.right
                    if y.left:
                        if y.left.height > y.right.height:
                            z = y.left

            # Perform tri node restructure only if z is not None
            if z:
                # I send back the sub tree root of x, y z after
                # restructuring
                subtree_root = self.tri.restructure(z)
                # I use that subtree_root to recalculate the height
                # of children that are rooted at subtree_root

                # Note: I need to call recalculate_heights for both
                # the children of subtree_root as its will consider
                # the heights of the grand children of subtree_root
                # and thereby updating the children and subtree_root's
                # height
                # Also note, the height of subtree_root will be updated
                # twice as recalculate_heights will propagate upwards twice
                # (once for each child)
                self.recalculate_heights(subtree_root.left)
                self.recalculate_heights(subtree_root.right)

                # This will be called only for delete operation
                if recurssive:
                    self.check_for_violations(subtree_root.parent)
                else:
                    return subtree_root

            # No violations as z is empty
            else:
                self.check_for_violations(node.parent)

    def insert(self, val):
        node = self.Node(val)
        self.bsto.insert_node(node, self.root)
        # Call recalculate height on the node before calling
        # check for violation, otherwise check_for_violation
        # will work with old heights
        self.recalculate_heights(node)
        self.check_for_violations(node, recurssive=False)

    def delete(self, val):
        # I slightly modified the bst delete to return the parent of
        # the deleted node (or parent of the successor,
        # depending on the case). I need this node for both
        # recalculate and check_for_violations functions
        temp_node = self.bsto.delete(val, self.root)
        if temp_node:
            # Call recalculate height on the node before calling
            # check for violation, otherwise check for violation
            # will work with old heights
            self.recalculate_heights(temp_node)
            self.check_for_violations(temp_node, recurssive=True)

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
    avl = AVL()
    avl.root = pt.populate()
    print '\nBefore Insertion'
    avl.print_tree()
    print '\n\nInserting 0'
    avl.insert(0)
    print 'After Instertion'
    avl.print_tree()
    print '\n\nDeleting 0'
    avl.delete(0)
    print 'After Deletion'
    avl.print_tree()
    print '\n\nDeleting h -> 1'
    avl.delete(1)
    avl.print_tree()
