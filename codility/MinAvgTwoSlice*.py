class MinAvgTwoSlice(object):

    """
    # Problem Description

    A non-empty zero-indexed array A consisting of N integers is given. A pair of integers (P, Q),
    such that 0 <= P < Q < N, is called a slice of array A (notice that the slice contains at least
    two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided
    by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q - P + 1).

    For example, array A such that:
        A[0] = 4
        A[1] = 2
        A[2] = 2
        A[3] = 5
        A[4] = 1
        A[5] = 5
        A[6] = 8

    contains the following example slices:
            slice (1, 2), whose average is (2 + 2) / 2 = 2;
            slice (3, 4), whose average is (5 + 1) / 2 = 3;
            slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

    The goal is to find the starting position of a slice whose average is minimal.


    Write a function:

        def solution(A)

    that, given a non-empty zero-indexed array A consisting of N integers, returns the starting
    position of the slice with the minimal average. If there is more than one slice with a minimal
    average, you should return the smallest starting position of such a slice.
    For example, given array A such that:

        A[0] = 4
        A[1] = 2
        A[2] = 2
        A[3] = 5
        A[4] = 1
        A[5] = 5
        A[6] = 8
    the function should return 1, as explained above.
    Assume that:
            N is an integer within the range [2..100,000];
            each element of array A is an integer within the range [-10,000..10,000].
    Complexity:
            expected worst-case time complexity is O(N);
            expected worst-case space complexity is O(N), beyond input storage (not counting the
              storage required for input arguments).
    Elements of input arrays can be modified.

    This problem doesn't even need prefix-sums, so that was a big red-herring. Well mostly.
     The 'trick' is not in the coding at all, but in a realisation about the nature of the problem...
     You're looking for the smallest average of a series of numbers.  At first it looks like you
     have to permute over an ever increasing collection of averages of various lengths.
     But, at some point, you'll realize that a small number will always pull the average down,
     no matter what numbers are around it.

     Thus, since it takes at least two numbers to make an average, you may be only looking for a pair
     of numbers which combine to provide the smallest total.
     To verify this presumption, consider the slope that graphing the moving average
     of the pair would make. Irrespective of the width of the average, the gradient will always tilt
     down, however slightly, when you come across a small number.

     So coding a two-point average is dead simple: just walk through the sequence from left to right adding each pair
     together and tracking the position of the smallest pair.

     I couldn't believe it would be this easy, but couldn't resist, and gave it a run... just 50%.

     After a run, the report tells you which tests failed and I couldn't help but glimpse it failed
     all the tests that had something about the number 3 in them.  That was perplexing because I
     was actually having trouble dreaming up a 3-point average which the 2-point didn't detect.
     So I googled it.


     The explanation is that sequences have an odd, or even, number of integers. So take 3-points:
     For example: [-8, -6, -10]
     In this sequence the two-point averages are -7 and -8, so the answer would be index point 1 (the -6).
     But note that the three point average is also -8, and commences one point earlier, on index point 0.
     So the correct answer is actually 0.


     So we're back questioning whether issue will replay for sequences of length 4, 5, 6 and beyond? Will it?

     Ok, let's consider a sequence of 4 values. [1,2,2,1]. It has three two-point averages. [1,2],[2,2],[2,1].
     Which evaluate to [1.5, 2, 1.5], offering 0 as the answer.  Meanwhile the four-point average is also 1.5. Hmm.
     How about [1,-1, 1,-1]?  The two-point averages are [0,0,0] and the four-point average is also [0].
     You can play this out all day, only to find that the four, six, eight etc point averages will never be
     less than one of the two-point averages within it.

     Ok, so if two is enough, why do we need the three point average?
     Consider [1, -1, 1, -1]? The two-point averages all come to 0.  And we've already established that
     a four-point average (of 0) can never best the two-point averages.
     But the three-point averages are 0.33 and -0.33.
     So the correct answer is index point 1.

     And a 5-point sequence? Ok, take [-1, 1, -1, 1, -1]:
     Two points = [0, 0, 0, 0] (best answer is 0)
     Three points = [-0.33, 0.33, -0.33] (better answer is 1)
     Four points = [0, 0] (just like the two points)
     Five points = [-0.33] (same as three points answer).

     Basically the two and three-point averages act like the factors/subcomponents of all the
     longer length averages.  They may be able to match one or other, but will never beat them.
     Thus we can confidently write some trivial code to do a single pass solution which considers only
     the two and three-point averages, but has all averages of longer length sequences covered.

    """

    @staticmethod
    def solution(A):
        # write your code in Python 3.6
        low_avg = None
        low_avg_idx = None

        if 2 <= len(A) <= 100000:
            for i, v in enumerate(A):
                if -10000 <= v <= 10000:
                    if i >= 1:
                        avg_ = (A[i] + A[i - 1]) / 2
                        if low_avg is None:
                            low_avg = avg_
                            low_avg_idx = i - 1
                        elif low_avg > avg_:
                            low_avg = avg_
                            low_avg_idx = i - 1

                    if i >= 2:
                        avg_ = (A[i] + A[i - 1] + A[i - 2]) / 3
                        if low_avg is None:
                            low_avg = avg_
                            low_avg_idx = i - 2

                        elif low_avg > avg_:
                            low_avg = avg_
                            low_avg_idx = i - 2

        if low_avg is not None:
            return low_avg_idx


if __name__ == '__main__':
    m = MinAvgTwoSlice()
    print m.solution([4, 2, 2, 5, 1, 5, 8])
