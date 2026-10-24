# Theorem ledger

## Main theorem — Exact Three-Anchor Excess

Let `r>=13` and let `H` be a graph on `3r-1` vertices with

- `alpha(H)<=3`,
- `omega(H)<=r-1`,
- `delta(H)>=r`.

If `H` contains three pairwise nonadjacent vertices `a1,a2,a3` of degree exactly `r`, then

`K_r(H)=2e(H)-r(3r-1)>=8`.

**STATUS: `PROVED_SYMBOLIC` for every `r>=13`.**

Together with the already-existing certified `r=12` closure in the parent project, this gives the requested Level-3 resolution of the Exact Three-Anchor Excess Conjecture for all `r>=12`. The present workstream does not claim that the historical `r=12` case has been replaced by the same parameterized proof; that is the remaining Level-4 cleanup target.

---

## Theorem 0 — parity collapse

`K_r(H)` is always even. Indeed `2e(H)` is even and `r(3r-1)` is even. Therefore any counterexample to `K_r>=8` would satisfy

`K_r<=6`.

This removes the entire apparent `K=7` layer.

---

## Theorem 1 — exact anchor partition

Let `Xi` be the vertices adjacent to exactly anchor `ai`; let `C` be the connector set, `c=|C|`; and let `t` be the number adjacent to all three anchors. Then

`c+t=4`.

Writing

`d_i=(r-2)-|Xi|`,

one has

`d_1+d_2+d_3=c-2`.

Hence, up to permutation, the only geometries are

- `c=2`: `d=(0,0,0)`;
- `c=3`: `d=(0,0,1)`;
- `c=4`: `d=(0,0,2)`;
- `c=4`: `d=(0,1,1)`.

Moreover if `q_i` is the number of connectors missing anchor `ai`, then

`q_i=d_j+d_k`.

Thus every connector incidence type is fixed by the deficit vector.

---

## Theorem 2 — c=2 closure

The `c=2`, `(r-2,r-2,r-2)` geometry is impossible for every `r>=12` under `K<=6`.

**STATUS: `PROVED_SYMBOLIC`.**

The proof uses the degree-2 tripartite transversal-cover lemma in `PROOF_ATTEMPTS.md`.

---

## Theorem 3 — c=3 closure

The `c=3`, `(r-2,r-2,r-3)` geometry is impossible for every `r>=13` under `K<=6`.

**STATUS: `PROVED_SYMBOLIC`.**

There is one triple connector and two pair connectors. Pair-connector nonneighbour rectangles show that two nonfocused pair connectors are too expensive; two focused connectors force a huge common-nonneighbour rectangle; hence exactly one is focused. The mixed branch is eliminated by a sharpened rectangle charge. Its unique `r=13,K=6` arithmetic equality forces the triple connector to be adjacent to all of an `(r-2)`-block despite insufficient degree.

---

## Theorem 4 — c=4, deficits (0,0,2), closure for every r>=13

Here `|X1|=|X2|=r-2`, `|X3|=r-4`; all four connectors are pair connectors, two missing `a1` and two missing `a2`, and all are incident to `a3`.

Call a connector **focused** if it is complete to `X3`.

### Focus cap
For two focused connectors `p,q`, if `pq` is a nonedge, their common nonneighbour set is a clique. Since they share `X3 union {a3}` (size `r-3`) as common neighbours,

`|M(p,q)| >= 2r-6-k_p-k_q >= 2r-12 > r-1`.

Thus any two focused connectors must be adjacent. Three focused connectors would then form a triangle and, together with `X3 union {a3}`, an `r`-clique. Therefore there are at most two focused connectors and hence at least two nonfocused connectors.

### Nonfocus charge
For a nonfocused connector of excess `k` and connector-degree `gamma`, let `a>=1` and `b>=1` be its nonneighbour counts in its incident zero-deficit block and in `X3`. Then

`a+b >= r-4-k+gamma`,

and its complete nonneighbour rectangle forces

`R_24(a,b)=a(b-2)_+ + b(a-4)_+`.

Since `R_24(a,b)>=a+b-6`,

`k+R_24 >= r-10+gamma`.

For `r>=17` this already contradicts `K<=6`. The values `r=13,14,15,16` are eliminated structurally, not by graph enumeration:

- `r=16`: every nonfocused connector has local charge at least six. Two different-group rectangles charge additively; two same-group nonadjacent connectors have disjoint nonneighbour supports; adjacency would raise the local bound above six. Hence two required nonfocused connectors cannot coexist.
- `r=15`: the same argument applies; if two same-group nonfocused connectors are adjacent, the only way a single one can stay within total budget six is the `k=6` boundary layer, so two cannot coexist.
- `r=14`: different-group or nonadjacent same-group nonfocused connectors already cost at least eight in total. If the same-group pair is adjacent, total budget six forces both to have `k=0` and the same `(a,b)=(10,1)` rectangle. Its unique `X3` vertex then carries all six excess units and has no remaining connector slot, contradicting that the other-group pair must be focused and hence complete to `X3`.
- `r=13`: a different-group nonfocused pair can fit budget six only in the equality `(k,a,b)=(3,4,2)` for both; this spends all excess and makes their `X3` rectangle vertices unavailable to any focused connector, while the remaining connectors must be focused — contradiction. Thus the two nonfocused connectors are the same-group pair and the other group is focused. The two focused connectors consume two external slots at every `X3` vertex. If the nonfocused pair is nonadjacent, its disjoint rectangles now each have the strengthened `(2,2)` charge and cost at least five, additively. If it is adjacent, the strengthened charge forces `k=6` for each connector. Both alternatives contradict `K<=6`.

Therefore the `(0,0,2)` geometry is impossible for every `r>=13`.

---

## Theorem 5 — c=4, deficits (0,1,1), closure for every r>=13

Here `|X1|=r-2`, `|X2|=|X3|=r-3`. There are two connectors missing `a1` (type U), one missing `a2`, and one missing `a3`.

A connector complete to a deficit-1 block `Xi` is said to focus on `Xi`.

### Focus-collision lemma
No two connectors can focus on the same deficit-1 block. If they are adjacent, `Xi union {ai,p,q}` is an `r`-clique. If they are nonadjacent, their common nonneighbour set is a clique and

`|M(p,q)| >= 2r-5-k_p-k_q >= 2r-11 > r-1`.

Hence at most one connector focuses on `X2` and at most one on `X3`; at least two of the four connectors are nonfocused.

### Local charges
For a type-U nonfocused connector (incident deficits `(1,1)`),

`k+R_33 >= r-10+gamma`,

where

`R_33=a(b-3)_+ + b(a-3)_+`.

For a nonfocused connector missing `a2` or `a3` (incident deficits `(0,1)`),

`k+R_23 >= r-8+gamma`,

where

`R_23=a(b-2)_+ + b(a-3)_+`.

For `r>=17` all connectors would have to focus, contradicting the focus-collision lemma. The boundary values are eliminated as follows.

- `r=16`: the two `(0,1)` connectors must focus on `X3` and `X2`, so both type-U connectors are nonfocused. They cannot be adjacent (that would raise a local charge above six); if nonadjacent, sharing the missing anchor forces their two nonneighbour supports to be disjoint, so the two local charges add to at least twelve.
- `r=15`: again the `(0,1)` connectors are forced to focus. The type-U pair is nonfocused. If nonadjacent, the disjoint charges sum to at least ten. If adjacent, staying within budget six forces each connector into the `k=6` equality layer, impossible for two distinct connectors.
- `r=14`: a nonfocused `(0,1)` connector would have to be isolated, carry `k=6`, have nonneighbour rectangle `(3,2)`, and consume the whole excess budget. Its saturated rectangle plus its absence of neighbours in the third block would force each of the other three connectors to be complete to the same deficit-1 block, violating the focus-collision lemma. Hence both `(0,1)` connectors focus, forcing the type-U pair nonfocused. A nonadjacent type-U pair has additive charge at least eight; an adjacent pair requires at least five connector excess units on each member. Contradiction.
- `r=13`: two nonfocused `(0,1)` connectors have additive charge at least ten. If exactly one `(0,1)` connector is nonfocused, focus capacity forces at least one type-U connector also nonfocused, and the two rectangles use disjoint opposite blocks, so their local charges add to at least eight. Hence both `(0,1)` connectors focus, forcing both type-U connectors nonfocused. If the type-U pair is nonadjacent, equality `K=6` would require both connectors to have `k=3` and `(3,3)` rectangles with disjoint supports; but every rectangle vertex already has the corresponding focused connector neighbour, contradicting exactness. If the pair is adjacent, the two focused connectors lower both effective rectangle capacities from 3 to 2; the strengthened charge forces `k=6` on each type-U connector. Contradiction.

Therefore the `(0,1,1)` geometry is impossible for every `r>=13`.

---

## Corollary — Level-3 completion

The four symbolic anchor geometries are exhausted. Thus

> **Exact Three-Anchor Excess Theorem: `K_r(H)>=8` for every `r>=13`.**

Composing this parameterized theorem with the existing `r=12` closure gives the desired all-`r>=12` result at Level 3.

The only remaining research target is Level 4: absorb `r=12` into the same short analytic proof so that no fixed-r closure is cited separately.
