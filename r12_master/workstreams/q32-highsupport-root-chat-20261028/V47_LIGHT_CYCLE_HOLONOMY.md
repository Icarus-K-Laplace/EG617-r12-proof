# E408 Q32 full support — four-light-cycle matching holonomy

Date: 2026-10-28  
Status: **PROVED local theorem with exact finite verification.** No global Q32 closure claimed.

## 1. Setup

Let A,B,C,D be pairwise disjoint independent 4-sets with alpha(G[A union B union C union D])<=4. Assume the four cycle pairs AB, BC, CD, DA each have exactly four edges, hence each is a perfect matching. Assume both diagonal pairs AC and BD have at most seven edges.

Normalize AB, BC, CD to identity matchings. Write the DA matching as D_i A_{sigma(i)} for a permutation sigma in S4. Then the two path compositions between A and C are the identity matching (through B) and the sigma^{-1} matching (through D); likewise the two path compositions between B and D are identity and sigma^{-1}.

By the two-light matching composition theorem, both diagonal graphs AC and BD must contain both of these perfect matchings.

## 2. Theorem

Under the setup above:

> **The cycle holonomy sigma is either the identity or a transposition.**

If sigma is a transposition, each diagonal pair contains the union of two distinct perfect matchings and therefore has at least six edges. Since the edge cap is seven, each diagonal has exactly six or seven edges.

## 3. Proof

Let s be the number of moved points of sigma. The identity matching and the sigma^{-1} matching share the 4-s edges corresponding to fixed points and differ on the s moved points. Their union therefore has exactly 4+s edges.

- If s=4 (a 4-cycle or double transposition), each diagonal must contain at least eight edges, contradicting the seven-edge cap.
- If s=3 (a 3-cycle), each diagonal must contain exactly seven edges and no other edges. Up to relabeling, take sigma=(0 1 2) fixing 3. The resulting 16-vertex graph has the independent 5-set
  `{A_0, A_3, B_2, C_1, D_0}`,
  contradicting alpha<=4. Relabeling gives the same contradiction for each 3-cycle.
- If s=2, sigma is a transposition, which is allowed by the local contract; the two diagonals each contain at least the union of the identity and transposition matchings, i.e. at least six edges.
- If s=0, sigma is the identity.

This proves the theorem.

## 4. Exact finite verification

The companion verifier checks:
- all six transpositions and all 11-by-11 choices of optional diagonal edges (726 graphs total); none has an independent 5-set;
- all eight 3-cycles with the forced seven-edge diagonals; each has an independent 5-set;
- both derangement types are impossible because their diagonal matching unions have eight edges.

The verifier returns `V47_LIGHT_CYCLE_HOLONOMY_EXHAUSTIVE_OK`. It checks only this normalized 16-vertex contract.

## 5. Application to the m=10 disconnected 2+8 / 3+7 cells

Every pair of outer blocks has at most seven edges, and the outer light graph has minimum degree at least four. Thus any four-cycle of light pairs has diagonal edge counts at most seven and falls under this theorem.

Consequently, every light 4-cycle has identity holonomy unless both diagonals are 6- or 7-edge pairs; in the exceptional case, the holonomy must be a transposition and both diagonals consume at least two units each of the weighted heavy-edge ledger. In the 3+7 cell, the per-block heavy-weight cap is two, so any such diagonal pair has weight exactly two and its endpoints have no other internal-heavy incidences.

This is an additional constraint on the matching-holonomy ledger, not a contradiction. It should be combined with the zero-slack residual-neighbor map, outer-block transversal caps, and the 18 residual path/cycle types. EG617(r=12) remains **OPEN / NOT_CERTIFIED**.
