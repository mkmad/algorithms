def combs(items):

    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2 ** N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


if __name__ == '__main__':
    for val in combs([1,2,3]):
        print val