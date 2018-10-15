class EditDistance(object):

    """
    Given a set of operations like edit, delete and add
    how many operations will it take to convert one string
    to another


    We need padding for both row and column, lets represent
    string2 in the column and string1 in the row. Now the 0th
    row suggests converting an empty string1 to string2. Hence
    the values in the 0th row will be same as the length of the
    substring denoted by the column index. The same goes for the
    0th column


    For all the other rows and columns, check

        if string2[col] == string1[row]:
            matrix[row][col] =  matrix[row][col] // no edit required
        else:
            matrix[row][col] = min(
                                    matrix[row - 1][col],        // modify str1 to str2 (mostly delete)
                                    matrix[row - 1][col - 1],    // don't modify
                                    matrix[row][col - 1]         // modify str2 to str1 (mostly delete)
                                )

    Retracing path is pretty straightforward, just follow the code

    """

    def __init__(self):
        self.string1 = None
        self.string2 = None
        self.matrix = None

    def build_matrix(self):
        self.matrix = [
            [0]*(len(self.string2) + 1) for _ in range(len(self.string1) + 1)
        ]

    def retrace_path(self, row, col):

        if row == 0 or col == 0:
            return

        # chars are the same so do nothing, just move
        elif self.string2[col - 1] == self.string1[row - 1]:
            self.retrace_path(row - 1, col - 1)

        elif self.matrix[row][col] == self.matrix[row - 1][col - 1] + 1:
            print "Edit {0} from string 2 to {1} in string1".format(
                self.string2[col - 1],
                self.string1[row - 1]
            )
            self.retrace_path(row - 1, col - 1)

        elif self.matrix[row][col] == self.matrix[row][col - 1] + 1:
            print "Delete {0} from String2".format(self.string2[col - 1])
            self.retrace_path(row, col - 1)

        elif self.matrix[row][col] == self.matrix[row - 1][col] + 1:
            print "Delete {0} from String1".format(self.string1[row - 1])
            self.retrace_path(row - 1, col)

        else:
            pass

    def solution(self, str1, str2):
        self.string1 = str1
        self.string2 = str2
        self.build_matrix()

        print "Before"
        for val in self.matrix:
            print val

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):

                if row == 0:
                    if col > 0:
                        self.matrix[row][col] = self.matrix[row][col - 1] + 1

                elif col == 0:
                    if row > 0:
                        self.matrix[row][col] = self.matrix[row - 1][col] + 1

                elif str2[col - 1] == str1[row - 1]:
                    self.matrix[row][col] = self.matrix[row - 1][col - 1]

                else:

                    self.matrix[row][col] = min(
                        self.matrix[row - 1][col],
                        self.matrix[row - 1][col - 1],
                        self.matrix[row][col - 1]
                    ) + 1

        print "After"
        for val in self.matrix:
            print val


if __name__ == '__main__':
    e = EditDistance()
    e.solution("azced", "abcdef")
    print
    e.retrace_path(len(e.matrix) - 1, len(e.matrix[0]) - 1)
