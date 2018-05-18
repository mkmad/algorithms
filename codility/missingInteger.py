# -*- coding: utf-8 -*-


class MissingInteger(object):

    """
    Given an array A of N integers, returns the smallest
    positive integer (greater than 0) that does not occur in A.

    For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

    Given A = [1, 2, 3], the function should return 4.

    Given A = [−1, −3], the function should return 1.

    Assume that:

    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range
    [−1,000,000..1,000,000].


    Note: The solution below works but the running time is more than
          o(n) because for each iteration I am checking if val is in nums
          that itself is a o(n) operation therefore the overall running
          time is o(n^2)

        def solution(A):

            nums = []
            if 1 <= len(A) <= 100000:
                for val in A:
                    if -1000000 <= val <= 1000000:
                        if val not in nums:
                            nums.append(val)

                for val in range(1, 1000000):
                    if val not in nums:
                        return val


    Hence I use the bit vector approach to solve this.
    Note: I need to consider two offsets:
        1) zero indexed
        2) the solution could be in N + 1 position

    """

    @staticmethod
    def solution(A):

        if 1 <= len(A) <= 100000:
            max_ = max(A)
            if max_ > 0:
                nums = [0] * (max_ + 2)
            else:
                return 1

            for val in A:
                if 0 < val <= 1000000:
                    if not nums[val]:
                        nums[val] = 1

            for i, val in enumerate(nums):
                if i > 0:
                    if not val:
                        return i


if __name__ == '__main__':
    m = MissingInteger()
    print m.solution([1, 3, 6, 4, 1, 2])
