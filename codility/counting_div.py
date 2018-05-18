# -*- coding: utf-8 -*-

import math


class CountingDiv(object):
    """

    Given three integers A, B and K, returns the number of integers
    within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

    For example, for A = 6, B = 11 and K = 2, your function should return
    3, because there are three numbers divisible by 2 within the range
    [6..11], namely 6, 8 and 10.

    Assume that:

    A and B are integers within the range [0..2,000,000,000];
    K is an integer within the range [1..2,000,000,000];
    A ≤ B.


    Note:
    Number of integer in the range [1 .. X] that divisible
    by K is X/K. So, within the range [A .. B], the result
    is B/K - (A)/K

    """

    @staticmethod
    def solution(A, B, K):
        if 0 <= A <= 2000000000 and 0 <= B <= 2000000000 and 1 <= K <= 2000000000:
            if A <= B:
                if A > 0 and B > 0:
                    return int(math.ceil(B / K - (A / K)))
                else:
                    if B > 0:
                        return int(math.ceil(B / K)) + 1
                    else:
                        return 1


if __name__ == '__main__':
    c = CountingDiv()
    print c.solution(1, 1, 11)
    print c.solution(10, 10, 5)
    print c.solution(10, 10, 7)
    print c.solution(10, 10, 20)
    print c.solution(0, 13, 2)
