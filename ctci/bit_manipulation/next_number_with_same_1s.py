class NextNumber(object):
    """
    Next Number: Given a positive integer, print the n
    ext smallest and the next largest number that
    have the same number of 1 bits in their binary
    representation
    """

    def get_next_number(self, num):
        """
        Note: The adjacent numbers or the every second
        number (left and right) might not always have the
        same number of 1 bits

        eg: If I am to check for 7

            In [105]: bin(5).count('1')
            Out[105]: 2

            In [106]: bin(6).count('1')
            Out[106]: 2

            In [107]: bin(7).count('1')
            Out[107]: 3

            In [108]: bin(8).count('1')
            Out[108]: 1

            In [109]: bin(9).count('1')
            Out[109]: 2

        """

        print '\nBinary representation of:', num
        print bin(num)[2:]

        big = self.get_big_number(num)
        small = self.get_small_number(num)

        if big:
            print '\nBiggest neighbour of:', bin(num)
            print bin(big)

        if small:
            print '\nSmallest neighbour of:', bin(num)
            print bin(small)

    def find_position(self, num, bit=0):
        """
        Depending on the bit value, find the
        the location of 0 that has at least
        one 1 bit to its right or find a 1 that
        has at least one 0 bit to its right
        """
        if bit == 0:
            one_count = 0
            position = 0
            while num:
                position += 1
                if num & 1:
                    one_count += 1
                else:
                    if one_count:
                        break
                num >>= 1

            if num:
                return position, one_count
            else:
                return None, None

        else:
            zero_count = 0
            position = 0
            while num:
                position += 1
                if not num & 1:
                    zero_count += 1
                else:
                    if zero_count:
                        break
                num >>= 1

            if num:
                return position, zero_count
            else:
                return None, None

    def get_big_number(self, num):
        """
        Find the first 0 (from right to left) that
        has 1's to its right so that  you can swap
        the 0 and 1

        Now you have to make the right portion of the
        swapped 1 as small as possible so that the
        resulting number is the smallest of all the
        numbers that are greater than the given num
        (with the same number of 1's and 0's)

        Note: You could argue that we can swap the
        first 0 and the first 1 to its right and be
        done with it, however the result is not the
        smallest of the all the big numbers with
        same 1's and 0's
        """

        temp = num
        position, one_count = self.find_position(temp, bit=0)
        if position:
            # change the 0 bit to 1
            mask = 1 << position - 1
            temp |= mask

            # clear all the bits to the right of the bit
            # you just set
            mask = (1 << (temp.bit_length())) - 1
            mask = mask & (mask << position - 1)
            temp &= mask

            # push all the one's (that were on the right side
            # of the bit which we just set) to the right as
            # much as possible. This will ensure that the rightmost
            # part to the bit we set las the lowest value possible
            mask = (1 << one_count - 1) - 1
            temp |= mask

            return temp

    def get_small_number(self, num):
        """
        Find the first 1 (from right to left) that
        has 0's to its right so that  you can swap
        the 1 and 0

        Now you have to make the right portion of the
        swapped 0 as big as possible so that the
        resulting number is the biggest of all the
        numbers that are smaller than the given num
        (with the same number of 1's and 0's)

        Note: You could argue that we can swap the
        first 1 and the first 0 to its right and be
        done with it, however the result is not the
        biggest of the all the small numbers with
        same 1's and 0's
        """

        temp = num

        position, zero_count = self.find_position(temp, bit=1)
        if position:
            # unset the 1 bit that has at least one 0 to its
            # right
            mask = (1 << (temp.bit_length())) - 1
            mask2 = 1 << position - 1

            # The xor will unset the bit since mask2 will
            # have 1 bit in the given location and 0's every
            # where else
            mask = mask ^ mask2
            temp &= mask

            # Pull all the 1's to the right of the location
            # to the left, to make the right side of the bit
            # bigger
            ones = position - zero_count + 1
            mask = (1 << ones) - 1
            temp |= mask

            return temp


if __name__ == '__main__':
    n = NextNumber()
    n.get_next_number(13948)
