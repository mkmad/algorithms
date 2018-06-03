import unittest

MAX_INTERSECTIONS = 10000000


class DiscIntersections(object):

    """

    # Problem Description

    We draw N discs on a plane. The discs are numbered from 0 to N - 1. A zero-indexed array A of N non-negative
    integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0)
    and radius A[J].

    We say that the J-th disc and K-th disc intersect if J <> K and the J-th and K-th discs have at least one common
    point (assuming that the discs contain their borders).

    The figure below shows discs drawn for N = 6 and A as follows:

      A[0] = 1
      A[1] = 5
      A[2] = 2
      A[3] = 1
      A[4] = 4
      A[5] = 0
    There are eleven (unordered) pairs of discs that intersect, namely:
            discs 1 and 4 intersect, and both intersect with all the other discs;
            disc 2 also intersects with discs 0 and 3.

    Write a function:
        def solution(A)


    that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of
    intersecting discs. The function should return -1 if the number of intersecting pairs exceeds 10,000,000.
    Given array A shown above, the function should return 11, as explained above.


    Assume that:
            N is an integer within the range [0..100,000];
            each element of array A is an integer within the range [0..2,147,483,647].


    Complexity:
            expected worst-case time complexity is O(N*log(N));
            expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).


    Elements of input arrays can be modified.


    Note:


    We need to know how many discs are open when a disc
    closes.  Thus we can step through all the closing points
    and simply count the number of discs that have opened since
    the last close. So, store the starting point and ending
    points of each disc and iterate through the ending point array(
    meanwhile checking how many discs are open by iterating through
    the starting point array)


    """

    @staticmethod
    def solution(A):
        # write your code in Python 3.6
        starts, ends = [], []
        for point, radius in enumerate(A):
            starts.append(point - radius)
            ends.append(point + radius)

        starts.sort()
        ends.sort()

        # every time a disc closes we add an intersection for every disc that has opened
        # since the last close
        intersections = start = 0
        for end in xrange(len(ends)):  # for every closing
            while start < len(starts) and starts[start] <= ends[end]:  # step through unreconciled openings
                start += 1
            intersections += start - end - 1  # and record them as intersections

            if intersections > MAX_INTERSECTIONS:
                return -1

        return intersections


solution = DiscIntersections().solution


class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([1, 5, 2, 1, 4, 0]), 11)

    def test_simple(self):
        self.assertEqual(solution([1, 1, 1]), 3)  # this is not 5, but 3!

    def test_extreme_small(self):
        self.assertEqual(solution([]), 0)
        self.assertEqual(solution([10]), 0)
        self.assertEqual(solution([1, 1]), 1)

    # def test_extreme_large(self):
    #     A = [10000000] * 100000
    #     self.assertEqual(solution(A), -1)


if __name__ == '__main__':
    unittest.main()
