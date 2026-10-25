# E407 Q32: classify the general 15-vertex saturated kernel

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained alpha-critical kernel reduction and its explicit external-theorem dependencies.

## Theorem

Let \(J\) be a triangle-free, non-bipartite, triangle-saturated graph with
\[
|V(J)|=15,\qquad e(J)=49,\qquad \Delta(J)\le7.
\]
Then \(J\) is isomorphic to the blow-up of \(C_5\) with part sizes
\[
(1,2,5,5,2),
\]
equivalently \((5,5,2,1,2)\).

The hypotheses are exactly the structural output of the E407 saturated-kernel reduction: \(J=\overline C\) is triangle-free and triangle-saturated; the 49 witness labels give \(\Delta(J)\le7\). The reduction to this 15-vertex graph remains conditional on DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md.

## Proof

### 1. \(J\) has a vertex of degree at most five

Suppose instead that \(\delta(J)\ge6=2|V(J)|/5\). The equality case of the Andrásfai–Erdős–Sós minimum-degree theorem says that a triangle-free graph with minimum degree at least \(2n/5\) is either bipartite or, when \(5\mid n\), the balanced blow-up \(C_5(n/5)\). This equality case is stated explicitly by Keevash–Sudakov, *Sparse halves in triangle-free graphs*, J. Combin. Theory Ser. B 96 (2006), Section 3, p. 617; PDF: https://people.maths.ox.ac.uk/keevash/papers/sparse-halves-journal.pdf.

Since \(J\) is non-bipartite, it would have to be \(C_5(3)\), which has \(5\cdot9=45\) edges, contradicting \(e(J)=49\). Hence \(\delta(J)\le5\). Fix \(v\in V(J)\) with degree \(d\le5\).

### 2. \(J-v\) is bipartite

The induced graph \(J-v\) is triangle-free and has
\[
e(J-v)=49-d\ge44.
\]
By the Brouwer bound for a non-bipartite triangle-free graph on 14 vertices,
\[
e(G)\le t_2(14)-\lfloor14/2\rfloor+1
=49-7+1=43.
\]
This bound follows, for example, from Kang–Pikhurko, *Maximum \(K_{r+1}\)-free graphs which are not \(r\)-partite*, Matematychni Studii 24 (2005), Theorem 1; PDF: https://matstud.org.ua/texts/2005/24_1/24_1_012_020.pdf. Therefore \(J-v\) must be bipartite. Let its bipartition be \(X,Y\), with \(|X|=p\), \(|Y|=14-p\).

### 3. The missing cross-edges of \(J-v\) form exactly \(K_{a,b}\)

Put
\[
A=N_J(v)\cap X,\quad B=N_J(v)\cap Y,\quad
a=|A|,\quad b=|B|.
\]
Because \(J\) is non-bipartite, \(a,b\ge1\); otherwise \(v\) could be placed on the side opposite all its neighbours, making \(J\) bipartite. Also \(a+b=d\le5\), so \(a,b\le4\).

Every missing cross-edge \(xy\) of \(J-v\), with \(x\in X,y\in Y\), must have common neighbour \(v\): in the bipartite graph \(J-v\), vertices in opposite sides have no common neighbour. Since \(J\) is triangle-saturated, adding \(xy\) must create a triangle, which can only be \(vxy\). Thus every missing cross-edge has \(x\in A,y\in B\).

Conversely, every pair \(x\in A,y\in B\) is a missing edge, because otherwise \(vxy\) would be a triangle in \(J\). Therefore the missing cross-edge set is exactly the complete bipartite graph \(K_{a,b}\), and
\[
e(J-v)=p(14-p)-ab=49-d. \tag{1}
\]

### 4. The bipartition must be balanced

If \(p\le6\), then \(p-a\ge1\) because \(a\le4\). Any vertex \(x\in X\setminus A\) is adjacent in \(J-v\) to every vertex of \(Y\), since all missing cross-edges lie in \(A\times B\). Hence
\[
d_J(x)=14-p\ge8,
\]
contradicting \(\Delta(J)\le7\). Thus \(p\ge7\).

Similarly, if \(p\ge8\), then \(|Y|=14-p\ge5>b\), so \(Y\setminus B\ne\varnothing\). Every vertex \(y\in Y\setminus B\) is adjacent to every vertex of \(X\), giving \(d_J(y)=p\ge8\), again a contradiction. Thus \(p\le7\).

Consequently \(p=7\), and equation (1) becomes
\[
49-ab=49-d,
\qquad\text{so}\qquad ab=d=a+b.
\]
For positive integers \(a,b\), the equation \(ab=a+b\) is equivalent to
\[
(a-1)(b-1)=1,
\]
hence \(a=b=2\) and \(d=4\).

### 5. Identify the graph

The graph \(J-v\) is \(K_{7,7}\) with exactly the four edges between \(A\) and \(B\) deleted. The vertex \(v\) is adjacent to the two vertices of \(A\) and the two vertices of \(B\), and to no other vertices.

Let \(X'=X\setminus A\) and \(Y'=Y\setminus B\), so \(|X'|=|Y'|=5\). The five independent parts
\[
\{v\},\quad A,\quad Y',\quad X',\quad B
\]
form a \(C_5\)-blow-up in this cyclic order, with sizes \((1,2,5,5,2)\). This proves the theorem. \(\square\)

## Consequence for the E407 saturated branch

This theorem removes the prior classification gap: under the retained saturated-kernel reduction, every admissible \(J\) is the explicit local model already excluded from every full-core extension in DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md. Thus the **general \(\delta=14\), non-four-partite, \(K_5\)-saturated terminal is conditionally excluded**, not merely the single blow-up example.

The condition remains important: the component-count step in DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md uses Didin's 2026 preprint theorem, whose proof is not independently audited in this workstream. This result does not close the other \(\delta\) cases, the five E407 shell templates, or the original \(K_{145}\)-to-T61 bridge.
