import sys


class DirectedGraphCycle(object):

    """
    Take all the vertices and put it in a set (white set).
    At the same time, maintain a grey set.

    For each vertex:
        1) if the vertex is in white, then put it in grey. If
           the vertex has neighbours repeat step 1 for its
           neighbours. After visiting all its neighbours( or if the
           vertex has no neighbours) remove the vertex from grey
           set
        2) if the vertex is grey, it means there is a cycle

    We also maintain a visited dict, which will help in printing
    the cycle (if it exists)

    Note: We can't use a simple dfs to detect a cycle in directed
          graph for the following reason(example):

          graph = {
            'A' : ['B', 'C'],
            'B': ['C'],
            'C': []
          }

          ^ This is not a cycle in directed graph, however its
            a cycle in undirected graph


         The below example is a cycle in directed graph

         graph = {
            'A' : ['B'],
            'B': ['C'],
            'C': ['A']
          }

          The reason maintaining a grey set works is because, say
          we start in 'A' (from the above example), then we put 'A'
          in grey set and recur to its neighbour ('B'). Now 'B' is
          in grey set and it moves on to 'C', now when 'C' checks
          for its neighbour ->'A' (which is in grey set) its exists
          saying its a cycle

          If we apply the same logic to the first example, since 'C'
          has no neighbour we remove 'C' from grey set and it will
          return to 'B'. Now, since 'B' explored all its neighbours
          we remove 'B' and ultimately 'A' because 'A' explored all
          its neighbours. The code exists (no cycle)

    """

    def detect_cycle(self, white, grey, graph):
        """
        At first, I din't have this function. I called
        dfs directly by passing 'A' as vertex param. This however,
        returned/exited at 'A' after visiting 'B' and 'C' as
        there was no cycle. But the algorithm says we need to
        make sure we work on all the vertices from white set,
        hence this function and hence the while loop.

        So, this is a unique example where I keep the code running
        even when the recursion exists prematurely while there is
        still more input data/entry points to work on
        """

        while white:
            self.dfs(list(white)[0], white, grey, graph)

    def dfs(self, vertex, white, grey, graph, prev=None, visited={}):
        """
        If the vertex is in white, move it to grey, work on its
        neighbours and remove from grey

        If the vertex is grey then cycle exists
        """

        # visited will help in cycle path (if cycle exists)
        visited[vertex] = prev
        if vertex in white:
            grey.add(vertex)
            white.discard(vertex)

            if graph[vertex]:
                for neighbour in graph[vertex]:
                    self.dfs(neighbour, white, grey, graph, prev=vertex, visited=visited)

            grey.discard(vertex)
        elif vertex in grey:
            print self.print_cycle(vertex, visited)
            sys.exit(0)

    def print_cycle(self, vertex, visited, path='', dicovered=[]):
        """
        This is pretty straightforward, however since there is a
        cycle and If I only rely on visited dict, recursion won't
        terminate. Hence use discovered to make sure I am not looping
        again and again as given in the example below:

        eg if visited has:

        D -> E
        E -> F
        F -> D

        """
        if vertex in visited and vertex not in dicovered:
            dicovered.append(vertex)
            path_ = '{0} -> {1}'.format(visited[vertex], vertex)
            if path:
                path = path_ + ' -> ' + path
            else:
                path = path_
            return self.print_cycle(visited[vertex], visited, path)
        else:
            return path


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': [],
        'D': ['A', 'E'],
        'E': ['F'],
        'F': ['D']
    }
    white = set()
    grey = set()

    # populate the white set
    for vertices in graph:
        white.add(vertices)

    dgc = DirectedGraphCycle()
    dgc.detect_cycle(white, grey, graph)
