class Staircase(object):
    """
    A child is running up a staircase with n steps
    and can hop either 1 step, 2 steps, or 3 steps
    at a time. Implement a method to count how many
    possible ways the child can run up the stairs


    Note: Initially when I approached this problem
    I assumed that the number of ways you can reach
    the top is:

    (n-1 + n-2 + n-3) + 1

    Because I thought there is 1 more step remaining
    from n-1 or n-2 or n-3

    But, the way you are supposed to look at recursion
    is to find out how many ways can you reach the top?

    n-1 is one of the ways (so is n-2 and n-3) so the
    final recursive formula then becomes:

    no of ways(n) = no of ways(n-1) + no of ways(n-2)...

    Also note: When it comes to recursion, always try to
    use memoization

    """

    def __init__(self):
        self.memo = {}

    def stairs(self, num_of_stairs):
        """
        There are two important base conditions, one
        for num of stairs = 1 and another for <= 0 (as
        we are decrementing the stairs value during recursive
        calls)
        """
        if num_of_stairs in self.memo:
            return self.memo[num_of_stairs]
        elif num_of_stairs <= 0:
            return 0
        elif num_of_stairs == 1:
            return 1
        else:
            self.memo[num_of_stairs] = self.stairs(num_of_stairs - 1) + \
                                       self.stairs(num_of_stairs - 2) + \
                                       self.stairs(num_of_stairs - 3)
            return self.memo[num_of_stairs]


if __name__ == '__main__':
    s = Staircase()
    print s.stairs(5)
