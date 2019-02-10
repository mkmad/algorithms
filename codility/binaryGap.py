SEEN_ONE = False
MAX_COUNT = 0


class BinaryGap(object):

    """
    A binary gap within a positive integer N is any maximal sequence
    of consecutive zeros that is surrounded by ones at both ends in
    the binary representation of N.

    For example, number 9 has binary representation 1001 and contains
    a binary gap of length 2. The number 529 has binary representation
    1000010001 and contains two binary gaps: one of length 4 and one of
    length 3. The number 20 has binary representation 10100 and contains
    one binary gap of length 1. The number 15 has binary representation
    1111 and has no binary gaps.


    Write a function:

    def solution(N)

    that, given a positive integer N, returns the length of its longest
    binary gap. The function should return 0 if N doesn't contain a binary
    gap.

    For example, given N = 1041 the function should return 5, because N
    has binary representation 10000010001 and so its longest binary gap
    is of length 5.

    Assume that:

    N is an integer within the range [1..2,147,483,647].


    Complexity:

    expected worst-case time complexity is O(log(N));
    expected worst-case space complexity is O(1).

    """
    # TODO: Note: About the runtime, the below code runs in O(log(N))
    # TODO: Since I am binary shifting everytime, I am dividing the
    # TODO: the number by 2

    def solution(self, N):

        global SEEN_ONE
        global MAX_COUNT

        # write your code in Python 3.6
        if type(N) != int:
            return

        if 1 <= N <= 2147483647:
            self.count_gap(N, 0)

        return MAX_COUNT

    def count_gap(self, number, running_count):

        global SEEN_ONE
        global MAX_COUNT

        # This check is important because 0 >> 1 is 0 and
        # the recursion will not terminate
        if number <= 0:
            return

        # Check if the last bit is 1 or not
        if number & 1:
            if not SEEN_ONE:
                SEEN_ONE = True
            else:
                MAX_COUNT = max(MAX_COUNT, running_count)

            self.count_gap(number >> 1, 0)

        else:
            if SEEN_ONE:
                running_count += 1
                self.count_gap(number >> 1, running_count)
            else:
                self.count_gap(number >> 1, 0)


if __name__ == '__main__':
    b = BinaryGap()
    print b.solution(529)


