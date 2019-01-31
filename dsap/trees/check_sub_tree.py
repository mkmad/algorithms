class CheckSubTree(object):

    """
    Given two Binary trees (not necessarily BST), find out if
    the second tree is a sub tree of the first tree

    """

    def check_sub(self, root1, root2):

        """

        :param root1:
        :param root2:
        :return:

        Cases to consider:

            1. Check if both nodes exist
            2. If both nodes exist then check whether
                a) If root2.left exist and move forward if it does
                b) If root2.right exist and move forward if it does

        Note: Both left and right var is initialized to True because
              say if root2.left (or right) doesn't exist then we return
              saying this particular node is part of the sub tree and
              return True
        """

        # This condition will explicitly check for root1, since this
        # function takes care of root2's availability we check if there
        # exists a node in root2 and not in root1
        if root1 and root2:
            left = True
            right = True

            # only move forward if the node's data are the same
            if root1.data == root2.data:
                if root2.left:
                    left = self.check_sub(root1.left, root2.left)

                if root2.right:
                    right = self.check_sub(root1.right, root2.right)

                # return the and of left and right irrespective of
                # whether root2 has children or not
                return left and right

            else:
                return False

        else:
            return False

    def find_node(self, root1, root2):
        """

        :param root1:
        :param root2:
        :return:

        Find the root2 node in the root1 tree first

        Note: I optimized the recursive call to check the left
              subtree of root1 first and only if it returns False
              I move on and check for right subtree. This way the
              code will exit after finding the first occurrence
              of the subtree
        """
        if root1 and root2:
            if root1.data == root2.data:
                # If node is found then check for subtree
                if self.check_sub(root1, root2):
                    print 'It is a Subtree'
                    return True
                else:
                    print 'Subtree doesnt exist'
                    return False
            else:
                if not self.find_node(root1.left, root2):
                    self.find_node(root1.right, root2)

        else:
            return False

    def main(self):
        self.find_node(root1=None, root2=None)
