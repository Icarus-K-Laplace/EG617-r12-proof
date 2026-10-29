# E408 Q32 — partial residual-projection packing lemma

Date: 2026-10-29  
Status: **PROVED conditional combinatorial lemma** under the common-factor contract and residual-signature injectivity theorem. This is a necessary constraint for the vertex-labelled CSP, not a Q32 closure.

## Definitions

For an exact color \(C\), let \(R_i(C)\subseteq T_i\) be its two residual vertices on each large track, and define its pair projection
\[
\Pi_{ij}(C)=(R_i(C),R_j(C)).
\]
For the common complementary perfect matching \(P_{ij}\), let
\[
B_{ij}(A,B)=A\times B,\qquad |A|=|B|=2
\]
be the four-edge bipartite block induced by a pair projection.

The common-factor contract says that \(M_{C,ij}\) restricts to one of the two perfect matchings of \(B_{ij}(R_i(C),R_j(C))\), and is edge-disjoint from \(P_{ij}\). Distinct colors' selected matchings are also edge-disjoint.

## Theorem

For any fixed pair \(ij\) and residual pair key \((A,B)\), the multiplicity
\[
m_{ij}(A,B)=|\{C:\Pi_{ij}(C)=(A,B)\}|
\]
is at most two. If it is two, then:

1. \(P_{ij}\) has no edge in the four-edge block \(A\times B\);
2. the two colors use the two complementary perfect matchings of \(K_{2,2}=A\times B\), so together they cover all four block edges;
3. neither color owns a large-pair surplus edge on pair \(ij\);
4. the two colors cannot share a second pair projection.

Consequently, every duplicated pair projection is a **P-free, exactly-two-color block**, and any two distinct colors share at most one of their three pair projections.

## Proof

Fix a pair key \((A,B)\). Each color with this projection must choose a perfect matching of the \(K_{2,2}\) block \(A\times B\). There are exactly two such perfect matchings, call them \(F_0,F_1\).

If \(P_{ij}\) contains any edge of \(A\times B\), that edge belongs to exactly one of \(F_0,F_1\). Since the selected matching \(M_{C,ij}\) must be disjoint from \(P_{ij}\), the matching containing that edge is forbidden, leaving only the other perfect matching available. All colors with this same pair key would then be forced to use that same matching, contradicting cross-color edge-disjointness. Therefore a duplicated key requires
\[
P_{ij}\cap(A\times B)=\varnothing.
\]

When the block is P-free, both \(F_0,F_1\) are available, but distinct colors must choose different ones. There are only two, so the multiplicity is at most two; if it is two, both matchings are used and all four block edges are covered. Since \(S_{ij}\subseteq P_{ij}\), the P-free condition also excludes any \(S_{ij}\) surplus edge in this block, proving item 3.

Finally, if two colors shared two pair projections, then their residual two-sets on all three tracks would coincide: any two of the three pair keys determine all three \(R_i\). This would give identical six-vertex residual signatures, ruled out by V47_Z01_RESIDUAL_SIGNATURE_INJECTIVITY.md. Hence they share at most one projection. \(\square\)

## CSP consequences

- A pair key touched by any \(P_{ij}\) edge (H, exact-repeat, or D-repeat) is globally unique among exact colors.
- A duplicated key must be marked P-free before any color matching is selected; it cannot later receive an H edge or any repeat edge from \(P_{ij}\).
- If a key is duplicated, its two colors consume both internal \(K_{2,2}\) perfect matchings. No third color can use either internal matching.
- Pair-projection multiplicity must be modelled as a block-level constraint, not merely as a penalty for duplicate full six-sets.

The lemma does not prohibit two colors from sharing one P-free pair key, and it does not establish that a global assignment exists or is impossible. The full-support \(v=47\), \(z=0,1\), \((2,2,2,1)\) cells remain **OPEN / NOT_CERTIFIED**.
