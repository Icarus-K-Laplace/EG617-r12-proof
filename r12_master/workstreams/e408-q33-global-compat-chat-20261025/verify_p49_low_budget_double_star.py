#!/usr/bin/env python3
"""Finite gadget/incidence verifier for the nine P_C=49 profiles with max r_i<=5.

Three proof modes are checked:
1. Basic common-(D,w) DP for the five profiles whose pairwise budgets imply
   p_i+p_j<=4 automatically.
2. Incidence-aware common-(D,w) DP for (5,3,1^5) and (5,2,2,1^4).
3. Fixed-D-family alignment with incidence allocations for (4,4,1^5) and
   (4,3,2,1^4), where the missing-edge blocker analysis forces the restricted
   pair profiles checked below.

The verifier checks the finite 11-vertex gadget and integer incidence
bookkeeping only. The exact-129 factor theorem, row-profile theorem, and
pairwise-blocker implications remain mathematical dependencies.
"""
from functools import lru_cache
from itertools import combinations

ALLOWED_SIZES = {
    1: ((5, 5),),
    2: ((5, 5), (5, 4)),
    3: ((5, 5), (5, 4), (5, 3), (4, 4)),
    4: ((5, 5), (5, 4), (5, 3), (4, 4), (5, 2), (4, 3)),
    5: ((5, 5), (5, 4), (5, 3), (4, 4), (5, 2), (4, 3),
        (5, 1), (4, 2), (3, 3)),
}

P49_SAFE = (
    (4, 2, 2, 2, 1, 1, 1),
    (3, 3, 3, 1, 1, 1, 1),
    (3, 3, 2, 2, 1, 1, 1),
    (3, 2, 2, 2, 2, 1, 1),
    (2, 2, 2, 2, 2, 2, 1),
)
P49_INCIDENCE = (
    (5, 3, 1, 1, 1, 1, 1),
    (5, 2, 2, 1, 1, 1, 1),
)


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


def allowed_pairs(vertices, adjacency, budget):
    by_size = {k: cliques(vertices, adjacency, k) for k in range(1, 6)}
    out, seen = [], set()
    for s, t in ALLOWED_SIZES[budget]:
        for H in by_size[s]:
            for J in by_size[t]:
                if not H.isdisjoint(J):
                    continue
                key = tuple(sorted((tuple(sorted(H)), tuple(sorted(J)))))
                if key not in seen:
                    seen.add(key)
                    out.append((H, J))
    return out


def pair_candidate_masks(vertices, adjacency, K5, budget):
    pairs = allowed_pairs(vertices, adjacency, budget)
    masks = []
    for H, J in pairs:
        masks.append(frozenset(
            (di, w)
            for di, D in enumerate(K5)
            for w in vertices
            if (w in H and H.isdisjoint(D))
            or (w in J and J.isdisjoint(D))
        ))
    return pairs, masks


def verify_basic_profile(b, profile):
    vertices, adjacency = make_gadget(b)
    K5 = cliques(vertices, adjacency, 5)
    candidates = frozenset(
        (di, w) for di, D in enumerate(K5) for w in vertices if w not in D
    )
    pair_masks = {
        r: pair_candidate_masks(vertices, adjacency, K5, r)[1]
        for r in set(profile)
    }
    states = {candidates}
    transitions = 0
    max_states = 1
    for r in profile:
        masks = pair_masks[r]
        transitions += len(states) * len(masks)
        states = {state & mask for state in states for mask in masks}
        if frozenset() in states:
            return False, transitions, max_states
        max_states = max(max_states, len(states))
    return True, transitions, max_states


def incidence_choice_vectors(vertices, adjacency, K5, budget):
    candidates = tuple(
        (di, w) for di, D in enumerate(K5) for w in vertices if w not in D
    )
    vectors = set()
    pairs = allowed_pairs(vertices, adjacency, budget)
    for H, J in pairs:
        overlap = 11 - len(H) - len(J)
        extra_budget = budget - overlap
        for p in range(min(4, extra_budget) + 1):
            for q in range(min(4, extra_budget - p) + 1):
                vals = []
                for di, w in candidates:
                    D = K5[di]
                    eligible = []
                    if w in H and H.isdisjoint(D):
                        eligible.append(p)
                    if w in J and J.isdisjoint(D):
                        eligible.append(q)
                    vals.append(min(eligible) if eligible else 99)
                vectors.add(tuple(vals))
    return candidates, vectors


@lru_cache(maxsize=None)
def cached_incidence_choices(b, budget):
    vertices, adjacency = make_gadget(b)
    K5 = cliques(vertices, adjacency, 5)
    return incidence_choice_vectors(vertices, adjacency, K5, budget)


DEAD = (99, 99)


def update_incidence_state(state, vector):
    out = []
    for old, p in zip(state, vector):
        if old == DEAD or p == 99:
            out.append(DEAD)
            continue
        largest, second = old
        top = max(largest, p)
        runner_up = max(min(largest, p), second)
        if top + runner_up > 4:
            out.append(DEAD)
        else:
            out.append((top, runner_up))
    return tuple(out)


def verify_incidence_profile(b, profile):
    candidates, _ = cached_incidence_choices(b, profile[0])
    choices = {r: cached_incidence_choices(b, r)[1] for r in set(profile)}
    states = {tuple((0, 0) for _ in candidates)}
    transitions = 0
    max_states = 1
    for budget in profile:
        vectors = choices[budget]
        transitions += len(states) * len(vectors)
        new = set()
        for state in states:
            for vector in vectors:
                next_state = update_incidence_state(state, vector)
                # An all-dead state is a counterexample tuple: no common
                # (D,w) permits pairwise partial-incidence sums <=4.
                if not any(value != DEAD for value in next_state):
                    return False, transitions, max_states
                new.add(next_state)
        states = new
        max_states = max(max_states, len(states))
    return True, transitions, max_states


def universal_D_family(b, vertices, adjacency):
    A = set(range(5))
    B = set(range(5, 10))
    x = 10
    A_prime = frozenset((A - {0}) | {x})
    if b == 1:
        family = [frozenset(A), frozenset(B)]
    elif b in (2, 3):
        family = [frozenset(A), frozenset(B), A_prime]
    else:
        family = [A_prime, frozenset(B)]
    return list(dict.fromkeys(family))


def allocations(H, J, r):
    overlap = 11 - len(H) - len(J)
    extra_budget = r - overlap
    return [
        (p, q)
        for p in range(min(4, extra_budget) + 1)
        for q in range(min(4, extra_budget - p) + 1)
    ]


def verify_44_profile(b):
    """The missing-edge branch forces both r=4 pair types to be 55 or 54."""
    vertices, adjacency = make_gadget(b)
    Ds = universal_D_family(b, vertices, adjacency)
    pairs55 = allowed_pairs(vertices, adjacency, 1)
    pairs54 = []
    by = {k: cliques(vertices, adjacency, k) for k in range(1, 6)}
    seen = set()
    for H in by[5]:
        for J in by[4]:
            if H.isdisjoint(J):
                key = tuple(sorted((tuple(sorted(H)), tuple(sorted(J)))))
                if key not in seen:
                    seen.add(key)
                    pairs54.append((H, J))
    pairs = pairs55 + pairs54
    checks = 0
    for P in pairs:
        for Q in pairs:
            for p, p2 in allocations(P[0], P[1], 4):
                for q, q2 in allocations(Q[0], Q[1], 4):
                    checks += 1
                    found = False
                    for D in Ds:
                        for H, ph in ((P[0], p), (P[1], p2)):
                            if not H.isdisjoint(D):
                                continue
                            for J, qh in ((Q[0], q), (Q[1], q2)):
                                if (J.isdisjoint(D) and H.intersection(J)
                                        and ph + qh <= 4):
                                    found = True
                                    break
                            if found:
                                break
                        if found:
                            break
                    if not found:
                        return False, checks
    return True, checks


def verify_432_profile(b):
    """The missing-edge branch forces row-pair types 55, 55, and 55/54."""
    vertices, adjacency = make_gadget(b)
    Ds = universal_D_family(b, vertices, adjacency)
    pairs55 = allowed_pairs(vertices, adjacency, 1)
    pairs2 = allowed_pairs(vertices, adjacency, 2)
    checks = 0
    for P in pairs55:
        for p, p2 in allocations(P[0], P[1], 4):
            for Q in pairs55:
                for q, q2 in allocations(Q[0], Q[1], 3):
                    for R in pairs2:
                        for x, y in allocations(R[0], R[1], 2):
                            checks += 1
                            found = False
                            for D in Ds:
                                for H, ph in ((P[0], p), (P[1], p2)):
                                    if not H.isdisjoint(D):
                                        continue
                                    for J, qh in ((Q[0], q), (Q[1], q2)):
                                        if not J.isdisjoint(D) or ph + qh > 4:
                                            continue
                                        for K, kh in ((R[0], x), (R[1], y)):
                                            if (K.isdisjoint(D)
                                                    and ph + kh <= 4
                                                    and qh + kh <= 4
                                                    and H.intersection(J)
                                                    and H.intersection(K)
                                                    and J.intersection(K)):
                                                found = True
                                                break
                                        if found:
                                            break
                                    if found:
                                        break
                                if found:
                                    break
                            if not found:
                                return False, checks
    return True, checks


def main():
    # Five profiles with pairwise budget sums <=6: every pair has
    # p_i+p_j <= (r_i-1)+(r_j-1) <=4.
    basic_checks = basic_transitions = basic_max_states = 0
    for b in range(1, 5):
        for profile in P49_SAFE:
            ok, transitions, max_states = verify_basic_profile(b, profile)
            assert ok, ("basic common-star failure", b, profile)
            basic_checks += 1
            basic_transitions += transitions
            basic_max_states = max(basic_max_states, max_states)
    assert basic_checks == 20
    assert basic_transitions == 2779700
    assert basic_max_states == 3077

    # The two high profiles require the incidence-aware state, because
    # their largest block-pair budgets can exceed four.
    incidence_checks = incidence_transitions = incidence_max_states = 0
    for b in range(1, 5):
        for profile in P49_INCIDENCE:
            ok, transitions, max_states = verify_incidence_profile(b, profile)
            assert ok, ("incidence common-star failure", b, profile)
            incidence_checks += 1
            incidence_transitions += transitions
            incidence_max_states = max(incidence_max_states, max_states)
    assert incidence_checks == 8
    assert incidence_transitions == 5343724
    assert incidence_max_states == 27714

    # The remaining two low-budget profiles are handled by fixed-D-family
    # alignments. All selected complements have size at least four, so any
    # two disjoint from D intersect inside the six-set U\\D.
    align44_checks = align432_checks = 0
    for b in range(1, 5):
        ok, checks = verify_44_profile(b)
        assert ok, ("(4,4,1^5) alignment failure", b)
        align44_checks += checks
        ok, checks = verify_432_profile(b)
        assert ok, ("(4,3,2,1^4) alignment failure", b)
        align432_checks += checks
    assert align44_checks == 117608
    assert align432_checks == 52440

    print("PASS: P_C=49 low-budget double-star verifier")
    print("basic common-star: 20 form/profile cases,", basic_transitions,
          "DP transitions; max states", basic_max_states)
    print("incidence-aware common-star: 8 form/profile cases,",
          incidence_transitions, "DP transitions; max states", incidence_max_states)
    print("fixed-D (4,4,1^5) incidence alignments:", align44_checks)
    print("fixed-D (4,3,2,1^4) incidence alignments:", align432_checks)
    print("Total form/profile families checked:", basic_checks + incidence_checks + 8)
    print("Scope: excludes all P_C=49 profiles with max r_i<=5; r=(6,2,1^5) and r=(7,1^6) are outside this script.")


if __name__ == "__main__":
    main()
