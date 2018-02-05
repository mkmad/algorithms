import math


class Balanced(object):
    """
    The concept is simple but I had some problems
    with what to return during recursion

    On one hand I wanted to return True/False based
    on the difference of left height and right height.
    But, if I do that then I wont be giving a int value
    (height) to the upper calls.

    So, this is an important example of how handle input
    and output for recursive programs

    You need to stick to one return type, or terminate the program
    mid way, you can't however, return two different types

    I chose to return inf incase I find in balance in the tree

    """
    def __init__(self):
        self.root = None

    def is_blanced(self, node=None, height=0):
        left = right = height
        if not node:
            return height
        else:
            if node.left:
                left = self.is_blanced(node.left, height=height + 1)
            if node.right:
                right = self.is_blanced(node.right, height=height + 1)

            if math.fabs(left - right) > 1:
                return float('inf')
            else:
                max(left, right)

    def popute_tree(self):
        pass