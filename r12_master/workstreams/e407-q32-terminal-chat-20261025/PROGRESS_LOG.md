# E407 Q32 terminal — progress log

## 2026-10-25 — Round 1

### New mathematical result

**Proved conditionally:** the delta=16 minimum-support boundary is automatically four-partite and reduces to one labelled core kernel.

The proof uses the 49 linear K4 witnesses, the exact core ledger, Brouwer's second-Turan bound, equality in Turan on 18 vertices, and the total degree-excess budget. It excludes endpoint splits (4,1) and (3,2) for the five cross edges in H[U].

The sole surviving endpoint allocation is (5,0): all five distinct D-endpoints have the same K4 as their exact W-neighbourhood, and that K4 is complete to D. Each vertex in the other three W-components must be complete to a 7-part; labels may vary within a component, and no component-wide bijection is proved.

### Verification

Ran the local arithmetic/kernel audit script. Output: E407_DELTA16_STRUCTURAL_KERNEL_ARITHMETIC_OK.

The script checks exact edge ledgers, integer partition profiles, and finite excess inequalities. It does not verify graph realization, all graph-theoretic lemmas, or the original K145 theorem.

A reverse-saturation lemma was also proved: every vertex of W is complete to exactly one U-part. The proof handles the exceptional possibility of a 13-neighbour W-vertex and excludes it by the four-endpoint K4 degree contradiction.

### Global effect

- New closed contracts: 1 structural reduction (delta=16 boundary).
- Fully excluded E407 templates: 0.
- Remaining E407 minimum-support branches: delta<=15 (four-partite and non-four-partite), plus the surviving delta=16 kernel.
- E408 Q32/Q33: untouched.
- Original T61-to-K145 bridge: still OPEN / NOT_CERTIFIED.

### Next attack

Combine the forced vertex-level U-part neighbourhoods and common-K4 endpoint structure with the exact row/hub requirements of templates A-E. In parallel, use the near-Turan classification for delta=14,15 to bound the remaining cross edges in H[W]. Do not claim any template closed until an actual incompatibility proof is obtained.


## 2026-10-25 — Round 2 (corrected): audit of the \(\delta=16\) endpoint split

### Correction

An attempted closure of the \((5,0)\) endpoint split was invalid and is withdrawn. The error was assuming that the three non-endpoint vertices of \(D\), each having five neighbours in \(W\), must be complete to a \(K_5\). In the \((5,0)\) split, the endpoint \(K_4\) is complete to all of \(D\), so each non-endpoint \(D\)-vertex already has four neighbours in that \(K_4\) and has **exactly one** additional \(W\)-neighbour. That extra neighbour need not make it complete to a \(K_5\). The proposed pigeonhole/excess contradiction therefore does not follow.

### Results that remain valid

- The \(\delta=16\) boundary is forced four-partite, with \(U\)-parts \(7,7,7,8\) and \(H[W]=K_5\cup K_5\cup K_4\cup K_4\).
- The five cross edges in \(H[U]\) form a matching.
- Every \(W\)-vertex is complete to exactly one \(U\)-part.
- The \((4,1)\) and \((3,2)\) endpoint splits are excluded by degree-excess contradictions.
- In the remaining \((5,0)\) split, the endpoint \(K_4\) is complete to \(D\); each vertex in the other \(K_4,K_5,K_5\) components is complete to a small part; each of the three non-endpoint \(D\)-vertices has exactly one additional \(W\)-neighbour outside the endpoint \(K_4\).

### Current status and next attack

- E407 Q32: **OPEN / NOT_CERTIFIED**.
- \(\delta=16\): OPEN, narrowed to the labelled \((5,0)\) kernel.
- \(\delta\le15\): four-partite near-extremal and non-four-partite cases remain open.
- E408 Q32/Q33 and the original \(K_{145}\)-to-T61 bridge: untouched.

Next, characterize the three extra \(D\)-to-\(W\) edges and the full-part labels of the 14 vertices outside the endpoint \(K_4\), then intersect this incidence system with the five V12 shell templates. Do not claim \(\delta=16\) closed until the \((5,0)\) kernel is excluded or realized.


## 2026-10-25 — Round 3: exact witness-array multiplicities

### New proved identity

Under the \(\delta=16\) four-partite boundary, the 49 witness blocks and seven exact-129 color classes induce a resolvable Latin-square incidence system:

- every \(A\)-\(B\), \(A\)-\(C\), and \(B\)-\(C\) pair occurs in exactly one block;
- each color class is a transversal of the resulting order-7 Latin square;
- each color class uses seven distinct \(D\)-vertices and omits exactly one of the eight;
- for every \(d\in D\), the number \(r_d\) of colors omitting \(d\) equals the number of missing witness partners of \(d\) in each of \(A,B,C\).

Thus \(\sum_{d\in D}r_d=7\). The five actual \(H[U]\) cross edges are five matching pairs among these missing pairs, so each of the five endpoint labels has \(r_d\ge1\). Therefore endpoint labels use at least five omission units, leaving at most two for the three non-endpoint labels. At least three endpoint labels have \(r_d=1\), and at least one non-endpoint \(D\)-vertex has \(r_d=0\) and appears in every color class.

The full statement and proof are in DELTA16_WITNESS_ARRAY.md.

### Why this matters

This converts the 49-witness count into a precise incidence/omission identity. It does not by itself exclude the surviving \((5,0)\) \(W\)-kernel or any of templates A–E. The next step is to combine the omission multiplicities with the template-specific shell-row/hub-hit requirements rather than use only scalar incidence totals.

### Current status

- \(\delta=16\): OPEN, narrowed to the labelled \((5,0)\) kernel plus the exact witness-array constraints.
- \(\delta\le15\): OPEN.
- E407 Q32 overall: OPEN / NOT_CERTIFIED.


## 2026-10-25 — Round 4: \(\delta=15\) non-four-partite branch reduced

### New proved result

At \(\delta=15\), a non-four-partite \(K_5\)-free graph \(L\) on 29 vertices has 309 edges, exactly the Brouwer second-Turán maximum. Applying the Kang–Pikhurko equality classification, \(L\) has a 28-vertex complete four-partite base plus an exceptional vertex \(x\), with base part profile one of
\[
(7,7,7,7),\quad(6,7,7,8),\quad(6,6,8,8).
\]

Using the 49 pairwise edge-disjoint witness \(K_4\)'s:
- Let \(A\) be the proper nonempty subset in the Kang–Pikhurko construction, \(a=|A|\), and \(t\) the number of witness blocks containing \(x\).
- \(P_1P_2\)-edge capacity gives \(t\ge49-n_1n_2+a\).
- The exceptional vertex has degree \(n_3+n_4+a+1\), and each \(x\)-block uses three distinct \(x\)-edges, so \(3t\le n_3+n_4+a+1\).

These two inequalities eliminate the base profiles \((6,7,7,8)\) and \((6,6,8,8)\). Thus only the balanced base profile \((7,7,7,7)\) can survive.

For that profile:
- \(a\le t\le\lfloor(15+a)/3\rfloor\);
- \(t_A,t_y\) (the two possible types of \(x\)-block) must be \((a,0)\), \((a-1,1)\), or \((a,1)\);
- every one of the 49 \(P_3P_4\) pairs is used by exactly one witness block;
- the 15-edge leave has exact pair-type counts, and every vertex in \(P_3\cup P_4\) has leave-degree exactly one.

The full proof and exact leave ledger are in DELTA15_SECOND_TURAN_PACKING.md. The equality classification is cited there to Kang–Pikhurko (2005).

### Effect and limits

This is a genuine reduction of the \(\delta=15\) non-four-partite branch, not its elimination. The balanced equality construction and its exact 15-edge leave remain compatible at the current counting level; the shell-row/hub constraints must still be applied.

Current status:
- \(\delta=16\): OPEN, narrowed to the \((5,0)\) endpoint kernel.
- \(\delta=15\) non-four-partite: only the balanced Kang–Pikhurko base profile remains; OPEN.
- \(\delta=15\) four-partite, \(\delta=14\), and \(\delta\le13\): OPEN.
- E407 Q32 overall: OPEN / NOT_CERTIFIED.


### Round 4 addendum — core-degree restriction on the KP exceptional vertex

Using \(d_{H[U]}(x)=13-a\), the core minimum degree, and the already classified \(H[W]\) profiles, the exceptional vertex has
\[
d_H(x,W)=a-1+\epsilon_x.
\]
The independence-number constraint forces it to be complete to a whole \(W\)-clique component. In the one-cross-edge \(K_4,K_4,K_5,K_5\) profile, degree at most five still forces a whole component because avoiding an independent transversal without completing a component would require at least six neighbours.

This reduces the Kang–Pikhurko subset size from \(a=1,\ldots,6\) to **\(a\in\{4,5,6\}\)**:
- with \(\epsilon_U=0\), the \(K_3\cup K_5^3\) profile permits \(a\ge4\), while the profiles with minimum clique size four require \(a\ge5\);
- with \(\epsilon_U=1\), \(H[W]=K_4\cup K_4\cup K_5\cup K_5\), so \(a\ge4\), and \(a=4\) forces \(\epsilon_x=1\).

This is another necessary-condition reduction; the balanced \((7,7,7,7)\) equality profile remains OPEN.


## 2026-10-25 — Round 5: \(\delta=15\) non-four-partite branch excluded

### New terminal contradiction

The balanced Kang–Pikhurko profile left after Round 4 is now excluded by combining the exceptional vertices \(x,y\) with the independent-set constraint on \(H\).

For the balanced \((7,7,7,7)\) base and \(a=|A|\):
\[
d_{H[U]}(x)=13-a,\qquad d_{H[U]}(y)=6+a,
\]
so
\[
d_H(x,W)=a-1+\epsilon_x,\qquad d_H(y,W)=6-a+\epsilon_y,
\qquad \epsilon_x+\epsilon_y\le\epsilon_U\le1.
\]

The exact core ledger gives \(e(H[W])=33-\epsilon_U\). Since \(\alpha(H[W])\le4\), the complement on 18 vertices has 120 or 121 edges, above the non-four-partite second-Turán threshold 118. Hence \(\overline{H[W]}\) is four-partite, and the allowed \(H[W]\) profiles are:
- \(\epsilon_U=0\): \(K_3\cup K_5^3\), \(K_4^3\cup K_6\), or \(K_4\cup K_4\cup K_5\cup K_5\) plus one cross edge;
- \(\epsilon_U=1\): \(K_4\cup K_4\cup K_5\cup K_5\).

Every \(u\in U\) must be complete to a whole \(W\)-clique part when the parts are anticomplete. In the one-cross-edge profile, the same conclusion holds for \(u\) with at most five \(W\)-neighbours: otherwise it needs at least six neighbours to block all independent transversals.

- If \(\epsilon_U=0\), \(x\) requires \(a-1\) to be at least the smallest part size, while \(y\) requires \(6-a\) to be at least that same minimum. The three profiles respectively force \(a\ge4,a\le3\); \(a\ge5,a\le2\); and \(a\ge5,a\le2\). Each is impossible.
- If \(\epsilon_U=1\), all parts have size at least four, forcing \(a-1+\epsilon_x\ge4\) and \(6-a+\epsilon_y\ge4\). Thus \(a\ge4\) but \(a\le3\), contradiction.

Therefore the whole \(\delta=15\), \(L\) non-four-partite branch is **EXCLUDED**, under the retained 49-witness/core contract and the Kang–Pikhurko equality classification.

### Current frontier

- \(\delta=16\): OPEN, reduced to the labelled \((5,0)\) endpoint kernel.
- \(\delta=15\), \(L\) non-four-partite: **EXCLUDED**.
- \(\delta=15\), \(L\) four-partite: OPEN.
- \(\delta=14\) and lower: OPEN.
- E407 Q32 overall: OPEN / NOT_CERTIFIED; no complete \(K_{145}\) proof is claimed.


## 2026-10-25 — Round 6: \(\delta=16\) four-partite branch excluded

### New terminal contradiction

The \(\delta=16\) support-boundary case is now excluded under the retained E407 core/witness contract.

The reduction forces:
- \(L=\overline{H[U]}\) four-partite with parts \(7,7,7,8\);
- \(H[U]\) has 91 within-part edges and five cross edges, which form a matching;
- \(\epsilon_U=0\), \(H[W]=K_5\cup K_5\cup K_4\cup K_4\);
- each of the five \(D\)-endpoints has exactly one \(K_4\) as its \(W\)-neighbourhood.

The \((4,1)\) and \((3,2)\) endpoint splits contradict the total four-unit excess budget. For the remaining \((5,0)\) split, all five endpoints share one \(K_4=C_0\). Every \(w\in C_0\) is adjacent to the five endpoint vertices. If \(w\) were not complete to the 8-part \(D\), reverse saturation forces it to be complete to a 7-part, giving at least \(7+5=12\) \(U\)-neighbours and hence \(\epsilon_w\ge3\). At most one \(w\in C_0\) can be such an exception. But then at least two non-endpoint vertices of \(D\) would have only three neighbours in \(C_0\) and two outside; neither set of neighbours contains a whole \(W\)-component (all components have size at least four), contradicting \(\alpha(H)\le4\). Hence all four vertices of \(C_0\) are complete to \(D\), yielding a \(K_8\cup K_4\) joined completely across, i.e. a forbidden \(K_{12}\) in \(H\).

This closes the last endpoint split. The proof is in FOUR_PARTITE_TERMINAL.md; the arithmetic consistency checks are in verify_e407_delta16_kernel.py.

### Independent audit of the \(\delta=15\) non-four-partite exclusion

The previous round's \(x,y\) degree contradiction was rechecked. Under the Kang–Pikhurko equality classification, the two unbalanced base profiles fail the 49-block edge-capacity inequalities. In the balanced \((7,7,7,7)\) profile,
\[
d_H(x,W)=a-1+\epsilon_x,\qquad d_H(y,W)=6-a+\epsilon_y,\qquad \epsilon_x+\epsilon_y\le\epsilon_U\le1.
\]
The \(W\)-side Brouwer bound forces the stated four-clique-part profiles. Independence-number saturation requires each of \(x,y\) to be complete to a whole \(W\)-part; for the one-cross-edge profile the same follows for vertices with at most five \(W\)-neighbours. Each allowed profile then forces incompatible lower and upper bounds on \(a\). The exclusion remains conditional on the retained core/witness contract and the cited Kang–Pikhurko equality classification.

### Updated frontier

- \(\delta=16\), four-partite: **EXCLUDED**.
- \(\delta=15\), non-four-partite: **EXCLUDED** under the retained contract.
- \(\delta=15\), four-partite: OPEN.
- \(\delta\le14\): OPEN (both four-partite and non-four-partite cases where allowed).
- E407 Q32 overall: **OPEN / NOT_CERTIFIED**.
- E408 Q32/Q33 and the original \(K_{145}\)-to-T61 bridge: untouched.


## 2026-10-25 — Round 7: \(\delta=15\) four-partite W-profile reduction

### New result

The four-partite \(\delta=15\) boundary has six cross edges between the 8-part \(D\) and the three 7-parts; the six small-side endpoints are distinct. The core excess is \(\epsilon_U\in\{0,1\}\).

Using \(\alpha(H)\le4\), degree saturation, and \(\omega(H)\le11\), the following subcases are excluded:

- **\(\epsilon_U=1\)**, where \(H[W]=K_4\cup K_4\cup K_5\cup K_5\): at least five \(D\)-endpoints have exact \(K_4\) W-neighbourhoods, so one \(K_4\) receives at least three. If it is complete to \(D\), it yields \(K_{12}\); otherwise its four vertices each require positive W-excess, but the W-excess budget is only three.
- **\(\epsilon_U=0\), \(H[W]=K_4\cup K_4\cup K_5\cup K_5\) plus one cross edge**: six endpoints split across the two \(K_4\) parts force at least four excess units in each part, exceeding the total four.
- **\(\epsilon_U=0\), \(H[W]=K_4^3\cup K_6\)**: all nine \(D\)-vertices must be assigned to one of the three \(K_4\) parts by their full W-neighbourhood; the corresponding endpoint counts \(n_1+n_2+n_3=9\) force at least \(4\sum_i\max(0,n_i-2)\ge12\) excess units, again impossible.

Thus the only remaining \(\delta=15\) four-partite profile is \(H[W]=K_3\cup K_5^3\) with \(\epsilon_U=0\).

In that profile, the \(K_3\) component must be complete to \(D\). Otherwise its common D-neighbourhood has size at most four; at least four D vertices are then nonadjacent to it and must be complete to the three \(K_5\) parts. Two share a \(K_5\), forcing five positive excess units. Hence the residual contains an allowed \(K_{11}\), namely \(D\cup K_3\), which remains to be checked against the shell templates.

Full proof and exact ledger: DELTA15_FOUR_PARTITE_TERMINAL.md.

### Current frontier

- \(\delta=16\) four-partite: **EXCLUDED**.
- \(\delta=15\) non-four-partite: **EXCLUDED** under the retained contract and Kang–Pikhurko equality classification.
- \(\delta=15\) four-partite: reduced to \(H[W]=K_3\cup K_5^3\), with \(D\cup K_3=K_{11}\); **OPEN**.
- \(\delta\le14\): **OPEN**.
- E407 Q32 overall: **OPEN / NOT_CERTIFIED**.


### Round 7 proof audit addendum — degree-two \(D\)-endpoint exception

A careful audit found that the generic “no whole \(U\)-part implies at least 13 \(U\)-neighbours” lemma needs one exception when a \(D\)-vertex has cross-degree two: a \(W\)-vertex can have exactly 12 \(U\)-neighbours, missing that \(D\)-vertex and two matched vertices in one small part. The lemma in DELTA15_FOUR_PARTITE_TERMINAL.md has been corrected to state this exact exception.

The terminal reductions remain valid:
- In the \(\epsilon_U=1\) profile, the exception would consume all three \(W\)-excess units at a \(K_4\)-vertex; the other three vertices in its \(K_4\)-part are then adjacent to all seven remaining \(D\)-vertices and cannot meet their degree requirements.
- In the \(\epsilon_U=0\), \(K_3\cup K_5^3\) profile, any \(D\)-vertex with positive cross-degree is complete to the \(K_3\). This rules out the exceptional no-part pattern for a \(K_3\)-vertex; for a \(K_5\)-vertex it conflicts with the fact that the exceptional pattern is adjacent to all but one \(D\)-vertex while at least one other \(D\)-vertex has positive cross-degree.
- In the minimum-part-size-four profiles, every \(D\)-vertex has cross-degree at most one, so the exception cannot arise.

The \(\delta=15\) four-partite frontier remains exactly the one stated above: only \(H[W]=K_3\cup K_5^3\), with \(D\cup K_3\cong K_{11}\), remains open.


## 2026-10-25 — Round 8: \(\delta=15\) four-partite branch fully excluded

### Final contradiction

The last surviving \(\epsilon_U=0\), \(H[W]=K_3\cup K_5^3\) profile is now excluded. From the previous round, the \(K_3\) component \(C_0\) is complete to \(D\), and every vertex in the three \(K_5\) parts is complete to exactly one small \(U\)-part. Let \(k_P\) count the \(K_5\)-vertices labelled to small part \(P\in\{A,B,C\}\). Then
\[
k_A+k_B+k_C=15.
\]

If a small part has a cross-edge endpoint, that endpoint has exactly five \(W\)-neighbours, so \(k_P\le5\). If a part has no endpoint, its seven vertices all have \(W\)-degree six; \(k_P=6\) would make the same six labelled vertices the entire \(W\)-neighbourhood of every vertex in that part. The independent-set saturation condition then forces a whole \(K_5\) part inside those six vertices, making all five vertices of that \(K_5\) labelled to \(P\), which creates a forbidden \(K_{12}\). Therefore \(k_P\le5\) for all three small parts, and the sum forces \(k_A=k_B=k_C=5\).

There is at least one cross-edge endpoint \(u\), with \(u\in P\). It has exactly five \(W\)-neighbours, precisely the five vertices labelled \(P\). Its neighbourhood must contain a whole \(W\)-clique part; it cannot be the \(K_3\), whose vertices are labelled \(D\), so it must be one of the \(K_5\) parts. All five vertices of that \(K_5\) are then labelled \(P\), again giving \(P\cup K_5\cong K_{12}\), contradiction.

Thus the whole \(\delta=15\) four-partite branch is **EXCLUDED** under the retained core/witness contract. The full proof is in DELTA15_FOUR_PARTITE_TERMINAL.md.

### Updated frontier

- \(\delta=16\), four-partite: **EXCLUDED**.
- \(\delta=15\), non-four-partite: **EXCLUDED** under the retained contract and Kang–Pikhurko equality classification.
- \(\delta=15\), four-partite: **EXCLUDED** by the label-count/K12 contradiction.
- \(\delta\le14\): OPEN (four-partite and non-four-partite cases).
- E407 Q32 overall: **OPEN / NOT_CERTIFIED**.


## 2026-10-25 — Round 9: \(\delta=14,\epsilon_U=0\) cover-capacity contradiction

### New theorem

Under the 49-witness boundary, four-partite U-complement, \(\omega(H)\le11\), and the W-profile \(H[W]=K_3\dot\cup K_4\dot\cup K_5\dot\cup K_6\), define \(S_s\) as the U-vertices complete to the W-clique \(K_s\). Independence-number saturation requires the four sets to cover all 29 points of U.

A reverse-saturation lemma says every W vertex of U-degree at most 11 is complete to a whole U-part. The only possible non-saturated vertices in the \(K_3,K_4,K_5\) components consume at least 2,3,4 units of excess respectively; the common-neighbour set is bounded by a zero/low-excess companion. Label each saturated W vertex by a U-part and count its extra U-edges. The resulting bounds are
\[
|S_6|\le\lfloor E_6/2\rfloor,\quad
|S_5|\le5+E_5,\quad
|S_4|\le8+E_4+\mathbf1_{\{E_4=0\}},\quad
|S_3|\le9+E_3+\mathbf1_{\{E_3=0\}},
\]
where \(E_3+E_4+E_5+E_6=4\). Hence
\[
\sum_s|S_s|\le26-\lceil E_6/2\rceil
+\mathbf1_{\{E_3=0\}}+\mathbf1_{\{E_4=0\}}\le28,
\]
contradicting the required cover of 29 U-vertices.

The proof is in DELTA14_EPS0_K3K4K5K6_COVER_CAPACITY.md. The finite arithmetic replay is in verify_delta14_eps0_cover_capacity.py; all 35 excess profiles pass the bound, with maximum 28.

### Frontier change

Together with DELTA14_EPS0_K4_PROFILE_EXCLUSIONS.md, three of the four \(\delta=14,\epsilon_U=0\) W profiles are now excluded. The only remaining profile in that row is \(K_3\cup K_5^3\) plus one cross edge. The \(\epsilon_U=1,2\) rows, \(\delta=14\) non-four-partite branch, and \(\delta\le13\) remain open.

### Limits

This is conditional on the retained T61/core/witness contract and W-profile classification. It does not close a full shell template, E407 Q32, or EG617(r=12).


## 2026-10-25 — Round 10: final \(\delta=14,\epsilon_U=0\) four-partite profile excluded

### New theorem

The last W-profile \(K_3\cup K_5^3\) plus one cross-edge is now excluded under the retained 49-witness/core and four-partite contracts.

1. **Saturation geometry.** If a vertex misses every W clique component, its non-neighbour sets at the two endpoints of the unique W-cross-edge must be singleton endpoint sets. The maximum possible number of W-non-neighbours is 12 when the edge joins \(K_3\) to \(K_5\), and 10 when it joins two \(K_5\)'s. Since each \(D\)-vertex has at least 13 W-non-neighbours, all \(D\)-vertices are component-saturated, forcing \(t_d\le2\).
2. **Reverse saturation.** With \(t_d\le2\), a W-vertex not complete to any U-part has \(d_H(w,U)\ge12\), by counting non-neighbours in \(D,A,B,C\). Thus a non-endpoint K5 vertex can be unsaturated only when its excess is four; a K5 endpoint cannot be unsaturated.
3. **Exception elimination.** The only possible unsaturated U-vertex \(u\) lies at a non-endpoint small-part vertex when the W-cross-edge joins \(K_3\) to \(K_5\). It is anticomplete to the two other K5 components. Every \(v\in U\setminus N[u]\) nonadjacent to the K5 endpoint \(y\) must be complete to one of those two K5s, giving \(|S_2|+|S_3|\ge15-\epsilon_y\). Their capacity is at most \(10+E_2+E_3\le14-\epsilon_y\), contradiction.
4. **Cover capacity.** With all U-vertices saturated, the component capacities sum to at most 27 in either cross-edge placement, whereas the four common-neighbour sets must cover 29 vertices.

Added DELTA14_EPS0_K3K5K5K5_CROSS_EDGE_CLOSURE.md and verify_delta14_eps0_k3k5_cross_edge.py. Arithmetic replay passed: the exceptional-vertex lower bound exceeds its upper bound by one for every \(\epsilon_y\in\{0,\dots,4\}\), and all 35 nonnegative excess allocations give cover cap 27.

### Frontier update

- \(\delta=16\) four-partite: **EXCLUDED**.
- \(\delta=15\) four-partite and non-four-partite: **EXCLUDED** under the retained contracts.
- \(\delta=14,\epsilon_U=0\) four-partite: **EXCLUDED** (all four W profiles).
- Still open: \(\delta=14,\epsilon_U\in\{1,2\}\), \(\delta=14\) non-four-partite, and \(\delta\le13\).
- E407 Q32 overall and EG617(r=12): **OPEN / NOT_CERTIFIED**. The five shell templates A–E remain open.


## 2026-10-25 — Round 11: \(\delta=14,\epsilon_U=1\) no-cross-edge profile excluded

### New theorem

For the \(e(H[W])=33\) profile \(H[W]=K_3\dot\cup K_5^3\), the four clique components are pairwise anticomplete. Thus every \(u\in U\) must be complete to one component, or a non-neighbour from each component together with \(u\) forms an independent 5-set.

Because every \(d\in D\) is also complete to a W-component, \(d_H(d,W)=5-t_d+\epsilon_d\ge3\), so \(t_d\le2+\epsilon_d\le3\). The reverse-saturation lemma then gives \(d_H(w,U)\ge11\) for any W vertex not complete to a U-part. An unsaturated K5 vertex must have excess 3, leaving a zero-excess companion and proving \(|S_i|\le5+E_i\); saturated components obey the same bound by label/extra-edge counting. For \(C_0=K_3\), \(|S_0|\le10+\lfloor E_0/3\rfloor\). Since W-excess sums to three, the total common-neighbour cover is at most 28, contradicting \(|U|=29\).

Added DELTA14_EPS1_K3K5K5K5_NO_CROSS_EDGE.md and verify_delta14_eps1_k3k5_profile.py. Arithmetic replay passed for all 20 component-excess allocations.

### Frontier update

- \(\delta=14,\epsilon_U=0\), four-partite: **EXCLUDED** (all four W profiles).
- \(\delta=14,\epsilon_U=1\): \(K_3\cup K_5^3\) with no W-cross-edge **EXCLUDED**; other W profiles OPEN.
- \(\delta=14,\epsilon_U=2\): OPEN.
- \(\delta=14\), non-four-partite: OPEN.
- \(\delta\le13\): OPEN.
- Five E407 shell templates and EG617(r=12): **OPEN / NOT_CERTIFIED**.


## 2026-10-25 — Round 10: \(\delta=14,\epsilon_U=0\), cross-edge between two \(K_5\)'s excluded

### New theorem

For \(H[W]=K_3\cup K_5^3\) with the unique cross-edge joining two \(K_5\) components \(P,Q\), any \(u\in U\) has at most six W-neighbours. If it were not complete to any W-component, an independent transversal could be blocked only by choosing both endpoints of the cross-edge; this would force \(u\) to have at least \(4+4=8\) W-neighbours. Therefore the four component common-neighbour sets cover \(U\).

The reverse-saturation lemma and excess budget give
\[
|S_T|\le9+E_T+\mathbf1_{\{E_T=0\}},\quad
|S_P|\le4+E_P,\quad |S_Q|\le4+E_Q,\quad |S_R|\le5+E_R,
\]
where \(E_T+E_P+E_Q+E_R=4\). Hence the total cover capacity is at most 27, contradicting \(|U|=29\). Full proof: DELTA14_EPS0_K3K5X1_K5K5_EDGE.md.

Arithmetic replay: verify_delta14_k5_cross_edge_capacity.py checked all 35 integer excess profiles; the maximum bound is 27.

### Frontier

The only remaining \(\delta=14,\epsilon_U=0\), four-partite W-profile is \(K_3\cup K_5^3\) with the unique cross-edge joining \(K_3\) to a \(K_5\). That endpoint placement remains OPEN. The \(\epsilon_U=1,2\), non-four-partite, and \(\delta\le13\) cases remain open. E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## 2026-10-25 — Round 11: final \(\delta=14,\epsilon_U=0\) W-profile excluded

### New theorem

The remaining profile \(H[W]=K_3\cup K_5^3\) with its unique cross-edge joining \(K_3\) to a \(K_5\) is now excluded.

Let \(T=K_3\), with cross-edge endpoint \(a\in T\), and let \(D_0=N_D(T)\). If \(T\) is not complete to \(D\), all vertices of \(T\) must be complete to small U-parts: otherwise reverse saturation supplies a non-neighbour \(d\in D\) with \(t_d>0\), but every positive-\(t_d\) vertex is complete to \(T\). The exact degree budget forces \(|D_0|=4\), \((\epsilon_a,\epsilon_{t_1},\epsilon_{t_2})=(2,1,1)\), and each T-vertex's U-neighbourhood is \(D_0\) plus one entire small part. The resulting three label patterns bound the U-cover by at most 25.

If \(T\) is complete to \(D\), then \(D\subseteq S_T\), and
\[
|S_T|\le8+\lfloor(5+E_T)/3\rfloor,\qquad
|X|\le2+\lfloor E_T/2\rfloor,
\]
where \(X\) consists of U-vertices not complete to any W-component. The component-cover bound is \(27,27,26,25,25\) for \(E_T=0,1,2,3,4\). Only the equality-bound cases need further treatment; there, \(|X|\) maximal forces \(S_T=D\), lowering the total to at most 28. Thus all cases contradict the required 29-point cover.

Proof: DELTA14_EPS0_K3K5X1_K3K5_EDGE.md. Arithmetic replay: verify_delta14_k3_k5_cross_edge.py; all 35 excess allocations pass, corrected maximum 28.

### Frontier change

All four-partite W-profiles at \(\delta=14,\epsilon_U=0\) are now excluded. This is still conditional on the retained T61/core/49-witness contract and the stated near-Turán W-profile classification. Remaining: \(\delta=14,\epsilon_U=1,2\), \(\delta=14\) non-four-partite, and all \(\delta\le13\). E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## 2026-10-25 — Round 12: \(\delta=14,\epsilon_U=1\), no-cross-edge \(K_4^3\cup K_6\) excluded

### Exact external-incidence theorem

Every \(d\in D\) is complete to exactly one W-component, because \(H[W]\) has four pairwise anticomplete clique components and \(d\) cannot have eight W-neighbours. If a D-vertex is assigned to \(K_6\), it must have \(\epsilon_d=1,t_d=0\); hence at most one such vertex exists. Let \(q\in\{0,1\}\) count these vertices, and let \(R\) be the number of D-to-W incidences outside the component assigned to their D endpoint. Exact accounting gives
\[
R=1-2q+\sum_{d\in D}\epsilon_d.
\]
Thus \(R\le2\) if \(q=0\), and \(R=0\) if \(q=1\).

If a K4 component receives \(k\ge3\) D assignments, a vertex of that K4 complete to all of D uses \(8-k\) external incidences. Therefore at most \(0,0,0,1,2\) vertices can be D-complete when \(k=3,4,5,6,7\), respectively. The remaining vertices must be complete to a small U-part; reverse saturation rules out the unsaturated exception, and their required W-excess exceeds the available three units. A K4 cannot receive eight D assignments either, as that creates a K12. Hence each of the three K4 components receives at most two D vertices, impossible when seven or eight D vertices must be assigned among them.

Added DELTA14_EPS1_K4K4K4K6_NO_CROSS_EDGE.md and verify_delta14_eps1_k4k4k4k6.py. Arithmetic replay passed. The verifier's initial E_D branch typo was corrected and the corrected arithmetic was rerun successfully.

### Frontier update

- \(\delta=14,\epsilon_U=0\), four-partite: **EXCLUDED** (all four W profiles).
- \(\delta=14,\epsilon_U=1\): both no-cross-edge profiles \(K_3\cup K_5^3\) and \(K_4^3\cup K_6\) **EXCLUDED**; the \((4,4,5,5)\)+one-cross-edge profile remains open.
- \(\delta=14,\epsilon_U=2\): OPEN.
- \(\delta=14\), non-four-partite: OPEN.
- \(\delta\le13\): OPEN.
- Five E407 shell templates and EG617(r=12): **OPEN / NOT_CERTIFIED**.


## 2026-10-25 — Round 13: final \(\delta=14,\epsilon_U=1\) W-profile excluded

### New theorem

For \(H[W]\) with clique sizes \((4,4,5,5)\) and one cross-edge, every D vertex is complete to a unique W component. Let \(q_5\) count D vertices assigned to a K5. The exact incidence identity is \(R=1-q_5+E_D\le2\), where \(R\) counts D-W edges outside the assigned component. Since \(q_5\le1+E_D\le2\), at least six of the eight D vertices are assigned to the two K4s, so one K4 receives \(k\ge3\).

The \(R\le2\) bound forces at least \(4,4,4,3,2\) vertices in that K4 not to be complete to all of D when \(k=3,4,5,6,7\). Any such vertex must be complete to a small U-part; otherwise reverse saturation and the excess ledger produce a second zero-excess non-D-complete vertex of impossible degree. The resulting minimum W-excess demands are \(4,8,12,12,10\), all greater than the available three. The case \(k=8\) gives a forbidden \(K_{12}\).

Added DELTA14_EPS1_K4K4K5K5_ONE_CROSS_EDGE.md and its arithmetic verifier. The verifier's deliberately malformed K12 assertion was caught and replaced before replay; the corrected arithmetic passed.

### Exact profile classification

Added DELTA14_EPS1_W_PROFILE_CLASSIFICATION.md and verify_delta14_eps1_w_profiles.py. For \(G=\overline{H[W]}\), \(e(G)=120\), \(G\) is K5-free, and \(t_4(18)=121\). Brouwer's second-Turán bound puts every non-four-partite K5-free graph below or at 118 edges, so \(G\) must be four-partite. Exact partition arithmetic leaves only:
- \(K_3\cup K_5^3\), no cross-edge in \(H[W]\);
- \(K_4^3\cup K_6\), no cross-edge;
- \((4,4,5,5)\) clique components plus one cross-edge.

All three H[W] profiles are now excluded by the three independent terminal theorems. The sorted partition verifier passed.

### Frontier update

- \(\delta=14,\epsilon_U=0\), four-partite: **EXCLUDED** (all four W profiles).
- \(\delta=14,\epsilon_U=1\), four-partite: **EXCLUDED** (all three W profiles, with Brouwer dependency explicit).
- \(\delta=14,\epsilon_U=2\): OPEN.
- \(\delta=14\), non-four-partite: OPEN.
- \(\delta\le13\): OPEN.
- Five E407 shell templates and EG617(r=12): **OPEN / NOT_CERTIFIED**.
