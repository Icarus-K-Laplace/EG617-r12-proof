# E408 exact-129 pairwise blocker compatibility

Date: 2026-10-24  
Status: PROVED under the E408 seven-block equality contract and the exact-129 factor theorem.  
Scope: stronger compatibility theorem for the twelve block-to-residual neighborhoods of one exact-129 color. It does not eliminate E408 Q32/Q33.

## 1. Frozen contract

Assume the original balanced coloring of K145 and the E408 equality decomposition into seven target-color K12 blocks B_0,...,B_6 and a 61-point residual R, with target edges joining neither distinct blocks nor a block to R.

Fix a non-target color C with e_C(R)=129. By the retained exact-129 factor theorem, C[R] is the disjoint union of ten isolated K5 components K_1,...,K_10 and an 11-vertex gadget U satisfying alpha(C[U])=2 and omega(C[U])=5.

For each b in B_i, set X_b=N_C(b) intersect R. The global one-or-two rule says that for every x in R, the number of b in B_i with x in X_b is d_C(x,B_i) in {1,2}. Also alpha(C)<=12 globally.

## 2. Individual blocker structure

Lemma 2.1. Every X_b meets every maximum independent 12-set of C[R].

Proof. If a maximum independent 12-set I of C[R] avoided X_b, then I union {b} would be independent of size 13 in C, contradicting alpha(C)<=12. QED.

Lemma 2.2. For every b in B_i, either X_b contains an entire K_j, or alpha(C[U\X_b])<=1. In the second case, U\X_b is a clique in C[U], so |X_b intersect U|>=6.

Proof. If X_b contains no entire K_j, one can choose a vertex outside X_b from each of the ten K5 components. If C[U\X_b] had an independent pair, that pair together with those ten vertices would be an independent 12-set avoiding X_b, contrary to Lemma 2.1. Thus U\X_b has independence number at most one. Since omega(C[U])=5, it has at most five vertices, proving the size bound. QED.

Consequently every blocker has size at least five, and a size-five blocker is exactly one of the K_j components.

## 3. Pairwise blocker compatibility inside a target block

Theorem 3.1. For distinct b,b' in the same target block B_i, put X=X_b and Y=X_b'. Let k(X,Y) be the number of K5 components K_j fully contained in X union Y. Then

alpha(C[U\(X union Y)]) <= k(X,Y).

Proof. Since b,b' lie in a target-color K12, the edge bb' is not color C. If C[R\(X union Y)] contained an independent 11-set I, then I union {b,b'} would be an independent 13-set in C: both b and b' have no C-neighbor in I, and bb' is not a C-edge. This contradicts alpha(C)<=12.

The graph C[R\(X union Y)] has an independence-number contribution of one from each K5 component not fully covered by X union Y, and contribution zero from each fully covered component. The gadget contributes alpha(C[U\(X union Y)]). Hence

alpha(C[R\(X union Y)]) = 10-k(X,Y)+alpha(C[U\(X union Y)]) <= 10,

which is equivalent to the claimed inequality. QED.

Useful boundary cases:
- If k=0, then X union Y must contain all of U.
- If k=1, then U\(X union Y) must be a clique in C[U] and therefore has at most five vertices.
- Two vertices in the same block cannot both have X_b=X_b'=K_j: then k=1 but U is untouched and has independence number 2.
- The one-or-two rule also implies that at most two neighborhoods X_b in a fixed block can contain any given K_j, since each vertex of K_j has C-degree at most two into that block.

These are pairwise constraints on the same labeled neighborhood family; they do not assume neighborhoods from different blocks are distinct.

## 4. Exact equality case e_C(B_i,R)=62

Theorem 4.1. For each block B_i, e_C(B_i,R)=sum_{b in B_i}|X_b| >= 62. If equality holds, the twelve neighborhoods have the following exact form:
- ten of them are the ten distinct K5 components K_1,...,K_10, each used once;
- the other two are six-subsets X,Y of U with X union Y=U and |X intersect Y|=1;
- equivalently, U\X and U\Y are disjoint five-vertex cliques of C[U];
- exactly one vertex of U has C-degree two into B_i, and every other vertex of R has C-degree one into B_i.

Proof. Let m be the number of size-five neighborhoods. Each is a K_j, and no K_j can occur twice in the same block by Theorem 3.1, so m<=10. All remaining neighborhoods have size at least six by Lemma 2.2. Therefore

e_C(B_i,R) >= 5m+6(12-m)=72-m>=62.

If equality holds, m=10 and all other two neighborhoods have size six. The ten size-five neighborhoods are the ten distinct K_j. A remaining size-six neighborhood cannot contain a K_j: pairing it with the exact K_j neighborhood would leave k=1, while its extra vertex can remove at most one vertex of U (or only a partial vertex from another K5), so the residual U still has independence number at least two, violating Theorem 3.1. Thus both size-six neighborhoods lie entirely in U. The pairwise condition with k=0 forces their union to be U, and their intersection has size one because 6+6-11=1. Their complements are disjoint five-cliques in C[U] by Lemma 2.2. The incidence degrees now follow directly: every K5 vertex is covered exactly once, and the U neighborhoods cover U once except at their unique intersection vertex. QED.

In particular, writing e_C(B_i,R)=61+r_i(C), every block has r_i(C)>=1; equality r_i(C)=1 is rigidly characterized by the structure above.

## 5. Global duplicate-budget consequence

The seven-block ledger gives P_C+R_C=62, where R_C=sum_i r_i(C) and sum_C P_C=252. Since each r_i(C)>=1,

sum_i (r_i(C)-1)=R_C-7=55-P_C.

Thus the total block-to-residual slack for C is exactly 55-P_C; each zero-slack block has the equality structure of Theorem 4.1. If P_C=55, all seven blocks are zero-slack. Then each K_j has one exact-K_j representative b_{i,j} in every block. Representatives for a fixed K_j in distinct blocks must be C-adjacent: otherwise an independent 11-set in R\K_j (nine K5 components plus an independent pair in U) together with the two representatives would give an independent 13-set in C. Hence each K_j together with its seven representatives forms a C-clique of size 12, and the ten such cliques are vertex-disjoint.

Since sum_C P_C=252, at most four colors can have P_C=55. E408 has at least eight exact-129 colors, so at least four exact-129 colors have at least one block with strict slack r_i(C)>1.

This is a structural restriction, not yet a contradiction: the strict-slack blocks and the remaining cross-block duplicate assignments still require joint analysis.
