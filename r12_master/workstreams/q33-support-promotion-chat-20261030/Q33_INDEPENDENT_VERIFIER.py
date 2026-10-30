#!/usr/bin/env python3
"""Q33 component-only profile verifier plus KP common-gadget degree check."""
from itertools import product
from math import comb

SUPPORT_MIN={8:31,9:32,10:34}
SPLITS=[(c,k) for c in range(5) for k in range(c+1)]
EXCLUDED={8:list(range(31,39)),9:list(range(32,40)),10:list(range(34,41))}
SURVIVORS={8:list(range(39,48)),9:list(range(40,48)),10:list(range(41,48))}

def p(n,k):
    if n<=k:return 0
    q,r=divmod(n,k)
    return (k-r)*comb(q,2)+r*comb(q+1,2)

def t(n,k): return comb(n,2)-p(n,k)

def lu(v):
    w=47-v
    if w==0:return comb(47,2)-284
    return comb(v,2)-280+12*w-p(w,4)

def opts_product(v):
    out=set()
    for z in product(SPLITS,repeat=3):
        cs=sum(c for c,k in z); ks=sum(k for c,k in z)
        if not 10<=cs<=12:continue
        g=19-cs; gu=v-28-ks
        if not 0<=gu<=g:continue
        gw=g-gu
        out.add((sum(comb(k,2) for c,k in z)+p(gu,2),
                 sum(comb(c-k,2) for c,k in z)+p(gw,2)))
    return out

def opts_recursive(v):
    states={(0,0,0,0)}
    for _ in range(3):
        nxt=set()
        for cs,ks,uc,wc in states:
            for c,k in SPLITS:nxt.add((cs+c,ks+k,uc+comb(k,2),wc+comb(c-k,2)))
        states=nxt
    out=set()
    for cs,ks,uc,wc in states:
        if not 10<=cs<=12:continue
        g=19-cs;gu=v-28-ks
        if 0<=gu<=g:
            gw=g-gu;out.add((uc+p(gu,2),wc+p(gw,2)))
    return out

def min_w(v):
    best=None; rows=[]
    for z in product(SPLITS,repeat=3):
        cs=sum(c for c,k in z);ks=sum(k for c,k in z)
        if not 10<=cs<=12:continue
        g=19-cs;gu=v-28-ks
        if not 0<=gu<=g:continue
        gw=g-gu;cost=sum(comb(c-k,2) for c,k in z)+p(gw,2)
        if best is None or cost<best:best=cost;rows=[]
        if cost==best:rows.append((tuple(c-k for c,k in z),gw))
    return best,rows

def global_states(m,v,options):
    n=11-m;w=47-v
    bu=lu(v)-42*m-n*p(v,12)
    bw=t(w,4)-n*p(w,12)
    if bu<0 or bw<0:return bu,bw,set()
    states={(0,0)}
    for _ in range(m):
        states={(u+a,z+b) for u,z in states for a,b in options if u+a<=bu and z+b<=bw}
        if not states:break
    return bu,bw,states

def nonexact_delta(q):
    return min(d for d in range(61) if d+p(60-d,11)<=q)

def verify_common_core_degree():
    for a in range(1,5):
        deg=[5]*9+[4+a,9-a]
        assert min(deg)==5 and sum(deg)==58
    floors={q:nonexact_delta(q) for q in (130,131,132)}
    assert floors=={130:2,131:1,132:1}
    counts={8:[130,130,130],9:[130,131],10:[132]}
    lower={m:5*m+sum(nonexact_delta(q) for q in qs) for m,qs in counts.items()}
    assert lower=={8:46,9:48,10:51}
    assert lower[9]>47 and lower[10]>47
    return floors,lower

def main():
    ov={}
    for v in range(31,48):
        a=opts_product(v);b=opts_recursive(v)
        assert a==b,(v,a^b);ov[v]=a
    for m,vmin in SUPPORT_MIN.items():
        rows=[]
        for v in range(vmin,48):
            bu,bw,st=global_states(m,v,ov[v])
            rows.append((v,bu,bw,len(ov[v]),len(st),bool(st)))
        ex=[v for v,_,_,_,_,ok in rows if not ok]
        su=[v for v,_,_,_,_,ok in rows if ok]
        assert ex==EXCLUDED[m] and su==SURVIVORS[m],(m,ex,su)
    for m,v,mw,bw0 in [(8,39,3,24),(9,40,2,18),(10,41,1,13)]:
        z,sh=min_w(v);assert z==mw
        assert all(max(parts)<=2 for parts,gw in sh)
        assert max(gw for parts,gw in sh)<=(4 if m<10 else 3)
        bu,bw,st=global_states(m,v,ov[v]);assert bw==bw0
        if m<10:assert m*z==bw and {w for u,w in st}=={bw}
        else:assert m*z==10 and bw-m*z==3 and {w for u,w in st}=={10,11,12,13}
    floors,lower=verify_common_core_degree()
    print("Q33 KP-REFINED COMPONENT-ONLY SCREEN: PASS")
    print("Nonexact minimum-degree floors:",floors)
    print("Common gadget-core lower degree:",lower)
    print("W_* empty for m=9,10; m=8 retains at most two saturated points.")
    print("Q33 remains OPEN / NOT_CERTIFIED.")

if __name__=="__main__":main()
