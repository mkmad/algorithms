class HamiltonianCycle(object):

    """
    For a given graph, see if you can
    start at a given position and traverse
    through all the vertices of the graph by
    visiting each vertex exactly once and return
    back to the start vertex


    This is a simple backtracking problem, for
    each vertex the number of branches will be
    the number of adjacent vertices. Also maintain
    a visited set to check if you have visited
    a vertex before or not


    Note: The difference between this problem and the other backtracking
          problems (graph coloring ) is, here you check if there is successful
          solution by selecting one neighbour at a time, in the other problems
          however, we check if any of the paths (any of the neighbour) lead to
          the solution (using `or` operator)
    """

    def __init__(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'c', 'e'],
            'c': ['a', 'b', 'd', 'e'],
            'd': ['a', 'c', 'e', 'f'],
            'e': ['b', 'c', 'd', 'f'],
            'f': ['d', 'e']
        }

    def traverse(self, vertex=None, visited=None, start=None):

        for neighbour in self.graph[vertex]:

            if neighbour == start:
                if len(visited.keys()) == len(self.graph.keys()):
                    print
                    print "Hamiltonian cycle exists"
                    self.print_cycle(visited, vertex, path="{0}".format(start))
                    return True
                else:
                    continue

            if neighbour not in visited:

                # select a particular neighbour, add it to the visited set and go and
                # actually visit it. if the cycle exists then return
                # true thereby eliminating further searches. If not del the neighbour
                # from the visited path, thereby removing this path from consideration

                visited[neighbour] = vertex
                if self.traverse(vertex=neighbour, visited=visited, start=start):
                    return True
                else:
                    del visited[neighbour]

    def print_cycle(self, visited, vertex, path=None):

        if visited[vertex]:
            path += "->{0}".format(vertex)
            self.print_cycle(visited, visited[vertex], path=path)
        else:
            print "{0}->{1}".format(path, vertex)

    def main(self):
        visited = {'a': None}
        self.traverse(vertex='a', visited=visited, start='a')




if __name__ == '__main__':
    h = HamiltonianCycle()
    h.main()
