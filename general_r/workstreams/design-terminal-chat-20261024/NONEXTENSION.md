# Nonextension route

## N0. Exact affine-plane nonextension already available

Status: **PROVED_ANALYTIC upstream**.

The architecture already proves: whenever the standard affine-plane coloring on `r^2` points exists, it cannot be extended by one vertex while preserving the property that every `(r+1)`-set sees all colors.

The abstract form only needs two colors whose old color graphs are exact orthogonal partitions into `r` copies of `K_r`.

This remains the ideal endgame if the terminal stability can be upgraded to exact orthogonal partitions.

## N1. Target clique-cap deletion floor

Status: **PROVED_ANALYTIC**.

Let `Q_0` be any ideal target clique partition into five groups `B_1,...,B_5`, with sizes summing to `5r+1`. Since the actual target graph has clique number at most `r-1`, inside each `B_j` some ideal clique edges must be deleted.

Let `D_j` be the missing-edge graph inside `B_j`. Then

`alpha(D_j)=omega(G_0[B_j])<=r-1`.

Any graph on `a` vertices with independence number at most `r-1` has at least `a-(r-1)` edges when `a>r-1`: a graph with `e` edges has at least `a-e` connected components, and one point from each component is independent.

Therefore the number of internal target deletions is at least

`sum_j max(0,|B_j|-(r-1)) >= (5r+1)-5(r-1)=6`.

So an exact five-clique target partition is impossible; at least six internal corrections are mandatory.

## N2. Product-cover / cylinder lemma

Status: **PROVED_ANALYTIC**.

Let `B_1,...,B_5` be any partition, and suppose `u,v in B_1` but `uv` is absent from the target graph. Assume `alpha(target)<=5`.

For every tuple

`(x_2,x_3,x_4,x_5) in B_2 x B_3 x B_4 x B_5`,

the six vertices `{u,v,x_2,x_3,x_4,x_5}` must contain some target edge. Since `uv` is absent and the tuple contains only one point from each other group, that edge must be a **cross-group target edge** among these six vertices.

Put `P=prod_(j=2)^5 |B_j|` and `L=min_(j=2)^5 |B_j|`. A cross edge incident with `u` or `v` and one point of `B_j` covers at most `P/|B_j|<=P/L` tuples; an edge between two of `B_2,...,B_5` covers fewer. The tuple space has `P` points. Hence

> at least `L` cross-group target edges are required.

In particular, for the Furedi target partition from the stability theorem,

`L >= r-sqrt(72r+41)`,

so every internal deletion forces a linear-size cross-edge correction for sufficiently large `r`.

### Equality structure in the equal-group case

If `|B_2|=...=|B_5|=L` and exactly `L` cross edges cover all tuples, every edge must be maximally efficient. Hence every cover edge is incident with `u` or `v` and a point in one fixed group `B_j`; the `L` resulting cylinders must be disjoint and exhaustive. Equivalently, for every `x in B_j`, exactly one of `ux,vx` is a target edge.

Thus minimum correction has a rigid one-coordinate **two-owner star** form.

This is a robust symbolic analogue of the small-r correction-allowance patterns, but it is derived without importing their casework.

## N3. Naive `RTD(5,r)+one point` terminal is impossible

Status: **PROVED_ANALYTIC** for `r>=6`, conditional only on the existence of the stated RTD template.

Consider the most natural exact-design attempt:

1. start from a resolvable `TD(5,r)` on five groups of size `r`, with `r` parallel classes;
2. use `r-1` parallel classes as the non-target colors;
3. add a new point `infinity` to one block of each used class, producing one 6-block and `r-1` 5-blocks in each non-target color.

For edge-disjoint color classes, the `r-1` selected old 5-blocks enlarged by `infinity` must be pairwise disjoint; otherwise the same edge `infinity-v` receives two colors. They therefore leave exactly five old points, one in each group.

This attempt fails twice.

### Immediate clique obstruction

Every original group is a target `K_r`, contradicting the terminal cap `omega(target)<=r-1`.

### Independent-six obstruction even if the clique cap is ignored

Omit the unused parallel class. Label each point by its block in that omitted class. In each group only the one leftover point is forbidden, leaving `r-1` available omitted-class labels. For `r>=6`, five sets each of size `r-1>=5` have a system of distinct representatives. Choose one available point from each group with five distinct omitted-class labels.

No pair among these five points lies in the omitted parallel class; all their cross-pairs lie in used non-target classes. Their edges to `infinity` are also non-target because none is leftover. Hence these five points together with `infinity` form a target-independent 6-set, contradicting `alpha(target)<=5`.

So the obvious exact resolvable-design completion is not a hidden infinite family of legal terminals.

## N4. Current nonextension frontier

The terminal is now known to be `O(r)` block-defect away from a partial resolvable `TD(5,r)`, while the simplest exact completion is impossible. What is still missing is a robust theorem saying that the allowed `O(r)` defects cannot repair both:

- the mandatory target clique-cap deletions; and
- the extra-point / parallel-class incidence obstruction.

Desired next theorem:

> every `r^2-O(r)`-block partial resolvable `TD(5,r)` satisfying the multicolor completion and target `alpha<=5, omega<=r-1` contracts is impossible for all sufficiently large `r`.

Status: **OPEN**.
