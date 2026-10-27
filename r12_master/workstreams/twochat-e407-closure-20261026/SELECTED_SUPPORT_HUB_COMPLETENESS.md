# E407 Q32 — selected-support hub completeness across all five templates

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL on the frozen V12 shell-template contract, selected-support component identity, and selected B-anchor floor. Necessary structure only; E407 Q32 remains OPEN.**

## 1. Setup

Work under the current E407 Q32 contract. For each exact-129 color c, its seven selected support blocks are pairwise-disjoint independent four-sets in U and are the core parts of seven isolated color-c K5 components. Let

\[
\mathcal B_c=\{Q:\text{the selected anchor of }Q\text{ lies in }B\},
\qquad b_c=|\mathcal B_c|.
\]

The selected-anchor theorem gives

\[
\boxed{b_c\in\{5,6,7\}}.
\]

For a shell vertex a write

\[
D_a=N_F(a)\cap H.
\]

For every regular B row b in E407 Q32,

\[
|D_b|=k_b=|N_M(b)\cap S|\le3.
\]

Call a support block Q **hub-complete** if it intersects all three hub rows D_s, s in S.

## 2. Fixed-full-row lemma

### Theorem 2.1

Assume the shell template contains at least one full B row f, i.e.

\[
N_M(f)\cap S=S,
\qquad |D_f|=3.
\]

Then, in every exact-129 color c, at most three blocks in \(\mathcal B_c\) fail to be hub-complete. Consequently

\[
\boxed{\#\{Q\in\mathcal B_c:Q\text{ hub-complete}\}\ge b_c-3\ge2.}
\tag{2.1}
\]

### Proof

Let Q in \(\mathcal B_c\) fail to be hub-complete, and choose a hub s with

\[
Q\cap D_s=\varnothing.
\]

Suppose also that Q misses D_f. Then:

- Q is an independent four-set in the target graph;
- f is target-anticomplete to Q because Q misses D_f;
- s is target-anticomplete to Q because Q misses D_s;
- fs is a missing shell edge because f is a full row.

Therefore \(Q\cup\{f,s\}\) is an independent six-set in F, contradicting \(\alpha(F)\le5\). Hence every non-hub-complete Q in \(\mathcal B_c\) must satisfy

\[
Q\cap D_f\ne\varnothing.
\]

The seven selected support blocks of one exact color are pairwise disjoint. Thus distinct non-hub-complete blocks consume distinct points of D_f. Since \(|D_f|=3\), there are at most three of them. This proves (2.1). QED.

### Corollary 2.2 — global selected-support floor

Let

\[
B_{\rm sel}=\sum_c b_c.
\]

Whenever a full row exists,

\[
\boxed{N_{\rm hub}^{\rm sel}\ge\sum_c(b_c-3)=B_{\rm sel}-21\ge14.}
\tag{2.2}
\]

These are genuine members of the 49 selected support blocks on the common U, not auxiliary component witnesses.

## 3. Which V12 templates have a full row

The audited V12 row-count constraints are:

- A: row counts \(n_0,n_1,n_3\), with \(3n_0+2n_1\le8\);
- B: \(n_0,n_2,n_3\), with \(3n_0+n_2\le8\);
- C: \(n_0,n_1,n_3\), with \(3n_0+2n_1\le9\);
- D: \(n_0,n_a,n_b,n_3\), with \(3n_0+n_a+n_b\le9\);
- E: \(n_0,n_1,n_2,n_3\), with \(3n_0+2n_1+n_2\le10\).

In every case the row counts sum to ten.

Elementary integer minimization gives

\[
n_3(A)\ge6,\qquad n_3(B)\ge2,\qquad n_3(C)\ge6,\qquad n_3(D)\ge1.
\]

Thus Theorem 2.1 applies unconditionally within each retained A-D shell contract.

For E, either \(n_3\ge1\), in which case Theorem 2.1 applies, or \(n_3=0\). In the latter case the two equations

\[
n_0+n_1+n_2=10,
\qquad 3n_0+2n_1+n_2\le10
\]

force

\[
\boxed{n_0=n_1=0,\qquad n_2=10.}
\tag{3.1}
\]

So every B row is exactly the ends-pair row of the P3 missing graph on S.

## 4. Template E with no full row

Let the two endpoints of the P3 on S be \(s_L,s_R\). Under (3.1), every B label b is missing to both endpoints.

### Theorem 4.1 — selected endpoint-complete floor

Assume template E and \(n_3=0\). Then every selected B-anchored support block Q is endpoint-complete:

\[
\boxed{Q\cap D_{s_L}\ne\varnothing,
\qquad Q\cap D_{s_R}\ne\varnothing.}
\tag{4.1}
\]

Hence every exact color has at least five selected endpoint-complete blocks and globally

\[
\boxed{N_{\rm end}^{\rm sel}\ge\sum_c b_c=B_{\rm sel}\ge35.}
\tag{4.2}
\]

### Proof

Let Q be selected with B anchor b. Since \(Q\cup\{b\}\) is a non-target monochromatic K5 component, b is target-anticomplete to Q, i.e. \(Q\cap D_b=\varnothing\).

Fix an endpoint s in \(\{s_L,s_R\}\). The shell edge bs is missing. If Q also missed D_s, then \(Q\cup\{b,s\}\) would be an independent six-set in F, contradicting \(\alpha(F)\le5\). Thus Q meets both endpoint rows. Since \(b_c\ge5\), (4.2) follows. QED.

## 5. All-five-template conclusion

The actual 49-block system therefore satisfies one of the following, with no auxiliary-witness substitution:

| V12 template | selected-support consequence |
|---|---|
| A | at least 2 hub-complete selected B-blocks per exact color; at least 14 globally |
| B | same |
| C | same |
| D | same |
| E, \(n_3\ge1\) | same |
| E, \(n_3=0\) | at least 5 endpoint-complete selected B-blocks per exact color; at least 35 globally |

More precisely, in every full-row branch the floor is

\[
N_{\rm hub}^{\rm sel}\ge B_{\rm sel}-21,
\]

so colors with \(b_c=6\) or 7 contribute at least three or four selected hub-complete blocks respectively.

## 6. Dependency and audit classification

This theorem uses:

1. **Pure T61 graph contract:** \(\alpha(F)\le5\), the shell/core decomposition, and the six-set contradiction;
2. **V12 shell contract:** the five row-type systems and \(|D_b|=k_b\le3\) for regular B rows;
3. **Labelled exact-129 contract:** selected support blocks are selected K5 core parts, are disjoint within one color, and \(b_c\ge5\).

It does **not** use the Didin-dependent delta=14 saturated branch, Brouwer/Kang-Pikhurko beyond the already-registered parent exact-factor theorem, or any delta=13/14/15/16 terminal classification.

The finite verifier checks only the row-count arithmetic and the resulting block-count floors. The graph-theoretic proof is the six-set argument above.

## 7. Remaining gap

The old label-transfer firewall is now substantially smaller: for A-D and the full-row E branch, at least fourteen **actual selected support blocks** in the common 29-point system are hub-complete; in the exceptional E branch at least thirty-five actual selected blocks hit both P3 endpoints.

No contradiction with the 284-edge core has yet been derived. The next step is to combine these selected-block hit requirements with support multiplicities, anchor injectivity, the U/W omission ledger, and exact shell-color ownership.