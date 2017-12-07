class common_ancestor(object):
    def __init__(self):
        self.path_p = []
        self.path_q = []

    def find_common(self, root = None, p = None, q = None):
        if root:
            if self.find_path(root, p, type="first", path=[]) and \
                    self.find_path(root, q, type="second", path=[]):
                print self.find_common_ancestor(root).data
            else:
                print "One or both of nodes not found"
        else:
            print "Invalid Input"

    def find_path(self, root, node, type = "first", path=[]):
        # note how path is passed around
        path.append(node)
        if root.data == node.data:
            if type == "first":
                self.path_p = path
            else:
                self.path_q = path
            return
        elif root.left:
            self.find_path(root.left, node, type, path)
        elif root.right:
            self.find_path(root.right, node, type, path)
        else:
            return

    def find_common_ancestor(self, root):
        if len(self.path_q) < len(self.path_p):
            for k,v in enumerate(self.path_q):
                # Finding the position where the nodes branch away from the
                # common node.
                if v != self.path_p[k]:
                    return self.path_q[k-1]

if __name__ == '__main__':
    c = common_ancestor()
    root, p, q = None, None, None
    c.find_common(root, p , q)