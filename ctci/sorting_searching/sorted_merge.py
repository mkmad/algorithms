class SortedMerge(object):

    """
    You are given two sorted arrays, A and
    B, where A has a large enough buffer at
    the end to hold B. Write a method to
    merge B into A in sorted order

    Note: Its pretty obvious that we need to
    start filling the space at the end of A
    but we need to compare from the end of A
    and B not the beginning
    """
    def __init__(self):
        pass

    def merge(self, array_a, array_b):
        if array_a and array_b:
            len_a = len(array_a)
            len_b = len(array_b)
            array_a.extend([None]*len(array_b))
            new_len_a = len(array_a)

            while len_a > 0 and len_b > 0:
                if array_a[len_a - 1] > array_b[len_b - 1]:
                    array_a[new_len_a - 1] = array_a[len_a - 1]
                    len_a -= 1
                else:
                    array_a[new_len_a - 1] = array_b[len_b - 1]
                    len_b -= 1
                new_len_a -= 1

            print array_a


if __name__ == '__main__':
    s = SortedMerge()
    s.merge([1, 2, 3], [4, 5, 6, 7, 8])



