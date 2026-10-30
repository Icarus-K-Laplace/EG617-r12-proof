"""Independent finite checks for the universal core proof and source audit.

No solver. Analytic nonexistence is in UNIVERSAL_Q32_THEOREM.md, not inferred
from search failure. Search graphs are checked from their
edge lists by direct subset enumeration, without importing the search code.
"""
import itertools as it,json,hashlib,platform
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def p(r,n):
    q,s=divmod(n,r)
    return s*q*(q+1)//2+(r-s)*q*(q-1)//2

def canon(supports):
    return min(tuple(sorted(tuple(sorted(pi[i] for i in s)) for s in supports))
               for pi in it.permutations(range(4)))

def verify_templates():
    opts=[s for k in range(2,5) for s in it.combinations(range(4),k)]
    classes={h:set() for h in (3,4,5)}
    for h in classes:
        for S in it.combinations_with_replacement(opts,h):
            if sum(map(len,S))!=h+5:continue
            degrees=[sum(i in s for s in S) for i in range(4)]
            if min(degrees)<2:continue
            classes[h].add(canon(S))
    assert classes[3]=={canon([(0,1,2,3),(0,1),(2,3)]),canon([(0,1),(0,2,3),(1,2,3)])}
    for S in classes[4]:
        d=[sum(i in s for s in S) for i in range(4)]
        assert sorted(d)==[2,2,2,3]
        center=d.index(3);low=set(range(4))-{center}
        if not any(len(s)==2 and set(s)<=low for s in S):
            assert set(S)=={tuple(sorted(low))}|{tuple(sorted((center,i))) for i in low}
    remaining=[]
    for S in classes[5]:
        d=[sum(i in s for s in S) for i in range(4)]
        if sorted(d)!=[2,2,3,3]:continue
        low={i for i in range(4) if d[i]==2}
        if any(set(s)==low for s in S):continue
        remaining.append(S)
    expected={canon([(0,1),(0,2),(0,3),(1,2),(1,3)]),
              canon([(0,1),(0,2),(0,2),(1,3),(1,3)])}
    assert set(remaining)==expected
    return dict(pre_reduction_orbit_counts={h:len(v) for h,v in classes.items()},
                all_support_orbits={h:sorted(v) for h,v in classes.items()},
                intermediate_support_orbits=sorted(remaining),
                surviving_templates_after_analytic_obstructions=[])

def verify_final_obstructions():
    mixed=[];diamond=[]
    for a in range(1,10):
        for b in range(1,11):
            mixed.append((max(0,9-a-b)+a*max(0,b-3)+b*max(0,a-2),a,b))
            diamond.append((max(0,9-a-b)+a*max(0,b-2)+b*max(0,a-2),a,b))
    assert min(v for v,a,b in mixed)==4
    assert min(v for v,a,b in diamond)==5
    # D local degree accounting: adjacent support edges lead to distinct cliques.
    # K10: just one adjacent K10 can have missing-set size zero.
    # K11: two adjacent K10s; if both sizes vanish the target RHS is zero.
    local_cases=0
    for neighbor_sizes in ([range(10),range(1,11),range(1,11)],
                           [range(10),range(10)]):
        for sizes in it.product(*neighbor_sizes):
            for mask in range(1<<len(sizes)):
                selected=[sizes[i] for i in range(len(sizes)) if mask>>i&1]
                lhs=max(0,sum(a-1 for a in selected))
                rhs=sum(max(0,a-2) for a in selected)
                assert lhs>=rhs
                local_cases+=1
    mixed_edges=[(0,2),(0,3),(1,2),(1,3)]
    completion_masks=[]
    for mask in range(16):
        completing=[e for k,e in enumerate(mixed_edges) if mask>>k&1]
        if any(sum(i in e for e in completing)>1 for i in (0,1)):continue
        assert 4-len(completing)>=2
        completion_masks.append(mask)
    assert 2*4>6 and 2*5>6
    return dict(mixed_pair_cases=len(mixed),mixed_pair_minimum=4,
                diamond_pair_cases=len(diamond),diamond_pair_minimum=5,
                diamond_local_accounting_cases=local_cases,
                diamond_allowed_completion_masks=completion_masks,
                double_template_required_excess=8,
                diamond_template_required_excess=10,available_excess=6)

def source_graph(a):
    E=set()
    for j in range(12):E.update(it.combinations(range(5*j,5*j+5),2))
    Ns=list(range(50,55));Nt=list(range(55,60));y=55;x=60
    E.update(tuple(sorted((y,v))) for v in Ns[:a])
    E.update(tuple(sorted((x,v))) for v in Ns[a:]+Nt[1:])
    return E

def verify_source():
    results=[]
    for a in range(1,5):
        E=source_graph(a);degree=[sum(v in e for e in E) for v in range(61)]
        assert len(E)==129 and degree[55]==4+a and degree[60]==9-a
        assert all(d==4 for d in degree[:50]) and min(degree[50:])>=5
        alpha=omega=0
        gadget=list(range(50,61))
        for mask in range(1<<11):
            S=[gadget[i] for i in range(11) if mask>>i&1]
            pairs=list(it.combinations(S,2))
            if all(e not in E for e in pairs):alpha=max(alpha,len(S))
            if all(e in E for e in pairs):omega=max(omega,len(S))
        assert alpha==2 and omega==5
        results.append(dict(a=a,edges=len(E),alpha=10+alpha,omega=omega,variable_degrees=[degree[55],degree[60]]))
    # Source occupancy exhaustiveness, not endpoint-labelled completion search.
    outside=[]
    for deficit in (1,2):
        for choices in it.combinations_with_replacement(range(12),deficit):
            b=[1]*12
            for i in choices:b[i]+=1
            outside.append(dict(x_location='O' if deficit==1 else 'H',b=b))
    assert len(outside)==90
    assert sum(x['x_location']=='O' for x in outside)==12
    assert sum(x['x_location']=='H' and max(x['b'])==3 for x in outside)==12
    assert sum(x['x_location']=='H' and max(x['b'])==2 for x in outside)==66
    return dict(parameters=results,occupancy_counts=dict(x_outside=12,two_doubles=66,one_triple=12))

def verify_search():
    path=ROOT/'core_search_results.json'
    if not path.exists():raise RuntimeError('bounded-search output missing')
    out=[]
    for case in json.loads(path.read_text(encoding='utf-8')):
        E={tuple(e) for e in case['edges']};assert len(E)==285
        adj=[set() for _ in range(47)]
        for u,v in E:
            assert 0<=u<v<47;adj[u].add(v);adj[v].add(u)
        deg=list(map(len,adj));assert min(deg)==12 and sum(d-12 for d in deg)==6
        G=case['groups'];seeds=[g[0] for g in G]
        assert sorted(map(len,G))==[10,10,11,11]
        for g in G:assert all(v in adj[u] for u,v in it.combinations(g,2))
        for z,s in zip(range(42,47),case['supports']):
            assert {i for i,v in enumerate(seeds) if v in adj[z]}==set(s)
        for i,s in enumerate(seeds):
            assert deg[s]==12
            assert all(not(adj[v]&set(seeds)-{s}) for v in G[i] if v!=s)
        n_i=0;witness=None
        for S in it.combinations(range(47),5):
            if all(v not in adj[u] for u,v in it.combinations(S,2)):
                n_i+=1
                if witness is None:witness=S
        n_k=0;k_witness=None
        for v in range(47):
            for tail in it.combinations(sorted(u for u in adj[v] if u>v),11):
                if all(y in adj[x] for x,y in it.combinations(tail,2)):
                    n_k+=1
                    if k_witness is None:k_witness=(v,)+tail
        assert n_i==case['independent5_count'] and n_k==case['clique12_count']
        assert n_i+100*n_k==case['best_energy']
        out.append(dict(template=case['template'],edges=285,minimum_degree=min(deg),
                        independent5_count=n_i,independent5_witness=witness,
                        clique12_count=n_k,clique12_witness=k_witness,
                        full_core_contract_pass=(n_i==0 and n_k==0)))
    return out

def main():
    low=[p(3,47-q)+12*q+6-q*(q-1)//2 for q in range(1,7)]
    assert low==[348,344,340,335,329,323] and min(low)>285
    assert 25*24//2-(25*25//4-25//2+1)==155>153
    pair=[(max(0,10-a-b)+a*max(0,b-2)+b*max(0,a-2),a,b)
          for a in range(1,11) for b in range(1,11)]
    assert min(x[0] for x in pair)==6 and [(a,b) for v,a,b in pair if v==6]==[(2,2)]
    star=[(max(0,9-a-b)+a*(b-1)+b*max(0,a-2),a,b)
          for a in range(1,10) for b in range(1,11)]
    assert min(x[0] for x in star)==6
    assert 2*(10*9//2)+2*(11*10//2)+10==210 and 285-210==75
    assert 38*37//2-2*(9*8//2)-2*(10*9//2)==541
    assert 541+38*5+5*4//2==741
    source=verify_source();templates=verify_templates();search=verify_search()
    final=verify_final_obstructions()
    result=dict(status='PASS finite checks supporting analytic Q32 core nonexistence',python=platform.python_version(),
                low_degree_independent4_bounds=low,common_antineighborhood_25_bounds=[155,153],
                pair_K11_integer_cases=len(pair),star_integer_cases=len(star),
                source=source,templates=templates,final_obstructions=final,bounded_search_recheck=search)
    (ROOT/'verification_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('PASS',json.dumps({k:v for k,v in result.items() if k not in ['source','templates','bounded_search_recheck']}))
    print('SUPPORT_ORBITS',templates['pre_reduction_orbit_counts'],'INTERMEDIATE',len(templates['intermediate_support_orbits']),
          'SURVIVING',len(templates['surviving_templates_after_analytic_obstructions']))
    print('SEARCH_RECHECK',json.dumps(search))

if __name__=='__main__':main()
