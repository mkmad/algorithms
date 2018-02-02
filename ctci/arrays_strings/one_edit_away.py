def one_edit_away(string_a, string_b):
    """
    Goal is to check if string_a is one edit away
    from string_b. Examples of edits:

    1) remove a char
    2) insert a char
    3) replace a char

    Note:
    In either case the lengths of string_b will tell
    you which operation to perform
    """

    if len(string_b) == len(string_a):
        return check_for_replace(string_a, string_b)
    elif len(string_b) < len(string_a):
        return check_for_delete(string_a, string_b)
    else:
        return check_for_insert(string_a, string_b)


def check_for_replace(a, b):
    i = 0
    replaced = False
    while i < len(a):
        if a[i] == b[i]:
            i += 1
        else:
            if a[i + 1] == b[i + 1] and not replaced:
                replaced = True
                i += 1
            else:
                print 'Difference is more than 1'
                replaced = False
                break

    if replaced:
        print 'One char replaced'

    return replaced


def check_for_delete(a, b):

    deleted = False
    li = 0
    ri = 0
    while li < len(b):
        if b[li] == a[ri]:
            li += 1
            ri += 1
        else:
            if b[li] == a[ri + 1] and not deleted:
                deleted = True
                ri += 1
            else:
                print 'Difference is more than 1'
                deleted = False
                break

    # NOTE: This condition is to ensure we also consider
    # if the very last char is deleted
    # Eg: if a = pales and b = pale then both ri and li == 4
    # because I am incrementing after I check equality
    if not deleted and ri == len(a) - 1:
        deleted = True

    if deleted:
        print 'One char deleted'

    return deleted


def check_for_insert(a, b):

    inserted = False
    li = 0
    ri = 0

    while li < len(a):
        if a[li] == b[ri]:
            li += 1
            ri += 1
        else:
            if a[li] == b[ri + 1] and not inserted:
                inserted = True
                ri += 1
            else:
                print 'Difference is more than 1'
                inserted = False
                break

    # NOTE: This condition is to ensure we also consider
    # if the very last char is inserted in b
    # Eg: if a = pale and b = pales then both ri and li == 4
    # because I am incrementing after I check equality
    if not inserted and ri == len(b) - 1:
        inserted = True

    if inserted:
        print 'One char inserted'

    return inserted


if __name__ == '__main__':
    print
    print one_edit_away('pale', 'ple')
    print
    print one_edit_away('pales', 'pale')
    print
    print one_edit_away('pale', 'bale')
    print
    print one_edit_away('pale', 'bae')
    print
    print one_edit_away('pale', 'pales')
