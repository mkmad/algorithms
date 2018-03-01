class Maze(object):

    def __init__(self, maze):
        self.maze = maze
        self.stack = []
        self.visited = []

    @property
    def row_max(self):
        return len(self.maze) - 1

    @property
    def column_max(self):
        return len(self.maze[0]) - 1

    def find_path(self, target, row=0, column=0):
        """
        Two important things to note, 1) maintain a visited
        list and 2) I need a stack not a queue because the
        very last value to be inserted is the initial starting
        point (0, 0) and while printing it needs to be LIFO
        """
        if 0 <= row <= self.row_max and 0 <= column <= self.column_max:
            if (row, column) not in self.visited and self.maze[row][column]:
                self.visited.append((row, column))
                if (row, column) == target:
                    self.stack.append((row, column))
                    return True
                else:
                    if self.find_path(target, row, column + 1):
                        self.stack.append((row, column))
                        return True
                    elif self.find_path(target, row + 1, column):
                        self.stack.append((row, column))
                        return True
            else:
                return False
        else:
            return False

    def print_path(self):
        while self.stack:
            print self.stack.pop(),


if __name__ == '__main__':
    maze = [
        [1,  1,  1,  0],
        [0,  0,  1,  1],
        [1,  1,  0,  1],
    ]
    m = Maze(maze)
    m.find_path((2, 3))
    m.print_path()
