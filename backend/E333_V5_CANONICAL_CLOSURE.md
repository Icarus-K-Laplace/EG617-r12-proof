# E333 V5 canonical closure

Status: `PROVED_RELATIVE_TO_CANONICAL_V4`.

This file records the independently replayed V5 result. The new repeated-pair capacity proof is analytic. The upstream legal-backend certification and V4 five-family forcing theorem are retained dependencies and are not recertified here.

## Dependency contract

Assume a hypothetical legal residual `F` has

- 49 vertices and 333 edges;
- `delta(F)=13`;
- `alpha(F)<=4`, `omega(F)<=11`;
- all inherited induced-set caps;
- for every degree-13 pivot, the 35-core has minimum degree at least12 and at least211 edges.

At a maximum `(q,tau)` pivot, the retained low-charge assets and V4 theorem reduce E333 to one of the five necessary repeated-pair families

- `D2-A`, repetition at least8;
- `D2-B`, repetition at least8;
- `D2-C`, repetition at least5;
- `D2-D`, repetition at least7;
- `R9`, repetition9.

These are necessary shell-row families, not realized graphs.

## 1. Repeated-pair core setup

Fix a common missing pair `S={a,b}` with two-point supports `U_i=N_H(x_i)` in one 35-core `H`. Put

`kappa_v=d_H(v)-12`,

`w_v=kappa_v+e_F(v,S)`,

`W=sum_H w_v = K+t_a+t_b`,

where `K=sum_H kappa_v = 2e(H)-420`.

All-pivot core minimum degree gives simultaneous row closure

`e_H(v,U_i)<=w_v` for every `v notin U_i`.

Maximality and exact exchange accounting give the row allowance

`sum_(v in U_i) w_v + delta_i <= a0`,

where `delta_i=1` if the support pair is a target nonedge.

The inherited 13/14-point caps give multiplicity inequalities. In particular for `r=1`, support multiplicity is at most2 and multiplicity-two vertices are pairwise nonadjacent.

## 2. Zero-charge concentration theorem

If `W<=28`, then

`alpha(H[union_i U_i])<=2`.

Reason: among 35 core vertices at least seven have `w=0`. If every zero-charge vertex were in the support union, row closure and `alpha(H)<=3` bound that zero set too strongly. Hence there is a zero-charge vertex outside the union; row closure makes it anticomplete to the entire union. An independent triple inside the union would then create an independent 4-set in H.

This is the key new joint-core theorem. It converts many separate necessary rows into a simultaneous structural object in one actual core.

## 3. Capacity consequences

The V5 analytic capacity theorems imply:

| family regime | required multiplicity | V5 capacity |
|---|---:|---:|
| D2-A | 8 | at most4 |
| D2-C | 5 | at most4 |
| D2-D | 7 | at most6 |
| R9 | 9 | at most6 |

Thus D2-A, D2-C, D2-D and R9 are impossible.

For the remaining allowance-two balanced-hub regime, if at least8 supports survive, the support union is forced to

`K_m + K_m + one perfect matching`,

with disjoint supports and all support vertices of charge1.

This structural conclusion is analytic; it is not inferred from the integer certificate.

## 4. D2-B exact residual ledger

For D2-B,

- `r=1`;
- `(t_a,t_b)=(12,12)`;
- `q=31`;
- `e(H)=211`;
- `K=2`;
- `W=26`;
- `8<=m<=9`.

Let the support union be `U=P sqcup Q`, `|P|=|Q|=m`, with two cliques joined by a perfect matching, so `e_H(U)=m^2`.

Let `Z` be all zero-charge core vertices. Row closure makes `Z` anticomplete to U. There are at least9 such vertices. Since U contains an independent pair and `alpha(H)<=3`, Z must be a clique, with

`9<=t=|Z|<=11`.

Put `B=H\(U union Z)`, `b=35-2m-t`. Exact cut counting gives

`e_H(B)=211+m^2-24m+(t^2-25t)/2-kappa_U`.

Because `alpha(H[B])<=3`, the Caro-Wei/Cauchy lower bound gives

`e_H(B)>=ceil(b(b-3)/6)`.

The complete endpoint table is:

|m|t|b|upper before subtracting kappa_U|lower bound|
|---:|---:|---:|---:|---:|
|8|9|10|11|12|
|8|10|9|8|9|
|8|11|8|6|7|
|9|9|8|4|7|
|9|10|7|1|5|
|9|11|6|-1|3|

Every row contradicts the lower bound even with `kappa_U=0`. Therefore D2-B is impossible.

## 5. E333 conclusion

All five V4 necessary families are impossible under the retained legal-backend/V4 contract. Therefore

> `E333 = EMPTY` relative to that accepted contract.

This does not recertify the upstream V4 forcing theorem or the all-pivot core minimum-degree theorem. It also does not imply any E334+ layer is empty.

## 6. Higher-layer boundary

The V5 capacity theorems are reusable, but E334/E335 are not automatic:

- `W=2e(H)-420+t_a+t_b` must be checked at the actual pivot;
- a 212-edge core has a larger excess budget than a 211-edge core;
- the V4 five-family forcing theorem was an E333 forcing statement, not a q32/q33 theorem.

Thus current status is

- `E333`: `PROVED_RELATIVE_TO_CANONICAL_V4`;
- `E334..E340`: `OPEN`.

## Independent verification

`python -B verify_v5.py` was rerun independently. It passed all 12 balanced-core endpoint inequalities, the r1/r2 multiplicity arithmetic, and capacity thresholds 4/6/7.

Every SHA-256 entry in `MANIFEST.json`, including the retained `HIGH_LAYER_BACKEND_V4.zip`, matched the uploaded package exactly. The verifier certifies the finite arithmetic only; the structural implications above are supplied by the written analytic proof.