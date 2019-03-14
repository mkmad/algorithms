class Regex(object):

    """

    Given a pattern and a string find if they are a match

    Solution,

    Build a 2D boolean matrix, the pattern is on top and the string
    is on the side. The conditions are as follows:

    1) If str[row] == pattern[col] or if pattern[col] == '*' then,
            matrix[row][col] = matrix[row - 1][col - 1]

    2) If pattern[col] == '*' then,
        a) check for 0 occurrence of the char in the pattern before '*'
           i.e. look for two chars to the left form the current position
           (because we are ignoring the previous char to check for 0 occurrence)
           i.e. matrix[row][col - 2] to see if its true, if not the go to step b
        b) If 0 occurrence of the prev char is false then check for 1 or more
           occurrence by checking if the previous char in the pattern is same as the
           current char in the string if it is then take the value from the top
           (i.e. ignoring the current char in the string). Else step c
        c) If both the above cases are false then just add false,
           i.e. matrix[row][col] = false


    """

    def __init__(self):
        self.matrix = None

    def solution(self, pattern, string):

        self.matrix = [[False] * (len(pattern) + 1) for _ in range(len(string) + 1)]

        # setting the very first element to True because an empty string with an
        # empty pattern is a match
        self.matrix[0][0] = True

        for row in range(1, len(self.matrix)):
            for col in range(1, len(self.matrix[0])):
                # step 1
                if pattern[col - 1] == string[row - 1] or pattern[col - 1] == ".":
                    self.matrix[row][col] = self.matrix[row - 1][col - 1]
                else:
                    # step 2
                    if pattern[col - 1] == "*":
                        # condition (a)
                        if self.matrix[row][col - 2]:
                            self.matrix[row][col] = True
                        # condition (b)
                        elif string[row - 1] == pattern[col - 2] and self.matrix[row - 1][col]:
                            self.matrix[row][col] = True

        for val in self.matrix:
            print val

        return self.matrix[len(self.matrix) - 1][len(self.matrix[0]) - 1]


if __name__ == "__main__":
    r = Regex()
    if r.solution("xa*b.c", "xaabyc"):
        print "\nRegex match"
    else:
        print "No Regex match"
