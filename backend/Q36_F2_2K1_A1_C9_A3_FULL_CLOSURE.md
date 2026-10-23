# q36 f=2, 2K1 far, a_F=1 — full closure of c=9, allowance three

Status: `PROVED` under `Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md`, common-S row closure, CORE211, inherited D14, lexicographic q36 maximality, `alpha(F)<=4`, and `alpha(H[R])<=2`.

For c=9, Y consists of one inactive decorated vertex y and `nu_Y=0`. If A=3, the inactive identity gives `g_y=3`.

## 1. Multiplicity at least three is impossible

A repeated support using full defect3 would repivot to q36 while retaining y and inserting three decorated support vertices, raising tau from2 to at least4. Hence repeated supports have defect at most2.

### Multiplicity four

For r(D)=4, D14 gives

`O_D+e_F(y,D)+e_H(D)<=2`.

A repeated support cannot have a disjoint support unless D is a K3, but the K3 case is already impossible in the displayed cap because `e_H(D)=3`. Thus all remaining owner incidences would have to intersect D, giving O_D>=5, contradiction.

### Multiplicity three

For r(D)=3,

`O_D+e_F(y,D)+e_H(D)<=5`.

If D is nonclique, its defect-at-most-two cross allowance is at most1 (two-edge D) or0 (one-edge D). Any disjoint support requires at least3 D--E target edges to cover an internal nonedge, so no disjoint support exists. Six owner incidences remain, giving O_D>=6, contradiction.

If D is a K3, its cross allowance is at most2. A disjoint nonclique support again requires at least3 cross edges. A disjoint K3 with at most two cross edges gives the standard six-point w-mass contradiction. Thus again O_D>=6, while the D14 inequality gives O_D<=2. Contradiction.

Hence every support multiplicity is at most2.                    (1)

## 2. No repeated support exists

Let D have multiplicity2. Its defect is at most2.

As above, a nonclique D cannot have a disjoint support: a one-edge D has cross allowance0, a two-edge D has allowance at most1, while an internal nonedge forces at least3 D--E target edges.

If D is a K3, a disjoint nonclique support requires at least3 cross edges while the allowance is at most2; a disjoint K3 is excluded by the six-point w-mass argument.

Therefore all seven remaining owner incidences meet D, so

`O_D>=7`.                                                   (2)

For r(D)=2, D14 gives

`O_D+e_F(y,D)+e_H(D)<=8`.                                  (3)

If D is nonclique, the inactive vertex y must meet every internal target-nonedge of D; otherwise `{a,b,y,u,v}` is an independent5-set. Hence `e_F(y,D)>=1`. Together with (2) and `e_H(D)>=1`, the left side of (3) is at least9, contradiction.

If D is a K3, (2) and `e_H(D)=3` already give at least10, contradiction.

Thus no repeated support exists. All nine supports are distinct singleton triples.       (4)

## 3. At most one singleton support can have q36

A q36 singleton support repivot retains the decorated vertex y. Since the old q36 shell has only two decorated vertices `{x0,y}`, the support can contain at most one globally decorated vertex; at least two of its vertices are clean private globally regular vertices.

If two q36 supports existed, choose clean private vertices u,v from them. Both are target-nonadjacent to y. If uv were a target nonedge, `{a,b,y,u,v}` would be an independent5-set, so uv must be a target edge. But row closure against one support forces the clean regular vertex from the other support to be target-anticomplete to it. Contradiction.

Hence at most one q36 support exists. At least eight supports have defect at most2.

Any defect-at-most-two support cannot be disjoint from another support, by the same one-edge/two-edge/K3 analysis used above. Therefore all nine supports are pairwise intersecting.

If D were the unique q36 support, all eight intersections with low-charge supports must use D's unique possible decorated support vertex z. Each proper overlap costs2 and the low support has defect at most2, so overlap equality forces `w_z=kappa_z+e_F(z,x0)=0`. The other two vertices of D are clean regular and also have w=0. Hence D's defect is only its internal missing count, at most2 because `alpha(H[R])<=2`, contradicting full defect3.

Thus every support has q<=35. Since the supports are pairwise intersecting, proper overlap costs2, so every support has defect exactly2 and every shared support vertex has w=0.         (5)

## 4. No support can be nonclique

Suppose D is nonclique. Any shared vertex s outside D has w_s=0, so row closure makes s target-anticomplete to D, and a target-nonedge pair inside D together with s forms an independent triple. Therefore every globally shared vertex lies inside D. Let S be the shared set, `1<=|S|<=3`.

All nine supports are pairwise intersecting.

### |S|=1

All nine supports contain one shared point. The other18 support incidences are private, requiring19 vertices in total, impossible in |R|=12.

### |S|=2

Pairwise intersection forces one point a to lie in all nine supports. Let the other shared point b have multiplicity k>=2. Private incidences number `27-(9+k)=18-k`; the 12-point capacity gives `2+18-k<=12`, hence k>=8.

A nonclique support containing a,b and one private point has incidence `lambda(D)=9+k+1=10+k`. The inactive vertex y must meet an internal nonedge, so `e_F(y,D)>=1`, and `e_H(D)>=1`. D14 gives

`10+k+1+1<=14`,

hence k<=2, contradiction.

### |S|=3

Then the nonclique support D equals S. The 12-point capacity gives

`3 + (27-lambda(D)) <=12`,

so `lambda(D)>=18`.

But D14 with `e_F(y,D)>=1` and `e_H(D)>=1` gives `lambda(D)<=12`. Contradiction.

Therefore every support is a target K3.                           (6)

## 5. Nine K3 singleton supports are impossible

Each support has defect exactly2. Shared vertices have w=0, so every support has private vertices carrying total positive w-mass2.

For each support let S_D be its set of shared vertices. Then `|S_D|<=2`, and the S_D are pairwise intersecting.

If the S_D have no common point, they are the edges of a triangle. Every support then has exactly two shared vertices and one private vertex with w=2. Since `e_F(v,x0)<=1`, each private vertex has `kappa_v>=1`. Nine distinct private vertices force total core excess at least9, contradicting CORE211.

If all S_D share a common point z, let k be the number of supports with a second shared vertex. Such a support has one private vertex with w=2 and hence kappa>=1, so k<=2. The number of private vertices is

`2(9-k)+k=18-k>=16`.

Together with z this exceeds the 12 vertices of R.

Contradiction.

## 6. Conclusion

No c=9,A=3 state exists:

> `c=9, A=3` is EMPTY.