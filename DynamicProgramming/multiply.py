# Split the array into 2 halves and compute the number of cells
# in both the sides

cache = {}

class mul():

    def __init__(self, array):
        self.array = array

    def multiply(self, row, column):

        if row in cache:
            return cache[row]

        if row == 1:
            cache[row] = column
            return cache[row]

        if row % 2 == 0:
            # Simply double it when row is divisible by 2
            res = self.multiply(row >> 1, column)
            cache[row] = res + res
            return cache[row]

        else:
            # Else compute the half and add one column to it
            temp = row >> 1
            res1 = self.multiply(temp, column)
            # The extra column
            res2 = res1 + column
            cache[row] = res1 + res2
            return cache[row]

    def main(self):
        row = len(self.array)
        column = len(self.array[0])
        print self.multiply(row, column)
        print cache

if __name__ == '__main__':
    array = [[0,0,0,0,0],[0,0,0,0,0]]
    m = mul(array)
    m.main()
