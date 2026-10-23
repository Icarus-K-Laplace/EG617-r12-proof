# q36 f=2, 2K1 far, a_F=1 — closure of the c=7,A=3 owner partition 3+2+2

Status: `PROVED` under `Q36_F2_2K1_A1_C7_A3_MULTIPLICITY_RIGIDITY.md`, row closure, CORE211, the K11/D14 cap, and `alpha(H[R])<=2`.

Assume seven owners are split among three support classes D,E,F with multiplicities 3,2,2.

## 1. The multiplicity-three support cannot be a target K3

By multiplicity rigidity, if D is a target K3 then its weighted overlap budget is at most2.

A repeated support disjoint from D is impossible:

- if the repeated support is nonclique, its defect<=2 leaves common-S cross allowance at most1 (two internal target edges) or0 (one internal target edge), but every vertex of the target K3 D must hit an endpoint of an internal nonedge of the other support, requiring at least3 cross edges;
- if the repeated support is itself a target K3, the two disjoint K3 blocks have at most2 target cross edges. For each vertex v in the six-point complement L, avoiding an independent triple with one vertex from each K3 forces `e(v,D)+e(v,E)>=3`. Row closure with `w_v=kappa_v+e_F(v,x0)` then gives `w_v>=2`, so `sum_L w_v>=12`, whereas CORE211 and |L|=6 give `sum_L w_v<=2+6=8`.

Therefore every repeated support other than D must meet D.

But each multiplicity-two support meeting D in one point contributes2 to D's weighted overlap. Two such supports would contribute at least4, exceeding the K3 overlap budget2. Thus D cannot be a target K3.

## 2. D is the exact one-edge equality support

Multiplicity rigidity therefore forces the other exact form:

- `e_H(D)=1`;
- `kappa(D)=0`;
- `e_F(x0,D)=0`;
- `e_F(Y,D)=0`;
- weighted overlap `O_D=4`.

Hence E and F must each meet D in exactly one vertex. In particular their proper-overlap cost is2, so because they are repeated their defect is exactly2 and their repivot charge is q=35.

## 3. E and F must be target K3s

Consider E. Let z be its unique intersection point with D and let u,v be the two vertices of E outside D.

The point z lies in D, so `kappa_z=e_F(x0,z)=0`.

For each external petal u, row closure against D gives

`e_H(u,D)<=kappa_u+e_F(u,x0)`.

Because D spans exactly one target edge, it has two target nonedges. To avoid an independent triple consisting of u and a target-nonedge pair of D, u must cover both missing pairs. The minimum target degree from u into D is therefore1. The same holds for v.

The total E-defect equals2:

`kappa(E)+m(E)+e_F(x0,E)=2`.

The shared point z contributes zero to `kappa+e(x0,.)`, so the two petals together require at least two units of `kappa+e(x0,.)`. Hence `m(E)=0` and equality is forced on the two petals.

Therefore H[E]=K3. The same argument gives H[F]=K3.

## 4. E and F cannot be disjoint

If E and F were disjoint, their intersections with D would be two distinct points. Hence the third point r of D lies outside E union F.

Since r belongs to D, it has

`kappa_r=e_F(r,x0)=0`.

But E and F are target K3s, and their common-S cross allowance is at most2. Thus the target-nonedge bipartite graph between E and F is K3,3 with at most two edges removed and has minimum vertex-cover size3.

To avoid an independent triple with r and one point from each of E,F, r would need

`e_H(r,E)+e_H(r,F)>=3`.

Row closure for E and F gives both cuts at most

`kappa_r+e_F(r,x0)=0`,

contradiction.

Therefore E and F intersect.

## 5. E and F cannot intersect in two points

If `|E intersect F|=2`, the K11/D14 incidence cap applied to E gives

- 6 owner incidences from the two E-owners;
- 3 additional incidences from the multiplicity-three class D through the one D-intersection;
- 4 additional incidences from the two F-owners through the two E-F intersections;
- 3 internal target edges because E=K3.

Thus

`lambda(E)+e_H(E)>=6+3+4+3=16>14`,

contradiction.

Hence `|E intersect F|=1`.

## 6. The one-point intersection is impossible

### Case 1: E and F share their D-intersection point

Let z be the common point in D. The other two points of D lie outside E union F and have zero weight `kappa+e(x0,.)`.

If z were one endpoint of the unique target edge of D, then the isolated D-vertex together with the other edge endpoint forms a target-nonedge pair. Either zero-weight outside D-point is target-anticomplete to E by row closure, producing an independent triple with an appropriate E-point. Hence the only possible common point is the isolated vertex z of the one-edge triple D.

Then the other two D-vertices a,b form the unique target edge of D and are target-anticomplete to both E and F by row closure.

For alpha(H[R])<=2, every petal of E must be target-adjacent to every petal of F; otherwise a,b are not needed—already a petal nonedge together with a (which is anticomplete to both blocks) would be an independent triple.

Thus the two E-petals are target-complete to the two F-petals.

But for an E-petal u, its exact defect equality gives `kappa_u+e_F(u,x0)=1`. Row closure against F therefore gives

`e_H(u,F)<=1`.

Since u is already target-adjacent to the shared point z inside F, it cannot also be adjacent to both F-petals. Contradiction.

### Case 2: E and F intersect outside D

Their intersections with D are then distinct points. Let r be the third point of D, outside E union F. Again `kappa_r=e_F(r,x0)=0`, so row closure makes r target-anticomplete to both E and F.

To avoid an independent triple containing r, every vertex of E outside the shared E-F point must be target-adjacent to every vertex of F outside that shared point.

Take an E-vertex u outside F. Its exact equality gives `kappa_u+e_F(u,x0)=1`. Row closure against F allows at most one target edge from u into F. But u is target-adjacent to the shared point because E is a target K3, and alpha-two requires target edges from u to both F-exclusive vertices. This requires at least three edges into F, contradiction.

Thus the one-point intersection is impossible as well.

## 7. Conclusion

Every possible geometry of the partition 3+2+2 is impossible. Therefore

> `c=7, A=3, owner partition 3+2+2` is EMPTY.

Together with the preceding rigidity theorem, the remaining allowance-three partitions are `3+2+1+1`, `3+1+1+1+1`, and partitions with maximum multiplicity at most2.