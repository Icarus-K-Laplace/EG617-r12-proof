"""Independent audit, not a formal proof. Standard library only; no source imports.

The reference recurrences are executed in separate processes ONLY after our
table has been computed. Their values never influence this implementation.
All writes are confined to this script's directory.
"""
from pathlib import Path
from itertools import combinations, combinations_with_replacement, product, permutations
from math import comb
from functools import lru_cache
import hashlib
import json
import platform
import random
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SOURCE_REL = 'r12_master/workstreams/astra-global-root-integration-chat-20261031'
SOURCE = REPO / SOURCE_REL
PIN = 'c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2'
SEED = 20261031617
random.seed(SEED)

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def digest(data):
    return hashlib.sha256(data).hexdigest()

def blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def integrity():
    files = []
    checkout_conversions=[]
    for p in sorted(SOURCE.rglob('*')):
        if not p.is_file():
            continue
        rel = p.relative_to(REPO).as_posix()
        worktree_data = p.read_bytes()
        data = git('show', f'{PIN}:{rel}')
        expected = git('rev-parse', f'{PIN}:{rel}').decode().strip()
        assert blob(data) == expected, rel
        if worktree_data != data:
            assert worktree_data.replace(b'\r\n',b'\n') == data, ('non-newline checkout difference',rel)
            checkout_conversions.append(rel)
        files.append(dict(path=rel, blob=expected, sha256=digest(data), bytes=len(data)))
    manifest = json.loads((SOURCE/'SOURCE_MANIFEST.json').read_text())
    for entry in manifest:
        original = git('show', entry['commit']+':'+entry['source_path'])
        frozen = git('show',PIN+':'+SOURCE_REL+'/'+entry['destination'])
        assert original == frozen
        assert blob(original) == entry['blob']
    frozen_paths={p.relative_to(SOURCE).as_posix() for p in (SOURCE/'frozen').rglob('*') if p.is_file()}
    assert frozen_paths=={entry['destination'] for entry in manifest}
    extra_commit='f56cc9eba646e71d63c4b55f468a2340bcdd64c2'
    extra_path='r12_master/workstreams/astra-q32-v47-universal-attack-chat-20261030/UNIVERSAL_Q32_THEOREM.md'
    extra=git('show',extra_commit+':'+extra_path)
    extra_sha=git('rev-parse',extra_commit+':'+extra_path).decode().strip()
    assert blob(extra)==extra_sha
    checked = 0
    for line in (SOURCE/'SHA256SUMS.txt').read_text().splitlines():
        sha, path = line.split(None, 1)
        assert digest(git('show',PIN+':'+SOURCE_REL+'/'+path.strip())) == sha, path
        checked += 1
    parents = git('show','-s','--format=%H %P',PIN).decode().strip()
    changes = git('diff','--name-status','b0459807acd4b7e386148056ddf77d7998918893',PIN).decode().splitlines()
    assert all(line.split('\t')[1].startswith(SOURCE_REL+'/') for line in changes)
    return dict(status='COMPUTATIONALLY_VERIFIED', pinned_commit=PIN,
                files=files, manifest_entries=len(manifest), checksums=checked,
                parent_line=parents, changes_from_global_root=changes,
                checkout_CRLF_conversions=checkout_conversions,
                supplemental_exact285_source=dict(commit=extra_commit,path=extra_path,blob=extra_sha,sha256=digest(extra)),
                hash_basis='raw git show bytes; checkout is compared modulo CRLF only')

def pairs(n):
    return n*(n-1)//2

def minimum_edges(n, alpha):
    # Sum the sizes of previously placed vertices in a balanced clique packing.
    return sum(i//alpha for i in range(n))

def cap(n):
    return pairs(n)-11*minimum_edges(n,12)

def ceil_ratio(x,y):
    return -((-x)//y)

def recurrence():
    B = {(0,n): None for n in range(146)}
    B[0,0] = 0
    orders = {0:0}
    initial = {(2,23):131,(3,35):210,(3,36):234,(4,47):284,(4,48):308}
    for a in range(1,13):
        B[a,0]=0
        for n in range(1,146):
            B[a,n]=None
            if B[a,n-1] is None or n>{1:11,2:23,3:36,4:48}.get(a,145):
                continue
            row_values=[]
            for m in range(n):
                h=n-1-m
                core=B[a-1,m]
                if core is None:
                    continue
                common=max(minimum_edges(h,10), pairs(h)-cap(h), pairs(h+1)-cap(h+1))
                if h>=11:
                    beta=max(m-orders[a-2],0)
                    if core+beta>cap(m+2):
                        continue
                    matching=max(ceil_ratio(h-10,2),1+int(h>=12)+int(h>=13))
                    common=max(common,beta-1,*[t*beta-pairs(2*t)+minimum_edges(2*t,a) for t in range(1,matching+1)])
                    channels=[max(common,*[t*beta-t*t for t in range(1,matching+1)])]
                    if a>=3:
                        gamma=max(m-orders[a-3],0)
                        if core+gamma<=cap(m+3):
                            channels.append(max(common,gamma-3))
                    common=min(channels)
                row_values.append(max(ceil_ratio(n*h,2),core+pairs(h+1)+common))
            if row_values:
                value=max(min(row_values),minimum_edges(n,a),initial.get((a,n),0),
                          ceil_ratio(n*B[a,n-1],n-2) if n>2 else 0)
                if value<=cap(n):
                    B[a,n]=value
        orders[a]=max(n for n in range(146) if B[a,n] is not None)
    nodes=[dict(a=a,n=n,bound=B[a,n]) for a in range(1,13) for n in range(146)]
    retained=json.loads((SOURCE/'FRONTEND_REPLAY.json').read_text())
    assert nodes==retained['nodes']
    # Run the unmodified source text in separate Python processes; no importing
    # modules/functions from the reference implementations into this program.
    adapters={
      'recurrence_a.py': '\nimport json\nt,_,_=compute()\nprint(json.dumps([None if t[a][n]>=INF else t[a][n] for a in range(1,13) for n in range(146)]))\n',
      'recurrence_b.py': '\nimport json\nt=replay()["bounds"]\nprint(json.dumps([t[a,n] for a in range(1,13) for n in range(146)]))\n'}
    comparisons={}
    for name,adapter in adapters.items():
        code=(SOURCE/'frozen/frontend'/name).read_text()+adapter
        data=subprocess.check_output([sys.executable,'-B','-c',code],cwd=HERE)
        reference=json.loads(data)
        assert reference==[v['bound'] for v in nodes],name
        comparisons[name]=len(reference)
    stops=[]
    for d,j in product(range(12),repeat=2):
        a,n=11-j,144-d-12*j
        budget=870-pairs(d+1)-66*j
        lower=B[a,n]
        stops.append(dict(d=d,j=j,a=a,n=n,bound=lower,budget=budget,
                          excluded=lower is None or lower>budget))
    survivors=[s for s in stops if not s['excluded']]
    assert survivors==[dict(d=11,j=6,a=5,n=61,bound=397,budget=408,excluded=False)]
    return dict(status='COMPUTATIONALLY_VERIFIED',nodes=nodes,stops=stops,
                survivors=survivors,reference_comparisons=comparisons,maxima=orders)

PERM3=list(permutations(range(3)))
MAP3=[[sum(1<<j for j in range(3) if mask&(1<<p[j])) for mask in range(8)] for p in PERM3]

def canon(weights,rows):
    return min((tuple(weights[i] for i in p),tuple(sorted((mapping[m],g) for m,g in rows)))
               for p,mapping in zip(PERM3,MAP3))

@lru_cache(None)
def decoration_options(number,floor,budget):
    # Weakly increasing lists enumerate the multisets on identical row types.
    if number==0:
        return (((),0),)
    ans=[]
    def visit(prefix,last,left):
        if len(prefix)==number:
            ans.append((tuple(prefix),sum(prefix)))
            return
        slots=number-len(prefix)
        for g in range(last,left//slots+1):
            visit(prefix+[g],g,left-g)
    visit([],floor,budget)
    return tuple(ans)

def shell_replay(q):
    states=set(); vector_count=0; filtered=0; allocations=0
    # Stars and bars: select seven separator positions from seventeen slots.
    for bars in combinations(range(17),7):
        walls=(-1,)+bars+(17,)
        count=tuple(walls[i+1]-walls[i]-1 for i in range(8))
        vector_count+=1
        z=sum(count[m]*m.bit_count() for m in range(8))
        if not 22<=z<=q:
            continue
        if any(sum(count[m] for m in range(8) if m&s)<s.bit_count() for s in range(1,8)):
            continue
        filtered+=1
        degrees=tuple(sum(count[m] for m in range(8) if m&(1<<i)) for i in range(3))
        G=q-z
        for hub_g in product(range(G+1),repeat=3):
            budget=G-sum(hub_g)
            if budget<0: continue
            weights=tuple(degrees[i]+hub_g[i] for i in range(3))
            groups=[]
            for mask in range(8):
                if not count[mask]: continue
                d=mask.bit_count()
                neighbors=[i for i in range(3) if mask&(1<<i)]
                floor=max([0]+[12-d-weights[i] for i in neighbors])
                if sum(weights[i] for i in neighbors)<d*(12-d):
                    floor=max(floor,1)
                groups.append((mask,count[mask],floor))
            if sum(c*f for m,c,f in groups)>budget: continue
            # Build all allowed decorated type multisets by a cost-bounded DP.
            partial={0:[()]}
            for mask,c,floor in groups:
                nxt={}
                for used,lists in partial.items():
                    for dec,cost in decoration_options(c,floor,budget-used):
                        rows=tuple((mask,g) for g in dec)
                        nxt.setdefault(used+cost,[]).extend(old+rows for old in lists)
                partial=nxt
            for rows in partial.get(budget,[]):
                allocations+=1
                if any(hub_g[i]==0 and sum(m.bit_count()+g for m,g in rows if m&(1<<i))<degrees[i]*(12-degrees[i]) for i in range(3)):
                    continue
                states.add(canon(weights,rows))
    assert vector_count==comb(17,7)==19448
    frozen=json.loads((SOURCE/'frozen/cover/VERIFICATION_RESULT.json').read_text())
    old=next(r for r in frozen['bipartite'] if r['q']==q)
    expected={canon(s['hub_weights'],s['rows']) for s in old['states']}
    assert states==expected,dict(q=q,extra=list(states-expected),missing=list(expected-states))
    subset_checks=0;ins_checks=0
    rebuilt=[]
    for weights,rows in sorted(states):
        adj=[0]*13
        for j,(mask,g) in enumerate(rows,3):
            for i in range(3):
                if mask&(1<<i):
                    adj[i]|=1<<j;adj[j]|=1<<i
        deg=[a.bit_count() for a in adj]
        w=list(weights)+[m.bit_count()+g for m,g in rows]
        decorations=[w[i]-deg[i] for i in range(13)]
        assert min(decorations)>=0
        assert sum(deg)//2+sum(decorations)==q
        edge=[0]*8192;wt=[0]*8192;gs=[0]*8192
        for S in range(1,8192):
            v=(S&-S).bit_length()-1;rest=S^(1<<v)
            edge[S]=edge[rest]+(adj[v]&rest).bit_count()
            wt[S]=wt[rest]+w[v];gs[S]=gs[rest]+decorations[v]
        for S in range(8192):
            T=8191^S
            assert wt[S]-edge[S]+edge[T]+gs[T]==q
            assert S.bit_count()<=10 or edge[S]>0
            subset_checks+=1
        for i in range(13):
            for j in range(i):
                if adj[i]&(1<<j):assert w[i]+w[j]>=12
            if decorations[i]==0:
                assert wt[adj[i]]-2*edge[adj[i]]>=deg[i]*(12-deg[i])
                ins_checks+=1
        rebuilt.append(dict(hub_weights=weights,rows=rows,missing_adjacency=adj,decorations=decorations))
    return dict(status='COMPUTATIONALLY_VERIFIED',q=q,row_vectors=vector_count,
                hall_edge_vectors=filtered,allocations=allocations,canonical_count=len(states),
                subset_checks=subset_checks,regular_INS11_checks=ins_checks,states=rebuilt)

def support_orbits():
    perms=list(permutations(range(4)))
    maps=[[sum(1<<p[i] for i in range(4) if m&(1<<i)) for m in range(16)] for p in perms]
    types=[m for m in range(16) if m.bit_count()>=2]
    answer={}
    for h in (3,4,5):
        representatives=set();raw=0
        for rows in combinations_with_replacement(types,h):
            if sum(m.bit_count()-1 for m in rows)!=5:continue
            d=[sum(bool(m&(1<<i)) for m in rows) for i in range(4)]
            if min(d)<2:continue
            raw+=1
            representatives.add(min(tuple(sorted(mp[m] for m in rows)) for mp in maps))
        answer[h]=dict(raw_count=raw,orbit_count=len(representatives),representatives=sorted(representatives))
    assert [answer[h]['orbit_count'] for h in (3,4,5)]==[2,3,5]
    named={3:[['0123','01','23'],['01','023','123']],
           4:[['01','01','023','23'],['01','012','03','23'],['01','02','03','123']],
           5:[['01','01','02','03','23'],['01','02','02','13','13'],
              ['01','02','03','12','13'],['01','01','02','13','23'],['01','01','01','23','23']]}
    for h,classes in named.items():
        expected=set()
        for labels in classes:
            row=[sum(1<<int(i) for i in s) for s in labels]
            expected.add(min(tuple(sorted(mp[m] for m in row)) for mp in maps))
        assert expected==set(answer[h]['representatives'])
    return dict(status='COMPUTATIONALLY_VERIFIED',by_h=answer,
                scope='47-point support orbits (low285/E286); h12 uses a different q20 shell classification')

def scalar_checks():
    formulas={
      'f11':(10,10,lambda a,b:max(0,10-a-b)+a*max(0,b-2)+b*max(0,a-2)),
      'f10_11':(9,10,lambda a,b:max(0,9-a-b)+a*max(0,b-3)+b*max(0,a-2)),
      'f9_11':(8,10,lambda a,b:max(0,8-a-b)+a*max(0,b-4)+b*max(0,a-2)),
      'f10_10':(9,9,lambda a,b:max(0,8-a-b)+a*max(0,b-3)+b*max(0,a-3)),
      'star10':(9,10,lambda a,b:max(0,9-a-b)+a*(b-1)+b*max(0,a-2)),
      'star9':(8,10,lambda a,b:max(0,8-a-b)+a*(b-1)+b*max(0,a-2)),
      'diamond':(9,10,lambda a,b:max(0,9-a-b)+a*max(0,b-2)+b*max(0,a-2))}
    answer={}
    for key,(aa,bb,f) in formulas.items():
        values=[(f(a,b),a,b) for a in range(1,aa+1) for b in range(1,bb+1)]
        minimum=min(v[0] for v in values)
        answer[key]=dict(minimum=minimum,minimizers=[v[1:] for v in values if v[0]==minimum])
    assert [answer[k]['minimum'] for k in formulas]==[6,4,2,2,6,5,5]
    assert answer['f11']['minimizers']==[(2,2)]
    for a,b in product(range(12),repeat=2):
        assert max(0,a+b-2)>=max(0,a-2)+max(0,b-2)
    for values in product(range(12),repeat=3):
        if values.count(0)<=1:
            assert max(0,sum(v-1 for v in values))>=sum(max(0,v-2) for v in values)
    odd={n:[2*k+1+k*(n-2*k-1)+(n-2*k-1)**2//4 for k in range(2,(n-1)//2+1)] for n in (18,23,25)}
    assert {n:max(v) for n,v in odd.items()}=={18:73,23:122,25:145}
    assert max(odd[23][1:])==119
    assert 22*8>5*35
    return dict(status='COMPUTATIONALLY_VERIFIED',scalar_minima=answer,odd_cycle_bounds=odd,
                caps={n:cap(n) for n in (13,14,23,24,36,37,38,49)},AES_margin_numerator=22*8-5*35)

def exchange_checks():
    rng=random.Random(SEED);tests=0
    for d in range(13):
        for trial in range(12):
            N=[set() for _ in range(61)]
            def add(x,y):N[x].add(y);N[y].add(x)
            A=set(range(1,14));C=set(range(14,61))
            S=set(rng.sample(range(2,14),d));D=set(rng.sample(range(14,61),d))
            for x in A:add(0,x)
            for x in A-{1}-S:add(1,x)
            for x in D:add(1,x)
            for x,y in combinations(range(2,61),2):
                if rng.random()<0.3:add(x,y)
            def e(U):return sum(len(N[x]&U) for x in U)//2
            def missing(U):return pairs(len(U))-e(U)
            def q(v):return missing(N[v])+sum(len(N[x])-13 for x in N[v])
            newC=set(range(61))-N[1]-{1}
            assert newC==(C-D)|S
            rho=missing(A-S)+sum(len(N[x])-13 for x in A-S)
            m=missing(S);kappa=missing(D);b=sum(len(N[x]&D) for x in S)
            for beta in (11,12):
                h=sum(len(N[x]&C)-beta for x in D)
                eta=sum(len(N[x]&newC)-beta for x in S)
                assert q(1)==d*(beta+1-d)+rho+h+kappa+b
                assert q(1)-q(0)==h-eta+kappa-m
                assert eta==q(0)-d*(beta+1-d)-rho-m-b
                tests+=1
    return dict(status='COMPUTATIONALLY_VERIFIED',tests=tests,seed=SEED,
                scope='Algebra on arbitrary two-regular-pivot graphs, not legal T61 graph witnesses')

def q20_replay():
    result=set();vectors=0
    for rowtypes in combinations_with_replacement(range(4),10):
        vectors+=1
        z=sum(m.bit_count() for m in rowtypes)
        if not 11<=z<=20:continue
        degrees=[sum(bool(m&(1<<i)) for m in rowtypes) for i in range(2)]
        G=20-z
        for g0 in range(G+1):
            for g1 in range(G-g0+1):
                weights=(degrees[0]+g0,degrees[1]+g1)
                budget=G-g0-g1
                groups=[]
                for m in range(4):
                    number=rowtypes.count(m)
                    if not number:continue
                    f=max([0]+[12-m.bit_count()-weights[i] for i in range(2) if m&(1<<i)])
                    groups.append((m,number,f))
                if sum(n*f for m,n,f in groups)>budget:continue
                partial={0:[()]}
                for m,n,f in groups:
                    nxt={}
                    for used,lists in partial.items():
                        for dec,cost in decoration_options(n,f,budget-used):
                            nxt.setdefault(used+cost,[]).extend(old+tuple((m,g) for g in dec) for old in lists)
                    partial=nxt
                for rows in partial.get(budget,[]):
                    forms=[]
                    for swap in (False,True):
                        convert=lambda m:((m&1)<<1)|((m&2)>>1) if swap else m
                        forms.append((weights[::-1] if swap else weights,tuple(sorted((convert(m),g) for m,g in rows))))
                    result.add(min(forms))
    expected={((10,10),tuple(sorted([(3,0)]*r+[(0,0)]*(10-r)))) for r in range(6,11)}
    assert result==expected,(result-expected,expected-result)
    return dict(status='COMPUTATIONALLY_VERIFIED',vectors=vectors,states=sorted(result),
                count=len(result),scope='All two-hub ten-low q20 states; reduction to this channel is analytic')

def lower_order_replay():
    # Enumerate maximal independent sets by include/exclude recursion directly
    # on W, not via the original Bron--Kerbosch complement implementation.
    def maximal_sets(N):
        out=[];universe=(1<<len(N))-1
        def visit(chosen,available):
            if not available:
                covered=chosen
                for v in range(len(N)):
                    if chosen&(1<<v):covered|=N[v]
                if covered==universe:out.append(chosen)
                return
            b=available&-available;v=b.bit_length()-1
            visit(chosen|b,available&~(b|N[v]))
            visit(chosen,available^b)
        visit(0,universe)
        return out
    def graph(sizes,deleted=None):
        groups=[];offset=0
        for size in sizes:
            groups.append(set(range(offset,offset+size)));offset+=size
        N=[0]*offset
        for i in range(5):
            for u,v in product(groups[i],groups[(i+1)%5]):
                if deleted==i and u==min(groups[i]) and v==min(groups[(i+1)%5]):continue
                N[u]|=1<<v;N[v]|=1<<u
        return groups,N
    cases=[]
    for a in range(1,11):
        for deletion in (None,0,1,2,3,4):
            cases.append(([10,a,1,1,11-a],deletion,[(0,2,3),(1,4,2),(1,4,3)]))
    cases.append(([9,9,2,1,2],None,[(0,2,3),(1,3,4)]))
    valid=0;discarded=0;independent=0;worst=0
    for sizes,deletion,choices in cases:
        groups,N=graph(sizes,deletion)
        sets=maximal_sets(N)
        if max(s.bit_count() for s in sets)>11:
            discarded+=1;continue
        valid+=1
        candidates=[sum(1<<v for i in ids for v in groups[i]) for ids in choices]
        assert all(s.bit_count()==12 for s in candidates)
        internal={s:sum((N[v]&s).bit_count() for v in range(23) if s&(1<<v))//2 for s in candidates}
        for I in sets:
            cost=min(internal[s]+(s&I).bit_count() for s in candidates)
            assert cost<=6,(sizes,deletion,I,cost)
            worst=max(worst,cost);independent+=1
    types=[{(i-1)%5,(i+1)%5} for i in range(5)]
    nonempty=[{i for i in range(5) if m&(1<<i)} for m in range(1,32)]
    allowed=[];exceptions=[];extensions=0
    for A,B in product(nonempty,repeat=2):
        if any(types[a]&types[b] for a in A for b in B):continue
        allowed.append((sorted(A),sorted(B)))
        assert min(len(A),len(B))==1 and max(len(A),len(B))<=2
        for v in set(range(5))-set.union(*(types[b] for b in B)):
            assert any(v in types[a] and all(not(types[a]&types[b]) for b in B) for a in range(5))
            extensions+=1
        for u,v in product(range(5),repeat=2):
            if any(types[u]&types[b] for b in B) or any(types[a]&types[v] for a in A):continue
            if not(types[u]&types[v]):continue
            assert len(A)==len(B)==1
            sizes=[1]*5;sizes[next(iter(A))]+=8;sizes[next(iter(B))]+=8;sizes[u]+=1;sizes[v]+=1
            assert any(tuple(sizes[(s+t*i)%5] for i in range(5))==(9,9,2,1,2) for s in range(5) for t in (-1,1))
            exceptions.append([sorted(A),sorted(B),u,v])
    assert len(allowed)==20 and len(exceptions)==10
    return dict(status='COMPUTATIONALLY_VERIFIED',families=len(cases),valid=valid,
                discarded_alpha12=discarded,maximal_independent_sets=independent,maximum_cost=worst,
                compatible_type_pairs=allowed,exceptional_endpoint_cases=exceptions,singleton_extensions=extensions)

def dag_check():
    def check(path):
        dag=json.loads(path.read_text())
        done=set();active=set();order=[]
        def visit(v):
            assert v in dag
            assert v not in active,('cycle',v)
            if v in done:return
            active.add(v)
            for w in dag[v]:visit(w)
            active.remove(v);done.add(v);order.append(v)
        for v in dag:visit(v)
        return dict(nodes=len(dag),topological_order=order)
    results={'source':check(SOURCE/'PROOF_DAG.json')}
    if (HERE/'CANONICAL_PROOF_DAG.json').exists():
        results['independent']=check(HERE/'CANONICAL_PROOF_DAG.json')
    return dict(status='COMPUTATIONALLY_VERIFIED',graphs=results,
                scope='Syntactic DAG only; mathematical hypothesis transport audited separately')

if __name__=='__main__':
    start=time.time()
    result=dict(mathematical_certification='See FINAL_CERTIFICATION_REPORT.md; this program does not decide analytic validity.',python=platform.python_version(),seed=SEED,
                command='python -B INDEPENDENT_REPLAY.py',actual_argv=sys.argv,
                source_sha256=digest(Path(__file__).read_bytes()),pinned_source=PIN,
                note='Computation status does not certify analytic obligations.')
    tasks=[('integrity',integrity),('recurrence',recurrence),('q27',lambda:shell_replay(27)),
           ('q28',lambda:shell_replay(28)),('support_orbits',support_orbits),
           ('scalars',scalar_checks),('exchange',exchange_checks),('q20',q20_replay),
           ('lower_order',lower_order_replay),('dag',dag_check)]
    for name,task in tasks:
        before=time.time()
        print('RUN',name,flush=True)
        try:
            result[name]=task()
            print('PASS',name,round(time.time()-before,3),flush=True)
        except Exception as exc:
            result[name]=dict(status='OPEN',execution_error=repr(exc))
            print('FAIL',name,repr(exc),flush=True)
        result['elapsed_seconds']=round(time.time()-start,3)
        (HERE/'INDEPENDENT_REPLAY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    failures=[name for name,task in tasks if result[name]['status']!='COMPUTATIONALLY_VERIFIED']
    result['replay_status']='OPEN' if failures else 'COMPUTATIONALLY_VERIFIED'
    result['execution_failures']=failures
    (HERE/'INDEPENDENT_REPLAY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('RESULT_SHA256',digest((HERE/'INDEPENDENT_REPLAY_RESULTS.json').read_bytes()),flush=True)
    sys.exit(bool(failures))
