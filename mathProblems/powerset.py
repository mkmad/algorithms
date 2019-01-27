# There are four subsets of the set {a1,a2} : {}, {a1},{a2),{a1, a2}
# Note : {a1, a2} is the same as {a2, a1}
import copy

inp = (4, 5, 6)
def power_set(input):
    if input:
        temp = copy.deepcopy(input)
        for val in inp:
            for sub_val in input:
                if val not in sub_val:
                    sub_val.append(val)
                    if sub_val.sort() not in temp:
                        if sub_val:
                            temp.append(sub_val)
        power_set(temp)
    else:
        return





if __name__ == '__main__':
    inp_ = []
    for val in inp:
        inp_.append([val])
    power_set(inp_)
