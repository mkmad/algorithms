class OptimalBST(object):

    """
    Given an array of keys/values in a BST along with the
    frequencies in which those keys are searched. Find the
    best arrangement of these keys in the BST where the total
    cost of searching every key is minimum

    we construct the BST using a 2D array. The values are
    populated diagonally. Each diagonal represents a level,
    hence the 2D array is filled level by level

    The first diagonal (0th level) is basically the array itself,
    we maintain the values of the frequency if the array

    In the second level we consider a sliding window of two
    elements at a time and determine which key should be the root
    and which key should be the child. This is important because
    the root level has cost = 1 and the 1st level has cost 2

    so for eg if the keys are [3, 4] then 4 should be the root
    because 4 * 1 + 3 * 2 < 3 * 1 + 4 * 2

    For 3rd level the sliding window is 3 elements at a time.
    Here there are three cases:

        1. If the 1st element is the root, then consider the value
           minimum value of a subtree that consists of 2nd and 3rd
           element (i.e right of root)
        2. If 2nd element is the root the value of
           left of root + right of root
        3. If the 3rd element is the root then consider the left
           of root

    Now, the final value will be the minimum of all the three cases
    above.

    Note: For levels 3 and above follow the same procedure.

    Also, note: Do not include the value of the root in the above
    three cases, we do this because even before calculating the
    values we add all the elements the the min value from the above
    calculation is added to the total.

    The program first considers all the values in the sliding window
    to be in the same level and hence adds all of them. Later
    depending of how it restructures the tree we add the values of the
    lower sub tree to the total (not the root) because lvl 1 is 1 and
    lvl 2 is 2 and so on..


    IMPORTANT
    ---------

    Note how to populate the values in the 2D array diagonally. We
    need a loop for each and every diagonal. Under this loop wee need
    another loop that controls the row and column value. In the inner
    loop the column value will start from where the outter loop starts
    (i.e start of each diagonal) meanwhile rows start from 0. At the
    end of the inner loop increment both row and column by 1 to traverse
    diagonally. Both the loops check for out of bounds len(matrix) as
    terminating condition

    """

    def __init__(self):

        # array of (keys, frequency of search) in the BST
        self.array = [(21, 3), (12, 2), (16, 6), (10, 4)]
        self.matrix = [[0] * len(self.array) for _ in range(len(self.array))]

    def calculate_values(self, row, col):
        res = []
        # If the no of elements < 3
        if col == row + 1:
            return min(self.array[row][1], self.array[col][1])
        # If the no of elements > 3
        else:
            # Note do not add the value at idx as that would
            # be the root
            for idx in range(row, col + 1):
                if idx == row:
                    res.append(
                        self.matrix[idx + 1][col]
                    )
                elif idx == col:
                    res.append(
                        self.matrix[row][idx - 1],
                    )
                else:
                    res.append(
                        self.matrix[row][idx - 1] +
                        self.matrix[idx + 1][col]
                    )
            return min(res)

    def solution(self):

        print "Before"
        for val in self.matrix:
            print val

        current_start_column = 0
        while current_start_column < len(self.matrix[0]):
            row = 0
            col = current_start_column

            while row < len(self.matrix) and col < len(self.matrix):
                # for the first diagonal
                if row == col:
                    self.matrix[row][col] = self.array[row][1]
                else:
                    level_sum = 0

                    # Calculate the total for the current
                    # sliding window, this is where we consider
                    # all the keys to be in the same level
                    for val in range(row, col + 1):
                        level_sum += self.array[val][1]

                    # Now try all possible restructuring and
                    # add the values of the sub tree to the total
                    values = self.calculate_values(row, col)
                    total_sum = level_sum + values

                    self.matrix[row][col] = total_sum

                row += 1
                col += 1

            current_start_column += 1

        print "After"
        for val in self.matrix:
            print val


if __name__ == '__main__':
    o = OptimalBST()
    o.solution()
