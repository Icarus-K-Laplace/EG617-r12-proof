# Global d=3 A2 M=6, b=1 Full Closure

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_A2_TWO_BLOCK_INCIDENCE_BUDGET.md`;
- zero-charge incidence-signature theorem;
- common-S row closure and overlap saturation;
- `alpha(H)<=3`;
- CORE211 / fully-decorated q32 charge ledger `W<=36`.

Purpose: close the bridge-one equality window of the final nine-owner fully-decorated q32 d3 state without attachment enumeration.

## 1. Equality setup

Let D,E be a maximal disjoint support pair with

`m_D+m_E=M=6`,

and suppose exactly one owner lies on a bridge support meeting both D and E:

`b=1`.

The two-block incidence budget gives

`2M+b+e_H(D union E)<=17`,

hence

> `e_H(D union E)<=4`.                                       (B1)

Every allowance-two 3-support has at least one internal target edge.

## 2. The pair D,E is uniquely one-edge plus K3

If D has one internal target edge, then its missing-edge defect is2, so its common-S charge is zero. Row closure then gives

`e_H(D,E)=0`.

If E had at most two internal target edges, each support would contain an internal target-nonedge pair, and because the supports are target-anticomplete those two pairs would form an independent4-set.

Hence E must be a target K3.

Conversely, if both D and E had at least two internal target edges, their internal edge total would already be at least4. Equality in (B1) would force zero cross edges. Two P3 supports would then have internal nonedge pairs forming an independent4-set; any K3 among them pushes the total internal edge count above4.

Therefore, up to exchange,

> D is a one-edge support,
> E is a target K3,
> and `e_H(D,E)=0`.                                          (B2)

Write

`D={a,b,c}`

with unique target edge ab; c is isolated in H[D].

Since D has defect2 at allowance2,

> every point of D has common-S charge zero.                 (B3)

The target edge ab and zero-signature theorem imply

> a and b have the same support-incidence signature.         (B4)

## 3. The unique bridge is an exact P3 through c and the unique zero vertex of E

The global two-block inequality is saturated:

`12+1+4=17`.

Hence all lower bounds used to derive it are equalities.

In particular:

- the bridge owner support meets D union E in exactly two points, one in each block;
- each of the remaining two side-owner supports meets D union E in exactly one point;
- there are no omitted r--(D union E) target edges.

Any proper support-overlap point at allowance2 must have common-S charge zero.

The bridge cannot meet D at a or b alone: by (B4), every support containing one of a,b contains the other. Hence it must meet D at c.

Let e be its unique point in E. Then e must have zero charge.

If E had a second zero-charge vertex, that vertex would be target-adjacent to e inside the K3 and therefore have the same incidence signature, forcing the bridge to contain both. Hence e is the unique zero-charge point of E.

Thus the other two E-vertices have positive integer charge. Since E has total support defect at most2 and is a K3, they both have charge1:

> E has charge distribution `(0,1,1)`.                       (B5)

Let the bridge be

`F={c,e,z}`.

The points c,e are target-nonadjacent because D--E is target-anticomplete. Proper overlap with both D and E forces F to have exact defect2. If z had charge0, all three points would be distinct zero-signature vertices, so no internal target edge would be possible, contradicting defect<=2. If z had charge2, F would have to be a K3, impossible because ce is a nonedge.

Therefore

> `w_z=1`,
> F is the two-edge path with center z,
> edges zc and ze.                                           (B6)

## 4. Every one-sided support is H-type K3

Consider a remaining side support meeting D only in c. Write

`R={c,u,v}`.

Proper overlap forces exact defect2 and the hub c is zero-charge.

If one private point, say u, also had zero charge, then cu is a target nonedge by distinct signatures. The other private point v must have charge1 and be adjacent to both c and u; this is the only possible Z-type P3 geometry.

But zero-charge u lies outside D and E, so row closure makes u target-anticomplete to both D and E. The vertex c is isolated from a,b inside D and D--E is target-anticomplete. Thus, for any e' in E,

`{c,u,a,e'}`

is an independent4-set, contradiction.

Hence both private points have charge1 and R is a target K3.

So every D-side support is an H-type K3 with hub c and two unit-charge private petals.

The same argument on the E side shows that every E-side support is an H-type K3 with hub e and two unit-charge private petals.             (B7)

## 5. The two side-owner supports must be the same support class

First suppose the two side owners use distinct supports on the same side, say

`R_1={c,u_1,v_1}`,
`R_2={c,u_2,v_2}`.

Type-H row closure makes the two private petal pairs target-anticomplete.

Also the zero vertex e is target-anticomplete to both R_i outside their hub, and each private petal has its unit allowance already consumed by the edge to c, so it is target-nonadjacent to a and b.

Choosing one private petal from each R_i and adding e and a gives an independent4-set.

Hence two distinct same-side classes are impossible.

Now suppose one side support is c-based and the other e-based:

`R_c={c,u,v}`, `R_e={e,x,y}`.

All private petals have charge1. The bipartite target graphs

- `{a,b}`--`{x,y}`,
- `{f,g}`--`{u,v}` where `E={e,f,g}`,
- `{u,v}`--`{x,y}`

are matchings: for each private petal, row closure allows at most one target edge into the corresponding opposite support, while the zero opposite hub contributes none.

Choose one vertex successively from the four 2-sets

`{a,b}`, `{x,y}`, `{u,v}`, `{f,g}`

along the path

`{a,b} -- {x,y} -- {u,v} -- {f,g}`.

Because every bipartite graph on each consecutive pair is a matching, after each choice at least one vertex remains nonadjacent to the previous choice. Nonconsecutive pair graphs are target-empty by the already established row-closure relations and D--E anticompleteness.

This yields an independent4-set, contradiction.

Therefore the two remaining side owners must use one and the same H-type K3 support class R, of multiplicity2, based either at c or at e.      (B8)

## 6. The support union has total charge five

The support-union vertices consist of

- D, charge0;
- E, total charge2;
- the bridge private center z, charge1;
- the two private petals of R, total charge2.

Thus

> `W_U=5`.                                                     (B9)

The total common-S charge in the fully-decorated q32 state is

`W=34+e_M(S)<=36`.

Hence the 26 core vertices outside this nine-point support union carry total charge at most

> `W-W_U<=31`.                                                (B10)

The support union contains the independent triple `{c,a,e}`. Any outside zero-charge vertex is outside every support and hence target-anticomplete to the whole support union by row closure. It would extend this triple to an independent4-set.

Therefore every outside vertex has charge at least1.

With 26 outside vertices and total charge at most31, at most five can have charge at least2. Consequently

> at least21 outside vertices have charge exactly1.          (B11)

## 7. Every outside charge-one vertex must be adjacent to e

Let x be an outside core vertex with `w_x=1`.

Suppose xe is a target nonedge.

Row closure gives at most one x-neighbour in D and at most one in E.

### If x is not adjacent to c

Then among the one-edge support D there is an internal target-nonedge pair of x-nonneighbours containing c: if x sees a choose `{c,b}`, if x sees b choose `{c,a}`, and if x sees neither choose either pair.

Because xe is a nonedge, the pair together with e and x forms an independent4-set (D--E is target-empty), contradiction.

### If x is adjacent to c

Then c consumes x's full row-closure allowance into D, so xa=xb=0. The bridge support `{c,e,z}` also contains c; row closure therefore gives xz=0 as well as xe=0.

If R is c-based, the edge xc similarly consumes the allowance into R, so x is nonadjacent to both private petals of R. Since e is zero-charge and lies outside R, e is also nonadjacent to those petals. Pick one petal u. Then

`{x,e,u,a}`

is independent.

If R is e-based, choose a private petal u of R target-nonadjacent to x (at least one exists because x has allowance1 into R and xe=0). The petal u already sees e in the original K3 E, so row closure against E makes u target-nonadjacent to f and g. Choose f in {f,g} target-nonadjacent to x; such an f exists because x has at most one neighbour in E and xe=0. Finally choose a in {a,b} target-nonadjacent to u; u has at most one target neighbour in D and uc=0, so one exists, and x is nonadjacent to both a,b because xc is its unique D-neighbour. Then

`{x,u,f,a}`

is independent.

Every possibility contradicts alpha(H)<=3.

Therefore

> every outside charge-one vertex is target-adjacent to e.    (B12)

## 8. Degree capacity contradiction

The unique zero vertex e of the K3 E has core degree12.

It already has the two internal E-neighbours and the bridge center z as core neighbours.

If the repeated side support R is e-based, e additionally has its two private petals as neighbours.

Hence e has at most

- 9 remaining core-neighbour slots if R is c-based;
- 7 remaining slots if R is e-based.

But (B11)--(B12) require e to be adjacent to at least21 distinct outside charge-one vertices.

Contradiction.

Therefore

> **M=6,b=1 is impossible.**                                 (B13)

## 9. Consequence

In the final nine-owner fully-decorated q32 d3 equality state, a maximal disjoint pair with total multiplicity6 cannot have bridge multiplicity1.

Together with `GLOBAL_D3_A2_M6_PAIR_GEOMETRY_REDUCTION.md`, the only M=6 window still requiring closure is the b=0 Type-C P3-plus-K3 geometry, which has already been bridged to at least14 high-decoration one-spoke pivots.
