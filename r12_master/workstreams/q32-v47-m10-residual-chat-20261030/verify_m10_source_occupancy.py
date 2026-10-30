#!/usr/bin/env python3
"""Enumerate all aggregate Type-I K5 outside-count assignments for m=10.

The twelve labelled factors are I0,...,I9,Ns,Nt. Every factor has at least
one outside vertex. If x_C is outside, the total outside count in the factors
is 13; if x_C is in H, it is 14. This enumerates only factor occupancy counts,
not endpoint-labelled y/A0/gadget placements or full Q32 completions.
"""
from itertools import combinations
from math import comb
import csv
import json
from pathlib import Path

FACTORS = [f"I{i}" for i in range(10)] + ["Ns", "Nt"]

def make_row(location, profile, chosen, b):
    bs, bt = b["Ns"], b["Nt"]
    x_out = location == "O"
    g11_h = 11 - bs - bt - int(x_out)
    k5_h_edges = sum(comb(5-v, 2) for v in b.values())
    isolated_count = (sum(b[f] == 3 for f in FACTORS[:10])
                      if profile == "triple"
                      else sum(b[f] == 2 for f in FACTORS[:10]))
    if location == "O":
        gmax = 4
        gmins = [0,0,0,0]
    elif profile == "two-double":
        gmax = 5
        base = 7 - bs - bt
        gmins = [max(0, base-a) for a in (1,2,3,4)]
    else:
        gmax = 6
        base = 8 - bs - bt
        gmins = [max(0, base-a) for a in (1,2,3,4)]
    return {
        "location_x": location,
        "profile": profile,
        "chosen_factor_or_pair": chosen,
        "isolated_double_or_triple_count": isolated_count,
        "Ns_outside": bs,
        "Nt_outside": bt,
        "G11_H_vertices": g11_h,
        "K5_interior_H_edges": k5_h_edges,
        "g_min_a1": gmins[0],
        "g_min_a2": gmins[1],
        "g_min_a3": gmins[2],
        "g_min_a4": gmins[3],
        "g_max": gmax,
    }

def enumerate_rows():
    out = []
    for f in FACTORS:
        b = {g:1 for g in FACTORS}; b[f] = 2
        out.append(make_row("O","one-double",f,b))
    for pair in combinations(FACTORS,2):
        b = {g:1 for g in FACTORS}; b[pair[0]]=2; b[pair[1]]=2
        out.append(make_row("H","two-double","+".join(pair),b))
    for f in FACTORS:
        b = {g:1 for g in FACTORS}; b[f] = 3
        out.append(make_row("H","triple",f,b))
    return out

def verify(rows):
    assert len(rows)==90
    from collections import Counter
    counts=Counter((r["location_x"],r["profile"]) for r in rows)
    assert counts=={("O","one-double"):12,("H","two-double"):66,("H","triple"):12}
    for r in rows:
        total_out = 13 if r["location_x"]=="O" else 14
        assert sum((2 if r["profile"]=="one-double" and r["chosen_factor_or_pair"]==f else
                    2 if r["profile"]=="two-double" and f in r["chosen_factor_or_pair"].split("+") else
                    3 if r["profile"]=="triple" and r["chosen_factor_or_pair"]==f else 1)
                   for f in FACTORS)==total_out
        assert r["G11_H_vertices"] == 11-r["Ns_outside"]-r["Nt_outside"]-(r["location_x"]=="O")
        expected_edges = 69 if r["profile"]=="one-double" else 66 if r["profile"]=="two-double" else 67
        assert r["K5_interior_H_edges"] == expected_edges
        expected_isolated = (int(r["chosen_factor_or_pair"].startswith("I")) if r["profile"]!="two-double"
                             else sum(f in r["chosen_factor_or_pair"].split("+") for f in FACTORS[:10]))
        assert r["isolated_double_or_triple_count"] == expected_isolated
        assert r["Ns_outside"]>=1 and r["Nt_outside"]>=1
        if r["location_x"]=="O":
            expected_mins=[0,0,0,0]; expected_max=4
        elif r["profile"]=="two-double":
            base=7-r["Ns_outside"]-r["Nt_outside"]
            expected_mins=[max(0,base-a) for a in (1,2,3,4)]; expected_max=5
        else:
            base=8-r["Ns_outside"]-r["Nt_outside"]
            expected_mins=[max(0,base-a) for a in (1,2,3,4)]; expected_max=6
        assert [r["g_min_a1"],r["g_min_a2"],r["g_min_a3"],r["g_min_a4"]]==expected_mins
        assert r["g_max"]==expected_max
    return counts

def main():
    rows=enumerate_rows()
    counts=verify(rows)
    out=Path(__file__).with_name("M10_SOURCE_OCCUPANCY_90.csv")
    with out.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader();w.writerows(rows)
    print(json.dumps({"rows":len(rows),"counts":{str(k):v for k,v in counts.items()},"csv":out.name},indent=2))

if __name__=="__main__":
    main()
