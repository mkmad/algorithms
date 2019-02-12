"""

                                    4 (6)
                               /             \
                            3 (3)         5 (2)
                         /     \            /
                   1 (1)    2 (1)     6 (1)

"""

trav = []


class Node(object):

    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


def buildTree():
    n1 = Node()
    n1.data = 1

    n2 = Node()
    n2.data = 2

    n3 = Node()
    n3.data = 3

    n4 = Node()
    n4.data = 4

    n5 = Node()
    n5.data = 5

    n6 = Node()
    n6.data = 6

    n4.left = n3
    n4.right = n5

    n3.left = n1
    n3.right = n2

    n5.left = n6

    return n4


def appendToTrav(node, N):
    global trav
    if node:
        trav.append(node)
        if len(trav) == N:
            return node


def FindNthNode(root, N):

    # return the Nth node in order traversal

    temp = None

    if root:

        if not root.left and not root.right:
            temp = appendToTrav(root, N)
            if temp:
                return temp

        else:
            if root.left:
                temp = FindNthNode(root.left, N)
                if temp:
                    return temp

            temp = appendToTrav(root, N)
            if temp:
                return temp

            if root.right:
                temp = FindNthNode(root.right, N)
        if temp:
            return temp

    else:
        return None


if __name__ == '__main__':
    root = buildTree()
    temp_ = FindNthNode(root, 7)
    if temp_:
        print temp_.data
    else:
        print "Nope"
