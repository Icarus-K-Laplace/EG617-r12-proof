"""Supplementary exhaustive local replay for C3+2P2 and C3+P4.

The analytic theorem is in COLORED_PACKING_OBSTRUCTION.md Section6.
Each eligible residual vertex may use its one extra incidence in this block
or outside it; the total in this block is at most two. No global SAT claim.
"""
import itertools as it
import json
from pathlib import Path
from verify_z4_empty_fibers import partitions,has_independent
from verify_z3_two_triangles import features,light_compatible
ROOT=Path(__file__).resolve().parent

def test():
    pats=features();results=[]
    standard=dict(ms=((1,0,2,3),)*3,es=((0,0),)*3)
    normal=dict(ms=((0,1,2,3),)*3,es=((1,0),)*3)
    T={0,1,2}
    for name,path_edges in [('C3+2P2',{(3,4),(5,6)}),('C3+P4',{(3,4),(4,5),(5,6)})]:
        R={(0,1),(0,2),(1,2)}|path_edges
        eligible=[r for r in range(7) if sum(r in e for e in R)==1]
        ps=partitions(R);cases=[];total=0;diverts=0;light_checks=0
        assert sum(not all(p) for p in ps)==1
        for F in ps:
          for G in ps:
            if all(F) and all(G):continue
            fs=list(map(set,F));gs=list(map(set,G))
            choices=[]
            for options in it.product(*[[-1]+[g for g in range(4) if r not in gs[g]] for r in eligible]):
                extra=tuple((r,g) for r,g in zip(eligible,options) if g>=0)
                if len(extra)>2:continue
                N=[b|{r for r,h in extra if h==g} for g,b in enumerate(gs)]
                if max(map(len,N))>3:continue
                choices.append((extra,N))
            accepted=0;example=None
            for P in pats:
              if any(P['k'][g]+len(gs[g])>3 for g in range(4)):continue
              for extra,N in choices:
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
                accepted+=1;total+=1
                if not all(F) and not all(G):
                    assert F==G and F==((),(0,1,2),(3,4),(5,6))
                    assert P['common'][1] in ({0},{1})
                    if P['common'][1]=={0}:
                        diverts+=1
                        assert P['ms']==standard['ms'] and P['es']==standard['es']
                    if light_compatible(P,standard):
                        light_checks+=1
                        assert any(P['ms']==Q['ms'] and P['es']==Q['es'] for Q in [standard,normal])
                elif not all(F):
                    if T in gs:
                        assert P['common'][gs.index(T)]=={fs.index(T)}
                    else:
                        assert all(s==0 for s,g in P['es'])
                else:
                    if T in fs:
                        assert P['common'][gs.index(T)]=={fs.index(T)}
                    else:
                        triangle_labels={s for s,b in enumerate(fs) if b<=T}
                        assert len(triangle_labels)==2
                        assert all(s in triangle_labels for s,g in P['es'])
                if example is None:
                    example=dict(matchings=P['ms'],extras=P['es'],residual_extra=extra)
            cases.append(dict(F=F,G=G,residual_neighborhood_choices=len(choices),
                              raw_accepted=accepted,example=example))
            print(name,'F',F,'G',G,'accepted',accepted)
        assert total>0 and diverts>0 and light_checks>0
        results.append(dict(residual=name,partitions=len(ps),ordered_cases=len(cases),
                            raw_patterns=len(pats),raw_accepted=total,
                            special_diversions=diverts,special_light_neighbors=light_checks,cases=cases))
        print('PASS',name,'local assertions;',total,'accepted;',diverts,'special diversions;',light_checks,'special light neighbors')
    # The analytic final count uses only these five integer constraints.
    counts=[(a,b,3*a) for a in range(2,8) for b in range(2,8-a) if a<=2 and b<=2]
    assert counts==[(2,2,6)] and counts[0][2]<9
    (ROOT/'triangle_matching_verification.json').write_text(json.dumps(dict(
        scope='Supplementary local replay, not full Q32 assignments or a full-model UNSAT certificate',
        results=results,terminal_count=counts,result='PASS'),indent=2)+'\n',encoding='utf-8',newline='\n')
    print('PASS terminal contradiction E0=6<9 for both cells')
if __name__=='__main__':test()
