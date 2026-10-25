# E407 Q32: additional \(\delta=14\) four-partite W-profile exclusions for \(\epsilon_U=1,2\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract and W-profile classification.

This note excludes four W-profiles that have no cross-edges between their clique components:
1. \(\epsilon_U=1,\ H[W]=K_3\cup K_5^3\);
2. \(\epsilon_U=2,\ H[W]=K_3\cup K_5^3\);
3. \(\epsilon_U=1,\ H[W]=K_4^3\cup K_6\);
4. \(\epsilon_U=2,\ H[W]=K_4\cup K_4\cup K_5\cup K_5\).

## 1. Shared contract and reverse-saturation threshold

Assume the \(\delta=14\) four-partite U-complement boundary:
\[
|U|=29,\quad |W|=18,\quad
e(H[U])=98,\quad \alpha(H)\le4,\quad\omega(H)\le11,
\]
with U-parts \(A,B,C,D\) of sizes \(7,7,7,8\), seven H[U] cross-edges between \(A\cup B\cup C\) and \(D\), and distinct small-side endpoints. Let \(\epsilon_U\in\{1,2\}\), and let
\[
\epsilon_v=d_H(v)-12\ge0,\qquad
\sum_{u\in U}\epsilon_u=\epsilon_U,\qquad
\sum_{w\in W}\epsilon_w=4-\epsilon_U=:E_W.
\]
Every profile treated below has four anticomplete clique components in \(H[W]\). Thus every U-vertex is complete to a whole W-component: otherwise one non-neighbour from each component gives an independent five-set.

If a W-vertex \(w\) is not complete to any U-part, let \(D'\) and \(A',B',C'\) be its non-neighbour sets. For every \(d\in D'\), every triple in \(A'\times B'\times C'\) must contain a cross-edge to \(d\); hence one of the three small non-neighbour sets is contained in \(N_H(d)\), and has size at most \(t_d\). Distinct \(d\)'s require distinct small parts because every small-side vertex has at most one cross-edge.

Let \(m\) be the smallest W-component size. Since each \(d\in D\) is complete to a W-component,
\[
d_H(d,W)=5+\epsilon_d-t_d\ge m,\qquad
t_d\le5+\epsilon_d-m\le5+\epsilon_U-m.
\]
If \(|D'|=1\), then \(d_H(w,U)\ge14-t_d\ge9+m-\epsilon_U\). The cases \(|D'|\ge2\) give a stronger lower bound by counting the distinct small non-neighbour sets. Therefore
\[
\boxed{w\text{ not complete to any U-part}\Longrightarrow
d_H(w,U)\ge9+m-\epsilon_U.} \tag{1}
\]
For \(m=3\), the threshold is \(12-\epsilon_U\); for \(m=4\), it is \(13-\epsilon_U\).

For each W-component \(C_s\cong K_s\), define \(S_s=\{u\in U:u\text{ is adjacent to all of }C_s\}\). Because the W-components are anticomplete,
\[
29=|U|\le\sum_s|S_s|. \tag{2}
\]

## 2. A \(K_3\) component capacity bound

For \(T\cong K_3\), write \(E_T=\sum_{w\in T}\epsilon_w\). Its vertices have U-degrees \(10+\epsilon_w\). Using U-part labels and extra-edge loads, if all three vertices are part-saturated and not all labels agree, then \(|S_T|\le9+E_T\). If all labels agree to a small part or to \(D\), the full-label bounds are respectively
\[
7+\left\lfloor\frac{9+E_T}{3}\right\rfloor,\qquad
8+\left\lfloor\frac{6+E_T}{3}\right\rfloor.
\]
If a vertex is not part-saturated, (1) bounds its excess from below. A zero/low-excess companion then bounds \(|S_T|\). For both \(\epsilon_U=1\) and \(2\), these cases give
\[
\boxed{|S_T|\le9+E_T+\mathbf1_{\{E_T=0\}}.} \tag{3}
\]

## 3. \(H[W]=K_3\cup K_5^3\), for \(\epsilon_U=1\) or \(2\)

For a saturated \(K_5\)-component, no five vertices can share one U-part label, because \(K_5\) joined to a U-part of size at least seven contains a forbidden \(K_{12}\). Its total extra-edge load is at most \(5+E_i\), so
\[
|S_{5,i}|\le5+E_i.
\]
If a K5 vertex is not part-saturated, (1) implies
\[
\epsilon_w\ge(12-\epsilon_U)-8=4-\epsilon_U.
\]
For \(\epsilon_U=1\), this can happen only when \(E_i=3\); the other four vertices then have excess zero and U-degree eight, giving \(|S_{5,i}|\le8=5+E_i\). For \(\epsilon_U=2\), it can happen only when \(E_i=2\); again the other four vertices have U-degree eight, so \(|S_{5,i}|\le8\). In this exceptional \(\epsilon_U=2\) case, \(E_T=0\) and the other two K5 components have zero excess. Thus the total cover is at most
\[
|S_T|+|S_{5,1}|+|S_{5,2}|+|S_{5,3}|
\le 10+8+5+5=28.
\]
If there is no unsaturated K5 vertex, (3) gives
\[
\sum_s|S_s|\le24+E_W+\mathbf1_{\{E_T=0\}}
=28-\epsilon_U+\mathbf1_{\{E_T=0\}}\le28.
\]
An unsaturated T-vertex is already covered by (3). In every case this contradicts (2). Therefore both \(\epsilon_U=1\) and \(\epsilon_U=2\) profiles \(K_3\cup K_5^3\) are excluded.

## 4. \(H[W]=K_4^3\cup K_6\), for \(\epsilon_U=1\)

Here \(E_W=3\) and \(m=4\), so (1) gives the reverse-saturation threshold \(d_H(w,U)\ge12\). Every \(K_6\)-vertex has U-degree \(7+\epsilon_w\le10\), so all six are part-saturated. No five can share a small-part label and no four can share the D label, or a \(K_{12}\) would result. Thus each \(u\in S_6\) needs at least two extra edges from the six labelled vertices. The total load of \(K_6\) is at most \(E_6\), whence
\[
|S_6|\le\lfloor E_6/2\rfloor\le1.
\]

Each \(K_4\)-component satisfies \(|S_4|\le9\). If one vertex is not part-saturated, (1) forces its excess to be at least three; the other three vertices then have excess zero and U-degree nine, giving the bound. Otherwise label all four vertices. Their total extra-edge load is at most \(8+E_4\le11\). If all labels are one small part, the common set has at most \(7+\lfloor11/4\rfloor=9\) vertices; all labels D would create a forbidden \(K_{12}\). If the labels are not all equal, a label multiplicity of three allows at most eight vertices in its part plus at most one outside (the outside vertices cost at least three load units each); multiplicity at most two allows at most \(\lfloor11/2\rfloor=5\). Hence each of the three K4 common-neighbour sets has size at most nine.

Consequently
\[
\sum_s|S_s|\le3\cdot9+\lfloor E_6/2\rfloor\le28<29,
\]
contradiction. This profile is excluded.

## 5. \(H[W]=K_4\cup K_4\cup K_5\cup K_5\), for \(\epsilon_U=2\)

Now \(E_W=2\), \(m=4\), and (1) gives \(d_H(w,U)\ge11\) for every W-vertex not complete to a U-part. Every K5 vertex has U-degree \(8+\epsilon_w\le10\), so all K5 vertices are part-saturated.

For a saturated \(K_5\)-component with excess \(E_i\le2\), choose U-part labels. A full common label is forbidden by \(\omega(H)\le11\). If no label occurs four times, every \(u\in S_5\) uses at least two extra edges, giving
\[
|S_5|\le\left\lfloor\frac{5+E_i}{2}\right\rfloor\le2+E_i.
\]
If four vertices have label \(P\) and one has another label, then \(S_5\cap P\) has size at most the extra-edge load of the single differently labelled vertex, at most \(1+E_i\). Any common neighbour outside \(P\) uses an extra edge at each of the four P-labelled vertices; at least one of those vertices has zero excess, so there is at most one such common neighbour. Hence again \(|S_5|\le2+E_i\).

Each K4 component has \(|S_4|\le9\). An unsaturated vertex would need excess at least two; since \(E_W=2\), a zero-excess companion of U-degree nine bounds the common set. If all are saturated, the total label load is at most \(8+E_4\le10\): a full label to a small part gives at most \(7+\lfloor10/4\rfloor=9\), a full D label is forbidden, and the non-full-label cases are bounded by nine by the same multiplicity argument as in Section 4.

It follows that
\[
\sum_s|S_s|\le 9+9+(2+E_5)+(2+E'_5)
\le22+E_W=24<29,
\]
contradiction. This profile is excluded.

## 6. Scope

These arguments exclude four additional four-partite W-profiles at \(\delta=14\): \(K_3\cup K_5^3\) for \(\epsilon_U=1,2\), \(K_4^3\cup K_6\) for \(\epsilon_U=1\), and \(K_4\cup K_4\cup K_5\cup K_5\) for \(\epsilon_U=2\). The \(\epsilon_U=1\), \((4,4,5,5)\)-plus-one-cross-edge profile remains OPEN, as do \(\delta=14\) non-four-partite cases and all \(\delta\le13\). E407 Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
