class Kadanes(object):

    """
    Iterate through the array and maintain a running sum,
    if the current val > current val + running sum then there
    is no point in adding the current val in the running sum(
    which represents the current max sub array)

    if current val + running sum > current val then add the current
    val to running sum (thereby adding it to the max sub array)

    the sub array is maintained by two indices, the start of the sub array
    and the the current index
    """
    def max_sub_array(self, array_):

        sub_array_start = 0
        running_sum = None
        sub_arrays = {}

        for i, val in enumerate(array_):
            if running_sum is None:
                running_sum = val
            else:
                if running_sum + val > val:
                    running_sum += val
                else:
                    sub_arrays[running_sum] = (sub_array_start, i - 1)
                    sub_array_start = i
                    running_sum = val

            if i == len(array_) - 1:
                sub_arrays[running_sum] = (sub_array_start, i)

        return sub_arrays


if __name__ == '__main__':
    k = Kadanes()
    print k.max_sub_array([-5, 6, 7, 1, 4, -8, 16])
