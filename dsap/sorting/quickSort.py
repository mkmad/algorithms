class QuickSort(object):
    """
    1. Pick a pivot (usually the last element in the array)
    2. Create 3 arrays, one to hold all elements less than
       pivot, one for equal elements and one for elements
       that are greater than the pivot
    3. recursively call quick sort on left array and right
       array (the return value will be a sorted left array
       and a sorted right array)
    4. Call merge on sorted left array, sorted right array
       and the mid array (which was untouched)
    5. Merge is simply iterating through and storing vals
       from left, then mid and then right

    """

    def quick_sort(self, array):
        """
        return's an array that's either
        an array with single element or a
        sorted array
        """
        if array:
            if len(array) == 1:
                return array
            else:
                pivot = array[-1]
                l_array = []
                m_array = []
                r_array = []
                for val in array:
                    if val < pivot:
                        l_array.append(val)
                    elif val > pivot:
                        r_array.append(val)
                    else:
                        m_array.append(val)

                # TODO: I return the sorted arrays here
                # TODO: unlike merge sort
                s_larray = self.quick_sort(l_array)
                s_rarray = self.quick_sort(r_array)
                return self.merge(s_larray, m_array, s_rarray)

    def merge(self, left, mid, right):

        result = []
        if left:
            for val in left:
                if val:
                    result.append(val)

        if mid:
            for val in mid:
                if val:
                    result.append(val)

        if right:
            for val in right:
                if val:
                    result.append(val)

        return result


if __name__ == '__main__':
    a = [2, 6, 7, 2, -4, 8, 9, 3]
    q = QuickSort()
    print q.quick_sort(a)
