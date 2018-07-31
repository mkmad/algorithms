class LCS(object):

    """
    Note: LCS doesn't necessarily require the chars to be
    continuous

    We have padding for both row and column because for any
    given position if the char in the row and the char in the
    column is the same then add 1 to the value at row - 1, col -1
    ( i.e the best possible value excluding the char at col and row )

    If the char at row and col is not the same then the value at the
    position is the max of value at either row - 1, col or row, col - 1

    To see what chars are present in the lcs, call the retrace path function
    the idea is to start from the very last indices for i and j.
    i.e set the initial position at row - 1, col - 1

    If the char at str2[col - 1] == str1[row - 1] then append the char at
    str2[col - 1] to subset and call retrace function with
    (row - 1 - 1, col - 1, -1)

    If the char are not the same, then check which of the value at
    (row, col - 1) or (row - 1, col) is greater and call retrace function
    at that position. If both the values are same then just move left i.e
    (row, col - 1)

    """

    def __init__(self):
        self.matrix = None
        self.str1 = None
        self.str2 = None
        self.subset = []

    def solution(self, str1, str2):
        # Note the padding for row and column
        self.str1 = str1
        self.str2 = str2
        self.matrix = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

        for j in range(1, len(self.matrix)):
            for i in range(1, len(self.matrix[0])):
                # if both
                if str2[j - 1] == str1[i - 1]:
                    self.matrix[j][i] = self.matrix[j - 1][i - 1] + 1
                else:
                    self.matrix[j][i] = max(self.matrix[j - 1][i], self.matrix[j][i - 1])

        return self.matrix

    def retrace_path(self, array, i, j):

        # need to be careful here, because if I let either
        # i or j to be 0 then i -1  is -1 which will give
        # the last value (wrapping)
        if i > 0 and j > 0:
            if self.str2[j - 1] == self.str1[i - 1]:
                self.subset.append(self.str2[j - 1])
                self.retrace_path(array, i - 1, j - 1)
            else:
                if array[j - 1][i] > array[j][i - 1]:
                    self.retrace_path(array, i, j - 1)
                else:
                    self.retrace_path(array, i - 1, j)


if __name__ == '__main__':
    lcs = LCS()
    res = lcs.solution('abcdaf', 'acbcf')
    for val in res:
        print val
    lcs.retrace_path(res, len(res[0]) - 1, len(res) - 1)
    print lcs.subset

