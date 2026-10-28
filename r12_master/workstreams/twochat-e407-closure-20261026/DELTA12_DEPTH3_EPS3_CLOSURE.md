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

We also use the single-vertex component rule. In a q=0 union of four cliques, every U vertex must be complete to one W-component; otherwise one nonneighbor from each component together with the U vertex gives an independent five-set. In the q=1 profile, if a U vertex is complete to no base component, avoiding an independent four-set among its W-nonneighbours forces the unique cross-edge endpoints to be the sole nonneighbours in both incident base components, costing at least six W-neighbours. Thus any q=1 U vertex of W-degree at most five must also contain a whole base component.

## 2. xy not restored: profile K3 + K5 + K5 + K5

The exceptional neighborhoods are disjoint and their union is exactly K3 plus one K5. Each of x,y must individually contain a whole W-component. Therefore, up to swapping,
\[
N_W(x)=K_3,
\qquad N_W(y)=K_5^A.
\tag{2.1}
\]

Take z in P3 union P4. The pair x,z must cover two components, so z is complete to one of the three K5 components. The pair y,z shows that the K5 cannot be K5^A alone; equivalently z must be complete to one of the two remaining K5s K5^B,K5^C. Since d_W(z)<=6, this label is unique.

If u in P3 and v in P4 have the same K5 label, each has at most one W-neighbour outside that K5. Their union therefore contains that K5 plus at most two further vertices, too few to contain any second W-component. But u,v are H-nonadjacent, contradicting the pair rule.

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

For z in P3 union P4, the two pairs x,z and y,z force z to be complete to a component usable as the second covered component for both pairs. Therefore z is complete to either K4^C or K6^D. Call these labels C and D. The label is unique because 4+6>6.

A cross P3-P4 pair with label D is impossible: both vertices are complete to the same K6 and have no room for a second full component. If one entire P-part had label D, its target K7 together with K6^D would give K13. Thus both P3 and P4 contain C-labelled vertices.

For a cross pair u,v both labelled C, each has at most two neighbours outside K4^C. The pair rule forces both degrees to be exactly six and their four outside incidences to partition one of K4^A,K4^B into two complementary 2-sets. Repeating this across all cross C-pairs shows that all C-labelled vertices on each side use one fixed outside 2-set and the two sides use complementary 2-sets in the same exceptional K4.

Any D-labelled vertex can occur on at most one side. If D occurs on one side, the other side is all C; a D vertex together with the other six vertices of its own target K7 part and K6^D gives a K13. Hence D does not occur at all. Therefore every vertex of P3 and P4 is C-labelled. Relabel A,B if necessary so there is a fixed E subset K4^A with |E|=2 such that
\[
N_W(z)=K_4^C\cup E \quad(z\in P_3),
\]
\[
N_W(z)=K_4^C\cup(K_4^A\setminus E) \quad(z\in P_4).
\tag{3.2}
\]
All these vertices have W-degree six and therefore no restored incidence.

### 3.1 Unpack the registered 309-edge equality model

The balanced equality model on U is the following exact labelled graph L3. The four base parts P1,...,P4 have size seven. There is y in P2, a nonempty proper A0 subset P1, and the exceptional x. Starting from the complete four-partite graph on P1,...,P4, the A0-y edges are deleted and x is joined in L3 to
\[
P_3\cup P_4\cup A_0\cup\{y\}.
\]
Equivalently in H0=bar(L3):
- every Pi is a target K7;
- x is target-adjacent exactly to P1\A0 and P2\{y} among the base vertices;
- y is target-adjacent to A0 and to the other six vertices of P2;
- P1 is target-anticomplete to P2\{y}.

This description gives the already-registered exceptional degree formulas
\[
d_W(x)=|A_0|-1+\epsilon_x-I_x,
\qquad
d_W(y)=6-|A_0|+\epsilon_y-I_y.
\]

In the present nonrestored survivor all three restored edges avoid x,y,P3,P4. Since L3 has no edges inside a base part, every restored edge therefore lies between P1 and P2\{y}. In particular every t in
\[
R:=P_1\cup(P_2\setminus\{y\})
\]
has epsilon_t=0 and H0-degree seven in U. Hence
\[
\boxed{d_W(t)=5-I_t\le5.}
\tag{3.3}
\]

### 3.2 Every R-vertex gets a binary A/B W-label

Fix t in R. It is H-nonadjacent to every vertex of P3 and P4, because those cross pairs are L3-edges and no restored edge meets P3 or P4.

Pair t with a P3 vertex. By (3.2), the P3 vertex already covers K4^C and E subset K4^A. To cover two whole W-components, N_W(t) must contain one of:
- K4^A\E together with E, i.e. all K4^A;
- all K4^B;
- all K6^D.

Pairing t with P4 gives the analogous requirement with E and K4^A\E interchanged. Hence satisfying both sides forces N_W(t) to contain all of K4^A, all of K4^B, or all of K6^D. The last option is impossible by d_W(t)<=5. Thus every t in R has a unique binary label A or B according as it is complete to K4^A or K4^B.

### 3.3 P1 is forced to use both labels

Keep N_W(x)=K4^A and N_W(y)=K4^B.

If t in A0 had label A, then xt is an H-nonedge and
\[
|N_W(x)\cup N_W(t)|\le4+5-4=5,
\]
so the pair cannot cover two W-components. Contradiction. Therefore every t in A0 has label B.

If t in P1\A0 had label B, then yt is an H-nonedge and the same argument with y gives a contradiction. Therefore every t in P1\A0 has label A.

Since A0 is nonempty and proper,
\[
\boxed{P_1\text{ uses both binary labels A and B}.}
\tag{3.4}
\]

### 3.4 Three restored edges cannot absorb the same-label cross pairs

Write
\[
a=|\{u\in P_1:u\text{ has label A}\}|,
\qquad
b=|\{v\in P_2\setminus\{y\}:v\text{ has label A}\}|.
\]
By (3.4), 1<=a<=6.

A same-label pair u in P1, v in P2\{y} must be a restored target edge. Otherwise u,v are H-nonadjacent and their W-neighborhood union consists of their common K4 label plus at most two extra vertices, too small to cover a second W-component. Thus every same-label cross pair consumes one of the three restored edges.

The number of same-label cross pairs is
\[
S(a,b)=ab+(7-a)(6-b).
\]
For fixed mixed a:
- if a<=3, S is minimized at b=6 and S>=6a>=6;
- if a>=4, S is minimized at b=0 and S>=6(7-a)>=6.

Hence
\[
\boxed{S(a,b)\ge6,}
\]
while only three restored edges exist. Contradiction.

Therefore the final all-C complementary-two-set survivor is impossible.

## 4. xy not restored: q=1 profile (4,4,5,5)+one cross edge

The exceptional union has size eight and is exactly the two K4 base parts. Since each exceptional degree is at most five and a non-component-saturating q=1 vertex needs at least six W-neighbours, x and y individually saturate the two K4s.

For z in P3 union P4, the pairs x,z and y,z have union size at most ten, so the one-defect escape is unavailable. Each pair must cover two base components. Therefore z must be complete to one of the two K5 parts. With degree at most six the label is unique.

A same-label cross P3-P4 pair has at most two total neighbours outside its common K5, too few to complete a K4. Hence cross labels are opposite. Each P-part is monochromatic and the two labels differ, producing K7 join K5 = K12. Contradiction.

Thus the q=1 profile is impossible.

## 5. xy restored

Now d_W(x)=d_W(y)=3.

For K4+K4+K4+K6, component exhaustion requires every U vertex to contain a full component, impossible at W-degree three.

For the q=1 (4,4,5,5) profile, a degree-three vertex neither contains a full component nor can realize the defect escape, whose minimum cost is six. Hence this profile is impossible.

For K3+K5+K5+K5, both x and y must be complete to the unique K3. For any z in P3 union P4, the pair x,z forces z to be complete to one of the three K5s. Since d_W(z)<=6, z has a unique K5 label.

A same-label cross pair cannot cover a second component. Hence the sets of K5 labels used on P3 and P4 are disjoint. No P-part may use only one label, because a target K7 complete to one K5 is K12. Thus each part uses at least two labels, impossible for two disjoint subsets of a three-label set.

Therefore the restored-xy branch is impossible.

## 6. Conclusion

All epsilon_U=3 depth-3 profiles are impossible. Therefore
\[
\boxed{
\delta=12,\ \text{non-four-partite depth3},\ \epsilon_U=3
\Longrightarrow\bot.
}
\]

The only remaining depth-3 epsilon is epsilon_U=4. The separate delta=12 four-partite-U branch and all delta<=11 remain open. E407 Q32 remains OPEN / NOT_CERTIFIED.

## 7. Dependency scope

The proof uses:
1. the registered balanced 309-edge Kang–Pikhurko equality model, including its exact labelled P1/P2/P3/P4,x,y,A0 construction;
2. the exact epsilon_U=3 W-profile list;
3. the low-W-degree lemma;
4. the proved q=1 one-defect pair rule;
5. pure alpha(H)<=4 and omega(H)<=11 pair/component reasoning.

The terminal arguments do not use Didin. The external equality model remains an explicit conditional dependency.