# Global Zero-Signature / Anchor-Partition Alignment Theorem

Status: **PROVED_ANALYTIC**.

This theorem strengthens the bridge between the support-incidence master theorem and the global three-anchor core theorem.  Three distinct zero-charge signatures do not merely produce three independent minimum-degree anchors: the entire three signature classes align with the three exclusive anchor cliques.

Dependencies:

- `GLOBAL_ZERO_CHARGE_INCIDENCE_SIGNATURE_THEOREM.md`;
- `GLOBAL_ZERO_CHARGE_SKELETON_DECOMPOSITION.md`;
- `GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md`;
- common-S charge `w_v=kappa_v+e_F(v,S)`.

No E-layer label, excess value, or solver is used.

---

## 1. Setup

Let H be a residual core with `alpha(H)<=3` and `delta(H)>=12`.

Consider a d-uniform common-S support system.  For every zero-charge support-union vertex v define its nonempty incidence signature

`sigma(v)={D:v in D}`.

Assume exactly three distinct zero-charge signatures occur.  Denote their classes by

`Z1,Z2,Z3`.

Choose representatives

`a_i in Z_i`.

The zero-signature theorem gives:

- vertices from different Z_i are target-nonadjacent;
- `w_{a_i}=0` implies `kappa_{a_i}=0`, hence `d_H(a_i)=12`.

Therefore `a1,a2,a3` are three pairwise nonadjacent degree-12 anchors.

Apply the three-anchor partition theorem to these anchors.  Let X_i be the exclusive class of vertices adjacent to `a_i` and to neither other anchor.

---

## 2. Every signature class aligns with one exclusive anchor block

Take

`v in Z_i\{a_i}`.

Because v has a different zero signature from `a_j` for every `j!=i`, the zero-signature theorem gives

`v a_j` target-nonedge for `j!=i`.

If v were also nonadjacent to `a_i`, then

`{v,a_1,a_2,a_3}`

would be an independent 4-set, contradicting `alpha(H)<=3`.

Hence v is adjacent to `a_i` and to neither other anchor.

Thus

> **`Z_i subseteq X_i union {a_i}` for i=1,2,3.**          (A1)

In particular, each zero-signature class is itself a target clique: `X_i union {a_i}` is a clique by the partition theorem.

This is stronger than merely selecting one anchor from each signature.

---

## 3. Uniform support size bounds each signature class

Every zero-charge support-union vertex has nonempty signature.  Fix i and choose any support

`D in sigma(a_i)`.

All vertices of Z_i have the same signature as a_i.  Therefore every point of Z_i lies in every support in `sigma(a_i)`, in particular in D.

Hence

`Z_i subseteq D`.

Since every support has size d,

> **`|Z_i|<=d`.**                                          (A2)

Consequently the total number of zero-charge vertices belonging to the active support union U is at most

> **`|{v in U:w_v=0}| <= 3d`.**                            (A3)

For the two master regimes:

- d=2: at most6 zero-charge support vertices;
- d=3: at most9 zero-charge support vertices.

This bound is independent of owner count and core excess.

---

## 4. Charge lower bound on the support union

Every nonzero integral charge is at least one.  Therefore (A3) gives

`W(U)=sum_{v in U} w_v`
`    >= |U|-3d`.

Thus

> **`W(U)>=|U|-3d`.**                                      (A4)

Equivalently,

> **`|U|<=W(U)+3d`.**                                      (A5)

This supplies a direct quantitative interface between

- support-union expansion / low multiplicity, and
- the charge budget,

inside the three-signature / three-anchor branch.

If the owner-support incidence count is dN and every support vertex has incidence multiplicity at most `mu_max`, then

`|U|>=ceil(dN/mu_max)`,

and therefore

> `W(U)>=ceil(dN/mu_max)-3d`.                               (A6)

This inequality is crude but completely general and can be sharpened with the hereditary multiplicity bounds in a concrete support regime.

---

## 5. Interaction with zero-skeleton patterns

The alignment theorem also localizes every zero skeleton.

By `GLOBAL_ZERO_CHARGE_SKELETON_DECOMPOSITION.md`, the zero set of a support is a union of whole signature classes.  By (A1), each such class lies in one exclusive anchor clique.

Thus every support zero skeleton is a union of at most three **anchor-aligned microcores**

`Z_i subseteq X_i union {a_i}`,

with each microcore of size at most d.

For boundary one-loss systems this is especially restrictive:

- d2 supports can only use one aligned microcore, or two singleton microcores;
- d3 supports cannot contain all three singleton anchor classes, because the three anchors are pairwise nonadjacent and would contribute internal defect three, exceeding the one-loss defect two.

Hence the t=3 branch is not an uncontrolled seven-pattern system once the three-anchor partition is taken into account.

---

## 6. K=6 equality interface

The theorem applies in particular to the K=6 equality geometries classified in

- `GLOBAL_THREE_ANCHOR_K6_C2_NORMAL_FORM.md`;
- `GLOBAL_THREE_ANCHOR_K6_C3_NORMAL_FORM.md`;
- `GLOBAL_THREE_ANCHOR_K6_C4_DOMINATOR_CAPACITY.md`.

In those geometries the three zero-signature classes must occupy three small subsets of the exclusive anchor cliques, each of size at most d.  All other support-union vertices have positive common-S charge.

Therefore any K=6 equality incompatibility proof may now use a single interface:

> support-union size beyond `3d` must be paid for by positive charge, while every zero skeleton is confined to the three aligned anchor microcores.

This is the missing geometric alignment between the support master theorem and the three-anchor equality reduction.

---

## 7. Generalization

The proof uses only:

- independence number at most3;
- distinct zero signatures are pairwise nonadjacent;
- zero charge implies minimum core degree;
- d-uniform support incidence.

For a residual core with independence number at most r and r distinct zero signatures, the same argument aligns each signature class with the corresponding exclusive anchor block and gives

`|Z_i|<=d`,

hence at most `rd` zero-charge support-union vertices.

Thus the theorem is naturally portable to higher-r support-compatibility problems.