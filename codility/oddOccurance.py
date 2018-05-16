class OddOccurance(object):

    """
    A non-empty array A consisting of N integers is given.
    The array contains an odd number of elements, and each
    element of the array can be paired with another element
    that has the same value, except for one element that
    is left unpaired.


    For example, given array A such that:

    A[0] = 9  A[1] = 3  A[2] = 9
    A[3] = 3  A[4] = 9  A[5] = 7
    A[6] = 9

    the function should return 7

    Note: If you xor two identical values, then the result
          will be 0. Also if a ^ b = c then c ^ a = b or
          c ^ b = a

          eg:

          In [1]: 427 ^ 533
          Out[1]: 958

          In [2]: 958 ^ 533
          Out[2]: 427

    """

    @staticmethod
    def solution(A):
        # write your code in Python 3.6
        if 1 <= len(A) <= 1000000:
            res = 0
            for val in A:
                if 1 <= val <= 1000000000:
                    res ^= val
                else:
                    return

            return res


if __name__ == '__main__':
    array_ = [9, 3, 3, 9, 7, 4, 4]
    o = OddOccurance()
    print
    print o.solution(array_)
