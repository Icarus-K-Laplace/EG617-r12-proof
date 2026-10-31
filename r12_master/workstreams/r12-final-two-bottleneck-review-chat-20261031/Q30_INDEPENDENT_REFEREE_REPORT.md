# Independent Q30 terminal referee report

Date: 2026-10-31. Verdict: **Q30 = PROVED**, in the quantified contract below.
AI-assisted informal mathematical audit; ready for accountable human review, not a formal proof-kernel certificate.

## 1. Source, scope and quantifiers

Source: integration c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2,
frozen/cover/COVER_THEOREM.md §§0–3,8,10–12, under
r12_master/workstreams/astra-global-root-integration-chat-20261031/.
Its originating COVER commit is 531e41c79e08dd2bb3892ca9ba8a491a56678565.
The certification at 09a88cc4fe1e2cf1f3a87475d6484f681910b23e was read as a map,
not used as a premise. No Q27/Q28 enumeration was rerun.

The assertion being proved is:
For EVERY simple F on 61 vertices with delta(F)=13, alpha(F)<=5,
omega(F)<=11, e(F)=408, and e(F[U])<=D(|U|) for EVERY U,
there cannot be Q=30, where Q is the maximum q_p over ALL degree-13 vertices.
D(n)=binom(n,2)-11 p12(n), p12(12a+b)=12 binom(a,2)+ab, 0<=b<12.
In the contradiction argument, EVERY maximizing pivot has a shell in I or II.
This is NOT a classification of arbitrary decorated 13-point graphs satisfying
EDGE12 alone, nor a statement about every nonmaximizing pivot with q=30.

Regular always means degree 13 in the same F. For a regular pivot p:
A=N_F(p), C=V(F)\N_F[p], |A|=13, |C|=47;
M=complement(F[A]), z=e(M);
g_a=d_F(a)-13>=0, G=sum_A g_a;
t_a=|N_F(a) intersect C|=d_M(a)+g_a; q_p=z+G.
The word "missing degree" means d_M(a), not g_a.

All licensed constraints:
E=91+q_p+e(C); z>=22 from D(14)=69; G<=8 when q_p=30;
alpha(M)<=10; each actual core is R(4,47);
all actual cores have delta>=11;
actual cores with <=288 edges have delta>=12;
EDGE12 on every M-edge; EDGE13 when e(C)<=288;
t(T)>=24 on every M-triangle and t(L)>=36 on every M-K4;
INS11 at every regular shell vertex; q_y<=Q at every regular repivot.
R(a,n) includes alpha<=a, omega<=11 and all induced D-caps.
The stronger core gate is proved below independently of E286.

## 2. Exact algebra and licensing

For S subset A, B=A\S, counting each missing edge by its endpoints gives
t(S)=2e_M(S)+e_M(S,B)+G_S, hence

q_p=t(S)-e_M(S)+rho,   rho=e_M(B)+G_B.                 (A1)

For regular y in A let d=d_M(y), S=N_M(y), D_y=N_C(y),
m=e_M(S), kappa=binom(d,2)-e_C(D_y), b=e_F(S,D_y),
h_beta=sum_{x in D_y}(d_C(x)-beta).
The new core is C_y=(C\D_y) union S. Its exact edge count is

e(C_y)=e(C)-sum_{D_y}d_C+e_C(D_y)+binom(d,2)-m+t(S)-b.

The +e_C(D_y) corrects the double removal of an internal edge. The -b removes
edges to deleted vertices, not edges in the new core. Subtracting the two
E-identities and substituting A1 gives

q_y=d(beta+1-d)+rho+h_beta+kappa+b.                    (A2)
eta_beta=sum_{s in S}(d_{C_y}(s)-beta)
        =q_p-d(beta+1-d)-rho-m-b.                    (A3)

Thus q_y-q_p=h_beta-eta_beta+kappa-m; there is no zero-cycle inference.
INS11 follows from eta_11>=0 and b>=0:
t(S)-2m>=d(12-d). The coefficient 2 is essential.

Lower-order input is reconstructed in the 286 audit's gate section:
R(2,24) empty; R(2,23) has >=131 edges;
delta(R(3,35))>=12; delta(R(3,36))>=13; R(3,37) empty.
For R(3,35), equality e=210 would give a 22-regular K4-free complement.
AES Theorem 1.1 implies it is 3-partite since 22>5*35/8; one part has >=12
vertices, violating omega<=11. Hence e>=211.
The original theorem was checked at https://real.mtak.hu/110445/1/1974-18.pdf,
p.207, forbidden clique parameter r=4. AES is a standard external theorem,
not a result claimed newly proved here.

An embedded R(3,36) in F would be 13-regular by D(36)=234. Each of the
remaining 25 vertices meets it in <=3 points by D(37)=237. An independent
triple outside would avoid at least 27 inside vertices; R(2,24) emptiness
supplies an independent triple there, contradicting alpha(F)<=5. The
outside therefore has alpha<=2, also impossible. Consequently every actual
47-core has delta>=11.

If an actual core C of <=288 edges has a degree-11 vertex x, its 35-point
antineighborhood H has delta>=12 and >=211 edges. Its 11-shell has a missing
edge ab (otherwise x extends a K11), whose H-rows cover >=12. The 11-shell
identity gives e(C)>=66+211+11=288. Equality forces e(H)=211, shell charge11,
and the two rows disjoint with union U of size12. W=H\U has alpha<=2 and
23 vertices, so e(W)>=131. Since sum_U d_H>=144,

e(H[U])=e(W)-e(H)+sum_U d_H>=64.

Then U+a+b spans >=64+12=76>D(14)=69. This excludes degree11 and proves
the <=288 gate WITHOUT the 286-edge obstruction.

For a missing shell edge ab with core <=288, a row union of size<=12 can be
enlarged to a 12-set X. The uncovered core is R(3,35), yet

e(C-X)=e(C)-sum_X d_C+e(C[X])<=288-144+66=210<211.

Thus EDGE13 holds. For Q30,E408 the chosen core has 287 edges. A new
core is allowed baseline12 only after q_y>=29 has been established, since
e(C_y)=317-q_y<=288. This ordering is retained in every step below.

## 3. Exhaustive classification, including all boundary degrees

For a regular shell vertex d lies in 0..12. At the maximizing pivot A2 with
beta12 has nonnegative rho,h,kappa,b. The values d(13-d) for d=0..12 are

0,12,22,30,36,40,42,42,40,36,30,22,12.

Therefore d=4..9 is impossible. If d=3 or10, A2 and Q=30 force q_y=30
and rho=h_12=kappa=b=0. The new core now has minimum degree12, so A3
forces m=0. In particular S and A\S are M-independent, and all points
outside S are regular.

For d=3, t(S)=30. Each inserted s has new-core degree t_s+2>=12;
therefore all three t_s=10. A regular vertex outside S has missing degree
at most3; EDGE13 implies it is either isolated or adjacent to every hub.
Thus M=K_{3,k} plus 10-k isolates, k=8,9,10 because z=3k>=22.
All lows are regular and the three hub decorations are 10-k.

For d=10, t(S)=30 and EDGE13 against y of weight10 gives t_s>=3,
so all ten weights equal3. Every active vertex in the complementary
three-set is regular and must have degree10 by EDGE13. Since z>=22,
all three are active. The ten S vertices then have degree3 and decoration0:
this is precisely Family I at k=10. Zero decoration is expressly included.

It remains to classify the channel with no regular d in 3..10.
Degrees0,1,2,11,12 have not been discarded.

First suppose an M-K4 L exists. A1 and the K4 bound force t(L)=36,
and the other nine vertices independent and regular. Every weight in L is
<=12 since the complementary triple has weight>=24. Outside degrees are
<=4, hence are 0,1,2 in this channel. Since z>=22 and L has six edges,
some outside y has d=2 (otherwise z<=15). Its S is an M-edge in L.
A1 gives rho=31-t(S), hence A2 gives q_y>=53-t(S)>=29.
The new core therefore has delta>=12. Each of its two inserted vertices
has degree t_s-e_F(s,D_y), because S is a target nonedge. Both t_s>=12.
They sum to24, leaving total weight12 on the other edge of L, contradicting
EDGE13. This proves K4-freeness without throwing away a legal K4 branch.

Let X={a:t_a>=11}. Four such points would give q>=44-6>30 by A1;
hence |X|<=3. Outside X every regular vertex has degree0,1,2; it cannot
meet another outside vertex in M because their weights sum to <=12.
Thus every edge induced outside X has two decorated endpoints.

* |X|=0: all M-edges lie on <=G<=8 decorated vertices. A K4-free graph
  on eight vertices has <=floor(64/3)=21 edges, below22.
* |X|=1, t_x=11: outside regular vertices cannot meet x either (degree
  at most1 would give weight sum12). If x is regular it cannot have
  11 neighbors among at most8 decorated points. If decorated, at most
  eight decorated points including x support all edges, again <=21.
* |X|=1, t_x>=12: the other 12-set contains either a triangle or a
  2-matching. Indeed a graph of matching number<=1 is a star or a triangle
  plus isolates; a star on12 has an independent11-set. With a triangle,
  K4-freeness and A1 give q>=12+24-5=31. With a 2-matching, EDGE13
  and the five-point K4-free bound8 give q>=12+26-8=30. Equality forces
  t_x=12, eight edges on those five vertices, and the remaining eight
  vertices independent and regular. Those eight can only meet x,
  so z<=8+8=16, impossible.
* |X|=3: A1 forces weight11 at all three hubs, an M-triangle, and
  ten independent regular outsiders. An active outsider has degree2
  (degree1 fails EDGE13; degree3 is excluded in this channel). For it
  t(S)=22,m=1,rho=30-22+1=9, hence q_y>=22+9=31. There is an active
  outsider since z>=22.
* |X|=2: its complementary 11-set contains an edge uv by alpha(M)<=10.
  For W=X+{u,v}, A1, EDGE13 and K4-freeness give
  30=q>=22+13-5=30. All equalities hold: the hubs weigh11, t_u+t_v=13,
  e_M(W)=5, and the other nine vertices are independent and regular.
  An active outsider must meet both hubs, so z=5+2k>=22 with k<=9
  implies k=9 and z=23. Each hub has at least nine outside neighbors;
  its degree in the K4-minus-edge W must therefore be2, not3.
  Thus the unique missing edge of W is the hub-hub pair. Both hubs
  are regular, degree11; u,v each have M-degree3 and
  g_u+g_v=7. Neither g is zero, since regular degree3 was excluded.

The only remaining structure is Family II: K_{2,11} plus edge uv on the
11-side; two regular hubs of weight11, nine regular lows of weight2,
and exceptional decorations (g_u,g_v)=(1,6),(2,5),(3,4),(4,3),(5,2),(6,1).
There are no omitted weight sets, degree cases, isolated vertices or zero
decoration boundaries. This is an analytic partition, not a numerical
inference from a list of observed shells.

## 4. Family I: exact global incidence and excess

Put K={p}+the ten lows, a regular target K11. For v in K let T_v be its
three neighbors outside K. At p and its inactive twins q_v=30.
At an active low d=3, the equality argument above gives q_v=30,
T_v a triangle, and a core of minimum degree12.

In every such view the missing graph is bipartite between the target
cliques K\{v} and T_v, so it cannot be Family II, which has M-triangles.
The classification forces Family I in every view. Every w in K is
adjacent to all or none of T_v. If T_v and T_w intersect, w is adjacent
to a member of T_v, hence to all of T_v, so T_w=T_v. Distinct triples
are therefore disjoint. Their multiplicities c_i=11-k_i lie in {1,2,3}
and sum to11.

For x in triple T_i, its hub weight in that view is10 and its missing
degree is 11-c_i. Thus g_x=c_i-1 and d_F(x)=c_i+12.
Its K-neighbors are exactly the c_i vertices of that row class.
In a core at a different class j its degree is
d_F(x)-c_i-e_F(x,T_j)=12-e_F(x,T_j)>=12.
Consequently all distinct triples are anticomplete. If their number is r,
then 4<=r<=5, using c_i<=3 and alpha(F)<=5.

Here is the COMPLETE vertex budget, with disjoint rows:

|Vertex class|Number|Degree excess above13|Contribution|
|---|---:|---:|---:|
|K|11|0|0|
|T_i|3 for each i|c_i-1|3 sum_i(c_i-1)=33-3r|
|R=V(F)\(K union all T_i)|50-3r|nonnegative|23-(33-3r)=3r-10|

The total23 is 2*408-13*61, not the core excess8.
Every edge between two classes appears once at each endpoint in this
handshake budget, which is required, not double charging a vertex.
Every K-incident edge is exhausted by K and the T_i. Hence R has no
K-neighbors. No unidentified excess remains outside this table.

If r=5, |R|=35 and its budget is5. Each w in R must complete one triple:
otherwise choose one nonneighbor in each of five anticomplete triples
to form an independent six-set with w. In that triple's core,
d_F(w)-e_F(w,T_i)>=12, so completing it requires d_F(w)>=15.
Each of35 distinct vertices costs >=2, requiring70>5.

If r=4, |R|=38 and its budget is2. At least36 vertices are regular.
Each regular w in R meets each triple in at most one point, by the
same core inequality. Two nonadjacent regular remainder vertices together
avoid a point of every triple, yielding independent6. Therefore those
>=36 regular vertices are a clique, contradicting omega<=11.
This excludes all multiplicities and all overlaps.

## 5. Family II: attempted extension and forced obstruction

Start from each of the six positive decoration allocations listed above;
each gives a locally legal candidate shell for the necessary shell tests.
These shells are NOT full counterexamples. Attempt to extend one to F.

Let K={p}+the nine ordinary lows. It is a regular target K10, complete
to both exceptional vertices u,v; uv is a target nonedge.
Each k_i in K has precisely two further neighbors T_i.
For an ordinary low y, d=2, S=the two original hubs, m=0,t(S)=22,
rho=30-22=8. A2 gives q_y=30+h_12+kappa+b, so equality forces
q_y=30 and its pair T_y to be an edge. This licenses delta(C_y)>=12.

Every K-view is subject to the complete Q30 classification. Family I
has just been excluded. Thus it is Family II. Since u and v have
strictly positive global decoration, they must be exactly its two
exceptional vertices. The other nine K-points, adjacent to both,
are ordinary lows; T_i is its regular hub pair.

In particular x in T_i has global degree13, exactly one K-neighbor k_i,
and no neighbor among {u,v}. It cannot belong to T_j for j!=i, since
that would give a second K-neighbor. Thus all ten pairs are disjoint.
For x in T_i and j!=i, x belongs to C_{k_j}, and

d_{C_{k_j}}(x)=13-1-e_F(x,T_j)>=12.

Hence the pairs are pairwise anticomplete. One vertex from any six pairs
already violates alpha(F)<=5 (all ten give independent10). This is an
explicit failed-extension certificate applying to every decoration split.
D-caps entered through the degree gates and EDGE13; they are not silently
required of an augmented graph. No search failure is used as nonexistence.

## 6. Result and limits

Q30 = PROVED: under the exact E408 hereditary parent contract, Q=30
forces one of two exhaustively derived families and both are impossible.
This terminal proof does not need the E286 theorem, Q27/Q28 enumeration,
or the E407/E408 conclusion as a premise. Standard Turan/Mantel and AES
are explicit external mathematical inputs. The support and arithmetic
checks elsewhere in this package are supplementary, not a formalization
of the graph-to-family reduction. Human specialist review should focus
on the core gate and the classification-to-row transport in §§3–5.
