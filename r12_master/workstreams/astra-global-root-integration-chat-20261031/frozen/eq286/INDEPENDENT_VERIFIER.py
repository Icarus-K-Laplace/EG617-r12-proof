"""Independent finite checks supporting the prose proof; not a formal proof assistant.
Does not import the search or trust its output. Python standard library only.
"""
import itertools as it
import json
from pathlib import Path


def canon(edges):
    return min(tuple(sorted(sum(1 << p[i] for i in range(4) if e >> i & 1)
                            for e in edges)) for p in it.permutations(range(4)))


def supports():
    allowed = [s for s in range(16) if s.bit_count() >= 2]
    result = {}
    for h in range(3,6):
        orbits = set()
        for edges in it.combinations_with_replacement(allowed,h):
            if sum(s.bit_count()-1 for s in edges) != 5:
                continue
            degrees = [sum(s >> i & 1 for s in edges) for i in range(4)]
            if min(degrees) >= 2:
                orbits.add(canon(edges))
        result[h] = orbits
    listed = [
        ['0123','01','23'],['01','023','123'],
        ['01','01','023','23'],['01','012','03','23'],['01','02','03','123'],
        ['01','01','02','03','23'],['01','02','02','13','13'],
        ['01','02','03','12','13'],['01','01','02','13','23'],['01','01','01','23','23']]
    expected = {h: {canon([sum(1 << int(i) for i in s) for s in row])
                       for row in listed if len(row)==h} for h in range(3,6)}
    assert result == expected
    return {str(h):len(v) for h,v in result.items()}


def scalar_checks():
    minima = {}
    for k,l,want,unique in [(11,11,6,None),(10,11,4,(2,3)),(9,11,2,(2,4)),(10,10,2,(3,3))]:
        values = {}
        for a in range(1,k):
            for b in range(1,l):
                cost = max(0,k+l-12-a-b)+a*max(0,k-13+b)+b*max(0,l-13+a)
                values[a,b] = cost
                if (k,l)==(11,11):
                    if cost<=8:
                        assert min(a,b)<=2
                        if a==2: assert b<=4
                    if (a<=b and a<=2) or a==2:
                        assert max(0,10-a-b)+a*max(0,b-2)>=6
        best=min(values.values())
        assert best==want
        if unique:
            assert [ab for ab,c in values.items() if c==best]==[unique]
        minima[f'{k}/{l}']=best
    for offset,k,want in [(9,10,6),(8,9,5)]:
        assert min(max(0,offset-a-b)+a*(b-1)+b*max(0,a-2)
                   for a in range(1,k) for b in range(1,11))==want
    assert min(max(0,9-a-b)+a*max(0,b-2)+b*max(0,a-2)
               for a in range(1,10) for b in range(1,11))==5
    # Shared leaf, and diamond center (at most one zero opposite missing set).
    checked=0
    for sizes in it.product(range(11),repeat=2):
        assert max(0,sum(x-1 for x in sizes)) >= sum(max(0,x-2) for x in sizes)
    for sizes in it.product(range(11),repeat=3):
        if sizes.count(0)>1: continue
        for mask in range(8):
            chosen=[x for i,x in enumerate(sizes) if mask >> i & 1]
            assert max(0,sum(x-1 for x in chosen))>=sum(max(0,x-2) for x in chosen)
            checked+=1
    for a,b,c in it.combinations_with_replacement(range(1,11),3):
        if a+b+c>=19: assert b>=5 and b+c>=13
    return {"pair_minima":minima,"diamond_subset_checks":checked}


def independent_intersections():
    # Ordered points, reconstructed using per-vertex incidence categories.
    best=1000
    count=0
    for a,b,aa,bb in it.product(range(1,11),repeat=4):
        for r in range(max(0,a+aa-10),min(a,aa)+1):
            for s in range(max(0,b+bb-10),min(b,bb)+1):
                for t in (False,True):
                    if t and (a+aa-r<=1 or b+bb-s<=1): continue
                    clique_cost=0
                    for one,two,both,op1,op2,overlap in [(a-r,aa-r,r,b,bb,s),(b-s,bb-s,s,a,aa,r)]:
                        clique_cost+=one*max(0,10+1+op1-12)
                        clique_cost+=two*max(0,10+1+op2-12)
                        clique_cost+=both*max(0,10+op1+op2-overlap-12)
                    own=max(0,22-a-b+int(t)-12)+max(0,22-aa-bb+int(t)-12)
                    if not t:
                        common=22-(a+aa-r)-(b+bb-s)
                        own=max(own,common-3)
                    best=min(best,clique_cost+own)
                    assert clique_cost+own>8
                    count+=1
    assert best==14
    return {"ordered_tuples":count,"minimum":best}


def arithmetic():
    def pk(n,k):
        q,r=divmod(n,k)
        return r*(q+1)*q//2+(k-r)*q*(q-1)//2
    bounds=[pk(47-q,3)+12*q+8-q*(q-1)//2 for q in range(1,9)]
    assert min(bounds)==310
    assert max((2*k+1)+k*(24-2*k)+(24-2*k)**2//4 for k in range(2,13))==145
    floor=lambda s:4 if s==0 else (3 if s==1 else 2)
    caps={}
    for S in (3,4):
        # all labeled allocations of S units to eleven colors
        floors=[]
        for allocation in it.combinations_with_replacement(range(11),S):
            floors.append(sum(floor(allocation.count(i)) for i in range(11)))
        caps[411-S]=60-min(floors)
    assert caps=={408:19,407:20}
    for E,q in [(407,30),(408,31)]:
        assert E-91-q==286
        for z in range(22,q+1):
            G=q-z; b=q+z
            assert (b-39)+G==2*E-13*61
            assert 39<=b and 91-z<=69
        assert E-91-287==q-1
    return {"regular_four_set_bounds":bounds,"full_color_caps":caps,
            "Type_I_allowed_pairs":[[5,8],[6,7],[7,6],[8,5]],
            "Type_I_note":"listed from audited source, not independently classifying extremal graphs"}


if __name__=='__main__':
    result={"status":"PASS","scope":"finite lemmas and accounting only; prose proof and accepted gates remain explicit",
            "support_orbits":supports(),"scalars":scalar_checks(),
            "double_pair":independent_intersections(),"arithmetic":arithmetic()}
    Path(__file__).with_name('VERIFICATION_RESULT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
