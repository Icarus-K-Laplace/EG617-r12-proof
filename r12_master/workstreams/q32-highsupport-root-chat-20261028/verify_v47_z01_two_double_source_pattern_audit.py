#!/usr/bin/env python3
"""Exact local audit of source incidence in the x-in-H two-double mode."""
from itertools import combinations, permutations

part = (0, 0, 1, 1, 2, 2, 3)  # three large tracks of size two; T0 singleton
vertices = tuple(range(7))
edges = tuple((u, v) for u in range(7) for v in range(u + 1, 7)
              if part[u] != part[v])
edge_bit = {e: 1 << i for i, e in enumerate(edges)}
s = (0, 2, 4)  # Ns H-triangle, one vertex in each large track
t = (1, 3, 5)  # Nt H-triangle, one vertex in each large track
x = 6

def emask(es):
    out = 0
    for u, v in es:
        e = tuple(sorted((u, v)))
        assert e in edge_bit, ("same-track edge", e)
        out |= edge_bit[e]
    return out

def alpha(mask):
    adj = {v: set() for v in vertices}
    for (u, v), bit in edge_bit.items():
        if mask & bit:
            adj[u].add(v)
            adj[v].add(u)
    best = 0
    for subset in range(1 << 7):
        size = subset.bit_count()
        if size <= best:
            continue
        chosen = [v for v in vertices if (subset >> v) & 1]
        if all(v not in adj[u] for u, v in combinations(chosen, 2)):
            best = size
    return best

triangles = [
    (s[0], s[1]), (s[0], s[2]), (s[1], s[2]),
    (t[0], t[1]), (t[0], t[2]), (t[1], t[2]),
]
def track_pair(e):
    return tuple(sorted((part[e[0]], part[e[1]])))

checked = {"yO_a3": 0, "yO_a2": 0, "yH_a2": 0, "yH_a1": 0}

# y in O, a=3: x sees the whole Nt H-triangle, no other H-H gadget edge.
base = triangles + [(x, t[i]) for i in range(3)]
full = list(base)
assert len(base) == 9 and alpha(emask(base)) == 2
assert alpha(emask(full)) == 2
assert len(full) - 9 == 0
checked["yO_a3"] += 1

# y in O, a=2: x sees the Nt triangle plus one H vertex in Ns\\A0.
for p in range(3):
    base = triangles + [(x, t[i]) for i in range(3)]
    extra = [(x, s[p])]
    full = base + extra
    assert len(base) == 9 and len(extra) == 1
    assert alpha(emask(base)) == 2 and alpha(emask(full)) == 2
    assert track_pair(extra[0]) == (p, 3)
    checked["yO_a2"] += 1

# y in H, a=2: A0_H occupies the two tracks other than q=track(y).
# The unique Ns\\A0 H vertex is s[q], so x has one neighbor in each track.
for q in range(3):
    base = triangles + [(x, s[q])] + [(x, t[i]) for i in range(3) if i != q]
    extra = [(t[q], s[i]) for i in range(3) if i != q]
    full = base + extra
    assert len(base) == 9 and len(extra) == 2
    assert alpha(emask(base)) == 3 and alpha(emask(full)) == 2
    assert all(track_pair(e) in {(q, i) for i in range(3) if i != q} for e in extra)
    assert all(t[q] in e for e in extra)  # source star centered at y
    assert len({track_pair(e) for e in extra}) == 2
    checked["yH_a2"] += 1

# y in H, a=1: p=track(A0_H), q=track(y), p!=q.
# x's Ns/Nt neighborhoods overlap only in the third track r.
for p in range(3):
    for q in range(3):
        if p == q:
            continue
        r = next(i for i in range(3) if i not in (p, q))
        x_neighbors = [s[i] for i in range(3) if i != p]
        x_neighbors += [t[i] for i in range(3) if i != q]
        assert len(x_neighbors) == 4
        assert sum(part[v] == i for v in x_neighbors) == (2 if i == r else 1)
        yA0 = (t[q], s[p])
        for keep in (s[r], t[r]):
            baseline_x = []
            for i in range(3):
                candidates = [v for v in x_neighbors if part[v] == i]
                baseline_x.append(keep if i == r else candidates[0])
            base = triangles + [(x, v) for v in baseline_x]
            full = triangles + [(x, v) for v in x_neighbors] + [yA0]
            extra = [e for e in full if tuple(sorted(e)) not in
                     {tuple(sorted(b)) for b in base}]
            assert len(base) == 9 and len(extra) == 2
            assert alpha(emask(base)) == 3 and alpha(emask(full)) == 2
            t0_extra = [e for e in extra if x in e]
            large_extra = [e for e in extra if x not in e]
            assert len(t0_extra) == len(large_extra) == 1
            assert track_pair(t0_extra[0]) == (r, 3)
            assert track_pair(large_extra[0]) == tuple(sorted((p, q)))
            assert set(track_pair(t0_extra[0])).isdisjoint(set(track_pair(large_extra[0])))
            assert tuple(sorted(yA0)) == tuple(sorted(large_extra[0]))
            checked["yH_a1"] += 1

assert checked == {"yO_a3": 1, "yO_a2": 3, "yH_a2": 3, "yH_a1": 12}
print("source placement cases checked:", checked)
print("y in O, a=3: class A, g=0, t=0")
print("y in O, a=2: class A, g=1, t=1")
print("y in H, a=2: class B, g=2, t=0; two-edge star at y")
print("y in H, a=1: class B, g=2, t=1; T0 pair disjoint from y-A0 pair")
print("V47_Z01_TWO_DOUBLE_SOURCE_PATTERN_AUDIT_OK")
print("Scope: x-in-H two-double source mode only; not global Q32 UNSAT.")
