# -*- coding: utf-8 -*-


class EqualNonEqual(object):

    """
    An integer X and a non-empty zero-indexed array A consisting of N
    integers are given. We are interested in which elements of A are equal
    to X and which are different from X. The goal is to split array A into
    two parts, such that the number of elements equal to X in the first part
    is the same as the number of elements different from X in the other part.
    More formally, we are looking for a number K such that:

    0 <= K <= N
    the number of elements equal to X in A[0..K−1] is the same as the number
    of elements different from X in A[K..N−1]. (For K = 0, A[0..K−1] does not
    contain any elements. For K = N, A[K..N−1] does not contain any elements)

    """

    def calculate(self, x, array_):
        positions = {}
        equals = 0
        non_equals = 0
        for i, v in enumerate(array_):
            if v == x:
                equals += 1
            positions[i] = equals

        for i in range(len(array_) - 1, -1, -1):
            if not array_[i] == x:
                non_equals += 1

            if positions[i] == non_equals:
                return i


if __name__ == '__main__':
    e = EqualNonEqual()
    print e.calculate(5, [5, 5, 1, 7, 2, 3, 5])
