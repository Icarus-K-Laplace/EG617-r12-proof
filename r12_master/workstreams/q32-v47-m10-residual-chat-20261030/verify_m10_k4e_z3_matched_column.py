#!/usr/bin/env python3
"""Exact necessary pair/triple cell catalog for the 4+6 K4-e, Z=3 slice.

Standard library only. This is not a full 4x6 grid solver or Q32 certificate.
"""
from __future__ import annotations
import csv, itertools, json
from collections import Counter
from pathlib import Path

N=7
EDGES=[(i,j) for j in range(N) for i in range(j)]
PERMS=list(itertools.permutations(range(4)))
CODES={
 "2C3+K1":"FCc"+chr(96)+"G",
 "C4+P3":"F"+chr(96)+"__g",
 "C3+P4":"Fh?GW",
 "P7":"FhCK?",
 "C6+K1":"FhEG?",
 "C5+P2":"Fhc?G",
}
EXPECTED={
 "2C3+K1":(168,17856,70848,{"3,3,1":24,"3,2,1,1":144},
  {"both-empty-same-partition":576,"F-empty-G-full":3456,"F-full-G-empty":3456,"full-aligned":3456,"full-nonaligned":6912}),
 "C4+P3":(96,4608,29952,{"2,2,2,1":96},
  {"full-aligned":2304,"full-nonaligned":2304}),
 "C3+P4":(168,15552,67392,{"3,2,2":24,"3,2,1,1":72,"2,2,2,1":72},
  {"both-empty-same-partition":576,"F-empty-G-full":2880,"F-full-G-empty":2880,"full-aligned":3456,"full-nonaligned":5760}),
 "P7":(96,5760,31104,{"2,2,2,1":96},
  {"full-aligned":2304,"full-nonaligned":3456}),
 "C6+K1":(48,1152,13824,{"2,2,2,1":48},
  {"full-aligned":1152}),
 "C5+P2":(120,8640,40320,{"2,2,2,1":120},
  {"full-aligned":2880,"full-nonaligned":5760}),
}

def decode_g6(code):
    vals=[ord(c)-63 for c in code]
    if not vals or vals[0]!=N: raise ValueError(code)
    bits=[]
    for x in vals[1:]: bits.extend((x>>b)&1 for b in range(5,-1,-1))
    bits=bits[:21]
    if len(bits)!=21: raise ValueError("short graph6")
    return sum(1<<i for i,b in enumerate(bits) if b)

def adjacency(gm):
    a=[0]*N
    for e,(i,j) in enumerate(EDGES):
        if gm>>e&1: a[i]|=1<<j; a[j]|=1<<i
    return a

def independent_sets(a,k):
    return [S for S in itertools.combinations(range(N),k)
            if all(not (a[i]>>j&1) for i,j in itertools.combinations(S,2))]

def clique_fiber_maps(a):
    return [f for f in itertools.product(range(4),repeat=N)
            if all(f[i]!=f[j] or (a[i]>>j&1) for i,j in EDGES)]

def empty_label(f):
    return next((i for i in range(4) if i not in f),None)

def partition(f):
    return frozenset(frozenset(v for v,x in enumerate(f) if x==i) for i in set(f))

def aligned(f,g,p):
    return all(g[v]==p[f[v]] for v in range(N))

def required_extra(f,g,p,ip,it):
    h=tuple(p.index(g[v]) for v in range(N))
    labels=set(range(4)); required=None
    for r,s in ip:
        U=labels-{f[r],f[s]}; V=labels-{h[r],h[s]}
        if U==V: continue
        if len(U-V)==1 and len(V-U)==1:
            edge=(next(iter(U-V)),next(iter(V-U)))
            if required is not None and required!=edge: return None
            required=edge
        else: return None
    for S in it:
        U=labels-{f[v] for v in S}; V=labels-{h[v] for v in S}
        if len(U)!=1 or len(V)!=1: return None
        a=next(iter(U)); b=next(iter(V))
        if a!=b:
            edge=(a,b)
            if required is not None and required!=edge: return None
            required=edge
    return ("free",None) if required is None else ("fixed",required)

def verify_type(name,code):
    gm=decode_g6(code)
    assert gm.bit_count()==6
    a=adjacency(gm)
    maps=clique_fiber_maps(a)
    ip=independent_sets(a,2); it=independent_sets(a,3)
    profile_maps=Counter()
    for f in maps: profile_maps[tuple(sorted(Counter(f).values(),reverse=True))]+=1
    categories=Counter(); pairs=cell_states=0
    for f in maps:
        zf=empty_label(f)
        for g in maps:
            zg=empty_label(g)
            states={}
            for p in PERMS:
                req=required_extra(f,g,p,ip,it)
                if req is not None: states[p]=req
            if not states: continue
            pairs+=1
            cell_states+=sum(12 if req[0]=="free" else 1 for req in states.values())
            if zf is None and zg is None:
                p0=[p for p in states if aligned(f,g,p)]
                if p0:
                    assert len(p0)==1 and len(states)==1 and states[p0[0]]==("free",None)
                    categories["full-aligned"]+=1
                else:
                    assert len(states)==1 and next(iter(states.values()))[0]=="fixed"
                    categories["full-nonaligned"]+=1
            elif zf is not None and zg is None:
                assert len(states)==2
                assert all(req[0]=="fixed" and req[1][0]==zf for req in states.values())
                ps=list(states); rel=tuple(ps[0].index(ps[1][x]) for x in range(4))
                moved=[i for i in range(4) if rel[i]!=i]
                assert len(moved)==2 and zf in moved
                categories["F-empty-G-full"]+=1
            elif zf is None and zg is not None:
                assert len(states)==2
                assert all(req[0]=="fixed" and req[1][1]==p.index(zg) for p,req in states.items())
                ps=list(states); rel=tuple(ps[0].index(ps[1][x]) for x in range(4))
                moved=[i for i in range(4) if rel[i]!=i]
                assert len(moved)==2 and ps[0].index(zg) in moved
                categories["F-full-G-empty"]+=1
            else:
                assert partition(f)==partition(g)
                p0=[p for p in states if aligned(f,g,p)]
                assert len(p0)==1 and len(states)==4 and states[p0[0]]==("free",None)
                z=zf
                for p,req in states.items():
                    if p==p0[0]: continue
                    rel=tuple(p0[0].index(p[x]) for x in range(4))
                    moved=[i for i in range(4) if rel[i]!=i]
                    assert len(moved)==2 and z in moved
                    k=next(x for x in moved if x!=z)
                    assert req==("fixed",(z,k))
                categories["both-empty-same-partition"]+=1
    got=(len(maps),pairs,cell_states,
         {",".join(map(str,k)):v for k,v in sorted(profile_maps.items(),reverse=True)},
         dict(sorted(categories.items())))
    exp=EXPECTED[name]
    assert got==(exp[0],exp[1],exp[2],dict(sorted(exp[3].items())),dict(sorted(exp[4].items()))), (name,got,exp)
    return got

def verify_matched_core_connectivity():
    # K4-e small-side light graph.
    small={(0,2),(0,3),(1,2),(1,3),(2,3)}
    def conn(n,edges):
        seen={0};todo=[0]
        while todo:
            u=todo.pop()
            for v in range(n):
                if (min(u,v),max(u,v)) in edges and v not in seen:
                    seen.add(v);todo.append(v)
        return seen==set(range(n))
    assert conn(4,small)
    # The four endpoints of two disjoint heavy matching edges induce C4.
    outer={(0,2),(0,3),(1,2),(1,3)}
    assert conn(4,outer)
    return {"small_light_graph":"K4-e connected","matched_outer_light_graph":"C4 connected"}

def main():
    here=Path(__file__).resolve().parent
    with (here/"M10_4PLUS6_TIGHT_RESIDUAL_FILTER.csv").open(newline="",encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    got={r["graph6"] for r in rows if r["branch"]=="K4e-small-Z1-3" and int(r["z"])==3}
    assert got==set(CODES.values())
    results={name:verify_type(name,code) for name,code in CODES.items()}
    connectivity=verify_matched_core_connectivity()
    print("M10_K4E_Z3_MATCHED_COLUMN_CATALOG_OK")
    print(json.dumps({"types":results,"matched_core_connectivity":connectivity},indent=2,sort_keys=True))
    print("SCOPE: necessary pair/triple cell catalog and matched-column core alignment only;")
    print("       unmatched outer blocks and the full six-column grid remain OPEN.")

if __name__=="__main__":main()
