"""Bounded adversarial search in the two universal core normal forms.

Degree-preserving switches minimize independent5 and clique12 counts.
Failure to find energy zero is NOT an infeasibility proof.
"""
import itertools as it,json,math,random,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
N=47;FULL=(1<<N)-1

def count_sets(adj,mask,k):
    if k==0:return 1
    if mask.bit_count()<k:return 0
    if k==1:return mask.bit_count()
    total=0
    while mask.bit_count()>=k:
        bit=mask&-mask;v=bit.bit_length()-1;mask^=bit
        total+=count_sets(adj,mask&adj[v],k-1)
    return total

def initial(template,rng):
    sizes=[10,10,11,11];groups=[];start=0
    for n in sizes:groups.append(list(range(start,start+n)));start+=n
    Z=list(range(42,47));seeds=[g[0] for g in groups]
    supports=([(0,1),(0,2),(0,2),(1,3),(1,3)] if template=='double'
              else [(0,1),(0,2),(0,3),(1,2),(1,3)])
    fixed=set()
    for g in groups:fixed.update(it.combinations(g,2))
    for z,support in zip(Z,supports):
        for i in support:fixed.add(tuple(sorted((z,seeds[i]))))
    private=[v for g in groups for v in g[1:]]
    group={v:i for i,g in enumerate(groups) for v in g}
    mutable=set(it.combinations(Z,2))|{tuple(sorted((u,z))) for u in private for z in Z}
    mutable|={tuple(sorted((u,v))) for u,v in it.combinations(private,2) if group[u]!=group[v]}
    for attempt in range(10000):
        high=set(rng.sample(private,6));need={v:12+(v in high) for v in range(N)}
        for u,v in fixed:need[u]-=1;need[v]-=1
        edges=set();ok=True
        # Choose a small initial graph on the five exceptional vertices.
        order=Z[:];rng.shuffle(order)
        for i in range(5):
            u,v=sorted((order[i],order[(i+1)%5]));edges.add((u,v));need[u]-=1;need[v]-=1
        for z in rng.sample(Z,len(Z)):
            choices=[v for v in private if need[v]>0]
            if len(choices)<need[z]:ok=False;break
            chosen=rng.sample(choices,need[z])
            for v in chosen:edges.add(tuple(sorted((v,z))));need[v]-=1
            need[z]=0
        if not ok:continue
        while any(need[v]>0 for v in private):
            u=max(private,key=lambda v:need[v]+rng.random()*.1 if need[v]>0 else -1)
            choices=[v for v in private if v!=u and need[v]>0 and group[v]!=group[u]
                     and tuple(sorted((u,v))) not in edges]
            if len(choices)<need[u]:ok=False;break
            choices.sort(key=lambda v:need[v]+rng.random(),reverse=True)
            for v in choices[:need[u]]:edges.add(tuple(sorted((u,v))));need[v]-=1
            need[u]=0
        if ok and all(x==0 for x in need.values()):
            return fixed,edges,mutable,groups,supports,high
    raise RuntimeError('initial degree realization failed')

def run(template,seed,steps):
    rng=random.Random(seed);fixed,edges,allowed,groups,supports,high=initial(template,rng)
    adj=[0]*N
    for u,v in fixed|edges:adj[u]|=1<<v;adj[v]|=1<<u
    comp=[FULL^adj[v]^(1<<v) for v in range(N)]
    indep=count_sets(comp,FULL,5);cliques=count_sets(adj,FULL,12);energy=indep+100*cliques
    initial_energy=energy;best=energy;bestedges=set(edges);history=[];accepted=0
    def flip(u,v,add):
        non=comp[u]&comp[v]&~((1<<u)|(1<<v))
        common=adj[u]&adj[v]
        a=count_sets(comp,non,3);b=count_sets(adj,common,10)
        adj[u]^=1<<v;adj[v]^=1<<u;comp[u]^=1<<v;comp[v]^=1<<u
        return (-a+100*b) if add else (a-100*b)
    started=time.monotonic()
    for step in range(steps):
        p,q=rng.sample(tuple(edges),2);a,b=p;c,d=q
        if len({a,b,c,d})<4:continue
        if rng.randrange(2):c,d=d,c
        r=tuple(sorted((a,c)));s=tuple(sorted((b,d)))
        if r not in allowed or s not in allowed or r in edges or s in edges:continue
        delta=flip(*p,False)+flip(*q,False)+flip(*r,True)+flip(*s,True)
        temperature=max(.15,8*(1-(step%5000)/5000))
        if delta<=0 or rng.random()<math.exp(-delta/temperature):
            edges.remove(p);edges.remove(q);edges.add(r);edges.add(s);energy+=delta;accepted+=1
            if energy<best:
                best=energy;bestedges=set(edges)
                if len(history)<200:history.append([step,best])
                if best==0:break
        else:
            flip(*s,False);flip(*r,False);flip(*q,True);flip(*p,True)
    adj=[0]*N
    for u,v in fixed|bestedges:adj[u]|=1<<v;adj[v]|=1<<u
    comp=[FULL^adj[v]^(1<<v) for v in range(N)]
    final_i=count_sets(comp,FULL,5);final_k=count_sets(adj,FULL,12)
    assert best==final_i+100*final_k
    degrees=[x.bit_count() for x in adj]
    assert min(degrees)==12 and sum(degrees)==570
    result=dict(template=template,seed=seed,requested_steps=steps,accepted_switches=accepted,
                elapsed_seconds=round(time.monotonic()-started,3),initial_energy=initial_energy,
                best_energy=best,independent5_count=final_i,clique12_count=final_k,
                groups=groups,supports=supports,high_vertices=sorted(high),degrees=degrees,
                edges=sorted(fixed|bestedges),improvements=history,
                status='CORE_WITNESS_FOUND' if best==0 else 'BOUNDED_SEARCH_NO_WITNESS; NOT_UNSAT')
    print({k:v for k,v in result.items() if k not in ['groups','supports','degrees','edges','improvements','high_vertices']},flush=True)
    return result

if __name__=='__main__':
    results=[run(t,s,30000) for t,s in [('double',61712),('diamond',61713)]]
    (ROOT/'core_search_results.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8',newline='\n')
