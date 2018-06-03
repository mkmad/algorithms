# -*- coding: utf-8 -*-


"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

The sequence should be returned as:

a Results structure (in C), or
a vector of integers (in C++), or
a Results record (in Pascal), or
an array of integers (in any other programming language).
For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Assume that:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
"""

class GenomicRangeQuerySlow(object):

    """
    This solution runs at O(N * M) and has 62% score. So,
    here for every index i at P and Q I take the slice and iterate
    through the slice to get the minimum impact factor. This may lead
    to O(N * M) because the slice may be the entire length of the sequence
    everytime

    """
    @staticmethod
    def solution(S, P, Q):
        impact_factor = {"A": 1, "C": 2, "G": 3, "T": 4}
        res = []
        if 1 <= len(S) <= 100000 and 1 <= len(P) <= 50000 and len(P) == len(Q) and S.isupper():
            for i in range(len(P)):
                if 0 <= P[i] < len(S) and 0 <= Q[i] < len(S):
                    t = S[P[i]: Q[i] + 1]
                    min = None
                    for c in t:
                        if min is None:
                            min = impact_factor[c]
                        else:
                            if impact_factor[c] < min:
                                min = impact_factor[c]
                    res.append(min)

            if res:
                return res


class GenomicRangeQueryFast(object):

    @staticmethod
    def solution(S, P, Q):

        impact_factor = {"A": 1, "C": 2, "G": 3, "T": 4}
        totA = []
        totC = []
        totG = []
        totT = []
        res = []

        if 1 <= len(S) <= 100000 and 1 <= len(P) <= 50000 and len(P) == len(Q) \
                and S.isupper():
            # We build four lists, one for each nucleo, which are as
            # long as the sequence itself.

            # The lists preserve the sequence order and track the sum total
            # of how many times we've seen that nucleo type as we progress
            # through the list.

            # Eg: The sum for "C" in "CAGCCTA" are [0,1,1,1,2,3,3,3]

            for c in S:
                if c == "A":
                    if not totA:
                        totA.append(1)
                    else:
                        totA.append(totA[-1] + 1)
                else:
                    if not totA:
                        totA.append(0)
                    else:
                        totA.append(totA[-1])

                if c == "C":
                    if not totC:
                        totC.append(1)
                    else:
                        totC.append(totC[-1] + 1)
                else:
                    if not totC:
                        totC.append(0)
                    else:
                        totC.append(totC[-1])

                if c == "G":
                    if not totG:
                        totG.append(1)
                    else:
                        totG.append(totG[-1] + 1)
                else:
                    if not totG:
                        totG.append(0)
                    else:
                        totG.append(totG[-1])

                if c == "T":
                    if not totT:
                        totT.append(1)
                    else:
                        totT.append(totT[-1] + 1)
                else:
                    if not totT:
                        totT.append(0)
                    else:
                        totT.append(totT[-1])

            # Each query defines a slice via indicies P and Q which correspond
            # to the start and end points.

            # By comparing the sum at both points we can readily determine how
            # many nucleos of that type appear within them.

            # Eg: In the sum [0,1,1,1,2,3,3,3], at index 2 there is a 1, and at
            # index 4, there is a 2.

            # Thus, somewhere between indexes 2 and 4, there must have been a
            #  nucleo of type 'C'.

            for i in range(len(P)):
                if 0 <= P[i] < len(S) and 0 <= Q[i] < len(S):

                    # check if both the indices are same, if it
                    # is then just append the value
                    if P[i] == Q[i]:
                        res.append(impact_factor[S[P[i]]])
                        continue

                    # check for impact factor in the increasing
                    # order of impact order, since we only care
                    # about the minimum impact order for a given
                    # range of substring

                    # Note: You need to append the impact factor
                    # that's what they are asking
                    if totA[Q[i]] > totA[P[i]]:
                        res.append(impact_factor["A"])
                    elif totC[Q[i]] > totC[P[i]]:
                        res.append(impact_factor["C"])
                    elif totG[Q[i]] > totG[P[i]]:
                        res.append(impact_factor["G"])
                    elif totT[Q[i]] > totT[P[i]]:
                        res.append(impact_factor["T"])
                    else:
                        if len(P) == 1:
                            res.append(impact_factor[S[0]])

            if res:
                return res


if __name__ == '__main__':
    g = GenomicRangeQuerySlow()
    print g.solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
    print g.solution('C', [0], [0])

    g = GenomicRangeQueryFast()
    print g.solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
    print g.solution('A', [0], [0])
