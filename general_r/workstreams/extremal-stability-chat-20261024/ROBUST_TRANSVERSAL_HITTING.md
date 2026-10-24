# Robust Transversal-Hitting — F-004

## Theorem RT-1: weighted defect-aware transversal hitting

Let H be a graph partitioned into q nonempty parts V_1,...,V_q of sizes n_j. Let A hit every K_q of H. Put a_j=|A intersect V_j|, and let b_jk count missing edges between V_j and V_k.

Choose X_j independently and uniformly from V_j, and let T={X_1,...,X_q}. If T avoids A, it cannot be a K_q, so it contains a missing cross-edge. These two events cover the sample space. By the union bound,
**1 <= sum_j a_j/n_j + sum_(j<k) b_jk/(n_j n_k).**

This allows arbitrary part sizes, arbitrary missing-edge placement, and overlap between the sets of transversals blocked by different missing edges. It does not assume that defect costs add disjointly.

If every n_j>=L>0, d=|A|, and b=sum b_jk, then 1<=d/L+b/L^2. Thus, when d<L,
**b >= L(L-d).**

## Application to EG617

For each color i, A_i=N_i(x) hits every K_r in H_i=complement(G_i): a K_r avoiding A_i, together with x, would omit color i.

Füredi's partition lemma applied to H_i gives an r-partition with at most 2s_i missing cross-edges. If s_i<r^2/4, the exact partition identity gives sum_a(n_a-r)^2<=4s_i, so every part has size at least L=r-2sqrt(s_i)>0. Therefore
1<=d_i/L+2s_i/L^2.

This proves the joint tradeoff in SLACK_NEIGHBORHOOD_TRADEOFF.md.

## Boundary audit

- If a partition has an empty part, this lemma cannot be applied to that partition. The EG617 application avoids this by requiring L>0.
- Internal edges within parts do not enter the transversal count because only one vertex is selected from each part; they consume a separate Füredi defect budget.
- A missing cross-edge may block many transversals. Its probability contribution is b_jk/(n_j n_k), so shared blockers are handled without double-counting.
- Equality in the union-bound estimate would require a special overlap pattern; no equality classification is claimed.
- The lemma is a hitting-cost inequality, not an exact skeleton reconstruction theorem.

## Status

- Weighted transversal lemma: PROVED_ANALYTIC.
- EG617 slack-neighborhood application: PROVED_CONDITIONAL on Füredi's partition lemma.
- Exact skeleton reconstruction: OPEN.
