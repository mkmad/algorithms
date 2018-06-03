class MaxProductThreeWrong(object):

    """
    Here I considered only the top three max values. But
    when it comes to multiplication two big -ve numbers makes
    one big +ve number


    Also note: when I was setting the values for the three indices
    I did not propagate the values properly, you need to check against
    all the max's to see if I can replace and propagate. I checked
    only against the first max and if it was not larger I skipped, I didn't
    consider that the val might be second largest
    """

    @staticmethod
    def solution(A):
        max_1 = None
        max_2 = None
        max_3 = None

        for val in A:
            if max_1 is None:
                max_1 = val
            else:
                if max_1 <= val:
                    max_3 = max_2
                    max_2 = max_1
                    max_1 = val
                else:
                    if max_2 is None:
                        max_2 = val
                    else:
                        if max_2 <= val:
                            max_3 = max_2
                            max_2 = val
                        else:
                            if max_3 is None:
                                max_3 = val
                            else:
                                if max_3 <= val:
                                    max_3 = val
        return max_1 * max_2 * max_3


class MaxProductThree(object):
    """
    The 'trick' with this one is to realise that two negatives make a positive.
    Sorting the array then multiplying the
    three biggest numbers will only get you a score of 44%.

    You have to include a branch in the code to accommodate two big negative numbers
    combining with a positive number to provide a greater product than multiplying
    the positives together.

    eg:
    [-100, -100, -100, 0, 50, 50, 50]
    The product of the top 3 is 125000, but the product of the bottom two
    (-100, 100) with the top one (50) is 500000!

    """

    @staticmethod
    def solution(A):
        if 3 <= len(A) <= 100000:
            A.sort()

            for val in A:
                if not -1000 <= val <= 1000:
                    return
            if A[0] < 0 and A[1] < 0 and A[-1] > 0:
                # excepting that two negatives make a positive...
                return max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])
            else:
                return A[-3] * A[-2] * A[-1]


if __name__ == '__main__':
    m = MaxProductThree()
    print m.solution([10, 10, 10])
    print m.solution([4, 5, 1, 0])
