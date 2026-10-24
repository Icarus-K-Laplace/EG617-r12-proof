#!/usr/bin/env python3
"""Arithmetic/profile verifier for the universal E408 Q33 S0>=12 note.

Checks the finite degree profiles and incidence counts in the proof. It does
not certify graph-theoretic clique/independence arguments or the T61 contracts.
"""
from math import comb


def main() -> None:
    # At S0=11, e_H(U,W)=125 and each W-neighbourhood has size >=7.
    assert 114 + 11 == 125
    assert 128 - 125 == 3
    assert 125 - 3 * 7 == 104 == 13 * 8
    assert 125 - 4 * 7 == 97 == 11 * 8 + 9

    # Finite T-incidence cases under the zero-excess vertex capacity.
    # (N7, q9 T-intersection b, #q8 T-type a, eps_T,
    #  #R-only q8 sets, special R-incidences, E_R, total s-incidences)
    cases = [
        (3, None, 3, 0, 10, 3, 11, 80),
        (4, 7, 1, 0, 10, 3, 11, 80),
        (4, 1, 2, 1, 9, 10, 10, 72),
        (4, 0, 2, 0, 9, 11, 11, 72),
    ]
    for k, b, a, eps_t, n_sets, special, e_r, total_s in cases:
        if k == 3:
            assert eps_t == 7 * a - 21
        else:
            assert eps_t == 7 * a + b - 14
        assert total_s == 72 + e_r - special
        assert total_s == 8 * n_sets
        assert 24 + e_r <= 35
    assert cases[0][2:4] == (3, 0)
    assert cases[1][2:4] == (1, 0)
    assert cases[2][2:4] == (2, 1)
    assert cases[3][2:4] == (2, 0)

    # If t distinct 8-sets have pairwise intersections <=1, union lower
    # bounds rule out t>=4 on a 24-point set.
    union_lower = {t: 8 * t - comb(t, 2) for t in range(4, 11)}
    assert union_lower == {4: 26, 5: 30, 6: 33, 7: 35, 8: 36, 9: 36, 10: 35}
    assert all(n > 24 for n in union_lower.values())

    # Multiplicity patterns under sum 10 / sum 9 and max multiplicity 4.
    pats10 = []
    for x in range(1, 5):
        for y in range(x, 5):
            for z in range(y, 5):
                if x + y + z == 10:
                    pats10.append((x, y, z))
    pats9 = []
    for x in range(1, 5):
        for y in range(x, 5):
            for z in range(y, 5):
                if x + y + z == 9:
                    pats9.append((x, y, z))
    assert pats10 == [(2, 4, 4), (3, 3, 4)]
    assert pats9 == [(1, 4, 4), (2, 3, 4), (3, 3, 3)]

    # Special-incidence contradictions:
    # multiplicity 2 needs >=8 special incidences; multiplicity 1 needs >=16.
    assert 3 < 8
    assert 10 < 16 and 11 < 16

    # Pair-counting transversal intersection limits:
    # if a q-set and an 8-transversal differ, with d common partitions,
    # then their intersection s satisfies s <= q-d.
    assert 8 - 7 == 1  # distinct 8-transversals across all seven partitions
    assert 8 - 6 == 2  # 8-set across six partitions
    assert 9 - 7 == 2  # 9-set across all seven partitions

    # Final clique contradiction: K8 joined to K4, or K8 joined to K3 plus y.
    assert 8 + 4 == 12 > 11
    assert 8 + 3 + 1 == 12 > 11
    print("E408_Q33_UNIVERSAL_S0_12_ARITHMETIC_OK")
    print("Scope: arithmetic and finite case tables only; proof remains in theorem note.")


if __name__ == "__main__":
    main()
