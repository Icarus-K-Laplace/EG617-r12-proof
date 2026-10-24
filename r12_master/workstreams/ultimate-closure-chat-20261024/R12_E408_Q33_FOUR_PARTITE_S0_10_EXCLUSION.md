# E408 Q33 four-partite boundary: exclude the S0=10 equality kernel

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the E408 Q33/d3 witness-packing contract. This strengthens the sibling four-partite bound from \(S_0\ge10\) to \(S_0\ge11\); it does not close the full E408 Q33 terminal.

## 1. Frozen four-partite kernel

Let H be the 47-vertex, 284-edge core with \(\alpha(H)\le4\), minimum degree 12, and total degree excess four. Assume the E408 Q33 minimum-support boundary:
- \(U\) has 31 vertices and is the union of 56 selected independent 4-sets \(\mathcal Q\);
- the Q-sets are linear: distinct Q-sets intersect in at most one vertex;
- \(W=V(H)\setminus U\) has 16 vertices;
- \(L=\overline{H[U]}\) is four-partite.

The 56 edge-disjoint witness K4s force the part sizes of L to be \(8,8,8,7\). Call the three 8-point parts A,B,C and the 7-point part D.

Every pair between D and any of A,B,C occurs in exactly one Q block: there are \(8\cdot7=56\) possible pairs and 56 blocks, with no repeated pair. Thus each d in D occurs in eight Qs, and each point in A union B union C occurs in seven Qs. Between any two large parts, the eight pairs not used by Q blocks form a perfect matching. Let \(\delta\) be the number of those 24 uncovered pairs that are present as extra edges of L, and let \(\epsilon_U=\sum_{u\in U}(d_H(u)-12)\). The exact core budget gives
\[
\delta+\epsilon_U\le17,\qquad
x:=e_H(U,W)=114+\epsilon_U+2\delta.
\]

Every \(w\in W\) must hit every Q, or \(Q\cup\{w\}\) would be an independent 5-set in H. Put \(q_w=|N_H(w)\cap U|\). Then \(q_w\ge7\). If \(q_w=7\), its neighbourhood is exactly D: each point of U occurs in at most eight blocks, so seven points can hit 56 blocks only if every selected point has incidence eight, which characterizes D.

At least three vertices of D have zero excess, because the total core excess is four. Each has exactly six neighbours in W. Therefore at most six vertices of W can have \(U\)-neighbourhood D.

## 2. The degree pattern forced by \(S_0=10\)

Set \(S_0=\epsilon_U+2\delta\), so \(x=114+S_0\). Suppose \(S_0=10\). Then
\[
\epsilon_U=10-2\delta,\qquad
0\le\epsilon_U\le4,\qquad
\delta\in\{3,4,5\}.
\]
Let k be the number of W vertices with \(q_w=7\), equivalently with neighbourhood D. All other W vertices have \(q_w\ge8\), so
\[
124=x\ge7k+8(16-k)=128-k.
\]
Together with \(k\le6\), this gives \(k\in\{4,5,6\}\).

For a hitting set T of size 8 or 9, either T contains all of D or it contains a full large part A, B, or C. Indeed, if T omits any d in D, its eight Q blocks require eight distinct large-part vertices, since each large-part vertex can meet at most one block containing d. Thus T contains at most one D point and at least eight large-part points. If no large part is fully contained, a missing point a in any large part has seven Q blocks; these must be hit by vertices outside that part, with at most one of those hits supplied by the single D point. Consequently each large part contributes at most two points, for at most six large-part points total, contradiction.

For any large part G, at least \(8-\delta-\epsilon_U=\delta-2\ge1\) of its vertices have zero excess and retain both H-neighbours in the other two large parts. Such a vertex has degree nine inside U and hence exactly three neighbours in W. Therefore at most three W vertices can have a neighbourhood containing an entire large part.

At most \(6-k\) W vertices beyond the k size-seven neighbourhoods can have a neighbourhood containing all of D: the three zero-excess D vertices already have their six W-neighbours among those k vertices. Hence at least
\[
(16-k)-(6-k)=10
\]
of the remaining W vertices must have a full large-part neighbourhood. The capacity bound is only three per each of A,B,C, so at most nine such vertices are possible. This contradiction excludes k=4 and k=5.

If k=6, the ten remaining vertices have total U-degree \(124-42=82\). As each has degree at least eight, their only possible degree multisets are
\[
(8^{10}),\quad (8^9,9),\quad (8^8,9^2),\quad (8^9,10),
\]
with the first three ruled out by the same “at least ten full-large-part neighbourhoods, capacity nine” argument. Thus the only possible pattern is:
- six W vertices have U-neighbourhood D;
- nine W vertices have U-neighbourhood equal to a full large part, exactly three for each of A,B,C;
- one exceptional vertex \(w_*\) has \(T_*=N_H(w_*)\cap U\) of size ten, containing no full large part and not all of D.

The final condition implies \(s:=|T_*\cap D|\le2\): if D is not contained in \(T_*\), any omitted d in D needs eight distinct large-part points to hit its eight blocks, but \(T_*\) has only \(10-s\) large-part points.

## 3. The exceptional size-ten hitting set cannot exist

Write \(t_A=|T_*\cap A|\), \(t_B=|T_*\cap B|\), \(t_C=|T_*\cap C|\). Because \(T_*\) contains no full large part, each \(t_i\le7\), and \(t_A+t_B+t_C=10-s\).

### Case s=0

For any missing point a in A, the seven Q blocks containing a must be hit by distinct points of B union C. Hence \(t_B+t_C\ge7\), so \(t_A\le3\). The same argument applies to B and C. Then \(t_A+t_B+t_C\le9\), contradicting the required sum 10.

### Case s=1

There are nine large-part points, and one selected D point can hit at most one of the seven Q blocks containing a fixed a in A. The remaining six blocks require distinct points from B union C, so \(t_A\le3\); similarly \(t_B,t_C\le3\). Their sum is nine, hence
\[
t_A=t_B=t_C=3.
\]

Fix any unselected d in D. Its eight Q blocks receive nine incidences from the nine selected large-part points, and every selected point occurs in exactly one block with d. Since all eight blocks must be hit, exactly one block is hit twice and all others once. Thus each of the six unselected D points supplies one distinct selected cross-part pair whose Q block has that D label. There are six such pairs total.

There are 27 selected cross-part pairs in \(T_*\), three pairs of large parts each contributing \(3\cdot3=9\). At most nine of these can be Q pairs whose D label is the one selected point: for each pair of large parts, its blocks with a fixed D point form a matching and contain at most three pairs from the selected 3-by-3 subsets. At most \(\delta\le5\) selected pairs can instead be extra L edges. Therefore
\[
27\le6+9+\delta\le20,
\]
a contradiction.

### Case s=2

There are eight large-part points. For a missing a in A, the two selected D points hit two distinct blocks containing a, so the remaining five blocks require five distinct points from B union C. Hence \(t_A\le3\), and likewise for B,C. The only possible multiset is
\[
(t_A,t_B,t_C)=(3,3,2)
\]
up to permutation.

For any unselected d in D, its eight Q blocks receive exactly eight incidences from the eight selected large-part points. Thus each block is hit exactly once. No selected pair from two large parts can lie in a Q block labelled by an unselected D point. For a pair of large parts with selected-set sizes \(a,b\), at most \(2\min(a,b)\) selected pairs can be Q pairs labelled by one of the two selected D points. Therefore at least \(ab-2\min(a,b)\) of their selected pairs must be extra L edges.

For sizes (3,3,2), the three pair types require at least
\[
3\cdot3-2\cdot3=3,\quad
3\cdot2-2\cdot2=2,\quad
3\cdot2-2\cdot2=2
\]
extra L edges, seven in total. But \(\delta\le5\). Contradiction.

All possible s are excluded, so \(w_*\) cannot exist. This contradicts \(S_0=10\).

## 4. Conclusion and scope

The four-partite E408 Q33 minimum-support boundary satisfies
\[
\boxed{\epsilon_U+2\delta\ge11,\qquad \delta+\epsilon_U\le17.}
\]
This strictly strengthens the sibling result \(S_0\ge10\), by excluding the sole residual equality pattern \(k=6,(q_w)=(7^6,8^9,10)\).

This theorem is conditional on the retained four-partite boundary and exact-129 witness-packing contracts. It does not address the non-four-partite E408 Q33 boundary, E408 Q32's 285-edge core, other support sizes, the T61-to-K145 bridge, or the original EG617 theorem. The global result remains OPEN / NOT_CERTIFIED.
