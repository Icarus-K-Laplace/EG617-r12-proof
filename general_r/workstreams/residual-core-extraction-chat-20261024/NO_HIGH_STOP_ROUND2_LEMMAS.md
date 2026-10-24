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

**Proof.** The exact predecessor identity gives

`sum_{i>0} z_i=n-q_0<=ar+1<=(a+1)r`.

Call a non-target color `i` good when `z_i<=2(a+1)sqrt(r)`. Markov counting shows that fewer than `sqrt(r)/2` colors are bad, so at least

`r-1-sqrt(r)/2`

colors are good. The exact hole identity

`sum_{b in B}(a-|S_{i,b}|)=z_i-1`

implies that a good color has at least `r-2(a+1)sqrt(r)+1` label classes of size exactly `a`.

By the fixed-`a` hub theorem, the target ideal groups have sizes `r+O_a(1)` and there is a set `X` of size `O_a(1)` such that each group minus `X` is a target-color clique. Since the classes `S_{i,b}` for a fixed color are disjoint, at most `|X|` classes meet `X`. Every remaining size-`a` class is target-independent and intersects each clean target group at most once, hence is an exact transversal.

Blocks of one color are disjoint; blocks of distinct colors share at most one point because every vertex pair has only one color. Therefore the clean blocks form a partial resolvable transversal design with at least

`(r-1-sqrt(r)/2)(r-2(a+1)sqrt(r)+1-O_a(1)) = r^2-(2a+5/2)r^(3/2)-O_a(r)`

blocks. \(\square\)

### Explicit `a=6` bound

For `a=6`, `sum_i z_i<=6r+1<=7r`, so fewer than `sqrt(r)/2` colors have `z_i>14sqrt(r)`. At least `r-1-sqrt(r)/2` colors are good.

The Brouwer-tightened hub theorem gives `|X|<=74` and target group sizes `r-8` through `r+9` for `r>=1000`. Each good color contributes at least

`r-14sqrt(r)-73`

clean transversal blocks. Thus the first-stop `R_6` contains a pairwise-linear partial resolvable transversal design on six groups with at least

`(r-1-sqrt(r)/2)(r-14sqrt(r)-73) >= r^2-(29/2)r^(3/2)-67r`

blocks for `r>=1000`.

Equivalently, all but `O(r^(3/2))` cross-group pairs are covered by exactly one clean block. This is a near-complete `TD(6,r)`-type geometry, not an exact design and not a contradiction.

### Why this matters / remaining gap

A high stop cannot be an arbitrary sparse perturbation of Turán structure: it carries almost `r^2` exact transversal blocks, arranged in almost-complete parallel classes, while all target internal defects pass through a bounded hub kernel. The next step is a **completion / robust nonextension theorem** for this near-complete resolvable transversal design, using the predecessor interface and the exact critical-core residue windows. `NO-HIGH-STOP` remains open.

## 7. Brouwer excess floors and a scalar-feasibility audit

This section sharpens the simultaneous ledger using the non-partite Turán theorem. It also records a deliberate abstract parameter countermodel: the scalar ledger, target-part sizes, hub cardinality, and pair-count identities alone do not rule out a high stop.

### Theorem 9 — all-color Brouwer floors

Assume a high-stop state with `n=ar+1`, `alpha(G_0)=a`, `omega(G_0)<=r-1`, and for every non-target color `i`, `alpha(G_i)<=r`. Let `F_i=bar(G_i)` and `x_i=t_{k_i}(n)-e(F_i)` as in the excess ledger, with `k_0=a` and `k_i=r` for `i>0`. Put `C=binom(a,2)`.

Then

`x_0>=r`,
`x_i>=a-1` for every `i>0`.

**Proof for the target color.** `F_0` is `K_{a+1}`-free. It is not `a`-partite: otherwise each independent part has size at most `alpha(F_0)=omega(G_0)<=r-1`, so `n<=a(r-1)<ar+1`. Brouwer's bound gives `x_0>=floor(n/a)-1=r-1`. If equality held, the Kang–Pikhurko equality classification gives an independent set in `F_0` of size at least `floor(n/a)=r`, contradicting `alpha(F_0)<=r-1`. Hence `x_0>=r`.

**Proof for a non-target color.** A color-`i` clique is target-independent, so `omega(G_i)<=alpha(G_0)=a` and therefore `alpha(F_i)<=a`. Also `F_i` is `K_{r+1}`-free. It cannot be `r`-partite, since its independent parts would each have size at most `a`, forcing `n<=ar`. Brouwer's bound gives

`e(F_i)<=t_r(n)-floor(n/r)+1=t_r(n)-a+1`,

so `x_i>=a-1`. This bound is sharp at the scalar level; no claim that equality is impossible is made. \(\square\)

### Corollary 9.1 — tightened excess and hub budgets

Combining the floors with the exact ledger

`x_0+sum_{i>0}x_i=S_a(r)=(C-1)r+a`,

gives

`x_0 <= (C-a)r+2a-1`,
`sum_{i>0}(x_i-(a-1)) <= (C-a-1)r+2a-1`.

For `a=6`, these become

`x_0<=9r+11`,
`sum_{i>0}(x_i-5)<=8r+11`.

Since `D<=x_0` and `(r-1)P<=D`, where `P=sum_j(|V_j|-r)_+`, the target ideal parts satisfy, for `a=6` and `r>=22`,

`r-8<=|V_j|<=r+9`.

Also `M_0<=2x_0`, so

`M_0<=18r+22`.

Using the product-cover hub theorem with `L>=r-8`, for `r>=1000`

`H_r=L-M_0/L >= r-27`,
`|X|<=4M_0/H_r <= 4(18r+22)/(r-27)<75`.

Thus **`|X|<=74` for `a=6, r>=1000`**, improving the earlier bound 116. The proof only uses the existing Füredi stability and cylinder inequality; no hub-propagation conclusion is inferred.

### Audit lemma 9.2 — when `alpha(G_0)=a` is automatic

For fixed `a>=6`, if `r>=a^2`, the exact excess ledger itself forces `alpha(G_0)=a` (assuming only the canonical upper bound `alpha(G_0)<=a`). For `a=6`, the same argument already works for `r>=24`.

Indeed, if `alpha(G_0)<=a-1`, then `e(G_0)>=p_{a-1}(n)`, while `e(G_0)=p_a(n)+x_0<=p_a(n)+S_a(r)`. The balanced-partition square-sum bounds give

`p_{a-1}(n)-p_a(n) >= n^2/(2a(a-1))-a/8`,

which is greater than `S_a(r)` for fixed `a>=6, r>=a^2`; for `a=6`, it is greater than `14r+6` for `r>=24`. This contradiction proves the claim. For `a` growing with `r`, this argument does not give a uniform threshold; that regime is not silently covered.

### Abstract parameter countermodel — scalar constraints do not close the gap

For `a=6` and any sufficiently large integer `r`, consider the following **abstract ledger assignment**:

`x_0=9r+11`, `x_i=5` for all `r-1` non-target colors;
`z_i=1` for all `i`, `q_0=5r+2`;
`(|V_1|,...,|V_6|)=(r+1,r,r,r,r,r)`, `Delta=0`;
`D=7`, `M_0=9r+18`, `|X|=7`.

Place all `r-1` duplicated vertices (one for each color) in the `r+1` target group; the remaining two vertices there can be its hubs, and each color's `r` label classes can be transversal at the group-count level. These numbers pass the currently proved scalar checks:

- Exact excess: `x_0+sum_i x_i=(9r+11)+5(r-1)=14r+6=S_6(r)`.
- Exact predecessor interface: `sum_i z_i=r-1`, `q_0=6r+1-(r-1)=5r+2`; predecessor increments are `x'_0=x_0+q_0=14r+13`, `x'_i=x_i+z_i=6`, summing to `S_7(r)=20r+7`.
- Target partition identity: `x_0=Delta+M_0-D=9r+11`.
- Stability budgets: `D<=x_0` and `M_0<=2x_0`.
- Group sizes meet the sharpened `r-8` to `r+9` range. Seven hubs are enough at the counting level to leave at most `r-1` ordinary vertices in each group (two hubs in the `r+1` group, one in each other group).
- If all `z_i=1` classes are transversals, their blocks cover `15r(r-1)` cross-group pairs, leaving `20r` pairs; the assignment `M_0+(11(r-1)-D)=(9r+18)+(11r-18)=20r` passes the global cross-pair count as well.

**Status of this object: `ABSTRACT_PARAMETER_COUNTERMODEL`, not a graph counterexample.** It does not certify a real edge-coloring, the full `K_{r+1}`-free constraints for every `F_i`, or the equality-case incidence pattern in Brouwer's theorem. Its purpose is narrower and important: the exact scalar ledgers, the improved hub count, and the pair-count identity alone still permit a formally consistent high-stop budget. Any proof of NO-HIGH-STOP must use additional incidence information, not merely rearrange these scalar inequalities.

### Consequence and next attack

The strongest new interface is now the **Brouwer excess vector**

`y_i:=x_i-(a-1)>=0`, with `sum_i y_i <= (C-a-1)r+2a-1`.

For `a=6`, the total non-target excess above the sharp individual floor is at most `8r+11`. The next step is to classify the `y_i=0` / small-`y_i` color graphs using the Kang–Pikhurko extremal templates and align their two-star defect pattern with the predecessor label classes `S_{i,b}`. The required theorem is a joint incidence-packing inequality linking those extremal templates to `D`, `M_0`, and the bounded hub kernel. The scalar countermodel above shows why another scalar-only refinement will not suffice.

## 8. Exact label-pair incidence and the per-color defect identity

This section uses the full predecessor interface, rather than only its scalar sum. It gives an exact edge-count identity and a pairwise obstruction for each duplicated color label. It does **not** close `NO-HIGH-STOP`.

Fix a non-target color `i`. Write `F_i=bar(G_i[R_a])`, `n=ar+1`, and

`S_b=S_{i,b}`, `s_b=|S_b|`, `h_b=a-s_b`, `Z=Z_i`, `z=|Z|=z_i`.

Thus the `S_b` are disjoint color-`i` cliques, `|S_b|<=a`, `Z` is the set of vertices duplicating color `i` on the predecessor clique `B`, and

`sum_b h_b=z-1`.

Let:

- `M_i` be the number of color-`i` edges between distinct classes `S_b,S_c`;
- `H_i` be the number of color-`i` edges between `Z` and `union_b S_b`;
- `K_i` be the number of color-`i` edges inside `Z`;
- `Q_i=sum_b binom(h_b,2)` be the hole-concentration statistic.

### Theorem 10 — exact predecessor-label defect identity

`M_i+H_i+K_i = x_i + (a-1)z_i + 1 - Q_i`.  (EL)

**Proof.** Since each `S_b` is independent in `F_i`, and every other pair is either a cross-class pair or meets `Z`,

`e(F_i) = sum_{b<c} s_b s_c - M_i + z_i sum_b s_b - H_i + binom(z_i,2)-K_i`.

Put `h_b=a-s_b`. Then `sum h_b=z_i-1`, `sum_b s_b=ar+1-z_i`, and

`sum_{b<c}s_b s_c = t_r(ar)-a(r-1)(z_i-1)+sum_{b<c}h_bh_c`.

Using `sum_{b<c}h_bh_c=binom(z_i-1,2)-Q_i` and `t_r(ar+1)=t_r(ar)+(r-1)a`, direct simplification gives

`t_r(n)-[sum_{b<c}s_b s_c+z_i sum_b s_b+binom(z_i,2)] = -(a-1)z_i-1+Q_i`.

Subtracting the edge formula from `t_r(n)` and using `x_i=t_r(n)-e(F_i)` proves (EL). `\square`

Interpretation: `M_i+H_i+K_i` is the exact number of color-`i` pairs in `R_a` that are not inside one of the predecessor-label classes `S_b`. The term `Q_i` matters: concentrated holes reduce this number, so it is not valid to replace the identity by `x_i+(a-1)z_i+1` without a correction.

### Lemma 10.1 — two-label product obstruction

Let `v in Z_i` duplicate color `i` at two distinct vertices `b,c in B`. Define

`A_b(v)=N_{F_i}(v) intersect S_b`, `A_c(v)=N_{F_i}(v) intersect S_c`,
`d_b(v)=|A_b(v)|`, `d_c(v)=|A_c(v)|`.

Then:

1. every pair in `A_b(v) x A_c(v)` is a color-`i` edge, so these pairs are counted by `M_i`;
2. `d_b(v)+d_c(v)<=a`;
3. the color-`i` edges from `v` to `S_b union S_c` number exactly `(s_b-d_b(v))+(s_c-d_c(v))`.

**Proof.** For any `u in S_b` and `w in S_c`, the set

`(B minus {b,c}) union {v,u,w}`

has `r+1` vertices. None of its edges to `B minus {b,c}` has color `i`; the only possible color-`i` edges in the set are among `v,u,w`. The balanced-coloring property forces at least one of `vu,vw,uw` to have color `i`. Therefore, if `u in A_b(v)` and `w in A_c(v)`, the first two edges are not color `i`, so `uw` must be color `i`. This proves (1). The sets `A_b(v)` and `A_c(v)` are each independent in `F_i`, and by (1) all cross pairs are absent from `F_i`; hence their union is independent in `F_i`. Since `alpha(F_i)=omega(G_i)<=a`, (2) follows. Statement (3) is the definition of `A_b,A_c`. `\square`

### Corollary 10.2 — a per-color duplicate-incidence inequality

Let `L_i` be the multigraph on `B` whose `z_i` edges are the duplicated label pairs of vertices in `Z_i`; let `deg_{L_i}(b)` count multiplicity. Then

`H_i >= a z_i - sum_b h_b deg_{L_i}(b) >= z_i(a-z_i+1)`

whenever the rightmost bound is positive.

**Proof.** Sum item (3) over all `v in Z_i`; the counted pairs are distinct because they have different endpoints `v`. By item (2), each summand is at least `s_b+s_c-a= a-h_b-h_c`. Summing over duplicated label pairs gives the first inequality. Since `deg_{L_i}(b)<=z_i` and `sum h_b=z_i-1`,

`sum_b h_b deg_{L_i}(b)<=z_i(z_i-1)`,

which gives the second inequality. `\square`

Combining this with (EL) gives the further necessary bound

`M_i+K_i <= x_i - z_i + 1 - Q_i + sum_b h_b deg_{L_i}(b)`

and hence the coarser bound

`M_i+K_i <= x_i + (z_i-1)^2 - Q_i`.  (MK)

For `a=6`, `z_i=6`, `x_i=5`, and a single class of size one (`Q_i=binom(5,2)=10`), (EL) reads `M_i+H_i+K_i=26`; (H) gives `H_i>=6`; and (MK) gives `M_i+K_i<=20`. The Kang–Pikhurko extremal construction attains this local budget with `H_i=6`, `M_i=5`, `K_i=15`. Thus the case `z_i=6` cannot be discarded by assuming that every color has `z_i=1`.

### Corollary 10.3 — sharpened one-duplicate excess inequality

If `z_i=1`, then every class has size `a`, `Q_i=0`, and `K_i=0`. For the unique duplicated vertex `v` with labels `b,c`, write `d_b=d_b(v)`, `d_c=d_c(v)`. Then

`x_i >= a-1 + (d_b-1)(d_c-1)`.  (OD)

In particular, if `x_i=a-1`, then `d_b=1` or `d_c=1`.

**Proof.** By Lemma 10.1, `M_i>=d_bd_c` and `d_b+d_c<=a`. By (EL), `M_i+H_i=x_i+a`. Also

`H_i=(a-d_b)+(a-d_c)`.

Therefore

`x_i+a = M_i+H_i >= d_bd_c+2a-d_b-d_c`

`=2a-1+(d_b-1)(d_c-1)`,

which proves (OD). `\square`

### Counterexample / dependency audit

- These statements do **not** follow from the scalar excess ledger alone; Lemma 10.1 uses the exact `r+1`-set predecessor interface, and (EL) uses the actual class sizes.
- The local Kang–Pikhurko extremal graph is a genuine `K_{r+1}`-free non-`r`-partite graph attaining `x_i=a-1`; its label-interface profile can have `z_i=a` and a class of size one. This is a per-color graph/interface model, **not** a full `r`-edge-coloring of the original `r^2+1`-vertex graph and not a counterexample to the Ramsey statement.
- Hence `z_i=1` cannot be assumed. The new inequalities are sharp on the known local extremal template and do not by themselves force a contradiction after summing over colors.
- The remaining structural question is whether the required two-label missing-bicliques and the `M_i,H_i,K_i` budgets can coexist **across all colors** with the target-group partition and its bounded hub kernel.

External extremal input for the sharp local template: Kang–Pikhurko, *Maximum K_{r+1}-free graphs which are not r-partite* (2005), Theorem 1 and Theorem 4/Lemma 5: https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf.

## 9. Aligning exact predecessor classes with Turán-stability partitions

The exact label classes `S_{i,b}` are not automatically the same as the parts supplied by Füredi stability. The following lemma proves that all but `O_a(r)` classes do align, globally across all non-target colors. This improves the earlier `r^2-O_a(r^(3/2))` partial-design bound to `r^2-O_a(r)`.

### Lemma 11.1 — alignment of full label classes

Fix a non-target color `i`. Let `P_{i,1},...,P_{i,r}` be the `r`-part partition of `F_i` supplied by Füredi stability. Write `I_i^*` for the number of `F_i` edges internal to its parts and `M_i^*` for the missing `F_i` cross-pairs. The established stability bounds give

`I_i^*<=x_i`, `M_i^*<=2x_i`.

Then the number of size-`a` label classes `S_{i,b}` that are not exactly equal to one of the parts `P_{i,j}` is at most

`2x_i/(a-1)+2x_i`.

**Proof.** First consider a size-`a` class `S=S_{i,b}` that meets at least two stability parts. Every pair of its vertices in different parts is a missing cross-pair of `F_i`, because `S` is independent in `F_i`. Any nontrivial split of `a` vertices creates at least `a-1` such pairs. Since distinct label classes are disjoint, their cross-part pairs are disjoint. Hence at most `M_i^*/(a-1)<=2x_i/(a-1)` full classes are split.

Now consider a full class `S` contained in one part `P`. If `|P|=a`, then `S=P`. Suppose `|P|>a`. If `P` contains exactly one full label class, every extra vertex `w in P\S` has at least one `F_i` edge to `S`; otherwise `S union {w}` would be an independent set of size `a+1`, contradicting `alpha(F_i)=omega(G_i)<=a`. Distinct such parts/classes charge distinct internal edges, so there are at most `I_i^*` of these classes.

If `P` contains `k>=2` disjoint full label classes `S_1,...,S_k`, then for every pair `S_j,S_l`, the bipartite graph of `F_i` edges between them has independence number at most `a` on `2a` vertices. Its minimum vertex-cover number is therefore at least `a`, so it has at least `a` edges. These edges are internal to `P`, and the edge sets for distinct pairs of label classes are disjoint. Thus `I_i^*>=a*binom(k,2)`. Since `k<=2*binom(k,2)` for `k>=2`, the number of full classes in all such parts is at most `2I_i^*/a`. Combining the two contained-but-not-equal cases gives at most `I_i^*+2I_i^*/a<=2x_i` classes. Adding the split-class count proves the lemma. `\square`

### Theorem 11.2 — a linear-defect partial resolvable `TD(a,r)`

For every fixed `a>=6`, for all sufficiently large `r`, any first `K_r`-free canonical stop `R_a` contains a pairwise-linear partial resolvable transversal design on its `a` target groups with

`r^2-O_a(r)`

blocks.

**Proof.** For each non-target color `i`, a class is clean if (i) it has size `a`, (ii) it equals one of the Füredi stability parts of `F_i`, and (iii) it is disjoint from the target hub set `X`. Such a class is a transversal of all `a` target groups: it is target-independent, and every group outside `X` is an actual target-color clique, so it contains at most one vertex from each group; its size is `a`.

The number of deficient classes of color `i` is at most `z_i-1`, by the exact hole identity. Lemma 11.1 bounds the number of full classes not aligned with a stability part by `2x_i/(a-1)+2x_i`. Since the `S_{i,b}` classes are disjoint, at most `|X|` classes of a fixed color meet `X`. Therefore the total number of non-clean classes across all `r-1` non-target colors is at most

`sum_{i>0}(z_i-1) + (2/(a-1)+2)sum_{i>0}x_i + (r-1)|X|`.

Now `sum_{i>0}(z_i-1)<= (a-1)r+2`, `sum_{i>0}x_i<=S_a(r)-x_0<=(binom(a,2)-2)r+a` by `x_0>=r`, and `|X|=O_a(1)` by the fixed-`a` hub theorem. The exception count is thus `O_a(r)`. There are `r(r-1)` label classes in total, so at least `r^2-O_a(r)` are clean.

Classes of a common color are disjoint. Classes of distinct colors share at most one vertex, because a pair cannot have two colors. Hence the clean classes form the claimed partial resolvable transversal design. `\square`

### Explicit `a=6` bound

For `a=6` and `r>=1000`, use `|X|<=74`, `sum_{i>0}x_i<=13r+6`, and `sum_{i>0}(z_i-1)<=5r+2`. The total number of non-clean classes is at most

`(5r+2) + (12/5)(13r+6) + 74(r-1) <= 111r`.

Therefore every first `K_r`-free `R_6` contains a pairwise-linear partial resolvable `TD(6,r)` with at least

`r^2-112r`

blocks for every `r>=1000`. This improves the earlier explicit `r^2-(29/2)r^(3/2)-67r` bound.

### Design-only countermodel — why the partial-TD bound is not a contradiction

For any prime power `r>=7`, the finite-field construction gives a `TD(6,r)` with `r^2` blocks and `r` parallel classes (restrict the standard field-based `TD(r+1,r)` to six groups). Delete one parallel class. The remaining `r^2-r` blocks form a pairwise-linear partial resolvable `TD(6,r)` with `r-1` parallel classes. Add one unused point to one group, giving group sizes `(r+1,r,r,r,r,r)` without changing the blocks.

For `r>=112`, this abstract design already exceeds the necessary lower bound `r^2-112r`. Thus the `r^2-O(r)` partial-design theorem, even with exact pairwise linearity and `r-1` resolvable classes, is not by itself contradictory.

**Scope warning:** this is a design-only model, not a full edge-coloring of `K_{r^2+1}` and not a graph satisfying the entire canonical high-stop contract. It does not check the excess ledger, the exceptional edge colors, or the full hereditary cap. Its role is to rule out the shortcut 'near-complete TD therefore impossible'; the missing contradiction must use the exceptional-block color/label incidence and the target hub structure.

### Limitation and adversarial audit

This is a stronger necessary structure, not a contradiction. The exceptional `O_a(r)` classes may carry all the non-extension obstruction; the theorem does not complete the design or show that an earlier `R_5` exists. A field-based `TD(6,r)` with one parallel class removed gives a design-only model with `r^2-r` blocks, so design density alone cannot close the gap. The proof uses only the existing Füredi stability bounds, the exact predecessor-label partition, `alpha(F_i)<=a`, and the bounded hub theorem. No fixed-`r` computation is promoted to an all-`r` result.

## 10. Hub-incidence slot budget: a 7-to-28 hub kernel

This section improves the hub localization by using the exact predecessor-label partitions. It is a necessary structural theorem, not a contradiction.

Let `V_1,...,V_6` be the target-stability groups in a first high-stop `R_6`, with `r-8<=s_j=|V_j|<=r+9` for `r>=22`. For each non-target color `i`, each label class `S_{i,b}` has size `s_{i,b}<=6`. Let `g_{i,b}` be the number of target groups it meets and define its missing-group-slot count

`m_{i,b}=6-g_{i,b}`.

Also set `h_{i,b}=6-s_{i,b}` and `c_{i,b}=s_{i,b}-g_{i,b}`. Then

`m_{i,b}=h_{i,b}+c_{i,b}`,
`sum_{i,b} h_{i,b}=sum_i(z_i-1)=5r+2-q_0<=5r+2`,
`sum_{i,b} c_{i,b}<=D<=x_0<=9r+11`,

where `D=sum_j e(F_0[V_j])` is the number of internal target-complement edges. The inequality `sum c<=D` holds because a class with multiplicities `t_1,...,t_6` contributes `sum(t_j-1)` to `c`, while its internal edges contribute `sum binom(t_j,2)>=sum(t_j-1)`; these internal pairs are disjoint across all color classes. Therefore the total missing-slot budget is

`W:=sum_{i,b}m_{i,b}<=14r+13`.  (WS)

### Lemma 12.1 — every hub consumes linearly many missing group slots

For each hub `x in X`, let `j(x)` be its target group and define

`W_x=sum_{i:x notin Z_i} m_{i,b_i(x)}`,

where `b_i(x)` is the unique predecessor label of `x` in color `i`. At most one color has `x in Z_i`. Then

`d_{C_0}(x)<=r+6-s_{j(x)}+5 1_{x in union_i Z_i}+W_x<=19+W_x`.

Consequently, for `r>=1000`,

`W_x>=(r-65)/2`.

**Proof.** Fix a target group `V_k` with `k!=j(x)`. For each non-target color `i` for which `x notin Z_i` and the class `S_{i,b_i(x)}` meets `V_k`, choose one vertex `y_i in S_{i,b_i(x)} intersect V_k`. The pair `xy_i` has color `i`; these chosen vertices are distinct for different colors because an edge has only one color. Thus `x` has at least

`(r-1-u_x)-m_{x,k}`

non-target neighbors in `V_k`, where `u_x=1` if `x in union_i Z_i` and `0` otherwise, and `m_{x,k}` counts the classes containing `x` that omit `V_k`. Therefore

`d_{C_0}(x,V_k)<=s_k-r+1+u_x+m_{x,k}`.

Summing over the five groups other than `V_{j(x)}` gives

`d_{C_0}(x)<=r+6-s_{j(x)}+5u_x+W_x<=14+5+W_x=19+W_x`.

Since `x` is a hub, `d_{C_0}(x)>=H_r/2>=(r-27)/2`; rearranging gives `W_x>=(r-65)/2`. `\square`

### Lemma 12.2 — multiple-hub classes have bounded total surcharge

Let `k_{i,b}=|S_{i,b} intersect X|`. Then

`sum_{x in X} W_x <= W+15|X|(|X|-1)`.

**Proof.** A class containing `k` hubs contributes `k m_{i,b}` to the left and `m_{i,b}` to `W`. If `k>=2`, then `k<=6`, `m_{i,b}<=6`, so the surcharge is at most `30`. A pair of hubs can share at most one label class over all colors, because that pair has only one edge color. Hence there are at most `binom(|X|,2)` classes containing at least two hubs, and the total surcharge is at most `30 binom(|X|,2)=15|X|(|X|-1)`. `\square`

### Theorem 12.3 — at most 28 hubs for sufficiently large `r`

For `a=6` and `r>=26272`,

`7<=|X|<=28`.

**Upper bound proof.** By Lemmas 12.1–12.2 and (WS),

`|X|(r-65)/2 <= 14r+13+15|X|(|X|-1)`.  (HK)

The previously proved hub cover gives `|X|<=74` for `r>=1000`. For `29<=|X|<=74`, the function

`f(k)=k(r-65)/2-15k(k-1)`

is increasing when `r>=26272`. At `k=29`, `f(29)>14r+13` for `r>=26272`, contradicting (HK). Thus `|X|<=28`.

**Lower bound proof.** Put `delta_j=s_j-r`, so `sum_j delta_j=1`. Since `G_0[R_6]` is `K_r`-free, `alpha(F_0[V_j])=omega(G_0[V_j])<=r-1`. Hence the minimum vertex-cover number of `F_0[V_j]` is at least `s_j-r+1=delta_j+1` whenever `delta_j>=0`. Every internal `F_0` edge meets `X`, so `X intersect V_j` is a vertex cover of `F_0[V_j]`. If `N` is the set of groups with negative `delta_j`, then

`|X|>=sum_{j:notin N}(delta_j+1)=7+sum_{j in N}(-delta_j)-|N|>=7`.

Thus the hub kernel is nonempty and in fact has between 7 and 28 vertices for `r>=26272`. `\square`

### Corollary 12.4 — sharpened linear-defect partial design

For `a=6,r>=26272`, the number of non-clean predecessor classes is at most

`(5r+2)+(12/5)(13r+6)+28(r-1)<=65r`.

Therefore a first high stop contains a pairwise-linear partial resolvable `TD(6,r)` with at least

`r^2-66r`

clean blocks.

### Scope and adversarial audit

- The theorem is independent of the earlier `z_i=1` special case; it uses every color's exact label partition and permits arbitrary `z_i>=1`.
- The upper bound counts missing group slots, not merely non-clean classes. The multiple-hub correction is necessary and is controlled by pairwise uniqueness of edge colors.
- The lower bound `|X|>=7` uses only `K_r`-freeness of the target color and the fact that every internal target-complement edge meets `X`.
- This does **not** contradict a high stop. A design-only TD with one parallel class deleted has `r^2-r` blocks and still exceeds `r^2-66r`; the remaining blocker is the exceptional classes' color/label incidence.

## 9. Status ledger for this round

### PROVED

- At least `floor(r/2)` non-target colors are within `a^2-1` edges of the exact Turán maximum in the complement.
- Uniform edit-distance partition stability and the global near-resolvable design are proved via Füredi.
- The critical-core polynomial confines fixed-`a` residues to explicit bounded-width windows for `r>=R_a`.
- The predecessor label-capacity lemma proves `z_i>=1` for every non-target color, with exact class-hole identity.
- The exact predecessor-label defect identity, two-label product obstruction, and stability-part alignment lemma are proved.
- Every fixed-a high stop contains a pairwise-linear partial resolvable `TD(a,r)` with `r^2-O_a(r)` blocks; for `a=6,r>=1000`, at least `r^2-112r` blocks are forced.
- For fixed `a`, target groups have absolute width and every internal target-complement edge is incident to at most `4M_0/H_r` hubs; after Brouwer tightening, for `a=6` at most 74 hubs suffice for `r>=1000`.
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

The critical-core potential has reduced the (a=6) case to four explicit residue windows. Any high stop forces a pairwise-linear partial resolvable `TD(6,r)` with at least `r^2-112r` blocks and a hub kernel of size at most 74 for `r>=1000`. The linear-defect theorem aligns all but `O_a(r)` predecessor classes with stability parts. This is a strong necessary structure, but no design-completion or earlier-stop theorem is proved; `NO-HIGH-STOP` remains open. The scalar and local KP countermodels show why neither scalar-only inequalities nor assuming `z_i=1` will suffice. The next highest-leverage step is to classify the `O(r)` exceptional blocks jointly across colors and derive a contradiction from their incidence with the hub kernel..