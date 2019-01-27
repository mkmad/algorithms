class CoinDenominations(object):

    """

    NOTE: This is a MEMOIZATION problem


    Coins: Given an infinite number of quarters
    (25 cents), dimes (10 cents), nickels (5 cents),
    and pennies (1 cent), write code to calculate the
    number of ways of representing n cents

    Note: This is particularly interesting when we are
    trying to memoize the recursive calls. I know that
    for a given sum I try to calculate all possible paths
    that may lead to the target sum, so I needed to figure
    out a way to store all the paths that comes after a
    particular sum (since there might be different paths
    that lead upto this sum). So in L48 I store all the paths
    that come after the current path to the current sum. This
    way, in case I encounter this sum again, I can simply append
    the path (which will be different) that lead to the sum with
       <------------------------------>
    all the precomputed paths for the sum


    Note: See how different this is than the maze storing path
          problem, there I add the path and then remove the path
          if the recursion did not end with success. Here on the
          other hand, I add the path to the denominations array
          immediately if the recursion ends successfully.

    Also note, while the denomination array is populated when the
               recursion terminated the memoization array is
               populated when the recursion returns successfully
    """

    def __init__(self):
        self.possibilities = [25, 10, 5, 1]
        self.denominations = []
        self.memo = {}

    def coins(self, path='', sum_=0, target=0):
        if sum_ in self.memo:
            for val in self.memo[sum_]:
                self.denominations.append(path+val)
        elif sum_ == target:
            self.denominations.append(path[:-2])
            return path
        elif sum_ < target:
            # Calculating paths for the current sum_

            # Also note: Ypu run through all the possibilities
            # at each branch
            for val in self.possibilities:
                # select the current val and check if the recursion returns
                # a result
                res = self.coins(path=path+str(val)+'->', sum_=sum_+val, target=target)
                # Store the path values (if its not None) to the sum_ key
                if res:
                    if sum_ in self.memo:
                        self.memo[sum_].append(res[len(path):])
                    else:
                        self.memo[sum_] = [res[len(path):]]
        else:
            return


if __name__ == '__main__':
    cd = CoinDenominations()
    cd.coins(target=25)
    print cd.denominations
