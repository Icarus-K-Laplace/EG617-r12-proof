# E407 Q32 — full-row linearity capacity for selected support blocks

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL on the frozen V12 row contract, selected-support anchor identity, and pairwise linearity of the 49 support blocks. Necessary structure only; E407 Q32 remains OPEN.**

## 1. Setup

Let R be the set of full B rows in the current shell template:

\[
R=\{b\in B:k_b=3\},\qquad h=|R|.
\]

For every full row b, \(|D_b|=3\). Let \(\mathcal N\) be the family of selected B-anchored support blocks which are **not** hub-complete.

Every Q in \(\mathcal N\) misses at least one hub s. Since every full row b is missing to every hub, the six-set argument forces

\[
Q\cap D_b\ne\varnothing\qquad\text{for every }b\in R.
\tag{1.1}
\]

Thus every Q in \(\mathcal N\) is a simultaneous transversal of all h full rows.

For u in U define

\[
d(u)=|\{b\in R:u\in D_b\}|.
\]

Because each full row has only three core neighbours,

\[
D:=\sum_{u\in U}d(u)\le3h,
\tag{1.2}
\]

with strict inequality if some full-row neighbour lies in W.

## 2. Point capacity from B-anchor injectivity

Let z(u) be the number of blocks of \(\mathcal N\) containing u.

Two independent restrictions apply.

1. A support point belongs to at most seven selected blocks, so \(z(u)\le7\).
2. The B-anchor labels on selected blocks through one support point are pairwise distinct. Moreover, if u is target-adjacent to a B label b, then a selected block through u cannot be anchored at b, because the anchor edge bu would have the exact non-target color of that K5 component. Since u is target-adjacent to at least d(u) B labels from the full-row set,
   \[
   z(u)\le10-d(u).
   \]

Hence

\[
\boxed{z(u)\le a(d(u)):=\min\{7,10-d(u)\}.}
\tag{2.1}
\]

## 3. Quadratic linearity bound

The 49 support blocks are pairwise linear: any pair of U points occurs together in at most one selected block. For every Q in \(\mathcal N\), (1.1) gives

\[
\sum_{u\in Q}d(u)\ge h.
\]

Therefore

\[
|\mathcal N|h^2
\le
\sum_{Q\in\mathcal N}\left(\sum_{u\in Q}d(u)\right)^2.
\tag{3.1}
\]

Expand the right side. The diagonal contribution is

\[
\sum_{u\in U}z(u)d(u)^2.
\]

For distinct u,v, pairwise linearity says the pair \(\{u,v\}\) occurs in at most one Q, so the off-diagonal contribution is at most

\[
2\sum_{u<v}d(u)d(v).
\]

Using (2.1),

\[
|\mathcal N|h^2
\le
\sum_u a(d(u))d(u)^2+2\sum_{u<v}d(u)d(v)
\]
\[
=
D^2+\sum_u\bigl(a(d(u))-1\bigr)d(u)^2.
\tag{3.2}
\]

For every integer \(0\le d\le10\),

\[
\bigl(\min\{7,10-d\}-1\bigr)d^2\le20d.
\tag{3.3}
\]

This is immediate for d=0,1,2,3; equality occurs at d=4,5; the values then decrease relative to 20d for d>=6. Hence, using D<=3h,

\[
|\mathcal N|h^2
\le D^2+20D
\le9h^2+60h.
\]

We obtain the global capacity theorem

\[
\boxed{|\mathcal N|\le\left\lfloor9+\frac{60}{h}\right\rfloor.}
\tag{3.4}
\]

Independently, any single full row has only three core neighbours and each point belongs to at most seven selected blocks, so

\[
|\mathcal N|\le21.
\tag{3.5}
\]

Combining,

\[
\boxed{|\mathcal N|\le C(h):=\min\left\{21,\left\lfloor9+\frac{60}{h}\right\rfloor\right\}.}
\tag{3.6}
\]

## 4. Selected hub-complete consequences

Let

\[
B_{\rm sel}=\sum_c b_c\ge35
\]

be the total number of selected B-anchored support blocks. Every such block is either in \(\mathcal N\) or is hub-complete. Thus

\[
\boxed{N_{\rm hub}^{\rm sel}\ge B_{\rm sel}-C(h).}
\tag{4.1}
\]

The capacity table is:

| h full rows | C(h) | hub-complete floor from Bsel>=35 |
|---:|---:|---:|
| 1-5 | 21 | 14 |
| 6 | 19 | 16 |
| 7 | 17 | 18 |
| 8 | 16 | 19 |
| 9 | 15 | 20 |
| 10 | 15 | 20 |

Consequently, because the V12 contracts force h>=6 in templates A and C,

\[
\boxed{N_{\rm hub}^{\rm sel}\ge16\quad\text{in A and C}.}
\tag{4.2}
\]

This improves the previous universal full-row floor 14. If a surviving A/C row profile has h>=7,8,9, the floor automatically strengthens to 18,19,20.

Templates B/D and the full-row branch of E retain the safe floor 14 unless their actual profile has h>=6.

## 5. Why this is a genuine common-core theorem

The proof uses simultaneously:

- the five-template full-row system;
- actual selected B-anchored support blocks on the common U;
- pairwise linearity of the 49-block family;
- pointwise anchor injectivity;
- the fact that target adjacency to a B label forbids that label as an exact selected anchor at the same support point.

It is therefore stronger than a shell-only count and stronger than the earlier auxiliary-component witness packing.

No delta=13/14/15/16 classification and no Didin-dependent theorem is used.

## 6. Remaining gap

Even the improved A/C floor of sixteen hub-complete selected blocks is not yet inconsistent with the 284-edge core. The next step is to use the exact support multiplicities \(m_u=7-r_u\), the U/W degree identity, or the target-excess/color-premium ledger to show that a family of this size cannot be supported by the 32+beta S-to-core target edges and the four units of core-internal excess.