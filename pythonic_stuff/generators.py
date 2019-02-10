def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'


def permu(xs):
    """
    Returns an iterator (generator) with the help of yield keyword
    """

    if len(xs) <= 1:
        yield xs
    else:
        """
        For each value of i, you select it and append it to each of the
        result of permu(xs[:i] + xs[i + 1])
        
        Also note, that the yield can be nested inside multiple loops
        """
        for i in range(len(xs)):
            for p in permu(xs[:i] + xs[i + 1:]):
                yield [xs[i]] + p


if __name__ == '__main__':
    """
    Creating generators
    
    Note: () are used to create the generators, but they are to used
          using inline for loops (or similar) because if you simply
          declare the values then that becomes a set
          
          eg:
          
                a = (1, 2, 3) is a set
                
                a = (x for x in range(3)) is a generator
    """
    print "\nStand alone Generators"

    nums = (x for x in range(3))

    print "Type of nums is : %s" % type(nums)

    for val in nums:
        print val

    """
    Generator functions
    """

    print "\nDemo of a generator function using for loop"

    for char in my_generator():
        print(char)

    print "\nDemo of the same generator function using iterators"

    a = my_generator()
    print a.next()
    print a.next()
    print a.next()
    # Note: If I call a.next() again it will error out

    """
    Generator functions using yield
    
    Here permu is a generator function that will return new value for
    each iteration
    """
    print "\nGenerator Functions using yield"

    # calling each value using for loop
    for i in permu([4, 5, 6]):
        print i

    # list() will also call each value and store it in a list
    print
    print list(permu([1, 2, 3]))

    # This is same as the above list call
    print
    print [i for i in permu([1, 2, 3])]
