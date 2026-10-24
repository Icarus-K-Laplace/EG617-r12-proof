# d2 Distinct-Support Matching Collapse

Assumptions:

- residual-core/backend hypotheses A+B;
- `r>=12` (the proof actually needs only `r>=8` at the final numerical comparison);
- the standard backend global independence cap `alpha(F)<=3`;
- the general residual edge cap `E=e(F)<=2r^2+4r+4` already used in the q-ceiling architecture.

Fix any regular d2 common-S class, and let Q be the simple graph on H whose edges are its **distinct** core supports `D_y`.

The theorem does not use the allowance a, q-flatness, decoration, or first-high-slack assumptions.

---

## 1. Every owner support hits every independent triple of H

Let y be a regular d2 owner with core support

`D_y=N_F(y) intersect H`, `|D_y|=2`.

The owner y is target-nonadjacent to every vertex of `H\D_y`.

If `T subset H\D_y` were an independent triple in H, then

`T union {y}`

would be an independent 4-set in F, contradicting `alpha(F)<=3`.

Therefore

> **`alpha(H\D_y)<=2`.**                                     (1.1)

Equivalently:

> **every independent triple of H intersects every owner support D_y.**   (1.2)

This is the support-transversal form of the global independence cap.

**Status:** `PROVED_SYMBOLIC` under `alpha(F)<=3`.

---

## 2. Four disjoint supports would force alpha(H)<=2

Suppose Q contained a matching of four pairwise-disjoint support edges

`D_1,D_2,D_3,D_4`.

By (1.2), every independent triple T of H would have to meet all four sets D_i. But T has only three vertices and the D_i are pairwise disjoint. This is impossible.

Hence H would contain no independent triple at all:

> **`alpha(H)<=2`.**                                         (2.1)

We now show that this is incompatible with the residual edge budget.

---

## 3. Mantel lower bound contradicts the residual core edge count

Put

`n=|H|=3r-1`.

If `alpha(H)<=2`, then the complement of H is triangle-free. By Mantel,

`e(overline H)<=floor(n^2/4)`.

Therefore

`e(H)>=C(n,2)-floor(n^2/4)`

and in particular

> **`e(H)>=n(n-2)/4=((3r-1)(3r-3))/4`.**                     (3.1)

On the other hand,

`e(H)=r(3r-1)/2+K/2`.

The general residual edge cap and `q>=0` give

`K=2(E-q-(2r^2+r+1))<=2[(2r^2+4r+4)-(2r^2+r+1)]`

so

> **`K<=6r+6`.**                                             (3.2)

Thus

> **`e(H)<=(3r^2+5r+6)/2`.**                                 (3.3)

Comparing the weaker Mantel lower bound (3.1) with (3.3), a contradiction follows whenever

`(9r^2-12r+3)/4 > (6r^2+10r+12)/4`,

i.e.

`3r^2-22r-9>0`.

This already holds for every integer `r>=8`.

Therefore four disjoint owner supports are impossible for all `r>=8`.

---

# 4. Matching-Three Theorem

> **Theorem.** For every `r>=12` in the general backend,
>
> **`nu(Q)<=3`.**                                            (4.1)

**Status:** `PROVED_CONDITIONAL` on the standard global `alpha(F)<=3` and residual edge cap.

This is allowance-independent and strictly stronger, for the termination program, than the earlier weighted matching estimate

`nu(Q)(a-1)<=W`.

---

## 5. Six-hub vertex-cover collapse

Take a maximal matching in Q. Its endpoints form a vertex cover. Since the matching has at most three edges,

> **Q has a vertex cover C with `|C|<=6`.**                   (5.1)

Thus every distinct d2 core support contains at least one vertex of one fixed at-most-six-point core hub set C.

Equivalently, every distinct-support family is a union of at most six support stars, with possible edges inside C.

This remains true even in the unique scalable fully-decorated q-flat regime `S subset X`, and it is independent of the allowance a.

Hence the distinct-support branch has an r-independent support-hypergraph skeleton.

---

## 6. Bounded signature encoding

Let

`R=V(Q)\C`.

There are no Q-edges with both endpoints in R. Each leaf `x in R` is therefore described, at the support-graph level, by its nonempty neighbourhood

`N_Q(x) subset C`.

Since `|C|<=6`, there are at most

> **`2^6-1=63`**                                             (6.1)

nonempty support-incidence signatures for outside core vertices.

For a q-flat fixed shell class, every support edge `cx` additionally satisfies

`w_c+w_x+mu(cx)=a`,

so once the hub weight `w_c` and the target/nonedge bit `mu(cx)` are fixed, the leaf weight is determined. Therefore the weighted q-flat support skeleton has a finite signature alphabet indexed by

- one of at most six hubs;
- a subset of the hub cover;
- target/nonedge bits on incident support edges;
- the induced hub weights.

Multiplicity of a signature may still scale with r, but the combinatorial support types do not.

---

## 7. Main-theorem impact

Before this theorem, the last genuinely scalable combinatorial blocker was a fixed fully-decorated d2 shell class with many distinct core supports.

After (4.1)--(5.1):

> **even the distinct-support branch has a fixed-width core-support skeleton: matching number at most three and a support vertex cover of size at most six.**

Thus both halves of the fully-decorated plateau are now structurally bounded-width:

1. repeated exact classes -> exact zeta exchange and Balanced Two-Chamber terminal;
2. distinct supports -> at-most-six-core-hub support skeleton.

The remaining problem is no longer support-shape proliferation. It is **multiplicity / weighted leaf compatibility inside finitely many hub signatures**.

This is the appropriate input for a final multi-pivot charge or fourth-potential theorem.