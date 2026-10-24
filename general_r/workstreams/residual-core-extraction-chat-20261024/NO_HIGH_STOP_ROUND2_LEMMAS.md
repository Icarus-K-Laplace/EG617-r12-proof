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

**Historical note.** The uniform edit-distance issue identified in the initial concentration analysis is resolved by Theorem 3 in Section 4 below, using Füredi's quantitative Turán theorem.

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

## 5. Constant-width target parts and cylinder hub localization

Let (G_0=G_0[R_a]) be the target-color graph at a first stop and (F_0=\overline{G_0}). Then (omega(F_0)=\alpha(G_0)=a), so (F_0) is (K_{a+1})-free. Its exact Turán deficit is (x_0\le S_a(r)). Apply Füredi stability and let (V_1,\ldots,V_a) be the resulting partition. Write

`s_j=|V_j|`, `D= sum_j e(F_0[V_j])`, `M_0=# missing F_0 cross-pairs`.

Then

`D<=x_0`, `M_0<=2x_0`, `sum_j(s_j-r)^2<=4x_0+1`.

### Theorem 5 — constant-width target groups

For `r>=binom(a,2)+a+1`,

`r-binomial(a,2)+2 <= s_j <= r+binomial(a,2)-1` for every `j`.

**Proof.** For each target ideal group (V_j), every non-target color graph (G_i[V_j]) has independence number at most (r). Hence

`e(F_0[V_j])=sum_{i=1}^{r-1}e(G_i[V_j]) >= (r-1)p_r(s_j) >= (r-1)(s_j-r)_+`.

Summing gives

`(r-1)P<=D<=x_0<=S_a(r)`,

where `P=sum_j(s_j-r)_+`. Put `C=binom(a,2)`, so `S_a(r)=(C-1)r+a`. The threshold gives `S_a(r)<C(r-1)`, hence the integer `P<=C-1`. Since `sum_j(s_j-r)=1`, total negative deviation is `P-1`; therefore every part has negative deviation at most `C-2` and positive deviation at most `C-1`. \(\square\)

For `a=6`, this gives the absolute-width bound

`r-13<=s_j<=r+14` for every `r>=22`.

### Theorem 6 — product-cover / cylinder inequality

Let (C_0) be the graph of target-color edges crossing distinct parts of the partition, so `e(C_0)=M_0`, and let `d_C(v)` be its degree at vertex (v). Put

`L=min_j s_j`.

For every internal edge `uv in E(F_0[V_j])`,

`d_C(u)+d_C(v) >= L-M_0/L`.  (CYL)

**Proof.** Choose one vertex from each of the other `a-1` parts. Together with `u,v`, these vertices would form a (K_{a+1}) in (F_0) unless the tuple contains at least one cross-pair absent from (F_0), i.e. one edge of (C_0). A fixed edge of (C_0) incident to `u` or `v` covers at most a `1/L` fraction of all tuples; all other cross edges together cover at most `M_0/L^2`. The union bound gives

`1 <= (d_C(u)+d_C(v))/L + M_0/L^2`,

which rearranges to (CYL). \(\square\)

### Theorem 7 — bounded target-hub cover

Define

`H_r=L-M_0/L`,
`X={v : d_C(v)>=H_r/2}`.

Whenever `H_r>0`, (CYL) implies that `X` meets every internal edge of (F_0). Since `sum_v d_C(v)=2M_0`,

`|X|<=4M_0/H_r`.  (HUB)

For `a=6`, the constant-width theorem gives `L>=r-13`, and the excess ledger gives `M_0<=2S_6(r)=28r+12`. For every `r>=1000`,

`H_r >= r-13-(28r+12)/(r-13) >= r-42`,

and therefore

`|X| <= 4(28r+12)/(r-42) <117`.

Hence **`|X|<=116` for every `r>=1000`**. Every internal edge of the target complement is incident to this bounded hub set, and outside `X` every target ideal group is an actual target-color clique.

### Limitation / next use

The hub theorem is stronger than a generic (O(\sqrt r)) part-size bound: the target groups have absolute width, and all internal target defects pass through a constant-size high-cross-degree kernel. It does not yet show that all hub-protection parts have a common sink or that the `O(r)` non-target block defects meet the same kernel. A directed cycle of hub protection remains possible; the required next result is hub propagation or robust nonextension, not another stability estimate.

## 6. Almost-complete resolvable transversal design forced by a high stop

This theorem combines the predecessor label-capacity lemma with the constant-width target groups and hub cover above. It is the strongest structural consequence obtained in this round.

### Theorem 8 — near-complete partial resolvable `TD(a,r)`

Fix `a>=6`. For all sufficiently large `r`, any first `K_r`-free canonical stop `R_a` forces a partial resolvable transversal design on `a` target groups of sizes `r+O_a(1)` with

`r^2-O_a(r^(3/2))` blocks.

Every block has one vertex from each target group; any two blocks share at most one vertex; and blocks of a common non-target color form a partial parallel class.

**Proof.** Let `C=binom(a,2)`. The exact excess ledger gives

`sum_{i>0} x_i<=S_a(r)<=Cr` for `r>=a`.

The predecessor label-capacity lemma gives

`sum_{i>0} z_i=n-q_0<=ar+1<=(a+1)r`.

Call a non-target color `i` good if

`x_i<=2C sqrt(r)` and `z_i<=2(a+1)sqrt(r)`.

By Markov counting, at most `sqrt(r)/2` colors violate the first bound and at most `sqrt(r)/2` violate the second. Therefore at least

`r-1-sqrt(r)`

colors are good.

For a good color `i`, the exact hole identity

`sum_{b in B}(a-|S_{i,b}|)=z_i-1`

implies that at least `r-z_i+1>=r-2(a+1)sqrt(r)+1` of its label classes have size exactly `a`.

By the hub theorem, for fixed `a` and sufficiently large `r`, there is a hub set `X` of size `O_a(1)` such that every target ideal group minus `X` is a target-color clique. At most `|X|` label classes of any one color meet `X`. Hence every good color contributes at least

`r-2(a+1)sqrt(r)+1-|X|`

size-`a` classes disjoint from `X`. Each such class is target-independent, so it intersects every clean target group in at most one vertex. Its size is `a`, so it is an exact transversal of all `a` groups.

Classes of one color are disjoint. Classes of different colors cannot share two vertices, because their shared pair would have two distinct colors. Thus the clean transversal blocks form a partial resolvable transversal design, with at least

`(r-1-sqrt(r))(r-2(a+1)sqrt(r)+1-O_a(1)) = r^2-O_a(r^(3/2))`

blocks. \(\square\)

### Explicit `a=6` bound

For `a=6`, `S_6=14r+6<=15r` and `sum_i z_i<=6r+1<=7r`. Thus at most `sqrt(r)/2` colors have `x_i>30sqrt(r)`, and at most `sqrt(r)/2` have `z_i>14sqrt(r)`. At least `r-1-sqrt(r)` colors satisfy both bounds.

For `r>=1000`, the cylinder theorem gives `|X|<=116`. Each good color therefore contributes at least

`r-14sqrt(r)-115`

clean transversal blocks. In total, the first-stop `R_6` contains a pairwise-linear partial resolvable transversal design on six groups of sizes `r+O(1)` with at least

`(r-1-sqrt(r))(r-14sqrt(r)-115) >= r^2-15r^(3/2)-102r`

blocks.

Equivalently, all but `O(r^(3/2))` cross-group pairs are covered by exactly one of these clean blocks. This is a near-complete `TD(6,r)`-type geometry, not yet an exact `TD(6,r)` and not yet a contradiction.

### Why this matters / remaining gap

A high stop cannot be an arbitrary sparse perturbation of Turán structure: it carries almost `r^2` exact transversal blocks, arranged in almost-complete parallel classes, while all target internal defects pass through a bounded hub kernel. The next step is a **completion / robust nonextension theorem** for this near-complete resolvable transversal design, using the predecessor interface and the exact critical-core residue windows. `NO-HIGH-STOP` remains open.

## 7. Status ledger for this round

### PROVED

- At least `floor(r/2)` non-target colors are within `a^2-1` edges of the exact Turán maximum in the complement.
- Uniform edit-distance partition stability and the global near-resolvable design are proved via Füredi.
- The critical-core polynomial confines fixed-`a` residues to explicit bounded-width windows for `r>=R_a`.
- The predecessor label-capacity lemma proves `z_i>=1` for every non-target color, with exact class-hole identity.
- For fixed `a`, target groups have absolute width and every internal target-complement edge is incident to at most `4M_0/H_r` hubs; for `a=6`, at most 116 hubs suffice for `r>=1000`.
### NOT PROVED

- (a=6) is impossible.
- Any (a\ge7) candidate contains a legal induced (R_{a-1}).
- Exact pairwise orthogonality / an exact resolvable-design skeleton.
- Hub propagation to a common target part; the hub-localization theorem alone does not give it.
- A design-trimming implication yielding an earlier (R_5) or (R_4).

### Current verdict

[
\boxed{\texttt{NO-HIGH-STOP = OPEN}.}
]

The critical-core potential has reduced the (a=6) case to four explicit residue windows, the color partitions form a global near-resolvable design, and any high stop forces an almost-complete partial resolvable TD(6,r) with `r^2-O(r^(3/2))` blocks plus a hub kernel of size at most 116 for `r>=1000`. No all-large-r contradiction has been established. The next highest-leverage step is a completion / robust nonextension theorem for this partial design.