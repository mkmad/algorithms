class MazeWithPaths(object):

    """
    At any given position, first append the position to
    path and if any of the future paths (top, down, left
    or right) returns a valid path then return true to the
    parent call else remove the position from the path array

    Also, maintain a visited array to check if we have
    visited that position before or not

    """

    def __init__(self):

        # Note, 0 is valid and 1 is not valid
        self.maze = [
            [0, 0, 0, 1],
            [1, 0, 1, 0],
            [1, 0, 0, 0]
        ]
        self.visited = set()

    def is_valid(self, x, y):
        if x < 0 or x > len(self.maze) - 1:
            return False
        elif y < 0 or y > len(self.maze[0]) - 1:
            return False
        elif self.maze[x][y] == 1:
            return False
        elif (x, y) in self.visited:
            return False
        else:
            return True

    def find_path(self, x, y, out_x, out_y, path):
        if self.is_valid(x, y):
            if x == out_x and y == out_y:
                path.append((x, y))
                self.visited.add((x, y))
                return True
            else:
                self.visited.add((x, y))
                path.append((x, y))
                if self.find_path(x, y + 1, out_x, out_y, path) or \
                        self.find_path(x + 1, y, out_x, out_y, path) or \
                        self.find_path(x, y - 1, out_x, out_y, path) or \
                        self.find_path(x - 1, y, out_x, out_y, path):
                    return True
                else:
                    path.pop()
                    return False

    def main(self):
        path = []
        self.find_path(0, 0, 1, 3, path)
        print path


if __name__ == '__main__':
    s = MazeWithPaths()
    s.main()
