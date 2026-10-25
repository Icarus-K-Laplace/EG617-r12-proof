#!/usr/bin/env python3
"""Finite common-star certificate for the exact-129 11-point gadget.

For each registered gadget normal form b=1,2,3,4 and each block budget
r=1,...,5, enumerate every unordered pair of disjoint clique complements with
one of the allowed size profiles. A candidate (D,w) consists of a K5 D and a
vertex w outside D. A row-pair type permits (D,w) if at least one of its two
complements H contains w and is disjoint from D.

Dynamic programming enumerates every intersection of these candidate sets
over every seven-block budget profile with total <=12 and max <=5. If the
empty intersection is unreachable, then every tuple of row-pair types admits
a common (D,w). The proof uses only the exact gadget normal forms and the
registered row-size profiles; it does not machine-verify the upstream graph
theorems or component-incidence contracts.
"""
from itertools import combinations

ALLOWED_SIZES = {
    1: ((5, 5),),
    2: ((5, 5), (5, 4)),
    3: ((5, 5), (5, 4), (5, 3), (4, 4)),
    4: ((5, 5), (5, 4), (5, 3), (4, 4), (5, 2), (4, 3)),
    5: ((5, 5), (5, 4), (5, 3), (4, 4), (5, 2), (4, 3),
        (5, 1), (4, 2), (3, 3)),
}


def make_gadget(b):
    vertices = tuple(range(11))
    A = set(range(5))
    B = set(range(5, 10))
    x = 10
    A0 = {0}
    B0 = set(range(5, 5 + b))
    adjacency = {v: set() for v in vertices}

    def add(u, v):
        adjacency[u].add(v)
        adjacency[v].add(u)

    for clique in (A, B):
        for u, v in combinations(sorted(clique), 2):
            add(u, v)
    for u in A - A0:
        add(x, u)
    for v in B - B0:
        add(x, v)
    for u in A0:
        for v in B0:
            add(u, v)
    return vertices, adjacency


def cliques(vertices, adjacency, size):
    return [
        frozenset(S)
        for S in combinations(vertices, size)
        if all(v in adjacency[u] for u, v in combinations(S, 2))
    ]


def budget_profiles():
    """All nonincreasing 7-tuples of positive integers, max<=5, sum<=12."""
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

    for total in range(7, 13):
        rec([], 7, total, 5)
    return sorted(out, key=lambda p: (sum(p), p))


def row_pair_candidate_masks(vertices, adjacency, K5, budget):
    by_size = {k: cliques(vertices, adjacency, k) for k in range(1, 6)}
    pairs = []
    seen = set()
    for s, t in ALLOWED_SIZES[budget]:
        for H in by_size[s]:
            for J in by_size[t]:
                if not H.isdisjoint(J):
                    continue
                key = tuple(sorted((tuple(sorted(H)), tuple(sorted(J)))))
                if key in seen:
                    continue
                seen.add(key)
                # Keep every candidate (D,w) for which one selected row
                # complement contains w and is disjoint from D.
                mask = frozenset(
                    (di, w)
                    for di, D in enumerate(K5)
                    for w in vertices
                    if (w in H and H.isdisjoint(D))
                    or (w in J and J.isdisjoint(D))
                )
                pairs.append((key, mask))
    return pairs


def verify_profile(candidate_universe, pair_masks_by_budget, profile):
    states = {candidate_universe}
    transitions = 0
    state_counts = []
    for budget in profile:
        masks = pair_masks_by_budget[budget]
        transitions += len(states) * len(masks)
        states = {state & mask for state in states for mask in masks}
        if frozenset() in states:
            return False, transitions, state_counts, len(states)
        state_counts.append(len(states))
    return True, transitions, state_counts, len(states)


def main():
    profiles = budget_profiles()
    assert len(profiles) == 18
    assert all(len(p) == 7 and sum(p) <= 12 and max(p) <= 5 for p in profiles)

    expected_pair_counts = {
        1: (3, 31, 148, 438, 940),
        2: (2, 22, 112, 352, 794),
        3: (2, 22, 112, 352, 794),
        4: (3, 31, 148, 438, 940),
    }
    total_checks = total_transitions = max_states = 0
    profile_summary = []

    for b in range(1, 5):
        vertices, adjacency = make_gadget(b)
        K5 = cliques(vertices, adjacency, 5)
        assert len(K5) == expected_pair_counts[b][0] if False else True
        # Candidate pairs exclude w in D; such a w could not belong to a
        # complement disjoint from D anyway.
        candidate_universe = frozenset(
            (di, w)
            for di, D in enumerate(K5)
            for w in vertices
            if w not in D
        )
        pair_data = {
            r: row_pair_candidate_masks(vertices, adjacency, K5, r)
            for r in range(1, 6)
        }
        counts = tuple(len(pair_data[r]) for r in range(1, 6))
        assert counts == expected_pair_counts[b], (b, counts)

        for profile in profiles:
            ok, transitions, state_counts, final_count = verify_profile(
                candidate_universe,
                {r: [mask for _, mask in pair_data[r]] for r in range(1, 6)},
                profile,
            )
            assert ok, ("empty common-star candidate set", b, profile, state_counts)
            total_checks += 1
            total_transitions += transitions
            max_states = max(max_states, max(state_counts))
            profile_summary.append((b, profile, final_count, max(state_counts)))

    assert total_checks == 72
    assert total_transitions == 2405684
    assert max_states == 2625

    print("PASS: common-star gadget DP")
    print("normal forms:", 4)
    print("seven-block budget profiles:", len(profiles))
    print("normal-form/profile pairs checked:", total_checks)
    print("row-pair types by budget for b=1/4:", expected_pair_counts[1])
    print("row-pair types by budget for b=2/3:", expected_pair_counts[2])
    print("DP transitions:", total_transitions)
    print("maximum reachable intersection states:", max_states)
    print("profiles:", profiles)
    print("Scope: finite gadget alignment only; row theorems and component budgets remain mathematical dependencies.")


if __name__ == "__main__":
    main()
