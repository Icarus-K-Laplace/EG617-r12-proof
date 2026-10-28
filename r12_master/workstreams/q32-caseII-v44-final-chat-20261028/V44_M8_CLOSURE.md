# E408 Q32 Case-II — v=44,m=8 complete closure

Date: 2026-10-28
Status: **CLOSED / PROVED_CONDITIONAL** under the registered E408-Q32 contract and the source-correct Type-I / 130-edge extremal inputs.

This file closes all three m=8 W-multiplicity partitions

`(2,2,2)`, `(3,2,2)`, `(3,3,2)`.

The central new input is `V44_M8_PAIR_RIGIDITY.md`.

## 1. Core-only degree-four color sets on W

For `w in W`, define

`L(w)={D among the three 130-edge nonexact colors : d_D(w)=4 and N_D(w) subset H}`.

The W-pair rigidity theorem proves:

> if `D in L(u) cap L(v)` for distinct W-points u,v, then edge uv has color D.

Hence

> `|L(u) cap L(v)|<=1`.

### 1.1 n_w=2 gives |L(w)|>=2

At an n=2 W-point, `V44_M8_NORMAL_FORM.md` proves:

- the six non-special exact colors own exactly twelve shell edges;
- one special exact color owns the thirteenth shell edge;
- the other special exact color has zero shell degree and owns pw;
- therefore no 130-edge nonexact color owns an edge from w to `O={p} union A`.

The special parameter pair is `(4,4)` or `(4,3)`.

- For `(4,3)`, all three pointwise slack units are consumed by the special exact colors, so all three nonexact colors have degree4.
- For `(4,4)`, only one slack unit remains, so at most one of the three nonexact colors can have degree greater than4.

Thus at least two nonexact colors have degree4, and all of their neighbors lie in H:

> **`|L(w)|>=2` at every n=2 W-point.**

### 1.2 n_w=3 gives |L(w)|>=2

At an n=3 W-point, the special parameters are `(4,4,4)`. Their three special-excess units consume all pointwise slack. Hence

- target degree is exactly13;
- all five non-special exact colors have degree4;
- all three 130-edge nonexact colors have degree4.

The five non-special exact colors each use at least two shell edges, hence at least ten shell edges total.

Among the three special exact colors, at most one can have zero shell degree by the zero-shell special-edge obstruction. Therefore at least two special exact colors use shell edges. Thus exact colors own at least twelve shell edges.

If one special exact color has zero shell degree, it also owns pw, so exact colors own at least thirteen of the fourteen edges from w to O. If none has zero shell degree, all three special colors use shell edges and exact colors own at least thirteen shell edges, again at least thirteen O-edges.

Therefore at most one edge from w to O can belong to a nonexact color. Since the three nonexact colors all have degree4, at least two have all four neighbors in H:

> **`|L(w)|>=2` at every n=3 W-point.**

## 2. Universal consequence: all three W--W edges are nonexact

Every m=8 multiplicity partition has three W-points, and by Section1 each has an L-set of size at least2 inside the same three-element set of 130-edge colors.

Any two size-at-least-two subsets of a three-element set intersect. Hence for every pair `u,v in W`, choose

`D in L(u) cap L(v)`.

W-pair rigidity forces uv to have color D.

Therefore

> **all three edges of H[W] are nonexact 130-color edges.**

In particular

`e_H(W)=0`.

## 3. Close multiplicity (2,2,2)

Here only six exact colors have their special point in W, so two exact colors have special point outside W.

Consider any exact color C with `x_C notin W`.

- If `x_C in O`, the remaining thirteen O-points occupy the twelve factor K5s. Hence there is exactly one double-outside factor and eleven single-outside factors. All three W-points are non-special and cannot lie in single-outside factors, so all three lie in that unique double-outside factor. Thus C owns all three W--W edges.
- If `x_C in U`, all three W-points are again non-special. A triple-type placement has only one multi-outside factor with two core slots and cannot contain all three W-points. Hence C is double type with two multi-outside factors. Three W-points distributed over two factors force two W-points into the same factor, so C owns at least one W--W edge.

Either way C must own a W--W edge, contradicting Section2.

Thus

> **`(2,2,2)` is impossible.**

## 4. Close multiplicity (3,2,2)

Here seven exact colors are special on W and one exact color C has `x_C notin W`.

The same argument as Section3 shows that this outside-W special exact color C must own at least one W--W edge.

Section2 says all three W--W edges are nonexact.

Contradiction. Hence

> **`(3,2,2)` is impossible.**

## 5. Reduce multiplicity (3,3,2)

Now all eight exact colors have special point on W. Let `w_0` be the unique n=2 W-point and `w_1,w_2` the two n=3 W-points.

Section2 says all W--W edges are nonexact.

### 5.1 The n=2 point has profile (4,4) and |L(w_0)|=2

If the n=2 parameter profile were `(4,3)`, all three nonexact colors would have degree4 and all their neighbors would lie in H, so `|L(w_0)|=3`.

But `|L(w_i)|>=2` at either n=3 point. Then

`|L(w_0) cap L(w_i)|>=2`,

and pair rigidity would force the single edge `w_0 w_i` to have two distinct colors, impossible.

Therefore the n=2 profile is `(4,4)`.

The same intersection argument also rules out `|L(w_0)|=3`. Hence

> `|L(w_0)|=2`.

Only one pointwise slack unit remains after the two special exact colors. Since exactly one nonexact color is not degree4/core-only, that unit is consumed by that nonexact color. Consequently at w_0:

- target degree is exactly13;
- all six non-special exact colors have degree4;
- nonexact degrees are `4,4,5`;
- the target shell degree is zero, so `d_H(w_0)=13` and the core excess is `epsilon_{w_0}=1`.

### 5.2 Each n=3 point has |L|=2 and core excess one

If `|L(w_i)|=3`, then its intersection with the two-element set `L(w_0)` has size2, again giving two colors to edge `w_0w_i`. Hence

> `|L(w_1)|=|L(w_2)|=2`.

All three nonexact colors have degree4 at an n=3 point, so exactly one nonexact color has an O-neighbor there.

The target degree is13 and `epsilon_w+r_A(w)=1`.

Suppose `r_A(w)=1`. Exact colors already own at least thirteen O-edges as in Section1.2, while one nonexact color owns an O-edge and the target owns one shell edge. That would require at least fifteen owners among the fourteen O-edges, impossible.

Thus

`r_A(w)=0`, `epsilon_w=1`

at both n=3 points.

Therefore all three W-points have core excess exactly one. Since the total core excess in H is six,

> `E_U=3`.

Together with `e_H(W)=0`, the exact v=44 core identity gives

> `e(bar(H[U])) = 703-E_U-e_H(W)=700`.

## 6. Every exact color is a=4, double type, with its two double factors ordinary

The two n=3 points have special profile `(4,4,4)`, and the n=2 point has profile `(4,4)`. Since these special labels account for all eight exact colors,

> **every exact color has source parameter `a=4`.**

Fix an exact color C, special at one W-point. Its other two W-points are non-special.

Because all W--W edges are nonexact, those two W-points cannot lie in the same factor K5 of C.

If C were triple type, its unique multi-outside factor would have to contain both non-special W-points, forcing their W--W edge to have color C. Impossible.

Hence C is double type, and its two non-special W-points lie in its two distinct double-outside factors.

At every W-point all non-special exact colors have degree4: this is automatic at n=3, and was proved in Section5.1 at n=2.

In the source-correct Type-I exact graph, the degree-four vertices are exactly the vertices in the ten isolated K5 components; every gadget vertex has degree at least5. Therefore each non-special W-point lies in an isolated K5 component.

Thus for every exact color C:

- its two double-outside factors are two of the ten isolated K5s;
- each double factor has two O-points, one W-point, and two U-points;
- both special gadget factors `N_s,N_t` are single-outside factors.

## 7. Every exact color uses at least 65 U-edges

Fix an exact color C.

### 7.1 Factor edges

Its ten single-outside factor K5s each supply a registered core-four witness in U, hence contribute

`10*C(4,2)=60`

C-edges inside U.

Its two double-outside isolated K5s each contain exactly two U-points, hence contribute one U-edge each:

`+2`.

### 7.2 The source gadget contributes at least three additional U-edges

For `a=4`, let `P subset N_s` be the four-element source subset and `y in N_t` the source point. The source construction gives all cross edges

`y--P`

in the original non-target color C.

The factor `N_t` is single-outside and contains no W-point. If `y` were its unique outside point, then the four vertices of `N_t\{y}` would all lie in U and

`{x_C} union (N_t\{y})`

would be a C-colored K5 wholly inside H, contradicting `alpha(H)<=4`.

Therefore `y in U`.

Similarly, `N_s` is single-outside and contains no W-point, so four of its five vertices lie in U. Since `|P|=4`, at least three vertices of P lie in U.

Hence at least three of the cross edges `y--P` lie wholly in U. These are cross-part gadget edges and are not among the factor-internal edges counted above.

Therefore

> **`e_C(U)>=60+2+3=65`.**

Across eight exact colors this gives at least

`8*65=520`

non-target U-edges.

## 8. The U-pool is saturated

Each of the three nonexact colors satisfies the ordinary 44-vertex floor

`e_D(U)>=p_12(44)=60`.

Therefore all eleven non-target colors use at least

`520+3*60=700`

edges of `bar(H[U])`.

Section5.2 proved that this complement has exactly700 edges. Hence equality holds everywhere:

> every exact color has exactly65 U-edges;

> every nonexact color D has exactly60 U-edges.

For a 44-vertex graph with independence number at most12, equality in the ordinary Turan-complement bound `e=60` is unique up to part sizes: the complement is the balanced 12-partite Turan graph. Since `44=8*4+4*3`,

> **`D[U] = 8 K4 dot-union 4 K3`**

for every nonexact color D.

Thus every connected component of `D[U]` is a clique.

## 9. Final contradiction in (3,3,2)

The three sets `L(w_0),L(w_1),L(w_2)` all have size exactly2. Pair rigidity gives pairwise intersections of size at most1, while any two two-subsets of a three-set intersect. Thus the three L-sets are the three distinct two-subsets of the three nonexact colors.

Consequently every nonexact color D belongs to exactly two of the L-sets. Let u,v be those two W-points. Pair rigidity gives `uv` color D.

At u, the local degree-four theorem gives

`S=N_D(u)`, `D[S]=K4-e`.

The vertex v belongs to S. We claim v is not one of the two missing-pair endpoints of this K4-e.

If it were a missing endpoint, then in the five-vertex graph `{u} union S = K5-e`, v would have three D-neighbors inside this set and one external D-neighbor z, because its total D-degree is four. The two central vertices of S and u already have D-degree four entirely inside the K5-e, so z is D-nonadjacent to all three of them. Hence the four-neighbor set `N_D(v)` would induce only a triangle plus an isolated vertex, contradicting the same local theorem at v, which requires `D[N_D(v)]=K4-e` with five edges.

Therefore v is a central vertex of the K4-e. The five-vertex cluster then consists of

- the two W-points u,v;
- one further central vertex c in U;
- two missing-pair endpoints a,b in U.

Inside U we have

`ca in E(D)`, `cb in E(D)`, but `ab notin E(D)`.

This is impossible in `D[U]=8K4 dot-union 4K3`: since c is adjacent to both a and b, all three vertices must lie in the same clique component, which would force ab to be a D-edge.

Contradiction.

Hence

> **`(3,3,2)` is impossible.**

## 10. Conclusion

All m=8 multiplicity partitions are impossible:

- `(2,2,2)` — closed;
- `(3,2,2)` — closed;
- `(3,3,2)` — closed.

Therefore

> **Case II / |U|=44 / m=8 is CLOSED.**

Combined with the already proved m=9 closure in this workstream and the inherited m=10 exclusion, there is no Case-II Q32 realization with `|U|=44`.

## 11. External theorem and verifier scope

External inputs:

1. source-audited Kang--Pikhurko Type-I equality factorization for exact129 colors;
2. Kang--Pikhurko Theorems 1 and4 at `(56,11)` through `V44_M8_PAIR_RIGIDITY.md`;
3. the already proved 130-edge minimum-degree-four theorem;
4. ordinary Turan equality at 44 vertices for the final `e_D(U)=60` structure.

No SAT/ILP nonexistence certificate is used or claimed. The closure is analytic. Finite arithmetic is limited to the three multiplicity partitions and the displayed exact edge sums.