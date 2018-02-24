class FlipBit(object):

    """
    Flip Bit to Win: You have an integer and you can
    flip exactly one bit from a 0 to a 1. Write code
    to find the length of the longest sequence of 1s
    you could create.

    SOLUTION
    EXAMPLE
    Input: 1775 (or: 11011101111) Output: 8
    """

    def find_max_1s(self, num):
        """
        The most efficient way to get the 1's compliment
        is to get a mask (of 1's) and doing an xor with
        num. The mask is obtained by:

        (1 << number of bits in num) - 1


        Note: The ~ operator gives 2's compliment not
              1's compliment

        Also not, the number of bits in a number can be
        obtained either by:

        1) math.ceil(math.log(num, 2))
        2) num.bit_length()

        """

        # If the 1's compliment of the number is 0
        # then it means that the number already has
        # the max number of 1's
        mask = (1 << num.bit_length()) - 1
        if num ^ mask == 0:
            return num.bit_length()

        else:
            """
            The cur max will keep count of all the 1's
            whether I used the allowed 1 bit or not
            
            The pre max however keeps track of all the
            1's just after the allowed bit is used. This
            is helpful when we encounter another 0 down the
            line the cur max is set to prev max + 1 (i.e. we
            now considering the encountered 0 as the position
            for the allowed 1 bit) and the cur max is supposed
            to consider all the 1's before the encountered 0
            
            The max val however, considers all overall max value
            
            The while loop works by shifting bits to the right on
            every iteration
            
            
            It helps if you write the number down and calculate 
            the values
            """
            max_val = 0
            cur_max = 0
            prev_max = 0
            used_the_allowed_bit = False

            while num:

                if num & 1 == 1:
                    cur_max += 1
                    if used_the_allowed_bit:
                        prev_max += 1

                elif num & 1 == 0:

                    if not used_the_allowed_bit:
                        used_the_allowed_bit = True
                        cur_max += 1
                        # Note: The prev_max will start
                        # from the next bit
                    else:
                        if cur_max > max_val:
                            max_val = cur_max

                        if prev_max:
                            cur_max = prev_max + 1
                            prev_max = 0

                num = num >> 1

            if cur_max > max_val:
                return cur_max
            else:
                return max_val


if __name__ == '__main__':
    f = FlipBit()
    res = f.find_max_1s(1775)
    print '\nOutput for 11011101111'
    print res
    res = f.find_max_1s(8059)
    print '\nOutput for 1111101111011'
    print res
