# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, A):
    """
    A small frog wants to get to the other side of a river.
    The frog is initially located on one bank of the river
    (position 0) and wants to get to the opposite bank
    (position X+1). Leaves fall from a tree onto the surface
    of the river.

    You are given an array A consisting of N integers representing
    the falling leaves. A[K] represents the position where one leaf
    falls at time K, measured in seconds.

    The goal is to find the earliest time when the frog can jump to
    the other side of the river. The frog can cross only when leaves
    appear at every position across the river from 1 to X (that is, we
    want to find the earliest moment when all the positions from 1 to X
    are covered by leaves). You may assume that the speed of the current
    in the river is negligibly small, i.e. the leaves do not change their
    positions once they fall in the river.

    For example, you are given integer X = 5 and array A such that:
    [1, 3, 1, 4, 2, 3, 5, 4]

    In second 6, a leaf falls into position 5. This is the earliest time when
    leaves appear in every position across the river.


    Note: If you want to get a mask with all 1's of length 5 then you need
          to shift 1 to 5 times to the left. This will let the 1 bit to be in
          the 6th position and when you subtract 1 from that you'll get
          a mask with 5 bits a that's all 1's

    Also note: That's is also the reason why I have a val - 1 when I am setting
               bit in the bits var, If I want to set a bit in the second position
               then I do 1 << (2 - 1) == 1 << 1 == '10', if not for that -1 the
               bit position would be '100'

    """

    # mask of len X with all bits set to 1
    mask = (1 << X) - 1
    bits = 0
    count = 0
    for val in A:
        # Shift the bits val - 1 times because if we
        # shift the bits 1 time then the result is '10'
        # but I was expecting just '1'

        # After shifting the bits, you set it to the bits var
        bits |= 1 << (val - 1)

        # If the xor of bits and mask is zero then it means all
        # the bits are set and the frog can now jump to the other
        # side
        if bits ^ mask == 0:
            return count
        count += 1

    return -1


if __name__ == '__main__':
    print solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
