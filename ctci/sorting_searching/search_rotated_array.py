class SearchInRotatedArray(object):

    """
    Given a sorted array of n integers that has been
    rotated an unknown number of times, write code to
    find an element in the array. You may assume that
    the array was originally sorted in increasing
    order


    EXAMPLE
    Input find 5 in {15, 16, 19, 20, 25, 1, 3 ,5 ,6 ,7 ,10 , 14}
    Output 8 (the index of 5 in the array)

    This is similar to binary search but at any given point (mid)
    it is a little tricky to decided which side to go next. Unlike
    binary search, where we compare the target against mid, here
    we make use of the idea that at any given moment of an rotated
    sorted array either the left of mid or the right of mid will
    be completely sorted linearly. Then we check if the target is
    in the range of the sorted section, if it is then go in that
    direction else go in the opposite direction

    """

    def search(self, array_, low, high, target):
        mid = (low + high) / 2
        if array_[mid] == target:
            print "Found element {0} at position {1}".format(target, mid)
        elif low > high or low < 0 or high > len(array_) - 1:
            return

        # check which section is sorted

        elif array_[low] < array_[mid]:  # The left side of mid is sorted linearly

            if array_[low] < target < array_[mid]:
                # search left
                self.search(array_, low, mid, target)
            else:
                # search right
                self.search(array_, mid, high, target)

        else:  # Right side of mid is sorted linearly

            if array_[mid] < target < array_[high]:
                # search right
                self.search(array_, mid, high, target)
            else:
                # search left
                self.search(array_, low, mid, target)


if __name__ == '__main__':
    s = SearchInRotatedArray()
    array_ = [15, 16, 19, 20, 25, 1, 3, 5, 6, 7, 10, 14]
    s.search(array_, 0, len(array_) - 1, 5)
