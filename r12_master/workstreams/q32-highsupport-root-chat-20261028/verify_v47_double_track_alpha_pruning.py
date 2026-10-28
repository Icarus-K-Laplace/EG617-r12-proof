#!/usr/bin/env python3
"""Verify the alpha(R)=3 residual-type list for the 3+7 double-track blocker.

For the registered 18 path/cycle types, alpha is additive across components:
alpha(P_n)=ceil(n/2), alpha(C_n)=floor(n/2), alpha(K1)=1.
A double-track vertex has no R-neighbors, so alpha(R) must be <=3.
"""
types_by_edges = {
    3: [("K1+3P2", [("K",1),("P",2),("P",2),("P",2)])],
    4: [("C3+2K1+P2", [("C",3),("K",1),("K",1),("P",2)]),
        ("K1+P2+P4", [("K",1),("P",2),("P",4)]),
        ("2P2+P3", [("P",2),("P",2),("P",3)])],
    5: [("K1+P6", [("K",1),("P",6)]),
        ("C3+K1+P3", [("C",3),("K",1),("P",3)]),
        ("C4+K1+P2", [("C",4),("K",1),("P",2)]),
        ("P2+P5", [("P",2),("P",5)]),
        ("P3+P4", [("P",3),("P",4)]),
        ("C3+P2+P2", [("C",3),("P",2),("P",2)])],
    6: [("C6+K1", [("C",6),("K",1)]),
        ("2C3+K1", [("C",3),("C",3),("K",1)]),
        ("P7", [("P",7)]),
        ("C3+P4", [("C",3),("P",4)]),
        ("C4+P3", [("C",4),("P",3)]),
        ("C5+P2", [("C",5),("P",2)])],
    7: [("C7", [("C",7)]), ("C3+C4", [("C",3),("C",4)])],
}

def alpha_component(kind, n):
    if kind == "K":
        return 1
    if kind == "P":
        return (n + 1) // 2
    if kind == "C":
        return n // 2
    raise ValueError(kind)

found = {}
for e, entries in types_by_edges.items():
    for name, comps in entries:
        alpha = sum(alpha_component(k, n) for k, n in comps)
        if alpha == 3:
            found.setdefault(e, []).append(name)

expected = {
    5: ["C3+P2+P2"],
    6: ["2C3+K1", "C3+P4", "C5+P2"],
    7: ["C7", "C3+C4"],
}
assert found == expected, (found, expected)
print("alpha(R)=3 types:", found)
print("V47_DOUBLE_TRACK_ALPHA_PRUNING_OK")
print("Scope: residual component alpha arithmetic only; no global Q32 closure.")
