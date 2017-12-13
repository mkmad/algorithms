import populate_tree


class Treetraversals(object):

    def __init__(self):
        pass

    def preorder(self, node):
        if node:
            print node.data,
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print node.data,
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.data,

    def get_root(self):
        return populate_tree.populate()

    def print_(self):
        print '\nPre order'
        root = self.get_root()
        self.preorder(root)
        print '\nIn order'
        self.inorder(root)
        print '\n Post order'
        self.postorder(root)
