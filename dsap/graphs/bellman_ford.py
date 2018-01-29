class BellmanFord(object):

    """
    Goal, to find single source shortest path
    to all the vertices.

    Note: Dijkstras also does the same thing, but
    this algorithm also works with graphs with negative
    edges and can also detect negative weight cycle.

    Algorithm is pretty straightforward, maintain
    a distance map and a discovered map.

    For each edge u->v, check if the distance
    from the source vertex to v is greater than
    the distance from source vertex to u + distance
    from u to v. If it is, then update
    distance and discovered map accordingly

    Repeat this above process N - 1 times, where N
    is the number of vertices in the graph.

    Note: To find negative weight cycle in the graph
    repeat the process one more time, if any of the
    distance is reduced then it means the graph has a
    negative weight cycle


    """

    def __init__(self):
        self.distance = {}
        self.discovered = {}
        self.edges = []

    def populate_distance(self, graph, source='0'):
        """
        Initiate distance map
        """
        for vertex in graph:
            if vertex == source:
                self.distance[vertex] = 0
            else:
                self.distance[vertex] = float('inf')

    def populate_edges(self, graph):
        """
        Need this function to get all the edges (this
        is only required due to the way the graph is
        represented)
        """
        for k, v in graph.items():
            for sv in v:
                self.edges.append((k, sv))

    def bellman_ford(self, graph):
        """
        In this example the graph has 5 vertices, so perform the
        algorithm 4 times to get the shortest distances from the
        source.

        Perform the algorithm the 5th time just to check if there
        is a negative weight cycle (i.e. if any distance is reduced
        or not)
        """
        self.populate_distance(graph, source='0')
        self.populate_edges(graph)
        no_iterations = len(graph) - 1
        for i in range(no_iterations):
            for edge in self.edges:
                if self.distance[edge[1]] > self.distance[edge[0]] + graph[edge[0]][edge[1]]:
                    self.distance[edge[1]] = self.distance[edge[0]] + graph[edge[0]][edge[1]]
                    self.discovered[edge[1]] = edge[0]

        for edge in self.edges:
            if self.distance[edge[1]] > self.distance[edge[0]] + graph[edge[0]][edge[1]]:
                raise Exception('Negative weight cycle exists')

        print self.distance
        print self.discovered


if __name__ == '__main__':
    graph = {
        '0': {
            '1': 4,
            '2': 5,
            '3': 8
        },
        '1': {
           '2': -3
        },
        '2': {
            '4': 4
        },
        '3': {
            '4': 2
        },
        '4': {
            '3': 1
        }
    }

    bf = BellmanFord()
    bf.bellman_ford(graph)
