class StackOfBoxes(object):

    """
    Stack of Boxes: You have a stack of n boxes,
    with widths Wi heights hi and depths di
    The boxes cannot be rotated and can only be
    stacked on top of one another if each box in
    the stack is strictly larger than the box above
    it in width, height and depth. Implement a method
    to compute the height of the tallest possible stack.
    The height of a stack is the sum of the heights of
    each box


    Note: The requirements of this problem stipulate
    that the lower boxes must be strictly greater
    than the higher boxes in all dimensions. Therefore,
    if we sort (descending order) the boxes on a dimension,
    any dimension- then we know we don't have to look
    backwards in the list

    We will again use memoization to cache the height
    of the tallest stack with a particular box at the base
    Note: I have not used memoization in this code

    """

    def __init__(self):
        pass

    class Box(object):

        def __init__(self):
            self.height = None
            self.width = None
            self.depth = None

    @staticmethod
    def can_be_above(b1, b2):

        if b1.height > b2.height and b1.width > b2.width \
                and b1.depth > b2.depth:
            return True
        else:
            return False

    def stack_boxes(self, boxes, stack, sum_=0):
        if boxes:
            if stack:
                if self.can_be_above(stack[-1], boxes[0]):
                    stack.append(boxes[0])
                    sum_ += boxes[0].height
            else:
                stack.append(boxes[0])
                sum_ += boxes[0].height

            self.stack_boxes(boxes[1:], stack, sum_)
        else:
            print sum_
            print

    def generate_boxes(self):
        boxes = []

        b = self.Box()
        b.height = 5
        b.width = 9
        b.depth = 5

        boxes.append(b)

        b = self.Box()
        b.height = 4
        b.width = 15
        b.depth = 4

        boxes.append(b)

        b = self.Box()
        b.height = 3
        b.width = 14
        b.depth = 3

        boxes.append(b)

        b = self.Box()
        b.height = 2
        b.width = 13
        b.depth = 2

        boxes.append(b)

        b = self.Box()
        b.height = 1
        b.width = 8
        b.depth = 1

        boxes.append(b)

        return boxes

    def main(self):
        boxes = self.generate_boxes()
        # sort according to height, as mentioned in the
        # description
        boxes = sorted(boxes, key=lambda x: x.height, reverse=True)
        for i, v in enumerate(boxes):
            self.stack_boxes(boxes[i:], [])


if __name__ == '__main__':

    s = StackOfBoxes()
    s.main()
