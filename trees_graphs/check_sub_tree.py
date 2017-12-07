class check_sub_tree(object):

    def __init__(self):
        self.bool = False

    def check_sub(self, root1, root2):

        '''

        Another approach is to convert it
        and append the traversal as a string.
        Then compare both the strings.

        '''
        queue1 = []
        queue2 = []

        queue1.append(root1.data)
        queue2.append(root2.data)
        while queue2:
            if queue1 != queue2:
                return False
            temp, temp2 = [], []
            for val in queue2:
                temp2.append(val.left)
                temp2.append(val.right)
            queue2 = temp2

            for val in queue1:
                temp.append(val.left)
                temp.append(val.right)
            queue1 = temp

        return True

    def find_node(self, root1, root2):
        if root1:
            if root1.data == root2.data:
                if self.check_sub(root1, root2):
                    print 'It is a Subtree'
                    self.bool = True
                    return
            else:
                self.find_node(root1.left, root2)
                self.find_node(root1.right, root2)
        else:
            return

    def main(self):
        self.find_node(root1=None, root2=None)
        if not self.bool:
            print 'Subtree doesnt exist'