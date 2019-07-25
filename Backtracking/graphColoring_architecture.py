class GraphColoring(object):

    """

    Problem:
    ========

    For a given graph with n vertices find all
    possible ways to color the vertices with m
    colors at your disposal

    Main condition:
    ===============

    No two adjacent vertices should have the same color

    Success:
    ========

    For each vertex you have to choose (branch) from m different
    colors, if you are able to color all the vertices then
    return true


    """

    def __init__(self, colors, vertices):
        self.color_mapping = {}
        self.colors = colors
        self.vertices = vertices

    def graph_coloring(self, vertex):
        """

        logic:
        ======

            for every vertex I need to know what are the
            colors of the neighbouring vertices to make a
            decision


        backtracking cases:
        ===================

            1. if we run out of colors (i.e if the for loop for picking
               different colors terminates) for a particular node
               we need to backtrack. This happens when the control checks
               to find out if none of the colors can be used for the given
               node, since all of them violate the main condition which is:

               "No two adjacent vertices should have the same color"


        terminating cases:
        ==================

            Failure
            -------
                1. If the for loop at the root/start node terminates

            Success
            -------
                1. If all the nodes are colored


        maintaining states (colors of each node in this case):
        =======================================================

            1. maintain a color dict that maps the nodes to its
               color. There are two scenarios where the color dict
               can get updated

                1. moving forward from a node to its neighbour
                2. When the control backtracks

        Design:
        =======

            The function needs to be recursive, since we are repeating the
            same thing for every node.

            Entry and Exit points
            =====================

                1. Control will enter the function in two ways:
                    a. from parent (normal flow)
                    b. from child (backtrack)

                2. Control will also exit in two ways:
                    a. move/exit to the child (if the node was able to find a
                       color for itself)
                    b. move/exit to parent (if the node was not able to find a
                       color for itself)

        Assumptions:
        ============

            1. The vertices dict is a adjacency map (each vertex has a map of all its
                neighbours)

        Flow:
        =====

            for a given vertex -> pick a color (if its safe) -> bfs traversal of all
            the neighbours -> return true to the parent (previous backtracked call)
            only any of the child recursive calls returns true, if none of the child
            recursive calls return true it means that the current chosen color is not
            valid so remove that from the color map



        """

        # get the neighbours thats been colored already
        neighbours = set(self.vertices[vertex]).intersection(set(self.color_mapping))

        for color in self.colors:
            if self.is_safe(neighbours, color):
                valid_color = False
                self.color_mapping[vertex] = color
                for neighbour in self.vertices[vertex]:
                    if neighbour not in self.color_mapping:
                        if self.graph_coloring(neighbour):
                            valid_color = True
                if not valid_color:
                    self.color_mapping.pop(vertex)
                    return False
                else:
                    return True

    def is_safe(self, neighbours, color):
        for _neighbour in neighbours:
            if self.color_mapping[_neighbour] == color:
                return False

        return True

