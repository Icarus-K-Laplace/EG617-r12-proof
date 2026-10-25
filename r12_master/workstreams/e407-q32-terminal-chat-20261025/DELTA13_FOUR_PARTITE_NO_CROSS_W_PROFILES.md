# E407 Q32 — exclude the delta-13 four-partite-U / anticomplete-W profiles

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained T61 / exact-129 49-witness core contract, the four-partite hypothesis on \(L=\overline{H[U]}\), and \(\omega(H)\le 11\). This theorem closes only the no-cross-edge \(W\)-profiles listed below.

## 1. Contract and exact U-side structure

Assume
\[
|H|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12,\quad \sum_{x\in H}\epsilon_x=4,
\]
where \(\epsilon_x=d_H(x)-12\ge0\). Let \(U\subset V(H)\), \(|U|=29\), and \(W=H\setminus U\), \(|W|=18\). Assume the E407 Q32 boundary contract: there are 49 pairwise edge-disjoint independent 4-sets on \(U\), seven from each of seven exact-129 colors, and
\[
e(H[U])=112-\delta,\quad e(H[W])=48-\epsilon_U-\delta,\quad
e_H(U,W)=124+\epsilon_U+2\delta,
\]
where \(\epsilon_U=\sum_{u\in U}\epsilon_u\).

In this theorem \(\delta=13\), \(1\le\epsilon_U\le3\), and \(L=\overline{H[U]}\) is assumed four-partite.

Every witness 4-set is a \(K_4\) in \(L\), hence meets each part of its 4-partition once. Each color supplies seven disjoint transversals. Therefore every part has at least seven vertices; since \(|U|=29\), the part sizes are \(7,7,7,8\). Name the parts \(A,B,C,D\), with \(|A|=|B|=|C|=7\) and \(|D|=8\).

For each pair of small parts, say \(A,B\), the 49 witnesses use 49 distinct \(A\)-\(B\) pairs: each of seven classes contributes seven such pairs, and a pair cannot repeat because the witnesses are edge-disjoint in \(L\). Since \(|A\times B|=49\), every \(A\)-\(B\) pair occurs exactly once. The same holds for \(A,C\) and \(B,C\). Thus every edge of \(H[U]\) joining distinct parts goes between \(D\) and \(A\cup B\cup C\). Since
\[
e(H[U])=112-13=99,\qquad
\sum_{P\in\{A,B,C,D\}}\binom{|P|}{2}=91,
\]
there are exactly eight such cross-edges.

Moreover, each small-part vertex \(u\in A\cup B\cup C\) is paired with seven distinct vertices of \(D\), one in each exact-color class. Those seven partners are distinct because the corresponding \(u d\) pairs are edges of \(L\) and cannot be reused by edge-disjoint witnesses. As \(|D|=8\), at most one \(D\)-pair at any small vertex is absent from \(L\). In particular,
\[
\boxed{d_{H[U]}(u,D)\le1\quad (u\in A\cup B\cup C).} \tag{1}
\]
This is the small-side incidence fact used below.

## 2. W ledger and saturation lemmas

The exact edge ledger gives
\[
e(H[W])=35-\epsilon_U,\qquad
E_W:=\sum_{w\in W}\epsilon_w=4-\epsilon_U.
\]

Suppose \(H[W]\) is a disjoint union of four cliques \(C_1,C_2,C_3,C_4\) with no edges between components. Every \(u\in U\) is complete to at least one \(C_i\); otherwise one non-neighbour from each component, together with \(u\), would be an independent 5-set. Thus, for
\[
S_i=\{u\in U:u\text{ is adjacent to every vertex of }C_i\},
\]
we have
\[
29=|U|\le\sum_{i=1}^4|S_i|. \tag{2}
\]

The same independent-transversal argument shows every \(d\in D\) is complete to some \(C_i\). If \(t_d=d_{H[U]}(d,A\cup B\cup C)\), then
\[
d_H(d,W)=5+\epsilon_d-t_d\ge m,\qquad
t_d\le5+\epsilon_d-m\le5+\epsilon_U-m, \tag{3}
\]
where \(m=\min_i|C_i|\).

**Reverse-saturation lemma.** If \(w\in W\) is not complete to any of \(A,B,C,D\), then
\[
\boxed{d_H(w,U)\ge 9+m-\epsilon_U.} \tag{4}
\]
Indeed, let \(D'\) and \(A',B',C'\) be its non-neighbour sets in the four U-parts. For each \(d\in D'\), every triple in \(A'\times B'\times C'\) must contain a vertex joined to \(d\) by an \(H[U]\) cross-edge, or that triple together with \(w,d\) would be an independent 5-set. Hence at least one of \(A',B',C'\) is contained in \(N_H(d)\), and its size is at most \(t_d\). Distinct \(d\in D'\) require distinct small parts, by (1). For \(|D'|=1\), (3) gives at most \((5+\epsilon_U-m)+7+7+1\) non-neighbours in \(U\), proving (4). For \(|D'|=2\), the two selected small non-neighbour sets are distinct and each has size at most \(5+\epsilon_U-m\); this gives a stronger lower bound. For \(|D'|=3\), all three small sets have that bound and again give a stronger lower bound. The case \(D'=\varnothing\) would make \(w\) complete to \(D\), contrary to assumption.

A W-vertex complete to a U-part has a unique such part: its U-degree is at most \(13\), whereas two U-parts together have at least \(7+7=14\) vertices. Call that part its label. For a component \(C_s\cong K_s\), write \(E_s=\sum_{w\in C_s}\epsilon_w\). A labelled vertex has U-degree \(13-s+\epsilon_w\); its extra-edge load beyond its label part is at most \(6-s+\epsilon_w\) for a small-part label, and at most \(5-s+\epsilon_w\) for label \(D\).

## 3. Exact no-cross-edge W profiles

Since \(\alpha(H[W])\le4\), four disjoint clique components have total edge count \(\sum_i\binom{|C_i|}{2}=35-\epsilon_U\). The sorted positive integer partitions of 18 give exactly:
\[
\begin{array}{c|c|c}
\epsilon_U & (|C_1|,|C_2|,|C_3|,|C_4|) & E_W\\\hline
1&(3,4,5,6)&3\\
2&(3,5,5,5)\ \text{or}\ (4,4,4,6)&2\\
3&(4,4,5,5)&1
\end{array}
\]
We exclude all four profiles.

## 4. Case \(\epsilon_U=1\): \(K_3\dot\cup K_4\dot\cup K_5\dot\cup K_6\)

Here \(m=3\), so (4) gives threshold \(d_H(w,U)\ge11\) for any unsaturated W-vertex. Put \(E_3+E_4+E_5+E_6=3\).

The common-neighbour capacities are
\[
|S_3|\le9+E_3+\mathbf1_{E_3=0},\quad
|S_4|\le8+E_4+\mathbf1_{E_4=0},\quad
|S_5|\le5+E_5,\quad
|S_6|\le\lfloor E_6/2\rfloor. \tag{5}
\]
Justification:
- For \(K_3\), if all vertices are labelled and labels are mixed, each common neighbour uses an extra edge, with total load at most \(9+E_3\). If all labels agree, the label part has size 7 or 8 and each common neighbour outside it uses three extra edges; the bound in (5) follows. If a vertex is unsaturated, its excess is at least one; the remaining U-degree bounds give the same cap.
- For \(K_4\), mixed labels give the \(8+E_4\) cap. A common label \(D\) is forbidden by \(\omega(H)\le11\); a common small label contributes its seven vertices and each additional common neighbour costs four extra edges, giving the indicator correction when \(E_4=0\). If a vertex is unsaturated, (4) forces excess at least two, and a zero-excess companion has U-degree nine, giving \(|S_4|\le9\), within (5).
- For \(K_5\), a common label is forbidden because \(K_5\) joined to a U-part of size at least seven contains \(K_{12}\). Every common neighbour uses an extra edge. If a W-vertex is unsaturated, (4) forces its excess to be three; the other four vertices then have U-degree eight and give the same cap.
- Every \(K_6\)-vertex is saturated because its U-degree is at most ten. No five vertices of \(K_6\) can share a small label, and no four can share label \(D\), or a \(K_{12}\) would result. Each common neighbour therefore uses at least two extra edges. Total load is at most \(E_6\), proving the last bound.

Summing (5),
\[
\sum_i|S_i|
\le25-\left\lceil E_6/2\right\rceil
+\mathbf1_{E_3=0}+\mathbf1_{E_4=0}
\le27<29,
\]
contradicting (2).

## 5. Case \(\epsilon_U=2\): \(K_3\dot\cup K_5^3\) or \(K_4^3\dot\cup K_6\)

Now \(E_W=2\).

### 5.1. \(K_3\dot\cup K_5^3\)

Here \(m=3\), so (4) gives threshold ten. The triangle component satisfies
\[
|S_3|\le9+E_3+\mathbf1_{E_3=0}.
\]
For a saturated \(K_5\) component, a common label is forbidden and each common neighbour uses at least one extra edge, giving \(|S_5|\le5+E_5\). An unsaturated \(K_5\)-vertex would need excess at least two by (4). Then that component has \(E_5=2\), its other four vertices have U-degree eight, and \(|S_5|\le8\); the other two \(K_5\)'s have zero excess and capacity at most five each, while \(E_3=0\) gives \(|S_3|\le10\). The total is at most \(10+8+5+5=28\). If all \(K_5\)'s are saturated, the sum is at most
\[
24+E_W+\mathbf1_{E_3=0}\le27.
\]
Both alternatives contradict (2).

### 5.2. \(K_4^3\dot\cup K_6\)

Here \(m=4\), so the threshold is eleven. Every \(K_6\)-vertex is saturated and the \(K_{12}\) restriction gives \(|S_6|\le\lfloor E_6/2\rfloor\le1\). Each \(K_4\) has \(|S_4|\le9\): an unsaturated vertex would need excess two, leaving a zero-excess companion of U-degree nine; if all are saturated, the total label load is at most \(8+E_4\le10\). A common label \(D\) is forbidden; a common small label yields at most \(7+\lfloor10/4\rfloor=9\); mixed labels with multiplicity at most two yield at most five common neighbours, while a 3+1 label split has at most four common neighbours in the three-label part and total load \(x+3y\le10\), hence \(x+y\le6\). Thus
\[
\sum_i|S_i|\le3\cdot9+1=28<29,
\]
contradicting (2).

## 6. Case \(\epsilon_U=3\): \(K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5\)

Here \(E_W=1\), \(m=4\), and (4) gives threshold ten. Each \(K_4\) has \(|S_4|\le9\): if an unsaturated vertex exists, it has excess one and its three zero-excess companions have U-degree nine; otherwise total label load is at most \(8+E_4\le9\), with a common small label giving at most \(7+\lfloor9/4\rfloor=9\), and a common \(D\)-label forbidden by \(K_{12}\).

All \(K_5\)-vertices are saturated because their U-degree is at most nine. For a \(K_5\) with component excess \(E_5\le1\), a common label is forbidden. If no label occurs four times, each common neighbour uses at least two extra edges, giving \(|S_5|\le\lfloor(5+E_5)/2\rfloor\le2+E_5\). If four vertices have a common small label, the fifth vertex's load bounds the common neighbours inside that part by \(1+E_5\); outside that part, a zero-excess among the four forces at most one additional common neighbour. Thus again \(|S_5|\le2+E_5\).

Consequently
\[
\sum_i|S_i|\le9+9+(2+E_{5,1})+(2+E_{5,2})
\le22+E_W=23<29,
\]
contradicting (2).

## 7. Conclusion and scope firewall

All four no-cross-edge W profiles at \(\delta=13\), \(\epsilon_U\in\{1,2,3\}\), are excluded under the stated four-partite-U and core/witness contracts.

This does **not** exclude:
- \(\delta=13,\epsilon_U=0\);
- \(\delta=13\) with W-cross-edges;
- non-four-partite \(L=\overline{H[U]}\);
- any \(\delta\le12\);
- the five shell templates A–E in their entirety;
- the upstream \(K_{145}\)-to-T61 reduction.

The original E407 Q32 and EG617(r=12) targets remain **OPEN / NOT_CERTIFIED**.
