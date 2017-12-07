list_heads = []
class Node(object):
    
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data
    
    def set_next(self, node):
        self.next = node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

class list_depths(object):
    
    def __init__(self):
        pass

    def get_node(self):
        return Node()

    def parse_tree(self, array):
        if not array:
            return

        next = []
        node = Node()
        cur = node
        for val in array:
            next.append(val.left)
            next.append(val.right)
            if node.data == None:
                list_heads.append(node)
                node.set_data(val.data)
                node.set_next(self.get_node().set_data(val.right))
                cur = node.next
            else:
                cur.set_next(self.get_node().set_data(val.left))
                cur.next.set_next(self.get_node().set_data(val.right))
                cur = cur.next.next
        self.parse_tree(next) # So this is additional recursive call that might
                              # need more space for the recursion stack.
                              # Instead use iterative method (while loop) for bfs.
if __name__ == '__main__':
    root = None # Pass root here.
    ld = list_depths()
    ld.parse_tree([root])
