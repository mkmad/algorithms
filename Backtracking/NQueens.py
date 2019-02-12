import math


class EightQueens(object):

    """
    Eight Queens: Write an algorithm to print all
    ways of arranging eight queens on an 8x8 chess
    board so that none of them share the same row,
    column, or diagonal.
    """

    @staticmethod
    def check_valid(x, y, placed):
        for x1, y1 in placed:
            if x == x1 or y == y1 or math.fabs(x - x1) == math.fabs(y - y1):
                return False

        return True

    def place_queen(self, row, column, num_queens, placed):
        # print if row == num_queens, since row is zero indexed
        if row == num_queens:
            print placed

        # Backtrack if the column goes overboard
        # Note, I remove the previously placed queen and look
        # for possible locations from one square after the prev
        # square (I don't look in the left of the prev square since
        # that was the first valid location for that row)
        elif column > num_queens - 1:
            prev = placed.pop()
            self.place_queen(row - 1, prev[1] + 1, num_queens, placed)

        # Check if the current square if valid, if it is then place
        # the queen and move to the next row else, move to the next
        # column
        elif self.check_valid(row, column, placed):
            placed.append((row, column))
            self.place_queen(row + 1, 0, num_queens, placed)
        else:
            self.place_queen(row, column + 1, num_queens, placed)


if __name__ == '__main__':
    e = EightQueens()
    num_of_queens = 8

    # Use this for loop to start from all possible
    # starting locations

    # Also note, I am just printing the first set of
    # combination to place the queens for any given
    # start location, so the algorithm doesn't consider
    # all the other available possibilities of placing
    # the queens for a given start location

    print
    for val in range(num_of_queens):
        print "Start location ({0} : {1})".format(0, val)
        e.place_queen(0, val, num_of_queens, [])
        print

