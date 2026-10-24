# CHAT K — Finite Geometry / Low-Slack Coordinatization

Branch: workstream/general-r-finite-geometry-20261024

Target: prove P(q) for prime powers q, or a sufficiently-large prime-power family. The headline theorem remains OPEN.

## Proved local theorems

### 1. Low-slack coordinatization

On any q^2-point restriction W of a hypothetical counterexample, define

\[
m_q=q\binom q2,\qquad s_i=e(G_i[W])-m_q.
\]

For q>=3, Brouwer's non-r-partite Turan threshold implies that if 0<=s_i<=q-2, then G_i[W] consists of q disjoint monochromatic K_q blocks plus exactly s_i same-color cross-block edges.

If two colors have slack <=q-2 on the same W, their two block partitions are exactly orthogonal. This is a 2-net/grid, not yet a full affine plane.

### 2. Strengthened local forcing and universal global excess

For x outside W, let B_a be the non-color-i neighbors of x inside the i-block P_a. Every B_a is nonempty in a counterexample. The one-block greedy argument gives min_a |B_a|<=s_i.

The weighted blocker inequality improves this: the defect graph on the B_a parts has no independent transversal, so some pair satisfies |B_a||B_b|<=s_i. Hence

\[
d_i(x)\ge2q-s_i(x)-1.
\]

Writing e_i=m_q+q+a_i and s_i(x)=q+a_i-d_i(x) yields a_i>=q-1 whenever color i is low-slack at a vertex. The exact average-slack identity upgrades this to the universal bound

\[
\boxed{a_i\ge q-1\quad\forall i.}
\]

If a_i<=q-2, the average local slack would be below q-1, forcing a low-slack vertex and contradiction. The total excess above this universal floor is q(q-1)(q-2)/2. The floor is sharp for the single-color graph constraints alpha(G_i),omega(G_i)<=q: a q-block-plus-extra-vertex construction attains a_i=q-1, although this is not a full coloring counterexample.

### 3. Local multicolor degree budget

For any vertex x, if L_s(x)={i:s_i(x)<=s} with 1<=s<=q-2, then

\[
|L_s(x)|\le\left\lfloor\frac{q^2}{2q-s-1}\right\rfloor,
\]

and the full low-slack set satisfies

\[
\sum_{i:s_i(x)\le q-2}(2q-s_i(x)-1)\le q^2.
\]

In particular, at most floor((q+1)/2) colors can have slack one at a fixed vertex, and at least one color has slack at least q-1 there. This is a multicolor compatibility inequality, not a contradiction.

### 4. Weighted blocker and small-slack classification

See TRANSVERSAL_BLOCKER_LEMMA.md and SMALL_SLACK_BLOCKER_CLASSIFICATION.md. The weighted inequality is

\[
\sum_{uv\in E(F)}\frac{1}{|B_{a(u)}||B_{a(v)}|}\ge1.
\]

If there is only one relevant defect edge, it must join two singleton residual parts. If there are at most two relevant edges, either there is a singleton-singleton edge or the two edges join a singleton part to the two different vertices of a size-two part.

The latter can involve three parts for arbitrary residual parts. Only in the aligned J-shell setting, where B_a=P_a minus Y and |Y|=2q-1, is the three-part 1,1,2 pattern ruled out for q>=4.

### 5. Slack-one crossed pattern

If two distinct colors i,j have s_i(x)=s_j(x)=1 on the same q^2 restriction, the partitions are orthogonal. Their unique defect edges and extra-vertex labels force a crossed 2-by-2 pattern: the i-defect edge joins two cells whose edges to x are color j, while the j-defect edge joins two cells whose edges to x are color i. Also a_i,a_j>=q-1.

Full proof: SLACK_ONE_CROSS_PATTERN.md. This is a rigid local pattern, not a contradiction.

### 6. Global slack dictionary

For N=q^2+1, every color has e_i>=m_q+q. Writing e_i=m_q+q+a_i gives sum_i a_i=m_q, s_i(x)=q+a_i-d_i(x), and sum_i s_i(x)=m_q. Also sum_x s_i(x)=q(q-1)+(q^2-1)a_i. Scalar averaging alone does not force two low-slack colors.

## Round 2 high-slack audit — local gap proved, global contradiction open

The new theorem in `HIGH_SLACK_COMPATIBILITY.md` proves `s_i(x)>=q-1` for every vertex x and every color i in a full hypothetical counterexample. Thus no color can be low-slack at any vertex; the former `at most one low-slack color` branch is superseded. This follows by combining the existing low-slack block decomposition and weighted blocker with the fact that each block plus x must contain all q colors.

The global high-slack contradiction remains OPEN: `sum_i s_i(x)=m_q` is compatible with every term being at least q-1. The formal scalar profile remains only an abstract scalar profile, not a graph-realizable example.

## Finite geometry: exact limits

- Two low-slack colors give two orthogonal partitions only.
- q being a prime power does not coordinatize arbitrary extracted partitions.
- Three full size-q blocks in distinct directions with pairwise intersections at most one would exceed a 2q-1 shell, but no such blocks have been extracted from compression failure.
- The J/K bridge is conditional: if a tight transversal X contains x_0 and a color i != c is low-slack on V minus {x_0}, then private witnesses of color i are confined to a bounded number of clique blocks, and in the aligned shell case slack 1 or 2 confines them to at most two blocks (q>=4).

## Current verdict

- Low-slack coordinatization conditional theorem: PROVED, but its premise `s_i(x)<=q-2` is impossible under the full counterexample contract by the new local slack-gap theorem.
- Weighted blocker inequality and two-block forcing: PROVED.
- Universal global excess floor a_i>=q-1: PROVED.
- Local multicolor degree-budget inequality: PROVED.
- Slack-one crossed pattern: PROVED as a conditional lemma; its premise is vacuous in a full hypothetical counterexample.
- Conditional tight-transversal interface: PROVED as a conditional lemma; its low-slack premise is vacuous under the full counterexample contract.
- Global low-slack alignment: NOT APPLICABLE under the full counterexample contract, because no local low-slack color exists.
- High-slack contradiction: OPEN.
- Full affine-plane/net completion: OPEN.
- Prime-power P(q): OPEN.


## Round 2 — Local Slack Gap Theorem

For every full hypothetical counterexample, `s_i(x)>=q-1` for all `x,i`. The proof combines (i) the low-slack structure theorem, (ii) the weighted blocker, and (iii) the q+1-set color-coverage condition on `{x} union A_a` for each monochromatic K_q block. Each block can contain at most one i-neighbor of x, while the blocker would force at least q+1 such neighbors if `s_i(x)<=q-2`.

This is a new exact multicolor rigidity theorem, but not an EG617 contradiction and not an H seed-floor theorem. See `HIGH_SLACK_COMPATIBILITY.md` and `SEED_FLOOR_INTERFACE.md`. The prior small-slack structural statements remain conditional graph lemmas; they must not be described as realizable local patterns of a counterexample.

## Round 2 — residual multinet extraction from J's tight-transversal case

New cross-workstream theorem: RESIDUAL_MULTINET_EXTRACTION.md. It cites J branch commit 009a546cf0d66e4060a601bba168674214e7ac6c and does not copy an unverified proof.

Under J's Case B contract, put q=r-1 and R=V minus X, |R|=q². The residual excesses of the q colors i!=c satisfy b_i>=0 and sum b_i<=C(q,2). Therefore at least ceil(q/2) colors have b_i<=q-2. For q>=3, Brouwer's threshold gives a q-clique partition for each such color, and any two of these partitions are orthogonal. Hence Case B forces a q-net with at least ceil(q/2) directions.

Exact consequence: N(q)>=ceil(q/2)-2 MOLS of order q. In particular, a hypothetical r=11 Case B counterexample forces three MOLS(10), whose existence remains open (Bright–Keita–Stevens, EJC 33(1) (2026), DOI 10.37236/13960). This is a conditional structural reduction, not a contradiction.

Subcase: if alpha(G_c[R])<=q as well, then all residual excesses vanish and R is an affine plane of order q. No extension contradiction with X has yet been proved. Case A remains outside this extraction.


## Targeted finite-geometry subproblems exposed by Case B

The residual q-net theorem gives two useful non-prime-power reductions:

- r=11 (q=10): Case B forces at least 5 directions, hence 3 MOLS(10). The general existence question remains open (Bright–Keita–Stevens, EJC 2026, DOI 10.37236/13960).
- r=15 (q=14): Case B forces at least 7 directions, hence 5 MOLS(14). Four MOLS(14) are known, while existence of a fifth remains open (Todorov, JCD 2012, DOI 10.1002/jcd.21298; subsequent MOLS literature).

Since affine planes of orders 10 and 14 do not exist, the full-affine-plane subcase is unavailable at these q. These are conditional reductions of Case B only; Case A remains open and neither design implication is a contradiction.


## Round 3 — first high-excess normal form

The residual multinet theorem is supplemented by Theorem K.RM4 in RESIDUAL_MULTINET_EXTRACTION.md. At b_i=q-1, the complement graph is an extremal non-q-partite K_{q+1}-free graph if it is not q-partite. Kang–Pikhurko's exact classification gives a one-exceptional-vertex form; in the q-partite alternative, G_i[R] is q equal clique blocks plus q-1 cross-block defects. The nonpartite form has a residual exceptional point of color-i degree 2q-2-a, 1<=a<=q-1.

This theorem is exact at the first high-excess threshold only. It refines the repeated-witness-color branch but does not exclude it; b_i>=q remains OPEN.


## Round 4 — exact r=7 Case B profile

Theorem K.RM5 is proved in RESIDUAL_MULTINET_EXTRACTION.md (commit eb238d01b9aebf98a7614dba00e2696a2f3d05cf). For q=6, absence of an orthogonal mate of order 6 bounds the number of q-partite residual color complements by three. The residual budget then forces exactly three non-q-partite colors with b_i=5 and three zero-excess colors with b_i=0.

The three zero-excess colors give a 3-net / Latin square of order 6. The omitted color c has exactly 75 edges on R and is a union of seven c-cliques of sizes 6,5,5,5,5,5,5. The 6-clique is a full transversal of the three directions; the six 5-cliques are near-transversals. Each high color is at the Kang–Pikhurko exceptional-star threshold.

This is an exact finite incidence kernel for Case B at r=7, not a contradiction. The partition into one transversal and six near-transversals does not itself give an orthogonal mate, so the Euler–Tarry theorem alone does not exclude it.


Audit correction for r=7: the design-level subkernel from K.RM5 is realizable. K branch file Q6_NEAR_TRANSVERSAL_OBSTRUCTION_AUDIT.md (commit 825c48ae4e5cc47e7feb6abab6337de62db6fd6c) gives an explicit order-6 Latin square partitioned into one full transversal and six disjoint near-transversals. This is not a full graph-level EG617 coloring, but it proves that the net-plus-clique-size pattern alone cannot be ruled out by the nonexistence of an orthogonal mate. The missing constraints are the three exceptional-star color graphs and root/witness incidence.


## Round 5 — strict residual budget and r=7 Case B closure

J branch commit c0c31e82b2bd8b4c3c5a7ab6092b660d16bd686b proves J.W8/J.W9: for q=r-1>=4, the equality residual budget sum b_i=C(q,2) creates q+1 c-clique blocks of sizes q and q-1 (q times). Every root must be c-adjacent to an entire block, but block capacities are 1 for the size-q block and 2 for each size-(q-1) block, totaling 2q+1<|X|=2q+2. Hence equality is impossible and at least ceil((q+1)/2) residual directions are forced.

At q=6 (r=7), this gives four directions, hence two orthogonal Latin squares of order 6, impossible. **The tight-transversal Case B is now CLOSED at r=7.** The Latin-square-only near-transversal partition remains realizable but cannot satisfy the full root-block constraints. Case A remains OPEN.
