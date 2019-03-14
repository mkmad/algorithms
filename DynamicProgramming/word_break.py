class WordBreak(object):

    """
    Given a dictionary and a string, find out if you
    can split the string in such a way that each of the
    words are also in the dictionary

    Sol,

    You populate the matrix diagonally, and each diagonal
    represents the length of the sub string that's in
    consideration. The first diagonal looks for substring
    of len 1, so for eg if the string is "mohan" then
    the first diagonal looks for "m", "o"..."n".

    The second diagonal looks for len 2 so: "mo",... "an".
    The third looks for len 3 and so on..

    So, for any given length there are two things you need to
    check

        1) Check if the entire word is in the dictionary
        2) If not, iterate through the substring that's
           under consideration finding different split
           points and checking if the split resulted in
           two words.
           Note: We can check if the two substrings are
                 words themselves or they can further be
                 split into different words. We get this
                 info from the matrix itself because we
                 have already checked for all possible
                 combinations of substrings (of smaller
                 length) before

    """

    def __init__(self):
        self.matrix = None
        self.dictionary = ["I", "am", "ace", "a"]

    def solution(self, string):

        self.matrix = [[False] * len(string) for _ in range(len(string))]

        diagonal = 0
        while diagonal < len(self.matrix):
            row = 0
            col = diagonal

            while row < len(self.matrix) and col < len(self.matrix):
                if diagonal > 0:
                    substring = string[row: col]

                    if substring in self.dictionary:
                        self.matrix[row][col] = True
                    else:
                        # Try splitting the substring and check if
                        # the sub strings are themselves words or
                        # they contain other words within them

                        # Note the for loop that's checking for
                        # different split points
                        for break_point in range(len(string) - 1):

                            left = string[:break_point + 1]
                            right = string[break_point + 1:]

                            # check if the words are in the dictionary
                            if left in self.dictionary or right in self.dictionary:
                                self.matrix[row][col] = True
                                break

                            # check if either of the words are
                            else:
                                if self.matrix[row][break_point] and self.matrix[break_point][col]:
                                    self.matrix[row][col] = True
                                    break

                col += 1
                row += 1

            diagonal += 1

        return self.matrix


if __name__ == "__main__":
    w = WordBreak()
    res = w.solution("Iamace")

    for val in res:
        print val

