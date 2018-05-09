class BooleanEvaluation(object):

    """
    Boolean Evaluation: Given a boolean expression consisting
    of the symbols 0 (false), 1 (true), & (AND), | (OR), and
    ^ (XOR), and a desired boolean result value, implement a
    function to count the number of ways of parenthesizing
    the expression such that it evaluates to result. The expression
    should be fully parenthesized  e.g.,(0)^(1) but not extraneously
    e.g., (((0))^(1)))

    EXAMPLE
    countEval("1^0|0|1", false) -> 2
    countEval("0&0&0&1^1|0", true) - > 10
    """

    def __init__(self):
        pass

    def evaluate(self, string, boolval=False):
        num = 0

        if not string:
            return 0

        if len(string) == 1:
            if bool(string) == boolval:
                return 1
            else:
                return 0

        for i, c in enumerate(string):
            if c not in ('^', '&', '|'):
                continue
            else:
                left = string[:i]
                right = string[i+1:]

                if c == '^':
                    if boolval:
                        num += self.evaluate(left, boolval=True) * self.evaluate(right, boolval=False)
                        num += self.evaluate(left, boolval=False) * self.evaluate(right, boolval=True)
                    else:
                        num += self.evaluate(left, boolval=True) * self.evaluate(right, boolval=True)
                        num += self.evaluate(left, boolval=False) * self.evaluate(right, boolval=False)

                elif c == '&':
                    if boolval:
                        num += self.evaluate(left, boolval=True) * self.evaluate(right, boolval=True)
                    else:
                        num += self.evaluate(left, boolval=True) * self.evaluate(right, boolval=False)
                        num += self.evaluate(left, boolval=False) * self.evaluate(right, boolval=True)
                        num += self.evaluate(left, boolval=False) * self.evaluate(right, boolval=False)

                elif c == '|':
                    if boolval:
                        num += self.evaluate(left, boolval=True) * self.evaluate(right, boolval=False)
                        num += self.evaluate(left, boolval=False) * self.evaluate(right, boolval=True)
                        num += self.evaluate(left, boolval=True) * self.evaluate(right, boolval=True)
                    else:
                        num += self.evaluate(left, boolval=False) * self.evaluate(right, boolval=False)
                else:
                    print 'Invalid character encountered', c
                    continue

        return num


if __name__ == '__main__':
    be = BooleanEvaluation()
    print be.evaluate("1^0|0|1", False)
    print be.evaluate("0&0&0&1^1|0", True)




