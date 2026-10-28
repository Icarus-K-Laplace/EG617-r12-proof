# E407 Q32 — delta=12 depth-2 epsilon_U=4 terminal closure

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL / CLOSED** under the registered 308-edge depth-2 kernel classification and the preceding endpoint-slack reductions. This closes the entire depth-2 epsilon_U=4 layer; E407 Q32 remains OPEN / NOT_CERTIFIED.

## 1. Remaining aggregate rows

`DELTA12_DEPTH2_EPS4_TWO_PROFILE_REDUCTION.md` leaves exactly
\[
(t_0,\epsilon_{d_0},E_C,E_{rest})
\in\{(0,4,0,0),(1,4,0,0)\}.
\tag{1.1}
\]
Here `t0` is the number of the two restored target edges incident with the unique degree-4 J point `d0`, and `E_C` is the total excess on the four degree-6 J points `C union E`.

For epsilon_U=4 the W graph is exactly
\[
H[W]=K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5
\tag{1.2}
\]
with no W-cross edges.

For a point `c in C union E`, if `t_c` restored edges are incident with c then
\[
d_H(c,W)=4+\epsilon_c-t_c.
\tag{1.3}
\]
In both surviving rows `E_C=0`, so every such c has `epsilon_c=0`.

## 2. Component-exhaustion lemma

### Lemma 2.1

Let `u in U`. If `H[W]` is a disjoint union of four nonempty cliques, then `N_H(u) cap W` contains one whole W-component.

### Proof

Suppose not. Then in each of the four W-components choose a vertex nonadjacent to u. Since there are no edges between distinct W-components, the four chosen vertices form an independent 4-set in H[W]. Together with u they form an independent 5-set in H, contradicting
\[
\alpha(H)\le4.
\]
QED.

For (1.2), every W-component has size at least four. Therefore
\[
\boxed{d_H(u,W)\ge4\quad\text{for every }u\in U.}
\tag{2.1}
\]

This is stronger than the generic delta=12 three-neighbour floor in this q=0 profile.

## 3. Exclude `(0,4,0,0)`

Here `t0=0`. Hence both restored target edges have their J-endpoints in `C union E`.

Their two incidences may be on one point or on two distinct points. In either case there exists `c in C union E` with `t_c>=1`. Since `epsilon_c=0`, (1.3) gives
\[
d_H(c,W)=4-t_c\le3,
\]
contradicting (2.1).

Thus
\[
\boxed{(0,4,0,0)\Longrightarrow\bot.}
\tag{3.1}
\]

## 4. Exclude `(1,4,0,0)`

Here one restored edge is incident with d0. The second restored edge therefore has a J-endpoint `c in C union E`, so `t_c>=1`. Again `epsilon_c=0`, and
\[
d_H(c,W)=4-t_c\le3<4,
\]
contradicting the component-exhaustion lemma.

Hence
\[
\boxed{(1,4,0,0)\Longrightarrow\bot.}
\tag{4.1}
\]

## 5. Conclusion

All epsilon_U=4 depth-2 aggregate profiles have now been excluded:
\[
\boxed{
\delta=12,\ \text{non-four-partite depth2},\ \epsilon_U=4
\Longrightarrow\bot.
}
\]

Together with the earlier epsilon_U=2 and epsilon_U=3 closures, the live depth-2 epsilon frontier is now only
\[
\epsilon_U\in\{0,1\}.
\]

## 6. Dependency audit and scope

The terminal argument itself uses only:

1. the preceding depth-2 reductions establishing the two aggregate rows and the q=0 W profile (1.2);
2. the exact degree formula (1.3);
3. the pure graph bound `alpha(H)<=4`.

It does not use Didin, the five-template shell argument, or any further external extremal theorem. The parent depth-2 model remains conditional on the registered 308-edge saturated-kernel classification.

This theorem does not close depth-2 epsilon_U=0 or 1, depth-3, delta=12 four-partite U, delta<=11, the five-template compatibility problem, E407 Q32, or EG617(r=12).
