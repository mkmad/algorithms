class strore_recurssion_path(object):
    def __init__(self):
        self.maze = [
            [0, 0, 0, 0],
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

    def find_path(self, x, y, out_x, out_y, path=[]):
        if self.is_valid(x, y):
            if x == out_x and y == out_y:
                path.append((x, y))
                self.visited.add((x, y))
                print path
            else:
                path.append((x, y))
                self.visited.add((x, y))
                self.find_path(x, y + 1, out_x, out_y, path)
                self.find_path(x + 1, y, out_x, out_y, path)
                self.find_path(x, y - 1, out_x, out_y, path)
                self.find_path(x - 1, y, out_x, out_y, path)
        else:
            return []

    def main(self):
        print self.find_path(0, 0, 1, 3, [])


if __name__ == '__main__':
    s = strore_recurssion_path()
    s.main()

'''
Couple of things, since recursion is a top down traversal try not to send values
up the recursion chain/ parent call, specially when there are 4 calls in function.

When, you encounter the end condition you can print the collected path.
Also, store the end vertex also in the visited set else the recursion just continues
further. Because apart from the obvious base conditions, visited set is the one that
terminates the recursion.

The length of the path completely depends on the the order in which you traverse.
here r,d,u,l gives the best result.

'''




