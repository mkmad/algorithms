class RodCutting(object):

    """
    Given a rod of length N and a cost array of tuples with
    the first element of each tuple being length <= N and the second
    element of the tuple being the profit price of the corresponding length

    Sol,

    The length of rod goes through the column with a padding i.e 0th col
    exists. The rows are same as the len of cost array

    At any given position we check whats the max profit of

    either cutting the rod at a given len (same as cost[row][0]) and
    adding the price of cost[row][1] with the price at
    matrix[row][col - cost[row][0]]

    or

    not cutting the rod at the given length and considering the price
    at matrix[row - 1][col]


    Retracing the path,

    Start from the rightmost element, and check if the current element
    is coming from the top ( matrix[row-1][col] ) if it is then just move
    the pointer to top else check if the given value is cost[row][1] +
    matrix[row][col - cost[row][0]] (i.e we cut the rod with the len
    cost[row][0]) then move the pointer to matrix[row][col - cost[row][0]]
    and add cost[row][0] to the result array. The recursion stops when the
    pointer reaches 0th col.

    Note: We check if the value is coming from top first and then check if
    the value is the addition later (i.e. prioritize that way) else the retrace
    won't work. Also, if you reach 0th row before you reach 0th col then
    you need to add the rod len at 0th row to the result array as well

    """

    def __init__(self, len_, cost):
        self.len = len_
        self.cost = cost
        self.matrix = [[0 for _ in range(len_ + 1)] for _ in range(len(self.cost))]

    def solution(self):

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                if col == 0:
                    self.matrix[row][col] = 0
                    continue  # do not move forward

                if col < self.cost[row][0]:
                    self.matrix[row][col] = self.matrix[row - 1][col]
                else:
                    self.matrix[row][col] = max(self.matrix[row - 1][col],
                                                self.cost[row][1] + self.matrix[row][col - self.cost[row][0]])

        for val in self.matrix:
            print val

    def retrace_path(self):
        row = len(self.matrix) - 1
        col = len(self.matrix[0]) - 1
        result = []

        while row >= 0 and col >= 0:
            if col == 0:
                break

            if row == 0:
                result.append(self.cost[row][0])
                break

            if self.matrix[row][col] == self.matrix[row - 1][col]:
                row = row - 1

            elif self.matrix[row][col] == self.cost[row][1] + self.matrix[row][col - self.cost[row][0]]:
                result.append(self.cost[row][0])
                col = col - self.cost[row][0]

        print result


if __name__ == '__main__':
    r = RodCutting(5, [(1, 2), (2, 5), (3, 7), (4, 8)])
    r.solution()
    r.retrace_path()
