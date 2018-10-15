class MinCoins(object):

    """
    Given a total, and a set of unlimited denominations of coins
    what is the minimum number of coins that's required to get
    the total

    This is similar to subset sum, I have padding on both
    the first column and the first row. The only difference
    here is if the col is <= coins[row] then select the
    coin and look back in the same row i.e

        1 + matrix[row][col - coins[row]]

    Also note, we also need to compare the value in the top
    row to check if the value is lesser than what we calculated
    above, this is the reason we need padding in the topmost
    row coz we need to compare the 1st row with 0th row

    Note: For the 1'st row don't get the min value of the current
    position and the top position as it will always result in 0
    (since the 0th row is filled with 0)

    we need padding in the 0th column because we need to fetch
    value from the left if the coins[row] >= col

    Retracing path is also pretty straightforward, if the value
    of a position is same as the one on top then the value is comin
    from top so don't select the row if not select the row and
    move to matrix[row][col - coins[row]]

    """

    def __init__(self):

        self.target = 11
        self.coins = [1, 5, 6, 8]

        self.matrix = [[0] * (self.target + 1) for _ in range(len(self.coins) + 1)]
        self.retrace = []

    def solution(self):

        print "Before"
        for val in self.matrix:
            print val

        # Start the iteration from the 1st row and the 1st
        # column
        for row in range(1, len(self.coins) + 1):
            for col in range(1, len(self.matrix[0])):
                # row - 1 because row values goes 1 above the len(self.coins)
                if self.coins[row - 1] <= col:
                    # Don't take min for the 1st row
                    # Also note, its the 1st row not 0th
                    if row == 1:
                        self.matrix[row][col] = 1 + self.matrix[row][(col - self.coins[row - 1])]
                    # For all other rows get the min value either from top or
                    # picking the coin
                    else:
                        self.matrix[row][col] = min(
                            1 + self.matrix[row][(col - self.coins[row - 1])],
                            self.matrix[row - 1][col]
                        )
                else:
                    # just get the value from top
                    self.matrix[row][col] = self.matrix[row - 1][col]

        print "\nAfter"
        for val in self.matrix:
            print val

    def retrace_path(self, row, col):
        if row == 0 or col == 0:
            return
        if self.matrix[row - 1][col] == self.matrix[row][col]:
            self.retrace_path(row - 1, col)
        else:
            # Don't forget that the coins index is
            # row - 1
            self.retrace.append(self.coins[row - 1])
            self.retrace_path(row, col - self.coins[row - 1])


if __name__ == '__main__':
    m = MinCoins()
    m.solution()
    m.retrace_path(len(m.matrix) - 1, len(m.matrix[0]) - 1)
    print
    print "Coins are:"
    print m.retrace

