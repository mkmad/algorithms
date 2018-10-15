class LIS(object):

    """
    Longest increasing sub-sequence for
    3, 4, -1, 0, 6, 2, 3    is:-

    -1, 0, 2, 3 (increasing order)

    Sol:-

    Maintain two pointers i & j, i goes through
    the length of the array and j keeps iterating
    from 0 to i and finds out if the element in i is
    greater than the element in j, if it is then
    the value in the res array at the j'th position will
    be max(res[i] + 1, res[j])

    The reason for the above formula is consider i pointing
    to 6 in the input array then j will go through 3 and 4
    thereby resulting in res[i] to be 3 and when j points to
    -1 in the input array then we can't blindly add 1 to res[i]
    even though input[i] > input[j]. This is because -1 does not
    contribute to LIS as 4 (previous element) > -1

    """

    def __init__(self, array):
        self.array = array

    def solution(self):

        # initialize the result array, with 1 (the minimum length
        # of longest increasing sub sequence of a single element)
        res = [1 for _ in range(len(self.array))]

        for i in range(1, len(self.array)):
            for j in range(i):
                if self.array[i] > self.array[j]:
                    res[i] = max(res[j] + 1, res[i])

        print "Input array:"
        print self.array
        print "\nLIS array"
        print res


if __name__ == '__main__':
    lis = LIS([3, 4, -1, 0, 6, 2, 3])
    lis.solution()
