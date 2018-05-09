class SortedMatrixSearch(object):

    """
    Sorted Matrix Search: Given an M x N matrix in which
    each row and each column is sorted in ascending order,
    write a method to find an element

    So, we partition our grid into four quadrants and
    recursively search the lower left quadrant and the upper
    right quadrant. These, too, will get divided into quadrants
    and searched. Observe that since the diagonal is sorted,
    we can efficiently search it using binary search.

    """
    def __init__(self):
        pass