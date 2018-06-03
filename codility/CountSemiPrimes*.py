# -*- coding: utf-8 -*-


class SemiPrimes(object):

    """
    A prime is a positive integer X that has exactly two distinct divisors:
    1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

    A semiprime is a natural number that is the product of two (not necessarily
    distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15,
     21, 22, 25, 26.

    You are given two non-empty arrays P and Q, each consisting of M integers.
    These arrays represent queries about the number of semiprimes within specified
    ranges.

    Query K requires you to find the number of semiprimes within the range (P[K],
     Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

    For example, consider an integer N = 26 and arrays P, Q such that:

        P[0] = 1    Q[0] = 26
        P[1] = 4    Q[1] = 10
        P[2] = 16   Q[2] = 20
    The number of semiprimes within each of these ranges is as follows:

    (1, 26) is 10,
    (4, 10) is 4,
    (16, 20) is 0.
    Write a function:

    def solution(N, P, Q)

    that, given an integer N and two non-empty arrays P and Q consisting of M
    integers, returns an array consisting of M elements specifying the consecutive
     answers to all the queries.

    For example, given an integer N = 26 and arrays P, Q such that:

        P[0] = 1    Q[0] = 26
        P[1] = 4    Q[1] = 10
        P[2] = 16   Q[2] = 20
    the function should return the values [10, 4, 0], as explained above.

    Assume that:

    N is an integer within the range [1..50,000];
    M is an integer within the range [1..30,000];
    each element of arrays P, Q is an integer within the range [1..N];
    P[i] ≤ Q[i].
    Complexity:

    expected worst-case time complexity is O(N*log(log(N))+M);
    expected worst-case space complexity is O(N+M) (not counting the storage
    required for input arguments).


    Note: The prime numbers from 2 to N can be calculated used siev algorithm
    but to calculate the semiprime in a given range in a good running time
    is a bit tricky, I have n^3 running below..

    """

    @staticmethod
    def siev(num, P, Q):
        # write your code in Python 3.6
        siev = [1] * (num + 1)

        # setting 0 and 1 as non prime
        siev[0] = 0
        siev[1] = 0

        # This algorithm works only if you start
        # from 2 (the first prime number)
        start = 2

        # This var keeps tracks of the number
        # of prime numbers between 2 and num

        for i in range(start, num + 1):
            idx = i * i

            while idx <= num:
                if siev[idx]:
                    siev[idx] = 0
                idx += i

        print(siev)

        output = [0] * len(P)
        for i in range(len(P)):
            seen = []
            for k in range(Q[i]):
                for j in range(Q[i]):
                    if siev[k] and siev[j]:
                        if P[i] <= k * j <= Q[i] and k * j not in seen:
                            seen.append(k * j)
                            output[i] += 1

        print output


if __name__ == '__main__':
    s = SemiPrimes()
    s.siev(26, [1, 4, 16], [26, 10, 20])
