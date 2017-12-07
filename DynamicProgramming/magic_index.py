#So, this is an interesting problem. Look for the solution.
# Hint: its very much like BS.
# A little trickier case would be if the elements not unique.

# Consider
# -20  -2  2  2  2  3  7  8  9
#  0    1  2  3  4  5  6  7  8

# According to the 1st approach I have to go right since 3 < 5. Because the top element
# can just reduce by 1 at max and bottom also will reduce by 1 at max, so we are in the
# same boat as before. This happens since case 1 has unique elements. But it fails in
# case 2 coz there may be repetitions 2 is the answer.

# Code for method 2.

def magic(start, end, a):
    mid = (start + end) /2
    if a[mid] == mid:
        return mid
    else:
        # To determine if the number is part of repetitive
        # sequence, note: you can skip some elements from
        # mid coz if you either go left or right you can
        # skip  mid =- a[mid] indices as the mid != a[mid]
        magic(start, min(mid -1, a[mid]), a)
        magic(max(mid +1, a[mid]),a)







