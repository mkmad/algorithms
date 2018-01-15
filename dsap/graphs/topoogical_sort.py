class TopologicalSort(object):
    """
    It needs to be a DAG

    Maintain a visited array, and a stack:

    1) Randomly pick a vertex in the graph, if the
       vertex is not in the visited array then add
       it to visited array and go to step 2

    2) If the vertex has no neighbours or all its
       neighbours are in the visited array the add
       the vertex to stack as well, and then go back
       to step 1 or its previous vertex (parent)

    3) If the vertex has neighbour(s) that are not
       in the visited array, then move to that
       neighbour and add it to the visited array and
       repeat step 2
    """

    def __init__(self):
        self.visited = []
        self.order = []

    def sort(self, vertex, graph):
        if vertex not in self.visited:
            self.visited.append(vertex)

            if vertex in graph:
                # Call sort on all the neighbours
                # of vertex
                for neighbour in graph[vertex]:
                    self.sort(neighbour, graph)
                # Add vertex to order after all the
                # neighbours are called
                self.order.append(vertex)
            else:
                # Add vertex to order if the vertex
                # has no other neighbours
                self.order.append(vertex)

    def topological_sort(self, graph):
        """
        Call sort for every vertex
        """
        for vertex in graph:
            self.sort(vertex, graph)

        # The topological sort is in reverse order
        self.order.reverse()
        return self.order


if __name__ == '__main__':
    dependancy_graph = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['H', 'F'],
        'F': ['G'],
    }
    tp = TopologicalSort()
    print tp.topological_sort(dependancy_graph)
