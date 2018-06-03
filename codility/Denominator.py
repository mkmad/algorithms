# -*- coding: utf-8 -*-


class Denominator(object):

    """
    An array A consisting of N integers is given. The dominator of array A is
    the value that occurs in more than half of the elements of A.

    For example, consider array A such that

     A[0] = 3    A[1] = 4    A[2] =  3
     A[3] = 2    A[4] = 3    A[5] = -1
     A[6] = 3    A[7] = 3
    The dominator of A is 3 because it occurs in 5 out of 8 elements of A
    (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

    Write a function

    def solution(A)

    that, given an array A consisting of N integers, returns index of any
    element of array A in which the dominator of A occurs. The function
    should return −1 if array A does not have a dominator.

    Assume that:

    N is an integer within the range [0..100,000];
    each element of array A is an integer within the range
    [−2,147,483,648..2,147,483,647].
    For example, given array A such that

     A[0] = 3    A[1] = 4    A[2] =  3
     A[3] = 2    A[4] = 3    A[5] = -1
     A[6] = 3    A[7] = 3
    the function may return 0, 2, 4, 6 or 7, as explained above.

    Complexity:

    expected worst-case time complexity is O(N);
    expected worst-case space complexity is O(1) (not counting the
    storage required for input arguments)



    Note:

        This is a perfect example of finding majority of an element in
        a collection, keep incrementing the votes if you find the element
        else decrement the votes if you don't, if the vote becomes 0 then
        the current candidate becomes the majority with 1 vote

        After finding the majority you also need to check if they won more
        than half the seats if they did then return any index of the candidate
        else return -1


    """

    @staticmethod
    def solution(A):
        # write your code in Python 3.6
        candidate = None
        count = 0

        for val in A:
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

        if not count:
            return -1

        count = 0
        candidate_idx = None
        for i, v in enumerate(A):
            if v == candidate:
                if not count:
                    candidate_idx = i
                count += 1

        if count > len(A) / 2:
            return candidate_idx
        else:
            return -1


if __name__ == '__main__':
    d = Denominator()
    print d.solution([3, 4, 3, 2, 3, -1, 3, 3])
