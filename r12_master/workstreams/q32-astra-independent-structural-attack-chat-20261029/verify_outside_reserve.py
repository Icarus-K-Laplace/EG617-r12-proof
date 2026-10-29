"""Independent finite checks and hypothesis countermodels; NOT a Q32 solver."""
import hashlib, itertools as it, json, platform
from pathlib import Path
from math import comb
ROOT=Path(__file__).resolve().parent
def pairs(v): return it.combinations(v,2)
def edge(u,v): return tuple(sorted((u,v)))
def clique_edges(v): return {edge(*p) for p in pairs(v)}
def components(n,E):
    adj=[set() for _ in range(n)]
    for u,v in E: adj[u].add(v); adj[v].add(u)
    unseen=set(range(n)); out=[]
    while unseen:
        stack=[min(unseen)]; unseen.remove(stack[0]); c=[]
        while stack:
            u=stack.pop(); c.append(u)
            for v in adj[u]&unseen:
                unseen.remove(v); stack.append(v)
        out.append(sorted(c))
    return out
def alpha_omega_small(vertices,E):
    vs=list(vertices); alpha=omega=0
    for mask in range(1<<len(vs)):
        s=[v for i,v in enumerate(vs) if mask>>i&1]
        k=len(s)
        if k>alpha and all(edge(u,v) not in E for u,v in pairs(s)): alpha=k
        if k>omega and all(edge(u,v) in E for u,v in pairs(s)): omega=k
    return alpha,omega
def verify_graph(data):
    n=data["n"]; E={edge(*p) for p in data["edges"]}
    assert len(E)==len(data["edges"]) and all(0<=u<v<n for u,v in E)
    O=set(data["O"]); T=list(map(set,data["tracks"])); p=data["pivot"]
    assert len(O)==14 and list(map(len,T))==[11,12,12,12]
    assert len(set.union(O,*T))==61 and sum(map(len,[O]+T))==61
    assert p in O and not any(edge(p,a) in E for a in O-{p})
    assert all(not (clique_edges(t)&E) for t in T)
    # Independent component decomposition; at most11 vertices per component.
    cs=components(n,E)
    aw=[alpha_omega_small(c,E) for c in cs]
    alpha=sum(a for a,w in aw); omega=max(w for a,w in aw)
    b=sum(u in O or v in O for u,v in E)
    return dict(edges=len(E),outside=b,alpha=alpha,omega=omega,
                component_orders=sorted(map(len,cs)))
def equality_countermodel(kind):
    # Two boundary models when omega<=5 is deliberately removed.
    if kind=="two_edges":
        bs=[[0,1],[2,3]]+[[v] for v in range(4,14)]
    else:
        bs=[[0,1,2]]+[[v] for v in range(3,14)]
    # p is an isolated O vertex in both constructions.
    p=13; large=[list(range(14+12*i,26+12*i)) for i in range(3)]
    small=list(range(50,61)); omitted=0
    cs=[]
    for j,B in enumerate(bs):
        c=B+[large[i][j] for i in range(3)]
        if j!=omitted: c += [small[j-1]]
        cs.append(c)
    E=set.union(*(clique_edges(c) for c in cs))
    return dict(kind="hypothesis_countermodel_not_Q32",mode=kind,n=61,
                O=list(range(14)),tracks=[small]+large,pivot=p,edges=sorted(E))
def source_graph(a):
    # Source labels: Ns=0..4, Nt=5..9, x=10, y=5, A0=0..a-1.
    E=clique_edges(range(5))|clique_edges(range(5,10))
    E|={edge(5,v) for v in range(a)}
    E|={edge(10,v) for v in range(a,5)}
    E|={edge(10,v) for v in range(6,10)}
    return E
def sharp_source_example():
    # Find one legal Type-I single-color example attaining57.
    # Exhaustiveness is NOT used: the explicit resulting graph is verified.
    for a in range(1,5):
        GE=source_graph(a)
        for go in it.combinations(range(11),4):
            gh=sorted(set(range(11))-set(go))
            if len(GE&clique_edges(gh))!=12: continue
            for one in gh:
                rem=[v for v in gh if v!=one]
                for perm in it.permutations(rem):
                    gt=[[one],list(perm[:2]),list(perm[2:4]),list(perm[4:])]
                    if any(GE&clique_edges(t) for t in gt): continue
                    O=list(go); T=[list(t) for t in gt]; E=set(GE)
                    for j in range(10):
                        B=list(range(11+5*j,16+5*j))
                        E|=clique_edges(B); O.append(B[0])
                        for k in range(4): T[k].append(B[k+1])
                    d=dict(kind="single_color_sharpness_not_Q32",n=61,a=a,
                           x=10,y=5,A0=list(range(a)),O=sorted(O),
                           tracks=T,pivot=11,edges=sorted(E))
                    stats=verify_graph(d)
                    assert stats["edges"]==129 and stats["outside"]==57
                    assert stats["alpha"]==12 and stats["omega"]==5
                    assert sum(5 in e for e in E)==4+a
                    assert sum(10 in e for e in E)==9-a
                    return d,stats
    raise AssertionError("no sharpness witness found")
def blockers(bs):
    # Compare all 16384 subsets with all maximum independent transversals.
    trans=[sum(1<<v for v in s) for s in it.product(*bs)]
    whole=[sum(1<<v for v in b) for b in bs]
    for mask in range(1<<14):
        hits=all(mask&t for t in trans)
        contains=any(mask&b==b for b in whole)
        assert bool(hits)==contains
    return len(trans),1<<14
def main():
    rows=[14-k+max(2,comb(k,2)) for k in range(14)]
    assert min(rows)==14 and [k for k,v in enumerate(rows) if v==14]==[2,3]
    assert 13+2>14
    proof_checks=[]
    for kind in ["two_edges","triangle"]:
        d=equality_countermodel(kind); s=verify_graph(d)
        assert s["outside"]==56 and s["alpha"]==12 and s["omega"]==6
        O=set(d["O"]); E=set(map(tuple,d["edges"]))
        bs=components(14,{e for e in E if set(e)<=O})
        assert len(bs)==12
        proof_checks.append(dict(mode=kind,blocker_check=blockers(bs),graph=s))
        (ROOT/(kind+"_without_clique_cap.json")).write_text(json.dumps(d,indent=2)+"\n", encoding="utf-8", newline="\n")
    d,s=sharp_source_example()
    (ROOT/"sharp_typeI_single_color.json").write_text(json.dumps(d,indent=2)+"\n", encoding="utf-8", newline="\n")
    # Source parameters checked independently for all four legal a values.
    for a in range(1,5):
        E=source_graph(a)
        assert len(E)==29 and alpha_omega_small(range(11),E)==(2,5)
        assert sum(5 in e for e in E)==4+a
        assert sum(10 in e for e in E)==9-a
    assert 14*47+comb(14,2)==749 and 749-(408-285)==626 and 11*57==627
    print(json.dumps(dict(status="PASS",python=platform.python_version(),
        scope="finite boundary/blocker replay and explicit single-color graphs; no global Q32 SAT/UNSAT",
        equality_cases=proof_checks,sharp_typeI=s,source_parameter=d["a"],
        outside_capacity=626,necessary_non_target_edges=627),indent=2))
if __name__=="__main__": main()

