from adjacency_map import AdjacencyMap as am


class BFS(object):

    """
    Some subtle differences between this bfs and
    the bst bfs. In bst the leaf nodes terminate
    to None, here there is no termination, instead
    the nodes point to the next neighbours.

    So, in L36, if If I append on the condition
    if v not in neighbour: neighbour.append(v)

    It will be maximum recursion depth problem
    because for every iteration I'll have neighbours.
    In the bst its not the case since neighbours will
    terminate in leaf nodes.

    So, be careful. Here visited dict is the one that
    actually determines when the recursion should
    terminate

    """

    def __init__(self):
        self.a_map = am()

    def bfs(self, vertices=None, visited=None):
        if vertices:
            neighbours = []
            for vertex in vertices:
                for neighbour in self.a_map.my_map[vertex]:
                    v = neighbour.keys()[0]
                    if v not in visited:
                        visited[v] = vertex
                        neighbours.append(v)
            self.bfs(vertices=neighbours, visited=visited)
            return visited

    def bfs_bst(self, root):
        queue = []

        queue.append(root)

        while queue:
            temp = []



if __name__ == '__main__':

    bfs = BFS()
    visited = {'A': 'A'}
    """
    See how it doesn't matter if I return visited (L38) 
    or not because the visited that's returned is the 
    same as the one in L44
    """
    print bfs.bfs(vertices=['A'], visited=visited)
    print visited
