#!/usr/bin/env python3
"""Independent re-enumeration of the COVER q=27/q=28 bipartite shell states.

This implementation is written separately from frozen/cover/INDEPENDENT_VERIFIER.py.
It enumerates row multiplicities, hub decorations, then nondecreasing low decorations
within each row type, and directly checks the necessary shell constraints.
Run: python -B RECHECK_COVER_Q27_Q28_INDEPENDENT.py
"""
from itertools import permutations
import json

def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for tail in compositions(total - x, length - 1):
            yield (x,) + tail

def sorted_partitions(total, length, lower=0):
    if length == 0:
        if total == 0:
            yield ()
        return
    for x in range(lower, total // length + 1):
        for tail in sorted_partitions(total - x, length - 1, x):
            yield (x,) + tail

def canon(hubs, rows):
    candidates = []
    for p in permutations(range(3)):
        wh = tuple(hubs[i] for i in p)
        rr = []
        for mask, g in rows:
            mm = sum(1 << j for j, i in enumerate(p) if mask & (1 << i))
            rr.append((mm, g))
        candidates.append((wh, tuple(sorted(rr))))
    return min(candidates)

def hall(counts):
    for S in range(1, 8):
        neighbours = sum(counts[m] for m in range(8) if m & S)
        if neighbours < S.bit_count():
            return False
    return True

def expected(q):
    out = set()
    if q == 27:
        for k in (8, 9):
            out.add(canon((9, 9, 9), [(7, 0)] * k + [(0, 0)] * (10-k)))
    else:
        for k in (8, 9):
            out.add(canon((9, 9, 10), [(7, 0)] * k + [(0, 0)] * (10-k)))
        for k in (7, 8):
            out.add(canon((9, 9, 9), [(7, 0)] * k + [(3, 1)] + [(0, 0)] * (9-k)))
        for k in (8, 9):
            out.add(canon((9, 9, 9), [(7, 0)] * (k-1) + [(7, 1)] + [(0, 0)] * (10-k)))
            out.add(canon((9, 9, 9), [(7, 0)] * k + [(0, 1)] + [(0, 0)] * (9-k)))
    return out

def direct_check(q, state):
    hubs, rows = state
    assert len(rows) == 10
    adj = [set() for _ in range(13)]
    for j, (mask, g) in enumerate(rows, 3):
        for i in range(3):
            if mask & (1 << i):
                adj[i].add(j)
                adj[j].add(i)
    weights = list(hubs) + [mask.bit_count() + g for mask, g in rows]
    decorations = [weights[i] - len(adj[i]) for i in range(13)]
    assert min(decorations) >= 0
    z = sum(len(adj[i]) for i in range(13)) // 2
    assert z >= 22 and z + sum(decorations) == q
    assert all(weights[i] + weights[j] >= 12 for i in range(13) for j in adj[i])
    # Hall's condition is exactly alpha(M)<=10 for a 3-by-10 bipartite graph.
    assert hall([sum(1 for mask, g in rows if mask == m) for m in range(8)])
    for mask in range(1 << 13):
        S = [i for i in range(13) if mask & (1 << i)]
        eS = sum(j in adj[i] for ii, i in enumerate(S) for j in S[ii+1:])
        if len(S) >= 11:
            assert eS > 0
        R = [i for i in range(13) if not mask & (1 << i)]
        eR = sum(j in adj[i] for ii, i in enumerate(R) for j in R[ii+1:])
        assert sum(weights[i] for i in S) - eS + eR + sum(decorations[i] for i in R) == q
    # INS11 for every regular pivot (decoration zero).
    for i in range(13):
        if decorations[i] == 0:
            N = sorted(adj[i])
            eN = sum(b in adj[a] for ii, a in enumerate(N) for b in N[ii+1:])
            assert sum(weights[j] for j in N) - 2*eN >= len(N)*(12-len(N))

def enumerate_q(q):
    states = set()
    counters = {"row_count_vectors": 0, "edge_hall_vectors": 0,
                "hub_decoration_vectors": 0, "complete_low_decorations": 0}
    for counts in compositions(10, 8):
        counters["row_count_vectors"] += 1
        z = sum(counts[m] * m.bit_count() for m in range(8))
        if not (22 <= z <= q) or not hall(counts):
            continue
        counters["edge_hall_vectors"] += 1
        deg = [sum(counts[m] for m in range(8) if m & (1 << i)) for i in range(3)]
        G = q - z
        row_types = [(m, counts[m]) for m in range(8) if counts[m]]
        for hub_budget in range(G + 1):
            for gs in compositions(hub_budget, 3):
                counters["hub_decoration_vectors"] += 1
                wh = [deg[i] + gs[i] for i in range(3)]
                low_budget = G - hub_budget
                def distribute(pos, remaining, rows):
                    if pos == len(row_types):
                        if remaining:
                            return
                        counters["complete_low_decorations"] += 1
                        for i in range(3):
                            if gs[i] == 0:
                                row_weight = sum(m.bit_count()+g for m,g in rows if m & (1 << i))
                                if row_weight < deg[i]*(12-deg[i]):
                                    return
                        state = canon(wh, rows)
                        states.add(state)
                        return
                    mask, count = row_types[pos]
                    d = mask.bit_count()
                    lower = max([0] + [12-d-wh[i] for i in range(3) if mask & (1 << i)])
                    if sum(wh[i] for i in range(3) if mask & (1 << i)) < d*(12-d):
                        lower = max(lower, 1)
                    reserve = 0
                    for m2, c2 in row_types[pos+1:]:
                        d2 = m2.bit_count()
                        f2 = max([0] + [12-d2-wh[i] for i in range(3) if m2 & (1 << i)])
                        if sum(wh[i] for i in range(3) if m2 & (1 << i)) < d2*(12-d2):
                            f2 = max(f2, 1)
                        reserve += c2*f2
                    for budget in range(count*lower, remaining-reserve+1):
                        for gs_group in sorted_partitions(budget, count, lower):
                            distribute(pos+1, remaining-budget, rows+[(mask,g) for g in gs_group])
                distribute(0, low_budget, [])
    assert counters["row_count_vectors"] == 19448
    assert states == expected(q), (q, states ^ expected(q))
    for state in states:
        direct_check(q, state)
    return {"q": q, "states": len(states), "counters": counters}

if __name__ == "__main__":
    result = {
        "implementation": "independent direct enumeration",
        "results": [enumerate_q(q) for q in (27, 28)],
        "disposition": "exactly matches 2 q27 and 8 q28 canonical states",
        "checks": "all 8192 subset identities and regular INS11 inequalities per state",
    }
    print(json.dumps(result, indent=2))
