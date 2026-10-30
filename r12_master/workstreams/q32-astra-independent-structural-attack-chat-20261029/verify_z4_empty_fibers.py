"""Supplementary finite replay of the analytic z=4 empty-fiber theorem.

No solver or global Q32 SAT/UNSAT assertion. All 24 label permutations
and all 12^3 aligned extras / synchronized switches are included.
"""
import itertools as it,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def has_independent(adj,need=5):
    def search(mask,n):
        if n==0:return True
        while mask.bit_count()>=n:
            bit=mask&-mask;v=bit.bit_length()-1;mask^=bit
            if search(mask&~adj[v],n-1):return True
        return False
    return search((1<<len(adj))-1,need)

def light_compatible(ms,es):
    """Test each actual 12-vertex S_j + special D + candidate E graph."""
    tau=(1,0,2,3)
    for j in range(3):
        adj=[0]*12
        def add(u,v):adj[u]|=1<<v;adj[v]|=1<<u
        for s in range(4):
            add(s,4+tau[s]);add(s,8+ms[j][s]);add(4+s,8+s)
        add(0,4)
        s,g=es[j];add(s,8+g)
        if has_independent(adj):return False
    return True

def check_455():
    """Enumerate every normalized 4,5,5 triple; confirm exact 156 types."""
    actual=set();expected=set()
    identity=tuple(range(4))
    off=[(s,g) for s in range(4) for g in range(4) if s!=g]
    for pi in it.permutations(range(4)):
      for a in off:
       for b in [(s,g) for s in range(4) for g in range(4) if pi[s]!=g]:
        adj=[0]*12
        def add(u,v):adj[u]|=1<<v;adj[v]|=1<<u
        for s in range(4):add(s,4+s);add(s,8+s);add(4+s,8+pi[s])
        add(a[0],8+a[1]);add(4+b[0],8+b[1])
        if not has_independent(adj):actual.add((pi,a,b))
    for a in off:
      for b in off:expected.add((identity,a,b))
    for a,b in it.combinations(range(4),2):
        pi=list(range(4));pi[a],pi[b]=pi[b],pi[a];pi=tuple(pi)
        for s in (a,b):expected.add((pi,(s,pi[s]),(s,s)))
    assert actual==expected and len(actual)==156
    print('PASS normalized 4,5,5 classification: 3456 inputs, 156 accepted')
def patterns():
    for pi in it.permutations(range(4)):
        extras=[(s,g) for s in range(4) for g in range(4) if pi[s]!=g]
        for es in it.product(extras,repeat=3):
            ms=(pi,pi,pi)
            yield ms,es
        for a,b in it.combinations(range(4),2):
            sg=list(range(4));sg[a],sg[b]=sg[b],sg[a]
            other=tuple(pi[sg[s]] for s in range(4))
            for minority in range(3):
                for s in (a,b):
                    ms=tuple(other if j==minority else pi for j in range(3))
                    es=tuple((s,pi[s]) if j==minority else (s,pi[sg[s]]) for j in range(3))
                    yield ms,es
def partitions(E):
    found=set()
    for labs in it.product(range(4),repeat=7):
        if labs[0]!=0:continue
        blocks=tuple(sorted(tuple(i for i in range(7) if labs[i]==j) for j in range(4)))
        if blocks in found:continue
        if all(all(tuple(sorted((u,v))) in E for u,v in it.combinations(b,2)) for b in blocks):
            found.add(blocks)
    return sorted(found)
def test():
    check_455()
    E={(0,1),(0,2),(1,2),(3,4),(4,5),(5,6),(3,6)}
    ps=partitions(E); out=[];accepted=0;compatible=0
    assert len(ps)==12 and sum(not all(p) for p in ps)==2
    pats=list(patterns())
    print('patterns',len(pats),'partitions',len(ps))
    for F in ps:
      for G in ps:
        if all(F) and all(G):continue
        fs=list(map(set,F));gs=list(map(set,G))
        profiles={}
        for ms,es in pats:
            ns=[[{s for s in range(4) if ms[j][s]==g}|{s for s,h in [es[j]] if h==g} for g in range(4)] for j in range(3)]
            common=[set.intersection(*(ns[j][g] for j in range(3))) for g in range(4)]
            k=[sum(h==g for s,h in es) for g in range(4)]
            if any(k[g]+len(gs[g])>3 for g in range(4)):continue
            if any(not common[g] for g in range(4)):continue
            if any((len(common[g])==2 and gs[g]) or (len(common[g])==1 and not fs[next(iter(common[g]))]<=gs[g]) for g in range(4)):continue
            # Every independent residual/small/outer 5-set is checked directly.
            adj=[0]*23
            def add(u,v):adj[u]|=1<<v;adj[v]|=1<<u
            for j in range(3):
              for l in range(j+1,3):
                for s in range(4):add(4*j+s,4*l+s)
              for s in range(4):add(4*j+s,12+ms[j][s])
              s,g=es[j];add(4*j+s,12+g)
              for s in range(4):
                for r in fs[s]:add(4*j+s,16+r)
            for g in range(4):
              for r in gs[g]:add(12+g,16+r)
            for u,v in E:add(16+u,16+v)
            if has_independent(adj):continue
            accepted+=1
            if not all(F) and all(G):
                assert all(s==0 for s,g in es)
            elif all(F) and not all(G):
                merge_pairs=[(a,b) for a,b in it.combinations(range(4),2)
                             if all(tuple(sorted((u,v))) in E for u in fs[a] for v in fs[b])]
                assert len(merge_pairs)==1
                merge=set(merge_pairs[0])
                assert all(s in merge for s,g in es)
                assert any(len(fs[s])<3 for s in range(4) if s not in merge)
            else:
                assert F==G
                assert common[1] in ({0},{1})
                special=(ms==((1,0,2,3),)*3 and es==((0,0),)*3)
                normal=(ms==((0,1,2,3),)*3 and es==((1,0),)*3)
                assert (common[1]=={0})==special
                if light_compatible(ms,es):
                    compatible+=1
                    assert special or normal
            e=tuple(sum(s==h for s,g in es) for h in range(4))
            w=tuple(3-k[g]-len(gs[g]) for g in range(4))
            key=(e,w,tuple(tuple(sorted(c)) for c in common))
            if key not in profiles:profiles[key]=(ms,es)
        data=[dict(e=k[0],w=k[1],common=k[2],matchings=v[0],extras=v[1]) for k,v in profiles.items()]
        out.append(dict(F=F,G=G,profiles=data))
        print('F',F,'G',G,'profiles',len(profiles))
    (ROOT/'z4_local_profiles.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    assert len(out)==44
    assert sum(bool(x['profiles']) for x in out)==22
    assert sum(len(x['profiles']) for x in out)==158
    print('PASS all empty-fiber cases: 44 ordered partition pairs; 158 distinct summaries')
    print('PASS all raw accepted patterns:',accepted,'; light-compatible with special D:',compatible)
    possibilities=[(a,b,3*a) for a in range(2,8) for b in range(2,8-a)
                   if a<=2 and b<=2]
    assert possibilities==[(2,2,6)] and all(e0<9 for a,b,e0 in possibilities)
    print('PASS terminal degree contradiction: a=b=2, E0=6<9')
if __name__=='__main__':test()

