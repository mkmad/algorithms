# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    # write your code in Python 2.7
    if not A:
        print "Invalid Input"
    if type(X) != int:
        print "Expected a number"
    calculate_value(X, A)
    
def calculate_value(X, A):
    bool = True
    mid = len(A) / 2
    while bool:
        common = calculate_common(X, A[:mid])
        noncommon = calculate_non_common(X, A[mid +1:])
        if common < noncommon:
            mid += 1
        elif common > noncommon:
            mid -= 1
        else:
            bool = False
    return mid
    
def calculate_common(X, array):
    if array:
        sum = 0
        for val in array:
            if val == X:
                sum += 1    
        return sum        

def calculate_non_common(X, array):
    if array:
        sum = 0
        for val in array:
            if val != X:
                sum += 1
        return sum        
    
if __name__ == '__main__':
    print solution(5, [5, 5, 1, 7, 2, 3, 5])
