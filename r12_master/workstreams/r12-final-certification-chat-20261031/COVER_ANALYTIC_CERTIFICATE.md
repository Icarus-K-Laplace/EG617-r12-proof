# Independent COVER derivation and adversarial checks

Pinned source: c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2,
`frozen/cover/COVER_THEOREM.md`. Source labels are not premises. The lower-order
lemmas used here are rederived in LOWER_ORDER_AND_CORE_CERTIFICATE.md.

## C1. Contract, sets and the two exact exchanges

Let F have 61 vertices, minimum degree 13, alpha at most 5, omega at most 11,
and every induced D-cap. For the energy-independent part, no E bound is used.
Let p have degree 13, A=N(p), C=V(F)\N[p], M=the complement of F[A]. Define
g(a)=d_F(a)-13, t(a)=|N_F(a) intersect C|, z=e(M), q=z+sum_A g.
The actual degree decomposition is

    d_F(a)=1+(12-d_M(a))+t(a), hence t(a)=d_M(a)+g(a).

Thus e(A,C)=2z+G and E=13+(78-z)+(2z+G)+e(C)=91+q+e(C).
No clique assumption about A is used. For S subset A, put B=A\S. Expanding
t(S)=2e_M(S)+e_M(S,B)+G_S gives exactly

    q=t(S)-e_M(S)+e_M(B)+G_B.                         (C1)

An independent five-set of C would extend with p, so C is R(4,47). The cap on
N[p] gives z>=22. An independent eleven-set of M would be a target K11 in A,
and would extend with p, so alpha(M)<=10.

For a regular y in A put S=N_M(y), D=N_C(y), d=|S|=|D|. The new core is
C'=(C\D) union S. Define m=e_M(S), kappa=binom(d,2)-e_F(D),
b=e_F(S,D), rho=e_M(A\S)+G_(A\S), and h_beta=sum_D(d_C(x)-beta).
Counting edges removed and inserted, with the D-internal edges corrected once,

    e(C')=e(C)-sum_D d_C+e(D)+binom(d,2)-m+t(S)-b.

Subtract this from the two energy identities, then use C1. The result is

    q_y=d(beta+1-d)+rho+h_beta+kappa+b.              (C2)

The sum of degrees of the inserted S vertices in C' is
t(S)-b+2binom(d,2)-2m. Therefore their excess above beta is

    eta_beta=q_p-d(beta+1-d)-rho-m-b.               (C3)
    q_y-q_p=h_beta-eta_beta+kappa-m.                (C4)

These are identities even when some degree excesses are negative. Nonnegativity
is invoked only after establishing the corresponding core minimum degree. The
independent random algebra tests are supplementary, and not used to prove C2–C4.
A closed walk only equates the sums of the two sides of C4; it never makes
individual terms vanish. All equalities below instead use q_y<=Q and a lower
bound equal to Q with nonnegative error terms.

## C2. Global beta=11 interface and coverage

An embedded R(3,36) would be 13-regular, with 234 edges, by the lower-order
floor and cap. Each of the other 25 vertices sends at most 3 edges into it.
An independent triple outside would leave at least 27 vertices inside avoiding
it; R(2,24) emptiness supplies an independent triple among those. This makes
an independent six-set. Thus the outside 25-set would have alpha<=2, itself
impossible. This uses no energy assumption.

If any actual 47-core had a vertex of degree<=10, its nonneighborhood would
contain such a forbidden 36-set. Thus every actual core has delta>=11. If two
degree-11 vertices of one core were nonadjacent, the second would have degree
at most 11 in the first's 35-antineighborhood, contrary to delta(R(3,35))>=12.
The degree-11 vertices therefore form a clique.

For a missing shell edge, vertices outside the two core rows have alpha<=3;
there can be at most 35 of them. Row union is at least 12. A missing triangle
leaves alpha<=2, so its row union is at least 24. A missing K4 leaves a clique
of size<=11, so its row union is at least 36. Sums of row sizes dominate unions.
In particular a K4 gives q>=36-6=30 by C1.

Apply C3 at beta=11: eta>=0, b>=0 imply

    t(N_M(y))-2e_M(N_M(y)) >= d_M(y)(12-d_M(y)).     (INS11)

Both the old and new cores are actual cores of regular vertices of the same F.

## C3. Reduction of every q<=28 shell

First M has a 3-matching. If its maximum matching has size two, let S be its
four endpoints and I the independent remaining nine vertices. The bipartite
S–I graph has vertex cover of size<=2. A cover with one point on either side
allows at most 12 cross edges, and a cover wholly in I allows at most 8.
Even adding all six S-edges cannot reach 22. Therefore two S vertices cover
all cross edges. There are at least 16 such edges, so each cover vertex has
at least 7 I-neighbors. Two disjoint cross edges then show that the other two
S vertices cannot be adjacent. They have no I-neighbors, giving independent11.
Matching size<=1 means a star or triangle plus isolates, also impossible.

If M is triangle-free, four matching edges would give q>=48-16=32 by C1
and Mantel on their eight endpoints. Its matching number is exactly three.
A shortest odd cycle is C5 or C7. A C7 permits neither an outside edge nor
an attachment, since either extends to a four-matching. It has only 7 edges.
For C5, the outside eight-set has matching number<=1. With no outside edge,
there are at most 16 attachments and 21 total edges. With one outside edge,
only its endpoints can attach, giving at most 10 total edges. With several,
the outside graph is a star; only the common center of all its edges can
attach. At most 7 outside edges and 2 attachments give at most 14. (A triangle
outside is already forbidden.) Therefore M is bipartite.

A size-three vertex cover X exists by the alternating-path matching/cover
argument. Write Y=A\X. If X has one edge, triangle-freeness allows at most
two X-neighbors per Y point, giving at most 21 total edges. If X has two edges,
reaching 22 forces every Y point onto the two nonadjacent X vertices; Y and
the third vertex are independent11. Three X-edges form a triangle. Hence X
is independent, Y is independent, and the only edges are between X3 and Y10.

The triangular channel needs a separate exclusion. For triangle T and B=A\T,
let u=e_M(B). C1 gives u+G_B<=q-21<=7. If ab is a B-edge, K4-freeness gives
at most two T-neighbors per endpoint, and d_B(a)+d_B(b)<=u+1. Thus
t_a+t_b<=5+u+G_B<=12. EDGE12 forces every inequality to equality: q=28,
t(T)=24, both endpoints have two T-neighbors, every B-edge meets {a,b}, and
all B-decoration is on {a,b}. Applying this to each edge leaves a star or
triangle as the nontrivial part of B. A triangle would force G_B=0 and u=3,
contradicting u+G_B=7.

For one B-edge, its two distinct two-element T-neighborhoods overlap in w.
The three triangle inequalities force weights t_w=12 and the other two hub
weights equal the endpoint weights, each<=9. All other B vertices are regular,
of weight<=2, and can only meet w. Thus z<=3+1+4+8=16. For a star of size
k>=2, all decoration is on its center: center weight9, leaf weight3. A leaf's
two T-neighbors and those of the center are distinct two-subsets. Their common
hub has weight12, the other two weights are9 and3. Two distinct common hubs
of weight12 are impossible since t(T)=24 and the third weight is positive.
The missing neighborhood of each leaf consequently has weights12,9,9 and
two edges, giving INS11 left side26<27. This excludes every u>0.

For u=0, the B–T incidence number is 19 or20 and each B vertex has degree<=2.
There are at most six decoration units. Every hub meets a regular degree-two
low: otherwise a regular degree-one neighbor violates EDGE12, and for a
decorated neighbor b, the number c of that hub's B-neighbors is at most
G_B-g_b+1. Then t_h+t_b<=5+G<=11, again impossible. No B-neighbor at all
gives independent11. Thus all three hub weights are>=10, with total<=31.
Every regular degree-two low sees adjacent hubs of total weight<=21; INS11
requires at least22. Contradiction. All triangle shells are now excluded.

In the bipartite channel, three matching edges and at most nine induced edges
on their endpoints give q>=27. Hence EVERY regular pivot has q>=27.

## C4. Exhaustive finite classification and its exact completeness domain

For the proved X3,Y10 channel, encode each low by (mask,g), where mask is any
subset of X and g is a nonnegative integer. Ten rows give eight multiplicities.
Seven bars in seventeen slots give binom(17,7)=19,448 vectors. No mask, including
the empty mask, is omitted. Keep 22<=z<=q. Hall's seven inequalities are exact:
matching all three hubs is equivalent to alpha(M)<=10 by the bipartite
matching/cover theorem.

For each vector enumerate every triple of nonnegative hub decorations with sum
at most G=q-z. The remaining budget is allocated over the low rows. EDGE12 gives
the per-type lower bound max(0,max_{i in mask}(12-|mask|-t_i)). If the regular
row would violate INS11, its decoration must instead be at least one. These
are necessary filters, never realization claims. A cost-indexed construction
combines every weakly increasing decoration list in each identical mask class.
Thus every admissible decorated list appears; only permutations of identical
mask rows are removed. All regular hub INS11 conditions are then tested.

Finally take the lexicographic minimum over the six hub relabelings. This is
an exact orbit representative: two lists have the same key precisely when
one is obtained by a hub permutation and within-mask low permutations. The
surviving hubs all have missing degree at least7, while lows have degree<=3,
so distinct surviving keys cannot secretly be isomorphic by exchanging hubs
and lows. Every actual parent therefore maps to a retained key, though retained
keys need not have a parent realization.

Actual independent replay: 2 states at q27, 8 at q28, exactly equal to the
frozen records. The independent program reconstructs adjacency and decorations,
checks all 8,192 subset identities per state, alpha(M)<=10, EDGE12 and INS11
at every regular vertex. Full keys are in INDEPENDENT_REPLAY_RESULTS.json.
The mathematical classification depends on this bounded exhaustive computation;
its graph-to-state completeness and symmetry argument are the analytic part.

The states have full rows (mask7) and empty rows, except possibly one decorated
row. At q27: hub weights9,9,9 and k=8 or9 full rows. At q28: two B1 states
with weights9,9,10 and k=8 or9; six others with weights9,9,9 and exactly one
decorated low (a two-hub row, a full row, or an empty row). Zero decorations
and empty rows are explicitly included.

## C5. Geometry eliminating Q=27 and Q=28

At Q27, every active low y has d=3,rho=0. At a non-B1 Q28 maximum, every
regular full low has d=3,rho=1. C2 and maximality in either case force
h_11=kappa=b=0. Thus each such row is a triangle of degree-11 core vertices,
anticomplete to X. If rows D_y,D_z differ, choose x in D_z\D_y. The deficient
clique lemma makes x adjacent to all of D_y; it has no X-neighbors. Its degree
in the actual core after y is 11-3=8, impossible. All full regular rows coincide.
There are at least seven. The target K11 consisting of p and all lows, together
with their common triangle, has at least55+3+21=79 edges on14 points, above69.

For B1, K={p} union Y is a regular K11. Each v in K has an outside triple T_v.
For active lows C2 gives q_v=27+h_11+kappa+b<=28. If kappa=1, h_11=0 makes
all three row points deficient, contradicting their missing edge. Larger kappa
is impossible, so T_v is a triangle. For inactive lows and p this follows from
the old hub triangle directly. Every v's shell, with its SPECIFIED cover T_v,
is bipartite, and its ten lows K\{v} are regular. The classification therefore
allows only q27 or B1. Each other K point meets all or none of T_v. Since its
own outside neighborhood is exactly T_w, the triples are equal or disjoint.
The multiplicity of a triple is c=11-k in {2,3}. Eleven points require at least
four classes (integer solutions are one 2-class plus three 3-classes, or four
2-classes plus one 3-class).

At least two points x of each triple have hub weight9. Their global degrees
are c+11: the shell degree calculation is t_x=d_F(x)-c-2. At a pivot p from
a different class, d_(C_p)(x)=11-e(x,T_p)>=11. Thus these base points have
degree11 in C_p and miss every different triple. Choose base points from two
other classes. They are nonadjacent deficient vertices of C_p, contradiction.
This proves Q>=29, without any E-specific assumption or cycle inference.

## C6. Strong core interface and Q29 promotion

The independently licensed 211 floor on R(3,35) is the only AES use here.
Suppose an actual core C has e(C)<=288 and a degree-11 vertex. Its 35-core H
has e>=211, delta>=12. Its 11-shell has a missing edge uv (else a K12).
The row union has size>=12; using d_M(u)+d_M(v)<=z+1 gives shell charge>=11.
Therefore e(C)>=66+211+11=288. Equality throughout makes the rows disjoint
with union U of size12, and H\U an R(2,23) with at least131 edges.
The degree sum of U in H gives e(H[U])>=144-211+131=64. Then U+u+v has
at least64+12=76 edges, violating D(14)=69. Thus delta(C)>=12.

For a missing edge ab of the original 13-shell, a row union of size<=12 can
be extended to X of size12. C\X belongs to R(3,35), but
e(C\X)<=288-144+66=210. Hence EDGE13 is valid whenever e(C)<=288.

Now q<=29, e(C)<=288, and G<=7. If no regular vertex has missing degree3–10,
put X={t>=11}. C1 gives |X|<=2 and M is K4-free. A regular point outside X
has degree<=2 and cannot have an edge to another point outside X by EDGE13.
Thus all edges of M[A\X] have decorated endpoints.
For X empty, seven decorated vertices support at most16 K4-free edges.
For |X|=1,t=11, no regular outside point can be adjacent (its degree would
be one), and a regular hub cannot attain degree11; at most seven decorated
vertices support the edges again. For one hub of weight>=12, the other12
vertices must contain a triangle or a 2-matching, else they have independent11.
A triangle with the hub gives q>=12+24-5=31; a 2-matching gives q>=12+26-8=30.
For two hubs, their remaining eleven-set contains an edge, giving
q>=22+13-5=30. These exhaust X. Therefore a regular middle-degree y exists;
C2 at beta12 gives q_y>=d(13-d)>=30. At E407,Q29 its core has287 edges,
and at E408,Q29 it has288. Both contradict maximality. E407 COVER follows.

## C7. Complete E408,Q30 classification

At a maximum q30 pivot the core has287 edges. A regular missing degree4–9
gives q_y>=36. Degrees3 and10 give q_y>=30; maximality forces
rho=h_12=kappa=b=0 and q_y=30. The new core has287 edges, so C3 is licensed
there too and eta_12=-m>=0, forcing m=0. The two sides S,A\S are M-independent,
and the latter has no decoration.

For d=3, each inserted hub has degree t_s+2>=12, while sum_S t=30. Hence all
three weights are10. EDGE13 forces a nonisolated regular low to have degree3,
and z>=22 gives k=8,9,10. This is Family I: K_(3,k) plus isolates, hub
decoration10-k, all ten lows regular. For d=10, ten inserted weights sum30
and each is>=3 by EDGE13 against y; all equal3. Each active regular point on
the three-side must then have degree10. z>=22 forces all three active, the
k=10 instance of Family I.

Assume instead no regular missing degree3–10. A K4 would force equality in
q>=36-6: the remaining nine vertices are independent and regular; the four
weights sum36, each<=12 because the complementary triangle has weight>=24.
Since z>=22, an outside y of degree2 exists. Its two missing neighbors S are
adjacent, so rho=31-t(S). C2 at beta12 gives q_y>=53-t(S)>=29. Its actual
core has at most288 edges and thus minimum degree12. The two inserted vertices
have degrees at most their old weights, forcing both weights>=12. The other
two K4 vertices then have weight sum<=12, contradicting EDGE13. M is K4-free.

Let X={t>=11}; now |X|<=3. The complete remaining cases are:

* |X|=0: at most eight decorated vertices, K4-free edge bound21<22.
* |X|=1,t=11: no regular incident outside point; a regular hub cannot attain
  degree11. Again at most eight decorated vertices, bound21.
* |X|=1,t>=12: the other12-set has a triangle or 2-matching. The triangle
  gives31. Matching equality gives hub weight12, four endpoint weights totaling26,
  eight edges on those five points, and eight independent regular outsiders.
  Each outsider can meet only the one heavy point, so z<=8+8=16.
* |X|=3: equality forces a triangle of weights11 and regular independent lows.
  An active low has degree2. Its two neighbors have t-sum22 and m=1, giving
  rho=9 and q_y>=22+9=31.
* |X|=2: an edge uv exists on the other11 points. Equality in
  q>=22+13-5 forces both hubs of weight11, t_u+t_v=13, five edges on the
  four-set, and nine regular independent outsiders. Each active outsider
  meets both hubs. z>=22 forces all nine active. Each hub consequently has
  induced four-set degree at most2; the only K4-minus-edge configuration
  satisfying this has the absent edge between the hubs. Both hubs are regular
  of degree11, u,v have missing degree3 and positive decorations summing7.

The last alternative is exactly Family II: K_(2,11) and one additional edge
uv on the 11-side. No degree, high-weight cardinality, empty row or zero
decoration alternative has been suppressed.

## C8. Terminal contradictions without overlapping excess

Family I gives regular target K11, K={p}+ten lows. Equality at active low
repivots gives triangles T_v and charge30 for all v in K. Every such shell
is bipartite, so its classification is again Family I (Family II contains
missing triangles). The triples partition into equal-or-disjoint row classes
of multiplicity c_i in {1,2,3}, sum c_i=11. A point in such a triple has
global degree c_i+12. In a core from another class its degree is
12-e(x,T_j)>=12; distinct triples are anticomplete. There are 4<=r<=5 triples.
The row vertices are disjoint, and contribute exactly 3sum(c_i-1)=3(11-r)
to global excess 2*408-13*61=23. K contributes zero. The remainder has
50-3r vertices and excess23-3(11-r), with no K-neighbors.

If r=5, every remainder vertex must complete at least one triangle, or it and
one avoided point from each triangle form independent6. Its degree in that
triangle's pivot core is d_F(v)-3>=12. Thus each has excess>=2, requiring
70 units where only5 are available. If r=4, at least38-2=36 remainder
vertices are regular. Each meets each triangle in at most one point. Two
nonadjacent such vertices together avoid one point of each triangle, making
independent6. They must form K36, impossible. No excess is charged twice.

Family II gives regular K10 consisting of p and nine ordinary lows; each sees
the same two globally decorated, target-nonadjacent vertices u,v and an
additional pair T_i. For an ordinary low, d=2,rho=8; C2 forces q_y=30 and
h_12=kappa=b=0. Thus each T_i is an edge, and every K pivot has a q30 core
with delta>=12. Family I is already impossible, so every view is Family II.
The globally decorated u,v must remain its only decorated lows. Its hub pair
is therefore precisely T_i, with each point regular, adjacent only to v_i
inside K, and to neither u nor v. The ten pairs are disjoint. For x in T_i,
i!=j, its degree in the v_j core is 13-1-e(x,T_j)>=12. Hence pairs are
mutually anticomplete. Selecting one point from each gives independent10.

Thus Q30 is impossible at E408. Together with C5–C6, COVER yields
E407 => Q>=30 and E408 => Q>=31. The separate 287 core floor gives respectively
Q<=29 and Q<=30 at EVERY regular pivot. Both contradictions are valid.
