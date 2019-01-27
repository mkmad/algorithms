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
           be useless as they might be repeating)

    If the a[index] is less then do the same thing in the other
    direction

    Note:
          1) Maintain a visited array as there might be
             redundant calls to a particular index because we
             might be searching both left and right side of a
             given index over and over again

          2) Watch out for negative values, because a[-ve value]
             will wrap around and not to mention

          3) I used sys.exit to stop the recursion when magic
             index is found this will not help of there are more
             than one magic index or in this case I tried to call
             the function twice(for repeating and non repeating
             arrays) sys.exit completely exited the control
             including main

    Also Note: This code checks for all possible magic indices not
               just the first occurrence of the magic index

    """

    def __init__(self):
        self.visited = []

    def find_magic_index_with_repeating_vals(self, array_, index=0):
        if 0 <= index < len(array_):
            # Only execute the code if the index is not been visited
            # before
            if index not in self.visited:
                self.visited.append(index)
                if array_[index] == index:
                    print "\nMagic Index is:", index

                else:
                    if array_[index] < index:
                        # since the values might be repeating, we check both sides
                        # of the index. For this particular condition since
                        # array_[index] < index, its obvious to check in the right
                        # side of the index but since the value might be repeating
                        # we also need to check the left side

                        # check left
                        next_mid = array_[index]
                        if next_mid > -1:
                            self.find_magic_index_with_repeating_vals(array_, next_mid)

                        # when the control returns check the right side like binary search
                        next_mid = (len(array_) + index - 1) / 2
                        self.find_magic_index_with_repeating_vals(array_, next_mid)
                    else:

                        # This is the case when the array_[index] > index so check the
                        # right side by bumping the next_mid to array_[index] and check
                        # the left side normally like binary search

                        # check the right side
                        next_mid = array_[index]
                        if next_mid > -1:
                            self.find_magic_index_with_repeating_vals(array_, array_[index])

                        # check the left side
                        next_mid = index / 2
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
