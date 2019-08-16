class Parenthesis(object):
    """
        Parens: Implement an algorithm to print all valid
        (Le., properly opened and closed) combinations of
        n pairs of parentheses.
        EXAMPLE
        Input: 3
        Output:((())),(()()), (())(), ()(()), ()()()

        Simple recursive tree solution, make sure the
        count of right parenthesis is always less than
        or equal to left parenthesis. Also maintain a
        limit variable which keeps track of the total number
        of left and right parenthesis that are allowed

        so the conditions are:
            left < limit , right < left < limit

    """
    def __init__(self):
        self.limit = 0
        self.res = []

    def generate_sequences(self, num_of_pairs):
        self.limit = num_of_pairs
        self.sequences()

        for val in self.res:
            print val,

    def sequences(self, seq=str(), l_count=0, r_count=0):

        if l_count < self.limit:
            self.sequences(seq=seq + '(', l_count=l_count+1, r_count=r_count)
        if r_count < self.limit and r_count < l_count:
            self.sequences(seq=seq + ')', l_count=l_count, r_count=r_count + 1)

        if l_count == r_count == self.limit:
            self.res.append(seq)


if __name__ == '__main__':
    p = Parenthesis()
    p.generate_sequences(3)

