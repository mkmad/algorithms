class SubsetSum(object):

    """
    Find if there exists a subset of numbers from
    a set that adds to a particular number

    So, for each and every number you can either choose it
    and move on or ignore it and move on
    """

    def findSubset(self, numbers, index, sum, target, path=''):

        if sum == target:
            print path.split('_')[:-1]
            return

        if index > len(numbers) - 1:
            return

        else:
            # Choose this number
            self.findSubset(numbers, index + 1, sum + numbers[index], target, path + str(numbers[index]) + '_')
            # Ignore this number
            self.findSubset(numbers, index + 1, sum, target, path)

    def main(self):
        arr = [5, 7, 10, 12, 15, 18, 20]
        target = 35
        self.findSubset(arr, 0, 0, target)


if __name__ == '__main__':
    s = SubsetSum()
    s.main()
