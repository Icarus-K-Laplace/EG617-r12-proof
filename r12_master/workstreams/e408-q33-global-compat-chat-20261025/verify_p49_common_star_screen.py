#!/usr/bin/env python3
"""Screen the exact P_C=49 (R_C=13) boundary using the common-star DP.

Imports the audited gadget and row-pair enumerator from
verify_high_p_common_star.py. This is a diagnostic partial closure, not a
complete P_C=49 proof: it identifies the profiles closed by the existing
common-star argument and the six remaining profile types.
"""
import verify_high_p_common_star as common

EXPECTED_COUNTS = {
    1: (3, 31, 148, 438, 940),
    2: (2, 22, 112, 352, 794),
    3: (2, 22, 112, 352, 794),
    4: (3, 31, 148, 438, 940),
}
EXPECTED_FAILURES = {
    (1, (4, 4, 1, 1, 1, 1, 1)),
    (4, (4, 4, 1, 1, 1, 1, 1)),
    (2, (4, 3, 2, 1, 1, 1, 1)),
    (3, (4, 3, 2, 1, 1, 1, 1)),
}
CLOSED_BY_PAIR_BUDGET = {
    (2, 2, 2, 2, 2, 2, 1),
    (3, 2, 2, 2, 2, 1, 1),
    (3, 3, 2, 2, 1, 1, 1),
    (3, 3, 3, 1, 1, 1, 1),
    (4, 2, 2, 2, 1, 1, 1),
}
UNRESOLVED = {
    (4, 3, 2, 1, 1, 1, 1),
    (4, 4, 1, 1, 1, 1, 1),
    (5, 2, 2, 1, 1, 1, 1),
    (5, 3, 1, 1, 1, 1, 1),
    (6, 2, 1, 1, 1, 1, 1),
    (7, 1, 1, 1, 1, 1, 1),
}


def profiles_upto_13():
    out = set()

    def rec(prefix, slots, remaining, upper):
        if slots == 0:
            if remaining == 0:
                out.add(tuple(prefix))
            return
        largest = min(upper, remaining - (slots - 1))
        for x in range(largest, 0, -1):
            rest = remaining - x
            if rest < slots - 1 or rest > x * (slots - 1):
                continue
            rec(prefix + [x], slots - 1, rest, x)

    for total in range(7, 14):
        rec([], 7, total, 5)
    return sorted(out, key=lambda p: (sum(p), p))


def main():
    profiles = profiles_upto_13()
    boundary = [p for p in profiles if sum(p) == 13]
    assert len(profiles) == 27
    assert len(boundary) == 9
    assert set(boundary) == CLOSED_BY_PAIR_BUDGET | {
        (5, 2, 2, 1, 1, 1, 1),
        (5, 3, 1, 1, 1, 1, 1),
        (4, 3, 2, 1, 1, 1, 1),
        (4, 4, 1, 1, 1, 1, 1),
    }

    failures = set()
    pass_profiles = set(boundary)
    total_transitions = max_states = checks = 0

    for b in range(1, 5):
        vertices, adjacency = common.make_gadget(b)
        K5 = common.cliques(vertices, adjacency, 5)
        pair_data = {
            r: common.row_pair_candidate_masks(vertices, adjacency, K5, r)
            for r in range(1, 6)
        }
        counts = tuple(len(pair_data[r]) for r in range(1, 6))
        assert counts == EXPECTED_COUNTS[b], (b, counts)
        universe = frozenset(
            (di, w)
            for di, D in enumerate(K5)
            for w in vertices
            if w not in D
        )
        masks = {
            r: [mask for _, mask in pair_data[r]]
            for r in range(1, 6)
        }
        for profile in boundary:
            ok, transitions, state_counts, _ = common.verify_profile(
                universe, masks, profile
            )
            checks += 1
            total_transitions += transitions
            if state_counts:
                max_states = max(max_states, max(state_counts))
            if not ok:
                failures.add((b, profile))
                pass_profiles.discard(profile)

    assert checks == 36
    assert failures == EXPECTED_FAILURES, (failures, EXPECTED_FAILURES)
    assert total_transitions == 5021134, total_transitions
    assert max_states == 3329, max_states
    assert pass_profiles == set(boundary) - {
        (4, 3, 2, 1, 1, 1, 1),
        (4, 4, 1, 1, 1, 1, 1),
    }

    for p in CLOSED_BY_PAIR_BUDGET:
        assert all(p[i] + p[j] <= 6 for i in range(7) for j in range(i + 1, 7))

    assert len(UNRESOLVED) == 6
    print("PASS: P_C=49 common-star boundary screen")
    print("all positive 7-part profiles with R_C=13:", len(boundary))
    print("gadget/profile checks:", checks)
    print("DP transitions:", total_transitions)
    print("maximum reachable intersection states:", max_states)
    print("common-star failures:", sorted(failures))
    print("closed by common-star plus pair-budget <=6:", sorted(CLOSED_BY_PAIR_BUDGET))
    print("remaining P_C=49 profiles:", sorted(UNRESOLVED))
    print("Scope: partial colorwise boundary screen only; P_C=49 remains open.")


if __name__ == "__main__":
    main()
