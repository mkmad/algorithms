class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def populate():
    a = node(1)
    b = node(2)
    c = node(3)
    d = node(4)
    e = node(5)
    f = node(6)
    g = node(7)
    h = node(8)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h

    return a