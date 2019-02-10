# -*- coding: utf-8 -*-


class MissingInteger(object):

    """
    Given an array A of N integers, returns the smallest
    positive integer (greater than 0) that does not occur in A.

    For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

    Given A = [1, 2, 3], the function should return 4.

    Given A = [−1, −3], the function should return 1.

    Assume that:

    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range
    [−1,000,000..1,000,000].

    Solution:

        Convert the array into a set, this will eliminate all the
        duplicates, then run a for loop from 1 to 1 million (since thats
        the limit). In the for loop just keep adding the number to the set,
        meanwhile keeping track of the previous length and the post adding
        length of the set. If its increased by 1 then we know that this is
        the first missing integer

    """

    @staticmethod
    def solution(A):

        # convert to set
        s = set(A)

        for val in range(1, 1000001):
            prev = len(s)
            s.add(val)
            if len(s) == prev + 1:
                return val

        return 0


if __name__ == '__main__':
    m = MissingInteger()
    print m.solution([1, 3, 6, 4, 1, 2])
    print m.solution([1, 3, 6, 4, 1, 2, 5])
    print m.solution([0, 0, 0, 0, 0, 0])
