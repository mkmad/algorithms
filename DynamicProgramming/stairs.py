# f(n) = f(n-1) + f(n-2) + f(n-3)

cache = {}
def memoize(func):
    def wrapper(*args):
        if args[0] not in cache:
            cache[args[0]] = func(*args)
            return cache[args[0]]
        else:
            return cache[args[0]]
    # Note the way I am calling the wrapper
    # function
    return wrapper

@memoize
def countStairs(n):
    if n == 1:
        return 1
    elif n <= 0:
        return 0
    else:
        return countStairs(n-1) + countStairs(n-2) + countStairs(n-3) + 3

if __name__ == '__main__':
    print countStairs(5)
    print cache.items()