class Multiply(object):
    """
    Recursive Multiply: Write a recursive function to multiply
    two positive integers without using the * operator
    (or / operator). You can use addition, subtraction, and bit
    shifting, but you should minimize the number of those
    operations.

    Concept is for a * b it is same as b + b + b... (a times)
    so you can recursively add b, a times. Also, note you can
    simply call the recursion a / 2 times and later multiply the
    result by 2 (using bit manipulation) and add b if a is odd
    """

    def __init__(self):
        pass

    def multiply_(self, a, b):
        if b == 0 or a == 0:
            return 0
        elif a == 1:
            return b
        else:
            half = a >> 1
            half_product = self.multiply_(half, b)
            if a % 2 == 0:
                # multiply by two
                return half_product << 1
            else:
                # For odd numbers, multiply by two
                # and add b
                return (half_product << 1) + b


if __name__ == '__main__':
    m = Multiply()
    print m.multiply_(12, 10)
    print m.multiply_(1234, 4567)
