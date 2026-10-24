# Canonical state — general-r residual-core extraction

Workstream branch: `workstream/general-r-residual-core-extraction-20261024`

Directory: `general_r/workstreams/residual-core-extraction-chat-20261024/`

Last major mathematical state: 2026-10-24.

## PROVED

### 1. R12 provenance map

Status: `PROVED_SYMBOLIC` / `SOURCE_REPORTED`.

- `r^2+1`, `5r+1`, `4r+1`, `3r-1`, `r+1` are genuinely structural orders.
- The r=12 proof of residual minimum degree depends on lower-order Ramsey seeds and is not itself an all-r proof.
- File: `R12_TO_GENERAL_DEPENDENCY_MAP.md`.

### 2. Outer-ray invariant and trimming normalization

Status: `PROVED_SYMBOLIC`.

For anchor degree `d=r-s`, after `j` extracted `K_r` blocks with `a=r-1-j`,

`n=ar+s`, so `n-ra=s` is invariant.

Induced-subgraph averaging collapses every `s>=1` state to the critical `s=1` state `ar+1` without worsening the canonical edge budget.

Files:

- `OUTER_RAY_INVARIANT.md`;
- `ANCHOR_NORMALIZATION_AND_GREEDY_EXTRACTION.md`.

### 3. Minimum-degree anchor source

Status: `PROVED_ANALYTIC`.

For `r>=3`, the least-color graph has a minimum-degree anchor with `d<=r-1`.

Proof: averaging plus Brooks; `delta>=r` would make the graph r-regular while `alpha<=r` forces chromatic number at least `r+1`.

### 4. General residual-core minimum degree — LEVEL A

Status: **`PROVED_ANALYTIC`**.

For every `r>=17`, any graph `H` on `3r-1` vertices satisfying

- `alpha(H)<=3`;
- `omega(H)<=r-1`;
- the inherited least-color hereditary cap

must satisfy

> **`delta(H)>=r`.**

Key chain:

- exact `2r` exclusion;
- boundary `d=r-1` compressed to a non-bipartite triangle-free graph on `2r-1` with edge count `(r-1)^2` or `(r-1)^2+1`;
- shortest odd cycle forced to `C5`;
- remainder forced to one of three near-complete-bipartite forms;
- hereditary cap gives every boundary row defect at most 8;
- any complement edge inside the `r-1` neighbor set requires two row defects summing to at least `r`;
- clique cap forces such an edge;
- contradiction for `r>=17`.

File: `CORE_MINDEG_BOUNDARY_THEOREM.md`.

External inputs: Andrasfai--Erdos--Sos and the classical Erdos non-bipartite triangle-free edge bound.

### 5. Full 4r+1 residual branch

Status: **`PROVED_ANALYTIC`** for `r>=17`.

Any induced `F` on `4r+1` vertices satisfying

- `alpha(F)<=4`;
- `omega(F)<=r-1`;
- hereditary cap

automatically has

> `delta(F)=r+1`.

Hence it has a degree-`(r+1)` pivot `p`, and

`H=F-N[p]`

satisfies the complete residual-core contract

`|H|=3r-1`,
`alpha(H)<=3`,
`omega(H)<=r-1`,
`delta(H)>=r`.

File: `RESIDUAL_BRANCH_CLOSURE.md`.

### 6. Canonical greedy block extraction

Status: `PROVED_SYMBOLIC` plus `PROVED_ANALYTIC` for the low end when `r>=17`.

After anchor normalization, states have

`|R_a|=ar+1`,
`alpha(R_a)<=a`,
`e(R_a)<=B_a=r((a+1)r-a+1)/2`.

If `R_a` contains a target-color `K_r`, deleting it yields the next canonical state `R_{a-1}`.

For `r>=17`, a canonical process cannot pass below `a=4`; reaching `R_4` forces it to be `K_r`-free and therefore gives the residual branch.

### 7. Recurrence-replacement scalar potentials

Status: `PROVED_SYMBOLIC` / `PROVED_ANALYTIC`.

File: `RECURRENCE_REPLACEMENT_POTENTIALS.md`.

#### Exact all-colour excess ledger

For a canonical state on `ar+1` vertices, if `x_0` is the target-colour excess above `p_a` and `x_i` are the other colours' excesses above `p_r`, then

> `x_0 + sum x_i = S_a(r)`

with

> `S_a(r)=[a(a-1)r+2a-2r]/2`.

Moreover

`S_a-S_{a-1}=(a-1)r+1`.

This is a genuine all-r scalar potential replacing much of the recurrence bookkeeping.

#### Alpha saturation

Every canonical state has

> `alpha(R_a)=a`,

not merely `<=a`.

#### Critical-core potential

Every canonical stop contains an induced `(r+1)`-critical graph `Q`. At a `K_r`-free stop,

> `|Q|>=3r-1` for `r>=4`.

Writing `|Q|=lr+t`, `0<=t<r`, compatibility with the hereditary cap and the Kostochka--Yancey critical-graph bound is exactly one scalar inequality

`P_{l,t}(r)<=0`

recorded in `RECURRENCE_REPLACEMENT_POTENTIALS.md`.

### 8. Exact 5r+1 terminal

Status: `PROVED_SYMBOLIC` as a terminal definition/reduction.

If the first `K_r`-free canonical stop is `a=5`, then `T_r` has

- `5r+1` vertices;
- **`alpha(T_r)=5`**;
- `omega(T_r)<=r-1`;
- hereditary cap;
- `e(T_r)<=3r^2-2r`;
- no `K_r`.

If irreducible to Branch A, the independent-5 hypergraph has transversal number at least `r+1`, `delta(T_r)>=r`, and every degree-r row satisfies an explicit independent-4 witness condition.

File: `FIVE_R_TERMINAL.md`.

### 9. High-stop excess concentration

Status: **`PROVED_SYMBOLIC`**.

For any first stop with `a>=6`, define

`C_{a,r}=ceil(2 S_a(r)/(r-1))`.

At least `floor(r/2)` non-target colors satisfy

`x_i<=C_{a,r}<=a^2-1`.

Equivalently, at least half of the non-target complements are `K_{r+1}`-free graphs within `a^2-1` edges of the exact Turán maximum.

For `a=6`, `S_6=14r+6); for `r>=41), at least `floor(r/2)` non-target colors have `x_i<=29`.

File: `NO_HIGH_STOP_ROUND2_LEMMAS.md`.

**Round-2 refinement:** the following section upgrades edge-count concentration to a uniform edit-distance / partition stability theorem and a global near-resolvable design.

### 9A. Uniform partition stability and global near-resolvable design

Status: **`PROVED_ANALYTIC`**, conditional only on the already-established exact excess ledger and Füredi's quantitative Turán theorem.

For each color i, the complement F_i is K_{k_i+1}-free with exact Turán deficit x_i, where k_0=a and k_i=r for non-target colors. Füredi's theorem gives a k_i-partition with at most x_i internal edges to delete. If I_i is the internal-edge defect, M_i the missing cross-pair defect, and Delta_i the part-size imbalance, then

`I_i<=x_i`, `Delta_i+M_i=x_i+I_i<=2x_i`, and `I_i+M_i<=3x_i`.

Since the balanced part sizes are q+1 once and q otherwise (q=r for the target partition, q=a for non-target partitions), the actual part sizes s_j obey

`sum_j (s_j-q)^2<=4x_i+1`.

Summing over all colors and using `sum_i x_i=S_a(r)`, at most `3S_a(r)` vertex pairs fail to be represented by exactly one block of their actual color and by no block of any other color. Thus the target a-partition and the r-1 non-target r-partitions form a global approximate pairwise-balanced/resolvable design with O(a^2 r) bad pairs among O(a^2 r^2) total pairs.

File: `NO_HIGH_STOP_ROUND2_LEMMAS.md`.

External theorem: Füredi's quantitative Turán stability bound, recalled in Balogh–Clemen–Lavrov–Lidický–Pfender (2021), DOI 10.1017/S0963548320000590.

**Limitation:** this is a near-resolvable design with O(r) exceptional pairs, not an exact design and not yet an earlier-stop theorem.

### 9B. Brouwer-tightened target groups and cylinder hub localization

Status: **`PROVED_ANALYTIC`** for every fixed `a>=6`, conditional on the exact high-stop contract; for `a=6`, the improved numerical bounds hold for `r>=22` and the hub bound below for `r>=1000`.

The non-partite Turán bound gives the simultaneous color floors `x_0>=r` and `x_i>=a-1` for every non-target color. The target floor uses the Kang–Pikhurko equality classification to rule out equality at `x_0=r-1`; the non-target floor is Brouwer's bound and may be attained.

Combining the floors with `sum_i x_i=S_a(r)=(binom(a,2)-1)r+a` yields

`x_0<=(binom(a,2)-a)r+2a-1`,
`sum_{i>0}(x_i-(a-1))<=(binom(a,2)-a-1)r+2a-1`.

For `a=6`,

`x_0<=9r+11`,
`sum_{i>0}(x_i-5)<=8r+11`.

Let `F_0=bar(G_0[R_a])`. Füredi's partition has internal-edge count `D<=x_0`, missing cross-pair count `M_0<=2x_0`, and balanced-part imbalance `Delta`. For a target ideal group `V_j` of size `s_j`, the hereditary cap gives

`e(F_0[V_j])=sum_{i>0}e(G_i[V_j]) >= (r-1)(s_j-r)_+`.

Writing `C=binom(a,2)` and `P=sum_j(s_j-r)_+`, we obtain `(r-1)P<=D<=x_0`. For `r>=C+a+1`,

`r-C+a+1<=s_j<=r+C-a`.

For `a=6`, this sharpens the group range to **`r-8<=s_j<=r+9`** for `r>=22`.

Let `C_0` be the target-color graph crossing distinct ideal groups and `L=min_j s_j`. For every internal edge `uv` of `F_0`, the product-cover argument gives

`d_{C_0}(u)+d_{C_0}(v)>=L-M_0/L`.

Set `H_r=L-M_0/L` and `X={v:d_{C_0}(v)>=H_r/2}`. If `H_r>0`, every internal target-complement edge meets `X`, and `|X|<=4M_0/H_r`.

For `a=6`, `L>=r-8` and `M_0<=18r+22`. For `r>=1000`, `M_0/L<=19`, so `H_r>=r-27` and

`|X|<=4(18r+22)/(r-27)<75`.

Thus **at most 74 hubs suffice for `a=6, r>=1000`**, improving the previous bound 116.

File: `NO_HIGH_STOP_ROUND2_LEMMAS.md`.

**Limitation:** the sharper hub and group-size bounds still do not prove that the non-target block defects share the same kernel or that the high stop is impossible.

### 9C. Exact predecessor label-capacity structure

Status: **`PROVED_SYMBOLIC`**.

For every non-target color `i`, let `z_i` count vertices whose cross-edges to the predecessor target clique `B=K_r` duplicate color `i`. Then

`z_i>=1`, `sum_i z_i>=r-1`, and `q_0<=(a-1)r+2`,

where `q_0` is the number of target-color edges from `R_a` to `B`.

Proof: for each `b in B`, vertices whose unique color-`i` edge to `B` goes to `b` form a color-`i` clique. Indeed, for any pair `u,v` in that class, the `r+1` vertices `(B\\{b}) union {u,v}` already exhibit every color except possibly `i`, so `uv` must have color `i`. The class is therefore target-independent and has size at most `alpha(G_0[R_a])=a`. There are `r` such classes, while `n-z_i=ar+1-z_i` vertices have a unique color-`i` edge, forcing `z_i>=1`.

More exactly, if these classes are `S_{i,b}`, then

`sum_{b in B}(a-|S_{i,b}|)=z_i-1`.

So each non-target color partitions all but `z_i` vertices into `r` exact monochromatic cliques of size at most `a`; when `z_i=1`, all `r` classes have size exactly `a`.

File: `NO_HIGH_STOP_ROUND2_LEMMAS.md`.

Combining `sum_i z_i<=6r+1`, the exact hole identity, and `|X|<=74`, at least `r-1-sqrt(r)/2` colors have at least `r-14sqrt(r)-73` clean size-6 transversal blocks. Hence for `r>=1000` the high stop contains a pairwise-linear partial resolvable `TD(6,r)` with at least

`r^2-(29/2)r^(3/2)-67r`

blocks. This sharpens the previous explicit `r^2-O(r^(3/2))` bound; it remains a near-design, not an exact TD or contradiction.

### 9D. Brouwer excess vector and scalar-feasibility audit

Status: **`PROVED_ANALYTIC`** for the all-color floors; **`ABSTRACT_PARAMETER_COUNTERMODEL`** for the numerical audit (not a graph counterexample).

At an exact high stop, `F_0=bar(G_0)` is non-`a`-partite and `K_{a+1}`-free. Brouwer gives `x_0>=r-1`; the Kang–Pikhurko equality classification gives an independent set of size at least `r` in an equality graph, so the terminal cap `omega(G_0)<=r-1` strengthens this to `x_0>=r`.

For every non-target `i`, `F_i=bar(G_i)` is non-`r`-partite and `K_{r+1}`-free: `omega(G_i)<=a` because color-`i` cliques are target-independent, so an `r`-partite `F_i` would have at most `ar` vertices. Brouwer therefore gives `x_i>=a-1`.

Consequently the excess above these individual floors satisfies

`sum_{i>0}(x_i-(a-1))<=(binom(a,2)-a-1)r+2a-1`.

For `a=6`, the upper bound is `8r+11`. The explicit abstract assignment in `NO_HIGH_STOP_ROUND2_LEMMAS.md` satisfies the exact excess ledger, predecessor increments, target partition identity, stability budgets, hub-count bound, and cross-pair count. It is **not** a real graph or coloring certificate; it shows only that these scalar constraints cannot by themselves close `NO-HIGH-STOP`.

An additional audit shows that for fixed `a>=6`, `alpha(G_0)=a` is automatic once `r>=a^2` (and for `a=6`, once `r>=24`): otherwise `e(G_0)>=p_{a-1}(ar+1)`, but the elementary bound `p_{a-1}-p_a >= (ar+1)^2/(2a(a-1))-a/8` exceeds the entire excess budget `S_a(r)`. This threshold is not uniform when `a` grows with `r`.

File: `NO_HIGH_STOP_ROUND2_LEMMAS.md`.

### 10. Critical-core residue windows

Status: **`PROVED_ANALYTIC`** as a necessary-condition reduction.

For `q=lr+t`, `0<=t<r`, if `r>=R_l=l(l-1)^2(l-2)+2l+2` and `P_{l,t}(r)<=0), then

`t<=l^2-3l+1` or `r-t<=l^2-l-1`.

For fixed `a`, this confines the critical-core order to bounded-width windows around multiples of `r`. In the `a=6` case, `R_6=614), and the only necessary candidate windows are

`[3r-1,3r+1] U [4r-5,4r+5] U [5r-11,5r+11] U [6r-19,6r+1]`

for `r>=614`.

These windows exclude every middle-residue regime, but do not by themselves eliminate the remaining regimes.

File: `NO_HIGH_STOP_ROUND2_LEMMAS.md`.

### 11. First-stop predecessor interface

Status: **`PROVED_SYMBOLIC`**.

If `B=K_r` is the target clique deleted from predecessor `R_{a+1}) to obtain the first stop `R_a`, then each `v in R_a` has either:

- exactly one target-color edge to `B), and every non-target color occurs exactly once on `vB); or
- no target-color edge to `B), and exactly one non-target color is duplicated on `vB).

If `q_0` is the number of target cross-edges and `z_i` counts vertices whose duplicated non-target color is `i), then

`sum z_i=ar+1-q_0`,
`x_0(R_{a+1})=x_0(R_a)+q_0`,
`x_i(R_{a+1})=x_i(R_a)+z_i`.

Thus each color excess is monotone when moving backward one canonical step, with exact total increment `S_{a+1}-S_a=ar+1`.

File: `NO_HIGH_STOP_ROUND2_LEMMAS.md`.

## CONDITIONAL

### Complete desired front-end dichotomy

Status: `PROVED_CONDITIONAL` on the NO-HIGH-STOP lemma.

For `r>=17`, if the first `K_r`-free canonical greedy stop cannot occur at `a>=6`, then every hypothetical counterexample yields exactly:

- Branch A: a `4r+1` residual with the fully proved `3r-1` core contract; or
- Branch B: the exact irreducible `5r+1` terminal.

No backend d2/d3/support theorem is used.

## OPEN

### Single highest-leverage blocker

> **NO-HIGH-STOP LEMMA.** For all sufficiently large `r`, a first `K_r`-free canonical state cannot occur at `a>=6`.

This remains open. Specifically:

- `a=6) has **not** been closed;
- no induction/trim theorem is known for arbitrary `a>=7);
- uniform edit-distance partition stability is proved via Füredi, target ideal groups have absolute width, and fixed-a target-complement defects localize to O(a^2) hubs; Brouwer floors now sharpen the excess vector, but the scalar-feasibility audit shows that joint incidence analysis and design trimming remain open;
- approximate orthogonality, an exact resolvable-design skeleton, and a design-trimming implication are not proved.

The blocker is now a precise structural problem. Any high-stop candidate must simultaneously satisfy:

1. exact alpha saturation `alpha=a`;
2. the exact all-colour excess ledger `S_a(r)`;
3. a `K_r`-free target color;
4. a large `(r+1)`-critical core whose order passes `P_{l,t}(r)<=0`;
5. at least half the non-target colors are within `a^2-1` edges of their Turán extremum;
6. the exact predecessor-interface near-permutation condition;
7. the full hereditary cap on every induced subgraph.

Secondary open questions:

- lower the current `r>=17` threshold in the core theorem;
- decide whether the irreducible `5r+1` terminal exists;
- turn the bounded hub set into a hub-propagation theorem / earlier-stop extraction;
- exploit the label-capacity lemma `z_i>=1` for every non-target color in each predecessor interface.

## DISPROVED

No mathematical theorem has been marked `DISPROVED` in this workstream.

Rejected proof shortcuts:

- substituting `r` into the r=12 47/48-vertex edge seeds;
- claiming r=12 recurrence certification proves all-r extraction;
- assuming `delta(H)>=r` without the analytic theorem;
- treating numerical matching at r=12 as symbolic provenance;
- treating near-Turán edge count alone as proof of an exact partition/design.

## NEXT HIGHEST-LEVERAGE TARGET

Prove a **joint incidence-packing / hub-propagation lemma** for `a=6`: use the sharpened part sizes `r-8` through `r+9`, at most 74 hubs for `r>=1000`, the excess floors `x_i>=5`, `x_0>=r`, and the exact `z_i` label classes. The scalar parameter audit passes, so the next proof must exploit the equality/small-defect structure of the Brouwer extremal templates and its alignment with the predecessor classes; do not try another scalar-only contradiction. Show either that these hubs force an earlier `R_5` satisfying the edge budget, or that their incidence pattern contradicts the critical-core residue windows. Do not return to fixed-r recurrence or claim NO-HIGH-STOP closed before a proof exists.
