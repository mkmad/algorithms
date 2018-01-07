class SelectionSort(object):

    def __init__(self):
        self.values = [3, 2, 6, -8, 4, 9, 1, 7]

    def swap(self, a, b):
        self.values[a], self.values[b] = \
            self.values[b], self.values[a]

    def sort(self):
        """
        run two for loops, for each iteration select
        the index of the minimum value and replace it
        with i.

        """
        print self.values
        for i in range(len(self.values) - 1):
            min_val = i
            for j in range(i+1, len(self.values)):
                if self.values[j] < self.values[min_val]:
                    min_val = j
            self.swap(i, min_val)

        print self.values


if __name__ == '__main__':
    s = SelectionSort()
    s.sort()


