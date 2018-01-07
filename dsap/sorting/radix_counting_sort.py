import math


class RadixCountingSort(object):

    def radix_sort(self, array):
        """
        Call counting sort for each index/radix of the values
        in the array
        """
        if array:
            max_value = max(array)
            min_value = min(array)

            # if the value is negative then do -1,
            # since str(-1234) -> length 5 when its supposed to be 4
            max_index = max(len(str(max_value)), len(str(min_value)) - 1)

            index = 1
            while index <= max_index:
                array = self.counting_sort(array, index)
                index += 1
            return array

    def counting_sort(self, array, index=None):
        """
        Algorithm is straightforward

        Step 1: Maintain a count dict/array, loop through
                input array and keep a count of the
                elements

        Step 2: Loop through the count dict and recalculate
                the count by count[index] += count[index -1]

        Step 3: Loop through the input array and store the val
                in the output array by the location specified
                in count[val], then reduce count[val] by 1


        Complexities with negative numbers:

        1) You can't have a count array, because arrays are
           0 indexed and will take only positive integers as
           indexes (a negative index will wrap around the array).
           This is a unique algorithm as this is index based and
           others (heap, merge, bucket...) are comparison based

        2) Since you have a count dict, you need to take all the
           values in the range min(array) and max(array) into
           account because when you recalculate count, you
           propagate values from left to right i.e. the linear
           chain is important (in array this is not a problem as
           it is linear in nature and dict is not)

        3) When you store the count of a value in the count dict
           you do so using the value of the input array as the key,
           so in the final step when you store the values from count dict
           onto the output array you need to be careful and do -1 i.e.
           output[count[val] - 1] because arrays are 0 indexed and
           count dict maintains the position that is not 0 indexed

        """
        output = [0 for _ in range(len(array))]

        # Count should be dict if we are to handle
        # negative numbers since array with negative
        # indices will wrap around
        count = {}

        if array:
            # If counting sort is used along with radix sort
            if index:
                indices = []
                # populate indices first and then populate count
                for val in array:
                    idx = self.get_index(val, index)
                    indices.append(idx)

                # populate count
                min_val = min(indices)
                max_val = max(indices)
                self.populate_count(count, min_val, max_val)

                # store the count of indices
                for val in indices:
                    count[val] += 1

                # recalculate count
                self.recalculate_count(count, min_val, max_val)

                for val in array:
                    idx = self.get_index(val, index)
                    # Note the - 1
                    output[count[idx] - 1] = val
                    count[idx] -= 1

            # For standalone counting sort
            else:
                min_val = min(array)
                max_val = max(array)
                self.populate_count(count, min_val, max_val)
                for val in array:
                    count[val] += 1

                self.recalculate_count(count, min_val, max_val)

                for val in array:
                    # Note the - 1
                    output[count[val] - 1] = val
                    count[val] -= 1

            return output
        else:
            return

    @staticmethod
    def recalculate_count(count, min_val, max_val):
        if count:
            for key in range(min_val, max_val + 1):
                if key - 1 in count:
                    count[key] += count[key - 1]

    def get_index(self, val, index):
        """
        Get the value in val based on the index
        """

        # Getting the last value since index = 1
        # need this condition because 4 / 10 -> 0
        # but we need 4
        if index <= 1:
            # This is for negative values
            if val < 0:
                # if a is negative the (a % b) - b will give
                # the negative mod
                # Eg:
                # 1) -2 % 10 -> 8; 8 - 10 -> -1
                # 2) -343 % 10 -> 7; 7 -10 -> -3
                return (val % 10) - 10
            else:
                return val % 10
        else:
            if val < 0:
                temp = - int(math.fabs(val) / 10**(index - 1))
            else:
                temp = int(math.fabs(val) / 10 ** (index - 1))

        if temp > 0:
            return temp % 10

        elif temp < 0:
            # Getting negative mod, same as above
            return (temp % 10) - 10

        # The val is less than 10 ** (index -1), which means
        # the val doesn't have a digit in that index/radix
        else:
            return 0

    @staticmethod
    def populate_count(count, min_val, max_val):
        for val in range(min_val, max_val + 1):
            count[val] = 0


if __name__ == '__main__':
    array = [3, 2, 6, -8, 4, 9, 1, 7]
    rdx = RadixCountingSort()
    print rdx.counting_sort(array)

    array = [9, 0, 6, 8, -7, 9, -1, -2]
    print rdx.radix_sort(array)



