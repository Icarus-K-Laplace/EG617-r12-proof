# Independent h12 and exceptional-parent closure

Date: 2026-10-31. Status: **PROVED**, using the frozen lower-order cap lemmas and CORE211 derived in the audited COVER proof. This is a dedicated48-point argument; the47-point287 floor is not transported by changing the order.

Write R(a,n) for alpha<=a, omega<=11 and all D caps, with D(n)=binom(n,2)-11 p12(n). The prior self-contained lower-order proof gives R(2,24) empty, delta(R(3,35))>=12, delta(R(3,36))>=13 and e>=234, and R(3,37) empty. AES then gives the35-point floor211, as independently mapped in COVER Section8.

## 1. Every R(4,48) graph has minimum degree at least12

For J in R(4,48), a vertex of degree at most10 leaves at least37 nonneighbors with independence at most3, impossible. If a vertex p has degree11, its36-core H belongs to R(3,36). The lower floor234 and D(36)=234 force e(H)=234. Every shell point a has at most3 neighbors in H, by the37-set cap D(37)=237.

The11-shell cannot be a target clique, since together with p it would make K12. Choose target-nonadjacent shell vertices a,b. Their common antineighborhood in H has independence at most2 and at most23 vertices by R(2,24) emptiness. Hence their H-row union has at least36-23=13 vertices. But the two rows each have at most3 vertices. Contradiction. Therefore delta(J)>=12, without any edge-count hypothesis.

## 2. A complete12-shell lemma at charge20

Consider a degree12 pivot in a minimum-degree12 parent. Let M be the missing graph on its12-shell, t=d_M+g, q=e(M)+sum g, with nonnegative integer g. Assume the inherited conditions:

    e(M)>=11; alpha(M)<=10;
    t_a+t_b>=12 on every M-edge;
    t(T)>=24 on every M-triangle.

These imply q>=20. A triangle gives q>=24-3=21. In the triangle-free case M has a2-matching: a graph of matching number at most1 is a star or triangle plus isolates; the former has independence at least11, and the latter has only3 edges. For the four endpoints S of a2-matching, t(S)>=24 and e_M(S)<=4 by Mantel, so q>=20.

At q=20 equality forces M[S]=K2,2, t(S)=24, and all eight other vertices are independent and undecorated. A3-matching is impossible, since its endpoints give q>=36-9=27. Every exterior point meets only one side of the K2,2 by triangle-freeness. Exterior attachments cannot occur on both sides: two such attachments plus the edge between the two unused cycle points make a3-matching. Thus all attachments meet one two-point side X, giving a two-hub cover and ten independent lows Y.

Summing the four K2,2 edge inequalities shows every such edge has weight sum12. The two X weights have a common value a and the two opposite weights are12-a. Opposite-side missing degree2 gives a<=10. Since z>=11, at least seven attachments exist. A nonisolated exterior point is regular of missing degree at most2, so its edge inequality against a forces a=10 and its degree2. Consequently

    M=K_(2,r) plus (10-r) isolates, 6<=r<=10,
    hub weights10, hub decorations10-r,
    every low regular, with row size2 or0.         (Q20)

This proves both the floor and the complete equality classification; no historical q20 black box is used.

## 3. Direct inserted-center obstruction

Suppose (Q20) occurs and y is a leaf. Its core row D_y has two points. Repivoting at y replaces D_y in the old core by the two old hubs. The hubs are target-adjacent, since their missing graph has no hub-hub edge. Each hub has only10 neighbors in the old core. Its degree in the new core is therefore at most10+1=11, even before subtracting any edges into D_y.

Thus (Q20) is impossible whenever the actual core at every degree12 pivot has minimum degree at least12. This contradiction needs no row-class rotation, no assumed disjointness of hub/leaf rows, and no equality assertion about the new core's edge count.

## 4. The generic48-point floor310

Let J in R(4,48). Section1 gives delta>=12. If delta>=13, handshake gives e(J)>=312. Otherwise take a degree12 pivot. Its35-core H belongs to R(3,35), has minimum degree12 and at least211 edges. D(13)=67 gives shell z>=78-67=11, and alpha(M)<=10. For a missing shell edge its uncovered35-core has alpha<=2 and order at most23, giving pair-row coverage12. For a missing triangle the uncovered core is a target clique of size at most11, giving triangle coverage24.

Section2 gives q>=20. But every leaf repivot has another35-core in R(3,35), so Section3 excludes q20. Hence q>=21 and

    e(J)=78+q+e(H)>=78+21+211=310.

This proof establishes the floor for all R(4,48), including graphs below309; it does not begin by assuming an unproved309 floor.

## 5. Full T61 h12 exclusion

Let F be a genuine61-point T61 graph, delta(F)=12, alpha<=5, omega<=11, all caps, and E<=408. A degree12 pivot has an actual48-core C in R(4,48). Section4 gives e(C)>=310. For its12-shell, the pair-row union is at least12: its uncovered core has alpha<=3 and cannot contain37 vertices. A missing triangle has union at least25 by R(2,24) emptiness, which is stronger than the24 required in Section2. The remaining shell conditions follow as above.

Thus

    E=78+q+e(C)>=78+20+310=408.

For E<408 there is already a contradiction. At E408 equality forces q20 and e(C)=310. Every degree12 repivot has another48-core in R(4,48), of minimum degree12 by Section1. The inserted-center obstruction contradicts this. Therefore all h12 T61 parents with E<=408 are impossible, including E406/E407/E408.

## 6. Other minimum degrees and exceptional pivots

For an actual contextual T61 graph, a vertex of degree at most11 leaves at least49 nonneighbors of independence at most4 and inherits omega<=11 and all caps. The independently audited contextual R(4,49) full-color exclusion forbids this. Thus delta>=12. If delta>=14 then E>=ceil(61*14/2)=427>408. Therefore h12/h13 exhaust the possible minimum degrees.

At h13 a degree13 pivot exists by definition, or by handshake if one starts from delta>=13. Decorated shell vertices are not silently treated as regular pivots. Nonmaximum regular pivots inherit the same core class and pointwise bounds. Each repivot in the proofs is in the same original parent, and only the actual set difference of cores is used; no disjoint-parent assumption occurs.

The historical48-point and h12 source proofs at global b0459807 are consistent with these conclusions, but their row-class rotation is unnecessary. The present direct inserted-center proof supplies a shorter complete replacement.
