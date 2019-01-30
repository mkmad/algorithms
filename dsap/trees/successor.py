import populate_tree as pt


class Successor(object):
    """

    Goal is to find in-order successor in a bst and there are two
    cases:

        1. If the node has a right subtree then find the leftmost node
           in that right subtree. Note if there are no left nodes then
           return the last leaf node where the recursion terminates

        2. If the node has no right subtree then you need to move up
           the to the parent nodes and check if the node under
           consideration is the left sub tree of the node's parent
           If there exists no parent that satisfy that condition then
           the node has no successor (it is the right most node in the
           tree)

    Note: Predecessor is the same as successor on the other direction

    Also note: If there are no pointers to the parents, you can simply
               find the node and build the path and try finding out the
               successor that way
    """
    def successor(self, node):
        if node:
            # Case 1
            if node.right:
                return self.find_leftmost(node.right, node)
            # Case 2
            else:

                cur = node
                succ = None

                while True:

                    if not cur.parent:
                        break

                    if cur is cur.parent.left:
                        succ = cur
                        break

                    else:
                        cur = cur.parent

                return succ

        else:
            raise Exception('Need a node')

    def find_leftmost(self, node, parent):
        if node.left:
            return self.find_leftmost(node.left, node)
            # TODO: I forgot to put a return statement here ^^
        else:
            return node, parent

    def main(self):
        root = pt.populate()
        print self.successor(root)[0].data
        print self.successor(root.right)[0].data
        print self.successor(root.left)[0].data


if __name__ == '__main__':
    s = Successor()
    s.main()
