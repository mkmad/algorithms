class ValidEquations(object):

    """
    Given numbers and dashes between them, find a
    valid equation which results in the target
    by filling either + or - in the dashes
    """

    def evaluate(self, num, target,  valid_ops, prev=0, index=0):
        if prev == target:
            return True
        elif index > len(num) - 1 or prev > target:
            return False
        else:
            if self.evaluate(num, target, valid_ops, prev=prev + num[index],
                             index=index + 1):
                valid_ops.append('+')
                return True
            elif self.evaluate(num, target, valid_ops, prev=prev - num[index],
                               index=index + 1):
                valid_ops.append('-')
                return True
            else:
                return

    def evaluate_(self, input, target, running_sum=None, index=0):

        if running_sum is None:
            if len(input) < 2:
                return
            else:
                minus = input[0] - input[1]
                addition = input[0] + input[1]
                self.evaluate_(input, target, running_sum=minus, index=2)
                self.evaluate_(input, target, running_sum=addition, index=2)
                return

        if running_sum == target:
            print "Found target: index {0}".format(index)
            return

        if index > len(input) - 1:
            return

        if running_sum > target:
            return
        else:
            self.evaluate_(input, target, running_sum=running_sum + input[index], index=index + 1)
            self.evaluate_(input, target, running_sum=running_sum - input[index], index=index + 1)

    def main(self):
        num = [2, 3, 4, 5]
        ops = []
        print "First method"
        if not self.evaluate(num, 6, ops, prev=num[0], index=1):
            print "No valid equation found"
        else:
            if ops and num:
                ops.reverse()
                for i in range(len(ops)):
                    print '{0} {1}'.format(num[i], ops[i]),
                print num[-1]

        print
        print "Second method"
        self.evaluate_(num, 6)


if __name__ == '__main__':
    v = ValidEquations()
    v.main()
