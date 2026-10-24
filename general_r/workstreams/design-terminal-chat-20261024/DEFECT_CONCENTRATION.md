# Constant-width target groups and defect concentration

This file strengthens the first-pass `O(r)` stability result. It uses only the terminal contract, the hereditary density caps, Furedi stability, and the product-cover argument.

## H1. Constant-width target groups

Status: **PROVED_ANALYTIC**.

Let `F=G_0[W]` be the target graph on `|W|=5r+1`. Let

`Q_0=K(B_1) union ... union K(B_5)`

be the five-clique ideal supplied by Furedi stability. Put

- `a_j=|B_j|`, so `sum a_j=5r+1`;
- `D=|E(Q_0)\E(F)|`, the number of ideal internal edges deleted from the target;
- `A=|E(F)\E(Q_0)|`, the number of target cross-group additions.

From Furedi and the total slack identity,

> `A+D <= 3s_0 <= 27r+15`.  (H-EDIT)

For each target ideal group `B_j`, the hereditary cap gives

`e_F(B_j) <= C(a_j,2)-(r-1)p_r(a_j)`.

Since `Q_0[B_j]` is complete,

`D_j >= (r-1)p_r(a_j)`.

The elementary component bound `p_r(a)>=max(0,a-r)` yields

> `D >= (r-1) P`, where `P=sum_j (a_j-r)_+`.  (H-DEL)

Combining with (H-EDIT),

`P <= (27r+15)/(r-1)=27+42/(r-1)`.

Hence for every `r>=44`, integer `P<=27`. Since

`sum_j(a_j-r)=1`,

the total negative deviation is `P-1<=26`. Therefore every target ideal group satisfies

> **`r-26 <= |B_j| <= r+27` for all `r>=44`.**

This improves the earlier `r+O(sqrt r)` energy conclusion to an absolute-width statement.

### Interpretation

The hereditary cap is doing essential work: an oversized target ideal clique of size `r+t` cannot be repaired by only `O(t)` missing target edges. It needs at least `(r-1)t` missing target edges because each of the other `r-1` colors must satisfy its own independence constraint inside the group.

## H2. Refined cylinder degree inequality

Status: **PROVED_ANALYTIC**.

Let `uv` be any deleted target edge inside one target ideal group `B_i`. Let `C` be the target cross-edge graph with edge set `E(F)\E(Q_0)`, so `e(C)=A`.

For each choice of one point from each of the other four groups, the resulting six vertices together with `u,v` cannot be target-independent. Therefore some target cross edge among those six vertices must hit every tuple.

Let

`L_i=min_(j!=i)|B_j|`.

An edge incident with `u` or `v` covers at most a `1/L_i` fraction of the tuple space. A target cross edge whose endpoints both lie among the other four groups covers at most a `1/L_i^2` fraction. By the union bound,

`1 <= (d_C(u)+d_C(v))/L_i + A/L_i^2`.

Thus

> `d_C(u)+d_C(v) >= L_i-A/L_i`.  (H-CYL)

For `r>=44`, H1 gives `L_i>=r-26`. Hence every deleted internal target edge obeys

> `d_C(u)+d_C(v) >= H_r`,

where

`H_r := (r-26) - (27r+15)/(r-26)`.

For `r>=70`, `H_r>0`, and asymptotically `H_r=r-53+o(1)`.

## H3. Bounded hub cover for all target internal deletions

Status: **PROVED_ANALYTIC**.

Assume `r>=70`. Define the high cross-degree set

`X={v in W : d_C(v)>=H_r/2}`.

By (H-CYL), every deleted internal target edge has at least one endpoint in `X`. Therefore:

> **`X` is a vertex cover of every target internal deletion inside all five ideal groups.**

Since the total cross degree is `2A`,

`|X| H_r/2 <= 2A`.

Therefore

> `|X| <= 4A/H_r <= 4(27r+15)/H_r = 108+o(1)`.

For example, the explicit bound gives `|X|<=114` for every `r>=1000`.

Equivalently, outside a bounded exceptional hub set, each target ideal group is an **actual target clique**:

> `F[B_j\X]` is complete for every `j`.

The terminal clique cap then gives

> `|B_j\X|<=r-1` for every target group.

## H4. Matching formulation

Status: **PROVED_ANALYTIC**.

Let `M` be the graph whose edges are all internal target deletions, i.e. the disjoint union over the five groups of `Q_0[B_j]\F[B_j]`.

If `M` has a matching of size `mu`, summing (H-CYL) over its pairwise-disjoint endpoints gives

`mu H_r <= 2A`.

Hence

> `mu <= 2(27r+15)/H_r = 54+o(1)`.

The endpoints of a maximal matching form a vertex cover of `M`, giving the same constant-size concentration phenomenon up to a factor 2.

## H5. Consequence for the design-terminal programme

The first stability pass left `O(r)` exceptional block incidences and, a priori, allowed target corrections to touch all `5r+1` vertices. H1--H4 rule out that possibility for the target internal layer:

> for sufficiently large `r`, all target internal defects are forced through `O(1)` high cross-degree hubs, while the five target groups themselves have sizes `r+O(1)`.

Thus a surviving terminal has the schematic form

`constant exceptional hub kernel + almost exact five-group transversal design on the ordinary vertices`.

This is a strictly stronger rigidity statement than generic Turan stability.

## Remaining gap

The theorem does **not** yet show that the `O(r)` bad non-target ideal blocks or all ideal-pair multiplicity defects also meet the same hub set. Proving that propagation is the next high-leverage target. If successful, the terminal would reduce to a finite exceptional kernel attached to an exact large `TD(5,r)` core, where the existing nonextension mechanisms become much more plausible.
