#!/usr/bin/env python3
"""Independent E407-Q32 V12 replay, version 2.

This implementation is standalone: it does not import the V12 generator,
its verifier, or its screen script. It uses bit-mask graphs, bounded-composition
weight enumeration, memoized multiplicity DP, and a fresh shell/screen checker.
"""
from __future__ import annotations
import itertools as it
import json, hashlib, collections, functools, math, pathlib, sys, argparse, zipfile, shutil

ROOT = None
CERT = None
SCREEN = None
ARCHIVE_PATH = None
OUT_DIR = None
FLOOR = {2:13, 3:25, 4:36, 5:47}
REGULAR_DEGREES = {0,1,2,3,10,11,12}
Q = 32

# Kernel graphs are encoded as (name, vertex_count, edge_set, K4_free, max_decoration).
TRIANGLE = {(0,1),(0,2),(1,2)}
KERNELS = [
    ('I3',3,set(),True,10),
    ('T3',3,set(TRIANGLE),True,10),
    ('K4',4,set(it.combinations(range(4),2)),False,2),
    ('W8',5,set(TRIANGLE)|{(3,4),(0,3),(1,3),(0,4),(2,4)},True,2),
    ('W7_overlap',5,set(TRIANGLE)|{(3,4),(0,3),(1,3),(0,4)},True,1),
    ('W7_separate',5,set(TRIANGLE)|{(3,4),(0,3),(1,3),(2,4)},True,1),
    ('W6_pair',5,set(TRIANGLE)|{(3,4),(0,3),(1,3)},True,0),
    ('W6_same',5,set(TRIANGLE)|{(3,4),(0,3),(0,4)},True,0),
    ('W6_different',5,set(TRIANGLE)|{(3,4),(0,3),(1,4)},True,0),
]

def mask_from_set(s):
    z=0
    for i in s: z |= 1<<i
    return z

def pairs_from_mask(mask):
    return [i for i in range(mask.bit_length()) if (mask>>i)&1]

def edge_count_inside(mask, adj):
    v=pairs_from_mask(mask)
    return sum(1 for i,j in it.combinations(v,2) if (adj[i]>>j)&1)

def make_adj(k, edges):
    a=[0]*k
    for i,j in edges:
        a[i]|=1<<j; a[j]|=1<<i
    return a

def clique_masks(adj, min_size=2, max_size=5):
    n=len(adj)
    out=[]
    for mask in range(1,1<<n):
        s=mask.bit_count()
        if s<min_size or s>max_size: continue
        vs=pairs_from_mask(mask)
        if all((adj[i]>>j)&1 for i,j in it.combinations(vs,2)):
            out.append(mask)
    return out

def weighted_ok(adj, weights):
    n=len(adj)
    for size in range(2,min(5,n)+1):
        for C in it.combinations(range(n),size):
            if all((adj[i]>>j)&1 for i,j in it.combinations(C,2)):
                if sum(weights[i] for i in C) < FLOOR[size]:
                    return False
    return True

def bounded_weights(base, total):
    """All t with base_i <= t_i <= 22 and sum t=total, in lexicographic order."""
    k=len(base)
    suffix_min=[0]*(k+1)
    for i in range(k-1,-1,-1): suffix_min[i]=suffix_min[i+1]+base[i]
    def rec(i,left,prefix):
        if i==k-1:
            x=left
            if base[i] <= x <= 22:
                yield tuple(prefix+[x])
            return
        lo=base[i]
        hi=min(22,left-suffix_min[i+1])
        for x in range(lo,hi+1):
            yield from rec(i+1,left-x,prefix+[x])
    yield from rec(0,total,[])

def regular_pivot_ok(kernel_adj, weights, Nmask):
    N=pairs_from_mask(Nmask)
    d=len(N)
    m=edge_count_inside(Nmask,kernel_adj)
    rho=Q-sum(weights[i] for i in N)+m
    charge=d*(13-d)+rho
    if rho<0 or charge>Q or (d==3 and rho>1): return False
    beta=12 if charge>=28 else 11
    for v in N:
        local_degree=(kernel_adj[v]&Nmask).bit_count()
        if weights[v]+d-1-local_degree < beta: return False
    return True

def allowed_types(kernel_adj, weights, r, k4_free):
    """All allowed outside-vertex types (N,g), sorted by g then N bitmask."""
    k=len(kernel_adj)
    ans=[]
    for g in range(r+1):
        for Nmask in range(1<<k):
            N=pairs_from_mask(Nmask); d=len(N)
            if g==0 and d not in REGULAR_DEGREES: continue
            # A new K4 appears exactly when N contains a kernel triangle.
            if k4_free and any(all((kernel_adj[u]>>v)&1 for u,v in it.combinations(T,2))
                               for T in it.combinations(N,3)):
                continue
            new_weight=d+g
            # Every clique formed by the new vertex and a nonempty clique in N
            # must satisfy the corresponding missing-clique weight floor.
            bad=False
            for s in range(1,min(4,d)+1):
                for C in it.combinations(N,s):
                    if all((kernel_adj[u]>>v)&1 for u,v in it.combinations(C,2)):
                        if sum(weights[u] for u in C)+new_weight < FLOOR[s+1]:
                            bad=True; break
                if bad: break
            if bad: continue
            if g==0 and not regular_pivot_ok(kernel_adj,weights,Nmask): continue
            ans.append((Nmask,g))
    return ans

def multiplicity_solutions(types, outside_n, r, min_incidence, capacities):
    """Count-vector DP with memoized completion counts, then unrank all solutions."""
    k=len(capacities); nt=len(types)
    suffix_max_deg=[0]*(nt+1); suffix_max_g=[0]*(nt+1)
    for i in range(nt-1,-1,-1):
        suffix_max_deg[i]=max(suffix_max_deg[i+1],types[i][0].bit_count())
        suffix_max_g[i]=max(suffix_max_g[i+1],types[i][1])
    @functools.lru_cache(maxsize=None)
    def ways(i,nleft,rleft,needleft,caps):
        if nleft==0:
            return int(rleft==0 and needleft<=0)
        if i==nt or nleft<0 or rleft<0: return 0
        if needleft>nleft*suffix_max_deg[i] or needleft>sum(caps): return 0
        if rleft>nleft*suffix_max_g[i]: return 0
        Nmask,g=types[i]; deg=Nmask.bit_count()
        upper=nleft
        if g: upper=min(upper,rleft//g)
        for j in range(k):
            if (Nmask>>j)&1: upper=min(upper,caps[j])
        total=0
        for c in range(upper+1):
            ncaps=tuple(caps[j]-c*((Nmask>>j)&1) for j in range(k))
            total+=ways(i+1,nleft-c,rleft-c*g,max(0,needleft-c*deg),ncaps)
        return total
    def unrank(i,nleft,rleft,needleft,caps,prefix):
        if nleft==0:
            if rleft==0 and needleft<=0: yield tuple(prefix+[0]*(nt-i))
            return
        if i==nt: return
        Nmask,g=types[i]; deg=Nmask.bit_count()
        upper=nleft
        if g: upper=min(upper,rleft//g)
        for j in range(k):
            if (Nmask>>j)&1: upper=min(upper,caps[j])
        for c in range(upper+1):
            ncaps=tuple(caps[j]-c*((Nmask>>j)&1) for j in range(k))
            nr=max(0,needleft-c*deg)
            if ways(i+1,nleft-c,rleft-c*g,nr,ncaps):
                yield from unrank(i+1,nleft-c,rleft-c*g,nr,ncaps,prefix+[c])
    initial=tuple(capacities)
    if ways(0,outside_n,r,min_incidence,initial)==0: return ()
    return tuple(unrank(0,outside_n,r,min_incidence,initial,[]))

def graph_from_count_vector(k, kernel_edges, kernel_weights, types, counts):
    n=13-k
    adj=make_adj(13,kernel_edges)
    out_g=[]; used_types=[]
    v=k
    for (Nmask,g),c in zip(types,counts):
        for _ in range(c):
            for u in pairs_from_mask(Nmask):
                adj[u]|=1<<v; adj[v]|=1<<u
            out_g.append(g); used_types.append((Nmask,g)); v+=1
    assert v==13
    degrees=[x.bit_count() for x in adj]
    gvec=[kernel_weights[i]-degrees[i] for i in range(k)]+out_g
    tvec=[degrees[i]+gvec[i] for i in range(13)]
    return adj,degrees,gvec,tvec,used_types

def legal_pivot_full(adj,tvec,y):
    N=adj[y]; d=N.bit_count()
    m=edge_count_inside(N,adj)
    rho=Q-sum(tvec[i] for i in pairs_from_mask(N))+m
    charge=d*(13-d)+rho
    if rho<0 or charge>Q or (d==3 and rho>1): return False
    beta=12 if charge>=28 else 11
    for v in pairs_from_mask(N):
        if tvec[v]+d-1-(adj[v]&N).bit_count() < beta: return False
    return True

def shell_is_necessary(adj,degrees,gvec,tvec):
    z=sum(degrees)//2
    if min(gvec)<0 or z<22 or max(degrees)>z-11: return False
    if z+sum(gvec)!=Q: return False
    if not weighted_ok(adj,tvec): return False
    for y in range(13):
        if gvec[y]==0:
            if degrees[y] not in REGULAR_DEGREES or not legal_pivot_full(adj,tvec,y): return False
    # alpha(M)<=10: every 11-subset contains a missing edge.
    for S in it.combinations(range(13),11):
        if all(not ((adj[u]>>v)&1) for u,v in it.combinations(S,2)):
            return False
    return True

def edge_list(adj):
    return [[i,j] for i in range(13) for j in range(i+1,13) if (adj[i]>>j)&1]

def record_key(s):
    return (s['kernel'],s['r'],tuple(tuple(e) for e in s['edges']),tuple(s['g']),tuple(s['t']))

def enumerate_all():
    expected_rows={(x['kernel'],x['r'],tuple(x['t'])):x for x in CERT['weights']}
    assert len(expected_rows)==len(CERT['weights'])
    seen_rows=set(); observed_survivors=[]; stats=[]; total_states=0
    for name,k,edges,k4free,rmax in KERNELS:
        kadj=make_adj(k,edges); base=[a.bit_count() for a in kadj]
        nweights=nstates=nsurvivors=0
        for r in range(rmax+1):
            total=Q+len(edges)-r
            for t in bounded_weights(base,total):
                if not weighted_ok(kadj,t): continue
                key=(name,r,t)
                assert key in expected_rows, ('missing expected weight row',key)
                row=expected_rows[key]; seen_rows.add(key); nweights+=1
                types=allowed_types(kadj,t,r,k4free)
                encoded_types=[[pairs_from_mask(N),g] for N,g in types]
                assert encoded_types==row['types'], ('type mismatch',key,encoded_types,row['types'])
                solutions=multiplicity_solutions(types,13-k,r,22-len(edges),[t[i]-base[i] for i in range(k)])
                nstates+=len(solutions)
                hit=0
                for counts in solutions:
                    adj,degrees,gvec,tvec,used=graph_from_count_vector(k,edges,t,types,counts)
                    if not shell_is_necessary(adj,degrees,gvec,tvec): continue
                    rec={'edges':edge_list(adj),'g':gvec,'t':tvec,'kernel':name,'r':r,
                         'kernel_weights':list(t),'types':encoded_types,'counts':list(counts)}
                    observed_survivors.append(rec); hit+=1
                assert len(solutions)==row['count_states'], ('count-state mismatch',key,len(solutions),row['count_states'])
                assert hit==row['survivors'], ('survivor mismatch',key,hit,row['survivors'])
            stats.append({'kernel':name,'r':r,'weights':nweights,'count_states':nstates,'survivors':nsurvivors})
        # Recompute kernel aggregate, not the per-r rows.
        expected_stat=next(x for x in CERT['weights'] if x['kernel']==name)
        del expected_stat
        stats.append({'kernel_total':name,'weights':nweights,'count_states':nstates,'survivors':sum(1 for x in observed_survivors if x['kernel']==name)})
        total_states+=nstates
    assert seen_rows==set(expected_rows), (len(seen_rows),len(expected_rows))
    expected_keys=[record_key(s) for s in CERT['survivors']]
    observed_keys=[record_key(s) for s in observed_survivors]
    assert collections.Counter(expected_keys)==collections.Counter(observed_keys), 'survivor multiset mismatch'
    assert len(seen_rows)==8677 and total_states==17957 and len(observed_survivors)==1984
    return observed_survivors,stats,total_states

def shell_low(adj,tvec,gvec,y):
    N=adj[y]; d=N.bit_count(); m=edge_count_inside(N,adj)
    rho=Q-sum(tvec[i] for i in pairs_from_mask(N))+m
    return d*(13-d)+rho, rho

def template_name(adj,tvec,gvec,y):
    S=adj[y]; vs=pairs_from_mask(S)
    if len(vs)!=3 or gvec[y]!=0: return None
    m=edge_count_inside(S,adj)
    w=sorted(tvec[v] for v in vs)
    if m==0 and w==[10,10,12]: return 'A'
    if m==0 and w==[10,11,11]: return 'B'
    if m==1:
        es=[(u,v) for u,v in it.combinations(vs,2) if (adj[u]>>v)&1]
        ends=set(es[0]); third=next(v for v in vs if v not in ends)
        if sorted(tvec[v] for v in ends)==[11,12] and tvec[third]==10: return 'C'
        if sorted(tvec[v] for v in ends)==[11,11] and tvec[third]==11: return 'D'
    if m==2:
        degS={v:(adj[v]&S).bit_count() for v in vs}
        centre=next(v for v in vs if degS[v]==2)
        ends=[v for v in vs if v!=centre]
        if tvec[centre]==12 and all(tvec[v]==11 for v in ends): return 'E'
    return None

def full_template_row_audit(adj,tvec,gvec,y,template):
    S=adj[y]; W=((1<<13)-1)^S
    Wv=pairs_from_mask(W)
    if len(Wv)!=10: return False,{'reason':'wrong W size','size':len(Wv)}
    if any(gvec[w]!=0 for w in Wv): return False,{'reason':'W contains decorated/nonregular vertex'}
    if any((adj[w]&W) & ~(1<<w) for w in Wv): return False,{'reason':'W not M-independent'}
    sv=pairs_from_mask(S)
    if template in ('A','B'):
        if edge_count_inside(S,adj)!=0: return False,{'reason':'S graph mismatch'}
    allowed=set()
    full=S
    if template=='A':
        hub=next(v for v in sv if tvec[v]==12)
        allowed={0,full,1<<hub}
    elif template=='B':
        pair=mask_from_set(v for v in sv if tvec[v]==11)
        allowed={0,full,pair}
    elif template=='C':
        edge=next((u,v) for u,v in it.combinations(sv,2) if (adj[u]>>v)&1)
        hub=next(v for v in edge if tvec[v]==12)
        allowed={0,full,1<<hub}
    elif template=='D':
        edge=next((u,v) for u,v in it.combinations(sv,2) if (adj[u]>>v)&1)
        third=next(v for v in sv if v not in edge)
        allowed={0,full,(1<<third)|(1<<edge[0]),(1<<third)|(1<<edge[1])}
    elif template=='E':
        centre=next(v for v in sv if (adj[v]&S).bit_count()==2)
        ends=[v for v in sv if v!=centre]
        allowed={0,full,1<<centre,mask_from_set(ends)}
    else: return False,{'reason':'unknown template'}
    row_masks=[]
    for w in Wv:
        row=adj[w]&S
        row_masks.append(row)
        if row not in allowed:
            return False,{'reason':'outside row not in template list','vertex':w,'row':pairs_from_mask(row),'allowed':[pairs_from_mask(x) for x in allowed]}
    # Verify the count inequalities recorded in C7.
    counts=collections.Counter(x.bit_count() for x in row_masks)
    if template=='A': ok=counts[0]+counts[1]+counts[3]==10 and 3*counts[0]+2*counts[1]<=8
    elif template=='B': ok=counts[0]+counts[2]+counts[3]==10 and 3*counts[0]+counts[2]<=8
    elif template=='C': ok=counts[0]+counts[1]+counts[3]==10 and 3*counts[0]+2*counts[1]<=9
    elif template=='D':
        # D has two distinct allowed pair types; its row-size 2 count is na+nb.
        ok=counts[0]+counts[2]+counts[3]==10 and 3*counts[0]+counts[2]<=9
    else: ok=counts[0]+counts[1]+counts[2]+counts[3]==10 and 3*counts[0]+2*counts[1]+counts[2]<=10
    if not ok: return False,{'reason':'template count inequality failed','counts':dict(counts)}
    return True,{'W':Wv,'row_counts':dict(counts),'allowed_rows':[pairs_from_mask(x) for x in allowed]}

def classify_screen(s):
    adj=make_adj(13,[tuple(e) for e in s['edges']]); g=s['g']; t=s['t']
    # Rule 1: regular d=3, rho=1.
    for y in range(13):
        if g[y]==0 and adj[y].bit_count()==3:
            low,rho=shell_low(adj,t,g,y)
            if rho==1: return {'rule':'D3_RHO1','vertex':y}
    # Rule 2: witnessed K12-minus-one-edge with enough regular pivots.
    for omit in it.combinations(range(13),2):
        P=((1<<13)-1)^mask_from_set(omit)
        missing=[(u,v) for u,v in it.combinations(pairs_from_mask(P),2) if (adj[u]>>v)&1]
        if len(missing)!=1: continue
        ends=set(missing[0]); K=[y for y in pairs_from_mask(P) if y not in ends and g[y]==0]
        k=1+len(K); L=sum(g[y] for y in pairs_from_mask(P) if y not in K)
        if k>=8 and all(shell_low(adj,t,g,y)[0]>=28 for y in K) and L+2*k-2>21:
            # The proof checker also requires K to be M-independent from all P.
            if any((adj[y]&P) & ~(1<<y) for y in K):
                return {'rule':'SCREEN_INCONSISTENCY','witness':'K not M-independent','K':K}
            return {'rule':'NEAR_K12_CAPACITY','omitted':list(omit),'K':[13]+K,'L':L}
    # Rule 3: K9 pair-row completion witness.
    for hubs in it.combinations(range(13),2):
        H=mask_from_set(hubs); P=((1<<13)-1)^H
        inner=[(u,v) for u,v in it.combinations(pairs_from_mask(P),2) if (adj[u]>>v)&1]
        if len(inner)!=2: continue
        centres=set(inner[0])&set(inner[1])
        if len(centres)!=1: continue
        centre=next(iter(centres)); B=mask_from_set(set(inner[0])|set(inner[1])); W=P^B
        Wv=pairs_from_mask(W); Bv=pairs_from_mask(B)
        if len(Wv)!=8 or any(g[w] for w in Wv): continue
        if not all((adj[h]>>b)&1 for h in hubs for b in Bv): continue
        if any((adj[w]&P) & ~(H|(1<<w)) for w in Wv): continue
        L=sum(g[b] for b in Bv)
        if L<7 or Q>25+L or any(shell_low(adj,t,g,w)[0]<28 for w in Wv): continue
        return {'rule':'K9_PAIR_ROWS','K':[13]+Wv,'B':Bv,'hubs':list(hubs),'L':L,'centre':centre,'hub_edge':int((adj[hubs[0]]>>hubs[1])&1)}
    # Rule 4: residual d3/rho=0 template.
    candidates=[]
    for y in range(13):
        if g[y]==0 and adj[y].bit_count()==3:
            low,rho=shell_low(adj,t,g,y)
            if low==30 and rho==0:
                T=template_name(adj,t,g,y)
                if T: candidates.append((y,T))
    return {'rule':'OPEN','candidates':candidates}

def audit_templates(survivors):
    counts=collections.Counter(); multi=collections.Counter(); failures=[]; per_survivor=[]
    for idx,s in enumerate(survivors):
        if classify_screen(s)['rule']!='OPEN': continue
        adj=make_adj(13,[tuple(e) for e in s['edges']]); g=s['g']; t=s['t']
        candidates=[]
        for y in range(13):
            if g[y]==0 and adj[y].bit_count()==3:
                low,rho=shell_low(adj,t,g,y)
                if low==30 and rho==0:
                    T=template_name(adj,t,g,y)
                    if T is None:
                        candidates.append({'y':y,'template':None,'full_rows_ok':False,'detail':{'reason':'d3/rho0 candidate does not match A-E'}})
                        failures.append({'survivor_index':idx,'y':y,'template':None,'detail':{'reason':'d3/rho0 candidate does not match A-E'}})
                    else:
                        ok,detail=full_template_row_audit(adj,t,g,y,T)
                        candidates.append({'y':y,'template':T,'full_rows_ok':ok,'detail':detail})
                        if ok: counts[T]+=1
                        else: failures.append({'survivor_index':idx,'y':y,'template':T,'detail':detail})
        ts=sorted(set(x['template'] for x in candidates))
        multi[len(ts)]+=1
        per_survivor.append({'survivor_index':idx,'templates':ts,'candidates':candidates})
    return counts,multi,failures,per_survivor

def main():
    global ROOT, CERT, SCREEN, ARCHIVE_PATH, OUT_DIR
    parser=argparse.ArgumentParser(description='Independent E407-Q32 V12 replay (no imports from the source package).')
    parser.add_argument('--archive',type=pathlib.Path,help='Path to T61_H13_V12.zip')
    parser.add_argument('--package-dir',type=pathlib.Path,help='Path to an already extracted T61_H13_V12 directory')
    parser.add_argument('--output-dir',type=pathlib.Path,default=pathlib.Path('.'),help='Directory for replay receipt and survivor map')
    args=parser.parse_args()
    OUT_DIR=args.output_dir.resolve(); OUT_DIR.mkdir(parents=True,exist_ok=True)
    if args.package_dir:
        ROOT=args.package_dir.resolve()
    elif args.archive:
        ARCHIVE_PATH=args.archive.resolve()
        extract_dir=OUT_DIR/'.v12_extract'
        if extract_dir.exists(): shutil.rmtree(extract_dir)
        extract_dir.mkdir(parents=True)
        with zipfile.ZipFile(ARCHIVE_PATH) as zf: zf.extractall(extract_dir)
        ROOT=extract_dir/'T61_H13_V12'
    else:
        parser.error('supply --archive or --package-dir')
    CERT=json.loads((ROOT/'E407_Q32_CERTIFICATE.json').read_text())
    SCREEN=json.loads((ROOT/'E407_Q32_SCREEN.json').read_text())
    survivors,stats,total_states=enumerate_all()
    rule_counts=collections.Counter(); screen_mismatches=[]
    # The original screen file is indexed against certificate survivor order.
    by_key={record_key(s):s for s in CERT['survivors']}
    for idx,s in enumerate(CERT['survivors']):
        got=classify_screen(s)
        rec=SCREEN[idx]
        rule_counts[got['rule']]+=1
        if got['rule']!=rec['rule']:
            screen_mismatches.append({'index':idx,'got':got,'expected':rec})
    template_counts,multiplicity,template_failures,per_survivor=audit_templates(CERT['survivors'])
    result={
      'archive_sha256':hashlib.sha256(ARCHIVE_PATH.read_bytes()).hexdigest() if ARCHIVE_PATH else None,
      'certificate_sha256':hashlib.sha256((ROOT/'E407_Q32_CERTIFICATE.json').read_bytes()).hexdigest(),
      'weights':len(CERT['weights']),'count_states':total_states,'necessary_shells':len(survivors),
      'screen_rule_counts':dict(rule_counts),'screen_mismatches':len(screen_mismatches),
      'full_template_candidate_counts':dict(template_counts),
      'templates_per_open_survivor':dict(multiplicity),
      'template_row_failures':len(template_failures),
      'kernel_totals':[x for x in stats if 'kernel_total' in x],
      'completed_parent_graphs':0,
    }
    out=OUT_DIR/'V12_INDEPENDENT_REPLAY_RESULT.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    (OUT_DIR/'V12_TEMPLATE_MAPPING_FULL.json').write_text(json.dumps(per_survivor,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    if screen_mismatches:
        print('SCREEN MISMATCH SAMPLE',json.dumps(screen_mismatches[:3],indent=2))
    if template_failures:
        print('TEMPLATE FAILURE SAMPLE',json.dumps(template_failures[:5],indent=2))

if __name__=='__main__': main()