# Canonical State — Exact Three-Anchor Excess workstream

Branch: `workstream/general-r-three-anchor-20261024`

## Contract
Assume `r>=12`, `|V(H)|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`, and three pairwise nonadjacent anchors `a1,a2,a3` with `d_H(ai)=r`. Define `K_r(H)=sum_v(d_H(v)-r)`.

## Verified symbolic partition
Let `Xi` be vertices adjacent to exactly anchor `ai`; let `C` be vertices adjacent to at least two anchors, `c=|C|`; let `t` be the number adjacent to all three anchors. Then:

- every non-anchor meets at least one anchor (else an independent 4-set);
- anchor incidence counting gives `c+t=4`;
- `Xi union {ai}` is a clique, hence `|Xi|<=r-2`;
- with `d_i=(r-2)-|Xi|`, `d_1+d_2+d_3=c-2`;
- therefore `c in {2,3,4}` and, up to permutation, the only deficit patterns are `(0,0,0)`, `(0,0,1)`, `(0,0,2)`, `(0,1,1)`.

No step above uses `r=12`.

## New exact connector-incidence identity
Let `q_i` be the number of connectors not adjacent to anchor `ai`. Since anchor `ai` has exactly `r` neighbours and `|Xi|=r-2-d_i`, it has exactly `2+d_i` connector neighbours. Therefore

`q_i = c-(2+d_i) = (d_1+d_2+d_3)-d_i = d_j+d_k`.

Hence connector types are fixed by the deficit pattern:

- `(0,0,0)`: two triple connectors;
- `(0,0,1)`: one triple connector and pair connectors missing the two zero-deficit anchors;
- `(0,0,2)`: four pair connectors, two missing each zero-deficit anchor, none missing the deficit-2 anchor;
- `(0,1,1)`: four pair connectors with missing-anchor multiplicities `(2,1,1)`.

## Proved general bound
Using the complement and the classical Andrasfai–Erdos–Sos theorem, the target theorem is proved for all `r>=68`: if `K_r<=7`, then the complement `J` is `K4`-free with `Delta(J)=2r-2` and `delta(J)>=2r-9`. Since `|J|=3r-1` and `2r-9 > 5(3r-1)/8` for `r>=68`, AES forces `J` to be 3-partite. A 3-partition of `3r-1` vertices has a part of size at least `r`, contradicting `alpha(J)=omega(H)<=r-1`.

Current theorem status: **PROVED_ANALYTIC for `r>=68`; OPEN for `12<=r<=67`**.

## Active route
Exploit the constant connector skeleton. For each connector `z`, its H-nonneighbours in the three exclusive blocks form a tripartite transversal-cover problem. For a pair connector missing anchor `ak`, the nonneighbour sets in the other two blocks must in fact be complete bipartite in H. Low total excess makes almost every exclusive vertex exact degree and therefore bounded cross-degree; this is the main route to lower the threshold from 68 to 13/12.
