import random


class RandomNode(object):

    def __init__(self):
        self.root = None

    class Node(object):

        def __init__(self):
            self.data = None
            self.left = None
            self.right = None
            self.left_size = 0
            self.right_size = 0

    def get_random_node(self, root=None, rand=0):
        """
        Since I custom build the tree, I have access
        to the left size and the right size of any given
        node. Now, since call to rand is expensive I need
        to limit it to just one call

        with the sizes I can generalize that there are
        left_size number of nodes in the left tree,
        right_size number of nodes in the right tree and the
        total number of nodes in the tree rooted at self.root
        will be:

            root.left_size + root.right_size + 1

        with this I can roll the dice and see where it falls,
        if the number is less than root.left_size then I go to
        the left tree, if it is equal to root.left_size + 1
        then I return root, if it is greater than
        root.left_size + 1 I need to make a small change to the
        random number.

        I traverse the right tree with
        random_number - (root.left_size + 1)

        This is necessary because, say for eg if the right size is
        just 4 and left size is 2 and the random number is 4

        then clearly 4 > left size + 1 but when I go to the right
        tree I need to return the very next node (because 4 is the
        next number in order) but if I don't subtract and just pass
        4 as the random number I'll end up returning the very last
        number in the right tree instead of the very next node to
        root

        """
        if root:
            if rand <= root.left_size:
                if root.left:
                    return self.get_random_node(root=root.left, rand=rand)
                else:
                    return root
            elif rand > root.left_size + 1:
                if root.right:
                    return self.get_random_node(
                        root=root.right, rand=rand - (root.left_size + 1))
                else:
                    return root
            else:
                return root
        else:
            root = self.root
            total_size = self.root.left_size + self.root.right_size + 1
            rand = random.randint(0, total_size)
            print '\nRandom Number is:'
            print rand
            return self.get_random_node(root=root, rand=rand)

    def insert_node(self, root, val):
        """
        This is bst insert, I just increment the size of the
        node if it is encountered (in the path of insertion)
        """

        if not root:
                self.root = self.Node()
                self.root.data = val

        else:
            if val < root.data:
                root.left_size += 1
                if root.left:
                    self.insert_node(root.left, val)
                else:
                    root.left = self.Node()
                    root.left.data = val

            else:
                root.right_size += 1
                if root.right:
                    self.insert_node(root.right, val)
                else:
                    root.right = self.Node()
                    root.right.data = val

    def build_tree(self):
        self.insert_node(self.root, 20)
        self.insert_node(self.root, 10)
        self.insert_node(self.root, 30)
        self.insert_node(self.root, 5)
        self.insert_node(self.root, 15)
        self.insert_node(self.root, 35)
        self.insert_node(self.root, 3)
        self.insert_node(self.root, 7)
        self.insert_node(self.root, 17)

    def main(self):
        self.build_tree()
        return self.get_random_node()


if __name__ == '__main__':
    r = RandomNode()
    rn = r.main()
    print '\nRandom node is:'
    print rn.data

