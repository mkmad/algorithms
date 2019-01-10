import populate_tree


class DFStreetraversals(object):

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
        print '\nPost order'
        self.postorder(root)

    def dfs_iterative(self):
        """
        I need two arrays for this, one for path and
        one for visited. The path acts as a stack that
        will help in returning to the node and the visited
        array will help in moving to the correct node
        and avoiding the nodes we already discovered
        """
        print '\nIterative Post order'
        root = self.get_root()
        if root:
            path = [root]
            visited = []
            while path:
                cur = path[-1]
                if cur.left and cur.left not in visited:
                    path.append(cur.left)
                    visited.append(cur.left)
                    continue
                if cur.right and cur.right not in visited:
                    path.append(cur.right)
                    visited.append(cur.right)
                    continue
                else:
                    print cur.data,
                    path.pop()


if __name__ == '__main__':
    t = DFStreetraversals()
    t.print_()
    t.dfs_iterative()
