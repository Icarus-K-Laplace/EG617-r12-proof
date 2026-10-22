# E406 d=2, e=1 terminal: clean 2-row support reduction

Status: `PROVED` for the reductions below. The `e=1` terminal and E406 remain `OPEN`.

Assume the unique d2 terminal left by `E406_D2_EGE2_CLOSURE.md` and `E406_D2_RETAINED_BLOCK.md`:

- q30 pivot p and q31 pivot y;
- exchanged shell pair S={s1,s2}, a target edge;
- exchanged old-core pair D={d1,d2};
- retained 10-set T;
- `M[T]=K2+8K1`;
- the two endpoints of the unique T-missing edge carry total decoration7;
- all eight T-isolates are undecorated;
- `e(S,D)=0`, and both S vertices have zero excess in the q31 core.

Write

`A=e_R(S,T)`, `B=e_R(D,T)`, `e_D=e_R(D) in {0,1}`.

The retained-block bounds specialize to

`A<=1`,
`B<=2-e_D`.

## 1. At least five clean retained pivots

Among the eight undecorated T-isolates, at most one is incident with an S--T target edge and at most two are incident with a D--T target edge.

Hence at least

`8-1-2=5`

T-isolates are simultaneously target-anticomplete to S and D.

Call them **clean vertices**.

Every clean t is a degree-13 pivot. Its old shell missing neighbourhood is exactly S, so

`d_M(t)=2`.

Let

`U_t=N_C(t)`, `|U_t|=2`.

## 2. q_t is 30 or31

In the old q30 shell the two S-row weights are both11. Therefore for a clean t

`t(S)-e_M(S)=22`.

The exact repivot lower bound gives

`q_t-q_p >= 2*(13-2)-22=0`.

The global E406 core floor gives `q_t<=31`. Thus

`q_t in {30,31}`.

Its new 47-core has 285 or284 edges, so Line-A theorem L4 applies:

`delta(C_t)>=12`.

## 3. U_t is anticomplete to S

The t-core is

`C_t=(C\U_t) union S`.

Each s in S has exactly11 neighbours in the old core C, and S itself is a target edge. Hence in C_t

`d_{C_t}(s)=12-e_R(s,U_t)`.

Minimum degree at least12 forces

`e_R(s,U_t)=0`

for both s. Therefore

`e_R(S,U_t)=0`.      (CLEAN-ANTI)

So every clean 2-row lies completely outside both 11-rows of S.

## 4. Exact q-value from the 2-row type

Put

`r_t=e_C(U_t) in {0,1}`,
`eps_t=sum_{u in U_t}(d_C(u)-12)`.

Using CLEAN-ANTI, exact core-edge exchange gives

`e(C_t)-e(C) = -1-eps_t+r_t`.

Since `q=315-e(core)` in E406,

`q_t-q_p = 1+eps_t-r_t`.

The ceiling `q_t<=31` therefore implies

`eps_t<=r_t`.

Thus exactly three support types are possible:

1. `U_t` is a target nonedge (`r_t=0`) and `eps_t=0`; then `q_t=31`.
2. `U_t` is a target edge (`r_t=1`) and `eps_t=0`; then `q_t=30`.
3. `U_t` is a target edge and `eps_t=1`; then `q_t=31`.

No other 2-row type is compatible with the E406 ceiling.

## 5. If D itself is a target nonedge

When `e_D=0`, the exchange identity gives zero old-core excess on both D vertices. For every clean support U_t, repivoting t retains D in the core and imports S, which is anticomplete to D.

Since the t-core has minimum degree at least12, a degree12 D-vertex cannot lose any neighbour in U_t. Hence

`e_R(D,U_t)=0`

for every clean t.

Thus in the `e_D=0` branch all at-least-five clean supports lie in the common core nonneighbourhood of the independent pair D.

Because `alpha(C)<=4`, that common nonneighbourhood has independence number at most2: an independent triple there together with the independent D-pair would give an independent5-set in C.

This is a strong secondary constraint for the remaining support-compatibility step.

## 6. Current d2 endpoint

The full d2 final-rise class has now collapsed to one terminal only:

- retained block `K2+8K1`;
- two decorated edge endpoints carrying total decoration7;
- at least five clean regular pivots;
- each clean pivot has a 2-row of exactly one of the three types in Section4;
- every clean 2-row is anticomplete to S;
- in the `e_D=0` subbranch, every clean 2-row is also anticomplete to D and lies in a core set of independence number at most2.

The next task is a finite/multipivot compatibility theorem for these at-least-five 2-row supports.