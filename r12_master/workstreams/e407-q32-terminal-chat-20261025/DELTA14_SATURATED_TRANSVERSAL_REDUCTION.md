# E407 Q32: independent-transversal reduction of the saturated \(\delta=14\) branch

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL for the explicit C5-blow-up candidate only; not a universal saturated-branch theorem.**

Dependencies: the retained 47-core / 49-witness contract; the saturated-local-model reduction in DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md (whose component-count step depends on Didin's 2026 preprint theorem); and Brouwer's second Turán theorem for non-four-partite \(K_5\)-free graphs.

## 1. Frozen contract and the distinguished low-degree core vertex

Let \(H\) be the 47-vertex core, \(U\) the 29-point support, and \(W=V(H)\setminus U\), so \(|W|=18\). Assume
\[
e(H)=284,\quad \alpha(H)\le4,\quad \delta(H)\ge12,\quad
\sum_{v\in H}(d_H(v)-12)=4.
\]
For the saturated non-four-partite \(\delta=14\) branch, the exact ledger gives
\[
e(H[U])=98,\qquad e(H[W])=34-\epsilon_U,\qquad
0\le\epsilon_U:=\sum_{u\in U}(d_H(u)-12)\le2.
\]

For this candidate-specific theorem, assume the local graph is exactly
\[
H[U]=K_7^A\ \dot\cup\ K_7^B\ \dot\cup\ \overline J,
\]
where \(J\) is the explicitly verified \(C_5\)-blow-up with part sizes \((5,5,2,1,2)\). This is one realizable local model, not a classification of every graph \(J\) allowed by the saturated-branch reduction. The broader reduction only gives a 15-vertex triangle-free, non-bipartite, triangle-saturated graph with 49 edges; it does **not** yet prove that every such \(J\) is this blow-up.

The singleton vertex \(d_0\) of this explicit \(J\) has \(d_J(d_0)=4\), hence
\[
d_{H[U]}(d_0)=14-d_J(d_0)=10.
\]
Write \(\epsilon_{d_0}=d_H(d_0)-12\). Then
\[
\boxed{d_H(d_0,W)=2+\epsilon_{d_0}},\qquad
0\le\epsilon_{d_0}\le\epsilon_U\le2. \tag{1}
\]

## 2. The 18-point \(W\)-side is four clique parts with at most \(2-\epsilon_U\) cross edges

Since \(\alpha(H[W])\le4\), the complement \(\overline{H[W]}\) is \(K_5\)-free. Also
\[
e(\overline{H[W]})=\binom{18}{2}-e(H[W])=119+\epsilon_U.
\]
For \(18\) vertices, \(t_4(18)=121\), while Brouwer's second-Turán bound says a non-four-partite \(K_5\)-free graph has at most
\[
121-\lfloor18/4\rfloor+1=118
\]
edges. Thus \(\overline{H[W]}\) is four-partite.

Choose a four-partition \(W=P_1\dot\cup P_2\dot\cup P_3\dot\cup P_4\) into independent sets of \(\overline{H[W]}\). Each \(P_i\) is a clique in \(H[W]\). Put
\[
T(P_1,\ldots,P_4)=\sum_{i<j}|P_i||P_j|.
\]
Then
\[
119+\epsilon_U\le T(P_1,\ldots,P_4)\le121.
\]
The number \(q\) of \(H[W]\)-edges crossing between these four clique parts is exactly
\[
q=T(P_1,\ldots,P_4)-(119+\epsilon_U)\le2-\epsilon_U. \tag{2}
\]
Every part has size at least three: if a part had size at most two, the maximum possible \(T\) for a partition of 18 vertices into four parts would be \(117<119\).

The exact integer partition audit gives:
| \(\epsilon_U\) | part sizes | cross edges \(q\) |
|---:|---|---:|
| 0 | \((3,4,5,6)\), \((3,5,5,5)\), \((4,4,4,6)\), or \((4,4,5,5)\) | \(0,1,1,2\), respectively |
| 1 | \((3,5,5,5)\), \((4,4,4,6)\), or \((4,4,5,5)\) | \(0,0,1\), respectively |
| 2 | \((4,4,5,5)\) | \(0\) |

## 3. Independent-transversal lemma

**Lemma.** Suppose \(W\) is partitioned into four cliques \(P_1,\ldots,P_4\), each of size at least three, and at most two edges of \(H[W]\) join distinct parts. Then for every \(S\subseteq W\) with \(|S|\le2\), there is an independent transversal \(T\subseteq W\setminus S\) meeting each \(P_i\) in exactly one vertex.

**Proof.** Let \(t_i=|P_i\setminus S|\). There are \(N=\prod_i t_i\) candidate transversals. A cross-edge with endpoints in \(P_i,P_j\) can forbid at most \(N/(t_it_j)\) candidates. If \(S\) removes two vertices from one part, then \(t_i\ge1\) there and all other \(t_j\ge3\), so each of at most two forbidden fractions is at most \(1/3\); their sum is at most \(2/3<1\). If \(S\) removes one vertex from each of two parts, then those two \(t_i\)'s are at least two and the others at least three; each forbidden fraction is at most \(1/4\), so the sum is at most \(1/2<1\). If \(|S|\le1\), every edge's forbidden fraction is at most \(1/6\), so the sum is at most \(1/3<1\). In every case, the union of the forbidden choices is smaller than \(N\). At least one independent transversal remains. \(\square\)

A second consequence will be used below: if all four parts have size at least four and there is at most one cross-edge, then every \(S\subseteq W\) of size at most three also misses an independent transversal. Indeed, after removing three vertices, the smallest possible remaining part sizes are \(1,4,4,4\) (all three removed from one part), \(2,3,4,4\) (a \(2+1\) split), or \(3,3,3,4\) (a \(1+1+1\) split). A single cross-edge forbids at most \(1/4\), \(1/6\), or \(1/9\) of the candidate transversals, respectively, always strictly less than all candidates.

## 4. Eliminate \(\epsilon_U=0\)

If \(\epsilon_U=0\), then \(\epsilon_{d_0}=0\), and (1) gives \(|N_W(d_0)|=2\). By the independent-transversal lemma, there exists an independent four-set \(T\subseteq W\setminus N_W(d_0)\). Since \(T\) is independent and \(d_0\) is anticomplete to it, \(T\cup\{d_0\}\) is an independent five-set in \(H\), contradicting \(\alpha(H)\le4\).

Therefore, the explicit candidate has no extension when \\(\\epsilon_U=0\\).

The \\(\\epsilon_U=1\\) and \\(\\epsilon_U=2\\) residual W profiles are now excluded for this candidate by DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md. Combining the two files, the explicit \\((5,5,2,1,2)\\) blow-up candidate has no full 47-core extension for any \\(\\epsilon_U\\in\\{0,1,2\\}\\).

The universal kernel classification in DELTA14_SATURATED_KERNEL_CLASSIFICATION.md now proves that every admissible 15-vertex graph \\(J\\) under the retained saturated-kernel contract is this blow-up. Combining the two files therefore excludes the entire saturated \\(\\delta=14\\) terminal conditionally. The upstream Didin-preprint component-count dependency remains unaudited; the \\(\\delta\\le13\\) cases, all five shell templates, and the original \\(K_{145}\\)-to-T61 bridge remain OPEN / NOT_CERTIFIED.
