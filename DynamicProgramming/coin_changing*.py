class CoinChanging(object):

    """
    Given a set of coins (with infinite supply of each coins)
    find out how many ways (combinations) there are to come up
    with a given total

    Eg:

        total = 5
        coins = [1, 2, 3]

        No of ways:

            1 1 1 1 1
            1 1 1 2
            1 1 3
            2 3
            1 2 2

            = 5 ways

    Sol,

        First construct a matrix with rows going from 0 to len(coin set) and
        column going from 0 to total

        The important insight is the 0th row and the 0th col:

            The 0th col indicates a total of 0, so irrespective of any coins
            the only way to achieve a total of 0 is by not picking it. Hence
            we populate the 0th col with 1's.

            The 0th row indicates 0 coins , hence irrespective of any
            total with 0 coins there is no ways to come up with that total.
            Therefore we populate the 0th row with 0's.


        For all the other rows and column we check if if coins[row - 1] (since
        we have an extra row) greater than the current col - which represents
        the current total.

            a) if coins[row - 1] > col then we can't make a total that's equal to col
               from coins[row - 1] therefore populate matrix[row][col] with the
               above value i.e. matrix[row - 1][col]

            b) if coins[row - 1] < col then we need to add all the ways we can get
               the total ( equals to col ) including the current coin (i.e coins[row - 1])
               and the ways excluding the current coin

               matrix[row - 1][col] <- excluding the current coin

               matrix[row][col - coins[row - 1]] <- including the current coin, i.e select the
                                                    current coin, subtract it from the total
                                                    and get the number of ways from:
                                                        col - coins[row - 1]

               So,

               matrix[row][col] = matrix[row - 1][col] + matrix[row][col - coins[row - 1]]


    Note:
        In L 80 I have a continue statement, this will make sure that the control
        doesn't go to L 85 for col = 0 where self.coins[row - 1] > 0

    """

    def __init__(self, coins, total):
        self.coins = coins
        self.total = total
        self.matrix = [[0 for _ in range(self.total + 1)] for _ in range(len(self.coins) + 1)]

    def solution(self):

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                if col == 0:
                    self.matrix[row][col] = 1
                    continue
                if row == 0:
                    self.matrix[row][col] = 0

                else:
                    if col < self.coins[row - 1]:
                        self.matrix[row][col] = self.matrix[row - 1][col]
                    else:
                        self.matrix[row][col] = \
                            self.matrix[row - 1][col] + self.matrix[row][col - self.coins[row - 1]]

        for val in self.matrix:
            print val


if __name__ == "__main__":
    c = CoinChanging([1, 2, 3], 5)
    c.solution()
