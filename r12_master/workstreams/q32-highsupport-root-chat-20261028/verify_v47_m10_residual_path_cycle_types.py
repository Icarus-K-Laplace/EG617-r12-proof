#!/usr/bin/env python3
"""Enumerate the 7-vertex path/cycle residual types in the m=10 split cases.

This is a finite graph-type regression for the proved conditions:
  |R|=7, Delta(H[R])<=2, alpha(H[R])<=4,
  clique_cover(H[R])<=4, e(H[R])=3+z with z in {0,...,4}.
It verifies the path/cycle type list only; it does not prove the split-case
hypotheses or certify the full-support Q32 branch impossible.
"""
from collections import defaultdict

# Component type: (kind, n), with K1, paths P_n (n>=2), cycles C_n (n>=3).
def component_metrics(kind, n):
    if kind == "K":
        assert n == 1
        return 0, 1, 1
    if kind == "P":
        return n - 1, (n + 1) // 2, (n + 1) // 2
    if kind == "C":
        return n, n // 2, (n + 1) // 2
    raise ValueError(kind)

types = [("K", 1)]
types += [("P", n) for n in range(2, 8)]
types += [("C", n) for n in range(3, 8)]
types.sort(key=lambda t: (t[1], {"K": 0, "P": 1, "C": 2}[t[0]]))

found = defaultdict(list)

def rec(start, vertices, edges, alpha, cover, chosen):
    if vertices == 7:
        if 3 <= edges <= 7 and alpha <= 4 and cover <= 4:
            sig = tuple(chosen)
            found[edges].append(sig)
        return
    if vertices > 7:
        return
    for i in range(start, len(types)):
        kind, n = types[i]
        if vertices + n > 7:
            continue
        e, a, c = component_metrics(kind, n)
        if edges + e > 7:
            continue
        rec(i, vertices+n, edges+e, alpha+a, cover+c, chosen+[f"{kind}{n}"])

rec(0, 0, 0, 0, 0, [])

expected = {
    3: [("K1", "P2", "P2", "P2")],
    4: [("C3", "K1", "K1", "P2"), ("K1", "P2", "P4"), ("P2", "P2", "P3")],
    5: [("K1", "P6"), ("C3", "K1", "P3"), ("C4", "K1", "P2"),
        ("P2", "P5"), ("P3", "P4"), ("C3", "P2", "P2")],
    6: [("C6", "K1"), ("C3", "C3", "K1"), ("P7",),
        ("C3", "P4"), ("C4", "P3"), ("C5", "P2")],
    7: [("C7",), ("C3", "C4")],
}
for e in sorted(found):
    got = sorted(tuple(sig) for sig in found[e])
    want = sorted(expected[e])
    assert got == want, (e, got, want)
    print(f"e(R)={e}, z={e-3}, y={8-2*(e-3)}: {len(got)} types")
    for sig in got:
        print("  " + " + ".join(sig))

assert sum(map(len, found.values())) == 18
print("V47_M10_RESIDUAL_PATH_CYCLE_TYPES_OK")
print("Scope: graph-type enumeration under stated residual constraints only.")
