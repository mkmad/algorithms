class Triangle(object):

    """

    A zero indexed array A consisting of N integers is given. A
    triplet (P, Q, R) is triangular if 0 <= P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

    For example, consider array A such that:

      A[0] = 10    A[1] = 2    A[2] = 5
      A[3] = 1     A[4] = 8    A[5] = 20

    Triplet (0, 2, 4) is triangular and the function should return 1

    Given array A such that:
      A[0] = 10    A[1] = 50    A[2] = 5
      A[3] = 1

    the function should return 0.


    Note:

    The smart solution you might say is tricky because it capitalizes
    on the not-so-obvious observation that testing the three numbers
    closest together is your best chance of identifying
    a 'triangle'.  Thus providing for a sort (O(log(N) and a single
    pass O(N)) => O(N * log(N))

    eg:
        input: [10, 2, 5, 1, 8, 20]
        sorted: [1, 2, 5, 8, 10, 20]

        tests:
        [1,2,5] = 3 > 5 = 0
        [2,5,8] = 7 > 8 = 0
        [5,8,10] = 13 > 10 = 1!

    eg:
        input: [10, 50, 5, 1]
        sorted: [1, 5, 10, 50]

        tests:
        [1,5,10] = 6 > 10 = 0
        [5,10,50] = 15 > 50 = 0

    """

    @staticmethod
    def solution(A):
        # write your code in Python 3.6
        if 3 <= len(A) <= 100000:

            A.sort()

            for i, v in enumerate(A):
                if i <= len(A) - 3:
                    if A[i] + A[i + 1] > A[i + 2] and \
                            A[i] + A[i + 2] > A[i + 1] and \
                            A[i + 1] + A[i + 2] > A[i]:
                        return 1

            return 0

        else:
            return 0


if __name__ == '__main__':
    t = Triangle()
    print t.solution([10, 2, 5, 1, 8, 20])
    print t.solution([10, 50, 5, 1])

