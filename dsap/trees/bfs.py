import populate_tree


class BFS(object):

    def __init__(self):
        pass

    def bfs(self, nodes=[]):
        if nodes:
            temp = []
            for i in nodes:
                print i.data,
                # Todo: Make sure you append only if the child is present else you'll
                # Todo: have array with None values.
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            self.bfs(temp)

    def print_bfs(self):
        self.bfs([populate_tree.populate()])
