"""Render the manually adjudicated obligation ledger; does not prove mathematics."""
from pathlib import Path
import json
import subprocess
import hashlib

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
items=[]
def add(key,statement,hypotheses,deps,derivation,critical,attack,status='PROVED'):
    items.append(dict(id=key,Lemma=statement,Hypotheses=hypotheses,dependencies=deps.split(),
                      Independent_derivation=derivation,Critical_step=critical,
                      Counterexample_search=attack,Status=status))

add('TURAN','e(J)>=p_a(n) if alpha(J)<=a','Simple finite graph; positive integer a','','Published Turan, complement specialization; F1','Complement direction','Checked balanced-part formula against integer sum')
add('BROOKS','Delta<=12 and no K13 component imply chi<=12','Finite simple graph; degree bound12>2','','Original Brooks reprint p537; F1','Disconnected graphs and clique exception','Checked every component, no odd-cycle exception at degree12')
add('AES','K4-free delta>5n/8 implies 3-partite','Finite simple graph; strict inequality','','Original1974 Theorem1.1 with r=4; F2','Strict rather than weak inequality','176>175; equality theorem not used')
add('SECOND_TURAN','Non-r-partite K_(r+1)-free graph has at most t_r(n)-floor(n/r)+1 edges','n>=r+3; 2<=r<=(n-1)/2','','Original2005 Theorem1 p13; F2','Correct range and nonpartiteness','n49,r12 and n25,r2 satisfy all conditions')
add('CAPS','Every induced target subgraph obeys D','Original K145 coloring with all12 colors in every13-set','TURAN','F1: sum lower bounds for other11 colors','Caps hold on every subset','No least-color assumption in induced cap derivation')
add('ODDCYCLE','B18<=73, B23<=122, B25<=145','Nonbipartite triangle-free graphs of indicated orders','TURAN','L1: shortest odd cycle, at most k attachments per outside vertex, Mantel outside','Cycle must be chordless; all k covered','Enumerated all feasible k; n23,k>=3 max119')
add('R224','R(2,24) is empty','R includes omega11 and all D-caps','CAPS','L1: forced12-regular target; 11-regular complement; quadratic contradiction','Complement may have target cross edges','Discriminant -47; no disjoint-union assumption')
add('R223','Every R(2,23) has >=131 edges','R(2,23)','ODDCYCLE','L1: complement cannot be bipartite and has <=122 edges','Using omega bound for nonbipartiteness','253-122=131')
add('TF23','Complete121/122 classification of23-point triangle-free W','alpha(W)<=11; e(W)>=121','ODDCYCLE','L1: C5 exterior80+, three bipartite possibilities, endpoint type analysis','K9,9 minus one edge exceptional endpoints','All20 type pairs and10 exceptional endpoint cases rebuilt')
add('COST12','For each classified W and independent I exists12-set T of cost<=6','TF23 hypotheses; I independent in W','TF23','L1: three explicit12-sets; deleted-edge and special blowup cases','New independent sets created by deletion','61 representatives,49 valid,263 maximal independent sets checked')
add('DEL335','Every R(3,35) has delta>=12','alpha3,omega11,induced caps','R224 COST12 CAPS','L2: degree11 gives complement23-neighborhood and14-set with72>69 edges','Common-neighbor set independent in complement','Explicit target cross-edge lower bound12-|T intersect I|')
add('ORD3637','R(3,36) has delta>=13,e>=234; R(3,37) empty','Respective R contracts','R224 DEL335 CAPS','L2: delete a neighbor at degree12; handshake at37','Deletion remains in hereditary R class','Degree11/12 and all lower degrees included')
add('CORE211','Every R(3,35) has e>=211','R(3,35)','DEL335 AES','L2: equality210 gives22-regular complement and forbidden independent part12','AES applies only at equality','Strict threshold checked from primary theorem')
add('GATE47','R(4,47),e<=286 implies delta>=12','Full R contract and edge range','ORD3637 DEL335 R224','L2: d<=9, d10 and d11 treated separately','Do not assume shell clique','d10 floor289; d11 floor287; all cross edges retained')
add('NO25','No25-set of alpha<=2 in low-edge47 graph','n47,delta12,omega11,T<=8','ODDCYCLE','L3: degree upper154 versus complement-derived lower155','Target need not be disjoint union of cliques','T6 and T8 boundaries separately checked')
add('COMMON','c(u,v)<=3+epsilon(u)+epsilon(v) for a nonedge','n47,delta12,alpha4,omega11,T<=8','NO25','L3: common antineighborhood size21+c-epsu-epsv','Use24, not23, as maximum uncovered size','At T8 bound11; uniqueness of K10 completion not imported')
add('REGULAR4','Independent four-set of degree12 vertices exists','n47,delta12,alpha4,omega11, e<=286','TURAN','L4: Turan on regular set plus incident exceptional edges','Subtract exceptional internal edges once','q0 included at T0; all q<=8 bounds checked')
add('SUPPORT_MAP','All actual four-seed supports map to enumerated multiset domain','REGULAR4; alpha4;omega11','REGULAR4','L4:48 incidences on43 vertices, surplus5; d_i>=2; h3..5','Repeated support sets and zero missing sets','All subsets of size2..4 allowed, multiplicities retained')
add('SUPPORT_ORBITS','Exactly2,3,5 support orbits at h3,4,5','Finite domain from SUPPORT_MAP','SUPPORT_MAP','L4 and support_orbits(): all combinations with replacement and24 permutations','Count agreement alone insufficient','Actual canonical sets equal all ten stated orbits; raw9,40,48','COMPUTATIONALLY_VERIFIED')
add('BLOCKERS','Two-support point forces complete bipartite missing sets; scalar minima6,4,2,2','Actual independent seeds; support exactly two; positive missing sets for scalar form','REGULAR4','L4: independent5 obstruction and disjoint vertex charges','Blocker invalid for triple support','Threshold proof plus full bounded scalar enumeration')
add('SHARED','Shared-leaf and diamond pointwise excess inequalities','Distinct opposite cliques; at most one negative increment, or two incidences','BLOCKERS','L4: baseline12; replace support neighbor by forced neighbors before summing','Do not sum two full excess charges at same vertex','All zero-size cases and all bounded increment tuples checked')
add('LOW285','No47 graph with e<=285,delta12,alpha4,omega11','Exactly the five abstract hypotheses; no caps required','COMMON SUPPORT_ORBITS BLOCKERS SHARED','L5: all support cases; pair equality trigger; P costs8 and D10','T0, complete K9/K10 attachments and support rotation','Direct analytic route reconstructed without augmentation')
add('EXACT285','No47 graph with e285,delta12,alpha4,omega11','Same five hypotheses, equality285','COMMON SUPPORT_ORBITS BLOCKERS SHARED','L5 specialized to T6; original U1-U6 source read and separately traced','Do not depend on low-edge augmentation','Source at f56cc9e, exact blob authenticated')
add('AUGMENT','Every nonedge can be added safely until285 edges','Abstract47 graph with282<=e<285,delta12,alpha4,omega11','COMMON EXACT285','L3: fewer than10 common neighbors prevents new K12; at most3 steps','D-caps need not be preserved','All five actual terminal hypotheses preserved, reapply capacity each step')
add('EQ286','No47 graph with e286,delta12,alpha4,omega11','Exactly five abstract hypotheses, T8','COMMON SUPPORT_ORBITS BLOCKERS SHARED','L6: all ten orbits, concentration, triple cost, doubled-pair intersection proof','T6 completion uniqueness and repeated excess would be invalid','All intersections of size1/2 missing sets treated explicitly')
add('FLOOR287','Every R(4,47) has e>=287','Full R contract','GATE47 LOW285 EQ286','L6 conclusion by disjoint edge ranges','Minimum-degree gate only licensed at<=286','No generic degree12 assertion for all47 cores')
add('PIVOT','47-core inheritance and E=91+q+e(C), subset identity','n61,delta13,alpha5,omega11,caps; p regular','CAPS','C1: exact degree and edge partition','A need not be clique','Explicit g=d_F-13 and t=d_M+g')
add('CORE11','Every actual47-core has delta>=11; deficient vertices form clique','Same61 contract, no energy restriction','ORD3637 R224 DEL335 PIVOT','C2: exclude embedded36 object; take antineighborhoods','All actual pivots, not selected pivot only','Outside25 alpha2 contradiction; nonadjacent deficient pair contradicted')
add('COVER_ROWS','Missing edge/triangle/K4 row unions >=12/24/36','Same61 contract','CORE11 R224','C2: uncovered alpha3/2/1 sets','Use union before sum of row sizes','Overlaps can only weaken size sum, never strengthen it illicitly')
add('EXCHANGE','C2-C4 exact repivot identities and INS11','p,y regular in same61 graph; beta licensed separately','PIVOT CORE11','C1-C2: removed/inserted edge counts with internal edges corrected once','Signs of m,kappa and eta; no closed-cycle zero inference','312 random algebra instances; independent symbolic derivation')
add('MATCH3','13-point M with z>=22,alpha<=10 has3-matching','Simple M on13 vertices','TURAN','C3: two-matching endpoints and bipartite cover cases','Cross cover with one endpoint on each side','Bounds12+6 and8+6 fail22; two S-cover points yield independent11')
add('SMALLQ_REDUCTION','Every regular q<=28 shell is bipartite3+10 and q>=27','Same61 contract, q<=28','COVER_ROWS EXCHANGE MATCH3 TURAN','C3: every triangular channel, odd-cycle and cover case','Single outside edge, stars, empty rows, decorated endpoints','INS11 excludes triangular leaf26<27; isolates retained')
add('ENUM_MAP','Every reduced shell appears in bounded row/decor enumeration; canonical keys exact','SMALLQ_REDUCTION, q27 or28','SMALLQ_REDUCTION','C4: stars-and-bars, Hall equivalence, all budget multisets and S3 quotient','Necessary filters may not be mistaken for sufficiency','19448 vectors; zero decoration and empty masks explicitly included')
add('ENUM2728','Exactly2 q27 and8 q28 canonical necessary states','Finite domain licensed by ENUM_MAP','ENUM_MAP','C4 and independently implemented shell_replay','An unenumerated state would invalidate geometry','Exact set comparison;81920 subset identities;107 regular INS11 tests','COMPUTATIONALLY_VERIFIED')
add('GEO2728','Q27 and six non-B1 Q28 states impossible','Maximum over all actual regular vertices; ENUM2728','ENUM2728 EXCHANGE CORE11','C5: maximality forces zero nonnegative corrections; deficient rows coincide','Cannot equate rows from cycle summation','Different-row point loses3 and gains0;14-set79>69')
add('B1','Both B1 Q28 states impossible','Same maximum-charge contract','ENUM2728 EXCHANGE CORE11','C5: regular K11; triples equal/disjoint, multiplicity2/3; base points','Classification at specified cover and global pivot quantifiers','At least4 row classes; two nonadjacent deficient base points in one core')
add('Q29','Q>=29 for every61 graph with minimum degree13 and stated hereditary contract','n61,delta13,alpha5,omega11,caps; no E restriction','SMALLQ_REDUCTION GEO2728 B1','C5 conclusion after all Q<=28 alternatives','Energy independence must be checked, not assumed','No407/408 parameter in derivation')
add('GATE288','Actual47-core of e<=288 has delta>=12 and original shell EDGE13','Same61 contract plus core edge bound','CORE11 CORE211 R223 COVER_ROWS','C6: equality288 produces14-set76>69; complement12-set gives210<211','Only strengthened cores receive beta12','Each actual repivot checked before eta12 use')
add('PROM29','At q<=29,e(C)<=288 there is a regular repivot q_y>=30','Same61 contract and stated local bounds','GATE288 EXCHANGE','C6: high-weight-set cases0,1,2; middle degree3..10','Decorated points outside X can still carry edges','All X cases and regular degrees0,1,2 included')
add('CLASS30','At E408,Q30 every maximizing shell is Family I or II','Same61 contract; chosen maximum q30','GATE288 EXCHANGE','C7: middle degrees4..9,3,10; K4 reduction; X sizes0..3','Classify every degree and justify new-core beta12','d2 K4 repivot first proves q>=29 before new core degree12')
add('FAMILY_I','Family I cannot occur at E408,Q30','CLASS30 actual same-parent graph','CLASS30 GATE288 EXCHANGE','C8: row classes; disjoint triangle excess3(11-r), r4/5','Remainder has no K-neighbors; no overlapping excess','r5 needs70 vs5; r4 forces clique at least36')
add('FAMILY_II','Family II cannot occur at E408,Q30','CLASS30 actual same-parent graph','CLASS30 FAMILY_I GATE288 EXCHANGE','C8: decorated pair stays exceptional; ten disjoint anticomplete regular pairs','Reapply classification only at verified q30 pivots','Each pair point has exactly one K-neighbor; degree13-1-e>=12')
add('COVER','E407=>Q>=30 and E408=>Q>=31','n61,delta>=13,alpha5,omega11,caps; E407/408 implies delta13','Q29 PROM29 FAMILY_I FAMILY_II','C6-C8 complete case split','Maximum set must match pointwise upper bounds','No absent regular pivot: average<14 and min>=13')
add('DEL48','Every R(4,48) has delta>=12','Full R(4,48) contract','ORD3637 R224 CAPS','F3: degree11 rows<=3 but missing pair union>=13','No assumed degree12 gate','All d<=10 leave forbidden37 set')
add('Q20','12-shell q>=20; equality exactly five K_(2,r) families r6..10','z>=11,alpha(M)<=10,EDGE12,triangle sum>=24,g>=0','TURAN','F3:2-matching equality K2,2; all attachments on one side; weights10','No omitted decorations on initial cycle vertices','Independent286-vector replay returns all five equality families')
add('INSERT20','Q20 impossible if every leaf repivot core has delta>=12','Actual minimum-degree12 parent and Q20','Q20','F3: inserted target-adjacent hubs have at most10+1 neighbors','Do not assume row disjointness or new-core edge equality','Deleting row can only lower inserted degrees')
add('FLOOR48','Every R(4,48) has e>=310','Full R(4,48) contract','DEL48 CORE211 Q20 INSERT20','F3: degree>=13 handshake312; degree12 core211 and q>=21','35-core belongs to correct class at every leaf','No47-to48 floor substitution')
add('H12','No61-point minimum-degree12 parent with E<=408','alpha5,omega11,all D-caps','FLOOR48 DEL48 Q20 INSERT20 ORD3637 R224','F3: E>=408; equality q20 contradicted by48-core delta12','All E below408 and equality handled','Same parent retained through all leaf repivots')
add('CTX49','No induced contextual R(4,49) in original coloring','Original12-color K145 counterexample retained','CAPS ORD3637 R224 SECOND_TURAN','F2: target>=319, eleven other colors>=79 each, target<=307','No contextual-to-generic promotion','Other-color omega4 derived from target alpha4')
add('EXTRACTION','Original counterexample gives one of144 residual contracts','Least-edge color G; original coloring','CAPS BROOKS','F1: maximal K12 packing; independent transversal; exact budget','Initial shell defect and interblock ledger','d0..11,j0..11 include all degenerate cases')
add('MATCH_ALL','Recurrence matching guarantee valid for every h','Missing h-shell alpha<=10 and induced caps','MATCH3 CAPS','F4: h12,13,14 separately; h>=15 generic unmatched bound','Formula extends beyond h13','h14 cut20+6<33; generic guarantee thereafter')
add('RECURRENCE_RULES','All B(a,n) lower-bound and emptiness rules valid','Induced contextual classes; licensed seeds and order cutoffs','TURAN CTX49 R224 R223 ORD3637 FLOOR287 FLOOR48 MATCH_ALL','F4: core induction, pair/triangle split, matching and deletion averaging','Take min of channels and min over degrees','All references decrease a or n; necessary filters only exclude impossible rows')
add('RECURRENCE_REPLAY','1752 nodes agree;143 stops excluded; sole stop(11,6,5,61),397..408','Precisely the finite recurrence domain a1..12,n0..145','RECURRENCE_RULES','F4 and independent recurrence()','Matching old outputs is not proof of the rules','Independent values computed first; full arrays and144 records retained','COMPUTATIONALLY_VERIFIED')
add('H13LOW','All h13 energies<=406 impossible','Actual61 contract, delta13,E<=406','PIVOT FLOOR287 Q29','F5: E>=91+29+287=407','Q29 used only after confirming energy independence','No historical per-energy closure label used')
add('H13TOP','h13 E407 and E408 impossible','Same61 contract and corresponding E','PIVOT FLOOR287 COVER','F5: EVERY pivot has q<=E-378, contradict maximum lower bound','Quantifier order: pointwise first, maximum second','E407 upper29 vs30; E408 upper30 vs31')
add('OTHER_DEGREES','Contextual T61 E<=408 has min degree12 or13','Contextual61 residual from extraction','CTX49','F5: degree<=11 leaves49; delta>=14 costs427','No regular degree13 case cannot escape','If delta13 absent and min>=13 then min>=14')
add('T61_EMPTY','No residual with the required61 contract and E397..408','Contextual61,alpha5,omega11,caps','H12 H13LOW H13TOP OTHER_DEGREES','F5: complete disjoint minimum-degree and energy split','Exceptional cases included','All12 reachable energies covered')
add('K145','No12-edge-coloring of K145 has every13-set containing all12 colors','Original problem, no additional balancing condition','EXTRACTION RECURRENCE_REPLAY T61_EMPTY','F5: extraction forces T61; every T61 alternative impossible','No generic49 theorem required','Reconstructed acyclic DAG and matched actual hypothesis transports')

dag={r['id']:r['dependencies'] for r in items}
assert len(dag)==len(items)
assert all(d in dag for deps in dag.values() for d in deps)
for r in items:
    r['Used_by']=[key for key,deps in dag.items() if r['id'] in deps]
(HERE/'CANONICAL_PROOF_DAG.json').write_text(json.dumps(dag,indent=2)+'\n',encoding='utf-8')
(HERE/'AUDIT_OBLIGATIONS.json').write_text(json.dumps(items,indent=2)+'\n',encoding='utf-8')
lines=['# Analytic obligation matrix','',
       'Scope: independent mathematical audit at pinned integration commit c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2.',
       'R(a,n) means alpha<=a, omega<=11 and all induced D-caps. C1-C8 refer to COVER_ANALYTIC_CERTIFICATE.md;',
       'L1-L6 to LOWER_ORDER_AND_CORE_CERTIFICATE.md; F1-F5 to FRONTEND_H12_AND_GLOBAL_CERTIFICATE.md.',
       'PROVED denotes the completed informal analytic derivation. COMPUTATIONALLY_VERIFIED denotes a finite',
       'exhaustive conclusion whose mathematical domain/completeness is separately proved in the preceding',
       'mapping/rule obligation. These finite rows have no outstanding analytic completeness premise.',
       'No row is promoted merely because a source says PROVED. Published external theorems are explicit accepted inputs.',
       'No proof assistant or independent human peer-review status is claimed. Counterexample_search records the actual',
       'attack/check used; it does not assert an exhaustive search over all61-vertex graphs.','',
       '| ID | Lemma | Hypotheses | Used by | Independent derivation | Critical step | Counterexample search | Status |',
       '|---|---|---|---|---|---|---|---|---|']
for r in items:
    fields=[r['id'],r['Lemma'],r['Hypotheses'],', '.join(r['Used_by']) or 'Final theorem',
            r['Independent_derivation'],r['Critical_step'],r['Counterexample_search'],r['Status']]
    lines.append('| '+' | '.join(s.replace('|','/').replace('\n',' ') for s in fields)+' |')
(HERE/'ANALYTIC_OBLIGATION_MATRIX.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

source_rel='r12_master/workstreams/astra-global-root-integration-chat-20261031'
source=REPO/source_rel
index=[]
pin='c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2'
for file in sorted(source.rglob('*.md')):
    relative=file.relative_to(REPO).as_posix()
    raw=subprocess.check_output(['git','-C',str(REPO),'show',pin+':'+relative])
    headings=[dict(line=i,text=s) for i,s in enumerate(raw.decode('utf-8').splitlines(),1) if s.startswith('#')]
    index.append(dict(path=relative,commit=pin,sha256=hashlib.sha256(raw).hexdigest(),headings=headings))
(HERE/'SOURCE_LOCATION_INDEX.json').write_text(json.dumps(index,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(obligations=len(items),statuses={s:sum(r['Status']==s for r in items) for s in sorted({r['Status'] for r in items})},source_documents=len(index))))
