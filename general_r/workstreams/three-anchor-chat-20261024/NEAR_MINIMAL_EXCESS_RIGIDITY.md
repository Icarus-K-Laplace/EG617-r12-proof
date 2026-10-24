# Near-minimal excess rigidity — Round 2

## Status

- Frozen theorem \(K\ge8\) for every \(r\ge12\): unchanged.
- **New proved strengthening:** \(K\ge10\) for every \(r\ge14\).
- **Full \(K=8\) equality classification:** OPEN_GAP, restricted to \(r=12,13\).
- No whole-graph SAT/ILP search was run; all claims below are analytic.

## 1. General finite-support rigidity

Let \(x_v=d_H(v)-r\ge0\) and \(K=\sum_vx_v\). If \(K\le16\), then
\[
|\operatorname{supp}(x)|\le K\le16,
\]
and the positive excess values form an integer partition of \(K\). The three anchors never belong to this support, since their degrees are exactly \(r\).

For any connector set \(C\) and exclusive blocks \(X_i\), define
\[
K_C=\sum_{z\in C}x_z,\qquad
K_X=\sum_i\sum_{v\in X_i}x_v.
\]
There are no other vertices, so \(K=K_C+K_X\). In particular, an equality argument must account for every positive excess in the connectors and exclusive blocks; an arithmetic rectangle profile by itself is not a graph construction.

## 2. Reusable exact charge interface

For \(v\in X_i\), the baseline number of external neighbours outside \(X_i\cup\{a_i\}\) is \(b_i=2+d_i\). If \(F_v\) is any set of **distinct, actually forced external neighbours** of \(v\), then
\[
x_v\ge (|F_v|-b_i)_+.
\tag{2.1}
\]
The set \(F_v\) must be a union of forced neighbours from all rectangles/focus constraints; it must not count the same vertex twice.

For a pair connector \(z\) incident with \(a_i,a_j\) and missing \(a_k\), let \(a,b\) be its nonneighbour counts in \(X_i,X_j\), \(n_k=|N(z)\cap X_k|\), and \(\gamma_z\) its number of connector-neighbours. The exact equation is
\[
a+b=r-2-d_i-d_j+\gamma_z+n_k-x_z.
\tag{2.2}
\]
For a triple connector \(z\),
\[
\sum_i |N(z)\cap X_i|=r-3+x_z-\gamma_z.
\tag{2.3}
\]
Equations (2.1)–(2.3) form a backend-ready local interface: connector excess is charged once at the connector; each exclusive vertex excess is charged once using the union of its forced external-neighbour sets.

If a rectangle family has disjoint opposite blocks, the established pointwise inequality permits additive rectangle charges. If supports can overlap, use the union-load bound (2.1), or the safe connector-pair bound \(k_1+k_2+\max(R_1,R_2)\) only where its hypotheses hold. Never add two \(R\)-charges merely because two rectangles have been named.

## 3. Rectangle thresholds available for all \(r\)

For positive integers \(a,b\), the exact rectangle lower bound is
\[
R_{pq}(a,b)=a(b-p)_++b(a-q)_+.
\]
The following bounds are proved by the frozen audit:
\[
\begin{array}{ll}
R_{22}\ge a+b-4,&R_{22}\ge a+b-3\quad(a+b\ge5),\\
R_{23}\ge a+b-5,&R_{23}\ge a+b-4\quad(a+b\ge6),\\
R_{24}\ge a+b-6,&R_{24}\ge a+b-5\quad(a+b\ge7),\\
R_{33}\ge a+b-6,&R_{33}\ge a+b-4\quad(a+b\ge7).
\end{array}
\tag{3.1}
\]
A pair connector with \(a,b\ge1\) therefore has a local necessary cost \(x_z+R_{pq}(a,b)\), but the exact degree equation (2.2), focus capacities, and overlap rule must still be checked. The threshold alone is not a sufficiency statement.

## 4. The \(K=8\) rigidity theorem

**Theorem.** Under the frozen three-anchor hypotheses, if \(K=8\), then
\[
r\le13.
\]
Consequently,
\[
\boxed{K\ge10\quad\text{for every }r\ge14.}
\]

**Proof outline with the new equality work.**

1. **\(c=2,(0,0,0)\):** the generalized empty-part self-consistency argument rules out an empty \(E_i\) for \(r\ge13\). The degree-two transversal-cover lemma and size count then rule out \(r\ge14\); the remaining \(r=13\) equality forces \(E_1=E_2=2,E_3=11\), a complete \(E_1-E_2\) bipartite graph, and then an impossible connector-neighbour count. Thus \(c=2\) equality is restricted to \(r=12\).
2. **\(c=3,(0,0,1)\):** both-focused is impossible. Both-nonfocused charges rule out \(r\ge13\), and the \(r=12\) equality is contradicted by the common-nonneighbour clique and saturated rectangle vertices. In the mixed-focus branch, the local bound excludes \(r\ge16\); the \(r=15\) equality is excluded by a common-nonneighbour clique of size at least fifteen. The \(r=14\) local profile list is exhausted: every profile either creates a too-large common-nonneighbour clique or makes a saturated rectangle vertex lie in such a clique with an opposite-block vertex. Thus only \(r=12,13\) remain.
3. **\(c=4,(0,0,2)\):** \(f=0\) and \(f=1\) are excluded for \(r\ge13\). The \(f=2\) overlap inequality excludes \(r\ge15\); its \(r=14\) equality is impossible by external-incidence counting, and the \(r=13\) one-singleton profiles are also impossible because the opposite long block needs 22 external incidences but can receive at most fifteen from the rectangle, connector, focus, and residual-excess slots. Thus only \(r=12\) remains.
4. **\(c=4,(0,1,1)\):** the \(s=0,1\) branches are excluded for \(K=8\). The only remaining \(s=2\) ownership pattern is the \(V/W\) pattern. The overlap inequality excludes \(r\ge15\); the \(r=14\) one-singleton equality is ruled out by the opposite size-12 block's 24 external-incidence requirement. Thus only \(r=12,13\) remain.

Since \(K\) is even, exclusion of \(K=8\) for \(r\ge14\), together with the frozen \(K\ge8\) theorem, gives \(K\ge10\) there. \(\square\)

## 5. Remaining \(K=8\) strata

The current analytic reduction is:

| Geometry | Remaining \(K=8\) parameter stratum |
|---|---|
| \(c=2,(0,0,0)\) | \(r=12\), empty-part exceptional layer or nonempty \((1,2)/(2,2)\) transversal-cover layer |
| \(c=3,(0,0,1)\) | \(r=12,13\), mixed focus only |
| \(c=4,(0,0,2)\) | \(r=12,f=0\) with same-group adjacency; \(r=12,f=1\); or \(r=12,f=2\) |
| \(c=4,(0,1,1)\) | \(r=12,13,s=2\), \(V/W\) own the two deficit-one focus slots |

This is a classification of necessary parameter strata, not a classification of realizable graphs. No remaining stratum is promoted to an actual graph, and no claim \(K\ge10\) is made for \(r=12,13\).

## 6. Limits of the backend interface

The interface above precisely controls connector excess, focused-neighbour capacity, and rectangle charge without double-counting. It does **not** by itself prove a repivot-termination theorem: residual-pivot costs and repeated colour-incidence variables must be mapped to these graph vertices/edges by the backend workstream before they can be added to the budget. No such unverified identification is assumed here.
