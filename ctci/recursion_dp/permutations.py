class Permutations(object):

    """
    refer to ctci/trees_graphs/bst_sequence_permutations_imp.py
    """

    def __init__(self):
        self.count = 0

    def permutation(self, string='', picked=''):
        if not string:
            print picked
            self.count += 1

        for i in range(len(string)):
            self.permutation(string[:i] + string[i+1:], picked=picked+string[i])


if __name__ == '__main__':
    p = Permutations()
    p.permutation('mohon')
    print 
    print p.count
