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

    """

    def __init__(self):
        self.power_set = []

    def get_power_set(self, input_set, running_set=None, count=2):
        if count <= len(input_set):
            if not running_set:
                self.power_set.append(set())
                self.power_set.append(input_set)
                running_set = copy.deepcopy(input_set)
            cur_set = set()
            for val in input_set:
                for s_val in running_set:
                    if val not in s_val:
                        temp = ''.join(sorted(val + s_val))
                        if temp not in cur_set:
                            cur_set.add(temp)
            self.power_set.append(cur_set)
            self.get_power_set(input_set, cur_set, count=count + 1)


if __name__ == '__main__':
    ps = PowerSet()
    input_set = set(['a', 'b', 'c'])
    ps.input = ['a', 'b', 'c']
    ps.get_power_set(input_set)
    print ps.power_set

