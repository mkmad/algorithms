# -*- coding: utf-8 -*-


class MaxSlice(object):

    """

    A non-empty array A consisting of N integers is given. A pair
    of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice
    of array A. The sum of a slice (P, Q) is the total of
    A[P] + A[P+1] + ... + A[Q].

    Write a function:

    def solution(A)

    that, given an array A consisting of N integers, returns the maximum
    sum of any slice of A.

    For example, given array A such that:

    A[0] = 3  A[1] = 2  A[2] = -6
    A[3] = 4  A[4] = 0
    the function should return 5 because:

    (3, 4) is a slice of A that has sum 4,
    (2, 2) is a slice of A that has sum −6,
    (0, 1) is a slice of A that has sum 5,
    no other slice of A has sum greater than (0, 1).
    Assume that:

    N is an integer within the range [1..1,000,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000];
    the result will be an integer within the range [−2,147,483,648..2,147,483,647].
    Complexity:

    expected worst-case time complexity is O(N);
    expected worst-case space complexity is O(N) (not counting the storage
    required for input arguments)


    Note: This is just like kadane's but here its strictly expected for the new
    value to increase the value of running sum, if it didn't increase the value
    then its not included

    """

    @staticmethod
    def solution(A):
        array_ = A
        sub_array_start = 0
        running_sum = None
        sub_arrays = {}

        for i, val in enumerate(array_):
            if running_sum is None:
                running_sum = val
            else:
                if running_sum + val > running_sum:
                    running_sum += val
                else:
                    sub_arrays[running_sum] = (sub_array_start, i - 1)
                    sub_array_start = i
                    running_sum = val

            if i == len(array_) - 1:
                sub_arrays[running_sum] = (sub_array_start, i)

        return max(sub_arrays.keys())


if __name__ == '__main__':
    m = MaxSlice()
    print m.solution([3, 2, -6, 4, 0])
