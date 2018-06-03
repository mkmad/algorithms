# -*- coding: utf-8 -*-


class StoneWall(object):

    """

    You are going to build a stone wall. The wall should be straight and N meters
    long, and its thickness should be constant; however, it should have different
    heights in different places. The height of the wall is specified by an array H
    of N positive integers. H[I] is the height of the wall from I to I+1 meters to
    the right of its left end. In particular, H[0] is the height of the wall's left
    end and H[N−1] is the height of the wall's right end.

    The wall should be built of cuboid stone blocks (that is, all sides of such blocks
    are rectangular). Your task is to compute the minimum number of blocks needed to
    build the wall.

    Write a function:

    def solution(H)

    that, given an array H of N positive integers specifying the height of the wall,
    returns the minimum number of blocks needed to build it.

    For example, given array H containing N = 9 integers:

      H[0] = 8    H[1] = 8    H[2] = 5
      H[3] = 7    H[4] = 9    H[5] = 8
      H[6] = 7    H[7] = 4    H[8] = 8
    the function should return 7. The figure shows one possible arrangement of seven
    blocks.

    Assume that:

    N is an integer within the range [1..100,000];
    each element of array H is an integer within the range [1..1,000,000,000].
    Complexity:

    expected worst-case time complexity is O(N);
    expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

    Note:

        this was my wrong solution:

        Here I tried to count the number of blocks when I am poping
        the values, which will not be accurate.


        def solution(H):
            stack_ = []
            count = 0
            for val in H:
                if len(stack_) == 0:
                    stack_.append(val)
                elif val >= stack_[-1]:
                    stack_.append(val)
                else:
                    while len(stack_) > 0:
                        if stack_[-1] > val:
                            count += 1
                            stack_.pop()
                        else:
                            break
                    stack_.append(val)

            return count


    So,

    Instead, when you append the the values to stack it means
    I am inserting a value that has height > stack_[-1], this
    means I need more blocks since the new value is higher. If
    the value < stack_[-1] it means I have already paid (have)
    blocks for all the levels below stack_[-1] so just pop the
    values until value > stack[-1] (This time you need to increment
    the block count again for the height you inserted)
    """

    @staticmethod
    def solution(H):

        stack_ = []
        count = 0
        for val in H:
            # add count whenever you append to stack_
            if len(stack_) == 0:
                stack_.append(val)
                count += 1
            elif val > stack_[-1]:
                stack_.append(val)
                count += 1
            else:
                while len(stack_) > 0:
                    if stack_[-1] > val:
                        stack_.pop()
                    else:
                        stack_.append(val)
                        count += 1
                        break

        return count


if __name__ == '__main__':
    s = StoneWall()
    print s.solution([8, 8, 5, 7, 9, 8, 7, 4, 8])
