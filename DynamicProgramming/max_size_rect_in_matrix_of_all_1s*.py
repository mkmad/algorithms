from mycode.dsap.stackNQueue.max_rect_area_histogram import MaxRectAreaHistogram as maxHist


class MaxRectAreaMatrix(object):

    def __init__(self, matrix):
        self.matrix = matrix
        self.stack = None
        self.max_area = -999
        self.result = None

    def copyStack(self, index, horizontal=True):
        if horizontal:
            for col in range(len(self.matrix[0])):
                if self.matrix[index][col] != 0:
                    self.stack[col] += self.matrix[index][col]
                else:
                    self.stack[col] = self.matrix[index][col]
        else:
            for row in range(len(self.matrix), -1, -1):
                self.stack[len(self.matrix) - row] += self.matrix[row][index]

    def check_max_area(self, res):
        if res[0] > self.max_area:
            self.result = res
            self.max_area = res[0]

    def solution(self):
        if len(self.matrix) > len(self.matrix[0]):
            # sweep vertically
            for col in range(len(self.matrix[0])):
                if not self.stack:
                    self.stack = [0 for _ in range(len(self.matrix))]

                self.copyStack(col, horizontal=False)
                m_ = maxHist(self.stack)
                res = m_.solution()
                self.check_max_area(res)

                # remove the None value that's appended in the maxHist class
                self.stack.pop()

        else:
            # sweep horizontally
            for row in range(len(self.matrix)):
                if not self.stack:
                    self.stack = [0 for _ in range(len(self.matrix[0]))]
                self.copyStack(row)
                m_ = maxHist(self.stack)
                res = m_.solution()
                self.check_max_area(res)

                # remove the None value that's appended in the maxHist class
                self.stack.pop()

        print self.result


if __name__ == "__main__":
    matrix = [
        [1, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1]
    ]
    m = MaxRectAreaMatrix(matrix)
    m.solution()
