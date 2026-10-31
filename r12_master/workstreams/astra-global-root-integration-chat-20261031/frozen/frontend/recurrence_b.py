"""Independent integer implementation of N2--N5, transcribed from proofs.

No imports from earlier recurrence implementations; no floating point or solver.
None means certified empty. Bounds are lower bounds, not claimed extrema.
"""

def choose2(n):
    return n*(n-1)//2

def turan_floor(a,n):
    u,v=divmod(n,a)
    return a*choose2(u)+u*v

def cap(n):
    return choose2(n)-11*turan_floor(12,n)

def ceildiv(x,y):
    return (x+y-1)//y

TARGETS={(5,60),(5,61),(6,73)}

def replay():
    limit=145
    bounds={(0,0):0}
    maxima={0:0}
    reports={}
    for n in range(1,limit+1): bounds[0,n]=None
    seeds={(2,23):131,(3,35):210,(3,36):234,(4,47):284,(4,48):308}
    empty_at={1:12,2:24,3:37,4:49}
    for a in range(1,13):
        bounds[a,0]=0
        for n in range(1,limit+1):
            if n>=empty_at.get(a,limit+1) or bounds[a,n-1] is None:
                bounds[a,n]=None
                continue
            deletion=ceildiv(n*bounds[a,n-1],n-2) if n>2 else 0
            generic=max(turan_floor(a,n),deletion,seeds.get((a,n),0))
            rows=[]
            for h in range(n):
                m=n-h-1
                core=bounds[a-1,m]
                row={'h':h,'m':m,'core':core,'handshake':ceildiv(n*h,2)}
                if core is None:
                    row['excluded']='empty core';rows.append(row);continue
                z=max(turan_floor(10,h),choose2(h+1)-cap(h+1),choose2(h)-cap(h))
                q=z
                row['z_floor']=z
                if h>=11:
                    beta=max(0,m-maxima[a-2])
                    row['pair_cover']=beta
                    if core+beta>cap(m+2):
                        row['excluded']='pair density';rows.append(row);continue
                    k=max(ceildiv(h-10,2),1+(h>=12)+(h>=13))
                    match_general=max(t*beta-choose2(2*t)+turan_floor(a,2*t) for t in range(1,k+1))
                    qbase=max(q,beta-1,match_general)
                    triangle_free=max(qbase,max(t*beta-t*t for t in range(1,k+1)))
                    gamma=max(0,m-maxima[a-3]) if a>=3 else None
                    triangular=max(qbase,gamma-3) if a>=3 and core+gamma<=cap(m+3) else None
                    q=min(triangle_free,triangular) if triangular is not None else triangle_free
                    row.update(matching_guarantee=k,general_matching_floor=match_general,
                               triangle_free_floor=triangle_free,triangle_floor=triangular,
                               triangle_cover=gamma)
                row.update(q_floor=q,local_identity_floor=choose2(h+1)+q+core)
                row['row_floor']=max(row['handshake'],row['local_identity_floor'])
                rows.append(row)
            active=[r['row_floor'] for r in rows if 'row_floor' in r]
            row_min=min(active) if active else None
            raw=max(generic,row_min) if row_min is not None else None
            bounds[a,n]=raw if raw is not None and raw<=cap(n) else None
            if (a,n) in TARGETS:
                reports[f'{a},{n}']={'floor':bounds[a,n],'density_cap':cap(n),
                    'turan_floor':turan_floor(a,n),'deletion_floor':deletion,
                    'seed_floor':seeds.get((a,n),0),'generic_floor':generic,
                    'row_minimum':row_min,'minimum_row_ties':[r['h'] for r in rows if r.get('row_floor')==row_min],
                    'floor_compatible_rows':[r['h'] for r in rows if 'row_floor' in r and r['row_floor']<=raw],
                    'rows':rows}
        maxima[a]=next((n-1 for n in range(1,limit+1) if bounds[a,n] is None),limit)
    return {'bounds':bounds,'maxima':maxima,'targets':reports,
            'inputs':{'floors':{f'{a},{n}':v for (a,n),v in seeds.items()},'empty_at':empty_at}}
