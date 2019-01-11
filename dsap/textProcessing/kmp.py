class KMP(object):

    """
    Given a string and a pattern, check if the pattern exists
    in the string
    """

    @staticmethod
    def failure_function(pattern):
        """

        The idea is to run two pointers i and j, i starting from 1
        and j from 0

        if values at the pattern i and j don't match then we check the
        possible value for j and this is found using the failure function
        array that's already computed so far. So, j is moved one index
        back and we check the value of f_array[j - 1] and move j there.
        This continues till we find a match between input[j] and
        input[i] or till j reaches 0

        if value matches however, value at i is changed to 'j' + 1 in the
        failure function array. Then both i and j are incremented. This is
        repeated until there is a mismatch or i reaches the end

        note
        its j + 1 (index j), not the actual value at f_array[j + 1].

        The concept behind this is, when we are actually checking the
        pattern with the string and if it mismatches at an index, then
        we look at our pre computed values (from above) and get an idea
        as to where in the pattern we can start from again

        eg

        if the string is

              v         v
        z l x a b c a b c a b y   (The substring under consideration is 'a b c a b c ')
                        ^

        and pattern is

                  v
        a b c a b y               (mismatch between 'y' and 'c')
            ^

        So, when we start the match and find mis match at 'c' (input array)
        and 'y' (pattern ) then instead of starting allover from 'a' (first char)
        from the pattern we can start from 'c' (in the pattern) because the prefix
        from 'c' is 'a b' and the suffix from 'c' is also 'a b'. Hence we eliminate
        the necessity of checking of the prefix ('a b') entirely and just start
        the next match from 'c' in the pattern

        We get the location of 'c' from the failure function.

        Watch TR if you have more questions

        """

        failure_array = [0 for _ in range(len(pattern))]

        # i starts from 1 anf j from 0, this makes sure that
        # the first value of failure function is always 0
        i = 1
        j = 0

        while i < len(pattern):
            if pattern[i] == pattern[j]:
                # If there is a match we store the value
                # at j + 1 (this is the value not index j)
                # This is what tells us where to start if
                # there was a mis match at i. We also increment
                # both i and j in this condition
                failure_array[i] = failure_array[j] + 1
                i += 1
                j += 1
            else:
                # If there is a mis match then change j to
                # the value at j - 1 (only if j > 0,
                # otherwise move on to the next value with i)

                # Note: i is not changed here
                if j > 0:
                    j = failure_array[j - 1]
                else:
                    i += 1

        return failure_array

    def kmp(self, string, pattern):

        failure_array = self.failure_function(pattern)

        # i iterates over the string and j iterates over the
        # pattern
        i = 0
        j = 0

        while i < len(string):
            if pattern[j] == string[i]:
                # Success when all the elements of the pattern
                # are parsed. Note, even though j is changed
                # or push back every now and then, it will never
                # go beyond len(pattern) - 1.
                #
                # If j == len(pattern) -1 then that means j has
                # successfully matched all the elements in the pattern
                # in the string. We could also return or print
                # the indices of the match where (i - j) will be the
                # start index of the pattern in the input string and
                # i being the end index
                if j == len(pattern) - 1:
                    return True
                else:
                    # If there are still elements remaining in
                    # the pattern then increment both i and j
                    i += 1
                    j += 1
            else:
                # If there is a mismatch then go to the
                # value computed for j in the failure function
                j = failure_array[j]

                # If j is 0 then I need to move on to the
                # next element, else this will be a infinite
                # loop
                if j == 0:
                    i += 1

        return False


if __name__ == '__main__':
    kmp = KMP()
    pattern = 'blah'
    string = 'mohanblahkumar'

    if kmp.kmp(string, pattern):
        print '\nMatch'
    else:
        print '\nNot a Match'

    pattern = 'blah'
    string = 'mohanblakumar'

    if kmp.kmp(string, pattern):
        print '\nMatch'
    else:
        print '\nNot a Match'




