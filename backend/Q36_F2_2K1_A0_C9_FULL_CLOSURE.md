# q36 f=2, 2K1 far, a_F=0 — full closure of the c=9 single-class terminal

Status: `PROVED` under `Q36_F2_2K1_A0_HIGH_C_SINGLE_CLASS_NORMAL_FORM.md`, row closure, CORE211, inherited D14, and `alpha(H[R])<=2`.

This closes the c=9 all-d3 / single missing-vertex branch.

## 1. Exact c=9 support form

By the high-c normal form:

- `R` has 11 vertices and `alpha(H[R])<=2`;
- `x` has exactly one non-neighbour `z` in R;
- every one of the nine low supports has the form
  `D={z,u,v}`
  with `u,v in N_H(x) intersect R`;
- every support class has multiplicity at most2;
- every support has `q<=35` and `kappa(D)+m(D)<=2`.

If a support class has multiplicity2, the D14 inequality is saturated. Hence

- all three vertices of D have core excess0;
- `m(D)=2`, so H[D] has exactly one target edge;
- the two petals u,v have no shell owners outside the two owners of this support class and x.

In particular the two petals of a repeated class occur in no other support class.

## 2. There is at most one repeated support class

Assume D={z,p,q} and E={z,r,s} are two distinct repeated classes.

Both triples have exactly one target edge and every vertex in them has core excess0.

Consider the isolated vertex of the one-edge triple D.

### Case 1: z is isolated in D

Then pq is the unique target edge of D.

For r, row closure against D gives

`e_H(r,D)<=kappa_r+e_F(r,F union {x})=1`.

Since H[D] has one edge and `alpha(H[R])<=2`, r must be adjacent to the isolated vertex z; otherwise avoiding independent triples with the two D-nonedges would require adjacency to both p and q, contradicting the row-closure bound1.

The same applies to s. Thus both r and s are adjacent to z, so E has at least two internal target edges, contradicting the one-edge equality for E.

### Case 2: a petal, say q, is isolated in D

Then zp is the unique target edge.

The same row-closure/independence argument forces each of r,s to be adjacent to q. Hence q has two target edges into E.

But q lies outside E, has `kappa_q=0`, and is adjacent to x but to neither far vertex. Row closure against E gives

`e_H(q,E)<=1`,

contradiction.

Therefore

> at most one c=9 support class has multiplicity2.          (1)

## 3. The singleton petal graph

Remove the two exclusive petals of the unique repeated class if it exists. Define a simple graph B on the remaining petal vertices:

- vertices are the available petals;
- an edge uv represents a singleton support `{z,u,v}`.

If there is no repeated class, B has 10 vertices and 9 edges.
If there is one repeated class, B has 8 vertices and 7 edges.
Thus in both cases

> `|E(B)|=|V(B)|-1`.                                       (2)

For a petal u let `d_B(u)` be its degree in B. Its old shell neighbours include x and exactly the singleton owners represented by incident B-edges, so its global decoration is at least `d_B(u)`.

For a singleton support D={z,u,v}, repivoting its owner retains the one other old decorated shell vertex. The common vertex z is adjacent to all nine low owners and therefore has decoration at least8. Hence

`G_D' >= 1+8+d_B(u)+d_B(v)`.

Since the support has q<=35, D14 gives `G_D'<=13`. Therefore

> `d_B(u)+d_B(v)<=4` for every edge uv of B.                (3)

## 4. Saturated support edges

Call an edge uv of B saturated if

`d_B(u)+d_B(v)=4`.

For its support D={z,u,v}, the preceding D14 inequality gives

`e_H(D)<=1` after cancellation with the exact q-charge bound. But `alpha(H[R])<=2` forces every 3-set to contain a target edge. Thus

> every saturated support triple has exactly one target edge. (4)

The same equality forces

`kappa_z=kappa_u=kappa_v=0`.                                (5)

## 5. Two disjoint saturated edges are impossible

Let `uv` and `rs` be disjoint saturated B-edges, with support triples

`D={z,u,v}`, `E={z,r,s}`.

Both are one-edge triples and all six petal/core vertices involved have zero core excess.

For any zero-excess petal w outside D, row closure gives

`e_H(w,D)<=1`.

Because D has exactly one target edge and `alpha(H[R])<=2`, w must be adjacent to the isolated vertex of D; otherwise it would have to be adjacent to both endpoints of the unique D-edge, requiring two edges into D.

Apply this to r and s.

- If z is isolated in D, both r and s are adjacent to z, so E has at least two internal edges, impossible.
- Otherwise the isolated vertex of D is u or v. Say it is u. Then both r and s are adjacent to u.

By symmetry, the isolated vertex of E cannot be z. Say it is r. Then both u and v are adjacent to r. But r now has two edges into D, contradicting row closure `e_H(r,D)<=1`.

Hence

> B contains no two disjoint saturated edges.               (6)

## 6. Pure graph-theoretic contradiction

Condition (3) implies every connected component of B is one of:

- a path;
- a cycle;
- the star K1,3;
- an isolated vertex.

Indeed maximum degree is at most3; a degree3 vertex can only meet degree1 vertices, so its component is exactly K1,3, while maximum-degree-two components are paths or cycles.

Equation (2) implies exactly one component is acyclic and every other nontrivial component is a cycle: each tree component contributes one unit to `|V|-|E|`, while a cycle contributes zero.

Every cycle edge is saturated (degree2+degree2=4). Thus:

- a cycle of length at least4 contains two disjoint saturated edges, contradicting (6);
- a 3-cycle itself has only intersecting saturated edges, but if a C3 component exists, the unique acyclic component has at least5 vertices because |V(B)| is8 or10. Such a component must be a path of length at least4 and therefore contains a saturated internal edge disjoint from every C3 edge, again contradicting (6).

Hence B has no cycle.

Then B is one connected tree on 8 or10 vertices. It cannot be K1,3, so it is a path P_n. Any path with n>=6 contains two disjoint internal edges whose endpoint degrees are2+2=4, i.e. two disjoint saturated edges, contradicting (6).

Therefore no such B exists.

## 7. Conclusion

The c=9 high-c single-class state is impossible:

> `c=9` is EMPTY.

Combined with `Q36_F2_2K1_A0_HIGH_C_SINGLE_CLASS_NORMAL_FORM.md`, the only all-d3 / single-class high-c channel not yet eliminated is c=10.