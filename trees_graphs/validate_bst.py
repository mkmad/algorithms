Invalid = False

class validate(object):
    def __init__(self):
        pass

    def validate_tree(self, array):
        global Invalid
        if not array:
            return
        if Invalid:
            return
        next = []
        for val in array:
            if val.data >= val.left.data and \
                            val.data < val.right.data:
                next.append(val.left)
                next.append(val.right)
            else:
                Invalid = True
                return

if __name__ == '__main__':
    root = None  # Supply root here
    v = validate()
    v.validate_tree([root])
    if Invalid:
        print "Invalid Tree"
    else:
        print "Valid Tree"

'''
The above code wont work for
       20
10           30
     25

As 25 is clearly in the wrong place, even though it
passes the condition in place.

so the solution is to do a inorder traversal and store it
in a array then see if the resulting array is in ascending
order

'''


class validate(object):
    def __init__(self):
        self.array = []

    def validate(self, node=None):
        if not node:
            return self.array
        else:
            if node.left:
                self.array.append(self.validate(node.left))
            self.array.append(node)
            if node.right:
                self.array.append(self.validate(self.node.right))

    def validate_sorted(self):
        if self.array == sorted(self.array):
            print 'Valid Binary Tree'
        else:
            print 'Invalid Binary Tree'

if __name__ == '__main__':
    root = None  # Supply root here
    v = validate()
    v.validate(root)
    v.validate_sorted()

'''
Note: In the above solution we dont need a array, just keep track of the
last element from the traversal and check if the next element is <= to the
last element.

'''




