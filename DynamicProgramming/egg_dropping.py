class EggDropping(object):

    """
    Given a number of eggs and a building with certain number of
    floors, find out which is the lowest floor where the egg will
    break

    The columns represent number of floors and the rows represent
    the number of eggs. There are no padding in either columns or
    row

    The first row is just filled with the column value. i.e at any
    given floor the min number of tries it takes to break an egg with
    just one egg is equal to the number of floors

    For all other rows, at a particular column we check the following

    for k going from 1 to col. we check two cases for every k and take the
    max of these two cases:
         1) if an egg breaks at the kth floor then we have n - 1 eggs and
            and k - 1 floors to work with (i.e matrix[row - 1][k - 1])
        2) if egg doesn't break then we have col - k floors and n eggs to
           work with (i.e. matrix[row][col - k])

    then we add 1 to max value for each iteration of k considering the
    current iteration as an attempt. We store the result in an temporary
    array.

    After all the k iterations we check for minimum value from the temporary
    array and then store it as the value for matrix[row][col]


    There are edge cases to consider:
    k = 0, k = col and since the matrix is 0 indexed and both floors and col
    starts from 1, we meed to consider that

    """

    def __init__(self, floors, eggs):
        self.floors = floors
        self.eggs = eggs

        self.matrix = [[0 for _ in range(floors)] for _ in range(eggs)]

    def solution(self):

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                if row == 0:
                    self.matrix[row][col] = col + 1
                    continue
                else:
                    sums = []
                    if row == 1 and col == 2:
                        pass
                    for k in range(col + 1):
                        if k == 0:
                            sums.append(1 + max(0, self.matrix[self.eggs - 1][col - 1]))
                        elif k == col:
                            sums.append(1 + max(self.matrix[self.eggs - 2][k - 1], 0))
                        else:
                            sums.append(1 + max(self.matrix[self.eggs - 2][k - 1],
                                                self.matrix[self.eggs - 1][col - k - 1]))
                    self.matrix[row][col] = min(sums)

        print self.matrix


if __name__ == '__main__':
    e = EggDropping(6, 2)
    e.solution()



