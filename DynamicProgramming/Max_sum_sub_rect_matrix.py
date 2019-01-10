import kadanes


class MaxSumSubRect(object):

    """
    Goal is to find a rectangle in the matrix who's sum is
    the maximum

    Note: This algorithm uses kadane's algorithm also ( max sum sub array)

    Sol,

    Two pointers (inner and outter) iterate through the columns of
    the matrix, both pointers start from the same column at every
    otter iteration. The inner pointer then iterates till the length of the
    columns

    We also maintain a sub array which is used in computing max
    sum sub array.

    At every outter iteration we reset the sub array with all values
    set to 0's and copy the values of the column over to the sub array
    and compute max sub array

    When the inner pointer moves on, we add the values of the column
    to the values of the values of the sub array and compute the
    max sum sub array using kadane's


    We also have 5 different variables, top, bottom, left, right and cur_max

    cur_max keeps track of the max value of all the rectangle's, i.e when
    kadane's algorithm returns the max value we check it against the cur_max
    if the value is higher then we update cur_max and set the other 4 variables

    top - the start position returned by kadane's
    dowm - end position returned by kadane's
    left - if the outter pointer
    right - is the inner pointer

    This way we can determine whats the max value (cur_max) and whats the
    co-ordinates of the max rectangle using top, down, left and right


    Note: For this algorithm to work there has to be at least one positive
    value in the matrix

    """

    def __init__(self, matrix_):
        self.left = self.right = self.top = self.down = 0
        self.matrix = matrix_
        self.kadanes = kadanes.Kadanes()

    def solution(self):
        cur_max = None
        for col in range(len(self.matrix[0])):
            # reset the sub array for every iteration
            subarray = [0 for _ in range(len(self.matrix))]

            # Here col is the outter pointer and fast_col is inner ptr
            fast_col = col
            while fast_col < len(self.matrix[0]):
                # copy / add the column over to the sub array
                for temp in range(len(self.matrix)):
                    subarray[temp] += self.matrix[temp][fast_col]

                # call kadanes to on the sub array to find the max
                # sub array
                res = self.kadanes.max_sub_array(subarray)

                if cur_max is not None:
                    # set all variables if the val from kadanes is
                    # greater then cur max
                    if cur_max < max(res.keys()):
                        cur_max = max(res.keys())
                        self.top, self.down = res[max(res.keys())]
                        self.left = col
                        self.right = fast_col
                else:
                    # execute the following if cur_max is None
                    cur_max = max(res.keys())
                    self.top, self.down = res[max(res.keys())]
                    self.left = col
                    self.right = fast_col

                # increment inner pointer
                fast_col += 1

        print self.top, self.down, self.left, self.right
        print cur_max


if __name__ == '__main__':

    matrix = [
        [2, 1, -3, -4, 5],
        [0, 6, 3, 4, 1],
        [2, -2, -1, 4, -5],
        [-3, 3, 1, 0, 3]
    ]
    m = MaxSumSubRect(matrix)
    m.solution()
