class MaxRectAreaHistogram(object):

    """
    Note: This algorithm has a bug, if the very last element
          if higher than the second last element then the area
          that's calculated just considers the last element and
          that's wrong

          eg : [0, 0, 3, 4, 2, 4]

          

    Goal is to find the largest area rectangle in the given
    histogram

    Sol

    Maintain a stack and iterate through the histogram,
    If the value in the histogram is higher than or equal to
    the current top (or the stack is empty) then add the
    "index" of the value to the stack

    If the value is smaller than the current top then there few
    cases:

        First pop the value from stack (element_popped)

        1) If i is not the index of the very last element and the
           stack is not empty

           keep popping the values from the stack until the value
           at histogram[i] > stack[top]

           With each element that's popped, we calculate the area
           as:

                area = histogram[element_popped] * (i - stack_top - 1)

                i.e:
                    (i - stack_top - 1) is the width,
                    histogram[element_popped] is the height


                    Also note, since we iterate till
                    histogram[i] >= stack[top] and for every
                    iteration we get new height and width is
                    increased by 1 and we update the max_area
                    accordingly

                    Also note, we have -1 in (i - stack_top - 1)
                    because we append an extra element (see below)

        2) If i is the last element or the stack is empty after the
           element is popped then:

                area = histogram[element_popped] * i


    Note: We append "None" at the end of the histogram array which
          serves as a padding, this is required because we need i to
          go till len(histogram) + 1 to calculate the final area
    """

    def __init__(self, histogram):
        self.histogram = histogram
        self.stack = []
        self.max_area = -999
        self.max_area_left = None
        self.max_area_right = None

    def check_max_area(self, area, left, right):
        if self.max_area < area:
            self.max_area = area
            self.max_area_left = left
            self.max_area_right = right

    def solution(self):

        # add a padding None value in the end to help facilitate
        # i going over the len (number) of elements in histogram
        self.histogram.append(None)

        i = 0

        while i < len(self.histogram):

            if not self.stack:
                # note we append i not histogram[i]
                self.stack.append(i)
            else:
                if self.histogram[i] >= self.stack[-1]:
                    # note we append i not histogram[i]
                    self.stack.append(i)
                else:

                    # case for i being the last element (the padded element)
                    # or stack being empty
                    if i == len(self.histogram) - 1 or not self.stack:
                        top = self.stack.pop()
                        area = self.histogram[top] * i
                        # Since this condition checks for the last element 0 is the
                        # leftmost index and i -1 is the rightmost index
                        self.check_max_area(area, 0, i - 1)

                    else:
                        # keep popping elements till self.histogram[i] < self.stack[-1]
                        while self.stack and self.histogram[i] < self.stack[-1]:
                            top = self.stack.pop()
                            # self.histogram[top] is the height and (i - self.stack[-1] - 1)
                            # is the width

                            # Also, top is the rightmost index of the max rect since the stack
                            # stores the indices and (i - self.stack[-1] - 1)
                            # is the leftmost index of the max rect
                            area = self.histogram[top] * (i - self.stack[-1] - 1)
                            self.check_max_area(area, i - self.stack[-1] - 1, top)

            i += 1

        return self.max_area, self.max_area_left, self.max_area_right


if __name__ == '__main__':
    # m = MaxRectAreaHistogram([2, 1, 2, 3, 1])
    m = MaxRectAreaHistogram([0, 0, 3, 4, 2, 4])
    res = m.solution()
    print "Max area is ", res[0]
    print "Max left is ", res[1]
    print "Max right is", res[2]
