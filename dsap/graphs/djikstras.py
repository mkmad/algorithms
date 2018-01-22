from priorityQueue import PriorityQueue


class Djikstraks(object):

    """
    Goal is to find single source shortest path
    to all the other vertices

    Its exactly same as prims algorithm. The only difference is
    when we calculate the distance to a vertex, its the some of
    the distance of min vertex to the neighbour and source vertex
    to min vertex

    """

    class Node(object):
        def __init__(self, data, label):
            self.data = data
            self.label = label

    def __init__(self):
        self.pq = PriorityQueue()
        self.discovered = {}
        self.distance = {}
        self.res = []

    def build_priority_queue(self, graph):
        """
        Build the priority queue by adding inf to all the vertices
        and update the location of each vertex in the heap
        accordingly
        """
        index = 0
        for vertices in graph:
            self.pq.myHeap.append(self.Node(float('inf'), vertices))
            self.pq.location[vertices] = index
            index += 1

    def djikstras(self, graph):
        """
        Remove the minimum weight vertex from the heap and check its
        neighbours. If the weight from the minimum vertex to its
        neighbour is less than that of the neighbours, update the
        neighbours weight.

        Also, update the discovered dict, saying you reached the neighbour
        from this vertex

        Update the distance also, he distance is the sum of the distance
        from source to min node and the distance from min node to the neighbour
        """
        if self.pq.myHeap:

            min_node = self.pq.remove_min()

            for neighbour, weight in graph[min_node.label].items():
                # I need to check if neighbour exists in location dict
                # because I am constantly deleting and updating the
                # location. I use location and not heap because heap
                # stores obj's

                # This also ensures that I don't check the neighbour if
                # it was already deleted from the queue (in other words; if
                # the edge already made it to result)
                if neighbour in self.pq.location:
                    if weight < self.pq.myHeap[self.pq.location[neighbour]].data:
                        self.pq.update(neighbour, weight)
                        self.discovered[neighbour] = min_node.label
                        self.distance[neighbour] = self.distance[min_node.label] + weight

            self.djikstras(graph)

    def main(self, graph, start='A'):
        """
        Note: The data value of the start vertex should be 0, as this
        will make sure we remove the start vertex first (since every other
        vertex is inf)

        The distance of the start vertex is set to 0 as well
        """
        self.build_priority_queue(graph)
        self.pq.myHeap[self.pq.location[start]].data = 0
        self.discovered[start] = None
        self.distance[start] = 0
        self.djikstras(graph)
        print self.discovered
        print self.distance


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

    d = Djikstraks()
    d.main(graph, start='A')
