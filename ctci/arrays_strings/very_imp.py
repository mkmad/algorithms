def check_palindrome_of_permutations(string):
    """
    Check if any of the permutation of the string is
    a palindrome or not


    Since, we are looking for any permutation we don't
    actually have to calculate all the permutations.
    We just need to check if number of each chars in
    the string are even (except middle one if the length
    is odd i.e. at most one odd char)

    One of the approaches is to maintain a boolean array
    with size of extended ascii char set - 256 (each cell
    denotes a char) initialized to 0. So, when we
    encounter an char we flip the value to 1. In the end
    we expect all values to be 0 with at most one value of
    1

    We can achieve the same thing using bit manipulation
    i.e. we can set/unset the bit corresponding to the char

    To set the bit:

        1) get the bit mask to the char
           mask = 1 << ord(char)

        2) check if the bit is already set in that position
           i.e. checker & mask == 0/1 (checker holds the final bits)

           if the above value is 0, it means that bit
           corresponding to the char is not set else its set

           eg.

           1) If the bit is already set

           checker = 1100010000
           mask = 10000

           then checker & mask ->

           1100010000 & 0000010000 == 0000010000 which is > 0

           2) If the bit is not set

           checker = 1100010000
           mask = 1000

           then;

           1100010000 & 0000001000 = 0000000000 == 0

        3) if the bit is not set then set the bit by:

           checker = checker | mask

           else if its already set then unset the bit by:

           checker = checker & ~mask (complement of mask)

           from the above ex:

           checker = 1100010000
           mask = 10000

           ~mask = 01111

           checker & ~mask = 1100010000 & 1111101111 === 1100000000

           Note: The leading values are 1 (this is because
           the bits are 0 filled on the left to begin with)

    After all the bits are set/unset we need to check for number of 1's
    in the checker. if its 0 or 1 then the string is a palindrome

    """

    checker = 0

    for c in string:
        mask = 1 << ord(c)
        if checker & mask > 0:
            # Bit exists, so unset it
            checker &= ~mask
        else:
            # Bit doesn't exist so set it
            checker |= mask
    if count_set_bits(checker) <= 1:
        print 'Palindrome'
    else:
        print 'Not palindrome'


# Function to get no of set bits in binary
# representation of passed binary no. */
def count_set_bits(n):
    """
    Eg: get number of 1's in 9

    n =  9 (1001)
    count = 0

    Since 9 > 0, subtract by 1 and do bitwise & with (9-1)
    n = 9&8  (1001 & 1000)
    n = 8
    count  = 1

    Since 8 > 0, subtract by 1 and do bitwise & with (8-1)
    n = 8&7  (1000 & 0111)
    n = 0
    count = 2

    Since n = 0, return count which is 2 now.
    """
    count = 0
    while n:
        n &= (n - 1)
        count += 1

    return count


if __name__ == '__main__':
    s = 'mmaassd'
    ns = 'mmaasssddd'
    check_palindrome_of_permutations(s)
    check_palindrome_of_permutations(ns)
