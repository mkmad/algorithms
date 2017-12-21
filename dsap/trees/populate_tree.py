class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


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

    return a
