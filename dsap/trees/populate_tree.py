class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = None
        self.lable = None


def populate():
    a = node(6)
    b = node(4)
    c = node(8)
    d = node(2)
    e = node(5)
    f = node(7)
    g = node(9)
    h = node(1)
    i = node(3)

    a.lable = 'a'
    b.lable = 'b'
    c.lable = 'c'
    d.lable = 'd'
    e.lable = 'e'
    f.lable = 'f'
    g.lable = 'g'
    h.lable = 'h'
    i.lable = 'i'

    a.left = b
    b.parent = a
    a.right = c
    c.parent = a
    b.left = d
    d.parent = b
    b.right = e
    e.parent = b
    c.left = f
    f.parent = c
    c.right = g
    g.parent = c
    d.left = h
    h.parent = d
    d.right = i
    i.parent = d

    h.height = 1
    i.height = 1
    d.height = 2
    e.height = 1
    b.height = 3
    a.height = 4
    c.height = 2
    f.height = 1
    g.height = 1

    return a
