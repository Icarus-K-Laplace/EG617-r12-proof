# Global Zero-Signature / Three-Anchor Dichotomy

Status: **PROVED_ANALYTIC**.

This theorem is the missing bridge between the support-incidence language and the global three-anchor core obstruction. It combines only already-proved analytic inputs:

- `GLOBAL_ZERO_CHARGE_INCIDENCE_SIGNATURE_THEOREM.md`;
- `GLOBAL_ZERO_CHARGE_SKELETON_DECOMPOSITION.md`;
- `GLOBAL_THREE_ANCHOR_K4_EQUALITY_CLOSURE.md`;
- `GLOBAL_THREE_ANCHOR_BACKEND_ENVELOPE.md`.

It is independent of the historical labels `D2-A/B/C/D`, `R9`, `E334`, ..., `E340`.

---

## 1. Setup

Let `H` be a 35-point residual core satisfying

- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`.

Consider one common-S support system with charge

`w_v = kappa_v + e_F(v,S)`,

where

`kappa_v=d_H(v)-12 >=0`.

Assume common-S row closure:

`e_H(v,D)<=w_v`

for every support `D` and every `v notin D`.

For every zero-charge support-union vertex define the incidence signature

`sigma(v)={D : v in D}`.

Let `t` be the number of distinct signatures represented among zero-charge support-union vertices.

The incidence-signature theorem gives

`t<=3`.

---

# 2. Three signatures force three minimum-degree anchors

Assume `t=3`.

Choose zero-charge vertices `z1,z2,z3` from the three different signature classes.

Because

`w_z = kappa_z + e_F(z,S)`

is a sum of nonnegative integers, `w_z=0` implies

`kappa_z=0`.

Hence

`d_H(z_i)=12`

for each `i`.

By the zero-charge incidence-signature theorem, two zero-charge vertices with different signatures are target-nonadjacent. Therefore

`z1,z2,z3`

are pairwise target-nonadjacent degree-12 vertices.

Thus:

> **Three-signature forcing lemma.**
> Three distinct zero-charge incidence signatures force three independent degree-12 anchors in the same residual core.

No support-size assumption is needed for this implication.

---

# 3. Immediate backend envelope

The global three-anchor theorem proves that any such 35-point core satisfies

`e(H)>=213`.

In a high-backend layer

`E = 91 + q + e(H)`.

Therefore the three-signature regime satisfies

> `q <= E-304`.

Explicitly:

|E|q upper bound in three-signature regime|
|---:|---:|
|334|30|
|335|31|
|336|32|
|337|33|
|338|34|
|339|35|
|340|36|

Hence any survivor above this envelope must have

> at most two zero-charge incidence signatures.

This is the first direct theorem-level bridge from repeated-support incidence data to a layer-independent backend contradiction/envelope.

---

# 4. At most two signatures imply at most three nonempty zero skeletons

Now assume `t<=2`.

By the zero-charge skeleton theorem, every support's zero-charge set is a union of whole signature classes. Hence the number of possible **nonempty** zero-skeleton patterns is at most

`2^t-1 <= 3`.

Thus every support containing a zero-charge point belongs to one of at most three canonical skeleton patterns.

Supports in the same pattern form a sunflower with exact common zero core and pairwise-disjoint private petals.

This converts the complement of the three-anchor regime into a bounded-complexity incidence system.

---

# 5. Boundary one-loss systems have no empty zero skeleton

Suppose now the support system is `d`-uniform and every active support is a boundary one-loss support:

`Delta(D)=d-1`,

with exact defect decomposition

`w(D)+mu(D)=d-1`,

where `mu(D)>=0` is the internal missing-edge defect.

If a support contained no zero-charge point, then every one of its `d` vertices would have positive integral charge, so

`w(D)>=d`,

contradicting

`w(D)<=d-1`.

Therefore:

> **Every boundary one-loss support has a nonempty zero skeleton.**

Consequently, in the `t<=2` regime **all** active support classes, not merely a subfamily, lie in at most three zero-skeleton patterns.

This is the key finite-complexity alternative to the three-anchor branch.

---

# 6. d=3 specialization: only Type-H / Type-P repeated geometry

For 3-point boundary one-loss supports,

`Delta(D)=2`.

Under `t<=2`, all support classes lie in at most three nonempty skeleton patterns.

By `GLOBAL_ZERO_CHARGE_SKELETON_DECOMPOSITION.md`, every pattern used by at least two distinct support classes is exactly one of:

### Type H — common zero hub

- one zero-charge common hub;
- two private petals per support;
- each private petal has charge one;
- every support is a target `K3`.

### Type P — common zero pair

- one zero-charge common pair;
- one positive-charge private petal;
- every support is either a two-edge triple or a target `K3`.

All other zero-skeleton patterns occur in at most one support class.

Therefore:

> **d3 dichotomy.**
> Every boundary one-loss d3 system in the r=12 core either
>
> 1. forces three independent degree-12 anchors and hence the backend envelope `q<=E-304`, or
> 2. is the union of at most three canonical zero-skeleton pattern families, whose only repeated geometries are Type H and Type P sunflowers.

There is no third uncontrolled overlap regime.

---

# 7. d=2 specialization: one-hub repeated geometry

For 2-point boundary one-loss supports,

`Delta(D)=1`.

Again every support contains a zero-charge point.

If `t<=2`, every support lies in at most three nonempty zero-skeleton patterns. A nontrivial repeated pattern cannot have a two-point common zero core, because then two distinct two-point supports would be identical. Hence every repeated pattern has a one-point zero core.

Its other support point is a private positive-charge point. Since the total defect is one, that private charge is exactly one and the internal missing-edge defect is zero.

Thus every support in a repeated pattern is a target `K2`.

Therefore:

> **d2 dichotomy.**
> Every boundary one-loss d2 system either
>
> 1. forces the three-anchor backend envelope, or
> 2. consists of at most three zero-skeleton patterns, and every nontrivial repeated pattern is a common-zero-hub sunflower of target `K2` supports with unit-charge private petals.

This gives a common structural explanation for the repeated-pair geometries appearing throughout the D2 backend families.

---

# 8. Hereditary-packing closure interface

The second branch is not an unstructured residual case.

For Type H / Type P / d2 common-hub families, the support internal density and owner multiplicities feed directly into

`GLOBAL_HEREDITARY_SUPPORT_PACKING_THEOREM.md`.

Thus the full support-compatibility strategy becomes:

1. **three zero signatures**
   -> three independent degree-12 anchors
   -> `e(H)>=213`
   -> backend envelope `q<=E-304`;

2. **at most two zero signatures**
   -> at most three canonical zero-skeleton patterns
   -> Type H / Type P / d2-hub sunflower geometry
   -> hereditary support packing + repetition charging.

This is a genuine global dichotomy, not an E-layer case split.

---

# 9. Equality / escape interpretation

The theorem identifies the only way a support system can avoid the three-anchor obstruction:

> its zero-charge incidence structure must collapse to at most two signatures.

That collapse is itself highly rigid. In the boundary one-loss layer it forces all supports into at most three sunflowers/singletons.

Therefore any remaining proof should classify only the equality geometry of these at-most-two-signature systems. It should not return to the original D2/R9 or E334--E340 case labels.

---

# 10. Generalization beyond r=12

The argument separates into two parts.

The incidence-signature theorem is already parameterized by `alpha(H)<=r_core` and gives at most `r_core` zero signatures.

For a different Ramsey residual core, if one proves an `s`-anchor global obstruction, then `s` distinct zero-charge signatures immediately force that obstruction because zero charge implies minimum core degree and distinct signatures imply pairwise target-nonadjacency.

Thus the general schema is:

> incidence-signature diversity -> independent minimum-degree anchors -> global core obstruction;
>
> low signature diversity -> bounded sunflower skeleton -> hereditary packing.

This is directly portable to r>=13 once the corresponding residual-core minimum degree, independence cap, clique cap and hereditary density function are available.