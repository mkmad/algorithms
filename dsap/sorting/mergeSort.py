class MergeSort(object):

    def __init__(self, mainArray):
        self.mainArray = mainArray

    def merge_sort(self, array):
        """
        We do not return anything from either of the two functions
        """
        n = len(array)
        if n > 1:
            mid = n / 2
            l_array = array[0: mid]
            r_array = array[mid: n]

            # Break up left array and right array even more
            # This will continue until the array size is 1
            # and both line 18 and 19 will return None and
            # eventually call merge function with l_array and
            # r_array with size one
            self.merge_sort(l_array)
            self.merge_sort(r_array)
            self.merge(l_array, r_array, array)
        else:
            # To show what happens when its a single element array
            print ''
            print self.mainArray
            print array
            print ''

    def merge(self, l_array, r_array, array):
        """
        We modify the original array, also since
        we are comparing i and j pointers the actual
        position of the original array is i + j

        eg: say i = 3 and j = 1
        it means we have already populated 4 positions
        in the main array i.e for values i -> 0..3 and j 0..1
        now the next position in the main array is 5th
        position (4 since its 0 indexed) so that's i + j
        """

        """
        The reason this algorithm works is because the array
        keeps changing, I got confused because i and j is always
        0 and If I am changing the main array in the same index then how 
        is this even working, so yeah I get a different array (with 
        length at least 2) to this merge call and I am modifying the 
        position of this new array
        
        Also note, the array in this call acts as a container who's 
        length is len(l_array) + len(r_array). hence the container in
        the very last call is indeed the original array. All the other
        containers are temporary
        """

        # To demonstrate the above point
        print ''
        print self.mainArray
        print array
        print ''

        i = 0
        j = 0

        # If both are pointers are still within the bounds
        while i < len(l_array) and j < len(r_array):
            if l_array[i] <= r_array[j]:
                array[i + j] = l_array[i]
                i += 1
            else:
                array[i + j] = r_array[j]
                j += 1

        # If one of the pointer is overflown (i in this case)
        if i > len(l_array) - 1 and j < len(r_array):
            while j < len(r_array):
                array[i + j] = r_array[j]
                j += 1

        # j is overflown
        elif i < len(l_array) and j > len(r_array) - 1:
            while i < len(l_array):
                array[i + j] = l_array[i]
                i += 1


if __name__ == '__main__':
    a = [4, -7, 2, 3, 6, 1]
    ms = MergeSort(a)
    ms.merge_sort(a)
    print a
