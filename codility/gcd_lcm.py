def gcd(p, q):
    # Note p > q
    if q == 0:
        return p
    return gcd(q, p % q)


def lcm(p, q):
    return (p * q) / gcd(p, q)



