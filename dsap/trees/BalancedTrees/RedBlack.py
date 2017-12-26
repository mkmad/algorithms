class RedBlackTree(object):

    def __init__(self):
        self.root = None

    class Node:

        def __init__(self, data):
            self.data = data
            self.colour = 'red'
            self.left = None
            self.right = None
            self.parent = None

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
                    y.colour = 'red'
                    x.colour = 'black'
                    z.colour = 'black'
                    return y
                else:
                    # Zig-Zag
                    self.right_rotation(x, y)
                    self.left_rotation(x, z)
                    x.colour = 'red'
                    y.colour = 'black'
                    z.colour = 'black'
                    return x
            else:
                if y is z.left:
                    # Zig-Zag
                    self.left_rotation(x, y)
                    self.right_rotation(x, z)
                    x.colour = 'red'
                    y.colour = 'black'
                    z.colour = 'black'
                    return x

                else:
                    # Zig-Zig
                    self.left_rotation(y, z)
                    y.colour = 'red'
                    x.colour = 'black'
                    z.colour = 'black'
                    return y

    def dual_node_restructure(self, x, y):
        if x is y.left:
            self.right_rotation(x, y)
        else:
            self.left_rotation(x, y)

        x.colour = 'black'
        y.colour = 'red'

    def recolour(self, x):
        z = x.parent
        y = z.left

        x.colour = 'black'
        y.colour = 'black'
        z.colour = 'red'

        return z

    def check_insert_violation(self, x, y, z=None):

        if z:
            # Check if z has a sibling, and if it does find
            # what colour it is
            if y is z.left:
                if z.right:
                    # Case 1 of insertion, black sibling
                    ####################################
                    if z.right.colour == 'black':
                        subtree_root = self.restructure(x, y, z)

                    # Case 2 of insertion, red sibling
                    ##################################
                    else:
                        subtree_root = self.recolour(x)
                        # Recursively check for violations all the
                        # way upto root
                        self.check_insert_violation(subtree_root,
                                                    subtree_root.parent,
                                                    subtree_root.parent.parent)

                # Case 1 of insertion, no sibling of z
                ######################################
                else:
                    subtree_root = self.restructure(x, y, z)
            else:
                if z.left:
                    # Case 1 of insertion, black sibling
                    ####################################
                    if z.left.colour == 'black':
                        subtree_root = self.restructure(x, y, z)

                    # Case 2 of insertion, red sibling
                    ##################################
                    else:
                        subtree_root = self.recolour(x)
                        self.check_insert_violation(subtree_root,
                                                    subtree_root.parent,
                                                    subtree_root.parent.parent)

                # Case 1 of insertion, no sibling of z
                ######################################
                else:
                    subtree_root = self.restructure(x, y, z)

        else:
            # It wont be a double red problem if y is the root, y should be black
            if y.colour == 'black':
                return
            else:
                raise Exception('Invalid RBT')

    def insert_node(self, node, root):
        if node:
            if root:
                if node.data < root.data:
                    if root.left:
                        self.insert_node(node, root.left)
                    else:
                        root.left = node
                        node.parent = root
                        return root
                else:
                    if root.right:
                        self.insert_node(node, root.right)
                    else:
                        root.right = node
                        node.parent = root
                        return root

    def delete_node(self, val, root):
        """
        Delete has 3 cases:

            1) if node has no children, then simply delete
               the node
            2) if node has one child, then promote the child
               by copying its data and delete the child.
            3) if it has two children, find successor/predecessor
               replace the data of the successor/predecessor with
               node and delete the successor or predecessor

        You also need to make sure to update the parent of the
        deleted node, since you are technically not deleting,
        you are just setting the pointer to None. The parent might
        still be pointing to the old node
        """
        node = self.find_node(val, root)
        parent = node.parent

        if node:

            # If node has no children
            if not node.left and not node.right:
                if parent:
                    if node is parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                    return parent, node
                else:
                    # If node has no parent, then its the root
                    self.root = None, None

            # If node has both children
            elif node.left and node.right:
                successor, succ_parent = self.successor(node)
                node.data = successor.data
                # Successor has to have a parent, update the parent
                if successor is succ_parent.left:
                    succ_parent.left = None
                else:
                    succ_parent.right = None
                return succ_parent, successor

            # Node has only one child
            elif node.right:
                if parent:
                    # update parent
                    if node is parent.left:
                        parent.left = node.right
                    else:
                        parent.right = node.right
                    return parent, node
                else:
                    # Has to be root, if it has no parent
                    self.root = node.right
                    """
                    I could have also done

                    node.data = node.right.data
                    node.right = None

                    Thereby the self.root pointer remains
                    untouched
                    """
                    return self.root, node

            # Same as above, in the other direction
            else:
                if parent:
                    if node is parent.left:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                    return parent
                else:
                    self.root = node.left
                    return self.root, node

        else:
            raise Exception('Node not found')

    def successor(self, node):
        if node:
            if node.right:
                return self.find_leftmost(node.right, node)
            else:
                raise Exception('Node has no Succesor')
        else:
            raise Exception('Need a node')

    def find_leftmost(self, node, parent):
        if node.left:
            return self.find_leftmost(node.left, node)
            # TODO: I forgot to put a return statement here ^^
        else:
            return node, parent

    def find_node(self, val, root):
        """
        Simple binary search, along with passing parent pointer
        """
        if root:
            if root.data == val:
                return root
            else:
                if val < root.data:
                    return self.find_node(val, root.left)
                else:
                    return self.find_node(val, root.right)
        else:
            return None

    def insert(self, val):

        if not val:
            raise Exception('Value is required')

        node = self.Node(val)
        if not self.root:
            node.colour = 'black'
            self.root = node
        else:
            parent = self.insert_node(node, self.root)
            if parent.colour == 'red':
                x = node
                y = parent
                z = parent.parent
                self.check_insert_violation(x, y, z)

    def delete(self, val):
        if not val:
            raise Exception('Value is required')

        parent, deleted_node = self.delete_node(val, self.root)

        if parent and deleted_node:
            #############################
            # Case 1, Deleted node is red
            #############################
            if deleted_node.colour == 'red':
                pass

            #######################
            # Deleted node is black
            #######################
            # Case 2 to 5 fall
            # under this
            #######################
            else:

                ###################################################
                # Case 2, child of the deleted black node is red
                if deleted_node.left:
                    # The child has to be red, in order to
                    # to preserve the black depth. So, mark it
                    # black to maintain the black height

                    # Also, the deleted should have only left child,
                    # since the deleted node is a successor
                    deleted_node.left.colour = 'black'
                ###################################################

                ############################################
                # A leaf black node is deleted, the deleted
                # node will have a sibling (So as to balance
                # the black height)
                # Case 3, 4 & 5 fall under this
                ############################################
                else:
                    if parent.left:
                        y = parent.left
                    else:
                        y = parent.right

                    ##################
                    # sibling is black
                    ##################
                    # Case 3 & 4 falls
                    # under this
                    ##################
                    if y.colour == 'black':

                        #############################################
                        # Case 3, if one of the children of y is red
                        # perform tri node restructuring making x as
                        # the red child, y is y and z is parent
                        # Note, y can have both reds, or a red and a
                        # black We chose the red/or one of the red as
                        # x
                        #############################################
                        x = None
                        z = None
                        if y.left:
                            z = parent
                            if y.left.colour == 'red':
                                x = y.left

                        elif y.right:
                            z = parent
                            if y.right.colour == 'red':
                                x = y.right

                        # It means there is a red child for y
                        if x:
                            old_z_colour = z.colour
                            self.restructure(x, y, z)

                            # We have to recolour it this way
                            y.colour = old_z_colour
                            x.colour = 'black'
                            z.colour = 'black'

                        #################################################
                        # Case 4, if the sibling has two black kids or if
                        # the sibling has no kids at all then we just
                        # recolour parent and the sibling
                        #################################################
                        if not all([y.left, y.right]) \
                                or y.left.colour == y.right.colour == 'black':
                            if parent.colour == 'black':
                                if y.left:
                                    y.left.colour = 'black'
                                else:
                                    y.right.colour = 'black'
                            else:
                                parent.colour = 'black'
                                if y.left:
                                    y.left.colour = 'red'
                                else:
                                    y.right.colour = 'red'

                    ################
                    # Sibling is red
                    ################
                    # Case 5 falls
                    # under this
                    ################
                    else:
                        # Since the sibling is red, it will
                        # have two black kids, so as to
                        # balance the deleted node (prev to
                        # deletion of course)

                        # Another insight is, parent's
                        # colour will be black since, red
                        # can't have red kids
                        z = parent
                        self.dual_node_restructure(y, z)

                        # Before restructuring, y had two
                        # black kids. So, after restructuring
                        # one the kids would have gone to z
                        # thus violating rb property as z will
                        # technically have only one kid (the
                        # heavier kid) after restructuring.
                        # Hence we recolour y, z so as to
                        # balance it out
                        y.colour = 'black'
                        z.colour = 'red'


if __name__ == '__main__':
    pass