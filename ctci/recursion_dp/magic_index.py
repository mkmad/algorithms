class MagicIndex(object):
    """
    Magic Index: A magic index in an array A[1. .. n-1]
    is defined to be an index such that A[i] = i. Given
    a sorted array with repeating/non repeating integers,
    write a method to find a magic index, if one exists,
    in array A

    Similar to binary search, check if the index is the magic
    index else if the a[index] is greater than the index there
    are two possibilities:

        1) The magic index has to be on the left of index
           (if there are no repeated values then the values
           to the right of index will be greater and all the
           indices in the right)

        2) The magic index might be in the right (if and only
           if there are repeated values, in that case simply
           move to a[index] as the next mid because all the
           intermediary indices from index to a[index] will
           be useless as they are repeating)

    If the a[index] is less then do the same thing in the other
    direction

    Note:
          1) Maintain a visited array as there might be
             redundant calls to a particular index
          2) Watch out for negative values, because a[-ve value]
             will wrap around
          3) I used sys.exit to stop the recursion when magic
             index is found this will not help of there are more
             than one magic index or in this case I tried to call
             the function twice(for repeating and non repeating
             arrays) sys.exit completely exited the control
             including main
    """

    def __init__(self):
        self.visited = []

    def find_magic_index_with_repeating_vals(self, array_, index=0):
        if 0 <= index < len(array_):
            self.visited.append(index)
            if array_[index] == index:
                print "\nMagic Index is:", index

            else:
                if array_[index] < index:
                    if array_[index] > -1 and array_[index] not in self.visited:
                        self.find_magic_index_with_repeating_vals(array_, array_[index])
                    next_mid = (len(array_) + index - 1) / 2
                    if next_mid not in self.visited:
                        self.find_magic_index_with_repeating_vals(array_, next_mid)
                else:
                    if array_[index] > -1 and array_[index] not in self.visited:
                        self.find_magic_index_with_repeating_vals(array_, array_[index])
                    next_mid = index / 2
                    if next_mid not in self.visited:
                        self.find_magic_index_with_repeating_vals(array_, next_mid)


if __name__ == '__main__':
    print '\nNon Repeating Array is:'
    array_ = [-40, -20, -1, 1, 2, 3, 6, 8, 9, 12, 13]
    print array_
    mi = MagicIndex()
    mi.find_magic_index_with_repeating_vals(array_)
    print '\n\nRepeating Array is:'
    array_ = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    print array_
    mi.visited = []
    mi.find_magic_index_with_repeating_vals(array_)
