# Independent frontend, h12 and global closure

This audit keeps the original coloring whenever a contextual statement is used.
All source locations refer to the integration commit c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2.

## F1. Original problem and extraction

Assume every13-set of a12-edge-coloring of K145 contains all12 colors. Each
color graph has alpha<=12, and hence on every n-set at least p12(n) edges
by Turan on its complement. Subtracting the other eleven colors gives every
target induced subgraph the cap D(n)=binom(n,2)-11p12(n). A monochromatic
K13 would violate the original property, so the initial target omega<=12.

Choose a least-edge color G: e(G)<=10440/12=870. If delta(G)>=12, handshake
forces G to be12-regular. Brooks applies with maximum degree12>2 and no K13
component, including when G is disconnected. A12-coloring of its vertices
gives an independent class of sizeceil(145/12)=13. Thus a minimum-degree
vertex v has d in0..11.

Set A=N(v), U=V(G)\N[v]. Pack a maximal collection of j disjoint K12s in U.
D(13)=67 and the66 internal edges of a K12 allow any outside vertex at most
one target neighbor in it. In particular, interblock edges form matchings.
Twelve blocks would admit greedy independent representatives (the kth block
loses at most k-1 of its12 vertices); together with v they give independent13.
So j<=11. The remainder R has n=144-d-12j, omega<=11 by maximality.
If R had an independent set of size12-j, each block retains at least j vertices
avoiding it. Greedy representatives from j blocks again extend with v to13.
Therefore alpha(R)<=11-j, including j=0 and j=11 (the latter forces R empty).

Let sigma=870-e(G), z=binom(d,2)-e(A), g=sum_A(d_G(a)-d), x the total
interblock edges, and y the block-to-remainder edges. All are nonnegative.
The minimum-pivot identity and the disjoint block edge partition give

    e(R)=870-binom(d+1,2)-66j-(sigma+z+g+x+y).

Edges from A to blocks or R are already in the shell identity; they are not
subtracted again in x or y. This checks the potentially dangerous overlap.
All144 possible(d,j) pairs are included, even nonrealizable ones.

## F2. Contextual49 exclusion and external theorem domains

If an induced target F on49 vertices has alpha<=4, omega<=11 and all caps,
degree<=11 leaves a forbidden R(3,37). At degree12 its36-core H has exactly
234 edges. The12-shell has a missing pair. Its rows into H cover at least13,
else an uncovered24-set belongs to R(2,24). Thus H plus that pair has at least
247 edges, violating D(38)=241. Hence delta(F)>=13 and e(F)>=319.

For any OTHER color C on the same49-set, alpha(C)<=12 and omega(C)<=4.
The latter holds because a monochromatic5-clique in C would be independent
in F. The complement of C is K13-free but not12-partite: twelve independent
parts would be twelve C-cliques of size<=4, covering at most48 vertices.
Kang–Pikhurko Theorem1, n=49,r=12, therefore gives
e(C)>=p12(49)+floor(49/12)-1=76+3=79. Its hypotheses n>=r+3 and
2<=r<=(n-1)/2 both hold. Eleven such colors leave e(F)<=1176-869=307,
contradicting319. The source theorem is about non-r-partite K_(r+1)-free
graphs; no equality characterization or stronger chromatic assertion is used.

This proves contextual49 emptiness only. The same upper bound cannot be
asserted for an arbitrary uncolored R(4,49), because the other eleven colors
are not then provided. That generic problem remains outside this certificate.

External statements actually retrieved on2026-10-31:

* [Brooks original paper, reprint Appendix A, p537](https://www.tu-ilmenau.de/fileadmin/Bereiche/MN/komgra/BackMatterSMM.pdf): maximum degree at most n>2 and no K_(n+1) component imply n-colorability. Specialization n=12 above. [Publisher DOI record](https://doi.org/10.1017/S030500410002168X).
* [Kang–Pikhurko2005, Theorem1, p13](https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf): in the applicable range, the maximum is t_r(n)-floor(n/r)+1. Specializations49,12 and optionally25,2. The latter has an elementary replacement in this audit.
* [Andrasfai–Erdos–Sos1974, Theorem1.1, p207](https://real.mtak.hu/110445/1/1974-18.pdf): no K_r and minimum degree greater than n(3r-7)/(3r-4) imply chromatic number below r. At r=4,n=35 this is the strict threshold175/8<22. Turan is also stated in the original paper and in the Kang–Pikhurko introduction.

The published external theorems are accepted mathematical inputs, with their
statements and applicability checked; their complete historical proofs are
not re-proved by the present program. No source claim about this project's
unpublished proof was supplied to a public search service.

## F3. Independent q20 classification and h12 closure

For J in R(4,48), degree<=10 leaves R(3,37). At degree11, its36-core has
234 edges. Every shell row has size<=3 by D(37)=237. A missing shell pair
exists (else K12) and would have to cover>=13 core vertices. This is impossible
with two rows of size<=3. Hence delta(J)>=12 without an edge-count assumption.

Consider a minimum-degree12 parent with12-shell missing graph M and q=z+G.
Assume z>=11, alpha(M)<=10, EDGE12 and triangle row sum>=24. A triangle
gives q>=21. Otherwise M is triangle-free and has a2-matching: matching
number<=1 would give a star with independent11 or a triangle with only3 edges.
The four endpoints S give q>=24-4=20. At equality M[S]=K2,2, t(S)=24,
and the other eight vertices are independent and undecorated. A3-matching
would give q>=36-9=27. Each outside point meets at most one side of K2,2.
Attachments on both sides, together with the edge joining the two unused
cycle vertices, would make a3-matching. Hence there is a two-hub cover X and
ten lows. Equality along the four cycle edges makes the two hub weights a
and the opposite weights12-a. The opposite vertices have missing degree2,
so a<=10. Since z>=11, some outside attachment exists; its regular endpoint
has degree<=2, and EDGE12 forces a=10 and degree2. All active lows therefore
meet both hubs, all low decorations vanish, and

    M=K_(2,r)+isolates, r=6..10, hub weights10, hub decorations10-r.

These are exactly five families. The independent two-hub replay considers
all286 row multiplicity vectors and all decoration budgets, with no positive
decoration or nonempty-row assumption, and returns exactly these five states.
The 2/3/5 support-orbit counts in the47-point proofs are a different enumeration;
they are not being misused to certify this12-shell lemma.

At a leaf repivot the two hubs are inserted into the new core. They are target
adjacent, and each has10 old-core neighbors. Even before subtracting neighbors
lost in the deleted two-point row, its new-core degree is at most11. Thus
q20 is impossible whenever every such new core has minimum degree12.

For R(4,48), if minimum degree>=13 then e>=312. Otherwise a degree12 pivot
has a35-core with delta>=12 and e>=211. Its shell has z>=78-D(13)=11,
EDGE12 from R(2,24), and triangle coverage24 from omega<=11. Each regular
leaf repivot has another R(3,35) core, so q20 is excluded. Consequently
e>=78+21+211=310.

For a T61 parent of minimum degree12 and E<=408, a minimum pivot has a48-core
in R(4,48), hence e>=310 and delta>=12. Missing pairs cover>=12 since the
uncovered core cannot contain R(3,37); missing triangles cover>=25 by R(2,24).
Thus q>=20 and E>=78+20+310=408. Equality would force q20. Every leaf has
global degree12 and its new48-core again has minimum degree12, contradicting
the inserted-hub degree<=11. This handles ALL h12 energies<=408, not just
an exceptional selected pivot.

## F4. Every recurrence rule and all integer comparisons

Bounds B(a,n) are for induced subgraphs of the fixed hypothetical color G,
with alpha<=a and omega<=11. Initial maximum orders11,23,36,48 for a=1..4
come from clique cap, L1, L2 and F2. Seeds131,210,234,284,308 at
(2,23),(3,35),(3,36),(4,47),(4,48) follow respectively from the already
proved stronger floors131,211,234,287,310. None requires T61 emptiness.

At minimum degree h and core order m=n-h-1, the same shell identity gives
e=binom(h+1,2)+q+e(C). The shell's alpha(M)<=10 and two caps give
z>=max(p10(h),binom(h,2)-D(h),binom(h+1,2)-D(h+1)). For h>=11 a missing
edge exists. Its row union is at least beta=max(0,m-N_(a-2)), giving q>=beta-1
and the necessary density condition B(a-1,m)+beta<=D(m+2).

Unmatched vertices of a maximum matching are independent; hence matching
size>=ceil((h-10)/2). The extra guarantees2 at h12 and3 at h13 are the
elementary shell matching arguments already independently derived. At h14,
matching size<=2 leaves an independent10-set; its bipartite cut to the four
matched endpoints has a cover of size<=2 and at most20 edges, so z<=26,
whereas the closed-shell cap gives z>=33. For h>=15 the generic bound already
gives3. This proves the formula for ALL h, not only those appearing at T61.

For t matched edges, their endpoints have weight sum>=t*beta. Target
alpha<=a gives e_M(S)<=binom(2t,2)-p_a(2t), so C1 gives
q>=t*beta-binom(2t,2)+p_a(2t). If M is triangle-free, Mantel improves this
to t*beta-t^2. If M has a triangle, its rows cover
gamma=max(0,m-N_(a-3)), giving q>=gamma-3; this channel is impossible when
B(a-1,m)+gamma>D(m+3). At a=2 a missing triangle is directly impossible.
Take the MINIMUM of the viable channel lower bounds. No necessary condition
is treated as sufficient: extra hypothetical rows only weaken the lower bound.

For each viable h the edge floor is the maximum of handshake ceil(nh/2) and
the shell identity floor. Minimize over h, then maximize with Turan, the
licensed seed and deletion averaging ceil(n*B(a,n-1)/(n-2)) for n>2.
Each edge appears in n-2 one-vertex deletions, proving that last inequality.
No viable row or a floor above D(n) means empty; emptiness propagates upward
by induced subsets. All dependencies decrease a or decrease n at fixed a.

Our separate implementation computes all1752 entries before consulting any
reference value. The two frozen source programs are then executed in separate
processes solely as comparators; neither is imported into our computation.
All1752 entries agree with both and with the retained JSON. All144 outer
stops are retained in the new result. Exactly143 fail and one survives:

    d=11, j=6, a=5, n=61, lower bound397, budget408.

## F5. Complete contradiction, quantifiers and dependency ordering

For this contextual T61, degree<=11 leaves a contextual49 subset of the
nonneighborhood, forbidden by F2. Minimum degree>=14 gives at least427
edges. Thus minimum degree is12 or13. F3 excludes12. At13 a regular vertex
exists, and every regular-pivot47-core is R(4,47), with e>=287 by L1–L6.
At each such pivot E=91+q_p+e(C_p); only after establishing this pointwise
bound do we maximize over the same fixed nonempty regular set.

The energy-independent COVER argument gives Q>=29, so E>=407. This closes
every h13 energy397..406 at once. At E407, the pointwise floor gives Q<=29
but COVER gives Q>=30. At E408 it gives Q<=30 but COVER gives Q>=31.
No T61 remains, contradicting the exhaustive extraction. Thus the assumed
K145 coloring does not exist.

The canonical DAG separates CORE211 (lower-order+AES) from the rest of COVER,
and the elementary shell matching lemma from the terminal COVER theorem.
This prevents a file-level apparent cycle: the recurrence's47/48 seeds are
proved before recurrence, and their proofs do not use extraction or T61
nonexistence. The contextual49 theorem uses only the original coloring,
lower-order lemmas and second Turan, never the high-energy backend. Generic
R(4,49) layers333..340 remain OPEN outside the proof's dependency path.
