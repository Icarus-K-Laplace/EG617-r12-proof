# q36 f=2, 2K1 far, a_F=1 — c=7 allowance-three multiplicity rigidity

Status: `PROVED REDUCTION` under `Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md`, the K11/D14 incidence cap, common-S row closure, CORE211, lexicographic q36 maximality, and `alpha(H[R])<=2`.

Setup: c=7, A=3, inactive set Y is a target K3 with decorations (1,1,1), and `{p} union C union Y` is a target K11. Seven low owners have common missing triple `S=F union {x0}` and 3-point core supports in the 12-point remainder R.

For a distinct support D let r(D) be its owner multiplicity. Let

`O_D=sum_(E!=D) r(E)*|D intersect E|`.

Then the K11/D14 cap applied to T=D gives

`3 r(D)+O_D+e_F(Y,D)+e_H(D)<=14`.                         (1)

Every repeated support has defect at most2: full defect3 would repivot to q36 while inserting three decorated support vertices and retaining the three inactive decorated vertices Y, increasing tau.

## 1. Multiplicity four is impossible

Assume r(D)=4. Equation (1) gives

`O_D+e_F(Y,D)+e_H(D)<=2`.                                 (2)

Because alpha(H[R])<=2, `e_H(D)>=1`.

### O_D=0

Then D is disjoint from every other support.

If `e_H(D)=1`, D has two target nonedges and its support defect bound2 forces

`kappa(D)=0`, `e_F(x0,D)=0`.

Thus its common-S cross allowance is zero. Any other disjoint support E is target-anticomplete to D. Taking a target-nonedge pair in D and any vertex of E gives an independent triple, contradiction.

If `e_H(D)=2`, D has one target nonedge. Equation (2) forces `e_F(Y,D)=0`, while defect<=2 gives

`kappa(D)+e_F(x0,D)<=1`.

Hence for any disjoint support E the joint-row theorem gives `e_H(D,E)<=1`. But every one of the three vertices of E must be adjacent to at least one endpoint of the unique target-nonedge of D, otherwise that vertex and the nonedge pair form an independent triple. Therefore `e_H(D,E)>=3`, contradiction.

The case `e_H(D)=3` is impossible already in (2).

### O_D>0

Equation (2) forces exactly

`O_D=1`, `e_F(Y,D)=0`, `e_H(D)=1`.

Thus only one singleton owner support can meet D, in one vertex. The other two owners not in the multiplicity-four class must belong to supports disjoint from D. As above, one-edge D has zero common-S cross allowance, so any such disjoint support yields an independent triple.

Therefore

> no support has multiplicity4.                              (3)

Hence every support multiplicity is at most3.

## 2. Multiplicity-three dichotomy

Let r(D)=3. Equation (1) becomes

`O_D+e_F(Y,D)+e_H(D)<=5`.                                 (4)

Repeated-support defect<=2 gives

`kappa(D)+m(D)+e_F(x0,D)<=2`,

where `m(D)=3-e_H(D)`.

### e_H(D)=2 is impossible

Here m(D)=1, so the common-S cross allowance

`u_D=kappa(D)+e_F(x0,D)<=1`.

If any other support E were disjoint from D, the unique target nonedge in D would force each of the three E-vertices to meet one of its endpoints, so `e_H(D,E)>=3`, contradicting `e_H(D,E)<=u_D<=1`.

Thus all four remaining owner incidences must come from supports intersecting D, so `O_D>=4`. But (4) with `e_H(D)=2` gives `O_D<=3`. Contradiction.

### e_H(D)=1: exact all-overlap state

Now m(D)=2, so defect<=2 forces

`kappa(D)=0`, `e_F(x0,D)=0`.

Any disjoint support would have zero target cross-edge to D by row closure and would form an independent triple with a target-nonedge pair of D. Hence every remaining owner support intersects D, so `O_D>=4`.

Equation (4) gives `O_D+e_F(Y,D)<=4`. Equality is forced:

> `O_D=4`, `e_F(Y,D)=0`.                                  (5)

Thus all four remaining owner incidences meet D exactly once in weighted total.

### e_H(D)=3: clique state

Here D is a target K3. Equation (4) gives

> `O_D+e_F(Y,D)<=2`.                                       (6)

So at least two of the four remaining owner incidences belong to supports disjoint from D.

Therefore every multiplicity-three support is exactly one of:

- a target K3 with weighted overlap at most2; or
- a one-edge equality triple with zero core excess, zero x0-incidence, zero Y-incidence, and weighted overlap exactly4.

## 3. The owner partition 3+3+1 is impossible

Suppose two support classes D,E have multiplicity3.

If D is a target K3, then (6) forbids intersection with E: an intersection of size1 already contributes multiplicity3 to O_D. Hence D and E are disjoint.

If E is nonclique, its defect<=2 gives common-S cross allowance at most1 (two-edge E) or0 (one-edge E), while alpha(H[R]) forces at least three cross edges from the clique D to cover an internal nonedge of E. Contradiction.

If E is also a target K3, then `e_H(D,E)<=2`. Put `L=R\(D union E)`, |L|=6. For every v in L, avoiding an independent triple with one vertex from D and one from E requires the neighbourhood of v in D union E to cover the target-nonedge graph `K3,3` with at most two edges removed. Its minimum vertex-cover size is3. Hence

`e_H(v,D)+e_H(v,E)>=3`.

With `w_v=kappa_v+e_F(v,x0)`, row closure gives each cut at most w_v, so w_v>=2. Thus `sum_L w_v>=12`, while CORE211 and |L|=6 give

`sum_L w_v<=kappa(L)+e_F(x0,L)<=2+6=8`,

contradiction.

It remains that D is a one-edge equality triple. Then every other owner support must intersect D by (5), so E intersects D. Symmetrically, if E were a target K3 its overlap budget (6) would be exceeded by the three owners of D. Hence E is also a one-edge equality triple and the two supports meet in exactly one vertex.

For both D and E, (5) gives zero core excess and zero x0-incidence on every support vertex. Let v be one of the two vertices of E outside D. Row closure against D gives

`e_H(v,D)<=kappa_v+e_F(v,x0)=0`.

But D has a target-nonedge pair, so v together with that pair is an independent triple in H[R], contradiction.

Therefore

> the partition `3+3+1` is impossible.                      (7)

## 4. New c=7,A=3 interface

The allowance-three terminal now satisfies:

- every support multiplicity is at most3;
- multiplicity-three supports have only the two exact forms above;
- owner partition `3+3+1` is impossible.

The next unresolved multiplicity partitions begin with `3+2+2`, `3+2+1+1`, and partitions with maximum multiplicity2.