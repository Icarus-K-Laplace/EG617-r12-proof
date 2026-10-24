# Cross-branch audit and repaired E408 Q33 four-partite S0=10 exclusion

Date: 2026-10-25  
Scope: independent read of the latest emergency-sprint, ultimate-closure, witness-packing, and zero-excess branches.  
Status: **PROVED_CONDITIONAL repaired four-partite boundary lemma; global EG617(r=12) remains OPEN / NOT_CERTIFIED.**

## 1. Live sibling refresh

Read-only sibling heads checked before this note:

- emergency sprint: `ad56a91c644458cb16dd590b7a4ed0e800978a81`;
- ultimate closure: `1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40`;
- witness packing: `5d0e3ceab7895be1a947e46853f92bb84477f4e5`;
- zero-excess witness: `98167ec779850a2ff57b1ec7113f939df42c35f4`;
- general-r architecture: `a922c4d7646eb8d0087bde8547562c8aace02ee2`;
- general-r asymptotic: `fa6a5f2b8b5d2a0fe821d50a4421884a69dc5366`.

Only this emergency-sprint directory is edited by the current workstream. No sibling files are modified.

## 2. Audit correction: beta-sensitive witness counts

The earlier version of `R12_WITNESS_UNION_CAPACITY_REFINEMENT.md` inferred eight S-avoiding K5 components per exact-129 color in E407 templates C/D/E, and in E408 Q33 when beta>0. This inference is not justified by the present contract: an edge in M[S] permits its endpoints to share a non-target K5, but does not force them to be in the same component. The safe universal count is seven S-avoiding components per exact-129 color, with at least six B-labelled after allowing one pivot-containing component.

The capacity theorem and witness-hitting inequality themselves remain valid. Their terminal applications have been corrected in the same branch. Safe consequences:
- E407, any template: seven exact-129 colors give N>=49 and |U|>=29; at least eight exact-129 colors give N>=56 and |U|>=31.
- E408 Q33: eight exact-129 colors give N>=56 and |U|>=31 for any beta.
- No 64-witness or |U|>=33 conclusion is imported from beta>0 alone.
- E408 Q32 remains separate: its core has 285 edges and excess six.

## 3. Repaired theorem for the E408 Q33 four-partite S0=10 boundary

### Frozen contract

Let H be a 47-vertex graph with alpha(H)<=4, minimum degree 12, and e(H)=284, so total degree excess is four. Let U have 31 vertices and be the union of 56 pairwise-linear independent 4-sets Q. Let W=V(H)\U have 16 vertices. Assume L=complement(H[U]) is four-partite with parts A,B,C of size 8 and D of size 7.

The 56 Q-blocks force every pair between D and A∪B∪C to occur exactly once. Between each pair of large parts A,B,C, the eight pairs not used by Q-blocks form a perfect matching. Let delta count the extra L-edges among those 24 unused large-part pairs, and let epsilon_U be the degree excess in U. The core budget gives
```
delta + epsilon_U <= 17,
e_H(U,W) = 114 + epsilon_U + 2 delta.
```

Every w in W must hit every independent 4-set of H, not merely the selected Q-blocks: otherwise w together with that independent 4-set would be an independent 5-set. In particular, T=N_H(w)∩U hits all 56 Qs.

### Lemma 3.1 — the size-10 exceptional hitting set is impossible

Suppose S0=epsilon_U+2delta=10. Then epsilon_U=10−2delta, hence delta∈{3,4,5}. Let k be the number of W vertices with |N_H(w)∩U|=7. Each such neighborhood is exactly D. Three zero-excess vertices in D each have six W-neighbors, so k<=6. Since every other W vertex must hit all Qs and therefore has U-degree at least eight,
```
124 = e_H(U,W) >= 7k + 8(16-k) = 128-k,
```
so k∈{4,5,6}.

For every large part G, at least 8−delta−epsilon_U=delta−2>=1 vertices of G have zero excess and no incident extra L-edge. Such a vertex has nine H-neighbors inside U, hence exactly three W-neighbors. Therefore at most three W vertices can have U-neighborhood containing G.

A hitting set T of size 8 or 9 either contains all of D or contains a whole large part. To see this, if it omits d∈D, its eight Q-blocks containing d require eight distinct large-part hits; with at most one D point in T, a set of size 8/9 cannot meet those blocks otherwise. If no large part is fully contained, the seven blocks containing any omitted point a in a large part require at least six (or, when T∩D is empty, seven) distinct selected points from the other two large parts. This bounds every large-part intersection by two, contradicting the need for at least eight large-part points.

At most 6−k additional W vertices can have a neighborhood containing all of D, because each zero-excess d∈D already has exactly six W-neighbors, k of which are the size-seven neighborhoods. Thus at least ten of the 16−k remaining vertices must have a full large-part neighborhood. There are at most three per large part, hence at most nine. This rules out k=4,5. If k=6, the remaining ten U-degrees sum to 82, so their multiset is either (8^8,9^2) or (8^9,10). The first again requires ten full-large-part neighborhoods and is impossible. Therefore the only residual pattern is six neighborhoods D, nine full-large-part neighborhoods (three for each A,B,C), and one exceptional w* with
```
T*=N_H(w*)∩U, |T*|=10,
```
where T* contains neither all of D nor a full large part.

Let s=|T*∩D| and t_A=|T*∩A|, t_B=|T*∩B|, t_C=|T*∩C|. Since T* is a hitting set, the following cases are impossible.

#### Case s=0

For every omitted a∈A, the seven Q-blocks containing a must be hit by seven distinct selected vertices in B∪C. Hence t_B+t_C>=7 and t_A<=3; cyclically all t_i<=3. But t_A+t_B+t_C=10, contradiction.

#### Case s=1 — repaired pair count

The nine large-part points must satisfy t_A=t_B=t_C=3: the selected D point can hit only one of the seven blocks containing a fixed large-part point, so the remaining six blocks require six distinct selected points from the other two large parts.

For each of the six unselected d∈D, the eight Q-blocks containing d receive nine incidences from the nine selected large-part points. Each selected point occurs in exactly one block with d, and all eight blocks must be hit. Thus exactly one block is hit twice, giving one selected cross-part pair in a Q-block labelled by this unselected d. These six pairs are distinct by linearity.

For the one selected d∈D, its Q-blocks form a matching between each pair of large parts; it contributes at most three selected pairs from each 3×3 subset, hence at most nine selected cross-part Q-pairs. Any selected cross-part pair not occurring in a Q-block must be one of the unused matching pairs for its pair of large parts; each such matching intersects a 3×3 selected subset in at most three pairs, so there are at most nine selected non-Q pairs in total. Therefore the 27 selected cross-part pairs would have to satisfy
```
27 <= 6 + 9 + 9 = 24,
```
a contradiction. This repair does not incorrectly assume that every non-Q pair is an extra L-edge; such a pair may instead be an H-edge.

#### Case s=2 — repaired triangle obstruction

Now t_A+t_B+t_C=8. For an omitted a∈A, the two selected D points hit two distinct blocks among the seven Q-blocks containing a; the remaining five blocks require five distinct selected points from B∪C. Hence t_A<=3, and cyclically every t_i<=3. Therefore (t_A,t_B,t_C)=(3,3,2) up to permutation. Rename the parts so |A'|=|B'|=3, |C'|=2, where A'=T*∩A, etc.; write A0=A\A', B0=B\B', C0=C\C'.

For each unselected d∈D\T*, the eight Q-blocks containing d receive exactly eight incidences from the eight selected large-part points. Since all blocks must be hit, each block contains exactly one selected large-part point. Thus no selected pair across two large parts can occur in a Q-block labelled by an unselected d.

For selected subsets of sizes a,b in two large parts, at most 2 min(a,b) pairs can occur in Q-blocks labelled by the two selected D points. Therefore at least ab−2 min(a,b) selected pairs are not Q-pairs. The three pair types (A',B'), (A',C'), (B',C') force respectively at least 3,2,2 non-Q pairs. Each pair of large parts has exactly one unused perfect matching, whose intersection with these selected subsets has size at most 3,2,2 respectively. Hence equality holds throughout: all three A'×B' matching pairs are selected, and both C' points are matched to selected A' points and to selected B' points.

The degree identity now supplies the key fact omitted from the sibling proof. For x in a large part, exactly three vertices of W have U-neighborhood equal to that large part, and w* is adjacent to x iff x∈T*. If j_x is the number of extra L-edges incident to x among its two unused large-part pairs, then
```
d_H(x,W)=3+1[x∈T*],
d_H(x,U)=9-j_x,
d_H(x)=12+epsilon_x,
so epsilon_x+j_x=1[x∈T*].
```
Consequently every large-part vertex outside T* has epsilon_x=j_x=0: no extra L-edge touches A0∪B0∪C0.

The unused AB matching has all three A' vertices matched to B', so its remaining five pairs match A0 to B0. Therefore each a∈A0 has exactly four L-neighbors in B0. The unused AC matching has both C' points matched to A' and the remaining five A0 points matched to C0, so every a∈A0 has exactly five L-neighbors in C0. Similarly every b∈B0 has exactly five L-neighbors in C0. Choose any a∈A0 and any L-neighbor b∈B0. Since |N_L(a)∩C0|=|N_L(b)∩C0|=5 and |C0|=6, their common L-neighborhood in C0 has size at least four. Choose c in that intersection. Then abc is a triangle in L[A0∪B0∪C0].

Choose d∈D\T*, which is nonempty because s=2 and |D|=7. Every pair between d and A∪B∪C is an L-edge, since each such pair occurs in a Q-block. Hence {a,b,c,d} is an independent 4-set in H. It is disjoint from T*=N_H(w*)∩U, so w* is anticomplete to it, producing an independent 5-set in H, contradiction.

All s=0,1,2 cases are excluded. Therefore the repaired theorem is
```
epsilon_U + 2 delta >= 11
```
under the stated four-partite E408 Q33 minimum-support contract.

## 4. Exact scope and remaining blockers

This repairs the conclusion of the sibling S0=10 note without using its invalid “non-Q pairs must be extra L-edges” assertions. The repaired proof uses the stronger universal fact that every independent 4-set must be hit by every outside vertex.

It is still conditional on the four-partite minimum-support contract. The non-four-partite E408 Q33 branch remains open. E408 Q32's 285-edge/excess-six core is not covered. E407 Q32's common-core completion remains open. The T61-to-K145 reduction and the original theorem remain OPEN / NOT_CERTIFIED.


## Subsequent strengthening (2026-10-25)

The later file `R12_E408_Q33_FOUR_PARTITE_S0_11_EXCLUSION.md` excludes S0=11 as well as S0=10, giving S0>=12 under the same four-partite minimum-support contract. Separately, `R12_E407_TRANSVERSAL_EXCESS_BOUND.md` strengthens the E407 v=29/49-witness bound to epsilon_U+2delta>=9 and delta>=3 without any four-partite assumption. This audit file records the earlier repaired S0=10 step; use the two later theorem files for the stronger current statements.
