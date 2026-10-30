# V47 source-triangle alignment, special-gadget localization, and matching skeleton

Date: 2026-10-30

**Scope:** one exact-129 Type-I color C in the full-support Q32 terminal, conditional on e_C(H) in {69,70}. No m=8/9 closure is claimed.

## 1. Near-Turan interface

Let D=C[H]. The source contract and the 69/70 near-Turan theorem give a partition
P_1,...,P_12 of H with eleven parts of size four and one part of size three. Every within-part pair is C-colored, and the total number of C-edges crossing the parts is
e_C(H)-69, hence zero or one.

Consequently every C-triangle is contained in one part: a triangle meeting at least two parts has at least two cross-part edges. Every C-K4 is also contained in one part (indeed it would need at least three cross-part edges if it crossed a 4+ partition).

The exact source profiles are:
- x in O: (2,1^11), giving eleven single-outside K4s and one double-outside K3;
- x in H, two-double: (2,2,1^10), giving ten single-outside K4s and two double-outside K3s, with x the uncovered H vertex;
- x in H, triple: (3,1^11), giving eleven single-outside K4s and one triple-outside K2, with x the uncovered H vertex.

The single-outside K4s fill distinct size-four parts.

## 2. Full source-triangle alignment

Every double-outside factor leaves a C-colored K3 in H. Since every C-triangle lies in one near-Turan part, its three H vertices must all receive the same part label.

### 2.1 x in O

There is exactly one double-outside factor. Its H-interior K3 occupies the size-three part, since the eleven single-outside K4s fill all eleven size-four parts.

The only possible H-H gadget edges are y--A0. Therefore
e_C(H)=69+1_{y in H}|A0 intersect H|.
In the 69/70 layer this extra term is 0 or 1.

### 2.2 x in H, two-double

The two source K3s are disjoint. They must occupy the remaining size-four and size-three parts separately; they cannot occupy the same part because six vertices do not fit in a part of size at most four. Hence x lies with one of the K3s in the size-four part.

The x-C neighborhood outside H's target edges is source-restricted to Ns\A0 and Nt\{y}. The K3 sharing a part with x must therefore be one of the two special factors Ns,Nt; it cannot be an isolated factor.

It cannot be Ns: if x shared the Ns K3, then Nt is the other double factor or a single-outside factor. In the former case Nt has three H vertices, at least two of which lie in Nt\{y}; in the latter it has four H vertices, at least three of which lie in Nt\{y}. Those would give at least two x--Nt cross-part C-edges, contradicting the one-edge cross-part cap.

Thus the x-part K3 is the Nt interior. This forces:
- Nt has outside occupancy two;
- y is outside H, so all three Nt H vertices are C-adjacent to x;
- all H vertices of Nt lie in the same part as x.

The remaining x--Ns gadget edges are all cross-part, so
|(Ns\A0) intersect H| <= 1.
The y--A0 edges have no H endpoint because y is outside. The K5 interiors contribute 66 edges and x--Nt contributes three internal H edges, hence
e_C(H)=66+3+|(Ns\A0) intersect H|
       =69+|(Ns\A0) intersect H|.
The last term is 0 or 1.

### 2.3 x in H, triple

The eleven single-outside K4s fill all eleven size-four parts. The remaining size-three part consists of x and the two H vertices of the unique triple-outside factor. Both x--K2 edges must be C-colored.

The triple factor must be one of Ns,Nt because x has no source C-edges to an isolated factor. It cannot be Ns: then Nt is single-outside and its four H vertices yield at least three cross-part x--Nt edges (even after omitting y), a contradiction.

Therefore:
- Nt has outside occupancy three;
- y is outside H;
- the two H vertices of Nt lie in the same part as x.

Ns is single-outside, and all x--Ns edges are cross-part, so
|(Ns\A0) intersect H| <= 1.
The K5 interiors contribute 67 edges and x--Nt contributes two internal H edges. Thus
e_C(H)=67+2+|(Ns\A0) intersect H|
       =69+|(Ns\A0) intersect H|,
again with the last term 0 or 1.

## 3. Unified special-gadget localization theorem

For an exact color with x in H and e_C(H) in {69,70}, the source-correct profile is necessarily two-double or triple, and:
- **PROVED_CONDITIONAL:** Nt carries the overfull source factor: |Nt intersect O|=2 in the two-double case, and 3 in the triple case;
- **PROVED_CONDITIONAL:** y is outside H;
- **PROVED_CONDITIONAL:** x and the entire H-interior of Nt occupy one near-Turan part;
- **PROVED_CONDITIONAL:** |(Ns\A0) intersect H|<=1;
- **PROVED_CONDITIONAL:** e_C(H)=69+|(Ns\A0) intersect H|.

For x in O, the unique double-outside factor's H-triangle occupies the size-three part and
e_C(H)=69+1_{y in H}|A0 intersect H|.

These are conditional structural reductions, not contradictions. They do not force any exact color into the 69/70 layer.

## 4. 253-edge target matching skeleton

Fix any non-target color C in the 69/70 layer and its partition P_1,...,P_12. Each part is an independent set in target graph H because all its pairs have color C.

For any two size-four parts A,B, the bipartite target graph H[A,B] has a perfect matching. Indeed, if Hall failed for S subset A, then |N_B(S)|<|S| and
S union (B\N_B(S))
would be an independent set in H of size at least five, contradicting alpha(H)<=4.

For a size-four part A and the size-three part B, the same argument applied to S subset B gives a matching saturating B.

Choose such a matching independently for every pair of parts. Their edge sets are disjoint because each edge joins a unique pair of parts. The resulting spanning subgraph M of H has
e(M)=4*C(11,2)+3*11=220+33=253.

Its degrees are:
- 36 vertices have degree 11 (three in each size-four part, plus all three vertices in the size-three part);
- 11 vertices have degree 10 (the unmatched vertex in each size-four part).

Let s_v=d_H(v)-12, so s_v>=0 and sum_v s_v=6. For F=H\M:
- e(F)=285-253=32;
- d_F(v)=1+s_v on the 36 degree-11 vertices of M;
- d_F(v)=2+s_v on the 11 degree-10 vertices of M;
- at least 30 vertices have degree exactly one in F, since at most six vertices can have s_v>0.

**Status: PROVED_CONDITIONAL** on alpha(H)<=4 and the 69/70 near-Turan partition. The matching choices are existential and may be made independently for each pair of parts.

## 5. Research significance and limitation

The new source-localization theorem removes all low-layer x-in-H placements except those with the overfull factor in Nt and y outside. It converts the residual gadget budget into the exact identity
e_C(H)=69+|(Ns\A0) intersect H|.

The matching-skeleton theorem turns any low-layer partition into a 253-edge subgraph of H with a 32-edge residual whose degree sequence is almost all 1s and 2s. It is a useful structural target for further compatibility attacks, but it is not itself a contradiction: neither the existence of such an F nor compatibility with omega(H)<=5 has yet been ruled out.

The isolated solver and independent verifier now encode/replay the source-localization constraints. The 253-edge matching skeleton is proved here but is not yet represented by explicit matching-choice variables in the CSP.
