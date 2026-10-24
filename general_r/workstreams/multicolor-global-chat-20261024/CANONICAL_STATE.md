# Multicolor-Global Workstream — Canonical State

Date: 2026-10-24
Branch: `workstream/general-r-multicolor-global-20261024`
Scope: global inequalities that essentially use the simultaneous r-color edge partition. Single-color residual/core lemmas are not counted as headline progress here.

## Headline status

- **I1: ACHIEVED.** Proved a genuine multicolor non-rainbow triangle budget, color-degree variance bound, and edgewise row-signature compatibility theorem.
- **I2: OPEN.** The present inequalities do not yet force one color into a quantitatively stronger structural class than ordinary averaging/stability.
- **I3: OPEN.** No sufficiently-large-r contradiction yet.
- **I4: OPEN.** No independent all-r solution yet.

## Core variables

`n=r^2+1`.

For colors `G_1,...,G_r`:

`d_i(v)=degree of v in G_i`,
`e_i=e(G_i)`,
`sum_i d_i(v)=r^2`,
`sum_i e_i=C(n,2)`.

Define

`V=sum_(v,i)(d_i(v)-r)^2`.

For local avoidance,

`W_i(v)=V\({v} union N_i(v))`,

so `|W_i(v)|=r^2-d_i(v)` and the counterexample property forces

`alpha(G_i[W_i(v)])<=r-1`.

## Main proved inequality

Let `T_2` be the number of triangles with exactly two colors and `T_3` the number of monochromatic triangles. Define

`P(v)=sum_i p_(r-1)(r^2-d_i(v))-r^2(r-1)^2/2 >=0`,
`P=sum_v P(v)`.

Then

> `2T_2+3T_3 <= n r^2(r-1)-P`.

Consequences:

`T_2+T_3 <= [n r^2(r-1)-P]/2`,

so all but `O(1/r)` of all triples are forced to be rainbow.

The same-color wedge identity gives

`V+2P <= n r^2(r-1)`.

Since

`P>=V/[2(r-1)]`,

we obtain

> `V<=n r(r-1)^2`.

## Edgewise compatibility form

For an edge xy of color i, let `b(xy)` count third vertices z for which xyz is non-rainbow. Then

`b(xy)=d_i(x)+d_i(y)-2-c_i(x,y)+sum_(j!=i)c_j(x,y)`.

Globally,

> `average_edge b(xy) <= 3(r-1)-3P/(n r^2)`.

Thus a typical pair of adjacent color-signature rows collides in only `O(r)` of `Theta(r^2)` third-vertex coordinates.

## Does the theorem genuinely use multiple colors?

**Yes.** Essential steps are:

1. the pointwise partition identity `sum_i d_i(v)=r^2`;
2. simultaneous convexity over all `W_i(v)`;
3. the fact that each pair xy has one unique edge color, allowing `sum_i e_i(W_i(v))` to be interpreted as a triangle-color-pattern count;
4. row-signature collisions across colors.

No single-color theorem alone yields the non-rainbow budget.

## Relation to Turan slack

With

`s_i=e_i-p_r(n)`,

one has exactly

`sum_i s_i=r^2(r-1)/2` and

`e_i-C(n,2)/r=s_i-C(r,2)`.

Hence

`V >= (4/n) sum_i (s_i-C(r,2))^2`.

The workstream now has a common variable V linking global color imbalance, local color-degree irregularity, non-rainbow triangles, and prospective partition stability.

## Current blocker

Single-color Turan stability still allows `Theta(r^2)` edits per typical color. The missing multicolor theorem must show that the row-signature collision budget forces these edit sets to be strongly correlated/orthogonal, yielding two near-clique partitions with an almost permutation intersection matrix.

The most direct next target is a robust two-partition compatibility lemma strong enough to feed the already proved affine-plane-style nonextension mechanism.

## H+I Joint Audit — 2026-10-24

The induced-residual transfer is PROVED: restricting a counterexample coloring to any induced subset preserves the every-(r+1)-set-sees-all-colors property, and the distinguished color's stronger alpha<=a assumption improves its local avoidance floor to p_{a-1}. The resulting `Lambda_{r,a}(m)` inequality is recorded in `MULTICOLOR_TO_SEED_INTERFACE.md`.

However, the derived inequality is not a lower seed-floor theorem. It currently gives an upper consistency constraint on the distinguished color's edge count, and the degree-free relaxation leaves a factor-a asymptotic gap at m=ar+O(1).

The robust partition route now has the exact collision-mass bound `sum_ab C(M_ab,2)<=E_i+E_j`, but stability only gives E_i=O(r^2) for the guaranteed pair. An explicit margin-compatible matrix shows this does not force o(r^2) exceptional cells. The requested strict low-slack/high-slack dichotomy, I2, I3, I4, and an explicit r0 remain OPEN.
