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

    # Method 1
    def place_queen(self, row, column, num_queens, placed):
        # print if row == num_queens, since its zero indexed
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

    # Method 2
    def place_queen_(self, placed, num_queens, row=0):

        if row == num_queens:
            return True

        elif row > num_of_queens:
            return False

        # Here instead of calling the previous iteration with
        # a different column we just iterate through the columns
        # for a given row. This way I don't have to worry about
        # column going overboard
        for pos in range(num_of_queens):
            if self.check_valid(row, pos, placed):
                placed.append((row, pos))
                if self.place_queen_(placed, num_queens, row=row + 1):
                    return True
                else:
                    placed.pop()
                    continue
        return False


if __name__ == '__main__':
    e = EightQueens()
    num_of_queens = 8

    # Use this for loop to start from all possible
    # starting locations

    print '\nMethod 1\n'
    for val in range(num_of_queens):
        e.place_queen(0, val, num_of_queens, [])

    print '\nMethod 2\n'
    placed = []
    e.place_queen_(placed, num_of_queens)
    print placed

