# Low-Slack Coordinatization on a `q^2` Restriction

Status: **PROVED, using Brouwer's non-r-partite Turan theorem.**

The theorem is valid for all integers `q>=3`; no prime-power assumption is needed.

## External theorem used

Brouwer's refinement of Turan's theorem:

> If `H` is a `K_(r+1)`-free graph on `n>=2r+1` vertices and
>
> `e(H) >= t_r(n)-floor(n/r)+2`,
>
> then `H` is `r`-partite.

Modern references include Kang--Pikhurko, *Maximum K_(r+1)-free graphs which are not r-partite* (2005), and Popielarz--Sahasrabudhe--Snyder, JCTB 132 (2018), which restates the Brouwer threshold.

## Setup

Let `W` be a `q^2`-vertex subset of a hypothetical counterexample to `P(q)`, and let `G_i=G_i[W]` be one color graph.

Because the ambient coloring is a counterexample,

`alpha(G_i)<=q`, `omega(G_i)<=q`.

Define

`m_q := q*C(q,2) = q^2(q-1)/2`,

which is the minimum number of edges in a `q^2`-vertex graph with independence number at most `q`, and define the local Turan slack

`s_i := e(G_i)-m_q >= 0`.

## Theorem K.3 — Low-slack clique-partition extraction

If

`0 <= s_i <= q-2`,

then `W` has a partition

`W=P_1 disjoint union ... disjoint union P_q`

such that

- `|P_a|=q` for every `a`;
- every `P_a` induces a monochromatic `K_q` of color `i`;
- exactly `s_i` additional color-`i` edges run between distinct blocks.

### Proof

Let `H=overline(G_i)`. Since `alpha(G_i)<=q`, the graph `H` is `K_(q+1)`-free.

Moreover

`e(H)=C(q^2,2)-m_q-s_i=t_q(q^2)-s_i`.

If `s_i<=q-2`, then

`e(H)>=t_q(q^2)-q+2`.

For `q>=3`, `q^2>=2q+1`, so Brouwer's theorem implies that `H` is `q`-partite.

Each part of this `q`-partition is independent in `H`, hence a clique in `G_i`. Since `omega(G_i)<=q`, every part has size at most `q`. There are at most `q` parts covering `q^2` vertices, so there are exactly `q` nonempty parts and every one has size exactly `q`.

The within-part edges contribute exactly `m_q` color-`i` edges. Since `e(G_i)=m_q+s_i`, precisely `s_i` color-`i` edges remain between different blocks.

## Corollary K.4 — Two low-slack colors give exact orthogonal coordinates

If distinct colors `i,j` both satisfy

`s_i,s_j <= q-2`,

then their extracted block partitions `P_1,...,P_q` and `Q_1,...,Q_q` obey

`|P_a intersect Q_b|=1`

for every `a,b`.

### Proof

No intersection can contain two vertices, because the edge between two such vertices would simultaneously lie in the color-`i` clique `P_a` and the color-`j` clique `Q_b`. There are `q^2` intersections and `q^2` vertices, each vertex lying in exactly one intersection, so all intersections have size exactly one.

Thus two low-slack colors canonically coordinatize `W` as a `q x q` grid. The only deviations from the two direction-class model are at most `q-2` extra cross-block edges in each color.

## Lemma K.5 — Near-line forcing from a low-slack color

Let `x` be the deleted ambient vertex and suppose color `i` has the partition above with slack `s=s_i`. Let `B_a subset P_a` be the vertices `v` for which edge `xv` is not color `i`.

If every `B_a` is nonempty, then the union of the `B_a` cannot contain an independent transversal for the color-`i` graph, because such a transversal together with `x` would form a `(q+1)`-set missing color `i`.

Let `E_i^cross` be the set of the `s` cross-block color-`i` edges. If every `B_a` contained a vertex not incident with `E_i^cross`, choosing such a vertex from every block would give an independent transversal. Therefore some block satisfies

`B_a subset V(E_i^cross)`,

hence

`|B_a| <= 2s`.

Equivalently, for some monochromatic `K_q` block `P_a`, the new vertex `x` has color-`i` edges to at least

`q-2s`

vertices of `P_a`.

For `s=0` this recovers the exact full-line forcing used in the affine-plane nonextension proof.

## Significance

This is the first quantitative coordinatization lemma on the K-line:

- exact equality is not required;
- the threshold is linear (`s<=q-2`), not infinitesimal;
- two low-slack colors already produce an exact orthogonal grid;
- the extra vertex sees an almost-monochromatic block when the cross-defect set is small.

The remaining issue is global: current total-slack identities do not yet force two colors into this low-slack window.