visited = []
minpath = 999


def minimumDistance(numRows, numColumns, area):
    # WRITE YOUR CODE HERE
    if 1 <= numRows <= 1000 and 1 <= numColumns <= 1000:
        t = traversal()
        t.traverse(0, 0, numRows, numColumns, area, visited, minpath, path="(0, 0) ")
        return t.minpath


class traversal(object):
    def __init__(self):
        self.minpath = 999

    def traverse(self, row, col, numRows, numColumns, area, visited_, minpath, path=""):
        # edge cases
        if numRows < 0 or numColumns < 0 or row < 0 or col < 0:
            return

        if row > numRows - 1 or col > numColumns - 1:
            return

        if not area:
            return

        # check numRows and numColumns
        if numRows != len(area) or numColumns != len(area[0]):
            return

        if (row, col) not in visited_:

            # if target is found
            if area[row][col] == 9:
                t_path = path.split()
                if len(t_path) < minpath:
                    self.minpath = len(t_path)
                return True

            visited_.append((row, col))

            self.traverse(row - 1, col, numRows, numColumns, area, visited_, self.minpath,
                          path=path + "({0},{1})".format(row - 1, col))
            self.traverse(row + 1, col, numRows, numColumns, area, visited_, self.minpath,
                          path=path + "({0},{1})".format(row + 1, col))
            self.traverse(row, col - 1, numRows, numColumns, area, visited_, self.minpath,
                          path=path + "({0},{1})".format(row, col - 1))
            self.traverse(row, col + 1, numRows, numColumns, area, visited_, self.minpath,
                          path=path + "({0},{1})".format(row, col + 1))


if __name__ == '__main__':
    print minimumDistance(3, 3, [
        [1, 0, 0],
        [1, 0, 0],
        [1, 9, 1]
    ])
