# E408 Q33 at S0=14: eliminate every seven-point transversal

Date: 2026-10-26  
Status: **PROVED_CONDITIONAL** under the registered 47-core / 284-edge / alpha<=4 / omega<=11 contract, the 31-point / 56-witness exact-129 factor, and the retained linearity conditions.

## Theorem

Assume the minimum-support E408 Q33 boundary and \(S_0=\epsilon_U+2\delta=14\). Then:

1. no \(w\in W\) has \(q_w=|N_H(w)\cap U|=7\);
2. there is no seven-point transversal \(T\subset U\) of the 56 witness blocks, even one not realized as a W-neighborhood;
3. consequently every \(w\in W\) has \(q_w=8\).

Thus the only remaining \(S_0=14\) terminal is the all-eight-neighborhood configuration with no seven-point transversal.

## Proof

The exact cross-edge count gives
\[
\sum_{w\in W}q_w=e_H(U,W)=114+S_0=128.
\]
Every \(w\) hits every witness block, so \(q_w\ge7\). Let \(k\) be the number with \(q_w=7\). The retained transversal lemma says that if \(k\ge1\), each such vertex has U-neighborhood equal to a seven-point transversal \(T\). The prior transversal uniqueness result makes \(T\) unique; \(T\) is a clique anticomplete to \(R=U\setminus T\), and each \(t\in T\) induces a partition of \(R\) into eight independent witness triples. Also \(k\le4\), since \(T\) together with the \(k\) degree-seven W-vertices is a clique.

Let \(a\) count the degree-eight vertices with U-neighborhood \(T\cup\{r\}\) for some \(r\in R\) (T-type vertices). Let \(h\) count the high vertices \(y\in W\) with \(q_y>8\) and \(N_H(y)\cap T=T\), i.e. \(b_y=7\).

### Step 1 — the T-type group is a clique

The \(k\) degree-seven vertices form a clique: two nonadjacent such vertices, together with any independent witness triple in \(R\), would be an independent five-set.

Every T-type vertex is adjacent to every degree-seven vertex. If \(x\) is T-type with sole R-neighbor \(r\), and \(v\) has U-neighborhood \(T\), then a witness triple in a fixed T-partition avoiding \(r\) exists. If \(xv\) were a nonedge, that triple plus \(x,v\) would be independent of size five.

Two T-type vertices with sole R-neighbors \(r,s\) are adjacent for the same reason: among the eight triples in any fixed T-partition, at most two contain \(r\) or \(s\), so a triple avoiding both exists. All these vertices are complete to \(T\). Therefore \(T\), the degree-seven group, and the T-type group form a clique, giving
\[
k+a\le4. \tag{1}
\]
Put \(s=k+a\).

### Step 2 — at least \(6-s\) high vertices must be T-complete

Write each high degree as \(q_y=8+d_y\), where \(d_y\ge1\). Since the total U-degree is 128,
\[
128=7k+8(16-k)+\sum_{q_y>8}d_y,
\]
so
\[
\sum_{q_y>8}d_y=k. \tag{2}
\]

If \(b_y=|N_H(y)\cap T|<7\), then y misses some \(t\in T\), and its R-neighborhood must hit all eight triples in the partition indexed by t. Hence \(q_y-b_y\ge8\), or \(b_y\le d_y\). It follows that
\[
B:=\sum_{q_y>8}b_y=7h+B_{\rm low},\qquad 0\le B_{\rm low}\le k. \tag{3}
\]

Summing degrees from \(T\) into \(W\) gives
\[
42+\epsilon_T=7k+7a+B,
\quad\text{so}\quad
\epsilon_T=7(s-6)+B.
\]
Since \(\epsilon_T\ge0\),
\[
B\ge7(6-s). \tag{4}
\]
Combining (3) and (4), \(7h+k\ge7(6-s)\). Because \(k\le4<7\), this forces
\[
h\ge6-s. \tag{5}
\]

### Step 3 — the T-complete high vertices join the same clique

For a high vertex y with \(b_y=7\), write \(q_y=8+d_y\). Its R-neighborhood has size \(d_y+1\). By (2), any two such vertices y,z satisfy
\[
|N_H(y)\cap R|+|N_H(z)\cap R|
=d_y+d_z+2\le k+2\le6.
\]
In any fixed T-partition, eight triples partition R, and at most six of those triples meet the union of the two R-neighborhoods. A remaining independent witness triple avoids both y and z. Therefore y,z must be adjacent, or they and that triple form an independent five-set.

The same argument shows each such y is adjacent to every degree-seven vertex (its R-neighborhood has at most five points) and every T-type vertex (the union of its R-neighborhood and the T-type vertex's single R-neighbor has size at most \(d_y+2\le k+2\le6\)). Hence
\[
T\ \cup\ W_7\ \cup\ W_{8,T}\ \cup\ W_{>8,b=7}
\]
is a clique of size \(7+k+a+h=7+s+h\). By (5), this size is at least 13, contradicting \(\omega(H)\le11\).

Thus \(k=0\): no W-vertex has \(q_w=7\).

### Step 4 — no seven-point transversal exists at all

Suppose a seven-point transversal \(T\subset U\) exists despite \(k=0\). The same transversal structure gives \(R=U\setminus T\), \(|R|=24\), and eight triple partitions of R.

All W-vertices have \(q_w=8\), because \(q_w\ge8\) and their sum is 128. Each such neighborhood is either T-type \(T\cup\{r\}\), or an R-only eight-transversal: if it misses any t in T, it must hit all eight triples of that t-partition, using all eight U-neighbors in R.

Let a be the number of T-type vertices and \(m=16-a\) the number of R-only neighborhoods. As in the S0=13 boundary ledger, for each \(r\in R\),
\[
d_H(r,W)=3+\epsilon_r+j_r,\qquad
\sum_{r\in R}(\epsilon_r+j_r)=S_0-\epsilon_T=14-\epsilon_T.
\]
For any distinct R-only set S occurring \(m_S\) times,
\[
8m_S\le\sum_{r\in S}d_H(r,W)
\le24+14-\epsilon_T\le38,
\]
so \(m_S\le4\). Distinct R-only transversals are disjoint, hence there are at most three of them and \(m\le12\). Therefore \(a=16-m\ge4\).

But T and the a T-type vertices form a clique (Step 1), so \(7+a\le11\), hence \(a\le4\). Consequently \(a=4\) and \(m=12\). The 12 R-only neighborhoods must consist of exactly three distinct transversals, each with multiplicity four; they partition R. The clique consequence of the three-part transversal lemma then gives a \(K_{12}\), contradiction.

No seven-point transversal exists. Since every W-vertex has \(q_w\ge7\), k=0 and \(\sum_Wq_w=128\) imply all 16 vertices have \(q_w=8\). This proves the theorem. \(\square\)

## Exact structure of the remaining all-q=8 terminal

For each color \(c\in\{1,\ldots,8\}\), let
\[
X_c=U\setminus\bigcup_{Q\in\mathcal Q_c}Q,\qquad |X_c|=3,
\]
the three U-vertices omitted by that color's seven disjoint witness blocks. Every remaining W-vertex \(w\) has \(q_w=8\) and hits all seven blocks of every color. Therefore
\[
|N_H(w)\cap X_c|\le1\quad\text{for every }w,c.
\]
If the intersection has size one, w hits each of the seven blocks exactly once. If it has size zero, all eight U-neighbors lie in the block union, so exactly one block is hit twice and the other six are hit once.

Let \(c_u\) be the number of colors whose selected witness blocks contain \(u\), and set \(\rho_u=8-c_u\). Then
\[
\sum_{u\in U}c_u=56\cdot4=224,\qquad
\sum_{u\in U}\rho_u=8\cdot31-224=24.
\]
The number \(\rho_u\) is exactly the number of omission triples \(X_c\) containing u. For each w define
\[
\tau_w=\bigl|\{c:N_H(w)\cap X_c\ne\varnothing\}\bigr|.
\]
Because each \(N_H(w)\) meets each \(X_c\) in at most one point,
\[
\boxed{\tau_w=\sum_{u\in N_H(w)\cap U}\rho_u.} \tag{6}
\]
In particular, if \(u,v\in X_c\) for any color c, then \(N_H(u)\cap W\) and \(N_H(v)\cap W\) are disjoint.

Let \(J\) be the graph of the \(\delta\) leftover edges of \(L\) not covered by the 56 witness \(K_4\)'s, and \(j_u=d_J(u)\). Since each witness block containing u contributes three distinct incident edges of L,
\[
d_L(u)=3c_u+j_u,\qquad
d_H(u,W)=12+\epsilon_u-d_H(u,U)
=6-3\rho_u+j_u+\epsilon_u. \tag{7}
\]
Here \(\sum_u j_u=2\delta\), \(\epsilon_U\in\{0,2,4\}\), and \(\delta\in\{7,6,5\}\), respectively.

Equations (6)–(7), together with the pairwise-disjoint W-neighborhood condition for each omission triple \(X_c\), are the reduced finite target. They do not yet imply a contradiction; no unproved claim about the existence or nonexistence of this all-q=8 system is made.

### Independent-four-set rigidity in W

For the all-\(q=8\) terminal, each \(w\in W\) has \(d_H(w,W)=4+\epsilon_w\). Since \(\epsilon_W=4-\epsilon_U\),
\[
e(H[W])=\frac{64+\epsilon_W}{2}=34-\frac{\epsilon_U}{2}\in\{32,33,34\}.
\]
Caro–Wei gives
\[
\alpha(H[W])\ge \frac{16^2}{2e(H[W])+16}
\ge \frac{256}{84}>3.
\]
Thus \(\alpha(H[W])=4\), and an independent four-set \(A\subset W\) exists.

For every such \(A\), each \(u\in U\) must have a neighbor in \(A\); otherwise \(A\cup\{u\}\) would be an independent five-set. Hence
\[
\bigcup_{w\in A}(N_H(w)\cap U)=U.
\]
The four U-neighborhoods each have size eight, so their total incidence count is 32 while their union has size 31. Therefore exactly one U-vertex belongs to exactly two of these four neighborhoods, and every other U-vertex belongs to exactly one. Equivalently, among the six pairs of vertices in any independent four-set \(A\subset W\), exactly one pair has a common U-neighbor, that intersection is a singleton, and the other five pairs have disjoint U-neighborhoods.

This rigidity is an additional necessary condition for the remaining terminal; it is not yet a contradiction.


More generally, for any independent set \(A\subset W\) of size \(r\le4\), every witness block \(Q\in\mathcal Q\) satisfies
\[
\left|Q\cap\bigcup_{w\in A}N_H(w)\right|\ge r.
\]
Otherwise at least \(5-r\) vertices of the independent block Q would be nonadjacent to every vertex of A, giving an independent five-set. Thus independent pairs, triples, and quadruples of W induce respectively 2-, 3-, and 4-fold covers of every witness block.


## Scope and next terminal

The theorem does not yet rule out \(S_0=14\). It reduces that equality case to:
- all 16 W-neighborhoods have U-degree exactly eight;
- the 56 witness blocks have no seven-point transversal in U;
- the 8 omission triples \(X_c\) each have size three, every W-neighborhood meets each in at most one point, and equations (6)–(7) hold.

The next proof target is this no-transversal all-\(q=8\) system. E408 Q33 at larger \(S_0\), larger witness supports, E407 Q32, E408 Q32, and the original \(K_{145}\)-to-T61 bridge remain OPEN / NOT_CERTIFIED.
