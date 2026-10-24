# R12 exact-129 high-support witness theorem — corrected

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** on the retained T61 shell contract and the exact-129 Kang–Pikhurko factor theorem.  
This file supersedes the earlier version on this branch. The previous five-component boundary split was unnecessarily weak; the corrected count is six B-labelled components.

## 1. Frozen contract

Let F be a 61-vertex T61 residual with pivot p, shell A=S dot-union B, |S|=3, |B|=10, and core H of size 47. Assume:
- alpha(F)<=5 and alpha(H)<=4;
- B is a target clique, equivalently M[B] is empty for M=bar(F[A]);
- the relevant shell contract gives h=|{b in B: k_b>=2}|>=5, where k_b=|N_M(b) intersect S|;
- every exact-129 non-target color C has ten vertex-disjoint isolated K5 components and an 11-vertex exceptional gadget, under the registered equality-classification contract.

For E407 Q32, the registered row-profile floors are h>=6,8,6,7,5 for templates A,B,C,D,E respectively. For E408 Q33/d3, the exact budget gives h>=6 when beta=e(M[S]) is 0 or 1, and h>=5 when beta is 2 or 3. Thus h>=5 is uniform over the eligible interfaces.

## 2. Correct component count

**Lemma 2.1.** Every exact-129 color has at least seven K5 components avoiding S, and at least six of those have the form {b} union Q with b in B and Q subset H, |Q|=4. The six B labels are distinct, the Q sets are pairwise disjoint within the color, and Q is independent in H and anticomplete to b.

**Proof.** The ten K5 components are vertex-disjoint, and only three vertices belong to S, so at least seven components avoid S. At most one of these can contain p. A component avoiding both S and p lies in B union H. It contains at most one B vertex because B is a target clique. It cannot lie entirely in H because that would be a target-independent five-set in H, contradicting alpha(H)<=4. Hence each such component is {b} union Q with four core vertices. At least six such components exist. Their labels are distinct because the components are disjoint. ∎

Across distinct non-target colors, any two selected Q sets intersect in at most one vertex: sharing two core vertices would assign their common edge two colors.

## 3. High-support witness in every exact-129 color

**Theorem 3.1.** Under the frozen contract, every exact-129 color contains a B-labelled no-S component {b} union Q for which k_b>=2. In particular, Q must meet at least two distinct hub rows from S.

**Proof.** Let L_C be the set of B labels of the at least six components in Lemma 2.1. They are distinct, so |L_C|>=6. There are only 10-h<=5 labels b with k_b<=1. Therefore L_C contains a label b with k_b>=2.

For each s in N_M(b) intersect S, the pair bs is target-nonadjacent. If Q also missed s, then Q union {b,s} would be a target-independent six-set: Q is independent in H, b is anticomplete to Q, and s is anticomplete to Q. This contradicts alpha(F)<=5. Thus Q hits every hub in N_M(b) intersect S, at least two distinct hubs. ∎

This eliminates the earlier h=5 “low-only” branch: six B-labelled components cannot all use the five low labels. No exact-star assumption is used.

## 4. Zero-excess witnesses

Let X={x in H:d_H(x)>12}. Since the 284-edge core has sum(d_H-12)=4, |X|<=4. The six B-labelled Q sets in Lemma 2.1 are pairwise disjoint. At most four of them can meet X, so every exact-129 color has at least two B-labelled witnesses Q whose four vertices all have core degree exactly 12.

Therefore:
- E407 Q32 has at least 14 pairwise-linear zero-excess B-labelled witnesses across its at least seven exact-129 colors.
- E408 Q33 has at least 16 across its at least eight exact-129 colors.

This is conditional only on the registered exact-129 factor theorem and the stated shell/core contract.

## 5. Boundary interfaces

Use the separate file R12_WITNESS_PACKING_BOUNDARY_KERNEL.md for the exact union-size bounds and the residual incidence ledgers. The proved support lower bounds are:
- E407 Q32: the seven-witness-per-color family has union size at least 29; if there are at least eight exact-129 colors, at least 31.
- E408 Q33: union size at least 31; if there are at least nine exact-129 colors, at least 32.

These are necessary conditions, not terminal contradictions. The only edge-count profiles not removed by the support bound remain E407 129^7,130^4 and E408 Q33 129^8,130^3.

## 6. Scope and audit discipline

- The theorem is valid for all eligible E407 templates A–E and E408 Q33/d3 because it uses only h>=5, B being a target clique, alpha(H)<=4, and the exact-129 factor contract.
- It does not assume that all selected Q sets are disjoint across colors; only the proved intersection-at-most-one rule is used.
- The claim in the sibling crosscut file that templates C/D/E automatically have eight S-avoiding K5 components requires an additional argument: an edge of M[S] does not force its endpoints to occupy the same K5 component of every fixed color. The safe universal count remains seven unless a stronger color-specific forcing lemma is supplied.
- EG617(r=12) remains OPEN / NOT_CERTIFIED.
