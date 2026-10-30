# Source-complete minimum-degree audit for the 47-point class

Date: 2026-10-30  
Status: **PROVED**.

## 0. Exact theorem and scope

Define
\[
p_{12}(n)=12\binom q2+qr,\qquad n=12q+r,\quad0\le r<12,
\]
and
\[
D(n)=\binom n2-11p_{12}(n).
\]
The class \(\mathcal R(a,n)\) consists of simple n-vertex graphs J satisfying all three conditions:
\[
\alpha(J)\le a,\qquad \omega(J)\le11,\qquad
e(J[U])\le D(|U|)\quad\text{for every }U\subseteq V(J).
\]
The hereditary density caps are part of the theorem and are retained at every induced-subgraph step.

**Theorem (minimum-degree source gate).**
\[
\boxed{J\in\mathcal R(4,47),\ e(J)\le286
\ \Longrightarrow\ \delta(J)\ge12.}
\]
No V11 conclusion, Q32 theorem, 49-point theorem, or non-source-replayed parent claim is used.

The exact cap values used below are
\[
D(13)=67,\quad D(14)=69,\quad D(23)=132,\quad
D(24)=144,\quad D(37)=237.
\]

## 1. The seed \(\mathcal R(2,24)=\varnothing\)

Suppose J is a 24-vertex graph with alpha(J)<=2, omega(J)<=11 and the inherited cap. For each vertex, its non-neighbourhood is a clique, hence has size at most11. Thus delta(J)>=12. Handshake gives e(J)>=144, while D(24)=144, so J is exactly 12-regular.

Let L be the complement. Then L is triangle-free and 11-regular. Also alpha(L)=omega(J)<=11, so L is non-bipartite: a bipartition of 24 vertices has a side of size at least12, which would be an independent set of L.

Let C be a shortest odd cycle of L, of length 2k+1>=5. It is chordless. Each vertex outside C has at most k neighbours on C, since its C-neighbourhood is independent in the cycle. Summing degrees over C gives
\[
11(2k+1)\le2(2k+1)+k(23-2k),
\]
or
\[
2k^2-5k+9\le0.
\]
The discriminant is \(25-72<0\), a contradiction. Hence
\[
\boxed{\mathcal R(2,24)=\varnothing.}
\]
The same exclusion applies to any induced 24-set of a larger graph in the class.

## 2. Triangle-free odd-cycle bound and Mantel input

If Q is triangle-free on n vertices and C is a shortest odd cycle of length 2k+1, then C is chordless, every outside vertex has at most k neighbours on C, and the outside graph is triangle-free. Mantel's inequality therefore gives
\[
e(Q)\le 2k+1+k(n-2k-1)
+\left\lfloor\frac{(n-2k-1)^2}{4}\right\rfloor. \tag{2.1}
\]
Mantel is used only in its elementary form: for each edge xy in a triangle-free m-vertex graph, d(x)+d(y)<=m; summing over edges and applying Cauchy gives e<=m^2/4.

The exact maxima from (2.1) are:
- n=23: 122;
- n=25: 145;
- n=18: 73.

These are also checked by Q33_SOURCE_COMPLETE_REPLAY.py.

## 3. The lower-order seed \(\delta(\mathcal R(3,35))\ge12\)

Let H be in \(\mathcal R(3,35)\), and let L be its complement. Since alpha(H)<=3, L is K4-free; since omega(H)<=11, alpha(L)<=11.

### 3.1 Degrees below 11

If d_H(v)<=10, the non-neighbourhood of v has at least24 vertices and has independence number at most2 (otherwise adjoining v gives an independent four-set). It inherits the density caps and clique bound, contradicting \(\mathcal R(2,24)=\varnothing\). Thus delta(H)>=11.

### 3.2 A degree-11 vertex would give a forbidden 14-set

Suppose d_H(v)=11. In L, v has degree23. Put W=N_L(v), so |W|=23, and let R be the other11 vertices. The graph L[W] is triangle-free and has alpha at most11. By (2.1), e(L[W])<=122.

The following exact classification is the one used in the retained source proof.

**122 edges.** Equality in (2.1) forces a C5 and a K9,9 exterior. The five cycle-neighbour types are the nonadjacent pairs of C5; compatibility across the K9,9 bipartition forces one side to have one type and the other side to use its two neighbouring types. Thus
\[
W=C_5(10,a,1,1,b),\quad a+b=11,\quad1\le a,b\le10.
\]

**121 edges.** A shortest odd cycle is again a C5. Its 18-vertex exterior has 80 or81 edges. It must be bipartite (a non-bipartite triangle-free 18-vertex graph has at most73 edges), hence is K9,9, K8,10, or K9,9 minus one edge. The type-compatibility analysis gives either an edge-deleted member of the 122-edge family or
\[
C_5(9,9,2,1,2).
\]
The full case split is retained in the hashed SEED_NEIGHBOURHOOD_EXCERPT.md source. In particular it treats all five possible deleted cycle-class edge types and the exceptional missing K9,9 cross-edge.

Because R cannot be independent in L (otherwise R union {v} is an independent 12-set), choose xy in E(L[R]). Let
\[
I=N_L(x,W)\cap N_L(y,W).
\]
The set I is independent in L[W], since an edge in I together with xy would make a K4 in L. Hence |I|<=11.

For every 12-set T subset W, each vertex of T minus I is adjacent in H to at least one of x,y, while xy itself is a nonedge of H. Consequently
\[
e(H[T\cup\{x,y\}])
\ge78-e(L[T])-|T\cap I|. \tag{3.1}
\]

For W=C5(10,a,1,1,b), the five maximal independent class-pair types are P+s, P+t, A+B, A+t, B+s. The choices T=P+s+t or T=(A union B)+s/t give cost
\[
e(L[T])+|T\cap I|\le6.
\]
For an edge-deleted member, if I was independent before deletion the same choice works; otherwise I contains both deleted endpoints and is contained in those endpoints plus the unique common non-neighbour class. The five edge types give cost at most3 (the deleted s-t edge is impossible because it would create an independent 12-set). For C5(9,9,2,1,2), the two 12-sets P+C+d and Q+d+E each have two L-edges and the maximal independent class-pair list gives cost at most4.

Thus in every 121/122 case there is T with cost at most6. Equation (3.1) gives at least72 edges on a 14-set, contradicting D(14)=69. Therefore e(L[W])<=120.

But W is an induced 23-set of H, so
\[
e(L[W])=253-e(H[W])\ge253-D(23)=121,
\]
a contradiction. Hence no degree-11 vertex exists and
\[
\boxed{\delta(\mathcal R(3,35))\ge12.}
\]
Handshake also gives e(H)>=210.

This seed uses the 14-point and 23-point inherited caps explicitly. It does not assume a total-edge equality, a binary decoration, or any 49-point parent.

## 4. The 36- and 37-point lower-order classes

### 4.1 \(\mathcal R(3,36)\)

If d_H(v)<=11, its non-neighbourhood has at least24 vertices and independence number at most2, contradicting Section1. Thus delta>=12.

If d_H(v)=12, delete one neighbour u of v. In H-u, vertex v has degree11, and H-u is an induced member of \(\mathcal R(3,35)\). This contradicts Section3. Therefore delta>=13 and
\[
\boxed{e(H)\ge36\cdot13/2=234.}
\]

### 4.2 \(\mathcal R(3,37)\) is empty

If a vertex had degree at most12, its non-neighbourhood would contain at least24 vertices and have independence number at most2, contradicting Section1. Thus delta>=13. Handshake gives
\[
e(H)\ge\lceil37\cdot13/2\rceil=241>D(37)=237.
\]
Therefore
\[
\boxed{\mathcal R(3,37)=\varnothing.}
\]

## 5. Minimum-degree transport to \(\mathcal R(4,47)\)

Let J be in \(\mathcal R(4,47)\), and let v be a minimum-degree vertex.

### 5.1 Degree at most nine

If d(v)<=9, the non-neighbourhood C has at least37 vertices and alpha(C)<=3, since an independent four-set in C together with v would be an independent five-set. Any 37-subset is in \(\mathcal R(3,37)\), impossible by Section4.2.

### 5.2 Degree ten

Suppose d(v)=10. Let S=N(v), |S|=10, and C=V(J) minus N[v], |C|=36. Then C is in \(\mathcal R(3,36)\), so e(C)>=234.

Write e_S=e(J[S]) and e_SC=e_J(S,C). Every x in S has degree at least10, and
\[
\sum_{x\in S}d_J(x)=10+2e_S+e_{SC}\ge100.
\]
Therefore
\[
e_S+e_{SC}\ge90-e_S\ge90-\binom{10}{2}=45.
\]
The complete edge partition is
\[
e(J)=e(C)+10+e_S+e_{SC}\ge234+10+45=289.
\]
This is the exact minimum-pivot count. It does **not** assume S is a clique.

### 5.3 Degree eleven

Suppose d(v)=11. Let S=N(v), |S|=11, and C=V(J) minus N[v], |C|=35. Then C is in \(\mathcal R(3,35)\), so e(C)>=210.

The shell S cannot be a K11, since v together with S would be a K12. Let M be the missing-edge graph on S, z=e(M)>=1. For a in S put
\[
g_a=d_J(a)-11\ge0,\qquad
D_a=N_J(a)\cap C,\qquad t_a=|D_a|.
\]
Since a has 10-d_M(a) neighbours inside S and one neighbour v,
\[
t_a=d_M(a)+g_a.
\]

Choose a missing shell edge ab in M. If |D_a union D_b|<=11, at least24 vertices of C are common non-neighbours of a,b. Their induced graph has alpha at most2, since an independent triple together with nonadjacent a,b would be an independent five-set. This contradicts Section1. Hence
\[
t_a+t_b\ge|D_a\cup D_b|\ge12.
\]
Also
\[
d_M(a)+d_M(b)\le z+1,
\]
because ab is counted twice and every other M-edge incident with a or b is counted at most once. Thus
\[
z+\sum_{x\in S}g_x
\ge z+g_a+g_b
\ge t_a+t_b-1
\ge11.
\]
Finally, summing the shell rows gives the exact edge identity
\[
e(J)=e(C)+11+\binom{11}{2}-z+\sum_{a\in S}t_a
=e(C)+66+z+\sum_{a\in S}g_a
\ge210+66+11=287.
\]

### 5.4 Conclusion

The cases d(v)<=9, d(v)=10, d(v)=11 are all impossible when e(J)<=286. Therefore
\[
\boxed{J\in\mathcal R(4,47),\ e(J)\le286
\Longrightarrow\delta(J)\ge12.}
\]

## 6. Independent audit of the retained 284-edge floor proof

This section is not needed for the minimum-degree implication above, but it is part of the historical source gate and was audited because the Q33 task explicitly requests the 127-row certificate and lower-order assets.

If J is in \(\mathcal R(4,47)\) and e(J)<=283, Section5 gives delta(J)>=12 and
\[
\sum_v(d(v)-12)=2e(J)-564\le2.
\]
At least45 vertices have degree12. A greedy independent-set selection in their induced graph (maximum degree at most12) gives an independent four-set I.

For each i, the vertices whose I-support is exactly {s_i}, together with s_i, form a private clique K_i of size at most11. The remaining set Z has support sizes2,3,4. The exact incidence surplus is
\[
\sum_{z\in Z}(|N(z)\cap I|-1)=5.
\]
Thus |Z| is 3,4,5, and the only clique-size profiles are
\[
11^4;\qquad(10,11,11,11);\qquad
(9,11,11,11)\text{ or }(10,10,11,11).
\]

For |Z|=3,4, the weighted-transversal lemma proves every regular Z-vertex is complete to one private clique. Its exact rational certificate has 127 rows: 32 for 11^4 and 95 for (10,11,11,11). For |Z|=5, each Z-vertex has support size2; the complete-bipartite blocker between the two private non-neighbour sets forces every regular Z-vertex to complete one of its two supported cliques. In all cases, completers assigned to a fixed K_i form a clique. The exact remaining-vertex count in the capacity step is at least
\[
47-b-s_i-2(12-s_i)-2=21-b+s_i\ge25
\]
when s_i<=10, b<=5, s_i>=9. This corrects a weak displayed lower bound in the archived proof: the archive says only “at least22” immediately before deriving t_1>=2; 22 alone would not imply that inequality, but the exact count is at least25 and implies the stated t_1>=2, t_2>=6, t_3>=8 (in fact stronger). Thus the graph argument is repaired without changing its conclusion.

The four clique capacities sum to
\[
\sum_i(11-|K_i|)=b-3,
\]
while at least b-2 vertices of Z are regular and must be assigned. Contradiction. Hence the cases e=282,283 are impossible and
\[
\boxed{e(J)\ge284\quad\text{for all }J\in\mathcal R(4,47).}
\]

The exact rational certificate and its standard-library verifier were both retained in FRONTEND_LINE_A_V1.zip. Both copies (the five-block V2 audit path and the terminal V1 input path) were run independently; each verified all127 rows exactly.

## 7. External theorem and archive audit

- The minimum-degree proof uses only the elementary shortest-odd-cycle bound, Mantel's inequality (proved in Section2), exact induced-density caps, the analytic 121/122 neighbourhood classification, and the exact rational certificate described above.
- Kang–Pikhurko is **not** a dependency of the minimum-degree proof or the Q33 core contradiction.
- No Q32 285-edge/excess-six statement is used.
- No V11 retained minimum-degree assertion is used.
- BACKEND49_FIRST_PRINCIPLES_AUDIT_V1 and HIGH_LAYER_BACKEND_V8 were inspected as historical context, but neither is a dependency.
- T61_H13_V11.zip was separately replayed; its finite kernel verifier passes, but the broader V11 analytic package remains outside this proof and is not imported.

## 8. Source provenance and hashes

The following hashes identify the exact retained source assets inspected:

| Asset | SHA256 |
|---|---|
| FRONTEND_LINE_A_V1.zip | 8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac |
| BACKEND49_FIRST_PRINCIPLES_AUDIT_V1.zip | 3801a02fa8e9f53b19c5d289d14deb2f9ef7923e8c63497ca829ad998b433315 |
| HIGH_LAYER_BACKEND_V8.zip | 8c05b4490a4c0cdaf08be20180902ec2b5e126f5f275c35f2f12ff353bb825da |
| T61_H13_V11.zip | 27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4 |
| STRICT_DESCENT_PROOF.md | d91e44a2d9a9cf17d8766f9b0b3c442d8e6bb0818b45a9657618c9119fc306ae |
| SEED_AND_CORE_AUDIT.md | ed2c98b85c82ce7ed439506b6828593639face53c87b2a78225dcba2f84565bc |
| SEED_NEIGHBOURHOOD_EXCERPT.md | b287b12026c4e7968d8acd1800c570b6c4ea2a2aaedd24f5083396da0a466ec0 |
| SEED_TRIANGLE_FREE_EXCERPT.md | 713b2163617650ee96e7e315f02a273a4873b8e87843e4ca90149991f007ef33 |
| CORE_FLOOR_284_PROOF.md | 0ebf37349c7e1c9fdfef54c95b9cb42363b9daa6c32e870cc9a4b5eca5bb837d |
| COMPLETION_CERTIFICATE.csv | 2603ef814d77fb34f2f13569d64ed15ca40bc4c9d9b85518b41e83da8feaecd9 |
| verify_completion.py | 094d2ea62847af6a28fec136ca2990e13ec32f7cb9beaac8a25ea51e7f39ba32 |
| VERIFIED_COMPLETION.json | f4e3688db01a6efefe34bb1cc9fa39c83575b7aaccacd1d828e20746adba51cc |
| Q33_SOURCE_COMPLETE_REPLAY.py | to be recorded in INDEPENDENT_REPLAY_LOG.md |

The archive sources are retained as the named uploaded assets; this workstream retains the hashes, exact file paths, replay scripts, and replay outputs.

## 9. Actual clean-room replay on 2026-10-30

The original FRONTEND_LINE_A_V1.zip was extracted from the current conversation upload. Its SHA256 and the three companion archive hashes were recomputed and matched the source manifest. The exact 127-row certificate and both retained original verifiers were then executed from the extracted archive.

Observed:
- both original Fraction verifiers: EXACT_CERTIFICATE_VERIFIED, 127 rows;
- exact maxima: 773/1089 and 39/44;
- original S31 arithmetic supplement verifier: EXACT_ARITHMETIC_SUPPLEMENT_VERIFIED, with 15 d3 parameter rows, 25 d3 defect rows and 4 d10 coupling rows; it explicitly reports the original K145 bridge OPEN;
- Q33_SOURCE_COMPLETE_REPLAY.py: PASS_EXACT_ARITHMETIC_REPLAY, including D(13), D(14), D(23), D(24), D(25), D(37), shortest-cycle bounds 122/145/73, R(3,35) charge maximum6, degree-10 floor289, degree-11 floor287, support counts9/40/48, mixed matrices P/D, charge minima6/6/4/5, and optional exact replay of all127 rational rows.

The 127-row certificate is a finite proof of the weighted-transversal inequality in the separate total-excess<=2 private-clique lemma. It is not a premise in the minimum-degree theorem of Sections1–5. The minimum-degree theorem is analytic and uses the full R(2,24), R(3,35), R(3,36), R(3,37) chain. The finite replay verifies arithmetic and certificate coverage; it does not replace the 121/122-edge analytic type classification.
