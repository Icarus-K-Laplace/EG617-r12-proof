# E406 d=12 final-rise: full closure

Status: `PROVED EMPTY` under the explicit E406 q30->q31 boundary contract.

Dependencies:

- `E406_D12_MATCHING2_SMALL_COVER.md`;
- near-284 core theorem: every 47-core with 284--286 edges has minimum degree at least12;
- exact q30/q31 subset-charge bounds;
- E406 PAIR-13 and regular-degree restriction.

The previous reduction leaves exactly three matching-two small-cover geometries on the old 12-point missing block S:

1. `K4-e` with cover h-pattern `(2,2,9,10)` and `G_U=0`;
2. `C4` with cover h-pattern `(2,9,2,9)` and `G_U=0`;
3. a paw with `sum_X h=22` and `G_U=0`.

Here X is the four-endpoint cover of a maximum matching and U=S\X consists of eight regular vertices. Every S-vertex has the additional missing edge to y, so its actual shell row weight is `t=1+h`.

The exact cover ledger requires at least five cover-to-U missing edges in every surviving geometry. We show that no such edge can exist.

## 1. A local plateau obstruction

Let z in U be regular and suppose its K_S-neighbourhood N lies in X. Its old shell missing side is

`{y} union N`.

The q30 regular-degree restriction gives `|N|<=2` because z already has the missing edge zy.

PAIR-11 forces every cover endpoint of a z-edge to have large h. In all three residual geometries, the only possibilities are:

- one h=10 cover vertex, giving |N|=1 and a d2 small side;
- two h>=9 cover vertices, giving |N|=2 and a d3 small side.

The subset-charge calculation in each case is at most the d2/d3 baseline, so the repivot has `q_z>=30`. Hence its new 47-core has at most285 edges and therefore minimum degree at least12.

Now inspect the vertices inserted into that new core.

### d2 insertion

The inserted small side is `{y,x}` where x is an h=10 cover vertex. Since y is missing-adjacent to every S-vertex, yx is a target nonedge.

The old row weight of x is

`t_x=1+h_x=11`.

After x enters the new core it gains no internal edge to y and may lose support vertices. Thus its new core degree is at most11, contradicting the minimum-degree12 theorem.

Therefore no d2 plateau edge can occur.

### d3 insertion

The inserted small side is `{y,x1,x2}` with cover h-values at least9. In the residual geometries the internal target edges among this triple are too few to raise every inserted cover vertex to degree12:

- in the `K4-e` residual, the h=9 vertex has old row weight10;
- in the `C4` residual, both h=9 vertices have row weight10 and are mutually target-adjacent, so each reaches at most11;
- in the paw residual, the only possible two-hub configuration contains an h=9 cover vertex of row weight10, while the remaining internal target edges contribute at most one.

Again the new q>=30 core would contain a vertex of degree at most11, contradiction.

Thus no d3 plateau edge can occur.

## 2. K4-e residual

The five-edge residual has cover h-pattern `(2,2,9,10)`.

The two h=2 vertices cannot meet U by PAIR-11. Any U-edge incident with the h=9 vertex must also use the h=10 vertex and hence is a d3 insertion, impossible by Section1. Any U-edge incident only with the h=10 vertex is a d2 insertion, also impossible.

Therefore there are no cover-to-U missing edges.

But the exact ledger requires at least five such edges. Contradiction.

## 3. C4 residual

The four-cycle residual has alternating h-pattern `(2,9,2,9)`.

The h=2 vertices cannot meet U. A regular U-vertex meeting one h=9 vertex must meet the other as well, since PAIR-11 requires `h_z=2`. Hence every cross edge belongs to a d3 insertion with small side `{y,x1,x2}`.

The two h=9 cover vertices have row weight10 and are opposite in the C4, so at most one target edge is available inside the inserted triple. One of them therefore has new core degree at most11. Section1 gives a contradiction.

Hence there are no cross edges, while at least six are required. Contradiction.

## 4. Paw residual

Write the paw cover as triangle A,B,C plus pendant D-A. The edge inequalities and `sum_X h=22` give

`h_A+h_D=11`,
`h_B+h_C=11`.

Any cover-to-U edge must be incident with a vertex of h at least9. If the unique high endpoint has h=10, a U-vertex adjacent only to it gives the forbidden d2 insertion of Section1. If a second h=9 endpoint is present, a U-vertex using both gives the forbidden d3 insertion.

No other cover vertex can meet a regular U-vertex by PAIR-11.

Thus no cover-to-U edge exists, contradicting the exact lower bound on their number.

## 5. Conclusion

All three matching-two small-cover geometries are impossible. Therefore

> **Every d=12 q30->q31 final-rise boundary is impossible.**

Together with the independent closures of d=1,2,3,10,11, all six possible E406 q30->q31 final-rise distance classes are now empty.