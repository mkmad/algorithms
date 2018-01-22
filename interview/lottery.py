import copy


class LotteryTicket(object):
    """
    Problem
    -------
    Given a large series of number strings, return each that
    might be suitable for a lottery ticket pick. Note that a
    valid lottery ticket must have 7 unique numbers between
    1 and 59, digits must be used in order, and every digit
    must be used exactly once.

    Approach
    --------

    I use Backtracking (Decision tree) to find all possible combinations
    of the input sequence and return valid (if any) lottery ticket
    sequence(s) that follows/obeys the rules mentioned in the problem
    statement.

    In each function call I pick the first element in the string, and pass it
    to a recursive call along with the remainder of the sequence. Then I pick
    first two elements in the string and pass it to another recursive call
    along with the remainder of the sequence.

    For each element that was chosen, I verify if it is in the range
    1 < element < 60 and if it is valid I move forward with the next set of
    recursive calls. I also maintain an output array that stores the chosen
    elements along the recursive stack. If the output array has 7 elements
    and the input sequence is empty I return the output array up the stack.

    Time Complexity
    ---------------

    For each and every call to the generate function it in turn calls itself
    twice hence the time complexity for generate function is 2^n, where n
    is the length of each sequence/input

    Note: The sequence_generator function calls generate for each and every
    sequence in the input array. Hence the overall time complexity is
    o(m * 2^(length of each sequence)), where m is the length of the input
    array. Hence this algorithm runs in exponential time.

    """

    def __init__(self):
        # Initialize limits/restrictions
        self.min_value = 1
        self.max_value = 60
        self.sequence_length = 7

    @staticmethod
    def validate_sequence(seq):
        """
        This function checks if the sequence contains
        only digits and is non negative

        :param seq: sequence to validate
        :return: True if valid and False if not
        """
        try:
            # check if seq has only digits
            value = int(seq)
            # check if it is non negative
            if value < 0:
                return False
            return True
        except ValueError:
            # return false if seq contains non digits
            return False

    @staticmethod
    def print_result(res):
        """
        This is a helper function, used to print the result
        (if any)
        :param res: result dict
        :return: None
        """
        if res:
            print '\nSequences found:'
            for k, v in res.items():
                print '{0} -> {1}'.format(k, v)
        else:
            print 'No sequences found'

    def generate(self, sequence=None, output=None):
        """
        Generate valid sequence recursively using Backtracking

        :param sequence: sequence for the current call
        :param output: output array for the current call
        :return: valid output array with 7 unique elements or None
        """

        l_branch = None
        r_branch = None

        # base condition for sequence
        if sequence:
            # if sequence has only element left
            if len(sequence) == 1:
                if len(output) == self.sequence_length - 1:
                    # If there is only one element in the sequence
                    # and only one spot in the output array, then
                    # add the last element and return output
                    output.append(int(sequence[0]))
                    return output

            # If there are more than one element
            else:
                if len(output) < self.sequence_length:

                    # Copy the output
                    temp = copy.deepcopy(output)
                    # Pick only one element (leftmost), add it to the
                    # temp output and call generate again with the picked
                    # element removed from the sequence
                    # Note: proceed only if the element is valid
                    if int(sequence[0:1]) >= self.min_value and \
                            int(sequence[0:1]) not in temp:
                        temp.append(int(sequence[0:1]))
                        l_branch = self.generate(
                            sequence[1:], output=temp)

                    # Copy the output
                    temp = copy.deepcopy(output)
                    # Pick two elements (leftmost), add it to the
                    # temp output and call generate again with the picked
                    # elements removed from the sequence
                    # Note: proceed only if the element is valid
                    if self.min_value < int(sequence[0:2]) < self.max_value and \
                            int(sequence[0:2]) not in temp:
                        temp.append(int(sequence[0:2]))
                        r_branch = self.generate(
                            sequence[2:], output=temp)

                    # If either of the calls returns a valid output then return
                    # the output
                    if l_branch:
                        return l_branch
                    elif r_branch:
                        return r_branch

        # If the sequence if empty, check if the output array is populated.
        # If it is populated and its length is 7 then return it
        else:
            if len(output) == self.sequence_length:
                return output

    def sequence_generator(self, input_array):
        """
        For each sequence in the input array, check if it is
        valid and then call generate function for that sequence

        If any output is returned it is stored in a result dict
        (used for printing)

        print the results (if any)

        :param input_array: sequences of input
        :return: None
        """
        result = {}
        if input_array:
            for seq in input_array:
                if self.validate_sequence(seq):
                    output = self.generate(sequence=seq, output=[])
                    if output:
                        result[seq] = output
                else:
                    print '\n{0} is not valid'.format(seq)
                    print 'Sequences should only contain ' \
                          'numbers and must be non negative'
            self.print_result(result)
        else:
            raise Exception('Input array cannot be empty')


if __name__ == '__main__':

    input_array = ["569815571556", "4938532894754",
                   "1234567", "472844278465445"]
    print "\nInput given"
    print input_array
    lt = LotteryTicket()
    lt.sequence_generator(input_array)
