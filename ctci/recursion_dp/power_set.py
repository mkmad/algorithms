import copy


class PowerSet(object):

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
    ps.get_power_set(input_set)
    print ps.power_set
