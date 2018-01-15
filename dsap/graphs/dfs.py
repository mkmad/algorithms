from adjacency_map import AdjacencyMap as am


class DFS(object):

    """
    The difference between this dfs and bst dfs is
    the leaf nodes in bst terminate to None, ie they
    don't have any neighbours. Here all the nodes have
    neighbours, so, visited map is used for terminating
    purposes

    """
    def __init__(self):
        self.a_map = am()

    def dfs(self, vertex, visited=None):
        if vertex in self.a_map.my_map:
            for vertices in self.a_map.my_map[vertex]:
                if vertices.keys()[0] not in visited:
                    visited[vertices.keys()[0]] = vertex
                    self.dfs(vertices.keys()[0], visited=visited)
            return visited


if __name__ == '__main__':
    dfs = DFS()
    print dfs.dfs('A', visited={'A': 'A'})
