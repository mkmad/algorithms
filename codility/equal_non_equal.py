class EqualNonEqual(object):

    """
    Question 3 from tony's problems
    pretty straightforward
    """

    def calculate(self, x, array_):
        positions = {}
        equals = 0
        non_equals = 0
        for i, v in enumerate(array_):
            if v == x:
                equals += 1
            positions[i] = equals

        for i in range(len(array_) - 1, -1, -1):
            if not array_[i] == x:
                non_equals += 1

            if positions[i] == non_equals:
                return i


if __name__ == '__main__':
    e = EqualNonEqual()
    print e.calculate(5, [5, 5, 1, 7, 2, 3, 5])
