# -*- coding: utf-8 -*-


class ChocolatesByNumbers(object):

    """
    Two positive integers N and M are given. Integer N represents the number
    of chocolates arranged in a circle, numbered from 0 to N − 1.

    You start to eat the chocolates. After eating a chocolate you leave only
    a wrapper.

    You begin with eating chocolate number 0. Then you omit the next M − 1
    chocolates or wrappers on the circle, and eat the following one.

    More precisely, if you ate chocolate number X, then you will next eat the
    chocolate with number (X + M) modulo N (remainder of division).

    You stop eating when you encounter an empty wrapper.

    For example, given integers N = 10 and M = 4. You will eat the following
    chocolates: 0, 4, 8, 2, 6.

    The goal is to count the number of chocolates that you will eat, following
    the above rules.

    Write a function:

    def solution(N, M)

    that, given two positive integers N and M, returns the number of chocolates
    that you will eat.

    For example, given integers N = 10 and M = 4. the function should return 5,
    as explained above.

    Assume that:

    N and M are integers within the range [1..1,000,000,000].
    Complexity:

    expected worst-case time complexity is O(log(N+M));
    expected worst-case space complexity is O(log(N+M)).

    Note: The naive solution times out for very large numbers. A much cleverer
    solution is if you think of M and N expanding linearly (instead of circular)
    they both will eventually meet at LCM of M & N. So to find out how many
    chocolates you ate (i.e the number of times M appeared) divide the result of
    LCM by M
    """

    @staticmethod
    def naive_solution(N, M):
        # write your code in Python 3.6
        chocolates = [1] * N
        count = 0
        initial = 0
        while chocolates[initial]:
            chocolates[initial] = 0
            count += 1
            initial = (initial + M) % N

        return count

    def gcd(self, p, q):
        if q == 0:
            return p
        return self.gcd(q, p % q)

    def lcm(self, p, q):
        return p * (q / self.gcd(p, q))

    def solution(self, N, M):
        return self.lcm(N, M) / M


if __name__ == '__main__':
    c = ChocolatesByNumbers()
    print c.solution(10, 4)
