import math


class BucketSort(object):

    @staticmethod
    def leftmost_digit(n):
        """
        Whole idea is based on logarithms
        ie;  log x(y) = z -> x ** z = y

        We calculate the highest power that needs
        to be raised to 10.

        Also note, we need to get the floor value as we need
        the power of 10 to be a whole number eg given below

        Finally the number / higest power will give the
        leftmost number


        Eg:

        For 334

        math.floor(math.log10(334)) -> 2.0

        Now 10 ** 2 -> 100

        334 / 100 -> 3


        Note: Division operator gives the quotient and
              Modulo operator gives the remainder
              ie 334 % 100 -> 34

        Note: We need to take the floor of the log value
              else the value will not be what we wanted

              Eg:
                math.log10(334) -> 2.52374
                and 10 ** 2.52374 -> 333.99502

                So 334 / 10 ** 2.52374 -> 1.000...

                Which is not what we need, so the highest
                power value should be a whole number

                this will lead to denominator being exact
                powers of 10 ie 10, 100, 1000 ...

                Some more examples:

                3850 / 1000 -> 3
                3850 % 1000 -> 850

                78345 / 10000 -> 7
                78345 % 10000 -> 8345

        """
        # Note, taking abs value is necessary otherwise
        # math.log10 wont work
        number = math.fabs(n)
        highest_power10 = math.floor(math.log10(number))
        denominator = 10 ** highest_power10
        return int(number / denominator)

    @staticmethod
    def generate_buckets():
        """
        Create a 2D array, to represent buckets for
        indices 1..9
        """
        array = []

        for val in range(0, 10):
            array.append([])

        return array

    @staticmethod
    def insertion_sort(a):
        if not a:
            return None
        for i in range(1, len(a)):     # i starts from 1
            for j in range(i):         # j starts from 0
                if a[i] <= a[j]:
                    k = i
                    cur = a[k]
                    # Note the extra while loop
                    # Note how I am pulling values from left to right,
                    # if I do a[k+1] = a[k] then it won't work because when
                    # you change the pointer from j -> j+1 then you have
                    # copy the j+1 value to j + 2 (which is the old value)
                    while k >= j:
                        # Push all the way upto j
                        a[k] = a[k-1]
                        k -= 1
                    # After pushing the values from left to right, insert
                    a[j] = cur

    def bucket_sort(self, a):
        """
        For each value in a, calculate the leftmost
        element and store it in the respective bucket

        Then call insertion sort on each bucket

        Finally append all the values from the buckets
        as the values will already be sorted

        Note: Negative vals will also be stored in their
              respective buckets wg -213 will be 2 bucket
        """

        if not a:
            return None
        else:
            result = []
            buckets = self.generate_buckets()
            for val in a:
                leftmost = self.leftmost_digit(val)
                buckets[leftmost].append(val)
            print buckets
            for val in buckets:
                if val:
                    self.insertion_sort(val)

            for val in buckets:
                if val:
                    for vals in val:
                        result.append(vals)

            return result


if __name__ == '__main__':
    bs = BucketSort()
    a = [5, 4, 3, -1, 2, 2, 9]
    print a
    print bs.bucket_sort(a)
