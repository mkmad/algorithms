import populate_tree as pt


class Successor(object):
    """
    Predecessor is the same as successor on the other direction
    """
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

    def main(self):
        root = pt.populate()
        print self.successor(root)[0].data
        print self.successor(root.right)[0].data
        print self.successor(root.left)[0].data


if __name__ == '__main__':
    s = Successor()
    s.main()
