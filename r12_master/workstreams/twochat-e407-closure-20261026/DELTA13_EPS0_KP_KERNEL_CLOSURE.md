# E407 Q32 — close delta=13, epsilon_U=0, four-partite-U branch

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL on the frozen core/support contract and the registered Brouwer/Kang–Pikhurko equality theorem. This closes the delta=13, epsilon_U=0, four-partite-U branch; E407 Q32 overall remains OPEN.**

## 1. Starting reduction

`DELTA13_EPS0_KP_KERNEL_REDUCTION.md` reduces this branch to five explicit W-kernels. Write

\[
U=P_1\dot\cup P_2\dot\cup P_3\dot\cup D,
\qquad |P_1|=|P_2|=|P_3|=7,\quad |D|=8.
\]

Each part is a clique in H[U]. The only H[U] edges between different parts are exactly eight D-to-small edges, and every small-part vertex has cross-degree at most one.

Since epsilon_U=0, every u in U has d_H(u)=12.

For w in W let

\[
d_U(w)=d_H(w,U),\qquad y_w=d_U(w)-7.
\]

The support-block transversal theorem gives d_U(w)>=7 for every w. If w,w' are nonadjacent in H, it also gives

\[
|N_U(w)\cap N_U(w')|\le y_w+y_{w'}.
\tag{1.1}
\]

Finally

\[
\sum_{w\in W}\epsilon_w=4.
\tag{1.2}
\]

## 2. Improved U-part saturation threshold

### Lemma 2.1 — every U point has a W neighbour

Every u in U has d_H(u,W)>=1.

**Proof.** The frozen feasible-profile theorem gives alpha(H[W])=4. If u were anticomplete to W, an independent 4-set in H[W] together with u would be an independent 5-set in H, contradicting alpha(H)<=4. QED.

For d in D, let tau_d be its number of H[U] cross-neighbours in the three small parts. Then

\[
d_H(d,U)=7+\tau_d,
\qquad d_H(d,W)=12-(7+\tau_d)=5-\tau_d.
\]

Lemma 2.1 implies

\[
\boxed{\tau_d\le4\quad(d\in D).}
\tag{2.1}
\]

### Lemma 2.2 — unsaturated W vertices have U-degree at least ten

If w is not complete to any one of the four U-parts, then

\[
\boxed{d_U(w)\ge10.}
\tag{2.2}
\]

**Proof.** Let A_i be the nonempty set of non-neighbours of w in P_i, i=1,2,3, and let D' be its nonempty set of non-neighbours in D.

Fix d in D'. If each A_i contained a vertex nonadjacent to d, choosing one such vertex from each small part would give, together with w,d, an independent 5-set: different small parts are H-anticomplete, and all five required incidences were chosen missing. Hence for every d in D', at least one A_i is contained in N_H(d). By (2.1), that A_i has size at most four.

Two distinct d,d' in D' cannot use the same A_i, because A_i is nonempty and every small-part vertex has D-cross-degree at most one. Thus |D'|<=3 and distinct D' vertices force distinct small parts.

If |D'|=1, the number of U-nonneighbours of w is at most

\[
4+7+7+1=19,
\]
so d_U(w)>=10.

If |D'|=2, it is at most

\[
4+4+7+2=17,
\]
so d_U(w)>=12.

If |D'|=3, it is at most

\[
4+4+4+3=15,
\]
so d_U(w)>=14.

This proves (2.2). QED.

## 3. Low W vertices carry a four-label clique colouring

Call w **low** if d_U(w)<=9 and **high** otherwise.

By Lemma 2.2, every low vertex is complete to a U-part. Since d_U(w)<=9, it cannot be complete to two parts, because the two smallest parts already have 7+7=14 vertices. Thus every low vertex has a unique label

\[
\lambda(w)\in\{P_1,P_2,P_3,D\}.
\]

### Lemma 3.1 — equal labels force a W-edge

If low vertices w,w' have the same label, then ww' is an H-edge.

**Proof.** Their common U-neighbourhood contains the whole labelled part and therefore has size at least seven. If ww' were a nonedge, (1.1) would give

\[
7\le |N_U(w)\cap N_U(w')|
\le y_w+y_{w'}\le2+2=4,
\]
contradiction. QED.

Hence each label class is a clique in H[W]. Joining it to its U-part gives a clique in H. Since omega(H)<=11,

\[
\boxed{|\lambda^{-1}(P_i)|\le4\quad(i=1,2,3),
\qquad |\lambda^{-1}(D)|\le3.}
\tag{3.1}
\]

Thus at most

\[
4+4+4+3=15
\]

W vertices are low. Consequently

\[
\boxed{|W_{\rm high}|\ge3.}
\tag{3.2}
\]

Equivalently, if J=bar(H[W]), the low vertices admit a proper four-colouring whose colour-class capacities are 4,4,4,3.

## 4. Excess cost of a high vertex

For w in W,

\[
d_U(w)=12+\epsilon_w-d_{H[W]}(w).
\]

If w is high, d_U(w)>=10, so

\[
\boxed{\epsilon_w\ge d_{H[W]}(w)-2.}
\tag{4.1}
\]

The total available excess is only four by (1.2). We now show that none of the five KP kernels can contain enough high vertices while leaving a capacity-4,4,4,3 colouring on the low vertices.

## 5. Exclude Family I: base (3,4,5,5)

For either a=1 or a=2 the H[W] degree multiset is

\[
3^3,4^{14},5^1.
\]

The three degree-3 vertices are exactly the base part N_1 of size three. By (4.1), the high-vertex costs are respectively 1,2,3 for target W-degrees 3,4,5.

Since at least three vertices must be high and total cost is at most four, there are only two possibilities:

1. all three vertices of N_1 are high;
2. exactly two vertices of N_1 and one degree-4 vertex are high.

### Case 1: all N_1 high

The two base K5 parts N_3,N_4 are completely low. In J the two parts are complete to each other. Each has five vertices, so by the colour-class capacity at most four it needs at least two labels. Their label sets must be disjoint. Hence N_3 and N_4 already consume all four labels. But N_2 contains low vertices and is J-complete to both N_3 and N_4, so none of the four labels is available. Contradiction.

### Case 2: two N_1 high and one degree-4 vertex high

If the degree-4 high vertex is outside N_3 union N_4, then both K5 parts are completely low and the previous contradiction applies.

Suppose it lies in N_3; the N_4 case is symmetric. Then low N_3 has four vertices and needs at least one label; low N_4 has five vertices and needs at least two. Because J is complete between N_3 and N_4, these label sets are disjoint, using at least three labels.

One vertex u of N_1 remains low, and all four vertices of N_2 remain low. The graph J[{u} union N_2] contains an edge: if u lies in the KP set A_0, it is adjacent to every N_2 vertex except y; if u is outside A_0, it is adjacent to all of N_2. Thus these five low vertices require at least two further labels. They are J-complete to N_3 union N_4, so these labels must be new. At least five labels are required. Contradiction.

Therefore both Family-I kernels are impossible.

## 6. Exclude Family II: base (4,4,4,5)

For a=1,2,3 the only degree-3 vertices are the four vertices of base part N_3. Every other high vertex costs at least two excess units. The degree multisets are

\[
3^4,4^{13},6^1;\quad
3^4,4^{12},5^2;\quad
3^4,4^{13},6^1.
\]

Using (3.2), (4.1), and total excess four, the high set has one of only the following forms:

1. three vertices of N_3;
2. all four vertices of N_3;
3. exactly two vertices of N_3 plus one degree-4 vertex.

No degree-5 or degree-6 vertex can appear in a three-vertex high set within budget four.

The KP graph J has:

- complete cross-edges between N_3 or N_4 and each other base part;
- J[N_1,N_2]=K_{4,4} minus the star yA_0;
- x adjacent in J to every vertex of N_3 union N_4, to A_0 subset N_1, and to y in N_2.

Because A_0 is nonempty and proper, J[N_1,N_2] is connected bipartite. Therefore any proper two-colouring of it has exactly the bipartition N_1,N_2, up to swapping colours.

### Case 1: three N_3 vertices high

One low N_3 vertex remains. Its label cannot be used by any low vertex of N_1,N_2,N_4, or by x, because J is complete from N_3 to all those sets. The low K5 part N_4 requires at least two additional labels. The graph on N_1 union N_2 requires at least two further labels. Thus at least five labels are required. Contradiction.

### Case 2: all four N_3 vertices high

The K5 part N_4 requires at least two labels. N_1 union N_2 requires at least two labels, and these label sets are disjoint because J is complete between N_4 and N_1 union N_2. Hence all four labels are consumed, with exactly two labels on N_1 union N_2.

By connectedness, those two colour classes are exactly N_1 and N_2. But x is J-adjacent to every N_4 vertex, to the nonempty set A_0 subset N_1, and to y in N_2. Thus x can use neither N_4 label nor either N_1/N_2 label. A fifth label is necessary. Contradiction.

### Case 3: two N_3 vertices and one degree-4 vertex high

Two low N_3 vertices remain and require a label unavailable anywhere outside N_3.

If the degree-4 high vertex is not in N_4, then all five N_4 vertices are low and require at least two further labels. The remaining low vertices of N_1 union N_2 still contain a cross-edge and require at least two labels, all disjoint from the N_3/N_4 labels. At least five labels are required.

If the degree-4 high vertex lies in N_4, then low N_4 has four vertices and can use one label. Together with the dedicated N_3 label, two labels remain for the full connected graph J[N_1,N_2], forcing its unique bipartition colouring. The vertex x remains low and is adjacent in J to N_3, N_4, A_0 and y, so it cannot use any of the four labels. Contradiction.

This excludes all three Family-II kernels.

## 7. Conclusion

All five Kang–Pikhurko equality kernels from `DELTA13_EPS0_KP_KERNEL_REDUCTION.md` are impossible. Hence

\[
\boxed{\delta=13,\ \epsilon_U=0,\ L_U\text{ four-partite is EXCLUDED}.}
\]

Combining this with the previously registered epsilon_U=1,2,3 closures, the entire

\[
\boxed{\delta=13,\ L_U\text{ four-partite branch is excluded}.}
\]

under the frozen core/support contract and the registered Brouwer/Kang–Pikhurko theorem.

This result does **not** exclude the delta=13 non-four-partite L_U branch, any delta<=12 branch, the conditional delta=14 saturated dependency, or the five shell templates globally. E407 Q32 therefore remains OPEN / NOT_CERTIFIED.

## 8. Independent finite replay

`verify_delta13_eps0_kp_closure.py` independently enumerates:

- the five KP target kernels;
- every possible high set whose minimum excess cost is at most four;
- every proper four-colouring of the remaining low graph with capacities 4,4,4,3.

It finds no feasible state. This verifier checks the finite case split only; the saturation and common-neighbour lemmas above are analytic.