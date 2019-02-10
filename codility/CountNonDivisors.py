# -*- coding: utf-8 -*-


class CountNonDivisible(object):

    """
    You are given an array A consisting of N integers.

    For each number A[i] such that 0 ≤ i < N, we want to count the number of
    elements of the array that are not the divisors of A[i]. We say that these
    elements are non-divisors.

    For example, consider integer N = 5 and array A such that:

        A[0] = 3
        A[1] = 1
        A[2] = 2
        A[3] = 3
        A[4] = 6
    For the following elements:

    A[0] = 3, the non-divisors are: 2, 6,
    A[1] = 1, the non-divisors are: 3, 2, 3, 6,
    A[2] = 2, the non-divisors are: 3, 3, 6,
    A[3] = 3, the non-divisors are: 2, 6,
    A[4] = 6, there aren't any non-divisors.
    Write a function:

    def solution(A)

    that, given an array A consisting of N integers, returns a sequence of
    integers representing the amount of non-divisors.

    The sequence should be returned as:

    a structure Results (in C), or
    a vector of integers (in C++), or
    a record Results (in Pascal), or
    an array of integers (in any other programming language).
    For example, given:

        A[0] = 3
        A[1] = 1
        A[2] = 2
        A[3] = 3
        A[4] = 6
    the function should return [2, 4, 3, 2, 0], as explained above.

    Assume that:

    N is an integer within the range [1..50,000];
    each element of array A is an integer within the range [1..2 * N].
    Complexity:

    expected worst-case time complexity is O(N*log(N));
    expected worst-case space complexity is O(N) (not counting the storage
    required for input arguments).

    Note: There is a o(n ^ 2) algorithm to check each number against
    evey other number and find out if its a divisor or not.

    Another way to do this is to find the min and max numbers in the array
    and create a divisor list for numbers from min to max. Now iterate
    through the input array and add to all the numbers that the particular
    value is a divisor (this is siev algorithm)

    Now that we have the divisor list we can again iterate through the input
    array and check how many numbers is not the divisors by subtracting the
    len of divisors and the len of input array

    Also note, since there might be duplicates we also need a frequency list
    which we use to subtract from the len of divisor list for the particular
    value

    """
    @staticmethod
    def solution(A):
        # write your code in Python 3.6
        divisors = {}
        frequency = {}
        max_val = max(A)
        min_val = min(A)
        for i in range(min_val, max_val + 1):
            divisors[i] = []

        for i in A:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1

        for val in A:
            start = val * 2
            while start <= max_val:
                divisors[start].append(val)
                start += val

        output = []
        for val in A:
            output.append(len(A) - len(divisors[val]) - frequency[val])

        return output


if __name__ == '__main__':
    c = CountNonDivisible()
    print c.solution([3, 1, 2, 3, 6])
