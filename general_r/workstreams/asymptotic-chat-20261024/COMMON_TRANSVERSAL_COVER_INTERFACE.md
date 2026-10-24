# Common Transversal-Cover Interface for C and D

**Status:** PROVED_SYMBOLIC; terminal closures remain OPEN.  
Branch: workstream/general-r-asymptotic-20261024  
Date: 2026-10-24

## 1. Abstract transversal-cover lemma

Let G be a graph and let B_1,...,B_s be pairwise disjoint nonempty vertex sets. A transversal is a tuple (x_1,...,x_s) with x_i in B_i.

### Theorem 1 — weighted cover

If every transversal contains at least one edge of G, then
\[
\boxed{\sum_{1\le i<j\le s}
\frac{e_G(B_i,B_j)}{|B_i||B_j|}\ge1.}
\]

**Proof.** Choose each x_i independently and uniformly from B_i. Let Z count the G-edges among the selected vertices. By hypothesis Z≥1 for every outcome. On the other hand,
\[
\mathbb E Z
=\sum_{i<j}\Pr(x_ix_j\in E(G))
=\sum_{i<j}\frac{e_G(B_i,B_j)}{|B_i||B_j|}.
\]
Thus E Z≥1. QED.

### Theorem 2 — fixed defect-pair cover

Suppose uv is a nonedge of G, alpha(G)≤s+1, and B_1,...,B_s are pairwise disjoint and disjoint from {u,v}. Then every set
\[
\{u,v,x_1,\ldots,x_s\},\qquad x_i\in B_i,
\]
contains a G-edge. Consequently,
\[
\boxed{
\sum_{i=1}^s\frac{d_G(u,B_i)+d_G(v,B_i)}{|B_i|}
+\sum_{i<j}\frac{e_G(B_i,B_j)}{|B_i||B_j|}
\ge1.}
\]

The proof is the same expectation argument, now with the fixed nonedge uv omitted from the edge count.

If all |B_i|≥L and A is the total number of G-edges among the auxiliary groups, this implies
\[
d_G(u,\cup_i B_i)+d_G(v,\cup_i B_i)\ge L-A/L.
\]
The direction is important: each edge-event probability is at most 1/L or 1/L², so the union bound gives 1≤d/L+A/L².

## 2. Exact application to C: clean pair-exchange design

Let P_1,...,P_m be pairwise-disjoint clean target K_2 blocks in the residual core H. For any four distinct blocks, choose one endpoint from each. Since alpha(H)≤3, the four chosen vertices contain an H-edge. Apply Theorem 1 with s=4 and |P_i|=2:
\[
\sum_{i<j}\frac{e_H(P_i,P_j)}4\ge1.
\]
Thus every four-block subsystem has at least four cross-block H-edges.

The stronger, separately certified finite 2-SAT audit says that because each block-pair interaction is a partial matching of K_2,2, an unsatisfiable four-block system needs at least **six** cross-block H-edges. Double-counting over all four-subsets gives
\[
E_{\mathrm{cross}}\binom{m-2}{2}
\ge6\binom m4,
\qquad
\boxed{E_{\mathrm{cross}}\ge\binom m2.}
\]

This is a rigorous global necessary condition. It is not a contradiction: the known high-density reduction leaves the nonempty linear interval
\[
\left\lceil\frac{4r}{3}+3\right\rceil
\le m\le\left\lfloor\frac{3(r-1)}2\right\rfloor.
\]
So Theorem 1 unifies the cover mechanism, while the exact 2-SAT strengthening is specific to the clean-pair structure.

## 3. Exact application to D: TD(5,r) terminal

Let G_0 be the target graph with alpha(G_0)≤5. Let B_1,...,B_5 be the five target ideal groups. If uv is a target-missing pair inside B_j, choose one point from each of the other four groups. Together with u,v this is a six-set, so it cannot be independent in G_0. Theorem 2 applies to the four auxiliary groups.

Write L=min_i |B_i| and let A be the total target cross-group edge count. Then
\[
d_{\mathrm{cross}}(u)+d_{\mathrm{cross}}(v)\ge L-A/L.
\]
Under the current D stability bounds, L≥r−26 and A≤27r+15. Hence each target-internal defect has an endpoint with cross-degree at least
\[
H_r/2,\qquad
H_r=(r-26)-\frac{27r+15}{r-26}=r-53+o(1).
\]
For r≥1000 the existing source proves the resulting hub set has size at most 114.

This recovers the certified bounded-hub concentration interface. It does **not** close the next step: the non-target K_6-free condition forces a new defect when a one-block star cover is used, but the global defect-chain/cycle cost is OPEN.

## 4. Relation to the residual-core pivot system

The common-S pivot system is linked through different exact identities:
- common-S owners plus pivot form a regular target clique;
- the multicolour capacity gives N≤(r−3+2epsilon+epsilon sqrt(4epsilon+1))/2;
- d2 repivot transitions obey d_i(y_j)=2−|D_i intersect D_j|.

No theorem currently maps every core support block to a target group of the TD(5,r) terminal. Therefore this note does not identify the objects or claim that Theorem 2 alone closes C*.

## 5. Synthesis conclusion

The C and D terminal interfaces share a precise, proved transversal-cover accounting principle. Their stronger consequences differ:
- C needs the finite 2-SAT matching refinement and then a strict global clean-pair nonextension inequality;
- D needs defect propagation beyond the bounded hub kernel.

This closes the **common counting-interface question**, not the full C or D terminal nonextension theorem. No unconditional all-large-r result follows from this lemma alone.
