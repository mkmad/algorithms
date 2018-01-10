class KMP(object):

    @staticmethod
    def failure_function(pattern):
        """
        The idea is to run two pointers i and j, i starting from 1
        and j from 0

        if values at the pattern i and j don't match then i simply
        moves to the next element

        if it matches however, value at i is changed to 'j' + 1, note
        its j + 1 (index j), not the actual value at j + 1. Then
        both i and j are incremented. This is repeated until there is
        a mismatch

        The concept behind this is, when we are actually checking the
        pattern with the string and if it mismatches at an index, then
        we look at our pre computed values (from above) and get an idea
        as to where in the pattern we can start from again

        eg

        if the string is

              v         v
        z l x a b c a b c a b y
                        ^

        and pattern is

        a b c a b y
            ^

        So, when we start the match and find mis match at 'c' then instead
        of starting allover from 'a' we can start from 'c' (in the pattern).
        This we get from the failure function. Also, note the failure
        function grantees that substring before 'c' (in the pattern) will
        also exist in the main string because of the way we calculate the
        failure function (we increment both i and j if there is a match)

        Watch TR if you have more questions

        """

        failure_array = [0 for _ in range(len(pattern))]

        # i starts from 1 anf j from 0
        i = 1
        j = 0

        while i < len(pattern):
            if pattern[i] == pattern[j]:
                # If there is a match we store the value
                # at j + 1 (this is the value not index j)
                # This is what tells us where to start if
                # there was a mis match at i
                failure_array[i] = failure_array[j] + 1
                i += 1
                j += 1
            else:
                # If there is a mis match then change j to
                # the value at j - 1 (only if j > 0,
                # otherwise move on to the next value with i)
                if j > 0:
                    j = failure_array[j - 1]
                else:
                    i += 1

        return failure_array

    def kmp(self, string, pattern):

        failure_array = self.failure_function(pattern)

        i = 0
        j = 0

        while i < len(string):
            if pattern[j] == string[i]:
                # Success when all the elements of the pattern
                # are parsed
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




