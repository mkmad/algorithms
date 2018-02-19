import math


class Fitbits(object):

    """
    You are given two 32-bit numbers, N and M, and two bit
    positions, i and j. Write a method to insert M into N
    such that M starts at bit j and ends at bit i. You can
    assume that the bits j through i have enough space to
    fit all of M

    Eg:

    N = 10001101000 , M = 10011 ; i = 2, j = 6

    Output: N = 10001001100


    So, you can't simple do an & or an | operation, that
    will not have all the bits of M in N. You need to
    clear all the bits between i and j before you do an
    | operation.

    Note: The positions are 0 indexed, and the rightmost
    bit is position 0 unlike strings and arrays where the
    leftmost position is 0


    """

    def get_mask(self, n, i, j):

        print '\nn: ', n
        print '\nBin of n:'
        print bin(n)[2:]

        # The number of bits is always the ceiling
        # of the log base 2 of the value
        no_of_bits = int(math.ceil(math.log(n, 2)))

        print '\nNo of bits in n'
        print no_of_bits

        print
        print 'j:', j
        print 'i:', i

        # create a mask with all 1's with the length of n.
        # 1 being push no_of_bits times will create
        # 100000.., so I I negate 1 from the value then
        # the remaining will be 11111.... (with the same
        # length as n)
        mask1 = (1 << no_of_bits) - 1

        """
        Now since mask1 is all 1's we need to shift
        it j + 1 times to have all the values before
        j as 1's and after j as 0's
        
        Note: Since python interprets ints as long
        when I shift vals to the left instead of
        overflowing, the values (0's) are appending
        to the right
        
        In [41]: bin(((1 << 11 + 1) - 1) << 7)
        Out[41]: '0b1111111111110000000'
        
        Hence, I need to limit it to the number of
        bits that n had, it can be achieved by using
        a mask with the desired length of all 1's
        
        mask & (((1 << no_of_bits + 1) - 1) << j)
        
        i.e.
        
        In [43]: bin(4095 & (((1 << 12) - 1) << 7))
        Out[43]: '0b111110000000'

        where 4095 == 111111111111
        
        This works because the left part of the 
        leftmost value is technically 0's so if you
        perform & operation all those values in the 
        left of the number will be set to 0

        """
        mask1 = mask1 & (mask1 << j + 1)

        print
        print 'Bin of mask1:'
        print bin(mask1)[2:]

        # Creating another mask, this time we push
        # it i times to the left and negate 1. This
        # will create a mask with all 1's to the right of
        # i
        mask2 = (1 << i) - 1

        print
        print 'Bin of mask2:'
        print bin(mask2)[2:]

        # Now if we do mask1 | mask2 then we get the desired
        # mask of 0's from j to i and 1's to the left of j and
        # right of i

        mask = mask1 | mask2

        print '\nBin of mask'
        print bin(mask)[2:]
        return mask

    def set_m_in_n(self, n, m, i, j):
        mask = self.get_mask(n, i, j)

        # clear the bits from i to j
        n = n & mask

        print
        print 'n after clearing bits'
        print bin(n)[2:]

        # shift m i times to the left
        # This is to get m right in between
        # i and j.
        # Note: The right of m will be 0's
        print
        print 'm before shifting i times:'
        print bin(m)[2:]

        m = m << i

        print
        print 'm after shifting i times'
        print bin(m)[2:]

        # Set m in n
        n = n | m

        print
        print 'n after setting m in positions i to j:'
        print bin(n)[2:]


if __name__ == '__main__':
    f = Fitbits()

    n = int('10111101010', 2)
    m = int('10010', 2)

    i = 2
    j = 6

    f.set_m_in_n(n, m, i, j)
