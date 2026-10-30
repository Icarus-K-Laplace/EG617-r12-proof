#!/usr/bin/env python3
"""Independent m=10 residual-graph relaxation catalog verifier.

Necessary-condition catalog for R=H\\Q, |R|=7. It checks e(R)=3+z,
0<=z<=7, alpha(R)<=4, clique_cover(R)<=4, and
B_min(R)=sum_v max(0,2-d_R(v)) <= 14-2z.

The CSV contains one graph6 representative per isomorphism type. Completeness
is certified by unique canonical codes, orbit-stabilizer sum equal to the
independently enumerated number of labelled feasible graphs, and a full
labelled enumeration over all seven-vertex graphs with 3..10 edges.
Fiber assignments are ordered maps R->[4] whose fibers are cliques; empty
fibers are allowed. This is not a 47-vertex Q32 solver.
"""
import argparse
import csv
import itertools
import json
from collections import Counter
from pathlib import Path

N = 7
# graph6 bit order: j=1..6, then i=0..j-1
EDGES = [(i, j) for j in range(N) for i in range(j)]
EINDEX = {e: k for k, e in enumerate(EDGES)}
ALL = (1 << N) - 1

SUB_EDGE = [0] * (1 << N)
for S in range(1 << N):
    em = 0
    vs = [i for i in range(N) if (S >> i) & 1]
    for i, j in itertools.combinations(vs, 2):
        em |= 1 << EINDEX[(i, j)]
    SUB_EDGE[S] = em

INDEP5_EDGE_MASKS = []
for S in itertools.combinations(range(N), 5):
    m = 0
    for i, j in itertools.combinations(S, 2):
        m |= 1 << EINDEX[(i, j)]
    INDEP5_EDGE_MASKS.append(m)

PERM_EDGE_MAPS = []
for p in itertools.permutations(range(N)):
    mp = []
    for i, j in EDGES:
        a, b = sorted((p[i], p[j]))
        mp.append(EINDEX[(a, b)])
    PERM_EDGE_MAPS.append(mp)

def alpha_le_4(gmask):
    return not any((gmask & m) == 0 for m in INDEP5_EDGE_MASKS)

def clique_cover_le_4(gmask):
    byv = [[] for _ in range(N)]
    for S in range(1, 1 << N):
        em = SUB_EDGE[S]
        if (gmask & em) == em:
            for v in range(N):
                if (S >> v) & 1:
                    byv[v].append(S)
    def rec(rem, k):
        if rem == 0:
            return True
        if k == 0:
            return False
        v = (rem & -rem).bit_length() - 1
        for S in byv[v]:
            if (S & rem) == S and rec(rem ^ S, k - 1):
                return True
        return False
    return rec(ALL, 4)

def adjacency(gmask):
    adj = [0] * N
    for e, (i, j) in enumerate(EDGES):
        if (gmask >> e) & 1:
            adj[i] |= 1 << j
            adj[j] |= 1 << i
    return adj

def degree_list(gmask):
    return [a.bit_count() for a in adjacency(gmask)]

def bmin_for_degrees(deg):
    return sum(max(0, 2 - d) for d in deg)

def graph6_decode(s):
    vals = [ord(c) - 63 for c in s]
    if not vals or vals[0] != N:
        raise ValueError(f"not a 7-vertex graph6 code: {s!r}")
    bits = []
    for x in vals[1:]:
        if not 0 <= x <= 63:
            raise ValueError(f"invalid graph6 character in {s!r}")
        bits.extend((x >> b) & 1 for b in range(5, -1, -1))
    bits = bits[:len(EDGES)]
    if len(bits) != len(EDGES):
        raise ValueError(f"short graph6 code: {s!r}")
    m = 0
    for i, bit in enumerate(bits):
        if bit:
            m |= 1 << i
    return m

def canonical_code_and_aut(gmask):
    best = None
    aut = 0
    for mp in PERM_EDGE_MAPS:
        m2 = 0
        for e, new_e in enumerate(mp):
            if (gmask >> e) & 1:
                m2 |= 1 << new_e
        if best is None or m2 < best:
            best = m2
        if m2 == gmask:
            aut += 1
    return best, aut

def fiber_profile(labels):
    return tuple(sorted(Counter(labels).values(), reverse=True))

def fiber_assignment_data(gmask, dump=None, z=None, graph6=None):
    adj = adjacency(gmask)
    total = 0
    profiles = Counter()
    for labels in itertools.product(range(4), repeat=N):
        ok = True
        for i, j in EDGES:
            if labels[i] == labels[j] and not ((adj[i] >> j) & 1):
                ok = False
                break
        if ok:
            total += 1
            profiles[fiber_profile(labels)] += 1
            if dump is not None:
                dump.write(json.dumps({
                    "z": z, "graph6": graph6,
                    "labels": labels,
                    "fiber_profile": fiber_profile(labels)
                }, separators=(",", ":")) + "\n")
    return total, profiles

def connected(gmask):
    adj = adjacency(gmask)
    seen = 1
    frontier = 1
    while frontier:
        v = (frontier & -frontier).bit_length() - 1
        frontier &= frontier - 1
        new = adj[v] & ~seen
        seen |= new
        frontier |= new
    return seen == ALL

def component_profile(gmask):
    adj = adjacency(gmask)
    unseen = ALL
    sizes = []
    while unseen:
        root = (unseen & -unseen).bit_length() - 1
        todo = 1 << root
        unseen ^= 1 << root
        size = 0
        while todo:
            v = (todo & -todo).bit_length() - 1
            todo &= todo - 1
            size += 1
            new = adj[v] & unseen
            unseen ^= new
            todo |= new
        sizes.append(size)
    return tuple(sorted(sizes, reverse=True))

def read_catalog(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append({
                "z": int(row["z"]),
                "graph6": row["graph6"],
                "bmin": int(row["bmin"]),
                "F_assignments": int(row["F_assignments"])
            })
    return rows

def enumerate_labelled(dump_graphs=None):
    raw = Counter()
    alpha_ok = Counter()
    cover_ok = Counter()
    budget_reject = Counter()
    feasible = Counter()
    comp_profiles = Counter()
    connected_count = Counter()
    f = open(dump_graphs, "w", encoding="utf-8") if dump_graphs else None
    try:
        for k in range(3, 11):
            z = k - 3
            y_max = 14 - 2 * z
            for comb in itertools.combinations(range(len(EDGES)), k):
                raw[z] += 1
                gm = 0
                deg = [0] * N
                for e in comb:
                    gm |= 1 << e
                    i, j = EDGES[e]
                    deg[i] += 1
                    deg[j] += 1
                if not alpha_le_4(gm):
                    continue
                alpha_ok[z] += 1
                if not clique_cover_le_4(gm):
                    continue
                cover_ok[z] += 1
                if bmin_for_degrees(deg) > y_max:
                    budget_reject[z] += 1
                    continue
                feasible[z] += 1
                comp_profiles[(z, component_profile(gm))] += 1
                if connected(gm):
                    connected_count[z] += 1
                if f is not None:
                    f.write(f"{z},{gm:06x}\n")
    finally:
        if f is not None:
            f.close()
    return {
        "raw_by_z": dict(sorted(raw.items())),
        "alpha_ok_by_z": dict(sorted(alpha_ok.items())),
        "alpha_and_cover_ok_by_z": dict(sorted(cover_ok.items())),
        "incidence_budget_rejected_by_z": dict(sorted(budget_reject.items())),
        "feasible_by_z": dict(sorted(feasible.items())),
        "feasible_total": sum(feasible.values()),
        "connected_labelled_by_z": dict(sorted(connected_count.items())),
        "component_size_profiles": {
            f"{z}:{'-'.join(map(str, p))}": c
            for (z, p), c in sorted(comp_profiles.items())
        }
    }

def verify_catalog(path, dump_fibers=None):
    rows = read_catalog(path)
    seen_codes = set()
    canonical_codes = set()
    by_z_types = Counter()
    by_z_F = Counter()
    by_z_pairs = Counter()
    by_z_connected = Counter()
    orbit_sum = 0
    total_F = 0
    total_pairs = 0
    dump = open(dump_fibers, "w", encoding="utf-8") if dump_fibers else None
    try:
        for row in rows:
            z, g6 = row["z"], row["graph6"]
            if g6 in seen_codes:
                raise AssertionError(f"duplicate graph6 row: {g6}")
            seen_codes.add(g6)
            gm = graph6_decode(g6)
            e = gm.bit_count()
            if e != 3 + z:
                raise AssertionError(f"edge/z mismatch: {g6}, z={z}, e={e}")
            deg = degree_list(gm)
            bmin = bmin_for_degrees(deg)
            if bmin != row["bmin"]:
                raise AssertionError(f"B_min mismatch: {g6}")
            if not alpha_le_4(gm):
                raise AssertionError(f"alpha>4: {g6}")
            if not clique_cover_le_4(gm):
                raise AssertionError(f"clique-cover>4: {g6}")
            if bmin > 14 - 2 * z:
                raise AssertionError(f"residual incidence budget fails: {g6}")
            nf, _profiles = fiber_assignment_data(gm, dump, z, g6)
            if nf != row["F_assignments"]:
                raise AssertionError(f"fiber assignment count mismatch: {g6}: {nf}")
            canon, aut = canonical_code_and_aut(gm)
            if canon in canonical_codes:
                raise AssertionError(f"isomorphic catalog representatives: {g6}")
            canonical_codes.add(canon)
            if 5040 % aut:
                raise AssertionError(f"non-dividing automorphism count: {g6}")
            orbit_sum += 5040 // aut
            by_z_types[z] += 1
            by_z_F[z] += nf
            by_z_pairs[z] += nf * nf
            by_z_connected[(z, connected(gm))] += 1
            total_F += nf
            total_pairs += nf * nf
    finally:
        if dump is not None:
            dump.close()

    labelled = enumerate_labelled()
    expected = {0:105, 1:1785, 2:12180, 3:45227,
                4:109455, 5:200025, 6:280875, 7:147420}
    if orbit_sum != labelled["feasible_total"]:
        raise AssertionError("orbit-stabilizer sum differs from labelled enumeration")
    if len(rows) != 371:
        raise AssertionError(f"expected 371 isomorphism types, got {len(rows)}")
    if total_F != 93120:
        raise AssertionError(f"expected 93120 fiber maps, got {total_F}")
    if total_pairs != 34794144:
        raise AssertionError(f"expected 34794144 ordered (F,G) pairs, got {total_pairs}")
    if labelled["feasible_by_z"] != expected:
        raise AssertionError("labelled per-Z counts changed")
    return {
        "isomorphism_types": len(rows),
        "orbit_sum": orbit_sum,
        "fiber_maps": total_F,
        "ordered_FG_pairs": total_pairs,
        "types_by_z": dict(sorted(by_z_types.items())),
        "fiber_maps_by_z": dict(sorted(by_z_F.items())),
        "ordered_FG_pairs_by_z": dict(sorted(by_z_pairs.items())),
        "connected_types_by_z": {
            str(k): v for k, v in sorted(by_z_connected.items())
        },
        "labelled_enumeration": labelled
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", default=str(Path(__file__).with_name("M10_RESIDUAL_GRAPH_CATALOG.csv")))
    ap.add_argument("--dump-fibers", default=None,
                    help="write all 93,120 ordered four-fiber maps on canonical representatives")
    ap.add_argument("--dump-labelled-graphs", default=None,
                    help="write every labelled feasible residual graph as z,edge-mask-hex")
    args = ap.parse_args()
    result = verify_catalog(args.catalog, args.dump_fibers)
    if args.dump_labelled_graphs:
        result["labelled_enumeration"] = enumerate_labelled(args.dump_labelled_graphs)
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
