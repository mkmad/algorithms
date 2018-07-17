"""
Note: This code can convert decimal to binary and vice versa for
      both +ve and -ve bases
"""


def convert_decimal_to_binary(n, base=2):
    # convert decimal to a number with base = base
    # This is similar to lcm division
    # Note: When you are dealing with -ve numbers then
    # convert the remainder to +ve (hence remainder += -base)
    result = []
    while n:
        remainder = n % base
        n = n / base
        if remainder < 0:
            remainder += -base
            n += 1
        result.append(remainder)

    return result


def convert_binary_to_decimal(binary, base=2):
    input_value = 0
    for idx, item in enumerate(binary):
        # Note -2 ** idx is different from (-2) ** idx
        # -2 ** 2 == -4 and (-2) ** 2 == 4
        input_value += int(item) * ((base) ** idx)

    neg_input_value = -input_value
    return convert_decimal_to_binary(neg_input_value, base=-2)


if __name__ == '__main__':
    print "\nThe digits are ordered from least significant " \
          "to most significant (reversed) \n"
    print convert_binary_to_decimal("10011", base=-2)
    print convert_decimal_to_binary(-9, base=-2)
