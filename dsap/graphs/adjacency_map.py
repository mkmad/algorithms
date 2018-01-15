class AdjacencyMap(object):

    class Edge(object):

        def __init__(self, label, vertex1, vertex2):
            self.label = label
            self.vertex1 = vertex1
            self.vertex2 = vertex2

        def opposite(self, vertex):
            if vertex is self.vertex1:
                return self.vertex2
            elif vertex is self.vertex2:
                return self.vertex1

        def get_vertices(self):
            return self.vertex1, self.vertex2

    def __init__(self):

        self.edges = {
            'e1': self.Edge('e1', 'A', 'B'),
            'e2': self.Edge('e2', 'B', 'C'),
            'e3': self.Edge('e3', 'C', 'D'),
            'e4': self.Edge('e4', 'D', 'E'),
            'e5': self.Edge('e5', 'A', 'E'),
            'e6': self.Edge('e6', 'A', 'F'),
            'e7': self.Edge('e7', 'B', 'E'),
            'e8': self.Edge('e8', 'B', 'F'),
            'e9': self.Edge('e9', 'E', 'F')
        }

        self.my_map = {
            'A': [
                {
                    'B': self.edges['e1']
                },
                {
                    'E': self.edges['e5']
                },
                {
                    'F': self.edges['e6']
                }
            ],
            'B': [
                {
                    'A': self.edges['e1']
                },
                {
                    'C': self.edges['e2']
                },
                {
                    'E': self.edges['e7']
                },
                {
                    'F': self.edges['e8']
                }
            ],
            'C': [
                {
                    'B': self.edges['e2']
                },
                {
                    'D': self.edges['e3']
                }
            ],
            'D': [
                {
                    'C': self.edges['e3']
                },
                {
                    'E': self.edges['e4']
                }
            ],
            'E': [
                {
                    'A': self.edges['e5']
                },
                {
                    'B': self.edges['e7']
                },
                {
                    'F': self.edges['e9']
                }
            ],
            'F': [
                {
                    'A': self.edges['e6']
                },
                {
                    'B': self.edges['e8']
                },
                {
                    'E': self.edges['e9']
                }
            ]
        }
