"""Exact finite certificate for the contextual, not generic, recurrence.

Run --write once to emit the certificate; otherwise independently verify it.
Both transcriptions implement the analytic rules in RECURRENCE_PROOF.md.
This is a finite arithmetic certificate, not a graph existence certificate.
"""
from pathlib import Path
from math import comb
import csv, json, sys
import recurrence_a as A
import recurrence_b as B

ROOT=Path(__file__).resolve().parent
def records():
    tab, maxima, details=A.compute()
    other=B.replay()
    nodes=[]
    for a in range(1,13):
        for n in range(146):
            av=None if tab[a][n]>=A.INF else tab[a][n]
            assert av==other['bounds'][a,n],(a,n,av,other['bounds'][a,n])
            nodes.append({'a':a,'n':n,'bound':av})
        assert maxima[a]==other['maxima'][a]
    outer=[]
    for d in range(12):
        for j in range(12):
            a,n=11-j,144-d-12*j
            budget=870-comb(d+1,2)-66*j
            val=None if tab[a][n]>=A.INF else tab[a][n]
            outer.append(dict(d=d,j=j,a=a,n=n,budget=budget,bound=val,
                              survives=val is not None and val<=budget))
    surviving=[r for r in outer if r['survives']]
    assert surviving==[dict(d=11,j=6,a=5,n=61,budget=408,bound=397,survives=True)]
    ar=details['5,61'];br=other['targets']['5,61']
    for aa,bb in zip(ar['rows'],br['rows']):
        assert (aa['status']=='EXCLUDED')==('excluded' in bb)
        if aa['status']=='BOUND':
            for f in ('core','q_floor','handshake','row_floor'):assert aa[f]==bb[f]
    low=[r for r in ar['rows'] if r.get('row_floor',A.INF)<=408]
    assert [(r['h'],r['core'],r['q_floor'],r['row_floor']) for r in low]==[(12,308,20,406),(13,284,22,397)]
    shell=[]
    for k in range(3):
        for a in range(8):
            for b in range(1,9):
                L=max(0,9-a-b)+a*max(0,b-2)+b*max(0,a-2)
                passes=L+max(0,k-1)<=6
                if not passes: disposition='local_lower_bound'
                elif k==2: disposition='certified_singleton_triangle_closure'
                elif a>=2 and L==6: disposition='new_saturated_B_vertex_closure'
                elif k==1 and (a,b)==(0,3): disposition='new_forced_tv_exceeds_budget'
                else: disposition='OPEN_scalar_case_only'
                shell.append(dict(k=k,a=a,b=b,local_lower=L,
                                  passes=passes,disposition=disposition))
    assert [sum(r['passes'] for r in shell if r['k']==k) for k in range(3)]==[22,22,6]
    assert [sum(r['disposition']=='OPEN_scalar_case_only' for r in shell if r['k']==k) for k in range(3)]==[14,13,0]
    assert A.p(5,49)==216 and A.p(6,61)==280 and A.p(12,61)==125
    assert 870-8*66-7*comb(8,2)-8*5==106
    assert 870-8*66-12*comb(8,2)-8*6==-42
    assert 870-7*66-6*comb(7,2)-7*6==240
    assert 870-7*66-12*comb(7,2)-7*7==107
    return dict(status='COMPUTATION_CERTIFIED',scope='exact arithmetic only; contextual no-induced-R449 hypothesis',
                nodes=nodes,max_orders=maxima,outer_rows=outer,O61_rows=ar['rows'],
                S30_local_rows=shell)

def main():
    data=records()
    path=ROOT/'FRONTEND_CERTIFICATE.json'
    if '--write' in sys.argv:
        path.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
        for name,rows in [('OUTER_STOP_TABLE.csv',data['outer_rows']),('S30_BC_CASES.csv',data['S30_local_rows'])]:
            with (ROOT/name).open('w',newline='',encoding='utf-8') as f:
                w=csv.DictWriter(f,list(rows[0]));w.writeheader();w.writerows(rows)
    else:
        assert json.loads(path.read_text(encoding='utf-8'))==data,'certificate differs from independent exact replay'
    print(json.dumps({'status':'COMPUTATION_CERTIFIED','nodes_checked':len(data['nodes']),
        'outer_stops_checked':len(data['outer_rows']),
        'surviving_stops':[r for r in data['outer_rows'] if r['survives']],
        'S30_checks':len(data['S30_local_rows']),
        'warning':'no graph completion or generic R449 emptiness is asserted'},indent=2))
if __name__=='__main__':main()
