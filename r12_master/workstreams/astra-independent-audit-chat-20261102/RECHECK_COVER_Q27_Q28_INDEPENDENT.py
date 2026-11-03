#!/usr/bin/env python3
"""Independent direct re-enumeration of COVER q=27/q=28 bipartite shells."""
from itertools import permutations
import json

def comps(n,k):
    if k==1:
        yield (n,); return
    for x in range(n+1):
        for tail in comps(n-x,k-1):
            yield (x,)+tail

def parts(n,k,lo=0):
    if k==0:
        if n==0: yield ()
        return
    for x in range(lo,n//k+1):
        for tail in parts(n-x,k-1,x):
            yield (x,)+tail

def canon(hubs,rows):
    out=[]
    for p in permutations(range(3)):
        h=tuple(hubs[i] for i in p)
        rr=[]
        for m,g in rows:
            mm=sum(1<<j for j,i in enumerate(p) if m>>i&1)
            rr.append((mm,g))
        out.append((h,tuple(sorted(rr))))
    return min(out)

def hall(counts):
    return all(sum(counts[m] for m in range(8) if m&S)>=S.bit_count()
               for S in range(1,8))

def expected(q):
    E=set()
    if q==27:
        for k in (8,9):
            E.add(canon((9,9,9),[(7,0)]*k+[(0,0)]*(10-k)))
    else:
        for k in (8,9):
            E.add(canon((9,9,10),[(7,0)]*k+[(0,0)]*(10-k)))
        for k in (7,8):
            E.add(canon((9,9,9),[(7,0)]*k+[(3,1)]+[(0,0)]*(9-k)))
        for k in (8,9):
            E.add(canon((9,9,9),[(7,0)]*(k-1)+[(7,1)]+[(0,0)]*(10-k)))
            E.add(canon((9,9,9),[(7,0)]*k+[(0,1)]+[(0,0)]*(9-k)))
    return E

def direct(q,state):
    hubs,rows=state
    adj=[set() for _ in range(13)]
    for j,(m,g) in enumerate(rows,3):
        for i in range(3):
            if m>>i&1: adj[i].add(j); adj[j].add(i)
    w=list(hubs)+[m.bit_count()+g for m,g in rows]
    g=[w[i]-len(adj[i]) for i in range(13)]
    assert min(g)>=0
    z=sum(map(len,adj))//2
    assert z>=22 and z+sum(g)==q
    assert all(w[i]+w[j]>=12 for i in range(13) for j in adj[i])
    assert hall([sum(1 for m,_ in rows if m==mask) for mask in range(8)])
    for mask in range(1<<13):
        S=[i for i in range(13) if mask>>i&1]
        eS=sum(j in adj[i] for r,i in enumerate(S) for j in S[r+1:])
        if len(S)>=11: assert eS>0
        R=[i for i in range(13) if not mask>>i&1]
        eR=sum(j in adj[i] for r,i in enumerate(R) for j in R[r+1:])
        assert sum(w[i] for i in S)-eS+eR+sum(g[i] for i in R)==q
    for i in range(13):
        if g[i]==0:
            N=sorted(adj[i])
            eN=sum(b in adj[a] for r,a in enumerate(N) for b in N[r+1:])
            assert sum(w[j] for j in N)-2*eN>=len(N)*(12-len(N))

def enumerate_q(q):
    states=set(); rows_seen=0; filtered=0; hub_trials=0; completed=0
    for cnt in comps(10,8):
        rows_seen+=1
        z=sum(cnt[m]*m.bit_count() for m in range(8))
        if z<22 or z>q or not hall(cnt): continue
        filtered+=1
        deg=[sum(cnt[m] for m in range(8) if m>>i&1) for i in range(3)]
        G=q-z
        types=[(m,cnt[m]) for m in range(8) if cnt[m]]
        for H in range(G+1):
            for gh in comps(H,3):
                hub_trials+=1
                wh=[deg[i]+gh[i] for i in range(3)]
                low=G-H
                def rec(pos,rem,rows):
                    nonlocal completed
                    if pos==len(types):
                        if rem: return
                        completed+=1
                        for i in range(3):
                            if gh[i]==0:
                                rw=sum(m.bit_count()+g for m,g in rows if m>>i&1)
                                if rw<deg[i]*(12-deg[i]): return
                        states.add(canon(wh,rows)); return
                    m,c=types[pos]; d=m.bit_count()
                    floor=max([0]+[12-d-wh[i] for i in range(3) if m>>i&1])
                    if sum(wh[i] for i in range(3) if m>>i&1)<d*(12-d):
                        floor=max(floor,1)
                    reserve=0
                    for m2,c2 in types[pos+1:]:
                        d2=m2.bit_count()
                        f2=max([0]+[12-d2-wh[i] for i in range(3) if m2>>i&1])
                        if sum(wh[i] for i in range(3) if m2>>i&1)<d2*(12-d2):
                            f2=max(f2,1)
                        reserve+=c2*f2
                    for budget in range(c*floor,rem-reserve+1):
                        for gs in parts(budget,c,floor):
                            rec(pos+1,rem-budget,rows+[(m,g) for g in gs])
                rec(0,low,[])
    assert rows_seen==19448
    assert states==expected(q),(q,states^expected(q))
    for s in states: direct(q,s)
    return {"q":q,"states":len(states),"row_vectors":rows_seen,
            "edge_hall_vectors":filtered,"hub_trials":hub_trials,
            "completed_low_decorations":completed}

if __name__=="__main__":
    result={"results":[enumerate_q(27),enumerate_q(28)],
            "conclusion":"2 q27 states and 8 q28 states; all direct checks passed"}
    print(json.dumps(result,indent=2))
