class NumFactors():

    """
    If a number (m) is a divisor of another number (n), then
    there will be another symmetric number ( n / m ) which
    will also be a divisor of m

    Note: ( n / m ) will be greater than n only if n < sqrt(m)
          for values of n that are greater then sqrt(m) the (n / m)
          value will be less than n, moreover it will point to the
          symmetric value that's already been calculated, see example
          below

    Eg: if n = 36

        for all values that are divisor of n, ie n % m == 0:


        m = 1
        sym of m = 36

        m = 2
        sym of m = 18

        m = 3
        sym of m = 12

        m = 4
        sym of m = 9

        m = 6
        sym of m = 6

        Note, 6 is sqrt(36) now all values greater than 6 the sym value
        will point to old value, eg

        m = 9
        sym of m = 4

        m = 12
        sym of m = 3

        and so on..


    Hence, iterate sqrt(n) times and if i*i < sqrt(n) then there are two
    divisors else if i*i == sqrt(n) then there only one divisor


    Also note: We can use the same concept to check if a number is prime or
    not

    def primality(n):
        i = 2
        while (i * i <= n):
            if (n % i == 0):
                return False
            i += 1
        return True

    """

    @staticmethod
    def Solution(N):

        i = 1
        factors = 0
        while i * i <= N:
            if N % i == 0:
                if i * i == N:
                    factors += 1
                else:
                    factors += 2

            i += 1

        return factors


if __name__ == '__main__':
    n = NumFactors()
    print n.Solution(36)
