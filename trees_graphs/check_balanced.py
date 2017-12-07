class check_balanced(object):

    def __init__(self, root):
        if not root:
            print 'Invalid Input'
        self.root = root

    def calculate_height(self, node_list):
        # See how I am passing a list here
        # this is because I am going to
        # generate the list of all children
        # and gonna call this function anyway
        # so why not just call the function
        # with a list that contains root.

        if not node_list:
            return 0
        else:
            next = []
            for val in node_list:
                if val.left:
                    next.append(val.left)
                elif val.right:
                    next.append(val.right)
            # See how this level is returning
            # 1 if it encounters even a single
            # node.
            return 1 + self.calulate_height(next)

    def check_if_balanced(self):
        left_sum = self.calculate_height([self.root.left])
        right_sum = self.calculate_height([self.root.right])
        if abs(left_sum - right_sum) > 1:
            print "Tree is not balanced"
        else:
            print "Tree is balanced"

if __name__ == '__main__':
    root = None # Supply root here.
    cb = check_balanced(root)
    cb.check_if_balanced()
            
'''
Note: I choose to do a bfs here as I am interested in the 
      Height of the tree, which is nothing but the number
      of levels in the tree. A DFS will let me calculate 
      the number of nodes much faster though.

IMP Note on Recursion:
      This example is a good way of showing how to design
      a recursive algorithm. So you have to keep the end/output
      in mind and design. Here I first see that my
      recursive algorithm is generating a list at the
      end so that will also be my input - A list
'''