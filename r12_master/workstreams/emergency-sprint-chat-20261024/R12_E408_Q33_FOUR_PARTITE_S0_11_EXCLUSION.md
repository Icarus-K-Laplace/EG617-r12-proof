# E408 Q33 four-partite boundary: exclude S0=11

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the E408 Q33 minimum-support / four-partite contract. Combined with the repaired S0=10 proof in `R12_CROSS_BRANCH_AUDIT_AND_S0_REPAIR.md`, this gives (S_0=\epsilon_U+2\delta\ge12) on the four-partite branch. It does not close the non-four-partite branch or the full E408 Q33 terminal.

## 1. Frozen contract

Let H be a 47-vertex graph with
```
alpha(H) <= 4, minimum degree >= 12, e(H)=284,
sum_x epsilon_x = 4, epsilon_x=d_H(x)-12 >=0.
```
Let U be the 31-point support of 56 pairwise-linear independent 4-sets Q, W=V(H)\U (|W|=16), and L=bar(H[U]). Assume L is four-partite with parts A,B,C of size 8 and D of size 7. Every D-large-part pair occurs in exactly one Q block. For each pair of large parts, the eight pairs not used by Q blocks form a perfect matching.

Put
```
delta = e(L)-336,
epsilon_U = sum_{u in U} epsilon_u,
S0 = epsilon_U + 2 delta.
```
The exact edge ledger gives
```
delta + epsilon_U <= 17,
e_H(U,W) = 114 + S0.
```

Every w in W must hit every independent 4-set of H, since otherwise that set together with w is an independent 5-set. In particular, (T_w=N_H(w)\cap U) hits every selected Q.

## 2. Two structural capacity facts

**(A) Seven-neighborhoods.** If (|T_w|=7), then (T_w=D): each selected point belongs to at most eight Q blocks, and the 56 blocks can be hit by seven points only if each contributes all eight incidences, which is true exactly for the seven D points. Let k be the number of such W vertices. At least three points of D have zero excess, and each has exactly six neighbors in W, so (k\le6). Every other W vertex has (|T_w|\ge8).

**(B) Size-8/9 hitting sets.** If T hits all Q and (|T|\in\{8,9\}), then either T contains all of D, or T contains an entire large part A, B, or C.

Proof: if T omits (d\in D), the eight Q blocks containing d require eight distinct large-part vertices, so T contains at least eight large-part vertices and at most one D point. If no large part is full, then for any omitted (a\in A), the seven blocks containing a require six distinct selected B/C vertices when T has one D point, or seven when it has none. In either case each large-part intersection has size at most two, impossible with at least eight large-part vertices.

For any large part G, the number of W vertices whose U-neighborhood contains all of G is at most three whenever (S_0=11). Indeed (epsilon_U=11-2\delta) and (\delta\in\{4,5\}). In G, at least
```
8 - delta - epsilon_U = delta - 3 >= 1
```
vertices have zero excess and no incident extra L-edge. Such a vertex has nine neighbors inside U and therefore exactly three neighbors in W. Every W vertex whose U-neighborhood contains G is adjacent to it, proving the capacity bound.

Also, at most (6-k) W vertices beyond the k seven-neighborhoods can contain all of D, by fixing any zero-excess (d\in D): its six W-neighbors already include those k vertices.

## 3. Exclude S0=11

Suppose (S_0=11). Then
[
\epsilon_U=11-2\delta,\qquad \delta\in\{4,5\},\qquad
x:=e_H(U,W)=125.
]
Since all W vertices outside the k seven-neighborhoods have U-degree at least eight,
[
125\ge7k+8(16-k)=128-k,
]
so (k\ge3), while (k\le6).

The remaining (16-k) U-degrees sum to (125-7k). Exhaustive integer patterns are:

| k | Number remaining | Sum of remaining degrees | Nondecreasing degree patterns |
|---:|---:|---:|---|
| 3 | 13 | 104 | (8^{13}) |
| 4 | 12 | 97 | (8^{11},9) |
| 5 | 11 | 90 | (8^{10},10) or (8^9,9^2) |
| 6 | 10 | 83 | (8^7,9^3), (8^8,9,10), or (8^9,11) |

Here (8^m) means m entries equal to eight.

### Case k=3 or k=4

All remaining neighborhoods have size 8 or 9. By fact (B), each either contains D or a full large part. At most (6-k) can contain D, so at least
[
(16-k)-(6-k)=10
]
must contain a full large part. But each of the three large parts can be contained in at most three such neighborhoods, giving capacity nine. Contradiction.

### Case k=5

The profile (8^9,9^2) is ruled out by the same capacity count: eleven size-8/9 neighborhoods require at least ten full-large-part neighborhoods.

Thus the only possible profile is (8^{10},10). Among the ten size-eight neighborhoods, exactly one must contain D; the other nine are full large parts, three per part. The exceptional size-ten neighborhood (T_*=N_H(w_*)\cap U) can contain neither all of D nor a full large part: D-capacity is already saturated, and the three-per-part capacity is already saturated.

The unique D-containing size-eight neighborhood is (D\cup\{z\}) for one large-part point z. Since (T_*) has size ten, omits some D point, and has no full large part, the standard block-hit count gives
[
|T_*\cap A|,|T_*\cap B|,|T_*\cap C|\le3.
]
Consequently each large part has at least five points outside (T_*), and at least four after also deleting z.

### Case k=6

The profile (8^7,9^3) is ruled out by the same capacity count: all ten neighborhoods would have to contain a full large part.

For profile (8^8,9,10), the nine size-8/9 neighborhoods are full-large-part neighborhoods, exactly three per part. The size-nine one contains a full large part plus one extra point z (possibly in D). The size-ten exceptional neighborhood (T_*) contains neither all of D nor a full large part. Its large-part intersections are at most three, so each complement has size at least five and at least four after deleting z if z is in a large part.

For profile (8^9,11), the nine size-eight neighborhoods are full large parts, three per part. The size-eleven exceptional neighborhood (T_*) contains neither all of D nor a full large part. If (s=|T_*\cap D|), then (s\le3); for each omitted point in a large part, the seven Q blocks containing it require (7-s) distinct hits from the other large parts. Since T* has (11-s) large points, each large-part intersection is at most four. Thus every large part has at least four points outside T*.

It remains to exclude the exceptional neighborhoods in the surviving patterns (k=5) and (k=6).

## 4. Triangle obstruction for the exceptional neighborhood

We use one common argument. Let (T_*=N_H(w_*)\cap U) be an exceptional hitting set of size q in ({10,11}), containing neither all of D nor a full large part. Let Z be the set of large-part spillover points from the one other size-8/9 neighborhood that is not exactly a full part; (|Z|\le1). In the k=5 profile, Z is the extra point in (D\cup\{z\}); in the k=6 profile (8^8,9,10), Z is the extra point in the size-nine neighborhood; for (8^9,11), Z is empty.

Define
[
A_0=A\setminus(T_*\cup Z),\quad
B_0=B\setminus(T_*\cup Z),\quad
C_0=C\setminus(T_*\cup Z).
]
The counts above give (|A_0|,|B_0|,|C_0|\ge4).

For any large-part vertex x outside (T_*\cup Z), its W-neighborhood consists of exactly the three W vertices whose U-neighborhood contains its own large part. The k seven-neighborhoods D do not contain x; the exceptional T* and spillover Z do not contain x; and no other W neighborhood includes x. Hence (d_H(x,W)=3).

Let (j_x) be the number of extra L-edges incident to x among its two unused large-part pairs. Since x has seven H-neighbors in its own 8-point part and (2-j_x) H-neighbors in the other two large parts,
[
d_H(x,U)=9-j_x.
]
The degree equation (d_H(x)=12+\epsilon_x) now gives
[
12+\epsilon_x=(9-j_x)+3,
\qquad\boxed{\epsilon_x=j_x=0}.
]
Thus no extra L-edge touches (A_0\cup B_0\cup C_0).

For every (a\in A_0), at most one pair from a to B is an unused matching pair, so a has at least (|B_0|-1\ge3) L-neighbors in B0. Choose one, b. Similarly a and b each have at least (|C_0|-1\ge3) L-neighbors in C0. Their common L-neighborhood in C0 has size at least (|C_0|-2\ge2), so choose c. Then abc is a triangle in (L[A_0\cup B_0\cup C_0]).

Since T* does not contain all of D, choose (d\in D\setminus T_*). Every pair between d and A∪B∪C is an L-edge because each D-large pair occurs in a Q block. Thus ({a,b,c,d}) is an independent 4-set in H. It is disjoint from (T_*=N_H(w_*)\cap U), so w* is anticomplete to it, giving an independent 5-set in H. Contradiction.

This excludes the only remaining profiles for k=5 and k=6. Hence (S_0=11) is impossible.

## 5. Conclusion and scope

Under the E408 Q33 minimum-support contract and the four-partite assumption on L,
[
oxed{S_0=\epsilon_U+2\delta\ge12.}
]
The proof is a necessary-structure theorem. It does not establish that the core is four-partite, and it does not close the non-four-partite E408 Q33 branch, E408 Q32's 285-edge core, E407 Q32, or the original (K_{145}) theorem. The global status remains **OPEN / NOT_CERTIFIED**.
