"""
https://stackoverflow.com/questions/10670379/find-xor-of-all-numbers-in-a-given-range

I have not analysed this solution
"""


def bitwisexor_0_to_a(a):
    list = [a, 1, a + 1, 0]
    return list[a % 4]


def solution(M, N):
    return bitwisexor_0_to_a(N) ^ bitwisexor_0_to_a(M-1)
