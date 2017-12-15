class Insertion(object):
    """
    run i pointer from 0,n
    run another pointer from 0,i

    if a[i] <= a[j]
        insert a[i] in a[j]
            and for values from j -> i
            pull the values j + 1 -> j

    """

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
                                       # if I do a[k+1] = a[k] then it won't work because when
                                       # you change the pointer from j -> j+1 then you have
                                       # copy the j+1 value to j + 2 (which is the old value)
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
