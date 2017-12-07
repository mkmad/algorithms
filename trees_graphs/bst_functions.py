class node():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.size = 0
        self.parent = None

class BST():
    def __init__(self, root):
        self.root = root

    def insert(self, root, val, parent):
        if root:
            if val < root.data:
                if root.left:
                    self.insert(root.left, val, root)
                else:
                    n = node()
                    n.data = val
                    n.size = root.size + 1
                    root.left = n
            else:
                if root.right:
                    self.insert(root.right, val, root)
                else:
                    n = node()
                    n.data = val
                    n.size = root.size + 1
                    root.right = n
        else:
            n = node()
            n.data = val
            n.size = 1
            self.root = n

    def search(self, root, node):
        if root.data ==  node.data:
            return root
        if node.data >= root.data:
            if root.right:
                self.search(root.right, node)
            else:
                return None
        else:
            if root.left:
                self.search(root.left, node)
            else:
                return None

    def findSuccesor(self, node):
        if not node.left:
            return node
        else:
            self.findSuccesor(node.left)

    def updateSuccessorNode(self, node):
        if not node.right:
            node = None
        else:
            # I know its left since I am finding
            # Minimum so this node has to go in the
            # parent's left
            node.parent.left = node.right

    def delete(self, root, val):
        node = self.search(root, val)
        if node:
            # Find the minimum in node.right sub tree.
            succ = self.findSuccesor(node.right)
            node.data = succ.data
            self.updateSuccessorNode(succ)
            return True
        else:
            return False

