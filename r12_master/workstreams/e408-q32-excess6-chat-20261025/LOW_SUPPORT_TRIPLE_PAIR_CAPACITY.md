# Low-support triple-pair capacity theorem — E408 Q32

Status: **PROVED_CONDITIONAL strict support reduction** under the registered exact-129 Type-I classification. No 284-edge/excess-four statement is used. This theorem is uniform over both shell-support branches \(M[B]=\varnothing\) and \(M[B]\ne\varnothing\).

## 1. Contract and low-support normal form

Let \(H\) be the 47-vertex core with \(e(H)=285\), \(\alpha(H)\le4\), and \(\delta(H)\ge12\). Let \(R\) be the 61-point E408 residual, \(p\) the degree-13 pivot, \(A=N_F(p)\), and \(H=V(R)\setminus(A\cup\{p\})\). The outside set is \(O=\{p\}\cup A\), with \(|O|=14\).

For every exact-129 non-target color \(C\), the registered Type-I equality structure supplies twelve pairwise-disjoint 5-cliques in \(C[R]\): ten isolated \(K_5\) components and two \(K_5\) cliques in the 11-point exceptional gadget. Every such clique meets \(O\), because otherwise it would be a 5-set independent in target \(H\), contradicting \(\alpha(H)\le4\).

Let \(Q_C\) be the union of the 4-point core parts of the cliques having exactly one outside-\(H\) vertex. Each such part is an independent 4-set in \(H\). If the exceptional gadget vertex lies outside \(H\), the twelve cliques have at most thirteen outside-\(H\) vertices available, so at least eleven cliques have exactly one outside vertex and the witness union has size at least 44. If any clique has three outside vertices, the same conclusion holds. Therefore, to analyze a putative support size \(v<44\), every exact color must have:
- exceptional gadget vertex \(x_C\in H\);
- exactly ten cliques with one outside-\(H\) vertex;
- exactly two cliques with two outside-\(H\) vertices;
- no clique with three outside-\(H\) vertices.

The two double-outside cliques cannot contain \(p\), because \(p\) is target-adjacent to every shell vertex. Their two outside vertices are therefore shell vertices forming an edge of \(M=\overline{F[A]}\). Their three-point core parts are disjoint independent triples \(T_{C,1},T_{C,2}\subset H\).

The ten independent 4-sets in \(Q_C\) are pairwise disjoint, so \(|Q_C|=40\). Let \(U\) be the union of all exact-color 4-set witnesses, \(v=|U|\), \(W=H\setminus U\), and \(O_C=U\setminus Q_C\). Then
\[
|W|=w=47-v,\qquad |O_C|=v-40,\qquad H\setminus Q_C=W\dot\cup O_C.
\]
The two triples and the exceptional vertex partition this seven-point remainder:
\[
W\dot\cup O_C=T_{C,1}\dot\cup T_{C,2}\dot\cup\{x_C\}.
\]

## 2. Pair uniqueness inside the common complement \(W\)

For any triple \(T\), write \(k(T)=|T\cap W|\). The number of unordered pairs of \(W\)-vertices used inside the two triples of color \(C\) is
\[
\kappa_C=\binom{k(T_{C,1})}{2}+\binom{k(T_{C,2})}{2}.
\]

No pair of \(W\)-vertices can be used by two distinct triples in this family. If a pair \(\{u,v\}\subseteq W\) occurred in triples from two different colors, the edge \(uv\) would receive two colors. The two triples of one color are disjoint, so they do not repeat a pair either. Hence
\[
\boxed{\sum_{C:\,e_C(R)=129}\kappa_C\le \binom w2.} \tag{1}
\]

Because \(T_{C,1},T_{C,2},x_C\) partition \(W\dot\cup O_C\), their total number of \(W\)-vertices is
\[
k(T_{C,1})+k(T_{C,2})=
\begin{cases}
w-1,&x_C\in W,\\
w,&x_C\in O_C.
\end{cases}
\]
Each triple has at most three vertices. The minimum possible \(\kappa_C\) for a given sum \(s\) is \(\min_{k_1+k_2=s,\ 0\le k_i\le3}\{\binom{k_1}{2}+\binom{k_2}{2}\}\).

## 3. Exact finite boundary table

| Support \(v\) | \(w=47-v\) | \(|O_C|=v-40\) | Minimum \(\kappa_C\) if \(x_C\in W\) | Minimum \(\kappa_C\) if \(x_C\in O_C\) | Available pairs \(\binom w2\) |
|---:|---:|---:|---:|---:|---:|
| 40 | 7 | 0 | 6 | impossible | 21 |
| 41 | 6 | 1 | 4 | 6 | 15 |
| 42 | 5 | 2 | 2 | 4 | 10 |
| 43 | 4 | 3 | 1 | 2 | 6 |

There are \(m\in\{8,9,10\}\) exact-129 colors. In each row, even the smallest per-color pair cost multiplied by eight exceeds the total available \(W\)-pair count:
\[
\begin{array}{c|c|c}
v&8\min\kappa_C&\binom{47-v}{2}\\\hline
40&48&21\\
41&32&15\\
42&16&10\\
43&8&6
\end{array}
\]
This contradicts (1) in every case \(v\in\{40,41,42,43\}\).

If \(v<40\), one color's ten disjoint 4-set witnesses already force \(v\ge40\). If any exact color has eleven single-outside cliques, then \(v\ge44\) directly. Consequently:
\[
\boxed{\ v\ge44\quad\text{for every E408 Q32 candidate under the registered contracts.}\ }
\]
This strict support reduction does not depend on whether \(M\) contains an independent 10-set.

## 4. Residual normal form at \(v=44\)

If \(v=44\), then \(|W|=3\) and every color with exactly ten witnesses has \(|O_C|=4\). If \(x_C\in O_C\), its two triples contain all three \(W\)-vertices, so at least one triple contains a pair from \(W\), costing at least one of the three available \(W\)-pairs. Pair uniqueness therefore implies that at most three exact colors can have \(x_C\in O_C\), and at most three colors in total can use any \(W\)-pair inside a triple.

Thus at least \(m-3\) colors have \(x_C\in W\) and zero \(W\)-pair cost. For each such color, the two triples split the two vertices of \(W\setminus\{x_C\}\) between them: each triple contains exactly one \(W\)-vertex and two vertices of \(O_C\).

This is a strict finite incidence terminal, not a contradiction. The current theorem does not bound the case \(v\ge44\).

## 5. Dependency firewall

The proof uses only:
- the 47-point 285-edge core contract and \(\alpha(H)\le4\);
- the registered exact-129 Type-I factorization into twelve disjoint \(K_5\) cliques plus the exceptional vertex;
- uniqueness of edge colors.

It does not use \(e(H)=284\), a four-unit core excess, the \(M[B]=\varnothing\) split, a SAT result, or an unverified degree claim about the exceptional gadget vertex.
