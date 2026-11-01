# Independent degree-12 four-set and ten-orbit classification

**Status:** PROVED (analytic; Brooks' theorem is the only external input).  
**Contract:** \(|V(H)|=47\), \(e(H)=286\), \(\delta(H)\geq12\), \(\alpha(H)\leq4\), \(\omega(H)\leq11\).

## 1. Existence of an independent degree-12 four-set

Put \(\epsilon(v)=d_H(v)-12\). The handshake lemma gives
\[
\sum_{v\in V(H)}\epsilon(v)=572-564=8.
\]
Since every positive excess is an integer at least one, at most eight vertices have positive excess. Let
\[
X=\{v:d_H(v)=12\}.
\]
Then \(|X|\geq39\). The induced graph \(H[X]\) has maximum degree at most12 and has no \(K_{13}\), since \(\omega(H)\leq11\).

Every connected component of \(H[X]\) is 12-colorable. Indeed, if its maximum degree is at most11, greedy coloring uses at most12 colors. If its maximum degree is12, Brooks' theorem applies: the component is not complete (there is no \(K_{13}\)) and cannot be an odd cycle (its maximum degree is12), so its chromatic number is at most12. Reusing the same palette on all components gives a proper 12-coloring of \(H[X]\).

One color class has size at least
\[
\left\lceil\frac{|X|}{12}\right\rceil
\geq\left\lceil\frac{39}{12}\right\rceil=4.
\]
Every vertex in this class has degree exactly12 in \(H\), and the class is independent. Thus there is an independent four-set \(I=\{s_0,s_1,s_2,s_3\}\) of degree-12 vertices.

## 2. Private cliques and incidence surplus

For \(x\notin I\), define \(\sigma(x)=N_H(x)\cap I\). Since \(\alpha(H)\leq4\), every such \(x\) has \(|\sigma(x)|\geq1\). The four seed vertices are independent and each has degree12, so
\[
\sum_{x\notin I}|\sigma(x)|=48.
\]
There are 43 vertices outside \(I\), hence
\[
\sum_{x\notin I}(|\sigma(x)|-1)=48-43=5.
\]

Let \(Z=\{x\notin I:|\sigma(x)|\geq2\}\), \(h=|Z|\), and
\[
P_i=\{x\notin I:\sigma(x)=\{s_i\}\},\qquad K_i=P_i\cup\{s_i\}.
\]
Each \(K_i\) is a clique. If two vertices of \(P_i\) were nonadjacent, they together with the other three seeds would form an independent five-set. Thus \(|P_i|\leq10\).

Write \(d_i=|N(s_i)\cap Z|\). Since \(d_H(s_i)=12\),
\[
|K_i|=1+|P_i|=13-d_i.
\]
The bound \(|P_i|\leq10\) gives \(d_i\geq2\). Counting incidences between \(Z\) and \(I\),
\[
\sum_i d_i=\sum_{z\in Z}|\sigma(z)|=h+5.
\]
Since each \(d_i\geq2\), \(h+5\geq8\), so \(h\geq3\). Since every \(z\in Z\) has support size at least two, \(h+5\geq2h\), so \(h\leq5\). Therefore \(h\in\{3,4,5\}\) and \(\sum_i d_i=h+5\).

## 3. Complete classification of the support multisets

A support of size two is viewed as an edge of a loopless multigraph on the four seed labels; repeated supports give parallel edges. The incidence degree of label \(i\) is \(d_i\), and every \(d_i\geq2\).

### \(h=3\)

There are eight total incidences. The support-size multiset is either \(4,2,2\) or \(3,3,2\).

- For \(4,2,2\), each seed already has one incidence from the four-support, so the two pairs must cover every label exactly once. They are complementary, giving \(\{0123,01,23\}\).
- For \(3,3,2\), let the two triples omit labels \(i,j\). Those labels need one further incidence, while the other two already have two. The pair must be \(ij\), giving \(\{01,023,123\}\) up to relabeling.

Thus there are exactly two orbits, with clique sizes \(11,11,11,11\).

### \(h=4\)

There are nine total incidences, so the support sizes are \(3,2,2,2\). The three pair supports form a loopless three-edge multigraph on four labels. Every label has positive degree, and the label omitted by the triple has degree at least two.

A loopless multigraph with three edges covering four vertices is either a three-edge star, a three-edge path, or a doubled edge disjoint from a single edge. The distinguished omitted label must respectively be the star center, an internal path vertex, or an endpoint of the doubled edge. These give exactly
\[
\{01,02,03,123\},\quad
\{01,012,03,23\},\quad
\{01,01,023,23\}.
\]
The clique sizes are \(10,11,11,11\).

### \(h=5\)

There are ten total incidences, so all five supports have size two. The support multigraph has five edges and minimum degree two. Its degree sequence is either \((4,2,2,2)\) or \((3,3,2,2)\).

- For \((4,2,2,2)\), let 0 be the degree-four vertex. The other three vertices have degree two. The only possibility is two parallel edges \(01\), single edges \(02,03\), and the edge \(23\), giving \(\{01,01,02,03,23\}\). The clique sizes are \(9,11,11,11\).
- For \((3,3,2,2)\), let \(u,v\) be the degree-three vertices and \(x,y\) the degree-two vertices. Let \(k\) be the multiplicity of \(uv\). The value \(k=0\) is impossible, since \(u,v\) would require six incidences across only five edges. If \(k=1\), the remaining multigraph is 2-regular on four vertices, hence a 4-cycle or two doubled disjoint edges; these give \(D\) and \(P\). If \(k=2\), the remaining edges are one edge from each high vertex to a low vertex, together with \(xy\); this gives \(B\). If \(k=3\), the remaining two edges form a double edge \(xy\); this gives \(C\).

Thus the four orbits are
\[
P=\{01,02,02,13,13\},\quad
D=\{01,02,03,12,13\},
\]
\[
B=\{01,01,02,13,23\},\quad
C=\{01,01,01,23,23\},
\]
with clique sizes \(10,10,11,11\).

In total there are exactly \(2+3+1+4=10\) support orbits.
