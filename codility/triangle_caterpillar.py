# -*- coding: utf-8 -*-


class TriangleCaterpillar(object):

    """
    An array A consisting of N integers is given. A triplet (P, Q, R) is
    triangular if it is possible to build a triangle with sides of lengths
    A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular
    if 0 ≤ P < Q < R < N and:

    A[P] + A[Q] > A[R],
    A[Q] + A[R] > A[P],
    A[R] + A[P] > A[Q].
    For example, consider array A such that:

      A[0] = 10    A[1] = 2    A[2] = 5
      A[3] = 1     A[4] = 8    A[5] = 12
    There are four triangular triplets that can be constructed from elements
    of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

    Write a function:

    def solution(A)

    that, given an array A consisting of N integers, returns the number of
    triangular triplets in this array.

    For example, given array A such that:

      A[0] = 10    A[1] = 2    A[2] = 5
      A[3] = 1     A[4] = 8    A[5] = 12
    the function should return 4, as explained above.

    Assume that:

    N is an integer within the range [0..1,000];
    each element of array A is an integer within the range [1..1,000,000,000].
    Complexity:

    expected worst-case time complexity is O(N2);
    expected worst-case space complexity is O(N) (not counting the storage
    required for input arguments)

    Note: This problem is same as the 'triangle.py' problem, the only difference
    here is we have to count how many triangles are possible and there we check
    if at least one triangle is possible or not. Hence we use caterpillar method
    here

    """
    @staticmethod
    def solution(A):
        A.sort()
        triangle_cnt = 0

        # Since the array is sorted, we can start q and r
        # as p + 1 and r + 1 (q and r don't have to less than
        # p) Also, note how the caterpillar works (how r and q
        # are incremented)
        for P_idx in xrange(0, len(A) - 2):
            Q_idx = P_idx + 1
            R_idx = P_idx + 2
            while R_idx < len(A):
                if A[P_idx] + A[Q_idx] > A[R_idx]:
                    triangle_cnt += R_idx - Q_idx
                    R_idx += 1
                elif Q_idx < R_idx - 1:
                    Q_idx += 1
                else:
                    R_idx += 1
                    Q_idx += 1

        return triangle_cnt


if __name__ == '__main__':
    t = TriangleCaterpillar()
    print t.solution([10, 2, 5, 1, 8, 12])
