# E407 Q32 — delta=12 depth-2 epsilon_U=0 closure

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL / CLOSED** under the registered 308-edge depth-2 kernel classification. Together with the epsilon_U=1,2,3,4 closures, this closes the entire delta=12 non-four-partite depth-2 branch. E407 Q32 remains OPEN / NOT_CERTIFIED.

## 1. Endpoint degree of d0

At epsilon_U=0 all U-excess vanishes. In the depth-2 kernel,
\[
d_W(d_0)=2-t_0,
\]
where `t0` is the number of the two restored target edges incident with d0.

We first show
\[
\boxed{t_0=0,\qquad d_W(d_0)=2.}
\tag{1.1}
\]

Let `D=N_W(d0)`. If `|D|<=1`, then `H[W\D]` has at least 17 vertices and at most36 edges. A graph on17 vertices with independence number at most3 has at least
\[
p_3(17)=\binom62+\binom62+\binom52=40
\]
edges. Hence `H[W\D]` contains an independent 4-set. It is anticomplete to d0, producing an independent 5-set in H, contradiction.

Therefore `|D|>=2`. Since `d_W(d0)=2-t0<=2`, (1.1) follows.

## 2. The two d0-neighbours force the unique W extremal graph

Now `D=N_W(d0)` has size two. Since d0 may not be extended by an independent four-set of W-nonneighbours,
\[
\alpha(H[W\setminus D])\le3.
\]
Thus
\[
e(H[W\setminus D])\ge p_3(16)
=\binom62+2\binom52=35.
\tag{2.1}
\]

Also
\[
e(H[W])=36.
\tag{2.2}
\]

### Lemma 2.1 — H[W] has minimum degree at least one

If some `w in W` were isolated in H[W], then H[W\{w}] has17 vertices and at most36 edges, below `p_3(17)=40`. It would contain an independent four-set; together with isolated w this gives an independent five-set in H[W], contradicting `alpha(H[W])=4`. Hence every W-vertex has positive W-degree. QED.

The two vertices of D therefore remove at least one W-edge. Consequently
\[
e(H[W\setminus D])\le35.
\]
Together with (2.1), equality holds throughout.

Hence:

1. `H[W\D]` is an extremal 16-vertex graph with independence number at most3 and exactly35 edges, so
   \[
   H[W\setminus D]=K_6\dot\cup K_5\dot\cup K_5;
   \]
2. exactly one W-edge is incident with D;
3. since both vertices of D have positive degree, that unique edge is the edge joining the two D vertices, and neither has any W-neighbour outside D.

Therefore
\[
\boxed{H[W]=K_2\dot\cup K_5\dot\cup K_5\dot\cup K_6,}
\tag{2.3}
\]
and
\[
\boxed{N_W(d_0)=K_2.}
\tag{2.4}

This conclusion was derived without assuming the W complement was four-partite.

## 3. Restored C/E endpoint contradiction

Because t0=0, both restored target edges have J-endpoints in `C union E`. All those points have zero excess, and
\[
d_W(c)=4-t_c.
\tag{3.1}
\]
At least one such point c has `t_c>=1`; hence
\[
d_W(c)\le3.
\tag{3.2}
\]

Apply the component-exhaustion lemma to the q=0 graph (2.3): every `u in U` must be complete to at least one W-component, otherwise one nonneighbour from each of the four components together with u gives an independent five-set.

The only W-component of size at most three is the K2. Thus the point c in (3.2) must be complete to that K2. By (2.4), d0 is also complete exactly to that same K2.

But d0 and c are H-nonadjacent in the classified C5 kernel. Their common W-nonneighbours contain all three components
\[
K_5\dot\cup K_5\dot\cup K_6.
\]
Choosing one vertex from each gives an independent triple. Together with the nonadjacent pair d0,c this produces an independent five-set in H, contradiction.

Therefore
\[
\boxed{
\delta=12,\ \text{non-four-partite depth2},\ \epsilon_U=0
\Longrightarrow\bot.
}
\]

## 4. Consequence for the full depth-2 branch

The workstream now has registered closures for every legal epsilon_U value:

- epsilon_U=0: this theorem;
- epsilon_U=1: `DELTA12_DEPTH2_EPS1_CLOSURE.md`;
- epsilon_U=2: `DELTA12_DEPTH2_EPS2_TERMINAL_CLOSURE.md`;
- epsilon_U=3: `DELTA12_DEPTH2_EPS3_Q0_CLOSURE.md` + `DELTA12_DEPTH2_EPS3_Q1_CLOSURE.md`;
- epsilon_U=4: `DELTA12_DEPTH2_EPS4_TERMINAL_CLOSURE.md`.

Hence
\[
\boxed{\delta=12,\ \text{non-four-partite augmentation depth2}\Longrightarrow\bot}
\]
under the registered 308-edge saturated-kernel classification.

## 5. Dependency and scope audit

The terminal proof uses:

1. the registered depth-2 308-edge kernel classification and its d0/C/E degree formulas;
2. pure graph `alpha(H)<=4` and `alpha(H[W])=4`;
3. elementary Turan extremality for alpha<=3 at n=16,17;
4. the pure component-exhaustion / nonadjacent-pair arguments.

It does not use Didin or the five-template shell system.

This theorem does not close depth3, delta=12 four-partite-U, delta<=11, the five-template compatibility problem, E407 Q32, or EG617(r=12).
