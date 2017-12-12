class Stack(object):

    def __init__(self):
        self.myStack = []

    def push(self, val):
        self.myStack.append(val)

    def pop(self):
        if not self.myStack:
            raise Exception('Empty stack')
        return self.myStack.pop()

    def top(self):
        if not self.myStack:
            raise Exception('Empty Stack')
        return self.myStack[-1]


