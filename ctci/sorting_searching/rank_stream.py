class RankStream(object):

    """
    Rank from Stream: Imagine you are reading in
    a stream of integers. Periodically, you wish
    to be able to look up the rank of a number x
    (the number of values less than or equal to x).
    Implement the data structures and algorithms to
    support these operations. That is, implement the
    method track(int x), which is called when each
    number is generated, and the method
    getRankOfNumber(int x), which returns the number
    of values less than or equal to x (not including
    x itself)

    we insert elements into a binary search tree. The
    method t rack(int x) will run in 0(log n) time,
    where n is the size of the tree (provided, of course,
    that the tree is balanced)

    To find the rank of a number, we could do an in-order
    traversal, keeping a counter as we traverse.The goal
    is that, by the time we find x, counter will equal the
    number of elements less than x

    As long as we're moving left during searching for x, the
    counter won't change. Why? Because all the values we're
    skipping on the right side are greater than x. After all,
    the very smallest element (with rank of 1) is the leftmost
    node

    When we move to the right though, we skip over a bunch of
    elements on the left. All of these elements are less than
    x, so we'll need to increment counter by the number of
    elements in the left subtree

    Rather than counting the size of the left subtree (which
    would be inefficient), we can track this information as
    we add a counter to each node that keeps tack of all the
    elements that are below it

    """