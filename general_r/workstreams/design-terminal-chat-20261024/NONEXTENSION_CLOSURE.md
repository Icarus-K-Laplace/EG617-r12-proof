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
