


'''
So, store the dependency list like this

(a, d), (f, b), (b, d), (f, a), (d, c)

project -> depends on

a -> f
b -> f
c -> d
d -> a, b
e ->
f ->

'''

projects = ['a', 'b', 'c', 'd', 'e', 'f']
deps = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

class build(object):
    def __init__(self):
        self.b_order = []
        self.bmap = {}
        for val in projects:
            self.bmap[val] = []

    def build_map(self):
        '''
        Convert deps into:

        a -> f
        b -> f
        c -> d
        d -> a, b
        e ->
        f ->
        '''

        if not deps:
            return 'Invalid Input'
        for val in deps:
            if val[1] in self.bmap:
                self.bmap[val[1]].append(val[0])
            else:
                'Invalid project'

    def populate_order(self, p): # See how recursion takes one parameter
        if self.bmap[p]: # Base case
            for val in self.bmap[p]:
                if val in self.b_order:
                    pass
                else:
                    # recurse here
                    self.populate_order(val)

        if p not in self.b_order: # Make sure there are no duplicates
            self.b_order.append(p)

    def build_order(self):
        self.build_map()
        for k,v in self.bmap.items():
            self.populate_order(k)
        print ' -> '.join(self.b_order)

if __name__ == '__main__':
    b = build()
    b.build_order()


