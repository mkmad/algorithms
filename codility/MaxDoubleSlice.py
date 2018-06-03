# -*- coding: utf-8 -*-


class MaxDoubleSlice(object):

    """

    Task description
    A non-empty array A consisting of N integers is given.

    A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

    The sum of double slice (X, Y, Z) is the total of A[X + 1] +
    A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

    For example, array A such that:

        A[0] = 3
        A[1] = 2
        A[2] = 6
        A[3] = -1
        A[4] = 4
        A[5] = 5
        A[6] = -1
        A[7] = 2
    contains the following example double slices:

    double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
    double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
    double slice (3, 4, 5), sum is 0.
    The goal is to find the maximal sum of any double slice.

    Write a function:

    class Solution { public int solution(int[] A); }

    that, given a non-empty array A consisting of N integers, returns
    the maximal sum of any double slice.

    For example, given:

        A[0] = 3
        A[1] = 2
        A[2] = 6
        A[3] = -1
        A[4] = 4
        A[5] = 5
        A[6] = -1
        A[7] = 2
    the function should return 17, because no double slice of array A
    has a sum of greater than 17.

    Assume that:

    N is an integer within the range [3..100,000];
    each element of array A is an integer within the range [−10,000..10,000].
    Complexity:

    expected worst-case time complexity is O(N);
    expected worst-case space complexity is O(N) (not counting the storage
    required for input arguments).

    Note: Pretty straightforward, maintain the sum at any given index by iterating
          from both sides, and then calculate the double sliced sum
    """

    @staticmethod
    def solution(A):
        ending_here = [0] * len(A)
        starting_here = [0] * len(A)

        for idx in xrange(1, len(A)):
            ending_here[idx] = max(ending_here[idx - 1],
                                   ending_here[idx - 1] + A[idx])

        for idx in reversed(xrange(len(A) - 1)):
            starting_here[idx] = max(starting_here[idx + 1],
                                     starting_here[idx + 1] + A[idx])

        max_double_slice = 0

        for idx in xrange(1, len(A) - 1):
            max_double_slice = max(max_double_slice,
                                   starting_here[idx + 1] + ending_here[idx - 1])

        return max_double_slice


if __name__ == '__main__':
    m = MaxDoubleSlice()
    print m.solution([3, 2, 6, -1, 4, 5, -1, 2])
