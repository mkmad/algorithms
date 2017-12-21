import populate_tree as pt
from successor import Successor
from bfs import BFS


class BSTOperations(object):

    def __init__(self):
        self.root = None
        self.succ = Successor()

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def insert(self, val):
        """
        Pretty straightforward
        """
        if val:
            node = self.Node(val)
            self.insert_node(node, self.root)
        else:
            raise Exception('Need a value')

    def insert_node(self, node, root):
        if root:
            if node.data < root.data:
                if root.left:
                    self.insert_node(node, root.left)
                else:
                    root.left = node
                    return
            else:
                if root.right:
                    self.insert_node(node, root.right)
                else:
                    root.right = node
        else:
            # TODO: IMP!!!, I used root = node here, since I was calling
            # TODO: insert_node with self.root I assumed that when I change
            # TODO: the value of root, it will reflect to self.root. But,
            # TODO: self.root gives its reference to root, when I do
            # TODO: root = someObj, I change the reference of root and not
            # TODO: self.root so self.root is still pointing to the old obj
            self.root = node
            return

    def delete(self, val):
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
        node, parent = self.find_node(val, self.root)
        if node:

            # If node has no children
            if not node.left and not node.right:
                if parent:
                    if node is parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    # If node has no parent, then its the root
                    self.root = None

            # If node has both children
            elif node.left and node.right:
                successor, succ_parent = self.succ.successor(node)
                node.data = successor.data
                # Successor has to have a parent, update the parent
                if successor is succ_parent.left:
                    succ_parent.left = None
                else:
                    succ_parent.right = None

            # Node has only one child
            elif node.right:
                if parent:
                    # update parent
                    if node is parent.left:
                        parent.left = node.right
                    else:
                        parent.right = node.right
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

            # Same as above, in the other direction
            else:
                if parent:
                    if node is parent.left:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    self.root = node.left

        else:
            raise Exception('Node not found')

    def find_node(self, val, root, parent=None):
        """
        Simple binary search, along with passing parent pointer
        """
        if root:
            if root.data == val:
                return root, parent
            else:
                if val < root.data:
                    return self.find_node(val, root.left, root)
                else:
                    return self.find_node(val, root.right, root)
        else:
            return None, None

    def assign_root(self):
        if not self.root:
            self.root = pt.populate()

    def print_tree(self):
        self.assign_root()
        bfs = BFS()
        bfs.bfs([self.root])
        print ''


if __name__ == '__main__':
    print '\nBFS of the tree'
    bst = BSTOperations()
    bst.print_tree()
    print '\nDeleting 5'
    bst.delete(5)
    bst.print_tree()
    print '\nInserting 5 again'
    bst.insert(5)
    bst.print_tree()
    print '\nDeleting root'
    bst.delete(6)
    bst.print_tree()
