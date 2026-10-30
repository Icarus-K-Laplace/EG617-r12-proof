"""Independent local replay for the 2C3+K1,z3 analytic obstruction.

Imports only the finite pattern generator, clique partition enumerator and
exact independent-set routine; no external solver or full coloring claim.
"""
import itertools as it
import json
from pathlib import Path
from verify_z4_empty_fibers import patterns,partitions,has_independent
ROOT=Path(__file__).resolve().parent

def light_compatible(P,Q):
    for j in range(3):
        adj=[0]*12
        def add(u,v):adj[u]|=1<<v;adj[v]|=1<<u
        for s in range(4):
            add(s,4+P['ms'][j][s]);add(s,8+Q['ms'][j][s]);add(4+s,8+s)
        s,g=P['es'][j];add(s,4+g)
        s,g=Q['es'][j];add(s,8+g)
        if has_independent(adj):return False
    return True

def features():
    out=[]
    for ms,es in patterns():
        ns=[[{s for s in range(4) if ms[j][s]==g}|{s for s,h in [es[j]] if h==g}
             for g in range(4)] for j in range(3)]
        common=[set.intersection(*(ns[j][g] for j in range(3))) for g in range(4)]
        k=[sum(h==g for s,h in es) for g in range(4)]
        out.append(dict(ms=ms,es=es,common=common,k=k))
    return out

def test():
    R={(0,1),(0,2),(1,2),(3,4),(3,5),(4,5)}
    ps=partitions(R); pats=features()
    assert len(ps)==7 and sum(not all(p) for p in ps)==1
    accepted=0;cases=[];equal=[]
    for F in ps:
      for G in ps:
        if all(F) and all(G):continue
        fs=list(map(set,F));gs=list(map(set,G));rows=[]
        rg=next(g for g in range(4) if 6 in gs[g])
        choices=[c for n in range(3) for c in it.combinations([g for g in range(4) if g!=rg],n)]
        for P in pats:
          if any(P['k'][g]+len(gs[g])>3 for g in range(4)):continue
          for extra in choices:
            N=[b|({6} if g in extra else set()) for g,b in enumerate(gs)]
            if any(P['k'][g]+len(N[g])>3 for g in range(4)):continue
            if any(not c or (len(c)==2 and N[g]) or
                   (len(c)==1 and not fs[next(iter(c))]<=N[g])
                   for g,c in enumerate(P['common'])):continue
            adj=[0]*23
            def add(u,v):adj[u]|=1<<v;adj[v]|=1<<u
            for j in range(3):
                for l in range(j+1,3):
                    for s in range(4):add(4*j+s,4*l+s)
                for s in range(4):add(4*j+s,12+P['ms'][j][s])
                s,g=P['es'][j];add(4*j+s,12+g)
                for s in range(4):
                    for r in fs[s]:add(4*j+s,16+r)
            for g in range(4):
                for r in N[g]:add(12+g,16+r)
            for u,v in R:add(16+u,16+v)
            if has_independent(adj):continue
            accepted+=1
            Q=dict(P,extra=extra)
            if all(F) or all(G):
                T=next(b for b in F if len(b)==3 and b in G)
                s=F.index(T);g=G.index(T)
                assert P['common'][g]=={s}
            else:
                assert F==G and F==((),(0,1,2),(3,4,5),(6,))
                assert P['common'][1] in ({0},{1}) and P['common'][2] in ({0},{2})
                kind=1 if P['common'][1]=={0} else (2 if P['common'][2]=={0} else 0)
                assert not (P['common'][1]=={0} and P['common'][2]=={0})
                Q['kind']=kind
                if kind:
                    if not extra:
                        tau=list(range(4));tau[0],tau[kind]=tau[kind],tau[0]
                        assert P['ms']==(tuple(tau),)*3 and P['es']==((0,0),)*3
                    else:
                        assert len(extra)==1 and all(s==3 for s,g in P['es'])
                equal.append(Q)
            rows.append(dict(matchings=P['ms'],extras=P['es'],residual_extra_columns=extra,
                             common=[sorted(c) for c in P['common']]))
        cases.append(dict(F=F,G=G,accepted=len(rows)))
        print('F',F,'G',G,'accepted',len(rows))
    assert len(cases)==13
    A=[P for P in equal if P['kind']==1];B=[P for P in equal if P['kind']==2]
    assert A and B
    assert all(not light_compatible(P,Q) for P in A for Q in B)
    print('PASS every opposite-diversion pair is incompatible with a light outer pair:',len(A)*len(B))
    standards={i:next(P for P in equal if P['kind']==i and not P['extra']) for i in (1,2)}
    for P in equal:
      if P['kind']==0:
        for i in (1,2):
          if light_compatible(P,standards[i]):
            assert P['ms']==((0,1,2,3),)*3 and P['es']==((i,0),)*3
        assert not all(light_compatible(P,standards[i]) for i in (1,2))
    print('PASS no remaining normal block is light-compatible with both special standards')
    possibilities=[(a,b) for a in range(2,8) for b in range(2,8-a) if a<=2 and b<=2]
    assert possibilities==[(2,2)] and 7-sum(possibilities[0])==3
    output=dict(residual='2C3+K1',raw_patterns=len(pats),partition_cases=cases,
                total_raw_accepted=accepted,equal_partition_accepted=len(equal),
                diverted_counts=[len(A),len(B)],opposite_pairs_checked=len(A)*len(B),
                equal_partition_assignments=[dict(matchings=P['ms'],extras=P['es'],
                    residual_extra_columns=P['extra'],kind=P['kind'],
                    common=[sorted(c) for c in P['common']]) for P in equal],
                result='PASS supplementary local verification; analytic contradiction uses parent clique cap')
    (ROOT/'z3_two_triangles_verification.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('PASS',len(cases),'partition cases;',accepted,'raw accepted configurations;',len(equal),'equal-partition configurations')
if __name__=='__main__':test()
