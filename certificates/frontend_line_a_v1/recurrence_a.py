"""Contextual recurrence A. Input: no induced R(4,49) in the FIXED G.
No generic R449 emptiness, no R449 edge floor, no P562 seed.
Adapted from archived replay_a.py; all modifications are stated above.
"""
from math import comb
INF=10**9
LIMIT=145
def p(a,n):q,r=divmod(n,a);return a*comb(q,2)+q*r
def D(n):return comb(n,2)-11*p(12,n)
def ceiling(x,y):return (x+y-1)//y
def compute():
    table=[[INF]*(LIMIT+1) for _ in range(13)]
    maxima=[0]+[LIMIT]*12
    details={}
    for a in range(1,13):
        table[a][0]=0
        for n in range(1,LIMIT+1):
            if a==1:
                table[a][n]=comb(n,2) if n<=11 else INF
                continue
            if (a==2 and n>=24) or (a==3 and n>=37) or (a==4 and n>=49) or table[a][n-1]>=INF:
                continue
            generic=p(a,n)
            deletion=ceiling(n*table[a][n-1],n-2) if n>2 else 0
            seed=0
            if (a,n)==(2,23):seed=131
            if (a,n)==(3,36):seed=234
            if (a,n)==(3,35):seed=210
            if (a,n)==(4,47):seed=284
            if (a,n)==(4,48):seed=308
            common=max(generic,deletion,seed)
            rows=[]
            for h in range(n):
                m=n-h-1;core=table[a-1][m]
                if core>=INF:
                    rows.append(dict(h=h,m=m,status='EXCLUDED',reason='core_empty'));continue
                z=max(p(10,h),comb(h+1,2)-D(h+1),comb(h,2)-D(h))
                q=z;pair_cover=0;triangle_cover=None;tf=None;tri=None
                if h>=11:
                    pair_cover=max(0,m-maxima[a-2])
                    q=max(q,pair_cover-1)
                    if core+pair_cover>D(m+2):
                        rows.append(dict(h=h,m=m,status='EXCLUDED',reason='pair_density',core=core,pair_cover=pair_cover));continue
                    matching=max(ceiling(h-10,2),3 if h>=13 else 2 if h>=12 else 1)
                    general=max(q,max(t*pair_cover-comb(2*t,2)+p(a,2*t) for t in range(1,matching+1)))
                    tf=max(general,max(t*pair_cover-t*t for t in range(1,matching+1)))
                    tri=INF
                    if a>=3:
                        triangle_cover=max(0,m-maxima[a-3])
                        if core+triangle_cover<=D(m+3):tri=max(general,triangle_cover-3)
                    q=min(tf,tri)
                handshake=ceiling(n*h,2)
                local=comb(h+1,2)+q
                row=max(handshake,core+local)
                rows.append(dict(h=h,m=m,status='BOUND',core=core,q_floor=q,pair_cover=pair_cover,
                    triangle_cover=triangle_cover,triangle_free_q=tf,triangle_q=tri,
                    local=local,handshake=handshake,structural=core+local,row_floor=row))
            best=min((row['row_floor'] for row in rows if row['status']=='BOUND'),default=INF)
            value=max(common,best)
            details[f'{a},{n}']=dict(a=a,n=n,turan_floor=generic,deletion_floor=deletion,seed_floor=seed,
                minimum_row=best,floor=value if value<=D(n) else INF,rows=rows)
            if value<=D(n):table[a][n]=value
        maxima[a]=next((n-1 for n in range(1,LIMIT+1) if table[a][n]>=INF),LIMIT)
    return table,maxima,details
