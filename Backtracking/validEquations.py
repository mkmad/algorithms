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

    def main(self):
        num = [2, 3, 4, 5]
        ops = []
        if not self.evaluate(num, 6, ops, prev=num[0], index=1):
            print "No valid equation found"
        else:
            if ops and num:
                ops.reverse()
                for i in range(len(ops)):
                    print '{0} {1}'.format(num[i], ops[i]),
                print num[-1]


if __name__ == '__main__':
    v = ValidEquations()
    v.main()
