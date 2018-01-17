from priorityQueue import PriorityQueue


class PrimsMinimumSpaningTree(object):

    """
    Goal is to find the minimum spanning tree of
    a weighted undirected graph

    Algorithm is pretty straightforward, for every vertex
    check which of it neighbours has the least weighted
    edge, pick that edge (it will be part of the minimum
    spanning tree) and move to that vertex and repeat the
    same


    Some optimizations:

    When we explore the neighbours of
    a vertex, we need to record the weights to determine
    which edge has the least weight. Hence a priority queue
    makes sense here, we can have the vertices as keys and
    weights as values, this will also help in extracting/remove
    min in constant time.

    After we remove min, we need a record of which edge goes in
    the final spanning tree, for this we use a discovered map.
    This map is updated at the same time we record the weights
    of the neighbours in the priority queue. So, when we do a
    extract/remove min we look at the discovered map to find out
    which edge was responsible for this min value and add it to
    the final result

    The last optimization is to make sure when the vertex is
    looking at all its neighbours (to calculate weight) it
    doesn't consider the edges that are already part of the
    spanning tree, for this we need to modify the priority queue
    so that it supports a contains operation. This can be
    achieved by internally having a map in the priority queue
    that stores the location (index) of the vertices in the queue.
    We can now refer to this map to find if the vertex exists in
    the queue and if does consider that vertex (because when we do
    extract min, we remove the min vertex and that becomes part of
    the spanning tree - we don't want to look at this vertex again)

    Also note, the internal map can also be an internal array if we
    just want to find out if a given vertex exists in the queue or not.
    However, having a map will also help us in update operations of
    vertices (remember we keep updating the value of the vertices
    in the queue)
    """

    class Node(object):
        def __init__(self, data, label):
            self.data = data
            self.label = label

    def __init__(self):
        self.pq = PriorityQueue()
        self.discovered = {}
        self.res = []

    def build_priority_queue(self, graph):
        index = 0
        for vertices in graph:
            self.pq.myHeap.append(self.Node(float('inf'), vertices))
            self.pq.location[vertices] = index
            index += 1

    def prim(self, graph):
        if self.pq.myHeap:

            min_node = self.pq.remove_min()

            for neighbour, weight in graph[min_node.label].items():
                if neighbour in self.pq.location:
                    if weight < self.pq.myHeap[self.pq.location[neighbour]].data:
                        self.pq.update(neighbour, weight)
                        self.discovered[neighbour] = min_node.label

            edge = '{0} -> {1}'.format(self.discovered[min_node.label],
                                       min_node.label)
            self.res.append(edge)
            self.prim(graph)

    def main(self, graph, start='A'):
        self.build_priority_queue(graph)
        self.pq.myHeap[self.pq.location[start]].data = 0
        self.discovered[start] = None
        self.prim(graph)
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

    p = PrimsMinimumSpaningTree()
    p.main(graph, start='A')
