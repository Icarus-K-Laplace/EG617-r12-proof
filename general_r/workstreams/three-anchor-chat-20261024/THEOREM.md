# Theorem ledger

## Main theorem — Exact Three-Anchor Excess

Let `r>=12` and let `H` be a graph on `3r-1` vertices with

- `alpha(H)<=3`,
- `omega(H)<=r-1`,
- `delta(H)>=r`.

If `H` contains three pairwise nonadjacent vertices `a1,a2,a3` of degree exactly `r`, then

`K_r(H)=2e(H)-r(3r-1)>=8`.

**STATUS: `INDEPENDENTLY_VERIFIED` by an analytic proof audit for every `r>=12` (Level 4).**

The publication-canonical proof is `PUBLICATION_VERSION.md`; the audit and full helper-lemma derivations are in `INDEPENDENT_AUDIT.md` and `LEMMA_VERIFICATION.md`. The former `r=12` residue has been absorbed into the same focus/rectangle proof. No historical fixed-r case table is needed. No full graph-level SAT/ILP search was run, and an external human referee review remains advisable.

---

## Theorem 0 — parity collapse

`K_r(H)` is always even: `2e(H)` is even, and `r(3r-1)` is even for every integer `r`. Therefore any counterexample to `K_r>=8` satisfies `K_r<=6`.

---

## Theorem 1 — exact anchor partition

Let `Xi` be the vertices adjacent to exactly anchor `ai`; let `C` be the connector set, `c=|C|`; and let `t` be the number of triple connectors. Then

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

If `q_i` is the number of connectors missing `ai`, then

`q_i=d_j+d_k`.

Thus the connector incidence type is fixed by the deficit vector.

---

## Theorem 2 — rectangle / focus mechanism

If a pair connector `z` misses anchor `ak` and is incident with `ai,aj`, then its nonneighbour sets

`A=Xi\N(z)`, `B=Xj\N(z)`

form a complete bipartite rectangle. If the two exclusive blocks have baseline external capacities `p,q`, that rectangle forces exclusive excess at least

`R_pq(a,b)=a(b-p)_+ + b(a-q)_+`.

Two additional rules are used repeatedly:

1. two nonadjacent connectors have a common-nonneighbour set that is a clique;
2. two nonadjacent pair connectors missing the same anchor have disjoint nonneighbour supports in both incident blocks.

When a connector is complete to an incident near-maximal block, it **focuses** on that block. A focused neighbour consumes one baseline external slot at every vertex of the block. Thus, for example, an `R24` rectangle becomes `R23` after one focus and `R22` after two focuses.

---

## Theorem 3 — c=2 closure

The `c=2`, `(r-2,r-2,r-2)` geometry is impossible for every `r>=12` under `K<=6`.

**STATUS: `PROVED_SYMBOLIC`.**

The proof is the degree-2 tripartite transversal-cover lemma recorded in `PROOF_ATTEMPTS.md`.

---

## Theorem 4 — c=3 closure

The `c=3`, `(r-2,r-2,r-3)` geometry is impossible for every `r>=12` under `K<=6`.

For `r>=13`, the focus/nonfocus rectangle inequalities close the branch; the unique `r=13` arithmetic equality forces the triple connector to see an entire `(r-2)` block despite insufficient degree.

At `r=12`, both pair connectors nonfocused cost at least eight, while both focused create either a forbidden 12-clique or a common-nonneighbour clique of size at least 13. Hence exactly one is focused. The mixed branch has effective `R22` charge. Every low-budget equality contains a saturated rectangle vertex. That vertex, together with the nonfocused connector and either the triple connector or the focused connector, forces adjacency to all/almost all of the opposite 10-clique, yielding either a 12-clique or an impossible degree count. Full details are in `R12_UNIFIED_CLOSURE.md`.

---

## Theorem 5 — c=4, deficits (0,0,2)

The `(r-2,r-2,r-4)` geometry is impossible for every `r>=12` under `K<=6`.

For `r>=13`, the parameterized focus/nonfocus closure in `PROOF_ATTEMPTS.md` applies.

At `r=12`, the blocks have sizes `(10,10,8)`. At most two connectors focus on the short block `X3`.

- with `f=0` focused connectors, additive `R24` charges exceed six; the only double-adjacency equality would require excess three on all four connectors;
- with `f=1`, effective `R23` charges on the three nonfocused connectors exceed six;
- with `f=2`, effective `R22` charges leave only two equality skeletons, `(a,b)=(1,8)` or `(8,1)`, with all six excess units concentrated on one exclusive vertex.

The `(1,8)` skeleton immediately gives an independent 4-set. In the `(8,1)` skeleton, a nonfocused and a focused connector have a common-nonneighbour set containing at least nine vertices of one long block and at least seven rectangle vertices of the other, contradicting the external degree capacity of an exact rectangle vertex.

---

## Theorem 6 — c=4, deficits (0,1,1)

The `(r-2,r-3,r-3)` geometry is impossible for every `r>=12` under `K<=6`.

No two connectors can focus on the same deficit-1 block. For `r>=13`, the parameterized closure in `PROOF_ATTEMPTS.md` applies.

At `r=12`, the block sizes are `(10,9,9)`. Let `s` be the number of occupied focus slots among the two deficit-1 blocks.

- `s=0`: the two `(0,1)` connector rectangles add to at least eight;
- `s=1`: an additive `R23/R22` pair costs at least seven;
- `s=2`: every ownership pattern except the one where the two `(0,1)` connectors own the two focus slots costs at least nine.

In the remaining ownership pattern, the two type-U connectors are nonfocused. If nonadjacent their supports are disjoint and cost at least eight. If adjacent, `K<=6` forces the same two `(1,8)/(8,1)` `R22` equality skeletons as in Theorem 5. In either orientation a saturated six-excess vertex and an exact focused connector produce an independent 4-set.

---

## Corollary — Level-4 completion

The four symbolic anchor geometries are exhausted for the full range `r>=12`. Therefore

> **Exact Three-Anchor Excess Theorem.** Let `r>=12` and let `H` be a graph on `3r-1` vertices with `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`. If `H` contains three pairwise nonadjacent degree-`r` vertices, then `2e(H)-r(3r-1)>=8`.

This is a direct analytic theorem, not a finite-r computation or a citation to the old `r=12` case closure.
