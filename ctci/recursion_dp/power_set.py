import copy


class PowerSet(object):
    """
    The set of all the subsets of a set

    Example: For the set {a,b,c}:

        The empty set {} is a subset of {a,b,c}
        And these are subsets of len 1: {a}, {b} and {c}
        And these are also subsets (len 2): {a,b}, {a,c} and {b,c}
        And {a,b,c} is a subset of {a,b,c}

    And altogether they make the Power Set:

    P(S) = { {}, {a}, {b}, {c}, {a,b}, {a,c}, {b,c}, {a,b,c} }

    How this works:

        BaseCase: n = 0
        There is just one subset of the empty set: {}.

        Case: n = 1.
        There are two subsets of the set {al } : {}, {a1}.

        Case:n =2.
        There are four subsets of the set{a1} a2} : {}, {a1},{a2},{a1, a2).

        Case:n =3.
        Now here's where things get interesting. We want to find away of generating
        the solution for n on the prior solutions.

        P(2) = {}, {a1} , {a2} , {a1, a2}
        P(3) = {}, {a1} , {a2} , {a3}, {a1, a2}, {a2, a3}, {a1, a3}, {a1, a2, a3}

        so, P(3) = adding a3 to all the elements in a2


    Solution:

        This is similar to bfs, i.e. queue the result from the current function
        call and then pass this queue for the next function call while store all
        the results to the external variable.

    """

    def __init__(self):
        self.result = []

    def power_set(self, input_set, sub_result):

        output = []
        # store the intermediate results in the result array
        # first. Then use the intermediate results to calculate
        # the next batch of results
        for val in sub_result:
            if val not in self.result:
                self.result.append(val)

        for val in input_set:
            for sub_val in sub_result:
                if val not in sub_val:
                    sub_val_ = copy.deepcopy(sub_val)
                    sub_val_.add(val)
                    output.append(sub_val_)
                    if len(sub_val_) == len(input_set):
                        self.result.extend(output)
                        return

        self.power_set(input_set, output)


if __name__ == '__main__':
    ps = PowerSet()
    input_set = {['a', 'b', 'c']}

    ps.power_set(input_set, [set()])
    print ps.result

