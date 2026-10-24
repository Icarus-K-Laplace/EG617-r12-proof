# T61 h13 full-color degree cap and common-antineighbourhood reduction

Status: **PROVED_RELATIVE_TO_BROUWER/KANG-PIKHURKO EXTREMAL THEOREMS**. This result is independent of the retained-seed status of the V11 Q31/Q32/Q33 package.

## 1. Setup

Let `F` be a genuine h13 T61 residual on 61 vertices in the original balanced 12-coloring. Thus

- `alpha(F)<=5`;
- `omega(F)<=11`;
- `delta(F)=13`;
- `E=e(F) in {407,408}` for the current high frontier.

For every non-target color `C_j` on these same 61 vertices,

- `alpha(C_j)<=12` by the balanced-coloring condition;
- `omega(C_j)<=5`, because a non-target K6 would be a target-independent 6-set.

The constrained minimum is

`e(C_j)>=129`.

Indeed, in the complement this is exactly the Brouwer/Kang-Pikhurko non-12-partite K13-free second Turan layer at `n=61`.

Since all 12 colors partition `C(61,2)=1830`, the total non-target excess above129 is

> **`S=411-E`.**

Hence

- E407: `S=4`;
- E408: `S=3`.

## 2. Pointwise degree floors for a non-target color

Write

`e(C)=129+s`.

### Exact cell s=0

Kang-Pikhurko equality classification gives

> **`delta(C)>=4`.**

### Cell s=1

Suppose a vertex v has `d_C(v)<=2`. Let N be its non-neighbourhood in C, excluding v. Then

`|N|=60-d_C(v)>=58`.

Since v is nonadjacent to every point of N, an independent12-set in C[N] would extend with v to an independent13-set. Therefore

`alpha(C[N])<=11`.

Also `omega(C[N])<=5`.

Because `|N|>55=11*5`, the complement of C[N] is K12-free and non-11-partite. Brouwer's theorem gives

`e(C[N])>=p_11(|N|)+floor(|N|/11)-1`.

For `d_C(v)=2`, `|N|=58`, so

`e(C[N])>=125+4=129`,

and hence

`e(C)>=129+2=131>130`, contradiction.

The cases degree0 or1 are even stronger. Thus

> **if `s=1`, then `delta(C)>=3`.**

### Cells s>=2 in the present frontier

If `d_C(v)<=1`, the same argument with `|N|>=59` gives

`e(C)>=135`.

Therefore for every color with `s<=4` in E407/E408,

> **if `s>=2`, then `delta(C)>=2`.**

## 3. Global target maximum-degree caps

Let the eleven non-target excesses be `s_1,...,s_11`.

### E408

Here

`sum s_j=3`.

Using the pointwise floors

- `f(0)=4`;
- `f(1)=3`;
- `f(2),f(3)>=2`,

the minimum possible sum of non-target degrees at any vertex is41. The minimizing excess partitions are `2+1` or `1+1+1`.

Thus every vertex v satisfies

`sum_(j!=target)d_j(v)>=41`.

Since the complete graph degree is60,

> **`d_F(v)<=19` for every v`.**

Therefore

> **`E408 => Delta(F)<=19`.**

### E407

Now

`sum s_j=4`.

The minimum possible non-target degree sum is40, attained only by the excess partitions

- `2+2`;
- `2+1+1`;
- `1+1+1+1`.

Hence

> **`E407 => Delta(F)<=20`.**

The partitions `4` and `3+1` cannot occur at any target-degree20 vertex, because their pointwise non-target degree floor is at least41 or42.

## 4. Direct near-anchor triple in every h13 T61 residual

Choose any target degree13 vertex p. It has47 target non-neighbours.

If among those47 vertices the points of target degree at most14 formed a clique, there would be at most11 of them. Hence at least36 non-neighbours would have degree at least15, contributing at least72 units of excess over13.

But the full target excess is

- E407: `2E-13*61=21`;
- E408: `23`.

Contradiction.

Therefore every degree13 pivot p lies in an independent target triple

> **`T={p,u,v}` with degree pattern `(13,<=14,<=14)`.**

## 5. Common target anti-neighbourhood window

Let W be the common target anti-neighbourhood of T.

Since T is independent and `alpha(F)<=5`,

`alpha(F[W])<=2`.

For every non-target color,

`alpha(C_j[W])<=12`.

Pair counting gives

`p_2(|W|)+11 p_12(|W|)<=C(|W|,2)`.

Together with the anchor degree sum, this yields

> **`17<=|W|<=23`.**

The upper values 25 and24 are already impossible by the pair count; the general sharp argument additionally excludes the analogues `2r+1=25` and `2r=24`.

## 6. The |W|=23 top cell

At `|W|=23`, the exact total pair-count slack is11.

Let

`J=bar(F[W])`.

Then J is triangle-free and `alpha(J)=omega(F[W])<=11`, so J is non-bipartite.

The sharp non-bipartite triangle-free theorem gives two top cells.

### Cell A

`e_F(W)=132`.

All eleven non-target colors are exact near-perfect matchings on W.

### Cell B

`e_F(W)=131` and

> **`J=S(K_11,11)`,**
>
> the graph obtained by subdividing one edge of `K_11,11` once.

The eleven non-target colors are the canonical factorization cell: ten near-perfect matchings and one matching-plus-P3 color.

Let w be the subdivision vertex. Then in the target graph

> **`d_(F[W])(w)=20`.**

## 7. E408 Cell B is impossible

From Section 3,

`Delta(F)<=19`

when E=408.

But Cell B contains w with target degree at least20 already inside W.

Contradiction.

Therefore:

> **No E408 h13 T61 residual can realize the |W|=23 Cell B normal form.**

This is unconditional relative to the contextual T61 contract and the cited extremal theorems; it does not use the V11 retained lower-order seeds.

## 8. E407 Cell B is rigid

For E=407,

`Delta(F)<=20`.

Thus Cell B forces

> **`d_F(w)=20`,**

so w has no target neighbours outside W.

The total target excess over13 is21. The vertex w alone contributes

`20-13=7`.

Hence all remaining60 vertices together have only14 target-excess units.

Equivalently, if O=V(F)\W and the two K11 sides of the Cell B target graph are denoted A,B, then writing

`d_F(s,O)=2+a_s` for `s in A union B`,

and

`kappa_o=d_F(o)-13` for `o in O`,

we obtain the exact defect ledger

> **`sum_s a_s + sum_o kappa_o =14`.**

Moreover `d_F(w,O)=0`.

Thus E407 Cell B is a 14-defect extension problem.

## 9. Interface with the current Q32/Q33 frontier

The V11 source-reported frontier remains

- E407: Q32 open;
- E408: Q32,Q33 open.

The present theorem does not by itself eliminate those charge cells. It supplies new independent constraints that every completion must satisfy:

- E408 globally has target maximum degree19 and cannot use the sharp |W|=23 Cell B design;
- E407 globally has target maximum degree20;
- any E407 |W|=23 Cell B completion has an externally target-isolated subdivision vertex and only14 residual excess units outside it.

These constraints should be intersected with the Q32/Q33 shell/core completion systems rather than treated as a separate case tree.