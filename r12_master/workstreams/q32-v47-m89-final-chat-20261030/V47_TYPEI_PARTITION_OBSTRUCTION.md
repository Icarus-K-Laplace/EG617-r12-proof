# E408 Q32 v47 — Type-I source partition obstruction

Date: 2026-10-30

Status: **PROVED** — conditional only on the registered exact-129 Type-I source factorization and the Q32 core contract.

## 1. Core contract

The target graph H satisfies
\[
|V(H)|=47,\quad e(H)=285,\quad \delta(H)\ge12,\quad
\alpha(H)\le4,\quad \omega(H)\le5.
\]

For an exact-129 non-target color C, the source-verified Type-I factorization supplies a point x and twelve disjoint monochromatic K5 factors
\[
B_1,\ldots,B_{12}
\]
partitioning \(V(K_{61})\setminus\{x\}\). Every \(B_i\) meets the 14-point outside set O: otherwise \(B_i\subseteq H\) would be an independent 5-set in H.

Let \(b_i=|B_i\cap O|\). Thus \(b_i\ge1\).

- If \(x\in O\), then \(\sum b_i=13\), so the profile is \((2,1^{11})\).
- If \(x\in H\), then \(\sum b_i=14\), so the profile is either \((2,2,1^{10})\) or \((3,1^{11})\).

Because every \(B_i\) is a C-monochromatic K5, its H-interior \(B_i\cap H\) is an independent set in H. These intersections are disjoint and, together with \(\{x\}\) when \(x\in H\), partition H.

Therefore every exact-129 Type-I color induces exactly one of these three forbidden partition shapes:

| Position/profile | Independent-part partition of H |
|---|---|
| \(x\in O\), \((2,1^{11})\) | \(11\cdot4+1\cdot3\) |
| \(x\in H\), \((2,2,1^{10})\) | \(10\cdot4+2\cdot3+1\cdot1\) |
| \(x\in H\), \((3,1^{11})\) | \(11\cdot4+1\cdot2+1\cdot1\) |

The next lemma excludes all three shapes without using the low-layer edge count \(e_C(H)\).

## 2. Unified tight-part obstruction

### Lemma

Let H satisfy the core contract above. Suppose H is partitioned into r independent 4-sets
\[
P_1,\ldots,P_r
\]
and some smaller independent parts, in one of the following cases:

1. \(r=11\), with one 3-set;
2. \(r=10\), with two 3-sets and one singleton;
3. \(r=11\), with one 2-set and one singleton.

Then H contains an independent 5-set or a clique of size at least six. In particular, none of these partitions exists under \(\alpha(H)\le4\) and \(\omega(H)\le5\).

### Proof

For any two independent 4-sets P,Q, the bipartite graph H[P,Q] has a perfect matching. Otherwise Hall gives S subset P with \(|N_Q(S)|<|S|\), and
\[
S\cup(Q\setminus N_Q(S))
\]
is an independent set of size at least five.

More generally, for a 4-set P and an independent k-set T with \(k\in\{2,3\}\), H[P,T] has a matching saturating T by the same Hall argument. For a 4-set P and a singleton \(\{x\}\), at least one H-edge joins x to P, since otherwise \(P\cup\{x\}\) is an independent 5-set.

Choose these matchings independently and let M be their union. Edges chosen for different unordered pairs of parts are distinct.

The resulting edge and degree ledger is:

| Partition | \(e(M)\) | M-degree sum on each 4-part | Lower bound on F-degree sum per 4-part | Lower bounds on smaller parts |
|---|---:|---:|---:|---:|
| \(11\cdot4+3\) | 253 | \(4\cdot10+3=43\) | \(48-43=5\) | 3-part: \(3\cdot(12-11)=3\) |
| \(10\cdot4+3+3+1\) | 250 | \(4\cdot9+3+3+1=43\) | \(48-43=5\) | each 3-part: \(3\cdot(12-10)=6\); singleton: \(12-10=2\) |
| \(11\cdot4+2+1\) | 253 | \(4\cdot10+2+1=43\) | \(48-43=5\) | 2-part: \(2\cdot(12-11)=2\); singleton: \(12-11=1\) |

Put \(F=H\setminus M\). Since \(e(H)=285\), the total F-degree sum \(2e(F)\) is respectively 64, 70, and 64. The sum of the displayed lower bounds is 58, 64, and 58. In every case the total excess over all part lower bounds is exactly six.

Consequently at least \(r-6\) of the r four-parts are tight, meaning
\[
\sum_{v\in P}d_F(v)=5.
\]
There are therefore at least four tight 4-parts in case 2 and at least five in cases 1 and 3.

Fix a tight part P. Its four nonnegative F-degrees sum to five. The three vertices \(u_1,u_2,u_3\) with smallest F-degrees therefore satisfy
\[
d_F(u_1)+d_F(u_2)+d_F(u_3)\le3.
\]
They are independent because P is independent in H.

There are \(r-1\) other 4-parts. At most three of them contain an F-neighbor of one of the selected vertices. Hence at least
\[
(r-1)-3=r-4\ge6
\]
other 4-parts Q are clean: no F-edge joins any \(u_i\) to Q.

For each clean Q, the chosen perfect matching M[P,Q] sends \(u_1,u_2,u_3\) to three distinct vertices of Q. Since Q is clean, those are their only H-neighbors in Q. Let \(w_Q\) be the fourth vertex of Q. Then \(w_Q\) is nonadjacent to all three selected vertices.

For two clean parts Q,Q', if \(w_Qw_{Q'}\notin E(H)\), then
\[
\{u_1,u_2,u_3,w_Q,w_{Q'}\}
\]
is an independent 5-set, impossible. Thus all the \(w_Q\) are pairwise adjacent. Since there are at least six clean parts, they form a clique of size at least six, also impossible.

This proves the lemma.

## 3. Exact-color contradiction

The Type-I source factorization forces one of the three partition shapes in Section 1. The lemma excludes each shape. Thus:

\[
\boxed{\text{No exact-129 Type-I non-target color can exist on a valid Q32 core.}}
\]

The full-support Q32 branches m=8 and m=9 each require at least eight exact-129 Type-I colors. Hence both branches are analytically impossible.

This argument is stronger than the preceding \(e_C(H)\ge71\) result: it does not use the 69/70 near-Turán classification, the 37-unit edge-gap ledger, pivot matching composition, or any m-specific reserve bound.

## 4. Scope firewall and remaining global status

- **Closed by this lemma:** the E408/Q32 full-support v=47 branches m=8 and m=9, conditional on the registered Type-I factorization and the stated core contract.
- **Not claimed:** closure of other Q32 support cases, the E408/Q33 terminal, the E407 terminal, the front-end bridge, or the complete original Erdős r=12 theorem.
- The CSP solver is now archival for these two branches; a full SMT SAT/UNSAT run is not needed to establish this analytic contradiction.
- The independent verifier implements an augmenting-path replay of the Hall matching skeleton and returns an explicit independent 5-set or a clique of size at least six for each induced source partition.
