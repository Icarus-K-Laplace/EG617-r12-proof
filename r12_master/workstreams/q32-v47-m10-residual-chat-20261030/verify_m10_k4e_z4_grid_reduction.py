#!/usr/bin/env python3
"""Independent finite verifier for the M10 4+6, K4-e, Z=4 reduction.

Checks the residual-map pair/triple necessary catalog on C7 and C3+C4,
all cuts of K6 minus a perfect matching, and the corrected 5,5,5 endpoint
branch used in the global proof. This is not a full grid or Q32 solver.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations, product

V = tuple(range(7))
LABELS = tuple(range(4))
PERMS = tuple(permutations(LABELS))


def cycle_edges(cycle):
    return {
        tuple(sorted((cycle[i], cycle[(i + 1) % len(cycle)])))
        for i in range(len(cycle))
    }


RESIDUALS = {
    "C7": cycle_edges(list(range(7))),
    "C3+C4": cycle_edges([0, 1, 2]) | cycle_edges([3, 4, 5, 6]),
}


def profile(f):
    return tuple(sorted(Counter(f).values(), reverse=True))


def empty_label(f):
    return next((x for x in LABELS if x not in f), None)


def partition(f):
    return frozenset(
        frozenset(v for v, c in enumerate(f) if c == lab)
        for lab in set(f)
    )


def is_clique_fiber_map(f, edges):
    fibers = defaultdict(list)
    for v, lab in enumerate(f):
        fibers[lab].append(v)
    return all(
        tuple(sorted((u, v))) in edges
        for fiber in fibers.values()
        for u, v in combinations(fiber, 2)
    )


def independent_sets(edges, size):
    return [
        S for S in combinations(V, size)
        if all(
            tuple(sorted((u, v))) not in edges
            for u, v in combinations(S, 2)
        )
    ]


def aligns(f, g, p):
    return all(g[v] == p[f[v]] for v in V)


def required_extra(f, g, p, independent_pairs, independent_triples):
    """Return None, ('free',None), or ('fixed',(a,b)).

    The outer block is normalized by p^{-1}. Independent pairs require a
    matching of size two on the two-by-two available subgraph; independent
    triples require the two remaining vertices to be adjacent.
    """
    h = tuple(p.index(g[v]) for v in V)
    all_labels = set(LABELS)
    required = None

    for r, s in independent_pairs:
        U = all_labels - {f[r], f[s]}
        W = all_labels - {h[r], h[s]}
        if U == W:
            continue
        if len(U - W) == 1 and len(W - U) == 1:
            edge = (next(iter(U - W)), next(iter(W - U)))
            if required is not None and required != edge:
                return None
            required = edge
        else:
            return None

    for S in independent_triples:
        U = all_labels - {f[v] for v in S}
        W = all_labels - {h[v] for v in S}
        if len(U) != 1 or len(W) != 1:
            return None
        a, b = next(iter(U)), next(iter(W))
        if a != b:
            edge = (a, b)
            if required is not None and required != edge:
                return None
            required = edge

    return ("free", None) if required is None else ("fixed", required)


def map_pair_states(f, g, edges, independent_pairs, independent_triples):
    return {
        p: req
        for p in PERMS
        if (req := required_extra(
            f, g, p, independent_pairs, independent_triples
        )) is not None
    }


def verify_residual(name, edges):
    independent_pairs = independent_sets(edges, 2)
    independent_triples = independent_sets(edges, 3)
    maps = [
        f for f in product(LABELS, repeat=7)
        if is_clique_fiber_map(f, edges)
    ]
    profiles = Counter(profile(f) for f in maps)
    compatible_pairs = 0
    cell_states = 0
    categories = Counter()

    for f in maps:
        for g in maps:
            states = map_pair_states(
                f, g, edges, independent_pairs, independent_triples
            )
            if not states:
                continue

            compatible_pairs += 1
            cell_states += sum(
                12 if req[0] == "free" else 1
                for req in states.values()
            )

            zf, zg = empty_label(f), empty_label(g)
            p0 = [p for p in PERMS if aligns(f, g, p)]

            if zf is None and zg is None:
                if p0:
                    assert len(p0) == 1
                    assert set(states) == {p0[0]}
                    assert states[p0[0]] == ("free", None)
                    categories["full-aligned"] += 1
                else:
                    assert len(states) == 1
                    assert next(iter(states.values()))[0] == "fixed"
                    categories["full-nonaligned"] += 1

            elif zf is not None and zg is None:
                assert len(states) == 2
                assert all(
                    req[0] == "fixed" and req[1][0] == zf
                    for req in states.values()
                )
                categories["F-empty/G-full"] += 1

            elif zf is None and zg is not None:
                assert len(states) == 2
                assert all(
                    req[0] == "fixed" and req[1][1] == p.index(zg)
                    for p, req in states.items()
                )
                categories["F-full/G-empty"] += 1

            else:
                assert partition(f) == partition(g)
                assert len(p0) == 1
                p_align = p0[0]
                assert len(states) == 4
                assert states[p_align] == ("free", None)
                z = zf

                for p, req in states.items():
                    if p == p_align:
                        continue
                    relative = tuple(
                        p_align.index(p[x]) for x in LABELS
                    )
                    matching_k = []
                    for k in LABELS:
                        if k == z:
                            continue
                        transposition = tuple(
                            k if x == z else z if x == k else x
                            for x in LABELS
                        )
                        if (
                            relative == transposition
                            and req == ("fixed", (z, k))
                        ):
                            matching_k.append(k)
                    assert len(matching_k) == 1
                categories["both-empty/same-partition"] += 1

    if name == "C7":
        assert len(maps) == 168
        assert profiles == Counter({(2, 2, 2, 1): 168})
        assert compatible_pairs == 12096
        assert cell_states == 56448
        assert categories == Counter({
            "full-aligned": 4032,
            "full-nonaligned": 8064,
        })
    else:
        assert len(maps) == 288
        assert profiles == Counter({
            (3, 2, 2): 48,
            (3, 2, 1, 1): 96,
            (2, 2, 2, 1): 144,
        })
        assert compatible_pairs == 29952
        assert cell_states == 120960
        assert categories == Counter({
            "both-empty/same-partition": 1152,
            "F-empty/G-full": 5760,
            "F-full/G-empty": 5760,
            "full-aligned": 5760,
            "full-nonaligned": 11520,
        })

    return {
        "maps": len(maps),
        "profiles": dict(profiles),
        "compatible_map_pairs": compatible_pairs,
        "pair_triple_cell_states": cell_states,
        "categories": dict(categories),
    }


def perfect_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    x = items[0]
    for y in items[1:]:
        rest = tuple(z for z in items[1:] if z != y)
        for tail in perfect_matchings(rest):
            yield ((x, y),) + tail


def cut_component_sizes(S, matching):
    S = set(S)
    T = set(range(6)) - S
    heavy = {frozenset(edge) for edge in matching}
    adjacency = {x: set() for x in range(6)}
    for a in S:
        for b in T:
            if frozenset((a, b)) not in heavy:
                adjacency[a].add(b)
                adjacency[b].add(a)

    unseen = set(range(6))
    sizes = []
    while unseen:
        start = next(iter(unseen))
        seen = set()
        stack = [start]
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            stack.extend(adjacency[x] - seen)
        sizes.append(len(seen))
        unseen -= seen
    return sorted(sizes, reverse=True)


def verify_outer_cuts():
    matchings = list(perfect_matchings(range(6)))
    assert len(matchings) == 15
    connected = 0
    one_isolate = 0

    for M in matchings:
        for size in (2, 3, 4):
            for S in combinations(range(6), size):
                assert cut_component_sizes(S, M) == [6]
                connected += 1
        for size in (1, 5):
            for S in combinations(range(6), size):
                assert cut_component_sizes(S, M) == [5, 1]
                one_isolate += 1

    assert connected == 750
    assert one_isolate == 180
    return {
        "perfect_matchings": 15,
        "connected_cuts_2_3_4": connected,
        "one_isolate_cuts_1_5": one_isolate,
    }


def off_edges(perm):
    return [
        (a, b) for a in range(4) for b in range(4)
        if b != perm[a]
    ]


def no_independent_five(n, edges):
    E = set(edges)
    for S in combinations(range(n), 5):
        if all(
            tuple(sorted((u, v))) not in E
            for u, v in combinations(S, 2)
        ):
            return False
    return True


def verify_555_endpoint_branch():
    sigma = (1, 0, 2, 3)
    identity = tuple(range(4))
    e_AE = (0, 1)
    idx = lambda block, x: 4 * block + x

    def add(edges, block1, x, block2, y):
        edges.add(tuple(sorted((idx(block1, x), idx(block2, y)))))

    checked = 0
    for e_AB in off_edges(identity):
        if e_AB[0] in {0, 1}:
            continue
        valid = []
        for e_BE in off_edges(sigma):
            edges = set()
            for x in range(4):
                add(edges, 0, x, 1, x)
                add(edges, 0, x, 2, x)
                add(edges, 1, x, 2, sigma[x])
            add(edges, 0, e_AB[0], 1, e_AB[1])
            add(edges, 0, e_AE[0], 2, e_AE[1])
            add(edges, 1, e_BE[0], 2, e_BE[1])
            if no_independent_five(12, edges):
                valid.append(e_BE)
        assert valid == [(0, 0)]
        checked += 1

    assert checked == 6
    return {
        "transposition": "(0 1)",
        "A_endpoint_outside_support_cases": checked,
        "forced_B_extra_edge": "(0,0)",
    }


def main():
    results = {
        name: verify_residual(name, edges)
        for name, edges in RESIDUALS.items()
    }
    cuts = verify_outer_cuts()
    branch = verify_555_endpoint_branch()

    print("M10_K4E_Z4_GLOBAL_GRID_LOCAL_CATALOG_OK")
    for name, result in results.items():
        print(name, result)
    print("OUTER_LIGHT_CUTS", cuts)
    print("CORRECTED_555_ENDPOINT_BRANCH", branch)
    print("SCOPE: pair/triple necessary cell catalog, cut geometry, and one")
    print("       corrected 5,5,5 endpoint branch; global grid contradiction")
    print("       is analytic in M10_K4E_Z4_GLOBAL_GRID_CLOSURE.md.")
    print("       full-support m=10 Q32 and EG617(r=12) remain OPEN.")


if __name__ == "__main__":
    main()
