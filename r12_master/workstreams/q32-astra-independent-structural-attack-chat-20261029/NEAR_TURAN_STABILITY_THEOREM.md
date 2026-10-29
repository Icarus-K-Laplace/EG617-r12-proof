# Outside-edge stability and blocker rigidity

Date: 2026-10-29
Status: PROVED (elementary graph theorem). Application to Q32 is PROVED_CONDITIONAL on the explicitly stated coloring contract. No full Q32/root closure is claimed.

## Theorem A: the 57-edge outside reserve

Let D be a simple graph on a disjoint union
O union T0 union T1 union T2 union T3,
where |O|=14, |T0|=11, and |Ti|=12 for i=1,2,3.
Assume:
1. alpha(D)<=12 and omega(D)<=5;
2. each Ti is independent in D;
3. O={p} union A, |A|=13, and p has no D-neighbor in A.

Put H=T0 union T1 union T2 union T3 and
b(D)=e_D(O,H)+e_D(O), counting actual edges once.
Then b(D)>=57.

No assumption on e(D), source factorization, minimum degree, residual signatures, or choice of pair matchings is needed.

### Proof: the 56-edge boundary and its equality cases

Each o in O has a D-neighbor in each Ti, i=1,2,3; otherwise Ti union {o} is an independent 13-set. These three edge classes contribute at least42.

Put Z={o in O: N_D(o) intersect T0 is empty}, k=|Z|.
Any two points of Z must be adjacent, by applying alpha(D)<=12 to T0 union {u,v}.
Thus Z is a clique. Since p is isolated in D[O], if p belongs to Z then Z={p}.

Also alpha(D[A])<=11, since p is isolated from A. Therefore e_D(A)>=2.
If p is in Z, the remaining outside contribution is at least13+2=15.
If p is not in Z, Z is a subset of A and
e_D(O,T0)+e_D(A) >= 14-k+max(2,binom(k,2)) >=14.
The last minimum is attained only for k=2 or3.
Hence b(D)>=56. If equality holds, every o has exactly one neighbor in each large Ti, and exactly one neighbor in T0 unless o is in Z. The two possible induced graphs on O are:
- k=2: two disjoint edges and ten isolated vertices; Z is one of the edges.
- k=3: one triangle and eleven isolated vertices; Z is the triangle.
For k=2, the second edge must be disjoint from the first: two adjacent edges have an independent12-set in A. All statements are about induced D[O], so no uncounted O-edge remains.

### Blocker-to-component rigidity

In either equality case D[O] is the disjoint union of exactly12 cliques B1,...,B12.
For every t outside O, N_D(t) intersect O contains an entire Bj. Otherwise choose one nonneighbor in each Bj, obtaining an independent12-set that extends by t.

Fix a large track Ti. The twelve sets N_D(t) intersect O, t in Ti, partition O because each o has exactly one neighbor in Ti. Each set contains an entire component. Disjointness and the equality of the two counts (twelve vertices, twelve components) force a bijection:
there is one vertex t_i(B) per component B, and N_D(t_i(B)) intersect O=B.

For distinct tracks i,j, the two representatives t_i(B),t_j(B) must be D-adjacent. If not, choose one vertex in each of the other eleven O-components. Their union with the two representatives is an independent13-set. Consequently B together with its three large-track representatives is a clique.

If k=3, take B=Z, a triangle. Its three large representatives form a K6 with B, contradicting omega(D)<=5.

If k=2, the active components O minus Z are exactly eleven cliques: ten singletons and the other edge B*. The eleven sets N_D(t) intersect O, t in T0, partition O minus Z. Each contains an entire O-component by the blocker argument; none can contain Z. Thus they are exactly the eleven active components, bijectively. In particular a vertex t0(B*) has O-neighborhood B*.
The same independent13 argument makes t0(B*) adjacent to each t_i(B*) for i=1,2,3. Therefore
B* union {t0(B*),t1(B*),t2(B*),t3(B*)}
is a K6, again impossible.

Thus equality b(D)=56 is impossible. Integrality proves b(D)>=57. QED.

## Theorem B: a simultaneous colored-packing obstruction

Let F be the target graph in a 12-edge-coloring of K61. Suppose:
- V=H disjoint-union O, |H|=47, O={p} union A, |A|=13;
- pA is entirely target-colored;
- H partitions into target cliques of sizes12,12,12,11;
- every non-target color C satisfies alpha(C)<=12 and omega(C)<=5.

Then
e(F)-e(F[H])<=122.

Proof. The number of unordered pairs with at least one endpoint in O is
14*47+binom(14,2)=749.
By Theorem A, the eleven edge-disjoint non-target colors own at least11*57=627 of these pairs. Hence the target owns at most749-627=122. QED.

In E408/Q32, e(F)=408 and e(F[H])=285, so the target owns123 such edges: contradiction.
This excludes EVERY completion with this four-clique partition, independently of m=8,9,10 and independently of the Type-I source modes.

## Corollary: registered aligned m=10 cells

At the frozen high-support HEAD 433a5b39a98325f00e99650b0270d79f7753a47d, V47_Z01_TRACK_ALIGNMENT.md proves the partition for the m=10 disconnected 3+7 cells z=0 and z=1 with fiber profile (2,2,2,1). Those cells are therefore excluded under their registered premises.

This is stronger than combining the new g_D=7 saturation with its equality cases: it does not need the exact-color cap g_C<=3, the 37-gap identity, source-mode classification, or even the number of exact colors. Alignment itself remains an imported conditional premise.

## An independent and shorter parent-contract exclusion

The genuine T61 parent also has omega(F)<=11.
This is explicit in front_end/FRONTEND_BRIDGE_THEOREM.md F7-F8,
front_end/T61_NEW_LEMMAS.md context, and
front_end/T61_H13_FULL_COLOR_DEGREE_AND_ANTINEIGHBORHOOD.md Section1.
It comes from inclusion-maximality of the six packed target K12 blocks in the anchor nonneighborhood.

Thus a target K12 inside H already contradicts the genuine parent contract.
More generally no genuine 47-point H can be partitioned into four target cliques:
each would have size at most11, covering at most44 vertices.
Equivalently chi(complement(H))>=5.

Theorem B is still useful as an independent obstruction for the relaxed four-track contract that omitted omega(F)<=11. It must not be confused with an exclusion of every full-support graph.
