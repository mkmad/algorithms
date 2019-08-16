denominations = [25, 10, 5, 1]
paths = {}


def coins(target, path, running_sum, idx):

    """

    Coins: Given an infinite number of quarters
    (25 cents), dimes (10 cents), nickels (5 cents),
    and pennies (1 cent), write code to calculate the
    number of ways of representing n cents.

    watch this: https://www.youtube.com/watch?v=k4y5Pr0YVhg

    The other solution is wrong

    Note: The most important insight is, during recursion; you don't
    have to iterate through all the available denomination again and
    again. This will lead to duplicate paths eg 1_2_1, 1_1_2 and 2_1_1.


    """

    if running_sum == target:
        if running_sum in paths:
            paths[running_sum].append(path)
        else:
            paths[running_sum] = [path]
        return path

    elif running_sum < target:
        for coin in range(idx, len(denominations)):
            res = coins(target, str(coin) + '_' + path, running_sum + denominations[coin], coin)
            if res:
                if running_sum in paths:
                    paths[running_sum].append(path)
                else:
                    paths[running_sum] = [path]


if __name__ == '__main__':
    target = 25
    coins(target, '', 0, 0)
    print len(paths[25])
