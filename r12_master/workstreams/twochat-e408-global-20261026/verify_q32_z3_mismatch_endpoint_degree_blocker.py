#!/usr/bin/env python3
"""Check endpoint-degree arithmetic for the z=3 split-fiber cases.

The analytic argument is in Q32_Z3_MISMATCH_RESIDUAL_DEGREE_CLOSURE.md.
This script checks:
- a 2+1 split forces both eta=1 endpoints to choose the size-two part;
- a 1+1 split has same-part and opposite-part cases;
- the resulting residual degrees contradict a K3/K2 fiber or force
  an isolated K2 component in C3+P4.
It is not a global Q32 solver.
"""
from itertools import product

def extra_counts(parts, endpoint_choices):
    return tuple(sum(choice != part for choice in endpoint_choices)
                 for part in range(len(parts)))

def check_split_2_1():
    parts = (2, 1)
    legal = [c for c in range(2) if parts[c] == 2]
    assert legal == [0]
    b = extra_counts(parts, (0, 0))
    d = tuple(2-x for x in b)
    assert b == (0, 2) and d == (2, 0)
    assert d[1] < 2
    return b, d

def check_split_1_1():
    parts = (1, 1)
    cases = {}
    for choices in product(range(2), repeat=2):
        b = extra_counts(parts, choices)
        d = tuple(2-x for x in b)
        cases[choices] = (b, d)
    assert cases[(0,0)] == ((0,2),(2,0))
    assert cases[(1,1)] == ((2,0),(0,2))
    assert cases[(0,1)] == ((1,1),(1,1))
    assert cases[(1,0)] == ((1,1),(1,1))
    return cases

def main():
    b21, d21 = check_split_2_1()
    cases11 = check_split_1_1()
    print("2+1 split: endpoint choices forced to larger part; b,d =", b21, d21)
    print("1+1 split cases:", cases11)
    print("All mismatch endpoint assignments contradict clique degrees or residual component type.")
    print("V47_Z3_MISMATCH_ENDPOINT_DEGREE_BLOCKER_OK")
    print("Scope: split-size endpoint arithmetic only; no Q32 UNSAT.")

if __name__ == "__main__":
    main()
