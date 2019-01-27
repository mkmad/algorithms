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
            left < limit and right < left < limit

    """
    def __init__(self):
        self.limit = 0
        self.res = []

    def generate_sequences(self, num):
        if num % 2 == 0:
            self.limit = num >> 1
            self.helper(inp='(', seq='', l_count=0, r_count=0)

        for val in  self.res:
            print val,

    def helper(self, inp=None, seq=None, l_count=0, r_count=0):
        if inp == '(' and l_count < self.limit:
            self.helper(inp='(', seq=seq+'(', l_count=l_count+1, r_count=r_count)
            self.helper(inp=')', seq=seq+'(', l_count=l_count+1, r_count=r_count)
            # r_count should be less than l_count, also since I am incrementing
            # r_count inside the condition it also takes case of
            # r_count == l_count
        elif inp == ')' and r_count < self.limit and r_count < l_count:
            self.helper(inp='(', seq=seq+')', l_count=l_count, r_count=r_count+1)
            self.helper(inp=')', seq=seq+')', l_count=l_count, r_count=r_count+1)
        elif l_count == r_count == self.limit:
            # enter this condition when the l_count or the r_count
            # is greater than limit or if r_count > l_count
            if seq not in self.res:
                self.res.append(seq)


if __name__ == '__main__':
    p = Parenthesis()
    p.generate_sequences(6)
