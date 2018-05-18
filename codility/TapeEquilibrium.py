# -*- coding: utf-8 -*-
import math


class TapeEquilibrium(object):

    """

        A non-empty array A consisting of N integers is given.
        Array A represents numbers on a tape.

        Any integer P, such that 0 < P < N, splits this tape into
        two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P],
        A[P + 1], ..., A[N − 1].

        The difference between the two parts is the value of:
        (A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])

        In other words, it is the absolute difference between the sum of
        the first part and the sum of the second part.

        For example, consider array A such that:

          A[0] = 3
          A[1] = 1
          A[2] = 2
          A[3] = 4
          A[4] = 3
        We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7


        Note: Even though this is a simple problem, there are some important
        subtle concepts I have to take care off.

            1. p is running one step ahead so I cannot use for loop here
            2. 0, False and None fail on if condition hence initialize
               a value to None and check ( if val is not None ) because
               in this problem min val was set to 0 and it was failing
               in the if condition inside the while loop


    """

    @staticmethod
    def solution(A):

        if 2 <= len(A) <= 100000:
            tot_sum = 0

            for val in A:
                if -1000 <= val <= 1000:
                    tot_sum += val
                else:
                    return

            running_sum = None
            rem_sum = tot_sum
            min_val = None
            p = 1
            while p < len(A):
                if running_sum is None:
                    running_sum = A[p - 1]
                else:
                    running_sum += A[p - 1]

                rem_sum -= A[p - 1]

                if min_val is None:
                    min_val = math.fabs(running_sum - rem_sum)
                else:
                    temp = math.fabs(running_sum - rem_sum)
                    if temp < min_val:
                        min_val = temp

                p += 1

            if min_val is not None:
                return int(min_val)


if __name__ == '__main__':
    t = TapeEquilibrium()
    print t.solution([3, 1, 2, 4, 3])
    print t.solution([1, 1])
    print t.solution([-1000, 1000])
