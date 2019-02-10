def permu(xs):
    if len(xs) <= 1:
        yield xs
    else:
        """
        For each value of i, you select it and append it to each of the
        result of permu(xs[:i] + xs[i + 1])
        """
        for i in range(len(xs)):
            for p in permu(xs[:i] + xs[i + 1:]):
                yield [xs[i]] + p


if __name__ == '__main__':
    for i in permu([4, 5, 6]):
        print i
