# E407 Q32 — delta=12 depth-3 epsilon_U=3 closure

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL / CLOSED** under the registered balanced 309-edge Kang–Pikhurko equality model and the recorded epsilon_U=3 W-profile classification. E407 Q32 remains OPEN / NOT_CERTIFIED.

## 1. Starting exceptional-pair reduction

Use `DELTA12_DEPTH3_EPS3_EPS4_PAIR_REDUCTION.md`. The exceptional pair is x,y.

If xy is not restored, then
\[
N_W(x)\cap N_W(y)=\varnothing,
\qquad d_W(x)+d_W(y)=8,
\]
all three U-excess units lie on x,y, and no restored edge is incident with x or y. Their union is a minimum two-component cover.

If xy is restored, then
\[
d_W(x)=d_W(y)=3,
\]
all three U-excess units lie on x,y, and xy is the only restored edge incident with the pair.

In either case every z in P3 union P4 has epsilon_z=0. No restored edge has P3-P4 type. In the nonrestored case no restored edge meets x or y; in the restored case the only restored edge meeting either is xy. Hence every z remains H-nonadjacent to both x and y, and
\[
d_W(z)=6-I_z\le6.
\tag{1.1}
\]
The two parts P3,P4 are target K7s and are target-anticomplete to each other.

We repeatedly use the pure pair rule: if u,v are H-nonadjacent, their common W-nonneighbours contain no independent triple. In q=0 four-clique profiles this means N_W(u) union N_W(v) contains two full W-components. In the q=1 (4,4,5,5) profile the same conclusion holds whenever the union has size at most ten, by the one-defect lemma.

We also use the single-vertex component rule. In a q=0 union of four cliques, every U vertex must be complete to one W-component; otherwise one nonneighbor from each component together with the U vertex gives an independent five-set. In the q=1 profile, if a U vertex is complete to no base component, avoiding an independent four-set among its W-nonneighbours forces the unique cross-edge endpoints to be the sole nonneighbours in both incident base components, costing at least (4-1)+(4-1)=6 W-neighbours. Thus any q=1 U vertex of W-degree at most five must also contain a whole base component.

## 2. xy not restored: profile K3 + K5 + K5 + K5

The exceptional neighborhoods are disjoint and their union is exactly K3 plus one K5. Each of x,y must individually contain a whole W-component. Therefore, up to swapping,
\[
N_W(x)=K_3,
\qquad N_W(y)=K_5^A.
\tag{2.1}
\]

Take z in P3 union P4. The pair x,z must cover two components, so z is complete to one of the three K5 components. The pair y,z shows that the K5 cannot be K5^A alone; equivalently z must be complete to one of the two remaining K5s K5^B,K5^C. Since d_W(z)<=6, this label is unique.

If u in P3 and v in P4 have the same K5 label, each has at most one W-neighbour outside that K5. Their union therefore contains that K5 plus at most two further vertices, too few to contain any second W-component (the smallest has size three). But u,v are H-nonadjacent, contradicting the pair rule.

Hence every cross P3-P4 pair has opposite binary labels. This forces each P3 and P4 to be monochromatic in the binary label and the two parts to have opposite labels. A target K7 together with its target-complete K5 gives K12, contradicting omega(H)<=11.

Thus this profile is impossible.

## 3. xy not restored: profile K4 + K4 + K4 + K6

The exceptional union is exactly two K4 components. By individual component exhaustion and disjointness,
\[
N_W(x)=K_4^A,
\qquad N_W(y)=K_4^B
\tag{3.1}
\]
up to swapping.

For z in P3 union P4, the two pairs x,z and y,z force z to be complete to a component usable as the second covered component for both pairs. Therefore z is complete to either K4^C or K6. Call these labels C and D. The label is unique because 4+6>6.

A cross P3-P4 pair with label D is impossible immediately: both vertices are complete to the same K6 and have no room for a second full component.

Suppose a cross pair u,v both has label C. Each has at most two neighbours outside K4^C. To satisfy the pair rule, both must have W-degree exactly six and their four outside incidences must partition one of K4^A,K4^B into two complementary 2-sets.

Fix u. All same-label-C vertices v on the opposite side must therefore have the same complementary 2-set, lying in the same one of K4^A,K4^B. In particular if both sides contain C-labelled vertices, every C-labelled vertex on each side has W-degree six and no restored incidence.

Now D cannot appear on both sides, while a side consisting entirely of D would be a target K7 complete to K6, giving K13. Hence both sides contain C. Since all cross pairs between C-vertices are legal only with the complementary-two-set pattern, each side's C vertices use one fixed outside 2-set and the opposite side uses its complement.

If either side has all seven vertices labelled C, its K7 is target-complete to K4^C, giving a K11, which is allowed; however every vertex on the opposite side is H-nonadjacent to all seven and cannot be D-only. Thus it also has a C vertex v. The fixed C neighborhoods of that side and v on the other side make their outside 2-sets complementary in, say, K4^A. Choose any C-vertex u on the first side. The pair u,v covers exactly K4^C and K4^A.

Take a D-labelled vertex w on either side if one exists. Crossing w with a C vertex on the opposite side, the union contains K6 plus K4^C, so it is legal; but crossing w with any D vertex is impossible. Hence all D labels, if present, lie on only one side. The opposite side is all C and forms K11 with K4^C. Each D vertex on the first side is also target-adjacent to all six vertices of K6, and to the other six vertices of its P-part. Thus it lies in a K13 with its own P-part and K6, contradiction. Therefore no D vertex exists.

Both P3 and P4 are all C. Then P3 union K4^C is K11 and P4 union K4^C is another K11 sharing K4^C. For any u in P3,v in P4 their extra two-sets must be complementary in a fixed K4, so all vertices of P3 have the same two outside W-neighbours and all vertices of P4 the complementary two. Let a be one of the two outside neighbours used by P3. Then a is target-adjacent to all seven vertices of P3 and to all four vertices of K4^C (same W component is a clique only if a lies in K4^C, which it does not), so this last step does not by itself create K12.

Therefore the all-C complementary-two-set configuration remains a genuine terminal subcase and is **not excluded by the preceding argument**.

Accordingly Section 3 records a strict reduction, not a contradiction. The epsilon_U=3 closure cannot be claimed from Sections 2-3 alone.

## 4. xy not restored: q=1 profile (4,4,5,5)+one cross edge

The exceptional union has size eight and must cover two base components; hence it is exactly the two K4 base parts. Since each exceptional degree is at most five and a non-component-saturating q=1 vertex needs at least six W-neighbours, x and y individually saturate the two K4s. Thus both have degree four.

For z in P3 union P4, the pairs x,z and y,z have union size at most ten, so the one-defect escape is unavailable. Each pair must cover two base components. Therefore z must be complete to one of the two K5 parts. With degree at most six the label is unique.

A same-label cross P3-P4 pair has at most two total neighbours outside its common K5, too few to complete a K4. Hence cross labels are opposite. Each P-part is monochromatic and the two labels differ, producing K7 join K5 = K12. Contradiction.

Thus the q=1 profile is impossible.

## 5. xy restored

Now d_W(x)=d_W(y)=3.

### Profiles with minimum component size four

For K4+K4+K4+K6, component exhaustion requires every U vertex to contain a full component, impossible at W-degree three.

For the q=1 (4,4,5,5) profile, a degree-three vertex neither contains a full component nor can realize the defect escape, whose minimum cost is six. Hence this profile is also impossible.

### Profile K3+K5+K5+K5

Both x and y must be complete to the unique K3:
\[
N_W(x)=N_W(y)=K_3.
\]
For any z in P3 union P4, the pair x,z forces z to be complete to one of the three K5s. Since d_W(z)<=6, z has a unique K5 label.

A same-label cross pair has at most two further W-neighbours outside its common K5, so cannot cover a second component. Hence the sets of K5 labels used on P3 and P4 are disjoint.

No P-part may use only one label, because a target K7 complete to one K5 is K12. Thus each of P3 and P4 uses at least two labels. Two disjoint subsets of a three-label set cannot both have size at least two. Contradiction.

Therefore the restored-xy branch is impossible.

## 6. Audited conclusion

Sections 2,4,5 are terminal contradictions. Section 3 leaves one explicit survivor:

> epsilon_U=3, xy not restored, W=K4+K4+K4+K6, all P3 and P4 vertices are complete to the same third K4, with degree six and fixed complementary two-subsets of one of the exceptional K4s across the two P-parts.

Thus the correct status is:
\[
\boxed{\epsilon_U=3\text{ depth3 is reduced to one all-C complementary-two-set terminal.}}
\]
It is **not yet closed**. This file deliberately records the failed attempted closure rather than promoting the survivor away.

## 7. Dependency scope

The reductions use the registered 309-edge equality model, exact W profiles, low-W-degree lemma, pure alpha/omega pair arguments, and for q=1 the proved one-defect pair lemma. Didin is not used in these terminal arguments. E407 Q32 and EG617(r=12) remain OPEN.