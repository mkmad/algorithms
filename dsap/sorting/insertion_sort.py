class Insertion(object):

    def __init__(self):
        pass

    def insertion_sort(self, a):
        if not a:
            return None
        for i in range(1, len(a)):
            for j in range(i):
                if a[i] <= a[j]:
                    k = i
                    cur = a[i]
                    while k:           # Note the extra while loop
                        a[k] = a[k-1]  # Note how I am pulling values from left to right,
                                       # if I a[k+1] = a[k] then it won't work
                        k -= 1
                    a[j] = cur
                    print a

    def main(self):
        a = [5, 4, 3, 1, 2]
        print a
        self.insertion_sort(a)


if __name__ == '__main__':
    i = Insertion()
    i.main()
