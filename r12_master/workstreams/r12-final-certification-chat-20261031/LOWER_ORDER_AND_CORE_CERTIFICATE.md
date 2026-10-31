# Independent lower-order, low-edge and 286-edge audit

All R(a,n) statements in this document include alpha<=a, omega<=11 and EVERY
induced D-cap. The two abstract 47-point nonexistence theorems explicitly do
not require caps. This distinction is essential to safe augmentation.

## L1. R(2,24), the 23-point classification, and the 12-set construction

For R(2,24), the nonneighbors of a vertex form a clique of size<=11, so
delta>=12. D(24)=144 forces 12-regularity. Its complement is triangle-free,
11-regular and not bipartite (otherwise two target cliques of size<=11 cover24).
A shortest odd cycle of length2k+1 is chordless. An outside vertex has at most
k neighbors on it because consecutive neighbors would form a triangle.
Summing degrees on the cycle gives 11(2k+1)<=2(2k+1)+k(23-2k), equivalent
to 2k^2-5k+9<=0. The discriminant is negative; contradiction.

More generally the shortest-odd-cycle count plus Mantel outside gives

    B(n,k)=2k+1+k(n-2k-1)+floor((n-2k-1)^2/4).

The maxima for n=18,23,25 are73,122,145, respectively. At23, k>=3 gives<=119.
Thus a triangle-free W on23 points with alpha<=11 and e>=121 has a shortest
C5 and an18-point exterior with at least80 edges. The exterior is bipartite
(its nonbipartite bound is73). Products of two part sizes summing18 leave only
K9,9, K8,10, or K9,9 minus one edge.

An exterior vertex's two cycle neighbors form one of five independent pairs
T_i={i-1,i+1}. Adjacent exterior vertices must have disjoint pairs; the
compatibility graph of these types is C5 itself. For complete bipartite
exterior, one side has a single type and the other at most two compatible types:
two distinct types have at most one common compatible type, three have none.
The20 ordered type-set pairs are independently enumerated in our replay.

At122 edges all inequalities are equalities, giving C5 blowups
(10,a,1,1,11-a), 1<=a<=10. At121 with exterior K9,9 there is one singleton
cycle row. It extends to a compatible two-row, whether the opposite side uses
one or two types, so the graph is a one-edge deletion of a122 graph. At121
with exterior K8,10, all cycle rows have size2; the blowup has an independent
class pair of size at least12 and is excluded. For K9,9 minus uv, remove u,v
and classify the remaining K8,8. Compatible endpoint types allow adding uv.
For incompatible endpoint types both remaining type sets must be singletons;
their endpoint possibilities give, up to the dihedral C5 symmetry,
(9,9,2,1,2). The independent enumeration finds all10 oriented exceptional cases.
This proves completeness, rather than only checking proposed examples.

For W=(P,A,s,t,B) with sizes(10,a,1,1,11-a), use the12-sets P+s+t, A+B+s,
A+B+t. Every independent set is contained in one of P+s, P+t, A+B, A+t, B+s.
The costs e(W[T])+|I intersect T| are bounded respectively by
min(a+1,11-a), min(a,12-a), 1, 2, 2; the first two are<=6.
After deleting one edge, an independent set newly created by that deletion
contains its endpoints and can otherwise use only the unique class nonadjacent
to both. For the four nonsingleton edge types, P+s+t has cost<=3,2,2,3.
Deleting st creates independent12 and is forbidden. Other deletions creating
independent12 are also discarded explicitly. For the special blowup(9,9,2,1,2),
the two12-sets P+C+d and Q+d+E have two internal edges, and one intersects
any independent set in at most two points. Thus cost<=4.

The independent implementation constructs all61 representatives (ten blowups,
their five deletion types each, and the special graph), enumerates maximal
independent sets by include/exclude recursion on the original graph, and checks
the indicated sets. It obtains49 admissible representatives,12 excluded by
alpha>=12,263 maximal independent sets and maximum cost6. Every independent
set extends to a maximal one and the cost is monotone in I, so this verifies
the universal finite test. The analytic class and edge symmetries justify the
representative selection. No original verifier function is imported.

Also R(2,23) has at least253-122=131 edges: its complement is nonbipartite,
triangle-free and thus subject to B(23,k).

## L2. Minimum degrees and the 211 lower bound

For J in R(3,35), R(2,24) forbids degrees<=10. If d(v)=11, its complement's
neighborhood W has23 vertices, is triangle-free, has alpha<=11 and at least
253-D(23)=121 edges. Let R be the other11 vertices. There is a complement
edge xy in R, since otherwise R+v is a target K12. The common W-neighbors I
of x,y in the complement form an independent set there (an edge would give
a complement K4). Choose a12-set T of cost<=6 by L1. Every point of T\I
has a target edge to x or y. Consequently the actual14-set T+x+y spans at
least66-e(W[T])+12-|T intersect I|>=72>D(14)=69. This argument does NOT
assume absence of target cross edges; it explicitly lower-bounds them.

For R(3,36), degrees<=11 violate R(2,24); degree12 becomes degree11 on35
vertices after deleting one neighbor. Thus delta>=13, e>=234. For R(3,37),
degrees<=12 are impossible by R(2,24), and handshake gives241>D(37)=237.

For R(3,35), e>=210 by delta>=12. Equality makes the complement22-regular
and K4-free. The original AES theorem, with forbidden clique order4, gives
3-partiteness when delta>5n/8. Here 8*22=176>175. A part has at least12
vertices, producing target K12. Hence e>=211. No equality version of AES or
unstated connectedness premise is used.

For J in R(4,47), minimum d<=9 leaves forbidden R(3,37). If d=10, its36-core
has at least234 edges; the ten shell degrees give 2e(S)+e(S,C)>=90, so
e(J)>=234+10+90-e(S)>=289. If d=11, the35-core has at least210 edges,
the11-shell has a missing edge, and its two rows cover>=12. Since their
missing degrees sum<=z+1, q>=11 and e(J)>=66+210+11=287. Therefore
e(J)<=286 implies delta(J)>=12. This gate is only used in its licensed edge range.

## L3. Common neighborhoods and safe augmentation

For a47-point graph with delta>=12 put epsilon=d-12 and T=2e-564. At e<=285,
0<=T<=6; at e=286, T=8. Any25-set W has e(W)<=150+T/2, hence at most153
or154. If alpha(W)<=2, its complement is triangle-free and nonbipartite;
two target cliques of size<=11 cannot cover25, even though cross edges may
exist. The B(25,k) bound145 gives e(W)>=155, contradiction.

For a nonedge uv the common antineighborhood has size
21+c(u,v)-epsilon(u)-epsilon(v) and alpha<=2. Therefore

    c(u,v)<=3+epsilon(u)+epsilon(v).                 (L3)

At T<=6 this is<=9, so two vertices cannot both complete the same K10:
if adjacent they form K12, if nonadjacent L3 fails. At T=8, the valid conclusion
is instead that two K10 completers spend at least7 combined excess; for K9
it is6. Importing the stronger T6 uniqueness bound into T8 would be invalid,
and the equality proof does not do so.

At e<285, any added nonedge cannot create K12 because its endpoints have fewer
than10 common neighbors. It preserves order, minimum degree and alpha<=4.
Its new edge count is still<=285. Repeat at most three times from e>=282,
reapplying L3 each time to the new graph. D-caps or original color decompositions
need not survive and are not premises of the exact285 theorem. That original
theorem was actually read at f56cc9eba646e71d63c4b55f468a2340bcdd64c2,
path `r12_master/workstreams/astra-q32-v47-universal-attack-chat-20261030/UNIVERSAL_Q32_THEOREM.md`.
Its U1–U6 argument is the T6 specialization of the direct derivation below,
so augmentation has a separately verified terminal theorem and no circularity.

## L4. Independent four-set, all support orbits, and correct excess allocation

At T<=8, at most q<=8 vertices are exceptional. If the other47-q vertices
have alpha<=3, Turan and the exceptional-degree sum give
e>=p3(47-q)+12q+T-binom(q,2). For T<=6 the weaker bounds at q=0..6 have
minimum317>285. For T=8, q=1..8 has minimum310>286. Thus an independent
four-set of degree12 vertices exists. The q=0 case is included at T=0.

Their48 incidences cover43 outside vertices. With Z the multiply covered
vertices, private classes together with their seeds are cliques K_i. If h=|Z|
and d_i counts its incidences at seed i, then |K_i|=13-d_i<=11,
sum d_i=h+5, and3<=h<=5. Every support is a subset of the four seeds of
size>=2, and the sum of support sizes minus1 is5. Our independent multiset
enumeration considers all such supports, including repeats, imposes d_i>=2,
and quotients by all24 seed permutations. It gives raw counts9,40,48 and
orbit counts2,3,5. The h5 degree sequences are4222 and3322. Thus all ten
orbits of the equality proof, including B and C, are accounted for. These
are47-point support orbits; they are not an h12 shell classification.

For a point z supported on exactly two seeds i,j, let A=K_i\N(z), B=K_j\N(z).
If both are nonempty, every A–B pair is an edge, else the pair, z and the two
other seeds are independent5. For clique sizes(s,t), the disjoint sets
{z},A,B give the valid excess lower bound

    max(0,s+t-a-b-12)+a*max(0,s-1+b-12)
                         +b*max(0,t-1+a-12).       (L4)

For11/11,10/11,9/11,10/10 the minima are6,4,2,2 at respectively(2,2),(2,3),
(2,4),(3,3). The last three minima put all excess on z. The minima follow
by splitting at each positive-part threshold; our full finite-domain check
also verifies their unique minimizers. Completing a K10 or K9 is not excluded
by setting a>0: zero missing sets are dealt with separately in each case.

For DISTINCT incident support edges, the forced opposite sets lie in different
cliques. At v in K_i, start with |K_i|-1+d_i=12 internal-plus-support neighbors.
Missing an incident support point replaces its one adjacency by a_opposite
forced adjacencies. Thus epsilon(v)>=max(0,sum(a_opposite-1)). For a K10 in
the diamond there is at most one negative summand (only the other K10 can
be completed). Every positive right-hand term max(0,a-2) has one spare unit
to absorb that possible -1. For K11 there are only two incidences, and

    max(0,a+b-2)>=max(0,a-2)+max(0,b-2), a,b>=0.

The same inequality holds on any subset of missing incidences. These are
POINTWISE bounds before summation, so shared leaf vertices' excess is counted
once. They do not license additive blockers for repeated support pairs;
the repeated-pair arguments below use disjoint sets or explicit unions instead.

## L5. Direct exclusion throughout T<=6

A11/11 pair forces the L4 minimum6, missing sizes2,2, all excess on its
support point and no uncounted neighbors of that point.
For h3, supports are {0123,01,23} or {01,023,123}. The first has two distinct
points each requiring all6 units. In the second, a missing vertex in one
clique has exactly10 internal plus2 forced neighbors and is regular. Replace
that seed by it; the old other two K11s remain private full cliques, since
they cannot enlarge. One triple becomes a11/11 pair with zero excess, impossible.

For h4, if there is a11/11 pair, each remaining pair point is regular and
must complete the unique K10: positive missing sets would give own degree
at least21-2-3=16 using zero-excess endpoint capacities. Two completers are
forbidden by L3. Otherwise supports are the three distinct star pairs and
their complementary triple. The simultaneous center charge is a(b-1), giving
max(0,9-a-b)+a(b-1)+b max(0,a-2)>=6 for a,b>=1. At most one pair can
miss the K10, so at least two complete it, again impossible.

For h5,4222 there is a11/11 pair using all excess; each other point must
complete K9 (otherwise degree>=20-2-4=14). Those four regular completers
are pairwise adjacent by L3 and give K13. For3322 a11/11 pair would force
four regular points to complete a K10, exceeding the two available completion
slots. With no11/11 pair, exactly one10/10 pair remains and the four mixed
pairs have2-by-2 multiplicity matrix with margins2. It is either P (two
doubled pairs) or D (all four distinct).

In P choose a noncompleter from each doubled pair. They occupy disjoint
clique pairs and distinct points, costing4+4=8. In D at least two mixed
points are noncompleters. The pointwise inequality L4 gives each cost>=5,
additively even when sharing a leaf. Thus T>=10. These contradictions prove
the abstract low-edge theorem without augmentation or an exact-edge black box.

## L6. Independent audit of all T=8 equality orbits

The concentration estimate for a11/11 pair is useful: after orienting a<=b,
L4<=8 implies a<=2, and z together with its small-side clique alone costs
max(0,10-a-b)+a max(0,b-2)>=6. If a=2 then b<=4. This concentrated bound
also holds for a=2,b=1. It is not a repeated charge of both cliques.

A triple on three K11s costs at least3 on that point and those cliques. For
if that local budget were<=2, its sorted missing sizes a<=b<=c would sum>=19,
so b>=5 and b+c>=13. Each clique point has at most4 outside neighbors.
Choose x in the smallest missing set. The other two sets, after its neighbors
are removed, are nonempty and have combined size>=9. They must be complete
to each other to avoid independent5 with x, the triple point and the fourth
seed. One side has size>=5, forcing an endpoint's outside degree>=5, impossible.

The ten orbits are now audited separately:

|h and support multiset|Independent elimination and where charge is disjoint|
|---|---|
|3: 0123,01,23|Two disjoint11/11 pairs cost12.|
|3: 01,023,123|Orient the01 small side; its point+one clique costs6. Choose the triple on the other three cliques: disjoint local cost3. Total9.|
|4: 01,01,023,23|Pair23 costs6. A noncompleting01 costs4 on disjoint cliques; if neither, two K0 completers cost7 on distinct points.|
|4: 01,012,03,23|The01 point must complete K0, by disjoint4+6. If03 also completes it, cost7+6. Otherwise its K0 missing vertices have the extra01 neighbor; cost5 combines with23's6 by the pointwise shared-leaf inequality.|
|4: 01,02,03,123|The star's simultaneous center bound costs6 for each positive missing set. One noncompleter leaves two completers costing7 on disjoint points; none leaves three completers whose pairwise excess sums>=7 imply total>=11.|
|5,4222: 01,01,02,03,23|Pair23 costs6, leaving local budget2 on doubled01 and K0,K1. The small-budget argument below forces both01 points to complete K9. A noncompleting02 or03 then costs5 in addition to6 by shared-leaf accounting. All four completing points are pairwise adjacent since their remaining total excess<=2<6, giving K13.|
|5,P: 01,02,02,13,13|Each doubled pair has a noncompleter; otherwise7 on one pair plus at least4 on the other exceeds8. Chosen disjoint blockers cost4+4 exactly. Their companions have zero excess and must complete the K10s, giving missing vertices degree9+3+1=13, contradiction.|
|5,D: 01,02,03,12,13|If a K10 has two completing mixed points, they cost7; the other K10 costs at least5 or7, disjoint from those points via pointwise counting. Otherwise at least two mixed noncompleters cost5 each.|
|5,B: 01,01,02,13,23|Pair23 costs6. Doubled10/10 pair01 has local budget2 and completes opposite K10s. A noncompleting02 has extra completion neighbor and costs5 additively with23; otherwise two K0 completers cost7 disjoint from23.|
|5,C: 01,01,01,23,23|Two points on the same11/11 pair are impossible by the intersection argument below.|

Small-budget doubled9/11 or10/10 pair: if one point misses both cliques,
L4 reaches its unique minimum2 and all local excess is on that point. Its
regular companion must complete at least one clique. A missing vertex of the
first point in that clique now has degree8+4+1 or9+3+1, both13, contrary to
zero excess. Thus both complete a clique. For9/11 this can only be K9; for
10/10 they complete opposite cliques, since two on the same K10 cost7.

For two11/11 points z,z', choose each a small missing side of size<=2.
If necessarily opposite, concentration gives disjoint6+6. Otherwise orient
both small sides in X, and a<=a'. If both are2, z+X costs6 and z' costs>=4.
If (a,a')=(1,2) with disjoint sets, the first missing vertex sees z' and B,
so it and z cost>=8; z' costs>=4. If the singleton is contained in the double,
its shared vertex and z cost>=7, while the other vertex and z' cost>=7,
on four distinct vertices. With two distinct singleton sets, each vertex+point
pair costs>=8. With the same singleton x, z,z' cannot be adjacent (ten shared
X-neighbors would form K12). Put B0=|B union B'|. They have at least21-B0
common neighbors, so L3 forces epsilon(z)+epsilon(z')>=18-B0. Meanwhile
epsilon(x)>=max(0,B0-2), totaling at least16. This explicitly handles every
intersection and never sums overlapping full excess budgets.

All ten orbits fail at T=8. Combining the abstract286 exclusion with the
minimum-degree gate and abstract low-edge theorem gives e(J)>=287 for EVERY
J in R(4,47). No claim that arbitrary47-point graphs have minimum degree12
was used, and no generic49-point theorem has been smuggled in.
