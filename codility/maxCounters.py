# -*- coding: utf-8 -*-


class MaxCounters(object):

    """

    You are given N counters, initially set to 0, and you have two
    possible operations on them:

    1) increase(X) − counter X is increased by 1
    2) max counter − all counters are set to the maximum value of any
    counter.

    A non-empty array A of M integers is given. This array represents
     consecutive operations:

    if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
    if A[K] = N + 1 then operation K is max counter.


    For example, given integer N = 5 and array A such that:

        A[0] = 3
        A[1] = 4
        A[2] = 4
        A[3] = 6
        A[4] = 1
        A[5] = 4
        A[6] = 4


    the values of the counters after each consecutive operation will be:

        (0, 0, 1, 0, 0)
        (0, 0, 1, 1, 0)
        (0, 0, 1, 2, 0)
        (2, 2, 2, 2, 2)
        (3, 2, 2, 2, 2)
        (3, 2, 2, 3, 2)
        (3, 2, 2, 4, 2)


    The goal is to calculate the value of every counter after all operations.



    Note: The below solution works fine but the worst case running
    time is o(N * M) eg if N = 5 and a = [6, 6, 6, 6..] then the inner
    for loop gets executed almost every time

    def solution(N, A):
        if 1 <= N <= 100000 and 1 <= len(A) <= 100000:
            counters = [0] * (N + 1)
            max_ = 0
            for val in A:
                if 1 <= val <= N + 1:
                    if val == N + 1:
                        for i in range(len(counters)):
                            counters[i] = max_
                    else:
                        counters[val] += 1
                        if counters[val] > max_:
                            max_ = counters[val]

            return counters[1:]

    Hence to eliminate the inner for loop I can maintain another variable
    called min_val that gets set to the current max when val = N + 1.
    Now when I increment the counter I check if the value is at least the
    min_val if not I first set it to that and then increment the counter
    for that position

    Note: I must also run through the counter array to see if all the values
    are set to at least the min_value or higher

    """

    @staticmethod
    def solution(N, A):
        min_val = 0
        if 1 <= N <= 100000 and 1 <= len(A) <= 100000:
            counters = [0] * (N + 1)
            max_ = 0
            for val in A:
                if 1 <= val <= N + 1:
                    if val == N + 1:
                        # set the min val
                        min_val = max_
                    else:
                        if counters[val] < min_val:
                            counters[val] = min_val
                        counters[val] += 1
                        if counters[val] > max_:
                            max_ = counters[val]

            # check if all the values are set to at least
            # min_value or higher

            for i, val in enumerate(counters):
                if val < min_val:
                    counters[i] = min_val

            return counters[1:]
