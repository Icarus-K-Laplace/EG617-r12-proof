# Geometric Extraction Theorem — Current Status

Status: **Conditional local extraction PROVED; global extraction OPEN**.

## Theorem K.G1 — Conditional two-direction extraction

Let a hypothetical counterexample to P(q) be given, with q>=3. Fix x and W=V minus {x}. If two colors i,j have local slacks

\[
1\le s_i(x),s_j(x)\le q-2,
\]

then the q^2 points W carry two orthogonal partitions into q monochromatic K_q blocks. Every block in either partition meets every block in the other in exactly one point.

For each color k in {i,j}, let E_k be its s_k cross-block defect edges. The extra vertex x determines a color label on every point of W. The non-k neighbors of x in each k-block form nonempty sets B_a^k, and E_k must block every transversal choosing one such non-k neighbor from each of the q blocks. The one-block forcing gives q-s_k attachments to x; the weighted blocker strengthens this to

\[
d_k(x)\ge2q-s_k(x)-1.
\]

Consequently, writing e_k=m_q+q+a_k gives

\[
\boxed{a_k\ge q-1}
\]

for every color k that is low-slack at x.

## Theorem K.G2 — Weighted defect-edge obstruction

If B_1,...,B_q are nonempty residual parts of sizes b_a and the induced defect-edge graph F has no independent transversal, then

\[
\sum_{uv\in E(F)}\frac{1}{b_{a(u)}b_{a(v)}}\ge1,
\qquad
|E(F)|\ge\min_{a<b}b_ab_b.
\]

This is proved in TRANSVERSAL_BLOCKER_LEMMA.md. Only defect edges with both endpoints in the residual parts contribute. The exact one- and two-edge cases are classified in SMALL_SLACK_BLOCKER_CLASSIFICATION.md.

## Theorem K.G3 — Interface with the tight-transversal branch

See the J-branch theorem TIGHT_TRANSVERSAL_LOW_SLACK_BRIDGE.md.

Conditionally assume the robust shell hypergraph has matching number two, its minimum transversal X has size 2q, x_0 belongs to X, and a color i != c has low slack 1<=s_i(x_0)<=q-2 on W=V minus {x_0}. Then Y=X minus {x_0} hits every independent q-set of G_i[W]. Any private witness of color i based in block P_a forces the residual part B_a=P_a minus Y to have size at most s_i; if some B_a is empty, all witnesses of color i must be based in that full block. Therefore at most floor((2q-1)/(q-s_i)) blocks can host private witnesses of color i.

If s_i=1 or 2, the exact small-blocker classification further confines the witnesses to at most two blocks for q>=4 (and for s_i=1 also when q=3).

This is a rigorous cross-workstream bridge, but the alignment premise remains OPEN.

## Theorem K.G4 — Universal global excess and local low-slack count

The exact average-slack identity and the two-block degree bound imply

\[
\boxed{a_i\ge q-1\quad\text{for every color }i.}
\]

For any vertex x and threshold 1<=s<=q-2, the number of colors with s_i(x)<=s is at most

\[
\boxed{\left\lfloor\frac{q^2}{2q-s-1}\right\rfloor,}
\]

because every such color contributes at least 2q-s-1 to the degree of x. More precisely,

\[
\sum_{i:s_i(x)\le q-2}(2q-s_i(x)-1)\le q^2.
\]

Proofs and the universal excess-floor argument are in LOW_SLACK_COORDINATIZATION.md and HIGH_SLACK_ALTERNATIVE.md. This is a genuine multicolor degree-budget constraint, but does not force two low-slack colors at a common vertex.

## What is not proved

- No global theorem forces two colors to satisfy 1<=s_i(x),s_j(x)<=q-2 at a common vertex x.
- No theorem forces a low-slack color to occur at a vertex x_0 inside the tight transversal X.
- Two orthogonal partitions give a 2-net, not a full affine plane.
- The positive-slack transversal-blocking systems have not been shown incompatible.

## Exact route to a finite-geometry contradiction

A valid completion would need to prove one of:

1. at least three pairwise orthogonal direction classes with relevant blocks identified;
2. a completion theorem whose hypotheses match the extracted incidence structure;
3. a direct contradiction from defect edges, the extra-vertex color matrix, and the witness-block concentration bound.

Only after proving that a shell contains full size-q blocks in distinct directions, with pairwise intersections at most one, may the partial Kakeya union bound be applied. The current theorem does not yet provide such a shell or three-direction family.