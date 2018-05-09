class HamiltonianCycle(object):

    """
    For a given graph, see if you can
    start at a given position and traverse
    through all the verices of the graph by
    visiting each vertex exactly once


    This is a simple backtracking problem, for
    each vertex the number of branches will be
    the number of adjacent vertices. Also maintain
    a visited set to check if you have visited
    a vertex before or not
    """