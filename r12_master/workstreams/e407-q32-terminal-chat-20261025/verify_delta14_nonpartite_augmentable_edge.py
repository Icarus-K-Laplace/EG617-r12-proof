#!/usr/bin/env python3
"""Finite arithmetic replay for the delta-14 augmentable-edge reduction.

This checks only the exact integer degree equations and component-saturation
thresholds stated in DELTA14_NONPARTITE_AUGMENTABLE_EDGE_REDUCTION.md. It does
not verify the upstream core reduction, Brouwer/Kang--Pikhurko theorems, or
graph realizability.
"""
from itertools import product

# (name, component sizes, number of cross edges, minimum W-degree if
# not component-saturated). For no-cross-edge profiles, unsaturation is
# impossible and the last field is None.
PROFILES = {
    0: [
        ("4455+2cross", (4, 4, 5, 5), 2, 5),
        ("3555+1cross", (3, 5, 5, 5), 1, 6),
        ("4446+1cross", (4, 4, 4, 6), 1, 6),
        ("3456", (3, 4, 5, 6), 0, None),
    ],
    1: [
        ("3555", (3, 5, 5, 5), 0, None),
        ("4446", (4, 4, 4, 6), 0, None),
        ("4455+1cross", (4, 4, 5, 5), 1, 6),
    ],
    2: [
        ("4455", (4, 4, 5, 5), 0, None),
    ],
}


def status_allowed(status, degree, min_component, cross_count, unsat_min):
    if status == "sat":
        return degree >= min_component
    return cross_count > 0 and unsat_min is not None and degree >= unsat_min


def main():
    feasible = []
    for eps_u, profiles in PROFILES.items():
        for name, sizes, cross_count, unsat_min in profiles:
            min_component = min(sizes)
            for a in range(1, 7):
                for eps_x, eps_y in product(range(eps_u + 1), repeat=2):
                    if eps_x + eps_y > eps_u:
                        continue
                    for ix, iy in product((0, 1), repeat=2):
                        dx = a - 1 + eps_x - ix
                        dy = 6 - a + eps_y - iy
                        for sx, sy in product(("sat", "unsat"), repeat=2):
                            if (
                                status_allowed(sx, dx, min_component, cross_count, unsat_min)
                                and status_allowed(sy, dy, min_component, cross_count, unsat_min)
                            ):
                                feasible.append(
                                    (eps_u, name, a, eps_x, eps_y, ix, iy, dx, dy, sx, sy)
                                )

    expected = [
        (1, "3555", 3, 1, 0, 0, 0, 3, 3, "sat", "sat"),
        (1, "3555", 4, 0, 1, 0, 0, 3, 3, "sat", "sat"),
    ]
    assert feasible == expected, (feasible, expected)
    print("PASS: only two integer terminals survive the relaxed degree/saturation system.")
    print("PASS: both have eps_U=1, W=K3+3K5, d_W(x)=d_W(y)=3, I_x=I_y=0.")
    print("PASS: the surviving (a,eps_x,eps_y) triples are (3,1,0) and (4,0,1).")
    print("Scope: arithmetic replay only; not a graph-realization certificate.")


if __name__ == "__main__":
    main()
