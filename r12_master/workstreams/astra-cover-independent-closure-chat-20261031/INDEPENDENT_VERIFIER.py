"""Independent exact COVER verifier, version 1.0.

Reconstructs every bipartite shell from eight row multiplicities, then hub
decorations, then sorted decorations within each row type. It neither imports
the exploratory generator nor reads its output. Analytic reductions remain
explicit in COVER_THEOREM.md; this is not a proof-assistant kernel.
"""
import hashlib
import itertools as it
import json
import platform
import random
import sys
from pathlib import Path


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for tail in compositions(total-first,length-1):
                yield (first,)+tail


def partitions(total, length, minimum=0):
    if not length:
        if total == 0: yield ()
        return
    for first in range(minimum,total//length+1):
        for tail in partitions(total-first,length-1,first):
            yield (first,)+tail


def canonical(weights, rows):
    return min((tuple(weights[i] for i in p),
                tuple(sorted((sum(1<<j for j,i in enumerate(p) if m>>i&1),g)
                             for m,g in rows)))
               for p in it.permutations(range(3)))


def expected_states(q):
    result=set()
    if q==27:
        for k in (8,9):
            result.add(canonical((9,9,9),[(7,0)]*k+[(0,0)]*(10-k)))
    else:
        for k in (8,9):
            result.add(canonical((9,9,10),[(7,0)]*k+[(0,0)]*(10-k)))
        # The remaining six have all hub weights9 and one decorated low.
        for k in (7,8):
            result.add(canonical((9,9,9),[(7,0)]*k+[(3,1)]+[(0,0)]*(9-k)))
        for k in (8,9):
            result.add(canonical((9,9,9),[(7,0)]*(k-1)+[(7,1)]+[(0,0)]*(10-k)))
            result.add(canonical((9,9,9),[(7,0)]*k+[(0,1)]+[(0,0)]*(9-k)))
    return result


def reconstruct_bipartite(q):
    states=set()
    counters={"all_row_count_vectors":0,"edge_and_Hall_vectors":0,
              "hub_decoration_trials":0,"completed_decorations":0}
    for counts in compositions(10,8):
        counters['all_row_count_vectors']+=1
        z=sum(c*m.bit_count() for m,c in enumerate(counts))
        if not 22<=z<=q: continue
        # Hall on the three hubs is equivalent to alpha(M)<=10.
        if any(sum(c for m,c in enumerate(counts) if m&s)<s.bit_count()
               for s in range(1,8)): continue
        counters['edge_and_Hall_vectors']+=1
        degrees=[sum(c for m,c in enumerate(counts) if m>>i&1) for i in range(3)]
        G=q-z
        for hub_total in range(G+1):
            for gs in compositions(hub_total,3):
                counters['hub_decoration_trials']+=1
                weights=tuple(degrees[i]+gs[i] for i in range(3))
                low_total=G-hub_total
                groups=[]
                lower_cost=0
                for m,c in enumerate(counts):
                    if not c: continue
                    d=m.bit_count()
                    floor=max([0]+[12-d-weights[i] for i in range(3) if m>>i&1])
                    if sum(weights[i] for i in range(3) if m>>i&1)<d*(12-d):
                        floor=max(floor,1)  # an undecorated row would violate inserted-core degrees
                    groups.append((m,c,floor))
                    lower_cost+=c*floor
                if lower_cost>low_total: continue
                def allocate(index,remaining,rows):
                    if index==len(groups):
                        if remaining: return
                        counters['completed_decorations']+=1
                        for i in range(3):
                            if gs[i]==0:
                                row_weight=sum(m.bit_count()+g for m,g in rows if m>>i&1)
                                if row_weight<degrees[i]*(12-degrees[i]): return
                        states.add(canonical(weights,rows))
                        return
                    m,c,floor=groups[index]
                    reserve=sum(cc*ff for mm,cc,ff in groups[index+1:])
                    for budget in range(c*floor,remaining-reserve+1):
                        for part in partitions(budget,c,floor):
                            allocate(index+1,remaining-budget,rows+[(m,g) for g in part])
                allocate(0,low_total,[])
    assert counters['all_row_count_vectors']==19448
    assert states==expected_states(q), ('omitted or extra state',q,states^expected_states(q))
    return {"q":q,"canonical_states":len(states),"counters":counters,
            "states":[{"hub_weights":x,"rows":rows} for x,rows in sorted(states)]}


def check_every_state_directly(record):
    for state in record['states']:
        xs=state['hub_weights']; rows=state['rows']
        adj=[set() for _ in range(13)]
        for j,(m,g) in enumerate(rows,3):
            for i in range(3):
                if m>>i&1: adj[i].add(j); adj[j].add(i)
        weights=list(xs)+[m.bit_count()+g for m,g in rows]
        dec=[weights[i]-len(adj[i]) for i in range(13)]
        assert min(dec)>=0
        z=sum(map(len,adj))//2
        assert z>=22 and z+sum(dec)==record['q']
        assert all(weights[i]+weights[j]>=12 for i in range(13) for j in adj[i])
        for mask in range(1<<13):
            vertices=[i for i in range(13) if mask>>i&1]
            e=sum(j in adj[i] for i,j in it.combinations(vertices,2))
            if len(vertices)>=11: assert e>0
            # Exact subset identity on every subset, not only the cover.
            rest=[i for i in range(13) if not(mask>>i&1)]
            er=sum(j in adj[i] for i,j in it.combinations(rest,2))
            assert sum(weights[i] for i in vertices)-e+er+sum(dec[i] for i in rest)==record['q']
        for i in range(13):
            if dec[i]==0:
                d=len(adj[i]); internal=sum(b in adj[a] for a,b in it.combinations(adj[i],2))
                assert sum(weights[j] for j in adj[i])-2*internal>=d*(12-d)


def arithmetic():
    def pk(n,k):
        a,b=divmod(n,k)
        return k*a*(a-1)//2+a*b
    def cap(n): return n*(n-1)//2-11*pk(n,12)
    assert {n:cap(n) for n in (13,14,23,24,36,37)}=={13:67,14:69,23:132,24:144,36:234,37:237}
    assert 22*8>5*35 # strict AES hypothesis, not rounded
    assert 66+211+11==288
    assert 131-211+144+12==76>cap(14)
    assert 288-144+66==210<211
    assert 407-91-287==29 and 408-91-287==30
    # All partitions of the regular K11 into twin classes of size2 or3.
    twin=[(a,b) for a in range(6) for b in range(4) if 2*a+3*b==11]
    assert twin==[(1,3),(4,1)]
    assert min(a+b for a,b in twin)>=4
    family_i=[]
    for E in (407,408):
        excess=2*E-13*61
        for r in range(1,6):
            if 3*r<11 or 3*(11-r)>excess: continue
            n=50-3*r; rem=excess-3*(11-r)
            if r==5: assert 2*n>rem
            elif r==4: assert n-rem>11
            else: raise AssertionError(('uncovered Family I multiplicity',E,r))
            family_i.append((E,r,n,rem))
    # Triangle outside-edge stars in the q<=28 audit.
    stars=[]
    for k in range(1,8):
        if k==1: assert 3+1+4+8<22
        else:
            assert (12+9+9)-2*2==26<3*(12-3)
        stars.append(k)
    return {"caps":"PASS","AES_strict_boundary":"PASS","twin_partitions":twin,
            "q30_family_I_cases":family_i,"triangle_star_sizes":stars}


def repivot_identity_checks():
    # Algebra-only test graphs: not claimed to satisfy the T61 graph contract.
    rng=random.Random(617)
    checked=0
    for d in range(13):
        for repeat in range(4):
            adj=[set() for _ in range(61)]
            def add(a,b): adj[a].add(b); adj[b].add(a)
            A=set(range(1,14)); C=set(range(14,61))
            S=set(rng.sample(list(range(2,14)),d)); row=set(rng.sample(sorted(C),d))
            for a in A: add(0,a)
            for a in (A-{1})-S: add(1,a)
            for a in row: add(1,a)
            for a,b in it.combinations(range(2,61),2):
                if rng.randrange(5)==0: add(a,b)
            edges=lambda U:sum(b in adj[a] for a,b in it.combinations(U,2))
            missing=lambda U:len(U)*(len(U)-1)//2-edges(U)
            charge=lambda v:missing(adj[v])+sum(len(adj[a])-13 for a in adj[v])
            assert len(adj[0])==len(adj[1])==13
            rho=missing(A-S)+sum(len(adj[a])-13 for a in A-S)
            m=missing(S); kap=missing(row)
            b=sum(len(adj[a]&row) for a in S)
            newC=(C-row)|S
            assert newC==set(range(61))-(adj[1]|{1})
            for beta in (11,12):
                h=sum(len(adj[x]&C)-beta for x in row)
                eta=sum(len(adj[x]&newC)-beta for x in S)
                assert charge(1)==d*(beta+1-d)+rho+h+kap+b
                assert eta==charge(0)-d*(beta+1-d)-rho-m-b
                assert charge(1)-charge(0)==h-eta+kap-m
                checked+=1
    return {"algebraic_instances":checked,"all_exchange_distances":list(range(13)),
            "scope":"arbitrary regular-pivot algebra, not T61 witnesses"}


if __name__=='__main__':
    records=[reconstruct_bipartite(q) for q in (27,28)]
    for record in records: check_every_state_directly(record)
    result={"status":"PASS","verifier_version":"1.0","python":platform.python_version(),
            "command":"python -B INDEPENDENT_VERIFIER.py",
            "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "scope":"independent complete finite bipartite classification and arithmetic; analytic lemmas remain in theorem",
            "bipartite":records,"direct_subset_checks":sum(r['canonical_states'] for r in records)*(1<<13),
            "arithmetic":arithmetic(),"repivot_identity":repivot_identity_checks()}
    Path(__file__).with_name('VERIFICATION_RESULT.json').write_bytes((json.dumps(result,indent=2)+'\n').encode())
    print(json.dumps({k:v for k,v in result.items() if k!='bipartite'},indent=2))
    print('canonical shell counts:',[r['canonical_states'] for r in records])
