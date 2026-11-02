#!/usr/bin/env python3
"""Two-transcription independent replay of the contextual EG617 frontend recurrence."""
from math import comb, ceil

def c2(n):
    return n*(n-1)//2

def p(k,n):
    q,r=divmod(n,k)
    return k*c2(q)+q*r

def cap(n):
    return c2(n)-11*p(12,n)

def ceildiv(x,y):
    return -(-x//y)

def replay_a():
    bound={(0,0):0}
    bound.update({(0,n):None for n in range(1,146)})
    maximum={0:0}
    seeds={(2,23):131,(3,35):210,(3,36):234,(4,47):284,(4,48):308}
    cutoff={1:12,2:24,3:37,4:49}
    terminal_rows=[]
    for a in range(1,13):
        bound[a,0]=0
        for n in range(1,146):
            if n>=cutoff.get(a,146) or bound[a,n-1] is None:
                bound[a,n]=None
                continue
            alternatives=[]
            rows=[]
            for h in range(n):
                m=n-1-h
                core=bound[a-1,m]
                if core is None:
                    rows.append({"h":h,"excluded":"empty core"})
                    continue
                defect=max(p(10,h),c2(h+1)-cap(h+1),c2(h)-cap(h))
                if h>=11:
                    beta=max(0,m-maximum[a-2])
                    if core+beta>cap(m+2):
                        rows.append({"h":h,"excluded":"pair cap"})
                        continue
                    k=max(ceildiv(h-10,2),1+int(h>=12)+int(h>=13))
                    ordinary=max([defect,beta-1]+[
                        t*beta-c2(2*t)+p(a,2*t) for t in range(1,k+1)
                    ])
                    channels=[max([ordinary]+[t*(beta-t) for t in range(1,k+1)])]
                    if a>=3:
                        gamma=max(0,m-maximum[a-3])
                        if core+gamma<=cap(m+3):
                            channels.append(max(ordinary,gamma-3))
                    defect=min(channels)
                value=max(ceildiv(n*h,2),core+c2(h+1)+defect)
                alternatives.append(value)
                rows.append({"h":h,"core":core,"q_floor":defect,"row_floor":value})
            if not alternatives:
                bound[a,n]=None
            else:
                value=max(p(a,n),seeds.get((a,n),0),
                          min(alternatives),
                          ceildiv(n*bound[a,n-1],n-2) if n>2 else 0)
                bound[a,n]=value if value<=cap(n) else None
            if (a,n)==(5,61):
                terminal_rows=rows
        maximum[a]=max(n for n in range(146) if bound[a,n] is not None)
    return bound,maximum,terminal_rows

def replay_b():
    limit=145
    bounds={(0,0):0}
    maxima={0:0}
    for n in range(1,limit+1):
        bounds[0,n]=None
    seeds={(2,23):131,(3,35):210,(3,36):234,(4,47):284,(4,48):308}
    empty_at={1:12,2:24,3:37,4:49}
    for a in range(1,13):
        bounds[a,0]=0
        for n in range(1,limit+1):
            if n>=empty_at.get(a,limit+1) or bounds[a,n-1] is None:
                bounds[a,n]=None
                continue
            deletion=ceildiv(n*bounds[a,n-1],n-2) if n>2 else 0
            generic=max(p(a,n),deletion,seeds.get((a,n),0))
            rows=[]
            for h in range(n):
                m=n-h-1
                core=bounds[a-1,m]
                row={"h":h,"m":m,"core":core,"handshake":ceildiv(n*h,2)}
                if core is None:
                    row["excluded"]="empty core"
                    rows.append(row)
                    continue
                z=max(p(10,h),c2(h+1)-cap(h+1),c2(h)-cap(h))
                q=z
                row["z_floor"]=z
                if h>=11:
                    beta=max(0,m-maxima[a-2])
                    row["pair_cover"]=beta
                    if core+beta>cap(m+2):
                        row["excluded"]="pair density"
                        rows.append(row)
                        continue
                    k=max(ceildiv(h-10,2),1+(h>=12)+(h>=13))
                    match_general=max(
                        t*beta-c2(2*t)+p(a,2*t) for t in range(1,k+1)
                    )
                    qbase=max(q,beta-1,match_general)
                    triangle_free=max(
                        qbase,max(t*beta-t*t for t in range(1,k+1))
                    )
                    gamma=max(0,m-maxima[a-3]) if a>=3 else None
                    triangular=(
                        max(qbase,gamma-3)
                        if a>=3 and core+gamma<=cap(m+3)
                        else None
                    )
                    q=min(triangle_free,triangular) if triangular is not None else triangle_free
                row.update(q_floor=q,local_identity_floor=c2(h+1)+q+core)
                row["row_floor"]=max(row["handshake"],row["local_identity_floor"])
                rows.append(row)
            active=[r["row_floor"] for r in rows if "row_floor" in r]
            row_min=min(active) if active else None
            raw=max(generic,row_min) if row_min is not None else None
            bounds[a,n]=raw if raw is not None and raw<=cap(n) else None
        maxima[a]=next(
            (n-1 for n in range(1,limit+1) if bounds[a,n] is None),
            limit
        )
    return bounds,maxima

def main():
    first,maxima,terminal_rows=replay_a()
    second,maxima2=replay_b()
    mismatches=[
        (a,n,first[a,n],second[a,n])
        for a in range(13) for n in range(146)
        if first[a,n]!=second[a,n]
    ]
    assert not mismatches
    assert maxima==maxima2
    stops=[]
    for d in range(12):
        for j in range(12):
            a=11-j
            n=144-d-12*j
            budget=870-c2(d+1)-66*j
            lower=first[a,n]
            stops.append({
                "d":d,"j":j,"a":a,"n":n,"budget":budget,
                "bound":lower,
                "survives":lower is not None and lower<=budget
            })
    survivors=[r for r in stops if r["survives"]]
    assert survivors==[{
        "d":11,"j":6,"a":5,"n":61,"budget":408,
        "bound":397,"survives":True
    }]
    eligible=[
        {"h":r["h"],"core_floor":r["core"],
         "charge_floor":r["q_floor"],"row_floor":r["row_floor"]}
        for r in terminal_rows
        if "row_floor" in r and r["row_floor"]<=408
    ]
    assert eligible==[
        {"h":12,"core_floor":308,"charge_floor":20,"row_floor":406},
        {"h":13,"core_floor":284,"charge_floor":22,"row_floor":397}
    ]
    print({
        "status":"PASS",
        "node_count":12*146,
        "mismatches":len(mismatches),
        "maximum_orders":maxima,
        "outer_stop_count":len(stops),
        "survivors":survivors,
        "budget_compatible_T61_rows":eligible
    })

if __name__=="__main__":
    main()
