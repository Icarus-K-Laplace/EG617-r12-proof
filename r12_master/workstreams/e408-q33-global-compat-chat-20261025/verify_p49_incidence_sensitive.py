#!/usr/bin/env python3
"""Incidence-sensitive common-star proof screen for two P_C=49 profiles.

The selected row's partial component incidence p is bounded by
p_H+p_J <= r-a, where a=11-|H|-|J|. For each row-pair type, the verifier
filters candidate (D,w) stars by incidence thresholds. It then checks every
tuple of row-pair types and all allowed partial-incidence allocations.

This is a finite conditional proof certificate for the two listed profiles.
It depends on the exact-129 row-profile theorem and four gadget normal forms.
"""
from itertools import combinations
import verify_high_p_common_star as common


def incidence_types(b, budget, thresholds):
    vertices, adjacency = common.make_gadget(b)
    K5 = common.cliques(vertices, adjacency, 5)
    by_size = {k: common.cliques(vertices, adjacency, k) for k in range(1, 6)}
    seen, out = set(), []
    for s, t in common.ALLOWED_SIZES[budget]:
        for H in by_size[s]:
            for J in by_size[t]:
                if not H.isdisjoint(J):
                    continue
                key = tuple(sorted((tuple(sorted(H)), tuple(sorted(J)))))
                if key in seen:
                    continue
                seen.add(key)
                Hc, Jc = frozenset(key[0]), frozenset(key[1])
                a = 11 - len(Hc) - len(Jc)
                for pH in range(budget - a + 1):
                    for pJ in range(budget - a - pH + 1):
                        masks = []
                        for threshold in thresholds:
                            mask = frozenset(
                                (di, w)
                                for di, D in enumerate(K5)
                                for w in vertices
                                if (pH <= threshold and w in Hc and Hc.isdisjoint(D))
                                or (pJ <= threshold and w in Jc and Jc.isdisjoint(D))
                            )
                            masks.append(mask)
                        out.append((key, pH, pJ, a, tuple(masks)))
    return out


def replay(b, profile, threshold_modes):
    vertices, adjacency = common.make_gadget(b)
    K5 = common.cliques(vertices, adjacency, 5)
    universe = frozenset(
        (di, w)
        for di, D in enumerate(K5)
        for w in vertices
        if w not in D
    )
    type_data = {
        r: incidence_types(b, r, [mode[r] for mode in threshold_modes])
        for r in set(profile)
    }
    initial = tuple(universe for _ in threshold_modes)
    states = {initial}
    transitions = max_states = 1
    state_counts = []
    empty = tuple(frozenset() for _ in threshold_modes)

    for budget in profile:
        new_states = set()
        for state in states:
            for _, _, _, _, masks in type_data[budget]:
                new_states.add(
                    tuple(state[k] & masks[k] for k in range(len(threshold_modes)))
                )
                transitions += 1
        states = new_states
        state_counts.append(len(states))
        max_states = max(max_states, len(states))
        assert empty not in states, ("no admissible common star", b, profile, state_counts)

    return transitions - 1, max_states, state_counts


def main():
    # Profile (5,2,2,1^4): every row pair can be filtered at p<=3 in
    # the r=5 block, p<=1 in r=2 blocks, and p=0 in r=1 blocks.
    profile_522 = (5, 2, 2, 1, 1, 1, 1)
    modes_522 = [{5: 3, 2: 1, 1: 0}]
    expected_522 = {
        1: (173512, 3329),
        2: (78362, 1937),
        3: (78362, 1937),
        4: (173512, 3329),
    }
    for b in range(1, 5):
        got = replay(b, profile_522, modes_522)
        assert got[:2] == expected_522[b], (b, got[:2], expected_522[b])

    # Profile (5,3,1^5): one of three incidence modes must work:
    # (p5<=2,p3<=2), or (p5<=3,p3<=1), or (p5<=4,p3=0).
    profile_531 = (5, 3, 1, 1, 1, 1, 1)
    modes_531 = [
        {5: 2, 3: 2, 1: 0},
        {5: 3, 3: 1, 1: 0},
        {5: 4, 3: 0, 1: 0},
    ]
    expected_531 = {
        1: (475799, 16860),
        2: (233080, 10009),
        3: (233080, 10009),
        4: (475799, 16860),
    }
    for b in range(1, 5):
        got = replay(b, profile_531, modes_531)
        assert got[:2] == expected_531[b], (b, got[:2], expected_531[b])

    print("PASS: incidence-sensitive P_C=49 profile screen")
    print("profile (5,2,2,1^4): four forms checked, 503748 transitions")
    print("profile (5,3,1^5): four forms checked, 1417758 transitions")
    print("total transitions:", 503748 + 1417758)
    print("all states retained at least one admissible common-star mode")
    print("Scope: closes these two budget profiles conditionally; four P_C=49 profiles remain open.")


if __name__ == "__main__":
    main()
