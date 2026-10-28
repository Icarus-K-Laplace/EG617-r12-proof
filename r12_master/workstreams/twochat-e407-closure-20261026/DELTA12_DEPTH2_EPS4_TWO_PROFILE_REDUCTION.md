# E407 Q32 — delta=12 depth-2 epsilon_U=4 two-profile reduction

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL strict reduction.** Starting from the four aggregate rows left by `DELTA12_DEPTH2_EPS4_ENDPOINT_SLACK_REDUCTION.md`, two more rows are excluded. Exactly two aggregate rows remain OPEN. E407 Q32 remains OPEN.

## 1. Starting frontier

The previous endpoint-slack theorem reduced epsilon_U=4 to
\[
(t_0,\epsilon_0,E_C,E_{rest})\in
\{(0,3,0,1),(0,3,1,0),(0,4,0,0),(1,4,0,0)\}.
\tag{1.1}
\]
Here `t0` is the number of restored target edges incident with d0, `epsilon0` is the excess at d0, `E_C` is total excess on the four C/E J-points, and `E_rest` is all remaining U-excess.

Throughout
\[
H[W]=K_4^P\dot\cup K_4^Q\dot\cup K_5^R\dot\cup K_5^T
\]
with no W-cross edges.

## 2. Fixed-eight-set lemma when d0 has degree five and some c has degree three

Suppose
\[
d_W(d0)=5
\]
and some c in C union E has
\[
d_W(c)=3.
\]
The pair d0,c is H-nonadjacent and its degree sum is eight. The pair rule therefore forces
\[
N_W(d0)\dot\cup N_W(c)=K_4^P\dot\cup K_4^Q.
\tag{2.1}
\]
Write
\[
x=|N_W(d0)\cap K_4^P|,
\]
so `1<=x<=4`.

Let v be an A/B point nonadjacent to both d0 and c with `d_W(v)<=6`. The pair `(v,c)` cannot use the same two K4s by taking all of `N_W(d0)`: then `(v,d0)` would have union at most six. Therefore `(v,c)` must cover one distinguished K4 and one K5.

The degree-six bound gives x=1 or x=4. By symmetry take x=1. Then

- `N_W(d0)` is one point q of K4^P plus all of K4^Q;
- `N_W(c)=K4^P\{q}`;
- every such v must satisfy
\[
\boxed{N_W(v)=\{q\}\cup K_5^j}
\tag{2.2}
\]
for one of the two K5 components.

Call (2.2) a labelled point. Two labelled points on opposite K7 sides cannot use the same K5: their union would be that K5 plus q, covering only one W-component. Thus labelled cross-K7 pairs have opposite binary labels.

The x=4 case is symmetric.

## 3. Exclude (t0,epsilon0,E_C,Erest)=(0,3,0,1)

Here d0 has degree five. Since E_C=0 and the two restored J-incidences total two, they must hit two distinct C/E points c1,c2; otherwise a double-hit c would have W-degree two, below the universal floor. Hence c1,c2 each have W-degree three, and both give the same fixed-eight-set decomposition (2.1).

### Distinct A/B-side restored endpoints are impossible

If the two restored edges have distinct A/B-side endpoints v1,v2, then each vi is nonadjacent to the other degree-three c-point. At most one of v1,v2 can carry the sole E_rest excess unit. The other has
\[
d_W(v)=5,
\]
but Lemma 2 forces any such nonpartner to have the six-point neighbourhood (2.2). Contradiction.

Therefore both restored edges share one A/B-side endpoint z.

All other thirteen A/B points have restored incidence zero. If the sole E_rest unit is on z or outside A union B, all thirteen are degree-six labelled points. One K7 side then has all seven vertices with one common K5 label, giving K12.

The only remaining possibility places the sole excess unit on another A/B point w and puts z,w on opposite K7 sides, leaving six labelled vertices on each side with opposite K5 labels.

The point w has W-degree seven and is nonadjacent to d0 and to both c1,c2. The c-pair plus d0-pair force w to contain q and one whole K5; the alternative of containing `N_W(d0)` leaves only two spare vertices and cannot complete a second component with d0. Thus w itself has a K5 label.

Crossing w with the six labelled vertices on the opposite K7 side forces w to use its own side's K5 label; otherwise it has the same label as those opposite vertices and violates the pair rule. But then its own side has seven vertices complete to one K5, giving K12. Contradiction.

Hence
\[
\boxed{(0,3,0,1)\text{ is impossible}.}
\tag{3.1}
\]

## 4. Exclude (0,3,1,0)

Again d0 has W-degree five, while all A/B vertices have zero excess.

Among the four C/E points at least one, call it c*, has W-degree three:
- if both restored edges hit one C/E point, that point must carry the unique E_C unit and has degree three;
- if the restored J-endpoints are distinct, at least one endpoint has zero excess and degree three.

Thus Lemma 2 applies to d0,c*.

If some restored edge goes to a different C/E point and has an A/B-side endpoint not also partnered with c*, that endpoint has W-degree five and is nonadjacent to c*, contradicting the six-point forcing (2.2). Therefore either

1. the two restored edges have distinct J-endpoints but share one A/B-side endpoint; or
2. both restored edges hit c*.

In case 1 there is only one exceptional A/B point and the other thirteen are labelled, so one K7 side has seven common K5 labels and gives K12.

In case 2, if the two A/B endpoints coincide the same one-exception argument applies. The only survivor has two distinct c*-partners, one in each K7, leaving six labelled vertices on each side with opposite K5 labels.

Let a0,b0 be these two partners. Each has W-degree five and is nonadjacent to d0. To make its pair with d0 cover two components, such a partner must either

- be complete to a K5, or
- contain the three-set `N_W(c*)` so that together with d0 it completes both K4s.

The K5 option is impossible: taking the opposite-side label violates a cross pair; taking its own-side label makes seven vertices on that K7 complete to a K5 and gives K12. Hence both a0,b0 contain the same three-set `N_W(c*)` and have only two further W-neighbours each.

Their mutual pair is H-nonadjacent. The union contains that common three-set and at most four additional vertices. If the missing fourth point of its K4 is among them, at most three vertices remain, too few to complete any second K4/K5. If it is absent, the first K4 is not complete, while four extra vertices can complete at most one K4. Thus the pair covers at most one W-component, contradiction.

Therefore
\[
\boxed{(0,3,1,0)\text{ is impossible}.}
\tag{4.1}
\]

## 5. Exact remaining epsilon_U=4 frontier

Only
\[
\boxed{(t_0,\epsilon_0,E_C,E_{rest})\in\{(0,4,0,0),(1,4,0,0)\}}
\tag{5.1}
\]
remain.

These two rows are necessary aggregate terminals, not asserted realizations. They are precisely the cases where all four excess units sit on d0 and the d0-C/E pair-cover inequality has positive slack.

## 6. Dependency audit

This reduction uses the registered depth-2 308-edge kernel classification, the delta=12 low-W-degree lemma, exact degree/excess accounting, alpha(H)<=4 / omega(H)<=11, and the nonadjacent-pair common-nonneighbour rule. It does not use Didin.

No claim is made that epsilon_U=4 is closed; the two rows in (5.1) remain OPEN.
