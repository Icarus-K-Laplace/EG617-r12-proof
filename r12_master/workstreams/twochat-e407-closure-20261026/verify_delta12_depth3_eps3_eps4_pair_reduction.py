#!/usr/bin/env python3
"""Arithmetic audit for DELTA12_DEPTH3_EPS3_EPS4_PAIR_REDUCTION.md.

This checks only the exceptional-pair degree/excess/restored-incidence cases and
minimum two-component cover sizes. The registered 309-edge equality model and
analytic pair-cover lemmas are inputs, not re-proved here.
"""


def allowed(eps, restored):
    out = []
    for ex in range(eps + 1):
        for inc in range(7):
            if restored and inc < 2:
                continue
            s = 5 + ex - inc
            if s < 6:  # low-W-degree lemma: both exceptional vertices have degree >=3
                continue
            if not restored and s < 8:  # pair-cover lemma for eps=3/4 profiles
                continue
            out.append((s, ex, inc))
    return sorted(set(out))


def main():
    # epsilon=3
    assert allowed(3, False) == [(8, 3, 0)]
    assert allowed(3, True) == [(6, 3, 2)]

    # epsilon=4
    assert allowed(4, False) == [
        (8, 3, 0),
        (8, 4, 1),
        (9, 4, 0),
    ]
    assert allowed(4, True) == [
        (6, 3, 2),
        (6, 4, 3),
        (7, 4, 2),
    ]

    # Minimum two-component covers in all live W profiles.
    profiles_eps3 = [(3,5,5,5), (4,4,4,6), (4,4,5,5)]
    profiles_eps4 = [(4,4,5,5)]
    assert all(sum(sorted(p)[:2]) == 8 for p in profiles_eps3)
    assert all(sum(sorted(p)[:2]) == 8 for p in profiles_eps4)

    print("DELTA12_DEPTH3_EPS3_EPS4_PAIR_REDUCTION_OK")
    print("eps3 nonrestored/restored:", allowed(3,False), allowed(3,True))
    print("eps4 nonrestored/restored:", allowed(4,False), allowed(4,True))
    print("Scope: arithmetic only; analytic equality/pair-cover inputs are external to this verifier.")


if __name__ == "__main__":
    main()
