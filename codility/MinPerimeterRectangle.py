class MinPerimeterRectangle():

    """
    An integer N is given, representing the area of some rectangle.

    The area of a rectangle whose sides are of length A and B is A * B,
    and the perimeter is 2 * (A + B).

    The goal is to find the minimal perimeter of any rectangle whose area
    equals N. The sides of this rectangle should be only integers.

    For example, given integer N = 30, rectangles of area 30 are:

    (1, 30), with a perimeter of 62,
    (2, 15), with a perimeter of 34,
    (3, 10), with a perimeter of 26,
    (5, 6), with a perimeter of 22.
    Write a function:

    def solution(N)

    that, given an integer N, returns the minimal perimeter of any rectangle
    whose area is exactly equal to N.

    For example, given an integer N = 30, the function should return 22, as
    explained above.

    Assume that:

    N is an integer within the range [1..1,000,000,000].
    Complexity:

    expected worst-case time complexity is O(sqrt(N));
    expected worst-case space complexity is O(1).


    Note: This uses the num of factors concept to find the
    symmetric divisors and calculate the min perimeter

    min perimeter will be 2 * (i + (N / i)) or 2 * (i + i)
    """

    @staticmethod
    def solution(N):

        if 1 <= N <= 1000000000:
            if N == 1:
                return 2 * (N + N)
            i = 1
            min_ = None
            while i * i <= N:
                if N % i == 0:
                    if i * i < N:
                        if min_ is None:
                            min_ = i + (N / i)
                        elif i + (N / i) < min_:
                            min_ = i + (N / i)
                    elif i * i == N:
                        if i + i < min_:
                            min_ = i + i
                i += 1
            return int(2 * min_)


if __name__ == '__main__':
    m = MinPerimeterRectangle()
    print m.solution(36)
