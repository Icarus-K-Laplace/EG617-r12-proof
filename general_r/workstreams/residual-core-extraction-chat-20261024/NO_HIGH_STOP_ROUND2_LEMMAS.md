# High-stop Round 2: excess concentration, critical windows, predecessor interface

Date: 2026-10-24  
Workstream: `general-r-residual-core-extraction-20261024`

Primary status: **partial progress; NO-HIGH-STOP remains OPEN**.

This file only attacks the high-stop obstruction. It does not revisit the residual-core minimum-degree theorem or fixed-r recurrence.

## 1. Exact simultaneous excess concentration

Let (R_a) be a first (K_r)-free canonical stop, (a\ge 6), with (n=ar+1). For the target color (0), let (x_0=e(G_0[R_a])-p_a(n)); for each non-target color (i\in\{1,\dots,r-1\}), let (x_i=e(G_i[R_a])-p_r(n)). The established ledger is

[
x_0+\sum_{i=1}^{r-1}x_i=S_a(r)
=\left(\binom a2-1\right)r+a.
]

All (x_i\ge0), so (\sum_{i=1}^{r-1}x_i\le S_a(r)).

### Theorem 1 — simultaneous near-Turán edge counts

Define

[
C_{a,r}:=\left\lceil\frac{2S_a(r)}{r-1}\right\rceil.
]

Then at least \(\lfloor r/2\rfloor\) non-target colors satisfy

[
x_i\le C_{a,r}\le a^2-1
qquad (r\ge a+1).
]

**Proof.** Let (m) be the number of non-target colors with (x_i>C_{a,r}). Since each such integer excess is at least (C_{a,r}+1>2S_a(r)/(r-1)),

[
m\frac{2S_a(r)}{r-1}<\sum_{i=1}^{r-1}x_i\le S_a(r),
]

so (m<(r-1)/2). Hence at least \(\lfloor r/2\rfloor\) colors lie below the threshold.

For the uniform bound, the inequality (C_{a,r}\le a^2-1) is equivalent to

[
(a+1)r\ge a^2+2a-1,
]

which holds strictly for (r\ge a+1). \(\square\)

For (a=6), (S_6(r)=14r+6), and

[
C_{6,r}=\left\lceil28+\frac{40}{r-1}\right\rceil.
]

Thus for (r\ge41), at least \(\lfloor r/2\rfloor\) non-target colors have (x_i\le29).

### Exact Turán interpretation

For each non-target color, (F_i:=\overline{G_i[R_a]}) is (K_{r+1})-free and

[
e(F_i)=t_r(ar+1)-x_i,
\qquad
t_r(n):=\binom n2-p_r(n).
]

Consequently at least half of the non-target complements are within (a^2-1) edges of the exact Turán maximum. Section 4 below closes the uniform partition-stability subgap using Füredi's quantitative theorem.

**Open stability issue.** The number of parts (r) grows with the parameter. A fixed-(r) stability statement cannot be applied with constants silently assumed uniform in (r). We still need a quantitative uniform lemma of the form

[
e(F)\ge t_r(ar+1)-C
\Longrightarrow
F\text{ is within }f(a,C)\text{ edits of }T_r(ar+1),
]

with an explicit (f) independent of (r). This implication is not claimed here.

## 2. Exact residue windows from the critical-core polynomial

Let (Q\subseteq R_a) be the induced ((r+1))-critical core, with

[
q=|Q|=\ell r+t,\qquad 0\le t<r.
]

The inherited cap and the Kostochka–Yancey lower bound require

[
P_{\ell,t}(r)\le0,
]

where

[
P_{\ell,t}(r)
=r^2(-\ell^2+3\ell+t-1)
+r(-2\ell t-2\ell-t^2+2t+1)-2t+2.
]

For \(\ell\ge2\), define

[
A_\ell=\ell^2-3\ell+1=(\ell-1)(\ell-2)-1,
\qquad
B_\ell=\ell^2-\ell-1=\ell(\ell-1)-1,
]

and

[
R_\ell:=\ell(\ell-1)^2(\ell-2)+2\ell+2.
]

### Theorem 2 — bounded residue windows

If (r\ge R_\ell) and (P_{\ell,t}(r)\le0), then

[
\boxed{t\le A_\ell
\quad\text{or}\quad
r-t\le B_\ell.}
]

When \(\ell=2\), the first alternative is impossible because (A_2=-1), so necessarily (r-t\le1).

**Proof sketch.** Put (u=r-t). Direct algebra gives the two equivalent forms

[
\frac{P_{\ell,t}(r)}r
=t(r-t)-2(\ell-1)t-A_\ell r-(2\ell-1)-\frac{2t-2}{r},
]

and

[
\frac{P_{\ell,r-u}(r)}r
=u(r-u)+2(\ell-1)u-B_\ell r-(2\ell+1)+\frac{2u+2}{r}.
]

Each right-hand side is a concave quadratic in its residue variable. For (r\ge R_\ell), it is positive at both endpoints of the interval from the proposed boundary (A_\ell+1) (respectively (B_\ell+1)) to (r/2). Concavity then makes it positive throughout that interval. Therefore (P\le0) forces one of the two stated boundary windows. All thresholds here are explicit. \(\square\)

For a fixed (a), (r\ge R_a) therefore confines (q\le ar+1) to bounded-width windows around multiples of (r). In particular,

[
R_6=614.
]

For (a=6), (r\ge614), and the already-proved (3r-1\le q\le6r+1), the only possible critical-core orders lie in

[
\boxed{
[3r-1,3r+1]
\;\cup\;
[4r-5,4r+5]
\;\cup\;
[5r-11,5r+11]
\;\cup\;
[6r-19,6r+1].
}
]

These are necessary windows, not existence claims. They eliminate every middle-residue regime but do **not** eliminate the surviving windows. In particular the current critical-core potential alone does not close (a=6).

## 3. First-stop predecessor interface

Suppose (R_a) is the first (K_r)-free state and (R_{a+1}) is its predecessor. Let (B\cong K_r) be the target-color clique deleted to obtain (R_a), and let (n=ar+1=|R_a|).

For each (v\in R_a), consider the (r) edges between (v) and (B). Since (B\cup\{v\}) has (r+1) vertices, the balanced-coloring condition requires every one of the (r) colors to occur among these edges or inside (B). The target color already occurs inside (B), so every non-target color must occur at least once among the (r) cross-edges.

Thus exactly one of the following happens for each (v):

1. (v) has exactly one target-color neighbor in (B), and each of the (r-1) non-target colors occurs exactly once on (vB);
2. (v) has no target-color neighbor in (B), and exactly one non-target color occurs twice on (vB), with all other non-target colors occurring once.

Let (q_0=e_0(B,R_a)), the number of vertices in case 1. For each non-target color (i), let (z_i) be the number of vertices in case 2 whose duplicated color is (i). Then

[
\sum_{i=1}^{r-1}z_i=n-q_0,
\qquad
e_i(B,R_a)=n+z_i.
]

The excesses of the predecessor and current states satisfy the exact identities

[
x_0(R_{a+1})=x_0(R_a)+q_0,
]

[
x_i(R_{a+1})=x_i(R_a)+z_i
\quad (i\ge1).
]

Consequently every color's excess is monotone nondecreasing when moving backward one canonical step, and the total increment is exactly

[
q_0+\sum_i z_i=n= S_{a+1}(r)-S_a(r).
]

This is a genuine first-stop constraint: the predecessor interface is a near-permutation matrix, with one target edge per column or one duplicated non-target color. The label-capacity lemma below strengthens it by proving that every non-target color must be duplicated at least once.

### Label-capacity lemma — every non-target color is duplicated

For every non-target color (i),

`z_i>=1`.

Consequently

`sum_i z_i>=r-1`,
`q_0<=n-(r-1)=(a-1)r+2`.

In words: at least (r-1) vertices of (R_a) have no target-color edge to (B), and every non-target color occurs twice on the (B)-neighborhood of at least one such vertex.

**Proof.** Fix a non-target color (i) and (b\in B). Let (S_{i,b}) consist of vertices (v\in R_a) for which (vb) is the unique color-(i) edge from (v) to (B). For any two distinct (u,v\in S_{i,b}), the ((r+1))-set

`(B\\{b}) union {u,v}`

already contains every color other than (i): the clique (B\\{b}) supplies the target color, and each of (u,v) has its unique (i)-edge at the omitted vertex (b). Therefore the balanced-coloring property forces (uv) to have color (i). So (S_{i,b}) is independent in the target-color graph (G_0[R_a]). Since (alpha(G_0[R_a])=a),

`|S_{i,b}|<=a`.

Every vertex except those counted by (z_i) has exactly one color-(i) edge to (B), and hence lies in exactly one of the (r) classes (S_{i,b}). Thus

`n-z_i=sum_{b in B}|S_{i,b}|<=ar`.

Since (n=ar+1), (z_i\ge1). Summing over the (r-1) non-target colors gives the stated bounds. \(\square\)

Moreover, the class sizes satisfy the exact hole identity

`sum_{b in B}(a-|S_{i,b}|)=z_i-1`.

Thus the predecessor clique induces, for every non-target color, an exact partition of all but (z_i) vertices of (R_a) into (r) monochromatic (i)-cliques, each of size at most (a). The total unused capacity of these (r) classes is exactly (z_i-1). If (z_i=1), all (r) classes have size exactly (a).

### Consequence for excess propagation

At every canonical step (R_{a+1}\to R_a),

`x_i(R_{a+1})-x_i(R_a)=z_i>=1` for every non-target color (i),

while the target increment satisfies

`x_0(R_{a+1})-x_0(R_a)=q_0< ar+1`.

This is a strict strengthening of the earlier monotonicity statement: all non-target excesses increase at every predecessor step, not merely in aggregate. It does not by itself rule out a high stop because the total ledger has quadratic-in-(a) slack.

## 4. Uniform partition stability from Füredi's theorem

External theorem used: Füredi's quantitative Turán stability bound, explicitly recalled in Balogh–Clemen–Lavrov–Lidický–Pfender, *Making K_{r+1}-free graphs r-partite*, Combinatorics, Probability and Computing 30 (2021), 609–618, DOI [10.1017/S0963548320000590](https://doi.org/10.1017/S0963548320000590), §1: if a K_{k+1}-free graph F has e(F) >= t_k(n)-x, then at most x edges need to be deleted to make F k-partite.

### Theorem 3 — quantitative partition stability for every color

Let n=ar+1. For each color i, put k_0=a for the target color and k_i=r for non-target colors. Let G_i be its color graph on R_a and F_i=bar(G_i). Then F_i is K_{k_i+1}-free and

`e(F_i)=t_{k_i}(n)-x_i`.

Füredi's theorem supplies a partition P_i into k_i parts. Let:

- I_i be the number of F_i-edges internal to parts;
- M_i be the number of missing F_i-edges across parts;
- Delta_i be the edge deficit of the complete k_i-partite graph on those same parts from t_{k_i}(n).

Then

`I_i<=x_i`,
`Delta_i+M_i=x_i+I_i<=2x_i`,
`Delta_i<=2x_i`, `M_i<=2x_i`,

and the edit distance from F_i to the complete multipartite graph on P_i is

`I_i+M_i<=3x_i`.

Because n=ar+1 and k_i is either a or r, the balanced part sizes are one part of size q+1 and all other parts of size q, where q=r for i=0 and q=a for i>=1. If s_j are the actual part sizes and d_j=s_j-q, then sum d_j=1 and

`sum_j d_j^2=2 Delta_i+1<=4x_i+1`.

Consequently:

- at most `4x_i+1` parts differ from size q;
- every part differs from q by at most `floor(sqrt(4x_i+1))`;
- each color's complement is within `3x_i` edge edits of a complete multipartite graph on the same vertex set.

This is a uniform-in-r quantitative stability theorem; it does not rely on a fixed-r Erdős–Simonovits constant.

### Theorem 4 — global near-resolvable design

Apply Theorem 3 simultaneously to the target and all non-target colors. Since `sum_i x_i=S_a(r)`,

`sum_i I_i<=S_a(r)`,
`sum_i M_i<=2 S_a(r)`,
`sum_i (I_i+M_i)<=3 S_a(r)`.

Call a vertex pair good if it lies in exactly one block across all color partitions and that block belongs to the pair's actual edge color. A pair is bad otherwise: either it is not in a block of its actual color, or it also lies in a block of a wrong color. Every bad pair is charged to at least one defect edge counted among the I_i or M_i: a pair missing from its actual-color partition is a missing cross-pair, while a pair inside a wrong-color block is an internal edge of that color's complement. Therefore

`# bad pairs <= 3 S_a(r) = 3[(binom(a,2)-1)r+a]`.

Thus the target partition into a row-blocks and the r-1 non-target partitions into r block-classes form an **approximate pairwise balanced / resolvable design**: all but O(a^2 r) of the O(a^2 r^2) vertex pairs are represented by exactly one block of their actual color and by no block of any other color. Across all color partitions, only O(a^2 r) internal or cross-edge defects occur. For fixed a, the proportion of bad pairs is O(1/r).

This is a genuine structural upgrade from near-extremality in edge count. It still does not imply an exact transversal design or an earlier R_5/R_4 state: the allowed O(r) exceptional pairs are on the same scale as the missing-parallel-class deficit, so their concentration and incidence pattern must be analyzed rather than ignored.

## 5. Hub localization in the target complement

Let (G_0=G_0[R_a]) be the target-color graph at a first stop and (F_0=\overline{G_0}). Then (omega(F_0)=\alpha(G_0)=a), so (F_0) is (K_{a+1})-free. The all-color ledger gives (x_0\le S_a(r)), and

`e(F_0)=t_a(ar+1)-x_0`.

Apply Theorem 3 to obtain a partition (V_1\cup\cdots\cup V_a), with (I_0) internal edges of (F_0), (M_0) missing cross-pairs, and part-size deficit (Delta_0). Then

`I_0<=x_0`, `M_0<=2x_0`, `Delta_0<=2x_0`,

`sum_j (|V_j|-r)^2=2 Delta_0+1<=4x_0+1`.

### Theorem 5 — fixed-a hub localization

For every fixed (a\ge6), if

`r >= 200 a(a-1)+1`,

then every internal edge of (F_0[V_j]) has an endpoint (h) for which at least (2r/5) cross-pairs from (h) to some other part are missing from (F_0). Let (H) be the set of all such vertices. Then

`|H| <= 5 a(a-1)`,

and every internal edge of (F_0) is incident to (H). In particular, each (V_j\setminus H) is a clique in the target-color graph (G_0).

**Proof.** Put (C=a(a-1)). Since (r\ge a), (S_a(r)\le Cr/2), so

`M_0<=2x_0<=Cr`,
`sum_j (|V_j|-r)^2<=2Cr+1`.

The stated threshold ensures (|V_j|\ge0.9r) for every (j), and (100M_0/r^2<1). Suppose an internal edge (uv\in E(F_0[V_j])) has neither endpoint missing at least (2r/5) cross-neighbors in any other part. For each (k\ne j), let

`W_k=N_{F_0}(u)\cap N_{F_0}(v)\cap V_k`.

Then (|W_k|\ge |V_k|-4r/5\ge r/10). Choose one vertex independently and uniformly from each (W_k). Any fixed missing cross-pair between two of these sets is selected with probability at most (100/r^2). By the union bound, the probability of selecting any missing cross-pair is at most (100M_0/r^2<1). Thus there is a transversal with all cross-pairs present in (F_0). Together with (u,v), it forms a (K_{a+1}), contradiction.

Therefore every internal edge has an endpoint in (H). Each vertex of (H) has missing cross-degree at least (2r/5), while the sum of missing cross-degrees is (2M_0). Hence

`|H| (2r/5)<=2M_0`, so `|H|<=5M_0/r<=5C`.

Deleting (H) removes all internal edges of (F_0); hence each remaining part is independent in (F_0), equivalently a target-color clique in (G_0).

### Sharpened a=6 instance

For (a=6), (S_6(r)=14r+6). If (r\ge5601), then

`4S_6(r)+1=56r+25<=r^2/100`,
`M_0<=28r+12`,
`100M_0/r^2<1`.

The same proof yields a hub set (H) of size at most (140), with every internal edge of (F_0) incident to (H). This is an explicit fixed-case theorem for the (a=6) high-stop branch, not a contradiction to its existence.

### Limitation / next use

The theorem localizes all defects inside the target partition to (O(a^2)) hub vertices, but it does not yet show that the hubs point to one common part or that a five-part induced subset has clique number at most five in (F_0). A directed/cyclic pattern of hub-protection parts is not ruled out. The remaining target is a hub-propagation lemma that either produces an earlier (R_5) satisfying its edge budget or contradicts the first-stop interface.

## 6. Status ledger for this round

### PROVED

- At least \(\lfloor r/2\rfloor\) non-target colors are within (a^2-1) edges of the exact Turán maximum in the complement.
- The critical-core polynomial confines fixed-(a) residues to explicit bounded-width windows for (r\ge R_a).
- The predecessor-clique cross-color incidence and excess increments are exact.

### NOT PROVED

- (a=6) is impossible.
- Any (a\ge7) candidate contains a legal induced (R_{a-1}).
- A uniform edit-distance partition-stability theorem is proved via Füredi.
- Exact pairwise orthogonality / an exact resolvable-design skeleton.
- Hub propagation to a common target part; the hub-localization theorem alone does not give it.
- A design-trimming implication yielding an earlier (R_5) or (R_4).

### Current verdict

[
\boxed{\texttt{NO-HIGH-STOP = OPEN}.}
]

The critical-core potential has reduced the (a=6) case to four explicit residue windows, the color partitions form a global near-resolvable design with O(r) bad pairs, and all internal target-complement defects localize to at most 140 hubs when a=6 and r>=5601. No all-large-r contradiction has been established. The next highest-leverage step is to classify the hub-protection digraph and prove that it yields an earlier R5 or a contradiction.