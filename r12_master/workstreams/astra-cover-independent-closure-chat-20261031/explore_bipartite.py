import itertools as it, json
from pathlib import Path

def enumerate_bip(q):
    found=[]; nodes=0
    for gy in range(q-21):
        for xs in it.combinations_with_replacement(range(1,q+1),3):
            if sum(xs)!=q-gy: continue
            types=[]
            for mask in range(8):
                d=mask.bit_count()
                for g in range(gy+1):
                    if any(xs[i]+d+g<12 for i in range(3) if mask>>i&1): continue
                    if not g and sum(xs[i] for i in range(3) if mask>>i&1)<d*(12-d): continue
                    types.append((mask,g,d))
            def rec(start,left,budget,degs,z,rows):
                nonlocal nodes
                nodes+=1
                if z+3*left<22 or z>q: return
                if any(degs[i]>xs[i] for i in range(3)): return
                if not left:
                    if budget or z<22: return
                    gs=[xs[i]-degs[i] for i in range(3)]
                    if sum(gs)+gy!=q-z: return
                    if any(degs[i]==0 for i in range(3)): return
                    for i in range(3):
                        if gs[i]==0:
                            ts=sum(d+g for mask,g,d in rows if mask>>i&1)
                            if ts<degs[i]*(12-degs[i]): return
                    # alpha(M)<=10 iff there is a matching saturating X
                    if not any(all(rows[js[i]][0]>>i&1 for i in range(3)) for js in it.permutations(range(10),3)): return
                    found.append({'x':xs,'hub_g':gs,'rows':[(m,g) for m,g,d in rows],'z':z})
                    return
                for j in range(start,len(types)):
                    mask,g,d=types[j]
                    if g>budget: continue
                    rec(j,left-1,budget-g,[degs[i]+(mask>>i&1) for i in range(3)],z+d,rows+[types[j]])
            rec(0,10,gy,[0,0,0],0,[])
    return {'q':q,'nodes':nodes,'candidates':found}
if __name__=='__main__':
    result=[enumerate_bip(q) for q in (27,28)]
    Path(__file__).with_name('BIPARTITE_EXPLORATION.json').write_text(json.dumps(result,indent=2))
    for r in result:
        print('q',r['q'],'nodes',r['nodes'],'candidates',len(r['candidates']))
        for c in r['candidates']: print(c)
