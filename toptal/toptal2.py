# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

visited = set()
total = 0
def solution(A, B):
    # write your code in Python 2.7
    navigate(0, 0, A, B, sum=0)
    if total == 0:
        return -1
    if sum >= 100000000:
        return -2
    else:
        print sum

def possible_paths(x, y):
    paths = [ 
      (2, 1),
      (1, 2),
      (-1, 2),
      (-2, 1),
      (-1, -2),
      (-2, -1),
      (1, -2),
      (2, -1) 
    ]
    possibilities = []
    for val in paths:
        possibilities.append((x + val[0], y + val[1]))
    print possibilities
    return possibilities
    
def navigate(x, y, A, B, sum=0):
    sum += 1
    if x == A and y == B:
        total = sum
        return   
    if abs(x - A) == 1 or abs(y - B) == 1:
        # Cannot Reach
        return
    poss = possible_paths(x, y)
    for val in poss:
        if (val[0], val[1]) in visited:
            continue
        else:
            visited.add((val[0], val[1]))
            navigate(val[0], val[1], A, B, sum)

if __name__ == '__main__':
    solution(4,5)
