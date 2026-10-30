#!/usr/bin/env python3
"""Check only the normalized 4,5,5 switch label pattern.

RETRACTION NOTICE: this script does NOT prove q is adjacent to residual
vertices in the transposed partner fiber. Shared neighbors do not imply
adjacency. It must not be cited as a partner-degree blocker.
"""
from itertools import combinations

def normalized_switch(s, j):
    assert s != j
    sigma = list(range(4))
    sigma[s], sigma[j] = sigma[j], sigma[s]
    labels = {}
    for t in range(4):
        labels[t] = {
            "A": {t} | ({s} if t == j else set()),
            "B": {t} | ({s} if t == j else set()),
            "C": {sigma[t]} | ({s} if t == s else set()),
        }
    k = {t: (2 if t == j else 1 if t == s else 0) for t in range(4)}
    for t in range(4):
        common = set.intersection(*labels[t].values())
        if t == j:
            assert common == {s}
            assert j in labels[t]["A"] and j in labels[t]["B"]
            assert k[t] == 2
        elif t == s:
            assert common == {s}
            assert j in labels[t]["C"]
            assert k[t] == 1
        else:
            assert common == {t}
            assert k[t] == 0
    return labels, k

def main():
    cases = 0
    for a, b in combinations(range(4), 2):
        for s, j in ((a, b), (b, a)):
            labels, k = normalized_switch(s, j)
            assert k[j] == 2 and j in labels[j]["A"] and j in labels[j]["B"]
            cases += 1
    assert cases == 12
    print("NORMALIZED_SWITCH_LABEL_PATTERN_OK:", cases)
    print("NO_RESIDUAL_ADJACENCY_CONCLUSION: shared neighbors do not imply adjacency")

if __name__ == "__main__":
    main()
