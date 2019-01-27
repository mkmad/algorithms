class Sparse_Search(object):

    """
    Given a sorted array of strings that is interspersed
    with empty strings, write a method to find the location
    of a given string.

    Sol: With empty strings interspersed, we can implement a
    simple modification of binary search. All we need to do is
    fix the comparison against mid, in case mid is an empty
    string. We simply move mid to the closest non-empty string

    The below code illustrates how:

    if (strings[mid ].isEmpty())
    {
        int left = mid - 1;
        int right = mid + 1;
        while (true) {
            if (left < first && right> last)
            {
                return -1;
            }
            else if (right <= last && !strings[right].isEmpty())
            {
                mid = right;
                break;
            } else if (left >= first && !strings[left].isEmpty())
            {
                mid = left;
                break;
            }
        right++;
        left--;
    }

    """

    def __init__(self):
        pass

