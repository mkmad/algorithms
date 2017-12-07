class Node(object):

    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def set_data(self, val):
        # check for invalid input
        self.data = val

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

class minimal_tree(object):
    
    def __init__(self, array):
        self.array = array
        # Always check for invalid input
        if not self.array:
            print 'Invalid Input'   
            return

    def create_tree(self, array):
        # Always guard your code with try catches
        try:
            # Always have the base condition for Recursion 
            # It depends on what the input is and what you 
            # return for that particular input.
            if not array:
                return None
            node = Node()
            mid = len(array) / 2
            node.set_data(array[mid])
            node.set_left(self.create_tree(array[:mid]))
            node.set_right(self.create_tree(array[mid+1:]))
            return node
        except Exception as e:
            print e.message

    def build_tree(self):
        root = self.create_tree(self.array)
        return root

class traverse_tree(object):

    def __init__(self, root):
        self.root = root
        self.traverse(self.root)

    def traverse(self, root):
        # For traversal pass the value of the Root
        # Don't store it as a global value

        # For any given function always check for its input for 
        # validity.
        if root:
            print 'Root ->', root.get_data()
            print 'Left ->', self.traverse(root.get_left())
            print 'Right ->', self.traverse(root.get_right())
        

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9]
    mt = minimal_tree(array)
    root = mt.build_tree()
    traverse_tree(root)

'''
Note: For recurssive functions always supply the input directly, 
      don't keep the input in the global space.

'''
