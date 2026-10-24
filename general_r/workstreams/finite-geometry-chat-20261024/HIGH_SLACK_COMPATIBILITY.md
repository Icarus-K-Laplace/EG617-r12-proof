# High-Slack Compatibility: Local Slack Gap Theorem

Date: 2026-10-24  
Status: **PROVED under the full hypothetical-counterexample contract. The high-slack contradiction remains OPEN.**

## 1. Contract

Let \(q\ge3\), and suppose a q-edge-coloring of \(K_{q^2+1}\) is a hypothetical counterexample to EG617: every \((q+1)\)-vertex set contains all q colors. Fix a vertex x, let \(W=V\setminus\{x\}\), and define
\[
m_q=q\binom q2,\qquad
s_i(x)=e(G_i[W])-m_q.
\]
Since \(\alpha(G_i[W])\le q\), the Turán-complement floor gives \(s_i(x)\ge0\).

## 2. Theorem I.HS1 — No local slack below q-1

**Theorem.** For every vertex x and color i,
\[
\boxed{s_i(x)\ge q-1.}
\]
Equivalently, the branch \(s_i(x)\le q-2\) is impossible in a full hypothetical counterexample. This is stronger than merely bounding the number of low-slack colors.

### Proof

Assume \(s=s_i(x)\le q-2\). The existing Brouwer low-slack structure theorem applies to \(G_i[W]\): W splits into q disjoint blocks \(A_1,\ldots,A_q\), each a monochromatic \(K_q\) of color i, plus exactly s color-i defect edges crossing between blocks.

**First constraint: each block contributes at most one i-neighbor of x.** For each a, the set \(\{x\}\cup A_a\) has q+1 vertices and must contain all q colors. Its internal edges already all have color i, so the q edges from x into \(A_a\) must include every one of the other q-1 colors. Consequently at most one of these q edges can have color i. Summing over the q blocks gives
\[
d_i(x)\le q.\tag{1}
\]

Let \(B_a=A_a\setminus N_i(x)\), the vertices of block a whose edge to x is not color i, and write \(b_a=|B_a|\). Each \(B_a\) is nonempty: otherwise x together with the entire block \(A_a\) is monochromatic in color i.

If s=0, the block partition has no cross-block color-i defect edges. Choosing one vertex from each nonempty \(B_a\) then gives a color-i-independent q-set whose vertices all avoid color i to x, contradicting the counterexample property. Hence s≥1.

For s≥1, the defect edges with both endpoints in the B-parts must block every independent transversal of \(B_1,\ldots,B_q\); otherwise that transversal plus x misses color i. Apply the already-proved weighted blocker lemma to this graph F:
\[
\sum_{uv\in E(F)}\frac1{b_{a(u)}b_{a(v)}}\ge1.
\]
It follows that \(|E(F)|\ge\min_{a<b}b_ab_b\). Since \(|E(F)|\le s\), some pair of parts has \(b_ab_b\le s\). For positive integers this implies \(b_a+b_b\le s+1\). All other q-2 parts have size at most q, so
\[
\sum_{a=1}^q b_a\le(q-2)q+s+1.
\]
But \(d_i(x)=\sum_a(q-b_a)=q^2-\sum_a b_a\), hence
\[
d_i(x)\ge2q-s-1\ge q+1,\tag{2}
\]
because s≤q-2. Equations (1) and (2) contradict each other. Therefore s_i(x)≥q-1. QED.

## 3. Immediate consequences and precise scope

1. **The high-slack branch is now forced locally:** every color at every vertex has \(s_i(x)\ge q-1\). The former alternative “at most one low-slack color at x” is not the right remaining branch; there are no such colors at all.
2. Using \(s_i(x)=q+a_i-d_i(x)\), the theorem also gives the pointwise degree cap
   \[
   d_i(x)\le a_i+1.
   \]
3. The average identity \(\sum_x s_i(x)=q(q-1)+(q^2-1)a_i\) recovers \(a_i\ge q-1\) for integer \(a_i\), but does not improve that global excess floor.
4. The theorem does **not** prove a contradiction: \(\sum_i s_i(x)=m_q\) is compatible with all q slacks being at least q-1 for q≥3.
5. The prior low-slack coordinatization, blocker classification, and slack-one crossed-pattern theorems remain valid as conditional graph lemmas. Under the full counterexample contract their premises \(s_i(x)\le q-2\), including slack one, are empty. They must not be presented as realizable local patterns of a counterexample.
6. This theorem is not an H seed-floor theorem. H's seed states are arbitrary induced residual graphs on \(ar+O(1)\) vertices with \(\alpha\le a\), not q²-point neighborhoods satisfying the full-color block-plus-x contract. A separate bridge is required.

## 4. Dependency audit

The proof uses:
- the already-established low-slack structure theorem for \(0\le s_i(x)\le q-2\);
- the already-established weighted independent-transversal blocker lemma;
- the defining counterexample property on every \((q+1)\)-set.

It does not assume a second low-slack color, affine-plane coordinatization, or prime-power structure. No external theorem is added in this step.
