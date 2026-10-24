# Nonextension closure: exact identities and defect-chain obstruction

## Status

- **PROVED_ANALYTIC:** exact affine/net nonextension under its exact partition hypotheses (upstream result).
- **PROVED_ANALYTIC:** the naive exact (RTD(5,r)+) one-point completion is invalid.
- **PROVED_ANALYTIC:** the target condition (\alpha(G_0)\le5) forces every non-target (G_i) to be (K_6)-free.
- **OPEN:** robust nonextension for every terminal satisfying the current near-design contract.
- **OPEN:** a global defect-chain budget closing all non-target cylinder covers.

## 1. Exact cross-pair budget

Let (a_j=|B_j|), (n=5r+1), and
[
C=\sum_{j<k}a_ja_k
]
be the number of cross-group pairs. Let (D) be the number of target-ideal internal edges deleted from the actual target graph, and (A) the number of actual target edges between distinct target groups. Let (S_{\rm non}=\sum_{i>0}s_i), and
[
\Delta_0=\sum_j\binom{a_j}{2}-p_5(n).
]
Then
[
s_0=\Delta_0-D+A,
\qquad
\boxed{A=C+D-(r-1)(10r+5)-S_{\rm non}.}
]
Equivalently,
[
\boxed{A=9r+5-\Delta_0+D-S_{\rm non}.}
]
Since (s_0\ge r),
[
\boxed{A\ge r-\Delta_0+D.}
]
These identities count each actual edge once. A target-deleted internal pair belongs to exactly one non-target color; it is not a target cross edge.

The cylinder lower bounds cannot simply be summed over all target deletions: multiple deletions may share a hub star. The proof needs a joint cover argument, not independent per-edge charges.

## 2. Joint K6 constraint on cheap cylinder covers

The local one-color construction that deletes a repeated pair (uv) and joins one endpoint to all five vertices of a clean transversal block (C) can force (\alpha(G_i)\le r) at constant edit cost. But it creates (C\cup\{u\}\cong K_6) in (G_i), hence an independent 6-set in the target graph. It is forbidden by the full terminal contract.

Therefore any valid one-block cylinder cover must make the cover block non-clique in the actual non-target color, creating another defect. That defect itself needs a cover. This starts a defect-propagation chain, but the chain's total cost has not yet been bounded.

A previously proposed (d_i=6) local pattern was withdrawn after checking independent sets that double two missing pairs and omit the special cover block. It is not a valid counterexample to the per-color independence condition and must not be used.

## 3. What exact nonextension currently proves

The existing exact affine/net result is usable only if its exact orthogonal-partition hypotheses have been established. The current terminal gives a partial resolvable (TD(5,r)) with (r^2-O(r)) clean blocks; it does not give an exact net or two exact orthogonal partitions on the needed point set.

The exact (RTD(5,r)+) one-point completion was already rejected: it violates the target clique cap and, even if that cap is ignored, yields a target-independent six-set. This rules out that particular exact template, not all near-design completions.

## 4. Minimum missing theorem

Prove a **defect-chain cost theorem**:

> Every chain/cycle of non-target missing pairs and cylinder covers that keeps every non-target color (K_6)-free must either exceed the combined non-target slack and target cross-cover budget, or produce an omitted-color ((r+1))-set.

The proof must track pair ownership exactly and cannot assume an affine plane exists. Until then, robust nonextension remains **OPEN**, and no sufficiently-large-(r) terminal closure is claimed.


## 5. New local obstruction: a two-defect cycle can close cheaply

A fully checked one-color block gadget has:
- one 6-block with a single missing pair;
- one 5-block with a single missing pair;
- nine cross-block additions;
- (\alpha(G_i)\le r) and (K_6)-freeness;
- slack (s_i=7), edit distance (11).

The explicit construction and proof are in `HUB_PROPAGATION_THEOREM.md`. It is not a target-labelled full terminal, but it disproves the local inference that K6-freeness forces every cylinder cover to generate an additional defect or that the local slack must exceed 8.

## 6. Exact target-label obstruction

Suppose a target hub (w\in B_j) has a target cross-star into (B_k), and (x\in B_k) lies with (w) in a non-target ideal block. Then (wx) is a target-colored edge missing from that non-target color. For any candidate cover block, its (B_k)-representative (z) cannot be adjacent in the non-target color to either (w) or (x) when (z\notin X): both (wz) (target star) and (xz) (ordinary internal target edge) belong to color 0.

Therefore a one-block cover must use an exceptional point in (X\), while an ordinary point forces a cover using other selected blocks or further target-internal deletions. This is the valid interface between target stability and non-target independence.

However, a fixed blocked coordinate can be handled locally by a 9-edge two-coordinate barrier. Thus a lower bound must account for the complete multi-block constraint network and pair ownership, not only one cylinder.

## 7. Updated minimum missing theorem

The missing theorem is now more precise:

> Under the exact target labels and pair-ownership rule, the total cost of all hub-block defects and all multi-block barriers across the (r-1) non-target colors exceeds the remaining global budget, unless an omitted-color ((r+1))-set exists.

The block-level slack bound (s_i\ge9) is false in general (the local gadget has (s_i=7)); any proof must use the target labels and cross-color compatibility essentially. Robust nonextension remains **OPEN**.
