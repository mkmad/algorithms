class PalindromicSubsequence(object):

    """
    Longest palindromic sub sequence is:

    eg:   agbdba
    sol:  abdba

    Sol:

    We go through the matrix diagonally, with each
    diagonal representing the length of the substring
    that's under consideration. We only fill the top right
    portion of the diagonal. The first diagonal represents
    substring of length 1 as denoted by the indices i.e
    matrix[i][j] where i == j.

    The second diagonal is of length 2. eg matrix[0][1]
    considers the substring from 0 to 3.

    The third diagonal considers substring of length 3 and
    so on..

    The first diagonal is populated with value 1 since LPS of
    a substring of length 1 is 1

    For all other diagonals, we check if
        substring[i] == substring[j]


    if it is then:

        matrix[i][j] = 2 + matrix[i + 1][j - 1]

        here:
            2 = len(string[i]) + len(string[j])
            matrix[i + 1][j - 1] = LPS value of the substring in between i and j

        Note: its i + 1 because i is the row pointer and we are looking at
              the bottom left box


    else:

        matrix[i][j] =  max(matrix[i][j - 1], matrix[i + 1][j])

        i.e. the max value between the LPS of substrings from i to j - 1
             and the sub string i + 1 to j



    """

    def __init__(self):
        self.matrix = None
        self.test_string = None

    def solution(self, test_string):
        self.test_string = test_string
        self.matrix = [[0] * len(test_string) for _ in range(len(test_string))]

        diagonal = 0

        while diagonal < len(test_string):

            col = diagonal
            row = 0
            while col < len(test_string):
                if diagonal == 0:
                    self.matrix[row][col] = 1
                else:
                    if test_string[row] == test_string[col]:
                        self.matrix[row][col] = 2 + self.matrix[row + 1][col - 1]
                    else:
                        self.matrix[row][col] = max(self.matrix[row][col - 1], self.matrix[row + 1][col])

                row += 1
                col += 1

            diagonal += 1

        for val in self.matrix:
            print val


if __name__ == '__main__':
    ps = PalindromicSubsequence()
    ps.solution(list('agbdba'))
