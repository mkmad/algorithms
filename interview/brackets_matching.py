# Complete the isBalanced function below.
def isBalanced(s):
    string = list(s)
    stack = []
    matching_pair = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for val in string:
        if val not in (['{','[', '(', ')', ']', '}']):
            return False
        else:
            if stack:
                if val in matching_pair:
                    if stack[-1] == matching_pair[val]:
                        stack.pop()
                    else:
                        stack.append(val)
                else:
                    stack.append(val)
            else:
                stack.append(val)

    if stack:
        return False

    return True


if __name__ == '__main__':
    print isBalanced("{(([])[])[]]}")
