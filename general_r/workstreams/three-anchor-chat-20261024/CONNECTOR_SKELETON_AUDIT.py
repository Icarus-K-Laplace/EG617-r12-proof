#!/usr/bin/env python3
"""Deterministic connector-skeleton relaxation for the three-anchor proof.

Enumerates all labelled connector adjacency graphs, all connector excess
allocations with total <= 6, and all allowed focus-owner assignments for
r=12,13,14,15. For each nonfocused connector it computes the minimum local
rectangle charge compatible with the degree inequality. Overlapping same-group
rectangles are charged by max(R1,R2), never by an unjustified sum.

This is deliberately a RELAXED skeleton search: it does not construct or
enumerate full graphs H, does not impose all alpha/omega constraints on every
vertex, and cannot certify the theorem. Its purpose is to cross-check that the
proof's structural reductions leave only the stated r=12 overlap signatures.
Uses only the Python standard library.
"""
from itertools import combinations, product
from functools import lru_cache


def R(a, b, p, q):
    return a * max(b - p, 0) + b * max(a - q, 0)


def edges_for(n):
    return list(combinations(range(n), 2))


def adjacency(n, mask):
    es = edges_for(n)
    adj = [[False] * n for _ in range(n)]
    for j, (u, v) in enumerate(es):
        if (mask >> j) & 1:
            adj[u][v] = adj[v][u] = True
    return adj


@lru_cache(None)
def min_rectangle(a_max, b_max, p, q, s_min):
    vals = [
        R(a, b, p, q)
        for a in range(1, a_max + 1)
        for b in range(1, b_max + 1)
        if a + b >= s_min
    ]
    return min(vals) if vals else None


def excess_allocations(n, budget=6):
    return [k for k in product(range(budget + 1), repeat=n) if sum(k) <= budget]


def enum_c2_connector_only():
    # Two triple connectors p,q; their edge is the only connector-graph choice.
    # The E_i proof is analytic and is not represented by this skeleton count.
    return 2 * len(excess_allocations(2))


def enum_c3(r):
    # Labels: 0=w (triple), 1=u, 2=v (pair connectors).
    count = 0
    focus_hist = {}
    ks = excess_allocations(3)
    for gm in range(2 ** 3):
        adj = adjacency(3, gm)
        gamma = [sum(row) for row in adj]
        for fmask in range(4):  # bit 0: u focused; bit 1: v focused
            fu, fv = bool(fmask & 1), bool(fmask & 2)
            if fu and fv:
                # Adjacent focused pair creates an r-clique; nonadjacent pair
                # has an oversized common-nonneighbour clique.
                continue
            f = int(fu) + int(fv)
            for k in ks:
                rects = []
                ok = True
                for i, focused in ((1, fu), (2, fv)):
                    if focused:
                        continue
                    val = min_rectangle(r - 2, r - 3, 2, 3 - f,
                                         r - 3 + gamma[i] - k[i])
                    if val is None:
                        ok = False
                        break
                    rects.append(val)
                if not ok:
                    continue
                # The two pair-connector rectangles have disjoint opposite
                # long blocks, so their charges add.
                if sum(k) + sum(rects) <= 6:
                    count += 1
                    focus_hist[fmask] = focus_hist.get(fmask, 0) + 1
    return count, focus_hist


def enum_c4_002(r):
    # Labels 0,1 miss a1; labels 2,3 miss a2. All are incident with a3.
    count = 0
    focus_hist = {}
    ks = excess_allocations(4)
    for gm in range(2 ** 6):
        adj = adjacency(4, gm)
        gamma = [sum(row) for row in adj]
        for fmask in range(1 << 4):
            foc = {i for i in range(4) if (fmask >> i) & 1}
            f = len(foc)
            if f > 2:
                continue
            if f == 2:
                x, y = tuple(foc)
                if not adj[x][y]:
                    continue
            for k in ks:
                rect = [0] * 4
                ok = True
                for i in range(4):
                    if i in foc:
                        continue
                    val = min_rectangle(r - 2, r - 4, 2, 4 - f,
                                         r - 4 + gamma[i] - k[i])
                    if val is None:
                        ok = False
                        break
                    rect[i] = val
                if not ok:
                    continue
                rcharge = 0
                for i, j in ((0, 1), (2, 3)):
                    if i in foc and j in foc:
                        continue
                    if i in foc:
                        rcharge += rect[j]
                    elif j in foc:
                        rcharge += rect[i]
                    elif adj[i][j]:
                        rcharge += max(rect[i], rect[j])
                    else:
                        rcharge += rect[i] + rect[j]
                # Cross-group rectangles add. For an adjacent same-group pair,
                # max(R1,R2) is the safe overlap relaxation.
                if sum(k) + rcharge <= 6:
                    count += 1
                    focus_hist[f] = focus_hist.get(f, 0) + 1
    return count, focus_hist


def enum_c4_011(r):
    # Labels: 0=U1, 1=U2, 2=V, 3=W.
    # X2 owners are None/U1/U2/W; X3 owners are None/U1/U2/V.
    x2_owners = (None, 0, 1, 3)
    x3_owners = (None, 0, 1, 2)
    count = 0
    slot_hist = {}
    ks = excess_allocations(4)
    for gm in range(2 ** 6):
        adj = adjacency(4, gm)
        gamma = [sum(row) for row in adj]
        for owner2 in x2_owners:
            for owner3 in x3_owners:
                occ2, occ3 = owner2 is not None, owner3 is not None
                owners = {x for x in (owner2, owner3) if x is not None}
                s = int(occ2) + int(occ3)
                for k in ks:
                    rect = [0] * 4
                    ok = True
                    for i in range(4):
                        if i in owners:
                            continue
                        if i in (0, 1):  # U: incident with X2 and X3
                            p, q = 3 - int(occ2), 3 - int(occ3)
                            a_max = b_max = r - 3
                            s_min = r - 4 + gamma[i] - k[i]
                        elif i == 2:  # V: incident with X1 and X3
                            p, q = 2, 3 - int(occ3)
                            a_max, b_max = r - 2, r - 3
                            s_min = r - 3 + gamma[i] - k[i]
                        else:  # W: incident with X1 and X2
                            p, q = 2, 3 - int(occ2)
                            a_max, b_max = r - 2, r - 3
                            s_min = r - 3 + gamma[i] - k[i]
                        val = min_rectangle(a_max, b_max, p, q, s_min)
                        if val is None:
                            ok = False
                            break
                        rect[i] = val
                    if not ok:
                        continue
                    # U1/U2 can overlap only when adjacent. V and W add, and
                    # the U-pair aggregate adds to each of their rectangles.
                    if 0 in owners and 1 in owners:
                        ucharge = 0
                    elif 0 in owners:
                        ucharge = rect[1]
                    elif 1 in owners:
                        ucharge = rect[0]
                    elif adj[0][1]:
                        ucharge = max(rect[0], rect[1])
                    else:
                        ucharge = rect[0] + rect[1]
                    rcharge = ucharge + rect[2] + rect[3]
                    if sum(k) + rcharge <= 6:
                        count += 1
                        slot_hist[s] = slot_hist.get(s, 0) + 1
    return count, slot_hist


def main():
    c2 = enum_c2_connector_only()
    print(f"c=2 connector-only skeletons (edge/no-edge x excess allocations): {c2}")
    expected = {
        12: {"c3": 44, "c4_002": 2, "c4_011": 2},
        13: {"c3": 4, "c4_002": 0, "c4_011": 0},
        14: {"c3": 0, "c4_002": 0, "c4_011": 0},
        15: {"c3": 0, "c4_002": 0, "c4_011": 0},
    }
    for r in range(12, 16):
        c3, h3 = enum_c3(r)
        c402, h402 = enum_c4_002(r)
        c411, h411 = enum_c4_011(r)
        actual = {"c3": c3, "c4_002": c402, "c4_011": c411}
        assert actual == expected[r], (r, actual, expected[r])
        print(f"r={r}: relaxed low-budget skeletons {actual}; c3-focus={h3}; c4_002-focus-count={h402}; c4_011-slot-count={h411}")
    print("PASS: every labelled connector adjacency graph and allowed focus-owner assignment was enumerated for c=3 and c=4.")
    print("LIMITATION: counts are local degree/rectangle relaxations, not full graphs H and not counterexamples.")


if __name__ == "__main__":
    main()
