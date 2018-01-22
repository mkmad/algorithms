class Kruskals(object):

    class mySet(object):

        def __init__(self):
            self.elements = []

    def __init__(self):
        self.set_map = {}
        self.edges = {}
        self.res = []

    def union(self, vertex1, vertex2):

        """
        I look at the set_map, and see if both the vertices
        are represented by the same obj or not, if it the same
        obj, it means both the vertices belong to the same set
        and no union is required. I return false

        If it not the same obj then, I check which vertex is bigger
        and copy the elements of the smaller vertex's obj to the
        bigger vertex's obj

        I also, update the set_map to reflect who represents the
        copied elements. I return true

        """

        if self.set_map[vertex1] is self.set_map[vertex2]:
            return False

        else:
            # comparison is based on the ascii value
            if vertex1 > vertex2:

                for sub_vertices in self.set_map[vertex2].elements:
                    self.set_map[vertex1].elements.append(sub_vertices)
                    self.set_map[sub_vertices] = self.set_map[vertex1]

            else:

                for sub_vertices in self.set_map[vertex1].elements:
                    self.set_map[vertex2].elements.append(sub_vertices)
                    self.set_map[sub_vertices] = self.set_map[vertex2]

            return True

    def populate_map(self, graph):
        """
        Note: The set should contain the elemet it represents
        eg:

        if set_map['A'] == some_obj

        then some_obj should have 'A' as one of its elements
        """

        for vertices in graph:
            set_ = self.mySet()
            # TODO: IMP!!! The vertex represents itself
            set_.elements.append(vertices)
            self.set_map[vertices] = set_

    def populte_edges(self, graph):
        """
        parse the graph and populate the edge along with weight
        of each edge
        """
        for vertices in graph:
            for neighighbours in graph[vertices]:
                edge = ''.join(sorted([vertices, neighighbours]))
                if edge not in self.edges:
                    self.edges[edge] = graph[vertices][neighighbours]

    def kruskal(self, graph):
        """
        After populating graphs and edges, I sort the edges and check
        for each edge( both the vertices) if I can perform a union or not.

        If I can perform union add the edge to the final result set
        """
        self.populate_map(graph)
        self.populte_edges(graph)

        # TODO: Note how I sort the edges
        for edge, weight in sorted(self.edges.items(), key=lambda(k, v): v):
            if self.union(edge[0], edge[1]):
                self.res.append(edge)

        print self.res


if __name__ == '__main__':

    graph = {
        'A': {
            'B': 3,
            'D': 1
        },
        'B': {
            'A': 3,
            'D': 3,
            'C': 1
        },
        'C': {
            'B': 1,
            'D': 1,
            'E': 5,
            'F': 4
        },
        'D': {
            'A': 1,
            'B': 3,
            'C': 1,
            'E': 6
        },
        'E': {
            'C': 1,
            'D': 6,
            'F': 2
        },
        'F': {
            'C': 4,
            'E': 2
        }
    }

    k = Kruskals()
    k.kruskal(graph)

