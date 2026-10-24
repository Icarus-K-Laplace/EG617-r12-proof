#!/usr/bin/env python3
"""Round-2 local integer-profile audit for K=8 equality boundaries.

Enumerates exact pair-connector degree equations and R22 charges in:
- c=3 mixed focus;
- c=4 deficits (0,0,2), two-focus overlap;
- c=4 deficits (0,1,1), two-slot U-overlap.

This is a local arithmetic/rectangle relaxation, not a graph generator and not
a SAT/ILP proof. It deliberately does not infer realizability from a surviving
integer profile.
"""

def R22(a, b):
    return a * max(b - 2, 0) + b * max(a - 2, 0)


def profiles(r, geometry, budget=8):
    if geometry == "c3_mixed":
        max_a, max_b, base = r - 2, r - 3, r - 3
        gamma_min, gamma_max = 0, 2
    elif geometry == "c4_002_f2":
        max_a, max_b, base = r - 2, r - 4, r - 4
        gamma_min, gamma_max = 1, 3
    elif geometry == "c4_011_s2":
        max_a, max_b, base = r - 3, r - 3, r - 4
        gamma_min, gamma_max = 1, 3
    else:
        raise ValueError(geometry)

    out = []
    for k in range(budget + 1):
        for gamma in range(gamma_min, gamma_max + 1):
            for n_opposite in range(r - 1):
                total = base + gamma + n_opposite - k
                for a in range(1, max_a + 1):
                    b = total - a
                    if not 1 <= b <= max_b:
                        continue
                    charge = R22(a, b)
                    if k + charge <= budget:
                        out.append((k, gamma, n_opposite, a, b, charge, k + charge))
    return sorted(out)


def main():
    c3_r14 = profiles(14, "c3_mixed")
    expected = set()
    for k in range(9):
        expected.add((k, 0, 0, 1, 10 - k, 8 - k, 8))
        expected.add((k, 0, 0, 10 - k, 1, 8 - k, 8))
    expected.add((6, 0, 0, 2, 3, 2, 8))
    expected.add((6, 0, 0, 3, 2, 2, 8))
    expected.add((7, 0, 0, 2, 2, 0, 7))
    expected.add((8, 0, 1, 2, 2, 0, 8))
    expected.add((8, 1, 0, 2, 2, 0, 8))
    assert set(c3_r14) == expected, (set(c3_r14) - expected, expected - set(c3_r14))

    p15 = profiles(15, "c3_mixed")
    assert p15 == [(8, 0, 0, 2, 2, 0, 8)], p15
    assert profiles(16, "c3_mixed") == []

    for geometry in ("c4_002_f2", "c4_011_s2"):
        p13 = [row for row in profiles(13, geometry) if row[0] <= 1]
        assert all(min(row[3], row[4]) == 1 for row in p13), [
            row for row in p13 if min(row[3], row[4]) != 1
        ]
        p14 = [
            row for row in profiles(14, geometry)
            if row[0] == 0 and row[6] == 8
        ]
        assert {
            (row[3], row[4], row[1], row[2]) for row in p14
        } == {(10, 1, 1, 0), (1, 10, 1, 0)}, (geometry, p14)
        print(
            f"{geometry}: r=13 profiles with k<=1: {len(p13)}; "
            f"r=14 equality profiles: {p14}"
        )

    print(f"c=3 mixed r=14 local profiles with cost <=8: {len(c3_r14)}")
    print("PASS: c=3 r=14 complete profile list, r=15 exceptional profile, r=16 empty.")
    print("LIMITATION: local integer/rectangle profiles only; no full graph H or SAT/ILP search.")


if __name__ == "__main__":
    main()
