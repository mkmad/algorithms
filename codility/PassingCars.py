# -*- coding: utf-8 -*-


class PassingCars(object):

    """
    A non-empty array A consisting of N integers is given.
    The consecutive elements of array A represent consecutive
    cars on a road.

    Array A contains only 0s and/or 1s:

    0 represents a car traveling east,
    1 represents a car traveling west.
    The goal is to count passing cars. We say that a pair of cars (P, Q),
    where 0 ≤ P < Q < N, is passing when P is traveling to the east and
    Q is traveling to the west.

    For example, consider array A such that:

      A[0] = 0
      A[1] = 1
      A[2] = 0
      A[3] = 1
      A[4] = 1

    We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).



    So given a non-empty array A of N integers, return the number of pairs
    of passing cars.

    The function should return −1 if the number of pairs of passing cars
    exceeds 1,000,000,000.


    Note: Initially when I coded the problem I had a dict that stored the
          positions of 0's that are before a given 1. So, after the while
          loop I iterated the dict to calculate the total num. Even though
          that seemed like an o(n) algorithm the solution was timing out.
          Hence be careful when you store such numbers. Even if the
          for / while loop is outside the main loop it still adds up to the
          total time

    """

    @staticmethod
    def solution(A):

        if 1 <= len(A) <= 100000:
            cur = []
            i = 0
            num = 0

            while i < len(A):
                if A[i] in (0, 1):
                    if A[i]:
                        num += len(cur)
                    else:
                        cur.append(i)

                    i += 1
                else:
                    return -1

            if num <= 1000000000:
                return num
            else:
                return -1
        else:
            return -1


if __name__ == '__main__':
    p = PassingCars()
    print p.solution([0, 1, 0, 1, 1])
