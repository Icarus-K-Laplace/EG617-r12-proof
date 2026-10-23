# q36 f=2 far-target-K2 — c=8, one d2 row, A=3 repeated-K3 full closure V2

Status: `PROVED` under `Q36_F2_FAR_K2_C8_D2_A3_MULTIPLICITY_REDUCTION.md`, `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CORRECT_REDUCTION.md`, common-S row closure, q36 lexicographic maximality, inherited K4-freeness, `alpha(F)<=4`, and the pure-d2 support contract.

This is the correct replacement for the retracted fixed-remainder closure. No fixed 12-point far-K2 remainder is used.

## 1. Setup

Let D be a target K3 support of multiplicity3 in the c=8,n2=1,A=3 branch. Let

`S=F union {x}`

be the common missing set and

`w_v=kappa_v+e_F(v,S)`.

Because D repeats, a full-defect3 repivot would stay at q36 while inserting three globally decorated support vertices and retaining the two inactive decorated shell vertices. Hence

`u(D)=sum_(d in D) w_d <=2`.                               (1)

The unique d2 support D0 is a pure target K2 of globally regular vertices, target-anticomplete to S and to the d3-support union U. Also `a_F=0`, so x is target-nonadjacent to both far vertices.

The multiplicity reduction gives at least two external owner incidences in supports disjoint from D, and every support disjoint from D is itself a target K3.

## 2. Two or more distinct disjoint support classes are impossible

Assume there are at least two distinct support classes E1,E2 disjoint from D.

The correct reduction already proves that any two such classes intersect in exactly two points. If three distinct classes formed the four-set Type-Q geometry, then three triples on the same four-set cover all six pairs of that four-set, producing a target K4. Therefore the inherited K4-free contract leaves at most two distinct classes, and two classes are necessarily of common-pair form

`E1=P union {z1}`, `E2=P union {z2}`,

where `P={u,v}`.

Because E1 and E2 are target K3s, u and v are adjacent to both petals. K4-freeness forces

`z1 z2` to be a target nonedge.                              (2)

Let

`A=e_H(D,P)`, `b_i=e_H(D,{z_i})`.

Joint row closure from the repeated support D gives

`A+b_i=e_H(D,E_i)<=u(D)<=2`.                                (3)

Since `alpha(H[U])<=2` and z1z2 is a nonedge, every d in D must be adjacent to z1 or z2; otherwise `{d,z1,z2}` would be independent in U. Hence

`b_1+b_2>=3`.                                               (4)

Summing (3) and using (4) gives

`2A+3<=4`,

so

`A=0`.                                                       (5)

Thus D is target-anticomplete to P.

Now apply row closure for E1 to z2. The vertex z2 is adjacent to both u and v, and is nonadjacent to z1, so

`2<=e_H(z2,E1)<=w_z2`.

Similarly `w_z1>=2`. Since each singleton K3 support has total defect at most3,

`w_u+w_v+w_zi<=3`,

and therefore

`w_u+w_v<=1`.                                               (6)

Hence one point p0 in P has

`w_p0=0`.                                                    (7)

Equation (7) means p0 is target-anticomplete to S. By (5) it is also target-anticomplete to D, and D0 is target-anticomplete to p0 because p0 lies in U.

From (1), the three vertices of D have at most two total S-incidences, so some d0 in D is target-anticomplete to all of S. Choose one vertex v0 in D0 and one far vertex f in F. Then

`{p0,d0,v0,x,f}`

is an independent5-set in the parent graph:

- p0 and d0 are nonadjacent by (5);
- p0,d0 are anticomplete to x and f;
- v0 is anticomplete to U and S;
- xf is a nonedge because a_F=0.

This contradicts `alpha(F)<=4`.

Therefore

> there cannot be two distinct support classes disjoint from D.      (8)

## 3. A single disjoint support class is impossible

By the multiplicity reduction, at least two external owner incidences are carried by supports disjoint from D. If there is only one distinct disjoint support class E, then E has owner multiplicity at least2 and is therefore repeated.

As above, E is a target K3. Repetition forbids full defect3, so

`u(E)=sum_(e in E)w_e<=2`.                                  (9)

Because D and E each contain three vertices and their nonnegative integer weights sum to at most2, choose

`d0 in D`, `e0 in E`

with

`w_d0=w_e0=0`.                                              (10)

Since e0 lies outside support D, row closure against D gives

`e_H(e0,D)<=w_e0=0`.

Hence in particular d0e0 is a target nonedge. Both d0 and e0 are target-anticomplete to S by (10), and D0 is target-anticomplete to U and S.

Choose v0 in D0 and f in F. Then

`{d0,e0,v0,x,f}`

is an independent5-set, again contradicting `alpha(F)<=4`.

Therefore

> a single repeated disjoint K3 class is also impossible.            (11)

## 4. Conclusion

Every multiplicity-three target-K3 support D requires at least two external owner incidences in supports disjoint from D. Sections 2 and 3 eliminate respectively

- two or more distinct disjoint support classes;
- one distinct disjoint support class with repeated owner multiplicity.

These exhaust the possibilities.

Therefore the repeated-K3 multiplicity-three terminal is EMPTY under the correct far-K2 contract.

Combined with `Q36_F2_FAR_K2_C8_D2_A3_ONEEDGE_FULL_CLOSURE.md`, this proves:

> in `c=8, n2=1, A=3`, every surviving d3 support has multiplicity at most2.

No fixed 12-point remainder assumption is used anywhere in this proof.