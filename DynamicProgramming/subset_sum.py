class SubsetSum(object):

    """

    Subset sum is given a total and a set of numbers. Find out
    if there is a subset of numbers that will add up to the given
    total

    concept is pretty simple, maintain a boolean 2D array with
    i (column) going from 0 to the total and len(set) j's (rows)

    Now for each row and column we check if the subset[row] value is
    same as the column value (i == subset[j]), if it is then it means
    we can attain the total (in this case the column value).

    If i < subset[j] then we check the top value (i, j - 1) to see
    if its true or not and set the value accordingly. If the top value
    is true it means that we can omit the current value and we are able
    to get the column sum from the previous rows

    For all the values of i that are > subset[j]. We check either the
    top value or if (i - subset[j], j - 1) is true. Note: set the value
    to true if either one of the value is true


    Note:

        The first column is populated with True, because for each row, we
        can simply omit the value and result will be 0.

        Also note: if i == subset[j] it can also be infered as value
        of matrix[j - 1][i - subset[j]] which is matrix[j - 1][0] which
        is True based on the values set in the columns

    To retrace the numbers, start from the very last (row, col). If
    the value at any given position is True and its
    (row - 1, col - subset[row]) is also True then pick this item and move to
    that position, else if the True is coming from the top value then just
    move to the top position, don't select

    """

    def __init__(self):
        self.total = 11
        self.subset = [3, 2, 10, 8, 7]
        self.matrix = [
            [False] * (self.total + 1) for _ in range(len(self.subset))
        ]
        self.result = []

    def solution(self):

        # Sort the array, else this algorithm won't work
        self.subset.sort()

        # Set the first column to true (The padding column)
        for val in range(len(self.subset)):
            self.matrix[val][0] = True

        for j in range(len(self.subset)):
            # Note, i starts from 1
            for i in range(1, len(self.matrix[0])):
                if j > 0:
                    if i >= self.subset[j]:
                        # Either the top value should be true or
                        # the j - 1, i - self.subset[j] should be true
                        if self.matrix[j - 1][i] or \
                                self.matrix[j - 1][i - self.subset[j]]:
                            self.matrix[j][i] = True
                    else:
                        # For the columns that are smaller than the
                        # subset[j] just get the value from the top
                        if self.matrix[j - 1][i]:
                            self.matrix[j][i] = True
                else:
                    # For the first row, set the value to true only
                    # if the column is same as the subset[j] i.e
                    # subset[0]
                    if self.subset[j] == i:
                        self.matrix[j][i] = True

    def retrace(self, i, j):
        if i > 0 and j > 0:
            if self.matrix[j][i]:
                if self.matrix[j - 1][i - self.subset[j]]:
                    self.result.append(self.subset[j])
                    self.retrace(i - self.subset[j], j - 1)
                elif self.matrix[j - 1][i]:
                    self.retrace(i, j - 1)


if __name__ == '__main__':
    s = SubsetSum()
    s.solution()
    print
    for val in s.matrix:
        print
        print val
    s.retrace(len(s.matrix[0]) - 1, len(s.matrix) - 1)
    print
    print "Subset is:"
    print s.result
