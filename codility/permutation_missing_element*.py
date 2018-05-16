class PermMissingElement(object):

    """
    An array A consisting of N different integers is given.
    The array contains integers in the range [1..(N + 1)],
    which means that exactly one element is missing.

    Your goal is to find that missing element.

    Write a function that, given an array A, returns the value
    of the missing element.

    For example, given array A such that:

      A[0] = 2
      A[1] = 3
      A[2] = 1
      A[3] = 5
    the function should return 4, as it is the missing element.

    Assume that:

    N is an integer within the range [0..100,000];
    the elements of A are all distinct;
    each element of array A is an integer within the range
    [1..(N + 1)].


    Complexity:

    expected worst-case time complexity is O(N)

    expected worst-case space complexity is O(1) (not counting the
    storage required for input arguments).


    Note: I missed a lot of edge cases, (refer to the solution tests)
    eg: empty array, array with one element or an array with no element
    missing (i.e either the first element (1) is missing or the last
    element (N + 1) is missing)

    Also note: The sum of a series that does not start with 1 is:

        sum = length of sum * ( (first number + last number) / 2 )

    Also note: The problem says that the numbers in the array might
               be in the range (1 ... N+1) it doesn't say that it starts
               from 1 and ends in N + 1 all the time
    """

    @staticmethod
    def solution(A):
        # case for empty array
        if not A:
            return 1
        sum = 0
        min_ = min(A)
        max_ = max(A)
        if 0 <= len(A) <= 100000:
            for val in A:
                if 1 <= val <= len(A) + 1:
                    sum += val
                else:
                    return

        # Expected sum for a given series (formula above)
        expected_sum = len(A) * ((min_ + (min_ + len(A) - 1)) / 2)

        # sum will be same as expected sum either if the array
        # has only one element or if the series is not missing
        # any intermediate element rather its  missing the
        # first element or the last element (this is due to the way
        # I calculate the expected sum using the formula ^)
        if sum == expected_sum:
            if len(A) == 1:
                if sum == 1:
                    return 2
                elif sum == 2:
                    return 1
            else:
                if min_ == 1:
                    return max_ + 1
                else:
                    return 1
        # If expected sum is different than the calculated sum
        # then the missing element has been replaced by the last
        # element hence subtract the max from the difference of
        # calculated sum and expected sum
        else:
            return int(max_ - (sum - expected_sum))
