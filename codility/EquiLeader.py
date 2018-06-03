# -*- coding: utf-8 -*-


class EquiLeader(object):

    """
    A non-empty array A consisting of N integers is given.

    The leader of this array is the value that occurs in more than half of
    the elements of A.

    An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences
    A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders
    of the same value.

    For example, given array A such that:

        A[0] = 4
        A[1] = 3
        A[2] = 4
        A[3] = 4
        A[4] = 4
        A[5] = 2

    we can find two equi leaders:

    0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose
    value is 4.
    2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose
    value is 4.

    The goal is to count the number of equi leaders.

    Write a function:

    def solution(A)

    that, given a non-empty array A consisting of N integers, returns the number
    of equi leaders.

    For example, given:

        A[0] = 4
        A[1] = 3
        A[2] = 4
        A[3] = 4
        A[4] = 4
        A[5] = 2
    the function should return 2, as explained above.

    Assume that:

    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range
    [−1,000,000,000..1,000,000,000].

    Complexity:

    expected worst-case time complexity is O(N);
    expected worst-case space complexity is O(N) (not counting the storage
    required for input arguments).

    """
    @staticmethod
    def solution(A):
        # write your code in Python 3.6
        candidate = None
        count = 0
        equi_leaders = 0

        for i, val in enumerate(A):
            if candidate is None:
                candidate = val
                count += 1
            elif val == candidate:
                count += 1
            else:
                count -= 1
                if not count:
                    candidate = val
                    count += 1

        candidate_count = 0
        for val in A:
            if val == candidate:
                candidate_count += 1

        if candidate_count > len(A) / 2:
            left_count = 0
            for i, val in enumerate(A):
                if val == candidate:
                    left_count += 1
                # If the left count is greater than (i + 1) / 2 i.e more
                # than half and right count is (len(A) - 1 - i) i.e. more
                # than right half then the current index must be a equi leader
                # because the majority on both sides is the candidate
                # You can also count majority on both sides when A[i] is
                # not the candidate
                if left_count > (i + 1) // 2 and \
                        (candidate_count - left_count) > (len(A) - 1 - i) // 2:
                    equi_leaders += 1

        return equi_leaders


if __name__ == '__main__':
    e = EquiLeader()
    print e.solution([4, 3, 4, 4, 4, 2])
    print e.solution([4, 4, 2, 5, 3, 4, 4, 4])
