class NumBits(object):
    """
    Write a function to determine the number
    of bits you would need to flip to convert
    integer A to integer B
    """

    def numBits(self, num1, num2):
        """
        Xor between two numbers tell us which
        bits are different. Hence get the bit
        count of 1

        Note: You can't simply get the number of 1's or 0's
        of both the numbers and say the difference is the
        output

        The questions asks the number of flips required
        hence even if the number of 1's and 0's are the same
        the number of flips might is not 0, so to convert
        one number to another get the xor of both the numbers
        and just get the count of the 1's in the result, coz
        the 1's in the result signify the difference in the
        bit position in both the numbers

        """
        diff = num1 ^ num2
        print 'Number of bits required to ' \
              'change the numbers:', bin(diff).count('1')


if __name__ == '__main__':
    n = NumBits()
    n.numBits(29, 15)

