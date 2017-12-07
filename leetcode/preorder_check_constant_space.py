def verifyPreorder(preorder):
    # stack = preorder[:i], reuse preorder as stack
    lower = -1 << 31
    i = 0
    for x in preorder:
        if x < lower:
            return False
        while i > 0 and x > preorder[i - 1]:
            lower = preorder[i - 1]
            i -= 1
        preorder[i] = x
        i += 1
    print preorder
    return True

if __name__ == '__main__':
    verifyPreorder([4,2,1,3,9,5,10])