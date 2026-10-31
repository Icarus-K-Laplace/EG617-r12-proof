"""Root integration arithmetic audit; no 47-graph or COVER shell search.

Run python -B INDEPENDENT_VERIFIER.py. Analytic proofs are in the accompanying
documents. PASS does not mean that a proof-assistant kernel checked those proofs.
"""
from pathlib import Path
from math import comb
import hashlib
import importlib.util
import itertools
import json
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent


def c2(n):
    return n*(n-1)//2


def p(k,n):
    quotient,remainder=divmod(n,k)
    return k*c2(quotient)+quotient*remainder


def cap(n):
    return c2(n)-11*p(12,n)


def ceildiv(x,y):
    return -(-x//y)


def import_file(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replay_third():
    """Third transcription of the proved contextual recurrence.

    Infinity is None. Returns every node and all min-degree rows for T61.
    No bound or case output is read from the two frozen implementations.
    """
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
            for degree in range(n):
                m=n-1-degree
                core=bound[a-1,m]
                if core is None:
                    rows.append({'h':degree,'excluded':'empty core'})
                    continue
                defect=max(p(10,degree),c2(degree+1)-cap(degree+1),
                           c2(degree)-cap(degree))
                if degree>=11:
                    beta=max(0,m-maximum[a-2])
                    if core+beta>cap(m+2):
                        rows.append({'h':degree,'excluded':'pair cap'})
                        continue
                    matching=max(ceildiv(degree-10,2),1+int(degree>=12)+int(degree>=13))
                    ordinary=max([defect,beta-1]+[
                        t*beta-c2(2*t)+p(a,2*t) for t in range(1,matching+1)])
                    channels=[max([ordinary]+[t*(beta-t) for t in range(1,matching+1)])]
                    if a>=3:
                        gamma=max(0,m-maximum[a-3])
                        if core+gamma<=cap(m+3):
                            channels.append(max(ordinary,gamma-3))
                    defect=min(channels)
                value=max(ceildiv(n*degree,2),core+c2(degree+1)+defect)
                alternatives.append(value)
                rows.append({'h':degree,'core':core,'q_floor':defect,'row_floor':value})
            if not alternatives:
                bound[a,n]=None
            else:
                value=max(p(a,n),seeds.get((a,n),0),min(alternatives),
                          ceildiv(n*bound[a,n-1],n-2) if n>2 else 0)
                bound[a,n]=value if value<=cap(n) else None
            if (a,n)==(5,61):
                terminal_rows=rows
        maximum[a]=max(n for n in range(146) if bound[a,n] is not None)
    return bound,maximum,terminal_rows


def verify_sources():
    manifest=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
    records=[]
    for row in manifest:
        data=(ROOT/row['destination']).read_bytes()
        blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        assert blob==row['blob'],row['destination']
        records.append({'path':row['destination'],'git_blob':blob,
                        'sha256':hashlib.sha256(data).hexdigest()})
    return records


def verify_frontend():
    third,maximum,rows=replay_third()
    a=import_file('frozen_a',ROOT/'frozen/frontend/recurrence_a.py')
    b=import_file('frozen_b',ROOT/'frozen/frontend/recurrence_b.py')
    first,ma,_=a.compute()
    second=b.replay()
    nodes=[]
    for alpha in range(1,13):
        for n in range(146):
            value=None if first[alpha][n]>=a.INF else first[alpha][n]
            assert value==second['bounds'][alpha,n]==third[alpha,n],(alpha,n)
            nodes.append({'a':alpha,'n':n,'bound':value})
        assert ma[alpha]==second['maxima'][alpha]==maximum[alpha]
    stops=[]
    for degree,packing in itertools.product(range(12),repeat=2):
        alpha,n=11-packing,144-degree-12*packing
        value=third[alpha,n]
        budget=870-c2(degree+1)-66*packing
        stops.append({'d':degree,'j':packing,'a':alpha,'n':n,'budget':budget,
                      'bound':value,'survives':value is not None and value<=budget})
    survivors=[r for r in stops if r['survives']]
    assert survivors==[{'d':11,'j':6,'a':5,'n':61,'budget':408,'bound':397,'survives':True}]
    eligible=[r for r in rows if r.get('row_floor',10**9)<=408]
    assert eligible==[{'h':12,'core':308,'q_floor':20,'row_floor':406},
                      {'h':13,'core':284,'q_floor':22,'row_floor':397}]
    payload={'scope':'contextual exact integer recurrence; analytic rules audited separately',
             'nodes':nodes,'max_orders':maximum,'outer_stops':stops,'T61_rows':rows}
    (ROOT/'FRONTEND_REPLAY.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    return {'implementations':3,'nodes_checked':len(nodes),'outer_stops_checked':len(stops),
            'survivors':survivors,'eligible_minimum_degrees':eligible}


def verify_cover_retained():
    module=import_file('cover_retained',ROOT/'frozen/cover/INDEPENDENT_VERIFIER.py')
    record=json.loads((ROOT/'frozen/cover/VERIFICATION_RESULT.json').read_text())
    digest=hashlib.sha256((ROOT/'frozen/cover/INDEPENDENT_VERIFIER.py').read_bytes()).hexdigest()
    assert digest==record['source_sha256']
    assert [r['canonical_states'] for r in record['bipartite']]==[2,8]
    for row in record['bipartite']:
        retained={module.canonical(s['hub_weights'],s['rows']) for s in row['states']}
        assert retained==module.expected_states(row['q'])
        module.check_every_state_directly(row)
    identities=module.repivot_identity_checks()
    assert identities['algebraic_instances']==104
    arithmetic=module.arithmetic()
    return {'retained_states':[2,8],'subset_identity_checks':81920,
            'repivot_identity_checks':104,'arithmetic':arithmetic,
            'shell_search_rerun':False,
            'completeness_evidence':'frozen enumeration algorithm, prior authenticated result, analytic reductions'}


def verify_new_arithmetic():
    assert 11*79==869 and c2(49)-869==307<319==ceildiv(49*13,2)
    assert p(12,49)==76 and cap(38)==241<234+13
    assert 22*8>5*35
    assert 78+20+211==309 and 78+21+211==310
    assert 78+20+310==408
    assert 91+29+287==407
    assert 407-91-287==29<30 and 408-91-287==30<31
    families=[]
    for r in range(6,11):
        z=2*r
        decoration=2*(10-r)
        assert z+decoration==20 and z>=11
        assert 10+1<12
        families.append({'r':r,'z':z,'decoration':decoration,'inserted_hub_degree_upper':11})
    # Only the tiny support quotient is reconstructed, not any 47-point graph.
    types=[frozenset(x) for size in (2,3,4) for x in itertools.combinations(range(4),size)]
    orbits={k:set() for k in (3,4,5)}
    for k in orbits:
        for labels in itertools.combinations_with_replacement(types,k):
            if sum(map(len,labels))!=k+5:continue
            if any(sum(i in label for label in labels)<2 for i in range(4)):continue
            canon=min(tuple(sorted(tuple(sorted(perm[i] for i in label)) for label in labels))
                      for perm in itertools.permutations(range(4)))
            orbits[k].add(canon)
    assert [len(orbits[k]) for k in (3,4,5)]==[2,3,5]
    pointwise=0
    for a,b in itertools.product(range(12),repeat=2):
        assert max(0,a+b-2)>=max(0,a-2)+max(0,b-2)
        pointwise+=1
    for xs in itertools.product(range(12),repeat=3):
        if xs.count(0)>1:continue
        assert max(0,sum(x-1 for x in xs))>=sum(max(0,x-2) for x in xs)
        pointwise+=1
    return {'contextual49':[319,307],'R448_floor':310,'h12_equality_families':families,
            'h13_lower_energy_floor':407,
            'support_orbits':[2,3,5],'shared_excess_pointwise_checks':pointwise}


def verify_lower_order_families():
    module=import_file('lower_order',ROOT/'frozen/low/INDEPENDENT_VERIFIER.py')
    # These are 23-point explicit family checks, not 284/285/286 graph searches.
    return {'types':module.type_classification(),
            'neighborhood_costs':module.neighborhood_extension_costs(),
            'minimum_degree_arithmetic':module.minimum_degree_and_parents()}


def verify_dag():
    path=ROOT/'PROOF_DAG.json'
    assert path.exists(),'proof DAG is required'
    graph=json.loads(path.read_text())
    seen=set()
    active=set()
    def visit(node):
        assert node in graph,node
        assert node not in active,('cycle',node)
        if node in seen:return
        active.add(node)
        for parent in graph[node]:visit(parent)
        active.remove(node)
        seen.add(node)
    for node in graph:visit(node)
    return {'status':'ACYCLIC','nodes':len(seen)}


def main():
    result={'status':'PASS','scope':'finite arithmetic and provenance; analytic proof audit in Markdown',
            'sources':verify_sources(),'frontend':verify_frontend(),
            'cover':verify_cover_retained(),'lower_order':verify_lower_order_families(),
            'new_arithmetic':verify_new_arithmetic(),'dag':verify_dag()}
    result['verifier_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT/'VERIFICATION_RESULT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('sources','cover')},indent=2))


if __name__=='__main__':
    main()
