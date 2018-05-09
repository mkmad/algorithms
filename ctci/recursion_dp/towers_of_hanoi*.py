class Tower_of_Hanoi(object):

    def __init__(self, no_discs):
        self.tower1 = []
        self.tower2 = []
        self.tower3 = []

        for val in range(no_discs, 0, -1):
            self.tower1.append(val)

    def move_discs(self, source, destination, buffer):
        pass
