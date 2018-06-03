# -*- coding: utf-8 -*-


class MaxProfit(object):

    """
    An array A consisting of N integers is given. It contains daily prices
    of a stock share for a period of N consecutive days. If a single share
    was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the
    profit of such transaction is equal to A[Q] − A[P], provided that
    A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

    For example, consider the following array A consisting of six elements
    such that:

      A[0] = 23171
      A[1] = 21011
      A[2] = 21123
      A[3] = 21366
      A[4] = 21013
      A[5] = 21367
    If a share was bought on day 0 and sold on day 2, a loss of 2048 would
    occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought
    on day 4 and sold on day 5, a profit of 354 would occur because
    A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would
    occur if a share was bought on day 1 and sold on day 5.

    Write a function,

    def solution(A)

    that, given an array A consisting of N integers containing daily prices of a
    stock share for a period of N consecutive days, returns the maximum possible
    profit from one transaction during this period. The function should return 0
    if it was impossible to gain any profit.

    For example, given array A consisting of six elements such that:

      A[0] = 23171
      A[1] = 21011
      A[2] = 21123
      A[3] = 21366
      A[4] = 21013
      A[5] = 21367
    the function should return 356, as explained above.

    Assume that:

    N is an integer within the range [0..400,000];
    each element of array A is an integer within the range [0..200,000].
    Complexity:

    expected worst-case time complexity is O(N);

    expected worst-case space complexity is O(1) (not counting the
    storage required for input arguments).


    Note:

        This is very similar to Kadanes's Algorithm. We iterate through
        the array and check:
            1) If the price drops below the min value (purchased date)
               then change the min value to this price
            2) If the price > min value then check if the profit to be
               made is greater than the previous profit or not.

               If the profit to be made is more, then the price point is
               at its highest (among the iterated values) else the price
               point is not the highest but its greater than the min value

    """
    @staticmethod
    def max_profit(array_):

        if len(array_) < 2:
            return 0

        else:
            min_val = array_[0]
            min_index = 0
            profit = 0
            profit_index = {}
            for i in range(1, len(array_)):
                if array_[i] < min_val:
                    min_val = array_[i]
                    min_index = i
                else:
                    temp = array_[i] - min_val
                    if profit < temp:
                        profit = temp
                        profit_index[profit] = (min_index, i)

            if profit_index:
                return profit_index[max(profit_index.keys())], \
                       max(profit_index.keys())

            else:
                return 0


if __name__ == '__main__':
    m = MaxProfit()
    print m.max_profit([23171, 21011, 21123, 21366, 21013, 21367])
