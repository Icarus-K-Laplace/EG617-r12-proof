#!/usr/bin/env python3
"""Replay the tightened 4+6 m=10 residual and outer-ledger reductions.

Standard library only. This is a necessary-condition verifier, not a Q32
SAT/UNSAT solver.
"""
from __future__ import annotations
import argparse, csv, itertools, json
from collections import Counter, defaultdict
from pathlib import Path

N=7
EDGES=[(i,j) for j in range(N) for i in range(j)]
EINDEX={e:k for k,e in enumerate(EDGES)}
ALL=(1<<N)-1
SUB_EDGE=[0]*(1<<N)
for S in range(1<<N):
    vs=[v for v in range(N) if S>>v&1]
    em=0
    for i,j in itertools.combinations(vs,2): em|=1<<EINDEX[(i,j)]
    SUB_EDGE[S]=em
INDEP5=[]
for S in itertools.combinations(range(N),5):
    em=0
    for i,j in itertools.combinations(S,2): em|=1<<EINDEX[(i,j)]
    INDEP5.append(em)
CLIQUE_BY_VERTEX=[[] for _ in range(N)]
for S in range(1,1<<N):
    for v in range(N):
        if S>>v&1: CLIQUE_BY_VERTEX[v].append(S)
PERM7_MAPS=[]
for p in itertools.permutations(range(N)):
    PERM7_MAPS.append([EINDEX[tuple(sorted((p[i],p[j])))] for i,j in EDGES])

def decode_g6(code):
    vals=[ord(c)-63 for c in code]
    if not vals or vals[0]!=N: raise ValueError(code)
    bits=[]
    for x in vals[1:]: bits.extend((x>>b)&1 for b in range(5,-1,-1))
    bits=bits[:21]
    if len(bits)!=21: raise ValueError("short graph6")
    return sum((1<<i) for i,b in enumerate(bits) if b)

def adj_of(gm):
    adj=[0]*N
    for e,(i,j) in enumerate(EDGES):
        if gm>>e&1: adj[i]|=1<<j;adj[j]|=1<<i
    return adj

def bmin(gm):
    deg=[0]*N
    for e,(i,j) in enumerate(EDGES):
        if gm>>e&1: deg[i]+=1;deg[j]+=1
    return sum(max(0,2-d) for d in deg)

def alpha4(gm): return not any((gm&m)==0 for m in INDEP5)

def cover4(gm):
    from functools import lru_cache
    @lru_cache(None)
    def rec(rem,k):
        if rem==0:return True
        if k==0:return False
        v=(rem&-rem).bit_length()-1
        for S in CLIQUE_BY_VERTEX[v]:
            em=SUB_EDGE[S]
            if S&rem==S and gm&em==em and rec(rem^S,k-1):return True
        return False
    return rec(ALL,4)

def fiber_profiles(gm):
    adj=adj_of(gm);out=Counter()
    for lab in itertools.product(range(4),repeat=N):
        if all(lab[i]!=lab[j] or (adj[i]>>j&1) for i,j in EDGES):
            out[tuple(sorted(Counter(lab).values(),reverse=True))]+=1
    return out

def aut_order(gm):
    aut=0
    for mp in PERM7_MAPS:
        image=0
        for e,new in enumerate(mp):
            if gm>>e&1:image|=1<<new
        if image==gm:aut+=1
    return aut

def is_connected(gm):
    adj=adj_of(gm);seen=1;front=1
    while front:
        v=(front&-front).bit_length()-1
        front&=front-1
        new=adj[v]&~seen;seen|=new;front|=new
    return seen==ALL

EXPECTED={
 "K4-small":{
 0:(1,105,24,0,{"2,2,2,1":24}),
 1:(3,1785,96,0,{"2,2,2,1":72,"3,2,1,1":24}),
 2:(10,12180,528,0,{"2,2,2,1":360,"3,2,1,1":144,"3,2,2":24}),
 3:(27,43092,2088,6,{"3,2,1,1":696,"2,2,2,1":1320,"3,3,1":24,"3,2,2":48}),
 4:(29,53070,4272,18,{"2,2,2,1":2832,"3,3,1":48,"3,2,1,1":1152,"3,2,2":240}),
 5:(9,11550,2592,8,{"3,2,2":192,"3,2,1,1":696,"2,2,2,1":1632,"3,3,1":72})},
 "K4e-small-Z1-3":{
 1:(3,1785,96,0,{"2,2,2,1":72,"3,2,1,1":24}),
 2:(6,5880,384,0,{"2,2,2,1":264,"3,2,1,1":96,"3,2,2":24}),
 3:(6,3997,696,1,{"3,3,1":24,"3,2,1,1":216,"2,2,2,1":432,"3,2,2":24})}}

def verify_residual(source_path,filtered_path):
    with source_path.open(newline="",encoding="utf-8") as f: source=list(csv.DictReader(f))
    selected=[];result={}
    for branch,zs,cap in (
      ("K4-small",range(6),lambda z:10-2*z),
      ("K4e-small-Z1-3",range(1,4),lambda z:8-2*z)):
        result[branch]={}
        for z in zs:
            rows=[r for r in source if int(r["z"])==z and int(r["bmin"])<=cap(z)]
            types=labelled=maps=connected=0;profiles=Counter()
            for row in rows:
                gm=decode_g6(row["graph6"])
                assert gm.bit_count()==3+z
                assert bmin(gm)==int(row["bmin"])
                assert alpha4(gm) and cover4(gm)
                fp=fiber_profiles(gm)
                assert sum(fp.values())==int(row["F_assignments"])
                aut=aut_order(gm)
                assert aut and 5040%aut==0
                types+=1;labelled+=5040//aut;maps+=sum(fp.values())
                connected+=int(is_connected(gm));profiles.update(fp)
                selected.append({"branch":branch,"z":z,"graph6":row["graph6"],
                                 "bmin":int(row["bmin"]),
                                 "F_assignments":int(row["F_assignments"])})
            got=(types,labelled,maps,connected,dict(sorted(
                (",".join(map(str,k)),v) for k,v in profiles.items())))
            assert got==EXPECTED[branch][z],(branch,z,got,EXPECTED[branch][z])
            result[branch][z]={"types":types,"labelled":labelled,"maps":maps,
                               "connected_types":connected,"profiles":got[4]}
    with filtered_path.open(newline="",encoding="utf-8") as f: saved=list(csv.DictReader(f))
    expected=[{k:str(v) for k,v in r.items()} for r in sorted(
      selected,key=lambda r:(r["branch"],r["z"],r["graph6"]))]
    assert saved==expected,"filtered CSV mismatch"
    return result

def compositions(total,slots):
    if slots==1:
        yield (total,);return
    for x in range(total+1):
        for tail in compositions(total-x,slots-1):yield (x,)+tail

def verify_outer_ledger():
    edges=list(itertools.combinations(range(6),2))
    eidx={e:i for i,e in enumerate(edges)}
    perm_maps=[]
    for p in itertools.permutations(range(6)):
        perm_maps.append([eidx[tuple(sorted((p[i],p[j])))] for i,j in edges])
    cache={(t,k):list(compositions(t,k)) for t in range(5) for k in (6,15)}
    states=Counter();xcounts=Counter();labelledW=defaultdict(set)
    canonicalW=defaultdict(set);allW=set();allCanon=set()
    for xT in range(5):
      for w in cache[(xT,15)]:
        td=[0]*6
        for (i,j),v in zip(edges,w):td[i]+=v;td[j]+=v
        for delta in range(3):
          for dv in cache[(delta,6)]:
            for YS in range(3-delta):
              for sT in range(3-delta-YS):
                for sv in cache[(sT,6)]:
                  yv=tuple(1+sv[j]-td[j]-dv[j] for j in range(6))
                  if min(yv)<0:continue
                  YT=sum(yv);z=2+xT-YS-sT
                  if not 0<=z<=5:continue
                  assert YT==6+sT-2*xT-delta
                  assert delta+YS+sT<=2
                  assert all(td[j]+dv[j]+yv[j]==1+sv[j] for j in range(6))
                  x=24+delta+xT;y=YS+YT
                  assert x+y+z==32
                  sr=y+2*z-8
                  assert sr==2-delta-YS-sT and sr>=0
                  states[z]+=1;xcounts[(z,xT)]+=1
                  labelledW[z].add(w);allW.add(w)
                  best=None
                  for mp in perm_maps:
                    image=[0]*15
                    for old,new in enumerate(mp):image[new]=w[old]
                    image=tuple(image)
                    if best is None or image<best:best=image
                  canonicalW[z].add(best);allCanon.add(best)
    assert dict(states)=={0:28,1:469,2:2272,3:3540,4:1110,5:15}
    assert dict(xcounts)=={
      (0,0):28,(1,0):49,(1,1):420,(2,0):22,(2,1):555,(2,2):1695,
      (3,1):165,(3,2):1365,(3,3):2010,(4,2):180,(4,3):555,(4,4):375,
      (5,3):15}
    assert {z:len(v) for z,v in canonicalW.items()}=={0:1,1:2,2:5,3:8,4:7,5:1}
    assert {z:len(v) for z,v in labelledW.items()}=={0:1,1:16,2:136,3:645,4:615,5:15}
    assert len(allW)==1036 and len(allCanon)==14
    return {"states_by_z":dict(states),
      "xT_by_z":{f"{z}:{xT}":v for (z,xT),v in sorted(xcounts.items())},
      "labelled_weighted_graphs_total":len(allW),
      "isomorphism_types_total":len(allCanon),
      "isomorphism_types_by_z":{z:len(v) for z,v in canonicalW.items()},
      "states_total":sum(states.values())}

def main():
    here=Path(__file__).resolve().parent
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-csv",default=str(here/"M10_RESIDUAL_GRAPH_CATALOG.csv"))
    ap.add_argument("--filtered-csv",default=str(here/"M10_4PLUS6_TIGHT_RESIDUAL_FILTER.csv"))
    a=ap.parse_args()
    residual=verify_residual(Path(a.source_csv),Path(a.filtered_csv))
    outer=verify_outer_ledger()
    print("M10_4PLUS6_TIGHT_RESIDUAL_FILTER_OK")
    print(json.dumps({"residual":residual,"outer_ledger":outer},indent=2,sort_keys=True))
    print("SCOPE: necessary residual and block-degree-sum filters only;")
    print("       no 4+6 cross-grid or full-support Q32 UNSAT claim.")

if __name__=="__main__":main()
