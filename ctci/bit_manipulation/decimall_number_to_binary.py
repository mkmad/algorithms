class RealtoBinary(object):

    def convert_decimal_to_binary(self, num):
        """
        If the number has natural numbers (left of .)
        convert that into binary first and then send the
        converted string along with the fractional numbers
        to decimal_to_binary

        If there are no natural numbers to begin with, then
        just call decimal_to_binary with '0.' as binary
        string

        Note: To get the natural numbers from the decimal
              use floor division // and to get the decimal
              numbers use %

              eg:

                a = 1.23

                a // 1 = 1.0
                a % 1 = 0.23

        """
        print 'Decimal to convert:', num
        if num > 1:
            # convert to int since bin() takes only int
            b_string = bin(int(num // 1))[2:]
            b_string += '.'
            return self.decimal_to_binary(num % 1, b_string)

        else:
            return self.decimal_to_binary(num, '0.')

    def decimal_to_binary(self, num, b_string):
        """
        The concept is simple, for any given decimal
        number multiple it by 2 (since this is binary
        conversion) then if the result has natural numbers
        add the binary of the natural number to the binary
        string and call this function recursively on the decimal
        part

        If there are no natural numbers then call this function
        again with the resulting decimal number

        The recursion will stop either if the binary string is
        of length 32 (representing a 32 bit binary number) or
        if the result from multiplying with 2 yields 0's in the
        decimal number
        """
        if num and len(b_string) < 32:
            num *= 2
            if num >= 1:
                b_string += bin(int(num // 1))[2:]
                return self.decimal_to_binary(num % 1, b_string)
            else:
                return self.decimal_to_binary(num, b_string + '0')
        else:
            return b_string

    def get_value(self, num, natural=True):
        """
        To get the decimal you need to multiply
        either with 2^i or 1 / 2^i depending on whether
        its a natural number or a decimal number.


        eg:
               1    1    0    1  .    1     1      0      1
              2^3  2^2  2^1  2^0    1/2^1 1/2^2  1/2^3  1/2^4

              Note: The power starts with 0 for natural and 1
                    for decimal numbers
        """
        sum = 0
        if natural:
            cnt = len(num) - 1
            for val in num:
                sum += int(val) * (2**cnt)
                cnt -= 1
            return sum
        else:
            cnt = 1
            for val in num:
                # Note, you need float in the denominator
                # else you will get 0
                # eg:
                # 1 / 2 = 0 and 1 / float(2) = 0.5
                sum += int(val) * (1 / float(2**cnt))
                cnt += 1
            return sum

    def binary_to_decimal(self, b_string):
        b_number = b_string.split('.')
        natural = b_number[0]
        decimal = b_number[1]

        natural_ = self.get_value(natural, natural=True)
        decimal_ = self.get_value(decimal, natural=False)

        print 'Converting Binary to Decimal\n'
        print 'Binary String: ', b_string
        print 'Natural part:'
        print natural_
        print 'Decimal part:'
        print decimal_

        print '\nDecimal output:'
        print natural_ + decimal_


if __name__ == '__main__':
    rb = RealtoBinary()
    print
    res = rb.convert_decimal_to_binary(0.72)
    print 'Output:', res
    print
    res = rb.convert_decimal_to_binary(3.703125)
    print 'Output:', res
    print
    rb.binary_to_decimal(res)
