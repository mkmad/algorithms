class Points(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


def check_slope(A, B):
    if (B.y / B.x) == (A.y / A.x):
        return True


def solution(A):
    # write your code in Python 3.6

    if not 1 <= len(A) <= 100000:
        return 0
    rays = 0
    statues = {}
    for i, v in enumerate(A):
        if -1000000000 <= v.x <= 1000000000 and -1000000000 <= v.y <= 1000000000:
            if v.x > 0 and v.y > 0:
                if 1 not in statues:
                    statues[1] = [v]
                    rays += 1
                else:
                    found = False
                    for sv in statues[1]:
                        if check_slope(sv, v):
                            found = True
                            break
                    if not found:
                        rays += 1

            elif v.x > 0 and v.y < 0:
                if 4 not in statues:
                    statues[4] = [v]
                    rays += 1
                else:
                    found = False
                    for sv in statues[4]:
                        if check_slope(sv, v):
                            found = True
                            break
                    if not found:
                        rays += 1

            elif v.x < 0 and v.y > 0:
                if 2 not in statues:
                    statues[2] = [v]
                    rays += 1
                else:
                    found = False
                    for sv in statues[2]:
                        if check_slope(sv, v):
                            found = True
                            break
                    if not found:
                        rays += 1
            else:
                if 4 not in statues:
                    statues[4] = [v]
                    rays += 1
                else:
                    found = False
                    for sv in statues[4]:
                        if check_slope(sv, v):
                            found = True
                            break
                    if not found:
                        rays += 1
        else:
            return 0

    print(rays)


if __name__ == '__main__':
    solution([Points(1, 2), Points(2, 4)])
