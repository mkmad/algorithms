class LCS(object):

    """
    This is different than longest common sub sequence. Here
    we just check if the value at col and row are the same and if
    they are then the value at matrix[row][col] = matrix[row][col] + 1
    else don't do anything (unlike LC Sub sequence where we consider the
     top value or the left value)

    Also note: I have a padding for 0th row and 0th col since we'll
               be looking at the top left value

               You can also keep track of the max value to find out
               whats the length of the longest common substring

    """

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

        self.matrix = [
            [0 for _ in range(len(self.str1) + 1)] for _ in range(len(self.str2) + 1)
        ]

    def solution(self):
        # var to keep track of longest common substring
        max_val = -1
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                if row == 0:
                    self.matrix[row][col] = 0
                    continue
                elif col == 0:
                    self.matrix[row][col] = 0
                    continue
                else:
                    if self.str1[col - 1] == self.str2[row - 1]:
                        self.matrix[row][col] = self.matrix[row - 1][col - 1] + 1
                        if self.matrix[row][col] > max_val:
                            max_val = self.matrix[row][col]

        for val in range(len(self.matrix)):
            print self.matrix[val]

        print
        print "Length of Longest common substring is",  max_val


if __name__ == '__main__':
    l = LCS('abcdaf', 'zbcdf')
    l.solution()
